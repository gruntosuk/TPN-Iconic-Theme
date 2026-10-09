import sys,re,os
os.chdir(os.path.expanduser('~/mnt/tpn-build'))
src=open('mockup.py').read()
src=re.sub(r"for s,g in \[.*?\]:",  "for s,g in [%s]:"%",".join("('%s',3)"%a for a in sys.argv[1:]), src)
src=src.replace('lines[:6]','lines[:%s]'%os.environ.get('MAXLINES','6'))
exec(compile(src,'mockup.py','exec'))
