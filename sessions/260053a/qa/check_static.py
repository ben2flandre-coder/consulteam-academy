from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
from collections import Counter
import json,re,subprocess,xml.etree.ElementTree as ET
BASE=Path(__file__).resolve().parents[1]
class Page(HTMLParser):
    def __init__(self,s):super().__init__();self.ids=[];self.refs=[];self.issues=[];self.feed(s)
    def handle_starttag(self,t,a):
        d=dict(a)
        for k,n in Counter(k for k,v in a).items():
            if n>1:self.issues.append('Attribut répété '+t+'.'+k)
        if d.get('id'):self.ids.append(d['id'])
        for k in ['href','src','poster']:
            if d.get(k):self.refs.append(d[k])
        if t=='img' and 'alt' not in d:self.issues.append('Image sans alternative : '+d.get('src',''))
        if t=='svg' and d.get('class')=='segno' and 'viewbox' not in d:self.issues.append('QR sans viewBox')
pages={p.resolve():Page(p.read_text(encoding='utf-8')) for p in BASE.rglob('*.html')}
errors=[];refs=0
for p,h in pages.items():
    for e in h.issues:errors.append({'file':p.name,'error':e})
    for id,n in Counter(h.ids).items():
        if n>1:errors.append({'file':p.name,'error':'ID répété : '+id})
    for u in h.refs:
        refs+=1;v=urlsplit(u)
        if v.scheme or u=='#':continue
        dst=(p.parent/unquote(v.path)).resolve() if v.path else p
        if dst.is_dir():dst/= 'index.html'
        if not dst.exists():errors.append({'file':p.name,'error':'Cible absente : '+u})
        elif v.fragment and dst in pages:
            dynamic=dst.name=='animation.html' and v.fragment.isdigit()
            if not dynamic and unquote(v.fragment) not in pages[dst].ids:errors.append({'file':p.name,'error':'Ancre absente : '+u})
    s=p.read_text(encoding='utf-8')
    for code in re.findall(r'<script(?![^>]*\bsrc=)[^>]*>([\s\S]*?)</script>',s):
        if not code.strip():continue
        result=subprocess.run(['node','--check'],input=code,text=True,capture_output=True,encoding='utf-8')
        if result.returncode:errors.append({'file':p.name,'error':result.stderr})
for p in (BASE/'js').glob('*.js'):
    r=subprocess.run(['node','--check',str(p)],text=True,capture_output=True,encoding='utf-8')
    if r.returncode:errors.append({'file':p.name,'error':r.stderr})
for p in (BASE/'assets/svg').rglob('*.svg'):
    try:ET.parse(p)
    except ET.ParseError as e:errors.append({'file':p.name,'error':str(e)})
report={'pages':len(pages),'local_and_external_references':refs,'errors':errors,'scope':'Existence des cibles locales, ancres statiques, attributs, alternatives, syntaxe JS et XML ; les services externes ne sont pas testés par ce contrôle.'}
(BASE/'qa/static-report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(report,ensure_ascii=False,indent=2))
if errors:raise SystemExit(1)
