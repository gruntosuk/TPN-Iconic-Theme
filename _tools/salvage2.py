import os
from PIL import Image, ImageDraw
NL=chr(10); TAB=chr(9)
CK='/Volumes/stuff/Emulation/TPN Iconic Theme/Retrobat/.emulationstation/themes/ckau-book-PixN/_inc/'
OUT='iconic-tpn/_inc/'
base=Image.open(OUT+'backgrounds/_default.webp').convert('RGBA').resize((1920,1080))
log=[l.split(TAB) for l in open('salvage_log.tsv').read().split(NL)]
new=[]
for row in log:
    name=row[0]
    if row[2]!='none': continue
    a=CK+'arts/'+name+'.png'
    if not os.path.exists(a): continue
    bg=base.copy(); art=Image.open(a).convert('RGBA')
    r=1000/art.height; art=art.resize((int(art.width*r),1000),Image.LANCZOS)
    bg.alpha_composite(art,(1920-art.width-60,40))
    bg.convert('RGB').save(OUT+'backgrounds/'+name+'.webp','WEBP',quality=88)
    row[2]='ckau-art'; new.append((name,bg.convert('RGB').resize((320,180))))
open('salvage_log.tsv','w').write(NL.join(TAB.join(r) for r in log))
sheet=Image.open('salvage_preview.jpg'); cols=4
allrows=(len(new)+cols-1)//cols
s2=Image.new('RGB',(sheet.width,sheet.height+allrows*215),(30,30,30)); s2.paste(sheet,(0,0)); d=ImageDraw.Draw(s2)
for i,(n,t) in enumerate(new):
    x=(i%cols)*330+5; y=sheet.height+(i//cols)*215+5; s2.paste(t,(x,y)); d.text((x,y+183),'%s (ckau-art)'%n,fill=(255,255,255))
s2.save('salvage_preview.jpg',quality=80)
print('added',len(new)); print([r[0] for r in log if r[2]=='none'])
