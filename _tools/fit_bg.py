# Scale and centre-crop an image to exactly 1920x1080 for a background.
# Usage: python fit_bg.py input.jpg output.webp
import sys
from PIL import Image
W,H=1920,1080
im=Image.open(sys.argv[1]).convert('RGB'); s=max(W/im.width,H/im.height)
im=im.resize((round(im.width*s),round(im.height*s)),Image.LANCZOS)
x=(im.width-W)//2; y=(im.height-H)//2; im=im.crop((x,y,x+W,y+H))
im.save(sys.argv[2],quality=90); print('saved',sys.argv[2])
