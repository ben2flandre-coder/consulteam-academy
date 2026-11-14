import json
from playwright.sync_api import sync_playwright
R='http://localhost:8765/evaluation.html'
res={}
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox']);pg=b.new_page(viewport={'width':1100,'height':900})
    errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto(R);pg.wait_for_selector('.card')
    evs=pg.evaluate("A.evals.map(e=>e.id)");res['niveaux']={}
    for e in evs:
        pg.goto(R+'#n-'+e);pg.reload();pg.wait_for_selector('#fm')
        n=pg.locator('fieldset.q').count()
        pg.click('button[type=submit]');t=pg.inner_text('#res')
        res['niveaux'][e]=n
    pg.goto(R+'#complete');pg.reload();pg.wait_for_selector('#fm');res['complete']=pg.locator('fieldset.q').count()
    pg.goto(R+'#all');pg.reload();pg.wait_for_selector('#fm');res['tirage75']=pg.locator('fieldset.q').count()
    # 100 % : cocher bonnes réponses via données
    pg.goto(R+'#n-bc');pg.reload();pg.wait_for_selector('#fm')
    pg.click('button[type=submit]');res['res_vide']=pg.inner_text('#res')[:120]
    res['min_niveau']=min(res['niveaux'].values());res['erreurs']=errs
    # répétabilité : deux tirages différents
    a=[];
    for _ in range(2):
        pg.goto(R+'#n-br');pg.reload();pg.wait_for_selector('#fm');a.append(pg.evaluate("[...document.querySelectorAll('legend')].map(l=>l.textContent).sort().join('|')"))
    res['tirages_differents']=a[0]!=a[1]
print(json.dumps(res,ensure_ascii=False,indent=1))
