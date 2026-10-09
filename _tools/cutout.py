# Cut an object (e.g. an arcade cabinet) out of its background for the
# system-image slot. Usage: python cutout.py input.jpg output.png
import sys, numpy as np
from PIL import Image
from rembg import remove, new_session
src=Image.open(sys.argv[1]).convert('RGB')
out=remove(src,session=new_session('isnet-general-use'))
a=np.asarray(out).copy(); al=a[...,3].astype(float)
al[al<70]=0; al=np.clip((al-70)/185*255,0,255)   # drop faint shadows, firm edges
a[...,3]=al.astype(np.uint8)
im=Image.fromarray(a,'RGBA'); im=im.crop(im.getbbox())
if im.height<700: k=2; im=im.resize((im.width*k,im.height*k),Image.LANCZOS)
im.save(sys.argv[2]); print('saved',sys.argv[2],im.size)
