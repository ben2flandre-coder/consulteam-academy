import sys
from playwright.sync_api import sync_playwright
pages=sys.argv[1:]
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
    pg=b.new_page(viewport={'width':1366,'height':900})
    errs=[]
    pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.on('console',lambda m:errs.append(m.text) if m.type=='error' else None)
    for u in pages:
        pg.goto('http://localhost:8765/'+u,wait_until='load');pg.wait_for_timeout(2500)
        n=u.replace('/','_').replace('#','_').replace('.html','')or'idx'
        pg.screenshot(path=f'/tmp/s_{n}.png',full_page=False)
        print(u,pg.title(),len(errs))
    print(errs[:8]);b.close()
