# -*- coding: utf-8 -*-
"""Livret de formation apprenant A260E2A (A4, Chromium) : même maquette que A2609LA / A260BNA.
Couverture, mode d'emploi, parcours, sommaire, parties colorées (fiches, QR « Sur le site », Mes notes),
corrigés, plan d'action, page de fin. Pas de notes formateur."""
import re, json, html as H, os
import deck_e2a as D
from deck_e2a import e, ico, icf, clean, sents, kpi, DANGER, J1, J2, CARTE, BASE

CODE = 'A260E2A'
TITRE = 'Habilitation électrique · formation initiale'
SOUS = 'B0 · H0 · H0V · BS · BE Manœuvre · BR · BC · symboles selon désignation'
DATES = 'Lundi 14, mardi 15 et mercredi 16 décembre 2026 · 21 h dont 7 h de pratique'
LIEU = 'Consul Team Security · La Seyne-sur-Mer · pour les équipes d’ADI sécurité'
EDITION = 'Édition du 14/11/2026'
COLORS = ['#0b68ae', '#102c53', '#0f8b8d', '#c98a0b', '#b5237a', '#2f7d32', '#6a4c93', '#c2410c', '#0369a1', '#7c2d12']
ORDER = [(1, [m for m, _ in J1]), (2, [m for m, _ in J2]), (3, [16] + CARTE)]
DAYLAB = {1: 'Jour 1 · lundi 14 décembre', 2: 'Jour 2 · mardi 15 décembre', 3: 'Jour 3 · mercredi 16 décembre et modules à la carte'}

CSS = r'''
@page{size:A4;margin:16mm 14mm 16mm 14mm}
@page cover{margin:0}
@page back{margin:0}
*{box-sizing:border-box;font-feature-settings:"calt" 0,"case" 0,"ss01" 0;font-variant-ligatures:none}
html{-webkit-print-color-adjust:exact;print-color-adjust:exact}
body{margin:0;font:9.4pt/1.4 "Segoe UI","Helvetica Neue",Arial,sans-serif;color:#16273d}
h1,h2,h3,h4{font-family:Bahnschrift,"DIN Alternate","Arial Narrow",Arial,sans-serif;margin:0;color:#102c53}
.cover{page:cover;height:297mm;width:210mm;background:#102c53;color:#fff;position:relative;overflow:hidden;break-after:page}
.cover:before{content:"";position:absolute;left:0;top:0;bottom:0;width:7mm;background:#f6b63d}
.cover .in{position:absolute;left:24mm;right:20mm;top:22mm}
.cover img.logo{width:62mm;filter:brightness(0) invert(1)}
.cover .kick{margin-top:70mm;color:#f6b63d;font:600 8.5pt Bahnschrift,Arial,sans-serif;letter-spacing:.28em}
.cover h1{color:#fff;font-size:30pt;line-height:1.1;margin:6mm 0 4mm}
.cover .sub{font:italic 12pt Georgia,serif;color:#cfe0f5;margin-bottom:10mm}
.cover .when{position:absolute;left:24mm;bottom:40mm;font-size:10pt;line-height:1.6}
.cover .when b{color:#f6b63d}
.cover .qr{position:absolute;right:20mm;bottom:40mm;background:#fff;padding:3mm;border-radius:3mm;text-align:center;color:#102c53;font-size:7pt;width:34mm}
.cover .qr img{width:28mm;height:28mm;display:block;margin:0 auto 1mm}
.cover .legal{position:absolute;left:24mm;right:20mm;bottom:14mm;font-size:7.5pt;color:#9fb6d3}
.cover .bandes{position:absolute;right:-20mm;top:120mm;width:110mm;height:110mm;border:2px solid rgba(246,182,61,.25);border-radius:50%}
.cover .bandes:after{content:"";position:absolute;inset:14mm;border:2px solid rgba(255,255,255,.12);border-radius:50%}
.pg{break-before:page}
.kicker{font:700 7.5pt Bahnschrift,Arial,sans-serif;letter-spacing:.2em;color:#0b68ae;text-transform:uppercase}
h2.t{font-size:19pt;margin:2mm 0 5mm}
.note{background:#fff7e0;border-left:3px solid #f6b63d;padding:3mm 4mm;font-size:9pt;margin-bottom:5mm;border-radius:0 2mm 2mm 0}
ol.use{padding-left:5mm;margin:0 0 4mm}ol.use li{margin:0 0 1.6mm}
.tiles{display:grid;grid-template-columns:repeat(4,1fr);gap:2mm;margin:1mm 0 2mm}
.tile{color:#fff;border-radius:2mm;padding:1.8mm 2.6mm;min-height:13mm;font:600 7.4pt/1.2 Bahnschrift,Arial,sans-serif;display:flex;flex-direction:column;justify-content:space-between}
.tile b{font-size:13pt}
.daylab{font:700 7.5pt Bahnschrift,Arial,sans-serif;letter-spacing:.14em;color:#53657a;text-transform:uppercase;margin:3mm 0 1mm}
.toc{margin:0;padding:0;list-style:none}
.toc li{display:flex;align-items:center;gap:3mm;padding:.9mm 0;border-bottom:1px solid #e3e8ef}
.toc .n{width:5.2mm;height:5.2mm;border-radius:1.2mm;color:#fff;font:700 7.5pt/5.2mm Bahnschrift,Arial,sans-serif;text-align:center;flex:none}
.toc .l{flex:1;font-weight:600}.toc .l small{display:none}
.toc .p{font-weight:700;color:#102c53}
.toc .sep{border:0;font:700 7.5pt Bahnschrift,Arial,sans-serif;letter-spacing:.14em;color:#53657a;text-transform:uppercase;padding-top:2.5mm}
.part{break-before:page}
.part.d1{font-size:9pt}.part.d1 .fiche{margin-bottom:2.8mm;padding:2.6mm 3.6mm}.part.d1 .fiche .ph img{height:28mm}.part.d1 .notes div{height:5.2mm}
.part.d2{font-size:8.6pt}.part.d2 .fiche{margin-bottom:2.2mm;padding:2.2mm 3.2mm}.part.d2 .fiche .ph img{height:22mm}.part.d2 .notes div{height:4.6mm}.part.d2 .fiche h3{font-size:10.5pt}
.part.d3{font-size:8.2pt}.part.d3 .fiche{margin-bottom:1.8mm;padding:1.8mm 3mm}.part.d3 .fiche .ph img{height:16mm}.part.d3 .notes div{height:4mm}.part.d3 .fiche h3{font-size:10pt}.part.d3 .site img{width:8mm;height:8mm}
.band{display:flex;align-items:center;gap:4mm;color:#fff;border-radius:2.5mm;padding:4mm 5mm;margin-bottom:4mm;break-after:avoid}
.band .num{font:700 17pt Bahnschrift,Arial,sans-serif;background:rgba(255,255,255,.18);border-radius:2mm;padding:1mm 3mm}
.band h2{color:#fff;font-size:15pt;line-height:1.15}.band small{display:block;opacity:.85;font-size:7.5pt;letter-spacing:.14em;text-transform:uppercase;margin-top:1mm}
.band .dots{margin-left:auto;display:flex;gap:1.2mm}.band .dots i{width:2.2mm;height:2.2mm;border-radius:50%;background:rgba(255,255,255,.35)}.band .dots i.on{background:#fff}
.fiche{position:relative;background:#f3f6fa;border:1px solid #dfe6ee;border-top:3px solid var(--c);border-radius:2.5mm;padding:3mm 4mm 2.5mm;margin:0 0 3.5mm;break-inside:avoid-column;-webkit-column-break-inside:avoid;page-break-inside:avoid;display:block}
.fiche .k{font:700 7pt Bahnschrift,Arial,sans-serif;letter-spacing:.18em;color:var(--c);text-transform:uppercase;display:flex;align-items:center;gap:1.5mm}
.fiche .k svg{width:3.4mm;height:3.4mm}
.fiche h3{font-size:11.5pt;margin:1mm 0 2mm;line-height:1.2}
.fiche p{margin:0 0 2mm}
.fiche ul{margin:0 0 2mm;padding-left:4.5mm}.fiche li{margin:0 0 1.2mm}
.fiche .ph{float:right;width:58mm;margin:0 0 2mm 5mm}
.fiche .ph img{width:100%;border-radius:2mm;display:block;border:1px solid #dfe6ee}
.fiche .ph small{display:block;font-size:6.5pt;color:#53657a;margin-top:.8mm}
.fiche .fig img{width:100%;max-height:92mm;object-fit:contain;display:block;background:#fff;border-radius:2mm;border:1px solid #dfe6ee}
.kpis{display:flex;gap:3mm;margin:1mm 0 3mm}
.kpi{background:#fff;border:1px solid #dfe6ee;border-radius:2mm;padding:2mm 4mm;font:700 15pt Bahnschrift,Arial,sans-serif;color:var(--c)}
.kpi small{display:block;font:400 7.5pt "Segoe UI",Arial,sans-serif;color:#53657a}
.warn{background:#fdecec;border-left:3px solid #b3261e;padding:2.5mm 3.5mm;border-radius:0 2mm 2mm 0;font-size:9.2pt;margin:2mm 0}
.warn b{color:#b3261e}
.adi{background:#fff4d6;border-left:3px solid #f6b63d;padding:2.5mm 3.5mm;border-radius:0 2mm 2mm 0;font-size:9.2pt;margin:2mm 0}
.adi b{color:#8a520a}
.site{display:flex;align-items:center;justify-content:flex-end;gap:1.5mm;font:700 5.5pt Bahnschrift,Arial,sans-serif;letter-spacing:.1em;color:#b8760f;text-transform:uppercase;margin-top:1.5mm;clear:both}
.site img{width:10mm;height:10mm}
.cols{column-count:2;column-gap:4mm}
.cols .fiche{width:100%}
.fiche.wide{column-span:all}
.fiche .ph{float:none;width:100%;margin:0 0 2mm}
.fiche .ph img{height:34mm;object-fit:cover}
.fiche.wide .ph{float:right;width:58mm;margin:0 0 2mm 5mm}
.fiche.wide .ph img{height:auto}
.rich table{border-collapse:collapse;width:100%;font-size:8.8pt;margin:2mm 0}.rich th{background:#102c53;color:#fff;text-align:left;padding:1.5mm 2.5mm}.rich td{border:1px solid #dfe6ee;padding:1.5mm 2.5mm;background:#fff}
.rich p{margin:0 0 2mm}.rich ol,.rich ul{padding-left:5mm;margin:0 0 2mm}
.steps{counter-reset:s;list-style:none;padding:0}.steps li{counter-increment:s;display:flex;gap:2.5mm;margin:0 0 1.8mm}.steps li:before{content:counter(s);flex:none;width:5mm;height:5mm;border-radius:50%;background:var(--c);color:#fff;font:700 8pt/5mm Bahnschrift,Arial,sans-serif;text-align:center}
.q{margin:0 0 2.5mm;break-inside:avoid}.q b{display:block;margin-bottom:.8mm}
.q span{display:block;padding-left:5mm;position:relative}.q span:before{content:"";position:absolute;left:0;top:1.6mm;width:2.6mm;height:2.6mm;border:1px solid #53657a;border-radius:50%}
.notes{break-inside:avoid;margin:2mm 0 0}.notes h4{font:700 7.5pt Bahnschrift,Arial,sans-serif;letter-spacing:.16em;color:#0b68ae;text-transform:uppercase}
.notes div{height:6mm;border-bottom:1px solid #b9c4d2}
.cc{column-count:2;column-gap:7mm}.cc h3{break-after:avoid}
.corr{break-inside:avoid;margin:0 0 2.6mm;font-size:9pt}.corr b{color:#102c53;display:block}.corr .a{color:#16794a;font-weight:700}.corr small{display:block;color:#53657a}
.corr h3{font-size:11pt;margin:3mm 0 1.5mm;color:#102c53}
table.pa{width:100%;border-collapse:collapse;margin-top:3mm}table.pa th{background:#102c53;color:#fff;text-align:left;padding:2mm 3mm;font-size:8.5pt}table.pa td{border:1px solid #b9c4d2;height:22mm}
.back{page:back;height:297mm;width:210mm;background:#102c53;color:#fff;position:relative;break-before:page}
.back .in{position:absolute;left:24mm;right:24mm;top:100mm}
.back .qr{background:#fff;display:inline-block;padding:3mm;border-radius:3mm;margin-bottom:6mm}.back .qr img{width:42mm;height:42mm;display:block}
.back h2{color:#fff;font-size:20pt;margin-bottom:3mm}.back p,.back li{color:#cfe0f5;font-size:9.5pt}.back a{color:#f6b63d}
.back .legal{position:absolute;left:24mm;right:24mm;bottom:14mm;font-size:7pt;color:#9fb6d3}
'''


def page_rules(parts):
    r = []
    r.append('@page{@bottom-left{content:"Consul Team · support pédagogique · %s";font:7.5pt Bahnschrift,Arial,sans-serif;color:#53657a}@bottom-right{content:counter(page) " / " counter(pages);font:7.5pt Bahnschrift,Arial,sans-serif;color:#53657a}@top-left{content:"LIVRET DE FORMATION APPRENANT";font:700 7pt Bahnschrift,Arial,sans-serif;letter-spacing:.14em;color:#53657a}@top-right{content:"%s";font:700 7.5pt Bahnschrift,Arial,sans-serif;color:#0b68ae}}' % (CODE, CODE))
    r.append('@page cover{@bottom-left{content:none}@bottom-right{content:none}@top-left{content:none}@top-right{content:none}}')
    r.append('@page back{@bottom-left{content:none}@bottom-right{content:none}@top-left{content:none}@top-right{content:none}}')
    for k, lab in parts:
        r.append('@page %s{@top-left{content:"LIVRET DE FORMATION APPRENANT · %s"}}' % (k, lab.replace('"', '')))
    return '\n'.join(r)


class Livret:
    def __init__(self, mods, vis, schemas, tps, qr_dir, dens=None):
        self.dens = dens or {}
        self.mods = {m['id']: m for m in mods}
        self.V = {v['id']: v for v in vis}
        self.schemas = schemas
        self.tps = tps
        self.pages = {}
        self.order = [(d, i) for d, ids in ORDER for i in ids]

    def color(self, k):
        return COLORS[k % len(COLORS)]

    # ---- briques
    def site(self, mid):
        return '<div class="site"><span>Sur le site<br>Module %s</span><img src="assets/qr/m%s.svg" alt="QR code : module %s sur le site"></div>' % (mid, mid, mid)

    def photo(self, vid):
        v = self.V.get(vid)
        if not v: return ''
        return '<div class="ph"><img src="%s" alt="%s"><small>%s · illustration non contractuelle</small></div>' % (e(v['fichier']), e(v['titre']), e(v['legende']))

    def bullets(self, text):
        ss = sents(clean(text))
        if len(ss) >= 3:
            return '<ul>%s</ul>' % ''.join('<li>%s</li>' % e(s) for s in ss)
        return '<p>%s</p>' % e(' '.join(ss))

    def fiche(self, kind, title, body, c, icon='bolt', extra='', site=None, ph='', wide=False):
        return ('<div class="fiche%s" style="--c:%s"><div class="k">%s%s</div><h3>%s</h3>%s%s%s%s</div>'
                % (' wide' if wide else '', c, ico(icon), e(kind), e(title), ph, body, extra, self.site(site) if site else ''))

    def module_fiches(self, mid, c):
        m = self.mods[mid]; out = []
        imgs = list(m.get('images') or [])
        out.append(self.fiche('Objectif', m['title'], '<p><b>%s</b></p>%s' % (e(clean(m['goal'])), ('<p>%s</p>' % e(clean(m['scenario']))) if m.get('scenario') else ''), c, 'target', site=mid, ph=self.photo(imgs.pop(0)) if imgs else ''))
        if m.get('html'):
            out.append(self.fiche('Repères', m['title'], '<div class="rich">%s</div>' % re.sub(r'\s*\[[^\]]*\]', '', m['html']), c, 'book', site=mid, wide=True))
        for t, x in m['sections']:
            if re.search(r'consulter «\s*Repères', x) or len(clean(x)) < 40: continue
            adi = bool(re.match(r'^chez adi', t, re.I))
            ph = self.photo(imgs.pop(0)) if (imgs and len(clean(x)) > 180 and not adi) else ''
            k = clean(x); kp = kpi(k)
            kpis = ('<div class="kpis"><div class="kpi">%s<small>valeur à retenir</small></div></div>' % e(kp)) if (kp and not adi and len(k) < 600) else ''
            body = self.bullets(x)
            warn = ''
            if not adi and DANGER.search(k):
                ws = [s for s in sents(k) if DANGER.search(s)][:1]
                if ws and len(sents(k)) >= 3:
                    warn = '<div class="warn"><b>Attention.</b> %s</div>' % e(ws[0])
            if adi:
                out.append(self.fiche('Chez ADI', t.replace('Chez ADI :', '').replace('Chez ADI', '').strip(' :·—-') or t, '<div class="adi">%s</div>' % self.bullets(x), c, 'fire', site=mid, ph=ph))
            else:
                out.append(self.fiche('À retenir', t, kpis + body + warn, c, icf(t), site=mid, ph=ph))
        for f in [s for s in self.schemas if s.get('module') == mid]:
            out.append(self.fiche('Schéma', f['titre'], '<div class="fig"><img src="%s" alt="%s"></div>' % (e(f['fichier']), e(f['titre'])), c, 'gauge', site=mid, wide=True))
        for fg in (m.get('figures') or []):
            out.append(self.fiche('Schéma', re.split(r'(?<=[a-zéèà])(?=[A-ZÉ])', fg[1])[0], '<div class="fig"><img src="%s" alt="%s"></div>' % (e(fg[0]), e(fg[1])), c, 'gauge', site=mid, wide=True))
        if m.get('decision'):
            out.append(self.fiche('Décision à prendre', 'Que faites-vous ?', '<p><b>%s</b></p><p style="color:#53657a">Notez votre réponse, puis comparez-la avec le corrigé en fin de livret.</p><div class="notes"><div></div><div></div><div></div></div>' % e(clean(m['decision'])), c, 'help', site=mid))
        if m.get('check'):
            out.append(self.fiche('Avant d’agir', 'Je vérifie', '<ul class="chk">%s</ul>' % ''.join('<li>☐ %s</li>' % e(x) for x in m['check']), c, 'lock', site=mid))
        if mid == 16:
            for t in self.tps:
                body = ('<p><b>Matériel.</b> %s</p><p><b>Avant.</b> %s</p><ol class="steps">%s</ol><div class="warn"><b>Arrêt immédiat.</b> %s</div><p><b>Après.</b> %s</p>'
                        % (e(t['material']), e(t['before']), ''.join('<li>%s</li>' % e(s) for s in t['steps']), e(t['stop']), e(t['after'])))
                out.append(self.fiche('TP · ' + t['scope'], t['id'].replace('TP-', 'TP ') + ' · ' + t['title'], body, c, 'tools', site=mid, wide=True))
        qs = [q for q in m.get('questions', []) if (q.get('type') or 's') == 's'][:3]
        if qs:
            body = ''.join('<div class="q"><b>%d. %s</b>%s</div>' % (n + 1, e(clean(q['q'])), ''.join('<span>%s. %s</span>' % ('ABCDEFGH'[j], e(clean(o))) for j, o in enumerate(q['options']))) for n, q in enumerate(qs))
            out.append(self.fiche('Pour vérifier', 'Questions flash', body, c, 'spark', site=mid))
        return out, qs

    def build(self, toc=None):
        toc = toc or {}
        parts_pages = []; body = []; corr = []; tiles = []; tocrows = []
        k = 0
        for day, ids in ORDER:
            tocrows.append('<li class="sep">%s</li>' % e(DAYLAB[day]))
            tiles.append('<div class="daylab">%s</div><div class="tiles">' % e(DAYLAB[day]))
            for mid in ids:
                m = self.mods[mid]; c = self.color(k); k += 1
                name = 'p%d' % mid
                fiches, qs = self.module_fiches(mid, c)
                parts_pages.append((name, '%d · %s' % (mid, m['title'])))
                dots = ''.join('<i class="on"></i>' if j <= (k - 1) * 10 // len(self.order) else '<i></i>' for j in range(10))
                band = '<div class="band" style="background:%s"><div class="num">%02d</div><div><h2>%s</h2><small>%d fiches · %s</small></div><div class="dots">%s</div></div>' % (c, mid, e(m['title']), len(fiches), e(m.get('scope') or ''), dots)
                notes = '<div class="notes"><h4>Mes notes</h4><div></div><div></div><div></div></div>'
                body.append('<section class="part d%d" id="p%d" style="page:%s">%s<div class="cols">%s%s</div></section>' % (self.dens.get(mid, 0), mid, name, band, ''.join(fiches), notes))
                tiles.append('<div class="tile" style="background:%s"><b>%02d</b>%s</div>' % (c, mid, e(m['title'])))
                tocrows.append('<li><span class="n" style="background:%s">%d</span><span class="l">%s<small>%d fiches</small></span><span class="p">%s</span></li>' % (c, mid, e(m['title']), len(fiches), toc.get('p%d' % mid, '')))
                if qs:
                    corr.append('<h3>%d · %s</h3>' % (mid, e(m['title'])))
                    for n, q in enumerate(qs):
                        corr.append('<div class="corr"><b>%d. %s</b><span class="a">Réponse : %s. %s</span><small>%s</small></div>' % (n + 1, e(clean(q['q'])), 'ABCDEFGH'[q['correct']], e(clean(q['options'][q['correct']])), e(clean(q.get('why', '')))))
                if m.get('decision'):
                    corr.append('<div class="corr"><b>Décision : %s</b><span class="a">Réponse : %s</span></div>' % (e(clean(m['decision'])), e(clean(m.get('answer', '')))))
            tiles.append('</div>')
        tocrows.append('<li class="sep">En fin de livret</li>')
        for key, lab in (('corr', 'Corrigés des questions flash et des décisions'), ('plan', 'Mon plan d’action'), ('loin', 'Pour aller plus loin')):
            tocrows.append('<li><span class="n" style="background:#102c53">·</span><span class="l">%s</span><span class="p">%s</span></li>' % (lab, toc.get(key, '')))
        cover = ('<section class="cover"><div class="bandes"></div><div class="in"><img class="logo" src="assets/img/logo-consulteam-groupe.png" alt="Consulteam Groupe"><div class="kick">LIVRET DE FORMATION APPRENANT · %s</div><h1>%s</h1><div class="sub">%s</div></div><div class="when"><b>%s</b><br>%s</div><div class="qr"><img src="assets/qr/home.svg" alt="QR code : accueil du site"><b>Le site de la formation</b></div><div class="legal">Conception et ingénierie pédagogique : Benoît Deflandre · Contact et informations : formation@consul-team.fr · %s</div></section>'
                 % (CODE, e(TITRE), e(SOUS), e(DATES), e(LIEU), EDITION))
        use = ('<section class="pg" id="use"><div class="kicker">Avant de commencer</div><h2 class="t">Comment utiliser ce livret</h2>'
               '<div class="note"><b>Ce livret accompagne la formation.</b> Il ne remplace ni les textes en vigueur, ni les consignes de votre employeur, ni les notices des fabricants. Il ne constitue pas une attestation : le titre d’habilitation est délivré par l’employeur.</div>'
               '<ol class="use"><li><b>Suivez les fiches</b> au fil de l’animation : elles reprennent les points projetés.</li><li><b>Notez à la marge</b> : un cadre « Mes notes » termine chaque partie.</li><li><b>Scannez le QR code</b> d’une fiche : il ouvre le module correspondant sur le site, à lire en parallèle.</li><li><b>Répondez aux questions flash</b>, puis comparez avec les corrigés en fin de livret.</li><li><b>Complétez le plan d’action</b> : une idée retenue, une action à porter.</li></ol>'
               '<div class="kicker">Le parcours en un coup d’œil</div>%s'
               '<p style="margin-top:5mm">Le site de la formation reste disponible après la session : <b>%s</b></p></section>' % (''.join(tiles), e(BASE.replace('https://', ''))))
        sommaire = '<section class="pg" id="som"><div class="kicker">Dans ce livret</div><h2 class="t">Sommaire</h2><ul class="toc">%s</ul></section>' % ''.join(tocrows)
        corr_s = '<section class="pg" id="corr"><div class="kicker">Corrigés</div><h2 class="t">Questions flash et décisions</h2><div class="cc">%s</div></section>' % ''.join(corr)
        plan = ('<section class="pg" id="plan"><div class="kicker">À remplir en fin de formation</div><h2 class="t">Mon plan d’action</h2><p>Une idée retenue, une action que je peux mettre en œuvre, une proposition que je porte.</p>'
                '<table class="pa"><tr><th>Ce que je retiens</th><th>Ce que je change ou propose</th><th>Avec qui, pour quand ?</th></tr>%s</table>'
                '<div class="notes" style="margin-top:8mm"><h4>Mes notes</h4>%s</div></section>' % ('<tr><td></td><td></td><td></td></tr>' * 5, '<div></div>' * 8))
        back = ('<section class="back" id="loin"><div class="in"><div class="qr"><img src="assets/qr/home.svg" alt="QR code : accueil du site"></div><h2>Pour aller plus loin</h2><p>Le site de la formation (parcours, schémas, glossaire, évaluations, arbres de décision) reste accessible après la session :</p><p><a>%s</a></p><ul><li>Scannez le QR code ou ouvrez l’adresse sur téléphone, tablette ou ordinateur.</li><li>Les pages se lisent aussi hors connexion après une première visite.</li></ul></div>'
                '<div class="legal">Livret de formation apprenant — %s · %s. Ce document est un support pédagogique : il ne remplace pas les textes en vigueur (référentiel INRS, NF C 18-510), ni les consignes de l’employeur. Les illustrations sont générées et non contractuelles. Aucune norme payante n’est reproduite. Conception et ingénierie pédagogique : Benoît Deflandre.</div></section>' % (e(BASE.replace('https://', '')), CODE, EDITION))
        css = CSS + page_rules(parts_pages) + '\n.fiche li.chk,ul.chk{list-style:none;padding-left:0}'
        doc = '<!doctype html><html lang="fr"><head><meta charset="utf-8"><title>Livret de formation apprenant — %s</title><style>%s</style></head><body>%s%s%s%s%s%s%s</body></html>' % (CODE, css, cover, use, sommaire, ''.join(body), corr_s, plan, back)
        return doc
