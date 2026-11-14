import sys, json, threading, http.server, socketserver, functools, os
from playwright.sync_api import sync_playwright
root=sys.argv[1]; pages=sys.argv[2:]
H=functools.partial(http.server.SimpleHTTPRequestHandler, directory=root)
H.log_message=lambda *a,**k: None
srv=socketserver.TCPServer(('127.0.0.1',0),H); port=srv.server_address[1]
threading.Thread(target=srv.serve_forever,daemon=True).start()
VP={'tel-390':(390,844,True),'tab-portrait-768':(768,1024,True),'tab-paysage-1024':(1024,768,True),'bureau-1280':(1280,800,False)}
out=[]
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
    for pg in pages:
        for name,(w,h,touch) in VP.items():
            ctx=b.new_context(viewport={'width':w,'height':h},has_touch=touch,is_mobile=touch)
            page=ctx.new_page(); errs=[]
            page.on('pageerror',lambda e:errs.append(str(e)[:120]))
            page.on('requestfailed',lambda r:errs.append('req:'+r.url[-60:]))
            try:
                page.goto(f'http://127.0.0.1:{port}/{pg}',wait_until='load',timeout=60000)
                page.wait_for_timeout(700)
                m=page.evaluate("""()=>{const d=document.documentElement;
                  const small=[...document.querySelectorAll('a,button,input,select,summary')].filter(e=>{const r=e.getBoundingClientRect();return r.width>0&&r.height>0&&(r.width<32||r.height<32)}).length;
                  const tot=document.querySelectorAll('a,button,input,select,summary').length;
                  const noalt=[...document.images].filter(i=>!i.hasAttribute('alt')).length;
                  return {sw:d.scrollWidth,cw:d.clientWidth,lang:d.lang||'',viewport:!!document.querySelector('meta[name=viewport]'),small,tot,imgs:document.images.length,noalt,fs:parseFloat(getComputedStyle(document.body).fontSize)}}""")
                m.update(page=pg,vp=name,overflow=m['sw']>m['cw']+1,errors=len(errs),err=errs[:2])
            except Exception as ex:
                m={'page':pg,'vp':name,'fail':str(ex)[:100]}
            out.append(m); ctx.close()
    b.close()
for m in out: print(json.dumps(m,ensure_ascii=False))
