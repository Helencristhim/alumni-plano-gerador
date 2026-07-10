import json, re, unicodedata, sys, os
from collections import defaultdict
HERE=os.path.dirname(os.path.abspath(__file__))
def snake(t,m=48):
    t=unicodedata.normalize('NFKD',t).encode('ascii','ignore').decode()
    t=re.sub(r"[^a-z0-9]+","_",t.lower()).strip('_'); return t[:m].rstrip('_')
def extract(html):
    out=[]
    for line in html.split('\n'):
        for mm in re.finditer(r"speakText\('((?:[^'\\]|\\.)*)'",line):
            t=mm.group(1).replace("\\'","'")
            if not t.startswith('['): out.append(t)
        for mm in re.finditer(r'data-phrase="([^"]*)"',line): out.append(mm.group(1))
    return out
cfg=json.load(open(os.path.join(HERE,'config.json'),encoding='utf-8'))
slides=open(os.path.join(HERE,'slides.html'),encoding='utf-8').read()
preclass=open(os.path.join(HERE,'preclass.html'),encoding='utf-8').read()
n=cfg['lesson']['n']
buckets=defaultdict(dict); collisions=[]
def check(prefix,text):
    k=snake(text)
    if k in buckets[prefix] and buckets[prefix][k]!=text:
        collisions.append((prefix,k,buckets[prefix][k],text))
    buckets[prefix][k]=text
sl=[]; seen=set()
for t in extract(slides):
    if t not in seen: seen.add(t); sl.append(t); check(f'a{n}_',t)
pc=[]; seenp=set()
for t in extract(preclass):
    if t not in seenp: seenp.add(t); pc.append(t); check(f'pc{n}_',t)
# listenings have explicit filenames; ensure unique
lf=[li['file'] for li in cfg['lesson'].get('listenings',[])]
print(f'distinct slides={len(sl)} preclass={len(pc)} listenings={len(lf)} listen_files_unique={len(set(lf))==len(lf)}')
if collisions:
    print('COLLISIONS:')
    for p,k,a,b in collisions: print(f'  [{p}{k}] A="{a}" B="{b}"')
    sys.exit(1)
print('OK: no snake[:48] collisions in any prefix bucket.')
