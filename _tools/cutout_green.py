# Cut out an object on a solid bright GREEN background (Gemini cabinet renders).
# Removes only green connected to the image edge, so green parts of the object
# (buttons, stripes) stay solid; soft edges; removes green spill along the outline only.
# Usage: python cutout_green.py in.png out.png
import sys, numpy as np, cv2
from PIL import Image
a=np.asarray(Image.open(sys.argv[1]).convert('RGB')).astype(np.float32)
# trim solid dark letterbox/pillarbox bars (Gemini pads portrait images onto a landscape canvas)
dark=(a.max(axis=2)<40)
rows=np.where(dark.mean(axis=1)<0.98)[0]; cols=np.where(dark.mean(axis=0)<0.98)[0]
if len(rows) and len(cols): a=a[rows.min():rows.max()+1, cols.min():cols.max()+1]
r,g,b=a[...,0],a[...,1],a[...,2]
bgk=np.clip(((g-np.maximum(r,b))-40)/60,0,1)
n,lab=cv2.connectedComponents((bgk>0.5).astype(np.uint8),connectivity=4)
border=set(np.unique(np.concatenate([lab[0],lab[-1],lab[:,0],lab[:,-1]])))-{0}
outside=np.isin(lab,list(border))
near=cv2.dilate(outside.astype(np.uint8),np.ones((5,5),np.uint8)).astype(bool)
alpha=np.where(near,1-bgk,1.0); alpha[outside]=0
alpha=cv2.GaussianBlur(alpha.astype(np.float32),(3,3),0)
n2,lab2,st,_=cv2.connectedComponentsWithStats((alpha>0.5).astype(np.uint8),8)
i=1+int(np.argmax(st[1:,cv2.CC_STAT_AREA])); alpha*=cv2.dilate((lab2==i).astype(np.uint8),np.ones((3,3),np.uint8))
# contaminated edge: within ~20px of the background, pixels that are yellow-green/olive
# (green close to or above the strongest other channel, blue well below green) are green spill
near20=cv2.dilate(outside.astype(np.uint8),np.ones((41,41),np.uint8)).astype(bool)&(~outside)
olive=near20&(g>np.maximum(r,b)-12)&(b<0.72*g)
alpha[olive]=0
alpha=cv2.GaussianBlur(alpha.astype(np.float32),(3,3),0)
n3,lab3,st3,_=cv2.connectedComponentsWithStats((alpha>0.5).astype(np.uint8),8)
i3=1+int(np.argmax(st3[1:,cv2.CC_STAT_AREA])); alpha*=cv2.dilate((lab3==i3).astype(np.uint8),np.ones((3,3),np.uint8))
band=cv2.dilate(outside.astype(np.uint8),np.ones((9,9),np.uint8)).astype(bool)&(~outside)
# trim the outermost pixel of the outline and fully neutralise green on the edge (15px band)
alpha=cv2.erode(alpha.astype(np.float32),np.ones((3,3),np.uint8))
band=cv2.dilate(outside.astype(np.uint8),np.ones((31,31),np.uint8)).astype(bool)&(~outside)
g2=g.copy(); lim=np.maximum(r,b); g2[band]=np.minimum(g[band],lim[band])
im=Image.fromarray(np.dstack([np.dstack([r,g2,b]).clip(0,255).astype(np.uint8),(alpha*255).astype(np.uint8)]),'RGBA')
im=im.crop(im.getbbox()); im.save(sys.argv[2]); print('saved',sys.argv[2],im.size)
