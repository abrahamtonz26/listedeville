"""Regenerate assets/new-york.json from tools/new-york.md.
Usage (from the repo root):  python3 tools/build-data.py
Edit the markdown list, run this, commit — the site updates."""
import re, json, sys, urllib.parse, os
here=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,here)
from platforms import lookup
import unicodedata
OCC={}
def norm(x):
    x=unicodedata.normalize('NFKD',x).encode('ascii','ignore').decode().lower(); return re.sub(r'[^a-z0-9]','',x)
SLUG=sys.argv[1] if len(sys.argv)>1 else 'new-york'
_ocf=os.path.join(here,'occasions.json' if SLUG=='new-york' else f'occasions-{SLUG}.json')
OCC=json.load(open(_ocf,encoding='utf-8')) if os.path.exists(_ocf) else {}
src=open(os.path.join(here,SLUG+'.md'),encoding='utf-8').read().split('\n')
SHORT={"Off-beat & only-in-Houston":"Off-beat","Off-beat & only-in-New Orleans":"Off-beat","Off-beat & only-in-Seattle":"Off-beat","Off-beat & only-in-Los Angeles":"Off-beat","Off-beat & only-in-San Francisco":"Off-beat","Off-beat & only-in-Chicago":"Off-beat","Off-beat & only-in-Miami":"Off-beat","Off-beat & only-in-Boston":"Off-beat","Off-beat & only-in-DC":"Off-beat","Cafés & all-day / chef's neighborhood spots":"Cafés","Speakeasies & hidden bars — descending order of amazingness":"Speakeasies","Rooftop bars":"Rooftops","Bars — notable mentions":"Bars","Coffee shops":"Coffee","Restaurants":"Restaurants","Brunch spots":"Brunch","Off-beat & only-in-New-York":"Off-beat","Bakeries":"Bakeries","Dessert bars & sweets":"Dessert","Notable mentions — scene dining, lounges & supper clubs":"Scene","Dance clubs & nightlife":"Nightlife"}
items=[]; cat=None; grp=''; order=0
for ln in src:
    if ln.startswith('## '):
        t=re.sub(r'\s*\(\d+\+?\)\s*$','',ln[3:]).strip(); cat=SHORT.get(t); grp=''; continue
    if cat is None: continue
    if ln.startswith('### ') or re.match(r'^\*\*.*\*\*$',ln.strip()):
        grp=ln.strip().strip('#').strip().strip('*').strip(); continue
    if not ln.strip().startswith('- ['): continue
    for part in re.split(r'\s·\s(?=\[)', ln.strip()[2:]):
        visited='[x]' in part
        raw=re.sub(r'^\[.\]\s*','',part).strip()
        m=re.match(r'^((?:[^(—]|\([^)]*\))*?)\s—\s(.*)$',raw)
        name,tags=(m.group(1),[x.strip() for x in re.split(r'\s·\s',m.group(2)) if x.strip()]) if m else (raw,[])
        name=name.strip(); place=''
        mm=re.match(r'^(.*?)\s*\((.*)\)\s*$',name)
        if mm: name,place=mm.group(1),mm.group(2)
        d={'id':order,'name':name,'place':place,'cat':cat,'group':grp,'visited':visited,'stars':0,'bib':False,'na50':None,'nyt':None,'new':False,'closed':False,'verify':False,'notes':[],'platform':None,'amex':False,'jbf':None,'occ':[],'price':0}
        for t in tags:
            if re.fullmatch(r'★{1,3}',t): d['stars']=len(t)
            elif t=='BIB': d['bib']=True
            elif t.startswith('NA50 #'): d['na50']=int(t[6:])
            elif t.startswith('NYT #'): d['nyt']=int(t[5:])
            elif t in('NYT100','NYT top 10'): d['nyt']=d['nyt'] or 100
            elif t.startswith('NEW'): d['new']=True
            elif t.startswith('CLOSED'): d['closed']=True; d['notes'].append(t.lower())
            elif t=='?' or t.startswith('? '): d['verify']=True; (t[2:] and d['notes'].append(t[2:]))
            elif t in('Resy','Tock','OpenTable','SevenRooms','Walk-in'): d['platform']=t
            elif t=='Amex ✓': d['amex']=True
            elif t.startswith('JBF 2026'): d['jbf']=t.replace('JBF 2026 · ','').replace('JBF 2026','nominee')
            elif t.startswith('W#'): d['nyt']=None; d['notes'].append('Washingtonian #'+t[2:])
            elif t=='WP': d['notes'].append('WP 10 Best New 2026')
            elif t=='opening': d['notes'].append('opening soon')
            elif re.fullmatch(r'\${1,4}',t): d['price']=len(t)
            else: d['notes'].append(t)
        if not d['platform']: d['platform']=lookup(name)
        if d['platform'] in('Resy','Tock') and not d['closed']: d['amex']=True
        if d['closed']: d['platform']=None; d['amex']=False
        d['occ']=[] if d['closed'] else OCC.get(norm(name),[])
        d['q']=urllib.parse.quote_plus(f"{name} {place.split(';')[0] if place else ''} New York".strip())
        items.append(d); order+=1
out=os.path.join(here,'..','assets',SLUG+'.json')
json.dump({'city':SLUG.replace('-',' ').title(),'edition':'Fall/Winter 2026','items':items},open(out,'w',encoding='utf-8'),ensure_ascii=False)
print('wrote',len(items),'places to',os.path.relpath(out))
