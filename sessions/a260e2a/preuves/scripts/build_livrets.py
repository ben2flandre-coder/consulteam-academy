import sys, os, json, re, subprocess
sys.path.insert(0,'/home/claude/work/src')
import livrets
from playwright.sync_api import sync_playwright
import pdfplumber
R='/home/claude/work/a260e2a'
OUT='/home/claude/work/livrets'; os.makedirs(OUT,exist_ok=True)
d=json.loads(re.sub(r'^window\.A=|;$','',open(R+'/data/content.js',encoding='utf-8').read()))
from PIL import Image
os.makedirs(R+'/_lvimg',exist_ok=True)
for v in d['visuels']:
    f=v['fichier']
    if f.endswith('.webp'):
        o='_lvimg/'+os.path.basename(f).replace('.webp','.jpg')
        if not os.path.exists(R+'/'+o):
            im=Image.open(R+'/'+f).convert('RGB'); im.thumbnail((800,800)); im.save(R+'/'+o,quality=78,optimize=True)
        v['fichier']=o
L=livrets.Livret(d['modules'],d['visuels'],d['schemas'],d['tps'],None)
def render(html,pdf):
    tmp=R+'/_livret_formation.html'; open(tmp,'w',encoding='utf-8').write(html)
    with sync_playwright() as p:
        b=p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
        pg=b.new_page(); pg.goto('file://'+tmp); pg.wait_for_timeout(1500)
        pg.pdf(path=pdf,prefer_css_page_size=True,print_background=True)
        b.close()
    os.remove(tmp)
def locate(pdf):
    toc={}
    with pdfplumber.open(pdf) as P:
        txt=[(pg.extract_text() or '') for pg in P.pages]
    for i,t in enumerate(txt):
        for mid in L.mods:
            m=L.mods[mid]
            if ('p%d'%mid) not in toc and re.search(r'fiches ·',t,re.I) and m['title'][:14] in t and re.search(r'^%02d\b'%mid,t,re.M) and i>2:
                toc['p%d'%mid]=i+1
        if i>3 and 'Questions flash et décisions' in t and 'corr' not in toc: toc['corr']=i+1
        if i>3 and 'Mon plan d’action' in t and 'Tableau' not in t and 'plan' not in toc and 'Ce que je retiens' in t: toc['plan']=i+1
    toc['loin']=len(txt); return toc,len(txt)
pdf=OUT+'/formation.pdf'
import numpy as np, glob, subprocess
def fills(pdf):
    for f in glob.glob('/tmp/lv/q-*.png'): os.remove(f)
    subprocess.run(['pdftoppm','-r','30','-gray','-png',pdf,'/tmp/lv/q'],capture_output=True)
    out=[]
    for f in sorted(glob.glob('/tmp/lv/q-*.png')):
        a=np.array(Image.open(f)); h=a.shape[0]; body=a[int(h*.06):int(h*.94)]
        rows=np.where((body<235).sum(axis=1)>2)[0]
        out.append(rows.max()/body.shape[0] if len(rows) else 0)
    return out
dens={}
toc={}
for rnd in range(4):
    L.dens=dens
    render(L.build(toc),pdf); toc,n=locate(pdf)
    render(L.build(toc),pdf); toc,n=locate(pdf)
    fl=fills(pdf)
    starts=sorted((toc['p%d'%m],m) for m in L.mods if 'p%d'%m in toc)
    changed=False
    for k,(st,m) in enumerate(starts):
        en=(starts[k+1][0]-1) if k+1<len(starts) else toc.get('corr',n+1)-1
        last=fl[en-1]
        if last<0.42 and dens.get(m,0)<3:
            dens[m]=dens.get(m,0)+1; changed=True
    print('round',rnd,n,'pages, dens',dens)
    if not changed: break
print(subprocess.run(['pdfinfo',pdf],capture_output=True,text=True).stdout.split('Pages:')[1].split()[0])

import shutil; shutil.rmtree(R+'/_lvimg',ignore_errors=True)
