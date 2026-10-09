# Normalise a logo to Iconic's standard canvas so it displays at the same
# size as the stock logos (SNES 540x110, N64 540x112): fit, then centre.
# Usage: python norm_logo.py input.png output.png
from PIL import Image
import sys
CANVAS=(540,110)
def normalise(src,dst):
    im=Image.open(src).convert('RGBA'); im=im.crop(im.split()[3].point(lambda v:255 if v>40 else 0).getbbox())
    k=min((CANVAS[0]-10)/im.width, CANVAS[1]/im.height)
    im=im.resize((round(im.width*k),round(im.height*k)),Image.LANCZOS)
    c=Image.new('RGBA',CANVAS); c.alpha_composite(im,((CANVAS[0]-im.width)//2,(CANVAS[1]-im.height)//2)); c.save(dst)
if __name__=='__main__':
    normalise(sys.argv[1],sys.argv[2])
