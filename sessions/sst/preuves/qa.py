import sys,glob,os,json
from playwright.sync_api import sync_playwright
root=sys.argv[1]; out=sys.argv[2]; os.makedirs(out,exist_ok=True)
res=[]
with sync_playwright() as p:
    b=p.chromium.launch()
    for w,h in((1280,900),(390,844)):
        ctx=b.new_context(viewport={'width':w,'height':h}); pg=ctx.new_page()
        errs=[]
        pg.on('console',lambda m:errs.append(m.text) if m.type=='error' else None)
        pg.on('pageerror',lambda e:errs.append(str(e)))
        for f in sorted(glob.glob(root+'/*.html')):
            n=os.path.basename(f); errs.clear()
            pg.goto('file://'+f); pg.wait_for_load_state('load'); pg.wait_for_timeout(1500)
            ov=pg.evaluate("document.documentElement.scrollWidth-document.documentElement.clientWidth")
            lang=pg.evaluate("document.documentElement.lang"); h1=pg.evaluate("document.querySelectorAll('h1').length")
            op=pg.evaluate("Math.min(...[...document.querySelectorAll('main>*')].map(e=>+getComputedStyle(e).opacity))")
            img=pg.evaluate("[...document.images].filter(i=>!i.alt&&i.alt!=='').length")
            pg.screenshot(path=f'{out}/{n[:-5]}_{w}.png',full_page=True)
            res.append((w,n,ov,lang,h1,img,len(errs),op))
        ctx.close()
    b.close()
bad=0
for r in res:
    flag='' if (r[2]<=1 and r[3]=='fr' and r[4]==1 and r[5]==0 and r[6]==0 and r[7]==1) else '  <-- ATTENTION'
    bad+=bool(flag); print(*r,flag)
print('ATTENTION:',bad)
