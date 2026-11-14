import sys,threading,http.server,socketserver,functools,json
from playwright.sync_api import sync_playwright
root=sys.argv[1]; out=sys.argv[2]
h=functools.partial(http.server.SimpleHTTPRequestHandler,directory=root); h.log_message=lambda *a,**k:None
srv=socketserver.TCPServer(('127.0.0.1',0),h);port=srv.server_address[1]
threading.Thread(target=srv.serve_forever,daemon=True).start()
res=[]
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
    for w,hh,tag in((390,800,'tel-390'),(1280,900,'bureau-1280')):
        pg=b.new_page(viewport={'width':w,'height':hh}); errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
        for m in (19,20,21,22):
            pg.goto(f'http://127.0.0.1:{port}/parcours.html#m{m}'); pg.wait_for_selector('h1'); pg.wait_for_timeout(600)
            r=pg.evaluate("""()=>({h1:document.querySelector('h1').textContent,ov:document.documentElement.scrollWidth>innerWidth,imgs:[...document.images].map(i=>[i.getAttribute('src'),i.complete&&i.naturalWidth>0])})""")
            f=f'{out}/module{m}-{tag}.png'; pg.screenshot(path=f,full_page=True)
            res.append(dict(module=m,vp=tag,h1=r['h1'],debordement=r['ov'],images=r['imgs'],erreurs_js=list(errs),capture=f.split('/')[-1]))
print(json.dumps(res,ensure_ascii=False))
