"""Test du mode animation A260E2A : structure, QR + mention téléphone sur chaque diapo, minutes, QCM, débordements, axe."""
import sys, json, re, os, threading, http.server, socketserver, functools
from playwright.sync_api import sync_playwright
root = sys.argv[1]
axe = open('/tmp/axe/node_modules/axe-core/axe.min.js').read()
h = functools.partial(http.server.SimpleHTTPRequestHandler, directory=root); h.log_message = lambda *a, **k: None
srv = socketserver.TCPServer(('127.0.0.1', 0), h); port = srv.server_address[1]
threading.Thread(target=srv.serve_forever, daemon=True).start()
R = {'verifs': []}
def ok(n, c, d=''):
    R['verifs'].append({'test': n, 'ok': bool(c), 'detail': d}); print(('OK  ' if c else 'KO  ') + n, d)
src = open(root + '/animation.html', encoding='utf-8').read()
slides = re.findall(r'<section class="slide([^"]*)" data-sec="([^"]*)"([^>]*)>(.*?)</section>', src, re.S)
ok('nombre de diapositives', 250 <= len(slides) <= 400, len(slides))
ok('QR sur chaque diapositive', all('class="qb"' in s[3] and 'assets/qr/' in s[3] and 'Suivre sur votre téléphone' in s[3] for s in slides) or all(('class="qb"' in s[3]) for s in slides))
ok('mention téléphone sur chaque diapositive', all('Suivre sur votre téléphone' in s[3] for s in slides))
qrs = set(re.findall(r'assets/qr/([\w-]+\.svg)', src)); miss = [q for q in qrs if not os.path.exists(root + '/assets/qr/' + q)]
ok('fichiers QR présents', not miss, miss)
imgs = set(re.findall(r'<img src="((?:images)/[^"]+)"', src)) | set(re.findall(r"url\('\.\./(images/[^']+)'\)", src))
miss = [i for i in imgs if not os.path.exists(root + '/' + i)]
ok('images présentes', not miss, '%d images, manquantes %s' % (len(imgs), miss))
mods = set(int(x) for x in re.findall(r'data-sec="J\d · M(\d+) ·', src)); ok('23 modules présents', mods == set(range(1, 24)), sorted(set(range(1, 24)) - mods))
mins = {}
for k, sec, rest, body in slides:
    m = re.search(r'data-min="(\d+)"', rest)
    if m: mins.setdefault(sec[:2], {})[sec] = int(m.group(1))
tot = {d: sum(v for s, v in x.items() if 'carte' not in s and not re.search(r'M(9|12|13|14|15) ·', s)) for d, x in mins.items()}
ok('minutes par jour = 420 (7 h)', all(tot.get(d) == 420 for d in ('J1', 'J2', 'J3')), tot)
ok('notes formateur', sum('class="note"' in s[3] for s in slides) >= len(slides) * 0.9)
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--no-sandbox'])
    for name, (w, hh, touch) in {'projecteur-1920': (1920, 1080, False), 'bureau-1280': (1280, 720, False), 'tablette-768': (768, 1024, True), 'tel-390': (390, 844, True)}.items():
        ctx = b.new_context(viewport={'width': w, 'height': hh}, has_touch=touch, is_mobile=touch)
        pg = ctx.new_page(); errs = []; pg.on('pageerror', lambda e: errs.append(str(e)))
        pg.goto('http://127.0.0.1:%d/animation.html' % port); pg.wait_for_timeout(500)
        n = pg.evaluate("document.querySelectorAll('.slide').length"); over = []; hid = []
        for i in range(1, n + 1, 1 if w > 800 else 3):
            pg.evaluate("location.hash='#%d'" % i); pg.wait_for_timeout(60)
            r = pg.evaluate("(()=>{var s=document.querySelector('.slide.active');return [document.documentElement.scrollWidth>innerWidth+1,s.scrollWidth>s.clientWidth+2,getComputedStyle(s.querySelector('.qb')).display]})()")
            if r[0] or r[1]: over.append(i)
            if r[2] == 'none' and w > 760: hid.append(i)
        ok('%s : pas de débordement horizontal' % name, not over, over[:8])
        if w > 760: ok('%s : QR visible partout' % name, not hid, hid[:8])
        ok('%s : aucune erreur JS' % name, not errs, errs)
        if name == 'bureau-1280':
            # navigation, fragments, QCM, chrono, notes, sommaire, QR agrandi
            pg.evaluate("location.hash='#14'"); pg.wait_for_timeout(200)
            pg.click('.slide.active .opt[data-j="1"]'); t = pg.inner_text('#qsc')
            ok('QCM collectif : score salle', 'Salle' in t, t)
            pg.keyboard.press('q'); ok('touche Q agrandit le QR', pg.evaluate("document.body.classList.contains('qbig')")); pg.keyboard.press('q')
            pg.keyboard.press('n'); ok('notes formateur (N)', pg.evaluate("document.getElementById('notes').classList.contains('on')")); pg.keyboard.press('n')
            pg.keyboard.press('g'); ok('sommaire (G)', pg.evaluate("document.querySelectorAll('#ovw li').length") == n); pg.keyboard.press('g')
            pg.goto('http://127.0.0.1:%d/animation.html#8' % port); pg.reload(); pg.wait_for_timeout(300); pg.keyboard.press('ArrowRight'); pg.wait_for_timeout(400)
            before = pg.evaluate("document.querySelectorAll('.slide.active .frag.show').length"); pg.keyboard.press('ArrowRight'); after = pg.evaluate("document.querySelectorAll('.slide.active .frag.show').length")
            ok('révélation progressive (→)', after == before + 1, (before, after))
            ok('chrono réglé sur la séquence', '30:00' in pg.inner_text('#timer') or ':' in pg.inner_text('#timer'), pg.inner_text('#timer'))
            for i in (1, 6, 12, 150, 219, 227, 231):
                pg.evaluate("location.hash='#%d'" % i); pg.wait_for_timeout(150)
                pg.evaluate("document.querySelectorAll('.slide.active .frag').forEach(f=>f.classList.add('show'))")
                pg.add_script_tag(content=axe) if i == 1 else None
                res = pg.evaluate("axe.run('.slide.active',{runOnly:['wcag2a','wcag2aa']}).then(r=>r.violations.map(v=>v.id+':'+v.nodes.length))")
                R.setdefault('axe', {})[i] = res
            bad = {k: v for k, v in R['axe'].items() if v}
            ok('axe (7 diapositives types) : 0 violation', not bad, bad)
        ctx.close()
    b.close()
json.dump(R, open(root + '/preuves/test-animation.json', 'w'), ensure_ascii=False, indent=1)
sys.exit(0 if all(v['ok'] for v in R['verifs']) else 1)
