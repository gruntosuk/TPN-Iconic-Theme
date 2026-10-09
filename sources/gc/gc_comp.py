import cv2,numpy as np,sys
from PIL import Image,ImageFilter
sc=float(sys.argv[1]); cx=int(sys.argv[2]); fy=int(sys.argv[3]); out=sys.argv[4]
im=cv2.imread('gc_re4_leon_zoomout_raw.jpeg'); m=cv2.imread('gc_leon_mask2.png',0)
ox,oy=906,160
poly=np.array([[50,0],[240,0],[240,150],[218,150],[218,285],[196,300],[194,515],[84,515],[84,300],[76,260],[52,240],[50,100]])+[ox,oy]
pm=np.zeros_like(m); cv2.fillPoly(pm,[poly.astype(np.int32)],255); m=cv2.bitwise_and(m,pm)
# legs: keep only dark trouser/boot pixels below the hip to drop teal/mud gaps
V=im.max(axis=2)
leg=np.zeros_like(m); leg[470:,:]=255
thr=np.where(np.arange(im.shape[0])[:,None]<600,45,62)
dark=((V<thr)*255).astype(np.uint8)
dark=cv2.morphologyEx(dark,cv2.MORPH_CLOSE,np.ones((7,7),np.uint8))
legm=cv2.bitwise_and(m,dark)
legm=cv2.morphologyEx(legm,cv2.MORPH_CLOSE,np.ones((15,15),np.uint8))
ff=legm.copy(); h2,w2=ff.shape; msk=np.zeros((h2+2,w2+2),np.uint8)
cv2.floodFill(ff,msk,(0,0),255)
legm=legm|cv2.bitwise_not(ff)
legm=cv2.bitwise_and(legm,m)
m=np.where(leg>0,legm,m).astype(np.uint8)
m=cv2.morphologyEx(m,cv2.MORPH_OPEN,np.ones((3,3),np.uint8))
n,lab,st,_=cv2.connectedComponentsWithStats(m); k=1+np.argmax(st[1:,4]); m=((lab==k)*255).astype(np.uint8)
ys,xs=np.where(m>0); x0,x1,y0,y1=xs.min(),xs.max(),ys.min(),ys.max()
leon=im[y0:y1+1,x0:x1+1]; lm=m[y0:y1+1,x0:x1+1]
lm=cv2.GaussianBlur(lm,(0,0),0.9)
nw,nh=int(leon.shape[1]*sc),int(leon.shape[0]*sc)
leon=cv2.resize(leon,(nw,nh),interpolation=cv2.INTER_LANCZOS4); lm=cv2.resize(lm,(nw,nh))
bg=cv2.imread('gc_clean_zoomout_raw.jpeg'); bg=cv2.resize(bg,(1365,768)).astype(np.float32)
px=cx-nw//2; py=fy-nh
# contact shadow
sh=np.zeros((768,1365),np.float32)
cv2.ellipse(sh,(cx+10,fy-4),(int(nw*0.42),int(14*sc)),0,0,360,1,-1)
sh=cv2.GaussianBlur(sh,(0,0),12)
bg*= (1-0.55*sh)[...,None]
a=(lm/255.0)[...,None]
Y0,Y1=max(py,0),min(py+nh,768); X0,X1=max(px,0),min(px+nw,1365)
roi=bg[Y0:Y1,X0:X1]; l=leon[Y0-py:Y1-py,X0-px:X1-px].astype(np.float32); aa=a[Y0-py:Y1-py,X0-px:X1-px]
bg[Y0:Y1,X0:X1]=roi*(1-aa)+l*aa
cv2.imwrite(out,np.clip(bg,0,255).astype(np.uint8)); print(nw,nh,px,py)
