# Cut out an object photographed on a plain WHITE background (product shots).
# Removes the white/pale-grey background connected to the image edge (incl.
# anti-aliased halo and soft floor shadow), strips pale pixels along the
# boundary, de-fringes edge colours. Optional --nofeet trims thin parts
# (e.g. caster wheels) below the main base.
# Usage: python cutout_white.py in.jpg out.png [--nofeet]
import sys, numpy as np, cv2
from PIL import Image
src=np.asarray(Image.open(sys.argv[1]).convert('RGB')).astype(np.int16)
mx=src.max(axis=2); mn=src.min(axis=2)
cand=((mn>185)&((mx-mn)<22)).astype(np.uint8)
n,lab=cv2.connectedComponents(cand,connectivity=4)
border=set(np.unique(np.concatenate([lab[0],lab[-1],lab[:,0],lab[:,-1]])))-{0}
bg=np.isin(lab,list(border)).astype(np.uint8)
fg=cv2.morphologyEx((1-bg).astype(np.uint8),cv2.MORPH_OPEN,np.ones((2,2),np.uint8))
band=cv2.dilate(bg,np.ones((7,7),np.uint8))&fg
fg[(band==1)&(mn>110)&((mx-mn)<30)]=0
fg=cv2.erode(fg,np.ones((2,2),np.uint8))
n,lab2,st,_=cv2.connectedComponentsWithStats(fg,8)
keep=np.zeros_like(fg)
for i in range(1,n):
    if st[i,cv2.CC_STAT_AREA]>40: keep|=(lab2==i).astype(np.uint8)
al=cv2.GaussianBlur(keep.astype(np.float32),(3,3),0)
solid=(al>0.99).astype(np.float32)
bc=cv2.blur(src.astype(np.float32)*solid[...,None],(5,5)); bw=cv2.blur(solid,(5,5))[...,None]
col=np.where((al<0.99)[...,None]&(bw>0.05), bc/np.maximum(bw,1e-3), src)
im=Image.fromarray(np.dstack([col.clip(0,255).astype(np.uint8),(al*255).astype(np.uint8)]),'RGBA')
im=im.crop(im.getbbox())
if im.height<700: im=im.resize((im.width*2,im.height*2),Image.LANCZOS)
if '--nofeet' in sys.argv:
    a=np.asarray(im).copy(); cov=(a[...,3]>128).sum(axis=1); y=len(cov)-1
    while y>0 and cov[y]<0.35*cov.max(): y-=1
    a[y+1:,:,3]=0; im=Image.fromarray(a,'RGBA'); im=im.crop(im.getbbox())
im.save(sys.argv[2]); print('saved',sys.argv[2],im.size)
