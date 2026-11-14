import os
from playwright.sync_api import sync_playwright
CODE=os.environ['FORMATEUR_CODE'];MAIL=os.environ['FORMATEUR_MAIL']
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox']);pg=b.new_page()
    errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
    def t(c,e):
        pg.goto('http://localhost:8765/formateur.html');pg.fill('#lc',c);pg.fill('#le',e);pg.click('#lb')
        pg.wait_for_function("document.getElementById('lm').textContent.indexOf('Vérification')<0 || document.getElementById('zone').innerHTML.length>0",timeout=30000)
        pg.wait_for_timeout(500)
        return ('OUVERT' if 'Déroulé proposé' in pg.inner_text('#zone') else 'fermé: '+pg.inner_text('#lm'))
    print('bon code+mail',t(CODE,MAIL))
    print('majuscules',t(CODE,MAIL.upper()+' '))
    print('mauvais code',t(CODE+'x',MAIL))
    print('mauvais mail',t(CODE,'autre@example.com'))
    print('erreurs JS',errs)
    b.close()
