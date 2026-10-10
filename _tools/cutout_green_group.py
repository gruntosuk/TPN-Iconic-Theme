# Like cutout_green.py but for a GROUP of cabinets that Gemini drew with thin green gaps between them:
# keeps every large component and bridges gaps narrower than --gap px (default 70) with a dark fill.
# Usage: python cutout_green_group.py in.jpg out.png [--gap 70]
import sys, numpy as np, cv2
from PIL import Image
gap=int(sys.argv[sys.argv.index('--gap')+1]) if '--gap' in sys.argv else 70
a=np.asarray(Image.open(sys.argv[1]).convert('RGB')).astype(np.float32)
r,g,b=a[...,0],a[...,1],a[...,2]
bgk=np.clip(((g-np.maximum(r,b))-40)/60,0,1)
n,lab=cv2.connectedComponents((bgk>0.5).astype(np.uint8),connectivity=4)
border=set(np.unique(np.concatenate([lab[0],lab[-1],lab[:,0],lab[:,-1]])))-{0}
outside=np.isin(lab,list(border))
alpha=(~outside).astype(np.float32)
# keep large components only
n2,lab2,st,_=cv2.connectedComponentsWithStats((alpha>0.5).astype(np.uint8),8)
keep=np.zeros_like(alpha)
big=st[1:,cv2.CC_STAT_AREA].max()
for i in range(1,n2):
    if st[i,cv2.CC_STAT_AREA]>0.05*big: keep[lab2==i]=1
alpha=keep
# bridge horizontal gaps with dark fill
closed=cv2.morphologyEx(alpha.astype(np.uint8),cv2.MORPH_CLOSE,cv2.getStructuringElement(cv2.MORPH_RECT,(gap,1)))
fill=(closed>0)&(alpha==0)
rgb=np.dstack([r,g,b]).copy(); rgb[fill]=(16,16,20)
alpha=closed.astype(np.float32)
# neutralise green spill on the outline
near=cv2.dilate(outside.astype(np.uint8),np.ones((9,9),np.uint8)).astype(bool)&(alpha>0)
lim=np.maximum(rgb[...,0],rgb[...,2]); rgb[...,1][near]=np.minimum(rgb[...,1][near],lim[near])
alpha=cv2.erode(alpha,np.ones((3,3),np.uint8)); alpha=cv2.GaussianBlur(alpha,(3,3),0)
im=Image.fromarray(np.dstack([rgb.clip(0,255).astype(np.uint8),(alpha*255).astype(np.uint8)]),'RGBA')
im=im.crop(im.getbbox()); im.save(sys.argv[2]); print('saved',sys.argv[2],im.size)
