import sys,threading,http.server,socketserver,functools,json
from playwright.sync_api import sync_playwright
root=sys.argv[1]
h=functools.partial(http.server.SimpleHTTPRequestHandler,directory=root); h.log_message=lambda *a,**k:None
srv=socketserver.TCPServer(('127.0.0.1',0),h);port=srv.server_address[1]
threading.Thread(target=srv.serve_forever,daemon=True).start()
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox']); ctx=b.new_context(); pg=ctx.new_page()
    pg.goto(f'http://127.0.0.1:{port}/index.html'); pg.wait_for_timeout(2500)
    ready=pg.evaluate("navigator.serviceWorker.ready.then(()=>true)")
    pg.reload(); pg.wait_for_timeout(1000)
    ctx.set_offline(True); out={'sw_pret':ready}
    pg.goto(f'http://127.0.0.1:{port}/parcours.html#m20'); pg.wait_for_selector('h1',timeout=8000); pg.wait_for_timeout(800)
    out['h1_hors_ligne']=pg.evaluate("document.querySelector('h1').textContent")
    out['images_chargees']=pg.evaluate("[...document.images].map(i=>[i.getAttribute('src'),i.complete&&i.naturalWidth>0])")
    print(json.dumps(out,ensure_ascii=False))
