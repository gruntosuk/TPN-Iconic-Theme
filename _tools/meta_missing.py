import re,glob,html,os
NL=chr(10); TAB=chr(9)
S={}
for f in ['es/es_systems.cfg']+sorted(glob.glob('es/es_systems_*.cfg')):
    t=open(f,encoding='utf-8',errors='ignore').read()
    for b in re.findall(r'<system>(.*?)</system>',t,re.S):
        g=lambda k:(re.search('<%s>(.*?)</%s>'%(k,k),b,re.S) or [None,''])[1].strip()
        S[g('theme') or g('name')]=dict(full=html.unescape(g('fullname')),man=html.unescape(g('manufacturer')),rel=g('release'),hw=g('hardware').lower())
HW={'console':'console','portable':'portable','computer':'computer','arcade':'arcade','port':'port','engine':'engine','emulator':'emulator','os':'os','peripheral':'peripheral','folder':'folder','pc':'computer','handheld':'portable'}
e=lambda s:html.escape(s,quote=False)
n=0
for sysn in [l.split(TAB)[0] for l in open('still_missing.tsv').read().split(NL) if l.strip()]:
    p='iconic-tpn/_inc/metadata/%s.xml'%sysn
    if os.path.exists(p): continue
    i=S.get(sysn,dict(full=sysn,man='',rel='',hw=''))
    yr=i['rel'][:4] if i['rel'][:4].isdigit() else ''
    x=NL.join(['<theme>','  <variables>','    <systemName>%s</systemName>'%e(i['full'] or sysn),'    <systemDescription></systemDescription>','    <systemManufacturer>%s</systemManufacturer>'%e(i['man']),'    <systemReleaseYear>%s</systemReleaseYear>'%yr,'    <systemHardwareType>${i18n.hardware-%s}</systemHardwareType>'%HW.get(i['hw'],'console'),'    <systemCoverSize>3-4</systemCoverSize>','    <systemCartSize>1-1</systemCartSize>','  </variables>','</theme>',''])
    open(p,'w',encoding='utf-8').write(x); n+=1
print('written',n)
