# Hypermax background layer + its standalone character (char.png, no frame),
# with the character placed centre-right like Iconic's hero art.
# Usage: python hy_char_bg.py <hypermax system folder> out.webp
import sys, os
from PIL import Image, ImageFilter
d=sys.argv[1].rstrip('/')+'/'
W,H=1920,1080
bg=Image.open(d+'_inc/background.png').convert('RGBA').resize((W,H))
c=Image.open(d+'char.png').convert('RGBA'); c=c.crop(c.getbbox())
k=min(860/c.height, 900/c.width, 2.4)          # target ~80% of screen height, cap upscaling
c=c.resize((int(c.width*k),int(c.height*k)),Image.LANCZOS)
cx=int(W*0.68); bottom=int(H*0.97)
x=max(int(W*0.40),min(cx-c.width//2,W-c.width-20)); y=bottom-c.height
sh=Image.new('RGBA',c.size,(0,0,0,0)); sh.putalpha(c.split()[3].point(lambda v:int(v*0.45)))
sh=sh.filter(ImageFilter.GaussianBlur(18))
bg.alpha_composite(sh,(x+14,y+10)); bg.alpha_composite(c,(x,y))
bg.convert('RGB').save(sys.argv[2],'WEBP',quality=88); print('saved',sys.argv[2],'char scale %.2f'%k)
