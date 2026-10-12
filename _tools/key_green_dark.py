import cv2,numpy as np,sys
src,out,view=sys.argv[1:4]
im=cv2.imread(src).astype(np.int32)
B,G,R=im[:,:,0],im[:,:,1],im[:,:,2]
gd=G-np.maximum(R,B)
bg=(gd>18).astype(np.uint8)*255
# only background connected to border
n,lab=cv2.connectedComponents(bg)
border=set(lab[0,:])|set(lab[-1,:])|set(lab[:,0])|set(lab[:,-1]);border.discard(0)
bgm=np.isin(lab,list(border)).astype(np.uint8)*255
fg=255-bgm
k=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
fg=cv2.morphologyEx(fg,cv2.MORPH_OPEN,k)
n,lab,st,_=cv2.connectedComponentsWithStats(fg)
big=1+np.argmax(st[1:,4]);fg=(lab==big).astype(np.uint8)*255
fg=cv2.erode(fg,np.ones((3,3),np.uint8))
a=cv2.GaussianBlur(fg,(0,0),1.0)
rgb=cv2.imread(src)
# despill: clamp G
r=rgb.astype(np.int32);m=np.maximum(r[:,:,2],r[:,:,0]);r[:,:,1]=np.minimum(r[:,:,1],m+4)
rgba=np.dstack([r.clip(0,255).astype(np.uint8),a])
ys,xs=np.where(a>10);rgba=rgba[ys.min():ys.max()+1,xs.min():xs.max()+1]
cv2.imwrite(out,rgba)
al=rgba[:,:,3:4]/255.;bgc=np.full(rgba.shape[:2]+(3,),200,np.float32)
cv2.imwrite(view,(rgba[:,:,:3]*al+bgc*(1-al)).astype(np.uint8))
