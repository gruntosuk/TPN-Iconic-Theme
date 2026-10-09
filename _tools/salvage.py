import os, html
from PIL import Image, ImageDraw
NL=chr(10); TAB=chr(9)
TH='/Volumes/stuff/Emulation/TPN Iconic Theme/Retrobat/.emulationstation/themes/'
HY=TH+'Hypermax-Plus-PixN/'; CK=TH+'ckau-book-PixN/_inc/'
OUT='iconic-tpn/_inc/'
miss=[l.split(TAB) for l in open('still_missing.tsv').read().split(NL) if l.strip()]
log=[]; thumbs=[]
def fit(im,w,h):
    r=min(w/im.width,h/im.height); return im.resize((max(1,int(im.width*r)),max(1,int(im.height*r))),Image.LANCZOS)
for name,full in miss:
    src=None; bg=None
    hb=HY+name+'/_inc/background.png'
    if os.path.exists(hb):
        bg=Image.open(hb).convert('RGBA').resize((1920,1080))
        hc=HY+name+'/_inc/character.png'
        if os.path.exists(hc):
            bg.alpha_composite(Image.open(hc).convert('RGBA').resize((1920,1080)))
        src='hypermax'
    else:
        cb=CK+'backgrounds/unified/'+name+'.png'
        if os.path.exists(cb):
            bg=Image.open(cb).convert('RGBA').resize((1920,1080),Image.LANCZOS)
            cc=CK+'consoles/'+name+'.png'
            if os.path.exists(cc):
                c=fit(Image.open(cc).convert('RGBA'),900,560)
                bg.alpha_composite(c,(1920-c.width-120,(1080-c.height)//2+60))
            src='ckau'
    if bg is not None:
        bg.convert('RGB').save(OUT+'backgrounds/'+name+'.webp','WEBP',quality=88)
        t=bg.convert('RGB').resize((320,180)); thumbs.append((name,full,src,t))
    lp='/tmp/ql/'+name+'.svg.png'; lg='none'
    if os.path.exists(lp):
        im=Image.open(lp).convert('RGBA'); bb=im.getbbox()
        if bb:
            im=fit(im.crop(bb),540,160); im.save(OUT+'logos/'+name+'.webp','WEBP',quality=92,lossless=False); lg='ckau'
    log.append(TAB.join([name,full,src or 'none',lg]))
open('salvage_log.tsv','w').write(NL.join(log))
# contact sheet
cols=4; rows=(len(thumbs)+cols-1)//cols
sheet=Image.new('RGB',(cols*330,rows*215),(30,30,30)); d=ImageDraw.Draw(sheet)
for i,(n,f,s,t) in enumerate(thumbs):
    x=(i%cols)*330+5; y=(i//cols)*215+5; sheet.paste(t,(x,y)); d.text((x,y+183),'%s (%s)'%(n,s),fill=(255,255,255))
sheet.save('salvage_preview.jpg',quality=80)
print('bg',len(thumbs),'logos',sum(1 for l in log if l.endswith('ckau')))
print([l for l in log if 'none' in l])
