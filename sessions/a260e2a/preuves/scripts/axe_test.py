import json,sys
from playwright.sync_api import sync_playwright
pages=['index.html','parcours.html','evaluation.html','documents.html','decision.html','registre.html','galerie.html','glossaire.html','livret.html','credits.html','cours/index.html','ressources.html','mediatheque.html']
axe=open('/tmp/axe/node_modules/axe-core/axe.min.js').read()
out={}
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
    for scheme in ('light','dark'):
        c=b.new_context(viewport={'width':390,'height':800},color_scheme=scheme)
        pg=c.new_page()
        for u in pages:
            pg.goto('http://localhost:8765/'+u,wait_until='load'); pg.wait_for_timeout(500)
            pg.evaluate(axe)
            r=pg.evaluate("axe.run(document,{runOnly:['wcag2a','wcag2aa','wcag21aa']})")
            out[scheme+':'+u]=[(v['id'],v['impact'],len(v['nodes'])) for v in r['violations']]
    b.close()
json.dump(out,open('/home/claude/work/a260e2a/preuves/qa-accessibilite-axe.json','w'),indent=1)
for k,v in out.items(): print(k,v)
