import re,os
from PIL import Image, ImageDraw, ImageFont
T='iconic-tpn/'; I=T+'_inc/'
W,H=1920,1080
lang=open(I+'ui-components/theme-lang.xml',encoding='utf-8').read()
en=lang.split('<variables lang')[0]
def i18n(s):
    return re.sub(r'\$\{(i18n\.[a-z-]+)\}',lambda m:(re.search('<%s>(.*?)</%s>'%(m.group(1),m.group(1)),en) or [0,''])[1],s)
def meta(sys):
    x=open(I+'metadata/%s.xml'%sys,encoding='utf-8').read().split('<variables lang')[0]
    g=lambda k:i18n((re.search('<%s>(.*?)</%s>'%(k,k),x,re.S) or [0,''])[1].strip())
    return g('systemName'),g('systemManufacturer'),g('systemReleaseYear'),g('systemHardwareType'),g('systemDescription')
F=lambda f,s:ImageFont.truetype(I+'fonts/'+f,s)
order=sorted(os.path.splitext(f)[0] for f in os.listdir(I+'metadata') if not f.startswith('_'))
def logo_img(sys,w,h,alpha):
    p=I+'logos/%s.webp'%sys
    if os.path.exists(p):
        im=Image.open(p).convert('RGBA'); r=min(w/im.width,h/im.height); im=im.resize((int(im.width*r),int(im.height*r)),Image.LANCZOS)
    else:
        name=meta(sys)[0].upper(); f=F('ChangaOne-Italic.ttf',int(0.036*H)); d=ImageDraw.Draw(Image.new('RGBA',(1,1)))
        bb=d.textbbox((0,0),name,font=f); im=Image.new('RGBA',(bb[2]+10,bb[3]+10)); ImageDraw.Draw(im).text((5,5),name,font=f,fill=(17,17,17,255),stroke_width=2,stroke_fill=(250,250,250,255))
        r=min(1,w/im.width); im=im.resize((int(im.width*r),int(im.height*r)))
    if alpha<1:
        a=im.split()[3].point(lambda v:int(v*alpha)); im.putalpha(a)
    return im
def center_text(d,y,txt,font,color,maxw):
    while d.textlength(txt,font=font)>maxw and len(txt)>3: txt=txt[:-2]
    d.text((W*0.25,y),txt,font=font,fill=color,anchor='mm')
def render(sys,games,out):
    bg=Image.open(I+'backgrounds/%s.webp'%sys).convert('RGBA').resize((W,H))
    ov=I+'overlays/%s.webp'%sys
    bg.alpha_composite(Image.open(I+'other/system-info-panel-dark.png').convert('RGBA'))
    c=I+'controllers/%s.webp'%sys
    c=c if os.path.exists(c) else I+'controllers/_default.webp'
    ci=Image.open(c).convert('RGBA'); r=min(0.225*W/ci.width,0.351*H/ci.height); ci=ci.resize((int(ci.width*r),int(ci.height*r)),Image.LANCZOS)
    bg.alpha_composite(ci,(int(0.25*W-ci.width/2),int(0.21*H-ci.height/2)))
    if os.path.exists(ov): bg.alpha_composite(Image.open(ov).convert('RGBA').resize((W,H)))
    d=ImageDraw.Draw(bg)
    name,man,yr,hw,desc=meta(sys)
    center_text(d,0.454*H,name.upper(),F('Gilroy-Bold.ttf',40),'#cccccc',0.26*W)
    center_text(d,0.486*H,man.upper(),F('Gilroy-Bold.ttf',21),'#adadad',0.26*W)
    center_text(d,0.523*H,(yr+' · '+hw if yr else hw).upper(),F('Gilroy-Bold.ttf',26),'#cccccc',0.26*W)
    center_text(d,0.585*H,'%d GAMES'%games,F('Gilroy-Bold.ttf',26),'#a0a0a0',0.26*W)
    f=F('Oxygen-Regular.ttf',26); words=desc.split(); lines=[]; cur=''
    for wd in words:
        t=(cur+' '+wd).strip()
        if d.textlength(t,font=f)>0.23*W: lines.append(cur); cur=wd
        else: cur=t
    if cur: lines.append(cur)
    for i,l in enumerate(lines[:6]): d.text((W*0.25,0.605*H+i*32),l,font=f,fill='#cccccc',anchor='ma')
    k=order.index(sys)
    for off in (-1,0,1,2,3):
        s=order[(k+off)%len(order)]; sel=off==0
        im=logo_img(s,int(W*0.13*(1.5 if sel else 1)),int(H*0.09*(1.5 if sel else 1)),1 if sel else 0.5)
        cx=W*(0.25+0.25*off); bg.alpha_composite(im,(int(cx-im.width/2),int(0.85*H-im.height/2)))
    bg.alpha_composite(Image.open(I+'other/bottom-bar-dark.png').convert('RGBA'))
    bg.convert('RGB').save(out,quality=92)
os.makedirs('mockups',exist_ok=True)
for s,g in [('pegasus',3),('mpu1000',3),('myvision',3)]:
    render(s,g,'mockups/%s.jpg'%s)
print('done')
