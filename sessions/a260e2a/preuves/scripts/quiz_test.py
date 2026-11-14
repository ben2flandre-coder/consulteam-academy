import sys,threading,http.server,socketserver,functools,json
from playwright.sync_api import sync_playwright
root=sys.argv[1]
h=functools.partial(http.server.SimpleHTTPRequestHandler,directory=root)
h.log_message=lambda *a,**k:None
srv=socketserver.TCPServer(('127.0.0.1',0),h);port=srv.server_address[1]
threading.Thread(target=srv.serve_forever,daemon=True).start()
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
    pg=b.new_page();errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
    for mode in('all','wrong'):
        pg.goto(f'http://127.0.0.1:{port}/evaluation.html');pg.evaluate("location.hash='#all'");pg.wait_for_selector('fieldset')
        res=pg.evaluate("""(mode)=>{
          const Q={};A.modules.forEach(m=>m.questions.forEach(q=>Q[q.q]=q));
          document.querySelectorAll('fieldset').forEach(fs=>{
            const q=Q[fs.querySelector('legend').textContent.replace(/^\\d+\\. /,'')];const t=q.type||'s';
            const opts=[...fs.querySelectorAll('.opt')];
            if(t==='o'){opts.forEach(l=>{const tx=l.querySelector('span').textContent;const i=q.options.indexOf(tx);const sel=l.querySelector('select');sel.value=String(mode==='all'?i:(i+1)%q.options.length)})}
            else{opts.forEach(l=>{const tx=l.querySelector('span').textContent;const i=q.options.indexOf(tx);const good=t==='s'?i===q.correct:q.correct.includes(i);const inp=l.querySelector('input');inp.checked=(mode==='all')?good:!good})}
          });
          document.getElementById('fm').requestSubmit();
          return document.getElementById('res').textContent.slice(0,40)}""",mode)
        print(mode,res)
    print('erreurs JS:',errs)
    b.close()
