NL=chr(10)
import re,glob,os,shutil,html,sys
sys.path.insert(0,'/tmp'); from tpn_map import M
os.chdir(os.path.expanduser('~/tpn-build'))
T='iconic-tpn/_inc/'
files=['es/es_systems.cfg']+sorted(f for f in glob.glob('es/es_systems_*.cfg'))
S={}
for f in files:
    t=open(f,encoding='utf-8',errors='ignore').read()
    for b in re.findall(r'<system>(.*?)</system>',t,re.S):
        g=lambda k:(re.search('<%s>(.*?)</%s>'%(k,k),b,re.S) or [None,''])[1].strip()
        th=g('theme') or g('name')
        S[th]=dict(full=html.unescape(g('fullname')),man=html.unescape(g('manufacturer')),rel=g('release'),hw=g('hardware'))
HW={'console':'console','portable':'portable','computer':'computer','arcade':'arcade','port':'port','engine':'engine','emulator':'emulator','os':'os','peripheral':'peripheral','folder':'folder','pc':'computer','handheld':'portable'}
def esc(s): return html.escape(s,quote=False)
done=[];bad=[]
for tgt,(src,kind) in sorted(M.items()):
    if kind=='skip': continue
    if not os.path.exists(T+'backgrounds/%s.webp'%src): bad.append((tgt,src)); continue
    info=S.get(tgt,dict(full=tgt,man='',rel='',hw=''))
    dirs=['backgrounds','overlays'] + (['logos','logos-svg','controllers'] if kind=='variant' else [])
    for d in dirs:
        for ext in ('webp','svg','png'):
            p=T+'%s/%s.%s'%(d,src,ext)
            if os.path.exists(p): shutil.copyfile(p,T+'%s/%s.%s'%(d,tgt,ext))
    if kind=='variant' and os.path.exists(T+'metadata/%s.xml'%src):
        x=open(T+'metadata/%s.xml'%src,encoding='utf-8').read()
        x=re.sub(r'<systemName>.*?</systemName>','<systemName>%s</systemName>'%esc(info['full'] or tgt),x,count=1)
    else:
        hw=HW.get(info['hw'].lower(),'console')
        yr=info['rel'][:4] if info['rel'][:4].isdigit() else ''
        x=NL.join(['<theme>', '  <variables>', '    <systemName>%s</systemName>', '    <systemDescription></systemDescription>', '    <systemManufacturer>%s</systemManufacturer>', '    <systemReleaseYear>%s</systemReleaseYear>', '    <systemHardwareType>${i18n.hardware-%s}</systemHardwareType>', '    <systemCoverSize>3-4</systemCoverSize>', '    <systemCartSize>1-1</systemCartSize>', '  </variables>', '</theme>', ''])%(esc(info['full'] or tgt),esc(info['man'] or ''),yr,hw)
    open(T+'metadata/%s.xml'%tgt,'w',encoding='utf-8').write(x)
    done.append(tgt)
have=set(os.path.splitext(x)[0] for x in os.listdir(T+'backgrounds'))
still=sorted((k,v['full']) for k,v in S.items() if k not in have)
print('mapped',len(done),'bad',bad)
print('still_missing',len(still))
open('still_missing.tsv','w').write(NL.join('%s\t%s'%s for s in still))#
print('; '.join('%s=%s'%s for s in still))
