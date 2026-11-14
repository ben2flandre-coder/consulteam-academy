import sys,os,re,json,glob,subprocess,time,html as H
from urllib.parse import urlparse,unquote
from playwright.sync_api import sync_playwright
root=sys.argv[1]; prev=os.path.join(root,'preuves'); os.makedirs(prev,exist_ok=True)
# 1 liens internes
bad=[];n=0
ids={}
for f in glob.glob(root+'/*.html'):
    ids[os.path.basename(f)]=set(re.findall(r'\sid="([^"]+)"',open(f,encoding='utf-8').read()))
for f in sorted(glob.glob(root+'/*.html')):
    s=open(f,encoding='utf-8').read()
    for m in re.finditer(r'(?:href|src)="([^"#][^"#]*)(#[^"]*)?"',s):
        u,a=m.group(1),(m.group(2) or '')[1:]
        if re.match(r'(https?:|mailto:|data:|javascript:)',u): continue
        n+=1; p=os.path.join(root,unquote(u))
        if not os.path.exists(p): bad.append((os.path.basename(f),u,'fichier absent'))
        elif a and u.endswith('.html') and a not in ids.get(u,set()): bad.append((os.path.basename(f),u+'#'+a,'ancre absente'))
    for m in re.finditer(r'href="#([^"]+)"',s):
        if m.group(1) not in ids[os.path.basename(f)]: bad.append((os.path.basename(f),'#'+m.group(1),'ancre locale absente'))
json.dump({'liens_testes':n,'casses':bad},open(prev+'/liens.json','w'),ensure_ascii=False,indent=1); print('liens',n,'casses',len(bad),bad[:5])
# serveur
srv=subprocess.Popen(['python3','-m','http.server','8765','-d',root],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL); time.sleep(1)
axe=open('/tmp/axe/node_modules/axe-core/axe.min.js',encoding='utf-8').read()
res={'axe':{},'hors_ligne':None,'quiz_module':None}
with sync_playwright() as p:
    b=p.chromium.launch(); ctx=b.new_context(viewport={'width':1280,'height':900}); pg=ctx.new_page()
    for f in sorted(glob.glob(root+'/*.html')):
        nme=os.path.basename(f); pg.goto('http://localhost:8765/'+nme); pg.wait_for_timeout(1300)
        pg.evaluate("document.querySelectorAll('main>*').forEach(e=>{e.style.animation='none';e.style.opacity=1;e.style.transform='none'})")
        pg.add_script_tag(content=axe); r=pg.evaluate("axe.run(document,{runOnly:['wcag2a','wcag2aa','wcag21aa','best-practice']}).then(r=>r.violations.map(v=>({id:v.id,impact:v.impact,n:v.nodes.length,help:v.help})))")
        res['axe'][nme]=r
    # hors ligne
    pg=ctx.new_page(); pg.goto('http://localhost:8765/index.html'); pg.wait_for_timeout(2500)
    sw=pg.evaluate("navigator.serviceWorker.ready.then(r=>!!r.active)")
    pg.reload(); pg.wait_for_timeout(1500)
    ctx.set_offline(True)
    try:
        pg.goto('http://localhost:8765/m3.html'); pg.wait_for_timeout(1500)
        ok=pg.evaluate("document.querySelectorAll('h1').length===1 && document.querySelectorAll('.quiz').length===1")
        pg.goto('http://localhost:8765/fiches-secourir.html'); pg.evaluate("document.querySelectorAll('img').forEach(i=>i.loading='eager')"); pg.evaluate('window.scrollTo(0,document.body.scrollHeight)'); pg.wait_for_timeout(1500)
        imgs=pg.evaluate("[...document.images].every(i=>i.complete&&i.naturalWidth>0)")
        res['hors_ligne']={'service_worker_actif':sw,'page_module_hors_ligne':ok,'images_fiches_chargees':imgs}
    except Exception as e: res['hors_ligne']={'service_worker_actif':sw,'erreur':str(e)[:200]}
    ctx.set_offline(False)
    # quiz de module
    pg.goto('http://localhost:8765/m5.html'); pg.wait_for_timeout(800)
    nq=pg.evaluate("document.querySelectorAll('.quiz fieldset').length")
    pg.click('.quiz fieldset:first-of-type label:first-of-type input'); pg.click('.quiz fieldset:first-of-type button')
    txt=pg.inner_text('.quiz fieldset:first-of-type .expl'); lnk=pg.get_attribute('.quiz fieldset:first-of-type .expl a','href')
    res['quiz_module']={'questions':nq,'correction_affichee':bool(txt),'lien_lecon':lnk}
    # PDF livret
    pg.goto('http://localhost:8765/livret.html'); pg.wait_for_timeout(1500)
    pg.emulate_media(media='print'); pg.pdf(path=root+'/pdf/livret-sst-consulteam.pdf' if os.path.isdir(root+'/pdf') else '/tmp/livret.pdf',format='A4',print_background=True,margin={'top':'14mm','bottom':'14mm','left':'12mm','right':'12mm'})
    b.close()
srv.terminate()
json.dump(res,open(prev+'/qa-accessibilite-axe-hors-ligne.json','w'),ensure_ascii=False,indent=1)
tot={}
for k,v in res['axe'].items():
    for x in v: tot.setdefault((x['id'],x['impact'],x['help']),[]).append((k,x['n']))
for k,v in tot.items(): print(k,len(v),v[:3])
print(res['hors_ligne'],res['quiz_module'])
