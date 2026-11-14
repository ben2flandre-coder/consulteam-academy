import json,sys
from playwright.sync_api import sync_playwright
R='http://localhost:8765/'
res={}
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox']);pg=b.new_page(viewport={'width':1280,'height':900})
    errs=[];pg.on('pageerror',lambda e:errs.append(str(e)));pg.on('console',lambda m:errs.append(m.text) if m.type=='error' else None)
    pg.goto(R+'parcours.html');pg.wait_for_selector('.card')
    res['cartes']=pg.locator('a.card[data-m]').count()
    pg.click('button.chip[data-sym="4"]');res['route_BC']=pg.locator('.route .card').count();pg.screenshot(path='/tmp/s_liste.png')
    pg.goto(R+'parcours.html#m11');pg.wait_for_selector('.rail')
    res['phases']=pg.locator('.rail .ph:not([data-ph="tout"])').count();pg.screenshot(path='/tmp/s_voir.png')
    pg.click('.rail .ph[data-ph="comprendre"]');pg.wait_for_selector('.pasbox')
    res['pasbox']=pg.locator('.pasbox').count()
    pg.click('.pasbox [data-pas="start"]');n=0
    while pg.locator('.pcard').count():
        pg.screenshot(path='/tmp/s_pas.png') if n==1 else None
        pg.click('.pcard [data-pas="next"]');n+=1
        if n>30:break
    res['etapes']=n;res['fin_pas']='Procédure déroulée' in pg.inner_text('.pv')
    pg.click('.rail .ph[data-ph="faire"]');pg.wait_for_selector('fieldset.qc')
    res['q_guidees']=pg.locator('fieldset.qc').count()
    fs=pg.locator('fieldset.qc').first
    fs.locator('[data-act="aid"]').click();t1=fs.locator('.qr').inner_text();fs.locator('[data-act="aid"]').click();t2=fs.locator('.qr').inner_text()
    res['aide1']=t1[:40];res['aide2']=t2[:60]
    fs.locator('[data-act="chk"]').click();res['fb_vide']=fs.locator('.qr').inner_text()[:40]
    fs.locator('label.opt input:not([disabled])').first.check();fs.locator('[data-act="chk"]').click();res['fb']=fs.locator('.qr').inner_text()[:30]
    pg.click('.rail .ph[data-ph="verifier"]');pg.wait_for_selector('#fv')
    nv=pg.locator('#fv fieldset').count();res['q_verif']=nv
    for i in range(nv):
        pg.locator('#fv fieldset').nth(i).locator('input,select').first.evaluate("e=>{if(e.tagName=='SELECT'){}else e.click()}")
    pg.click('[data-act="fin"]');res['score']=pg.inner_text('#vres')[:30]
    pg.screenshot(path='/tmp/s_verif.png')
    pg.click('.rail .ph[data-ph="retenir"]');res['check']=pg.locator('ul.chk li').count()
    pg.click('.next [data-ph="fin"]')
    pg.wait_for_timeout(300);res['retour_liste']=pg.locator('.chips').count()
    # modules sans exos : tous les modules s'ouvrent sans erreur
    bad=[]
    for i in range(1,24):
        pg.goto(R+'parcours.html#m%d'%i);pg.reload();pg.wait_for_selector('.rail',timeout=5000)
        for ph in ['comprendre','faire','verifier','retenir']:
            pg.click('.rail .ph[data-ph="%s"]'%ph)
        if pg.locator('.pan').inner_text().strip()=='' : bad.append(i)
    res['modules_ko']=bad
    # mobile
    pg.set_viewport_size({'width':390,'height':844});pg.goto(R+'parcours.html#m19/faire');pg.reload();pg.wait_for_selector('.rail')
    res['debordement_mobile']=pg.evaluate("document.documentElement.scrollWidth>innerWidth+2");pg.screenshot(path='/tmp/s_mobile.png')
    res['erreurs']=errs[:5]
    b.close()
print(json.dumps(res,ensure_ascii=False,indent=1))
