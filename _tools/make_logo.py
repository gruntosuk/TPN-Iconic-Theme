# Turn a transparent logo into an Iconic-style logo: white sticker border,
# then placed centred on the standard 540x110 canvas (same as SNES/N64).
# Usage: python make_logo.py input.png output.webp
import sys
from PIL import Image, ImageFilter
from norm_logo import normalise
im=Image.open(sys.argv[1]).convert('RGBA'); im.putalpha(im.split()[3].point(lambda v:0 if v<=40 else v)); im=im.crop(im.getbbox())
if im.width<1000: k=1000/im.width; im=im.resize((round(im.width*k),round(im.height*k)),Image.LANCZOS)
pad=30; b=Image.new('RGBA',(im.width+2*pad,im.height+2*pad)); b.alpha_composite(im,(pad,pad))
al=b.split()[3].point(lambda v:255 if v>40 else 0).filter(ImageFilter.MaxFilter(25)).filter(ImageFilter.GaussianBlur(2))
s=Image.new('RGBA',b.size,(255,255,255,255)); s.putalpha(al); s.alpha_composite(b); s=s.crop(s.split()[3].point(lambda v:255 if v>40 else 0).getbbox())
tmp='/tmp/_logo_sticker.png'; s.save(tmp); normalise(tmp,sys.argv[2]); print('saved',sys.argv[2])
