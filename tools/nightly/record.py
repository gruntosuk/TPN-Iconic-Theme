import os,re,shutil,subprocess,sys,json,datetime
os.chdir(os.path.expanduser('~/mnt/tpn-build'))
data=json.load(open('work/nightly/systems.json'))
done=json.load(open('work/nightly/recorded.json')) if os.path.exists('work/nightly/recorded.json') else []
today='2026-10-09'
nas=os.path.expanduser('~/mnt/Emulation/TPN Iconic Theme')
for code,d in data.items():
    if code in done: continue
    sd='sources/%s'%code; os.makedirs(sd,exist_ok=True)
    for src,dst in d['sources']:
        if os.path.exists(src):
            shutil.copy2(src,os.path.join(sd,dst))
            if src.startswith('incoming/'): os.remove(src) if False else None
    # logs
    open('salvage_log.tsv','a').write('%s\t%s\tcustom\tgemini\n'%(code,d['name']))
    open('controllers_log.tsv','a').write('%s\t%s\n'%(code,d['ctl']))
    pm=open('iconic-tpn/PROMPTS.md').read(); line='- %s %s - %s\n'%(today,code,d['prompt']); mk='\n\n## Arcade three-cabinet groups'
    pm=pm.replace(mk,'\n'+line.rstrip('\n')+mk,1) if mk in pm else pm+line
    open('iconic-tpn/PROMPTS.md','w').write(pm)
    open('iconic-tpn/CREDITS-TPN.md','a').write('- %s: %s\n'%(d['name'],d['credit']))
    s=open('make_todo.py').read()
    s=s.replace('custom={','custom={%s:%s,'%(json.dumps(code),json.dumps(d['todo'])),1)
    open('make_todo.py','w').write(s)
    done.append(code)
json.dump(done,open('work/nightly/recorded.json','w'))
