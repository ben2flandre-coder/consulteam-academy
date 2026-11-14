"""Verrouillage de l'animation et de l'espace formateur : rien en clair, mauvais code refusé, bon code ouvre."""
import sys, json, os, re, threading, http.server, socketserver, functools
from playwright.sync_api import sync_playwright
root, code, email = sys.argv[1], os.environ['FORMATEUR_CODE'], open('/home/claude/work/private/emails.txt').read().split()[0]
h = functools.partial(http.server.SimpleHTTPRequestHandler, directory=root); h.log_message = lambda *a, **k: None
srv = socketserver.TCPServer(('127.0.0.1', 0), h); port = srv.server_address[1]
threading.Thread(target=srv.serve_forever, daemon=True).start()
R = []
def ok(n, c, d=''): R.append({'test': n, 'ok': bool(c), 'detail': str(d)}); print(('OK  ' if c else 'KO  ') + n, d)
for page, marker in (('animation.html', 'data-sec='), ('formateur.html', 'Déroulé proposé')):
    raw = open(root + '/' + page, encoding='utf-8').read()
    ok(page + ' : aucun contenu en clair', marker not in raw and 'Habilitation électrique : formation initiale' not in raw)
    ok(page + ' : contenu chiffré présent', '"ct"' in raw or 'ct' in raw and 'AES' in raw or "'ct'" in raw)
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--no-sandbox'])
    for page, probe in (('animation.html', "document.querySelectorAll('.slide').length"), ('formateur.html', "document.body.innerText.includes('Déroulé proposé')")):
        for good in (False, True):
            ctx = b.new_context(viewport={'width': 1280, 'height': 800}); pg = ctx.new_page(); errs = []; pg.on('pageerror', lambda e: errs.append(str(e)))
            pg.goto('http://127.0.0.1:%d/%s' % (port, page)); pg.fill('#lc', code if good else 'mauvais-code'); pg.fill('#le', email if good else 'x@y.fr'); pg.click('#lb' if pg.query_selector('#lb') else 'form button'); pg.wait_for_timeout(6000)
            r = pg.evaluate(probe)
            if good: ok(page + ' : bon code ouvre', (r == 324) if page == 'animation.html' else r, r)
            else: ok(page + ' : mauvais code refusé', not r, pg.evaluate("(document.getElementById('lm')||{}).textContent"))
            ok(page + (' bon' if good else ' mauvais') + ' : aucune erreur JS', not errs, errs)
            ctx.close()
    b.close()
json.dump(R, open(root + '/preuves/test-verrouillage.json', 'w'), ensure_ascii=False, indent=1)
sys.exit(0 if all(x['ok'] for x in R) else 1)
