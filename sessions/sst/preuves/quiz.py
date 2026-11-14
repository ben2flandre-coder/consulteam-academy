import sys,json
from playwright.sync_api import sync_playwright
root=sys.argv[1]
qs=json.load(open(root+'/data/questions.json',encoding='utf-8'))
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':390,'height':844}); errs=[]
    pg.on('pageerror',lambda e:errs.append(str(e))); pg.on('console',lambda m:errs.append(m.text) if m.type=='error' else None)
    pg.goto('file://'+root+'/valider.html'); pg.wait_for_timeout(800)
    n=pg.locator('fieldset').count(); print('questions rendues',n,'attendu',len(qs))
    good=bad=0
    for i,q in enumerate(qs):
        fs=pg.locator('fieldset:has(input[name="%s"])'%q['id'])
        fs.locator('input').nth(q['bonne']).check(); fs.locator('button').click()
        t=fs.locator('p').inner_text()
        good+=t.startswith('Correct')
        w=(q['bonne']+1)%len(q['options']); fs.locator('input').nth(w).check(); fs.locator('button').click()
        bad+=fs.locator('p').inner_text().startswith('Pas tout')
    print('correct détectées',good,'/',len(qs),'; fausses détectées',bad,'/',len(qs)); print('erreurs console',len(errs),errs[:2])
    ov=pg.evaluate("document.documentElement.scrollWidth-document.documentElement.clientWidth"); print('débordement',ov)
    pg.screenshot(path='/home/claude/work/qa/shots/valider_390.png',full_page=False); b.close()
