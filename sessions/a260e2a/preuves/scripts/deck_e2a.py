# -*- coding: utf-8 -*-
"""Mode animation A260E2A : diaporama statique modelé sur les supports « Travail en hauteur »
(sections minutées, notes formateur, fragments, QCM collectifs, QR et mention téléphone sur chaque diapo)."""
import re, json, html as H
from bs4 import BeautifulSoup
import skin

ICO = json.loads(re.search(r'var ICO=(\{.*?\});', skin.ICONS_JS, re.S).group(1))
BASE = 'https://ben2flandre-coder.github.io/consulteam-academy/sessions/a260e2a/'

def e(x): return H.escape(str(x), quote=True)
def ico(n, cls='ic'):
    return '<svg class="%s" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">%s</svg>' % (cls, ICO.get(n, ICO['bolt']))
KEYS = [('chez adi','fire'),('danger','alert'),('risque','alert'),('batter','battery'),('alimentation','battery'),('source','battery'),('consign','lock'),('vérif','gauge'),('mesur','gauge'),('essai','gauge'),('zone','ruler'),('voisinage','ruler'),('distance','ruler'),('secours','cross'),('accident','cross'),('alerte','bell'),('habilit','badge'),('titre','badge'),('symbole','badge'),('rôle','users'),('qui fait','users'),('dépann','wrench'),('maintenance','wrench'),('remplac','wrench'),('décision','target'),('situation','target'),('objectif','target'),('visite','clip'),('catégor','building'),('appareil','plug'),('tableau','plug')]
def icf(t):
    t = t.lower()
    for k, v in KEYS:
        if k in t and v in ICO: return v
    return 'bolt'

TAG = re.compile(r'\s*\[[^\]]*\]')
def clean(t): return re.sub(r'\s+', ' ', TAG.sub('', t)).strip()
def tags(t): return sorted(set(x.strip() for g in re.findall(r'\[([^\]]*)\]', t) for x in g.split(',') if x.strip()))
def sents(x): return [s for s in re.split(r'(?<=[.!?])\s+(?=[A-ZÀÂÉÈÊÎÔÛÇ«(0-9])', x.strip()) if s]

DANGER = re.compile(r'(interdit|jamais|danger|ne pas |ne doit pas|ne peut pas|mortel|brûlure|arc |électrisation|électrocution|chute|risque)', re.I)
KPI = re.compile(r'(\d[\d  ,.]*\s?(?:kV|V|mA|kA|A|m|cm|mm|Hz|min|h|s|%|ans|mois|jours))(?![\w])')

def kpi(t):
    m = KPI.search(t)
    return m.group(1).strip() if m else None

# ---------------------------------------------------------------- séquences / minutes
# (jour, id module ou clé spéciale, minutes) — 21 h = 3 × 7 h ; à valider avec le formateur [R]
J1 = [(1,30),(2,50),(3,30),(4,40),(18,40),(5,40),(6,30),(7,30),(8,60),(23,20)]
J2 = [(19,60),(20,50),(21,60),(22,50),(10,40),(11,60),(17,75)]
CARTE = [9,12,13,14,15]
DAYS = {1: ('Jour 1 · lundi 14 décembre', 'Comprendre et se situer', ['Mission, titres d’habilitation, danger électrique', 'Zones et voisinage (B0, H0, H0V)', 'BS, BE Manœuvre, secours et incendie']),
        2: ('Jour 2 · mardi 15 décembre', 'Le métier d’ADI en pratique', ['Appareillage d’un tableau : reconnaître, équilibrer', 'Remplacer, installer', 'BR, consignation BC, systèmes de sécurité incendie']),
        3: ('Jour 3 · mercredi 16 décembre', 'Pratiquer et valider', ['Travaux pratiques individualisés', 'Évaluations théorique et pratique', 'Avis après formation, bilan'])}

class Deck:
    def __init__(self, mods, vis, tps, evals_cfg):
        self.M = {m['id']: m for m in mods}
        self.V = {v['id']: v for v in vis}
        self.tps = tps
        self.out = []
        self.sec = ''
        self.n = 0

    # ---- briques
    def qr(self, mid=None, label=None):
        src = 'assets/qr/m%s.svg' % mid if mid else 'assets/qr/home.svg'
        url = BASE + ('parcours.html#m%s' % mid if mid else '')
        lab = label or ('Module %s' % mid if mid else 'Accueil')
        return ('<div class="qb"><img src="%s" alt="QR code : %s sur le site" width="110" height="110" data-nozoom><span><b>Suivre sur votre téléphone</b>%s · scannez ou ouvrez<br><a href="%s" target="_blank" rel="noopener">%s</a></span></div>'
                % (src, e(lab), e(lab), ('parcours.html#m%s' % mid) if mid else 'index.html', 'Parcours' if mid else 'Accueil'))

    def img(self, vid, cls=''):
        v = self.V.get(vid)
        if not v: return ''
        return '<figure class="vis %s"><img src="%s" alt="%s" loading="lazy" data-nozoom><figcaption>%s</figcaption></figure>' % (cls, e(v['fichier']), e(v['titre']), e('Illustration générée — non contractuelle.'))

    def slide(self, inner, title, mid=None, kind='', min_=None, note='', qrlab=None, src=None, style=''):
        self.n += 1
        a = ' data-sec="%s"' % e(self.sec) + (' style="%s"' % style if style else '')
        if min_: a += ' data-min="%s"' % min_
        if src:  # traçabilité : sources déclarées dans le texte
            note += ('<p><em>Sources : %s. Contenu à relire par le formateur [R].</em></p>' % e(', '.join(src))) if src else ''
        nt = '<div class="note">%s</div>' % note if note else ''
        self.out.append('<section class="slide %s"%s data-title="%s">%s%s%s</section>' % (kind, a, e(title), self.qr(mid, qrlab), inner, nt))

    # ---- diapos types
    FB = ['TC01','TC02','TC03','TC04','TC05','TC06','TC07','TC08','TC09','PC01','PC02','PC03']
    def imgs(self, m):
        l = [i for i in (m.get('images') or []) if i in self.V]
        if len(l) < 4:  # compléter pour que chaque diapositive de contenu ait un visuel
            k = m['id'] % len(self.FB)
            l += [self.FB[(k + j) % len(self.FB)] for j in range(4 - len(l)) if self.FB[(k + j) % len(self.FB)] not in l]
        return l

    def opener(self, m, minutes, day):
        imgs = self.imgs(m)
        v = self.V.get(imgs[0]) if imgs else None
        bg = ''
        sty = "--bgimg:url('%s')" % ('../' + v['fichier']) if v else ''
        niv = ''.join('<span class="pill">%s</span>' % e({'TC':'Tous niveaux','Tous':'Tous niveaux'}.get(n, n)) for n in (m.get('niveaux') or []))
        inner = ('<div class="mhead"%s><span class="bigico">%s</span><span class="k">Module %s · Jour %s · %s min</span><h1>%s</h1><p class="lead">%s</p><div class="pills">%s</div>'
                 '<p class="links"><a href="parcours.html#m%s">Ouvrir le parcours</a><a href="cours/index.html">Cours de base</a></p>%s</div>'
                 % (bg, ico(icf(m['title'])), m['id'], day, minutes, e(m['title']), e(clean(m['goal'])), niv, m['id'],
                    ('<div class="sit frag"><b>Situation de départ.</b> %s <i>Que faites-vous ?</i></div>' % e(clean(m['scenario']))) if m.get('scenario') else ''))
        note = '<p><strong>%s min.</strong> Annoncer l’objectif, le périmètre (%s) et le lien avec le métier d’ADI sécurité. Les stagiaires suivent sur leur téléphone via le QR (page « Parcours » du module %s).</p>' % (minutes, e(m.get('scope', '')), m['id'])
        self.slide(inner, 'Module %s — %s' % (m['id'], m['title']), m['id'], 'mod', minutes, note, src=tags(m['goal']), style=sty)

    def situation(self, m):
        if not m.get('scenario'): return
        im = ''
        imgs = m.get('images') or []
        if imgs: im = '<div class="figs">%s</div>' % self.img(imgs[0])
        inner = ('<span class="k">Situation de départ</span><h2>Que faites-vous ?</h2><div class="split"><div class="txt"><div class="callout warn big">%s</div>'
                 '<p class="frag lead">Gardez cette situation en tête : nous y revenons à la fin de la séquence.</p></div>%s</div>' % (e(clean(m['scenario'])), im))
        self.slide(inner, 'Situation — ' + m['title'], m['id'], '', None, '<p>Laisser 1 à 2 minutes de réponses libres avant d’avancer ; noter les idées au tableau.</p>', src=tags(m['scenario']))

    def tiles(self, items, cols=None):
        n = len(items)
        c = cols or ('cols3' if n == 3 else ('cols2' if n in (2, 4) else ('cols3' if n > 4 else 'cols2')))
        h = ''
        for ti, t in enumerate(items):
            k = kpi(t)
            if DANGER.search(t) and not k:
                h += '<div class="callout danger frag">%s<span>%s</span></div>' % (ico('alert', 'ic sm'), e(t))
            else:
                h += '<div class="tile acc frag">%s<p>%s</p></div>' % (('<b class="kpi">%s</b>' % e(k)) if k else '<span class="num">%d</span>' % (ti + 1), e(t))
        return '<div class="%s">%s</div>' % (c, h)

    def content(self, m, title, text, adi=False, image=None, lead_chunks=True):
        raw = text
        ss = sents(clean(text))
        if not ss: return
        # une diapositive par section : phrase d'ouverture + 4 encarts maximum (chiffres et dangers d'abord) ; le reste va aux notes
        lead, others = ss[0], ss[1:]
        keep = []
        if len(others) > 4:
            pr = sorted(range(len(others)), key=lambda i: (0 if kpi(others[i]) else (1 if DANGER.search(others[i]) else 2), i))[:4]
            keep = [others[i] for i in sorted(pr)]
        else:
            keep = others
        extra = [s for s in others if s not in keep]
        chunks = [[lead] + keep]
        for i, ch in enumerate(chunks):
            lead, rest = ch[0], ch[1:]
            t = title + (' (%d/%d)' % (i + 1, len(chunks)) if len(chunks) > 1 else '')
            ic = 'fire' if adi else icf(title)
            kick = 'Chez ADI sécurité' if adi else 'Module %s' % m['id']
            body = '<p class="big lead%s">%s</p>' % (' leadadi' if adi else '', e(lead))
            if rest: body += self.tiles(rest)
            fig = '<div class="figs">%s</div>' % self.img(image) if (image and i == 0) else ''
            inner = '<span class="k">%s</span><h2>%s%s</h2>' % (e(kick), ico(ic, 'ic h'), e(t))
            inner += ('<div class="split"><div class="txt">%s</div>%s</div>' % (body, fig)) if fig else body
            note = '<p>Lire la première phrase, puis révéler les encarts un à un (→ ou Espace) en demandant aux stagiaires de les reformuler. Les chiffres encadrés sont à contrôler dans la source avant la session.</p>' + ('<p><strong>À l’oral, en complément (détail dans la page du module) :</strong> ' + e(' '.join(extra)) + '</p>' if extra else '')
            self.slide(inner, t, m['id'], 'adi' if adi else '', None, note, src=tags(raw))

    def figure(self, m, f):
        inner = '<span class="k">Schéma · module %s</span><h2>%s</h2><figure class="vis svg"><img src="%s" alt="%s" data-nozoom></figure>' % (m['id'], e(re.split(r'[:.]', f[1])[0]), e(f[0]), e(f[1]))
        self.slide(inner, f[1][:70], m['id'], 'planche', None, '<p>%s Schéma de principe, non à l’échelle ; il ne remplace ni la notice du constructeur ni les prescriptions.</p>' % e(f[1]))

    def decision(self, m):
        ck = ''
        if m.get('check'):
            n = len(m['check'])
            ck = '<h3 class="frag">%sAvant d’agir</h3><div class="%s">%s</div>' % (ico('shield', 'ic h'), 'cols5' if n >= 5 else 'cols3', ''.join('<div class="tile acc frag"><span class="chk">✓</span><p>%s</p></div>' % e(clean(c)) for c in m['check']))
        if not m.get('decision') and not ck: return
        d = ''
        if m.get('decision'):
            d = ('<div class="callout warn big">%s</div><div class="callout ok big frag"><b>Réponse.</b> %s</div>' % (e(clean(m['decision'])), e(clean(m['answer']))))
        self.slide('<span class="k">Décision à prendre</span><h2>%sMettons-nous à la place de l’habilité</h2>%s%s' % (ico('target', 'ic h'), d, ck), 'Décision — ' + m['title'], m['id'], 'dec', None,
                   '<p>Faire voter à main levée avant de révéler la réponse, reprendre la situation de départ, puis dérouler la liste des réflexes et demander à un stagiaire de la rejouer.</p>', src=tags((m.get('decision') or '') + ' ' + (m.get('answer') or '')))

    def qcm(self, qs, label, mid, many=False):
        for i, q in enumerate(qs):
            opts = ''.join('<button type="button" class="opt" data-j="%d"><span class="l">%s</span><span>%s</span></button>' % (j, 'ABCD'[j], e(clean(o))) for j, o in enumerate(q['options']))
            inner = ('<span class="k">%s · question %d sur %d</span><h2>%s</h2><div class="opts" data-ok="%d">%s</div><p class="qexp" aria-live="polite" hidden>%s</p>'
                     % (e(label), i + 1, len(qs), e(clean(q['q'])), q['correct'], opts, e(clean(q.get('why', '')))))
            self.slide(inner, 'QCM — %s %d' % (label, i + 1), mid, 'qcm', None, '<p>Réponse collective : main levée, puis toucher la réponse choisie par la salle. Reprendre oralement chaque erreur. Réponse attendue : %s. %s</p>' % ('ABCD'[q['correct']], e(clean(q.get('why', '')))), src=tags(q.get('why', '')))

    # ---- module complet
    def html_blocks(self, m):
        soup = BeautifulSoup(m['html'], 'html.parser')
        res = []
        for el in soup.find_all(recursive=False):
            if el.name == 'p': res.append(('p', clean(el.get_text(' '))))
            elif el.name in ('ol', 'ul'):
                its = []
                for n, li in enumerate(el.find_all('li', recursive=False)):
                    b = li.find('b')
                    ti = clean(b.get_text()).rstrip('.:') if b else 'Étape %d' % (n + 1)
                    tx = clean(li.get_text(' '))
                    if b and tx.startswith(clean(b.get_text())): tx = tx[len(clean(b.get_text())):].strip()
                    its.append((ti, tx))
                res.append((el.name, its))
            elif el.name == 'table': res.append(('table', str(el)))
            else: res.append(('p', clean(el.get_text(' '))))
        return res

    def steps_slide(self, m, its, title, n0=0):
        for i in range(0, len(its), 3):
            ch = its[i:i + 3]
            tl = ''.join('<div class="tile acc frag"><b class="n">%d</b><h3>%s</h3><p>%s</p></div>' % (n0 + i + j + 1, e(t), e(x)) for j, (t, x) in enumerate(ch))
            self.slide('<span class="k">Module %s · pas à pas</span><h2>%s%s</h2><div class="cols3">%s</div>' % (m['id'], ico(icf(title), 'ic h'), e(title), tl), '%s (%d/%d)' % (title, i // 3 + 1, (len(its) + 2) // 3), m['id'], '', None, '<p>Dérouler les étapes une à une ; demander « que se passe-t-il si on saute cette étape ? ».</p>', src=tags(m.get('source', '')))

    def module(self, mid, minutes, day):
        m = self.M[mid]
        self.sec = 'J%d · M%s · %s' % (day, mid, m['title'])
        self.opener(m, minutes, day)
        imgs = self.imgs(m)
        if m.get('html'):
            np = 0
            for kind, val in self.html_blocks(m):
                if kind == 'p':
                    np += 1
                    self.content(m, 'Repères' if np == 1 else 'À retenir', val, False, imgs[np % len(imgs)])
                elif kind in ('ol', 'ul'):
                    self.steps_slide(m, val, 'Les étapes' if kind == 'ol' else 'Points clés')
                else:
                    self.slide('<span class="k">Module %s · en un coup d’œil</span><h2>%sTableau de synthèse</h2><div class="tbl">%s</div>' % (m['id'], ico('clip', 'ic h'), val), 'Tableau — ' + m['title'], m['id'], 'tab', None, '<p>Lire une ligne, demander aux stagiaires de la compléter avant de révéler la suivante.</p>')
        for i, (st, tx) in enumerate(m.get('sections', [])):
            adi = st.startswith('Chez ADI') or mid == 17
            self.content(m, st, tx, adi, (['SI0%d' % (1 + (i + mid) % 6)] if adi and 'SI01' in self.V else [imgs[(i + 1) % len(imgs)]])[0])
        for f in m.get('figures', []): self.figure(m, f)
        if mid == 16:
            self.tp_slides(m)
        self.decision(m)
        pool = [q for q in (m.get('exercices') or []) if q.get('type', 's') == 's'] + [q for q in m['questions'] if q.get('type', 's') == 's']
        seen, qs = set(), []
        for q in pool:
            if q['q'] not in seen and len(qs) < 2: seen.add(q['q']); qs.append(q)
        self.qcm(qs, 'Module %s' % mid, mid)
        self.m_pool = getattr(self, 'm_pool', {}); self.m_pool[mid] = [q for q in m['questions'] if q.get('type', 's') == 's']

    def tp_slides(self, m):
        for t in self.tps:
            steps = ''.join('<div class="tile acc frag"><b class="n">%d</b><p>%s</p></div>' % (i + 1, e(s)) for i, s in enumerate(t['steps']))
            self.slide('<span class="k">Travaux pratiques · %s</span><h2>%s%s</h2><div class="split"><div class="txt"><p><b>Périmètre :</b> %s<br><b>Matériel :</b> %s</p><p class="lead">%s</p></div><div class="callout danger"><b>STOP si</b> %s</div></div><div class="cols2 sm">%s</div>' % (e(t['id']), ico('wrench', 'ic h'), e(t['title']), e(t['scope']), e(t['material']), e(t['before']), e(t['stop']), steps), 'TP %s — %s' % (t['id'], t['title']), m['id'], '', None, '<p>Le formateur fait l’appel du matériel, rappelle la consigne STOP, puis observe l’exécution individuelle avec la grille de preuves.</p>')
            ev = ''.join('<div class="tile acc frag"><span class="chk">✓</span><p>%s</p></div>' % e(x) for x in t['evidence'])
            self.slide('<span class="k">TP %s · preuves observées</span><h2>%sCe que le formateur observe</h2><div class="cols2">%s</div><div class="callout ok frag"><b>Retour d’expérience.</b> %s</div>' % (e(t['id']), ico('eye', 'ic h'), ev, e(t['after'])), 'TP %s — preuves' % t['id'], m['id'], '', None, '<p>Debrief individuel de 5 minutes par stagiaire.</p>')

    # ---- jours / ouverture / fin
    def day_slide(self, d, seq):
        lab, ti, pts = DAYS[d]
        self.sec = 'J%d · Ouverture' % d
        rows = ''.join('<li><b>M%s</b> %s <span>%s min</span></li>' % (i, e(self.M[i]['title']), mn) for i, mn in seq if i in self.M)
        pts_h = ''.join('<div class="tile acc frag">%s<p>%s</p></div>' % (ico('bolt', 'ic sm'), e(p)) for p in pts)
        self.slide('<span class="k">%s</span><h2>%s</h2><div class="cols3">%s</div>%s' % (e(lab), e(ti), pts_h, ('<ul class="seq frag">%s</ul>' % rows) if rows else ''), lab, None, 'jour', 10,
                   '<p>Rappeler l’objectif du jour, les horaires, et la règle : téléphone pour suivre la formation (QR de chaque diapositive), pas pour autre chose.</p>', qrlab='Accueil')

    def bilan(self, d, ids):
        self.sec = 'J%d · Bilan' % d
        pool = []
        for i in ids:
            qs = [q for q in self.M[i]['questions'] if q.get('type', 's') == 's'][-2:]
            pool += [(i, q) for q in qs[:1]]
        pool = pool[:6]
        self.slide('<span class="k">Bilan du jour %d</span><h2>%sRéactivation en %d questions</h2><p class="lead">Une question par séquence de la journée. Réponse collective, correction immédiate.</p>' % (d, ico('spark', 'ic h'), len(pool)), 'Bilan jour %d' % d, None, 'jour', 15, '<p>Annoncer le score collectif visé (à fixer avec l’organisme).</p>', qrlab='Évaluation')
        for k, (i, q) in enumerate(pool):
            self.qcm([q], 'Bilan J%d' % d, i)

    def build(self):
        M = self.M
        # ouverture
        self.sec = 'J1 · Accueil'
        imgs = M[1].get('images') or []
        self.n += 1
        self.out.append('<section class="slide cover" data-sec="%s" data-min="25" data-title="Habilitation électrique : formation initiale">%s<img class="logo" src="assets/img/logo-consulteam-groupe-valto.png" alt="Consulteam Groupe · Groupe Valto"><span class="tag2">A260E2A · 21 heures · 3 jours</span><h1>Habilitation électrique<br>formation initiale</h1><p class="meta">14, 15 et 16 décembre 2026 · La Seyne-sur-Mer · pour les équipes d’ADI sécurité</p><p class="meta2">B0 · H0 · H0V · BS · BE Manœuvre · BR · BC · symboles selon désignation</p><div class="note"><p><strong>Accueil, 30 min.</strong> Émargement, tour de table : tâches réelles de chacun (détection, mise en sécurité, alimentation, maintenance). Présenter les trois jours et la règle du téléphone (QR).</p></div></section>' % (e(self.sec), self.qr(None, 'Accueil')))
        self.slide('<span class="k">Comment suivre</span><h2>%sVotre téléphone est un second écran</h2><div class="cols3"><div class="tile acc frag"><b class="n">1</b><h3>Scannez</h3><p>Chaque diapositive porte un QR en bas à droite : il ouvre la page du module en cours.</p></div><div class="tile acc frag"><b class="n">2</b><h3>Lisez et zoomez</h3><p>Schémas à agrandir, cas, questions d’entraînement : tout est dans la page « Parcours ».</p></div><div class="tile acc frag"><b class="n">3</b><h3>Revenez en salle</h3><p>Le score et vos réponses restent sur votre appareil. Pensez à ajouter le site à l’écran d’accueil.</p></div></div><div class="callout warn frag">Sans téléphone ? Le formateur donne la page : <b>Parcours → module → section</b>. Le site fonctionne hors connexion après une première ouverture.</div>' % ico('users', 'ic h'), 'Suivre sur votre téléphone', None, '', None, '<p>Faire scanner le QR de l’accueil par tous (2 minutes), vérifier que chacun accède au parcours. Proposer le QR au vidéoprojecteur : touche Q pour l’agrandir.</p>', qrlab='Accueil')
        goals = [m for m in (1, 4, 5, 7, 11, 17)]
        gt = ''.join('<div class="tile acc frag">%s<b>%s</b><p>%s</p></div>' % (ico(icf(M[i]['title']), 'ic sm'), e(M[i]['title']), e(clean(M[i]['goal']))) for i in goals)
        self.slide('<span class="k">Programme</span><h2>%sCe que vous saurez faire à la fin des trois jours</h2><div class="cols3">%s</div>' % (ico('target', 'ic h'), gt), 'Objectifs de la formation', None, '', None, '<p>Objectifs repris des fiches de module. Public : personnels spécialistes des installations de systèmes de sécurité incendie (ADI sécurité). Programme et symboles à confirmer [R].</p>', qrlab='Parcours')
        # déroulé
        rows = ''
        for d, seq in ((1, J1), (2, J2)):
            rows += '<tr><td><b>J%d</b></td><td>%s</td></tr>' % (d, ' · '.join('M%s' % i for i, _ in seq))
        self.slide('<span class="k">Programme</span><h2>%sTrois jours, 21 heures dont 7 de pratique</h2><div class="cols3"><div class="tile acc frag"><span class="pill">Lundi 14 déc.</span><h3>Comprendre et se situer</h3><p>Mission et titres, danger, rôles · zones et voisinage · BS, BE Manœuvre · secours et incendie</p></div><div class="tile acc frag"><span class="pill">Mardi 15 déc.</span><h3>Le métier d’ADI en pratique</h3><p>Appareillage et équilibrage · remplacer, installer · BR, BC · systèmes de sécurité incendie</p></div><div class="tile acc frag"><span class="pill">Mercredi 16 déc.</span><h3>Pratiquer et valider</h3><p>TP individualisés · évaluations théorique et pratique · avis après formation</p></div></div><p class="frag lead">Les horaires précis et les modules « à la carte » (B1, B2, H1, H2, HC, HE, BE mesurage) se calent sur les symboles réellement désignés par ADI sécurité.</p>' % ico('badge', 'ic h'), 'Déroulé des trois jours', None, '', None, '<p>Temps indicatifs par séquence : voir le chrono en haut à droite, il se règle sur la séquence en cours. À ajuster avec le responsable ADI sécurité [R].</p>', qrlab='Parcours')
        # jours
        for d, seq in ((1, J1), (2, J2)):
            self.day_slide(d, seq)
            for mid, mn in seq:
                self.module(mid, mn, d)
            self.bilan(d, [i for i, _ in seq if i in self.M][:6])
        self.day_slide(3, [(16, 270)])
        # à la carte
        self.sec = 'J3 · À la carte'
        self.slide('<span class="k">À la carte</span><h2>%sCompléments selon les symboles désignés</h2><div class="cols3"><div class="tile acc frag"><b>Module 9</b><p>Travaux hors tension B1 · B1V · B2 · B2V</p></div><div class="tile acc frag"><b>Modules 12 à 14</b><p>H1 · H2 · HC · HE Manœuvre</p></div><div class="tile acc frag"><b>Module 15</b><p>BE mesurage, vérification, essai</p></div></div><p class="lead frag">Ces modules ne sont déroulés que si l’employeur a désigné les symboles correspondants ; ils se prennent sur le temps des TP du jour 3.</p>' % ico('badge', 'ic h'), 'Modules à la carte', None, 'jour', 5, '<p>Confirmer avec ADI sécurité la liste des symboles visés avant de lancer ces modules [R].</p>', qrlab='Parcours')
        for mid in CARTE: self.module(mid, 20, 3)
        self.module(16, 270, 3)
        self.sec = 'J3 · Évaluations'
        self.slide('<span class="k">Évaluations</span><h2>%sTrois évaluations, une décision de l’employeur</h2><div class="cols3"><div class="tile acc frag"><b class="n">1</b><h3>Théorie</h3><p>QCM par niveau sur la plateforme (page « Évaluation »), correction immédiate.</p></div><div class="tile acc frag"><b class="n">2</b><h3>Pratique</h3><p>Grille de preuves observées par le formateur, par symbole.</p></div><div class="tile acc frag"><b class="n">3</b><h3>Avis</h3><p>Avis du formateur transmis à l’employeur, qui délivre le titre d’habilitation.</p></div></div><div class="callout warn frag">Ni la formation ni le score ne délivrent le titre : il est établi et signé par l’employeur, selon l’avis rendu et la désignation des symboles [R].</div>' % ico('badge', 'ic h'), 'Évaluations', None, '', 100, '<p>Évaluation théorique : 16 questions par niveau, seuil proposé 70 % [R]. Évaluation pratique : grille TP. Avis individuel à renseigner après la session.</p>', qrlab='Évaluation')
        self.qr_eval = True
        self.sec = 'J3 · Clôture'
        self.slide('<span class="k">Clôture</span><h2>%sBilan de la formation et avis</h2><div class="cols3"><div class="tile acc frag"><b>Ce que je retiens</b><p>Un geste, une règle, un réflexe à appliquer dès lundi.</p></div><div class="tile acc frag"><b>Ce qui me manque</b><p>Une situation de mon métier que je ne sais pas encore traiter.</p></div><div class="tile acc frag"><b>Mon avis</b><p>Questionnaire de satisfaction à remplir avant de partir.</p></div></div>' % ico('users', 'ic h'), 'Bilan de la formation', None, '', 40, '<p>Recueillir les attentes non couvertes et le questionnaire d’avis après formation.</p>', qrlab='Accueil')
        self.n += 1
        self.out.append('<section class="slide fin" data-sec="J3 · Clôture" data-title="Merci">%s<span class="k">Fin de la formation</span><h1>Merci, et prudence sur les installations</h1><p class="lead">Les pages du site restent disponibles : parcours, cours, évaluations, galerie de schémas.</p><p class="meta">formation@consul-team.fr · Consulteam Security · La Seyne-sur-Mer</p></section>' % self.qr(None, 'Accueil'))
        return '\n'.join(self.out)

CSS = r'''
:root{--n:#102c53;--b:#0b68ae;--y:#f6b63d;--i:#16273d;--m:#53657a;--l:#cbd5e1;--bg:#f3f5f8;--ok:#16794a;--ko:#b3261e;--fs:clamp(16px,.7vw + 1.3vh,30px);--bar:52px;--ff:Bahnschrift,"DIN Alternate","Segoe UI Semibold","Arial Narrow",system-ui,sans-serif;--fb:"Segoe UI",system-ui,-apple-system,Roboto,Arial,sans-serif}
*{box-sizing:border-box}html,body{height:100%;margin:0;overflow:hidden;background:var(--n)}
body.deck{font-size:var(--fs);line-height:1.4;color:var(--i);font-family:var(--fb)}
h1,h2,h3,.k,.tag2,.pill{font-family:var(--ff)}
.dk-top{position:fixed;inset:0 0 auto 0;height:var(--bar);z-index:20;display:flex;align-items:center;gap:10px;padding:0 12px;background:var(--n);color:#fff;border-bottom:3px solid var(--y);font-size:14px}
.dk-top img{height:30px;width:auto}.dk-top a{color:#fff;font-weight:700;text-decoration:none;padding:10px 6px;white-space:nowrap}.dk-top a:hover{color:var(--y)}
.dk-top .sec{font-weight:800;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;min-width:0;flex:1}.dk-top .cnt{font-variant-numeric:tabular-nums;opacity:.85;white-space:nowrap}
.dk-top button{background:#0d3a5c;color:#fff;border:1px solid #9ed0ea;border-radius:8px;padding:6px 10px;cursor:pointer;font:inherit;font-weight:800;min-height:36px}
body.qbig #qbtn{background:var(--y);color:var(--n)}
.timer.over{background:var(--ko)!important}
#stage{position:fixed;top:var(--bar);bottom:148px;left:0;right:0;background:var(--bg);overflow:hidden}
.slide{display:none;height:100%;overflow:auto;padding:clamp(14px,3vh,40px) clamp(16px,4.5vw,72px) 24px;position:relative}
.slide.active{display:block;animation:sl .32s ease both}@keyframes sl{from{opacity:0}to{opacity:1}}
.slide.back.active{animation-name:slb}@keyframes slb{from{opacity:0}to{opacity:1}}
.slide h1{font-size:2.4em;margin:.1em 0 .3em;line-height:1.08;color:var(--n)}.slide h2{font-size:1.75em;line-height:1.12;margin:.05em 0 .55em;color:var(--n);display:flex;align-items:center;gap:.4em}.slide h3{font-size:1.15em;margin:.1em 0 .3em;color:var(--n)}
.slide .k{display:block;color:#8a520a;font-weight:900;letter-spacing:.14em;text-transform:uppercase;font-size:.62em;margin-bottom:.25em}
.ic{width:1.3em;height:1.3em;flex:none}.ic.h{width:1.2em;height:1.2em;color:var(--b)}.ic.sm{width:1.6em;height:1.6em;color:var(--b);margin-bottom:.15em}
.slide p,.slide li{margin:.35em 0}.lead,.big{font-size:1.2em}.lead{color:var(--i)}
.cols2{display:grid;gap:1em;grid-template-columns:repeat(2,minmax(0,1fr))}.cols3{display:grid;gap:1em;grid-template-columns:repeat(3,minmax(0,1fr));align-items:stretch}.cols5{display:grid;gap:.8em;grid-template-columns:repeat(5,minmax(0,1fr))}
.tile{background:#fff;border:1px solid var(--l);border-radius:14px;padding:.8em 1em;box-shadow:0 2px 10px rgba(16,44,83,.08);min-width:0}.tile.acc{border-top:.28em solid var(--y)}
.tile p{margin:.2em 0;font-size:.95em}.tile b.n{display:block;font-size:2em;color:var(--b);line-height:1;font-family:var(--ff)}.tile b.kpi{display:block;font-size:2.1em;color:var(--n);line-height:1.05;font-family:var(--ff);margin-bottom:.1em}
.num{display:inline-flex;width:1.7em;height:1.7em;border-radius:50%;background:var(--n);color:var(--y);align-items:center;justify-content:center;font-weight:900;font-family:var(--ff);font-size:.9em}.chk{display:inline-flex;width:1.7em;height:1.7em;border-radius:50%;background:var(--ok);color:#fff;align-items:center;justify-content:center;font-weight:900}
.callout{border-radius:14px;padding:.75em 1em;margin:.7em 0;border-left:.4em solid var(--b);background:#e9f2fb;display:flex;gap:.6em;align-items:flex-start}.callout span{flex:1}
.callout.danger{border-color:var(--ko);background:#fdeceb}.callout.danger .ic{color:var(--ko);margin:0;flex:none}.callout.warn{border-color:var(--y);background:#fff6e6}.callout.ok{border-color:var(--ok);background:#e9f7f0}
.frag{opacity:0;transform:translateY(10px);pointer-events:none;transition:opacity .35s,transform .35s;visibility:hidden}.frag.show{opacity:1;transform:none;pointer-events:auto;visibility:visible}
.split{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,.9fr);gap:clamp(16px,2.4vw,44px);align-items:center}
.vis{margin:0}.vis img{width:100%;height:auto;max-height:52vh;border-radius:14px;object-fit:cover;display:block;box-shadow:0 6px 24px rgba(16,44,83,.18)}.vis figcaption{font-size:.6em;color:var(--m);margin-top:.3em}
.vis.svg img{object-fit:contain;background:#fff;border:1px solid var(--l);box-shadow:none;max-height:62vh}
.slide.planche .vis{text-align:center}.slide.planche .vis img{width:auto;max-width:100%;max-height:calc(100vh - 410px);margin:0 auto}
.slide.adi{background:linear-gradient(90deg,#fff 0,#fff 96%,#fbe3e0 100%);border-left:.5em solid var(--ko)}.slide.adi .k{color:var(--ko)}.slide.adi h2 .ic{color:var(--ko)}.leadadi{border-left:.3em solid var(--ko);padding-left:.6em}
.slide.dec{background:linear-gradient(135deg,#eaf7f0,#fff)}.slide.qcm{background:linear-gradient(135deg,#eaf1fb,#fff)}.slide.jour{background:linear-gradient(135deg,#fff7e3,#fff)}
.pill{display:inline-block;background:var(--n);color:#fff;border-radius:999px;padding:.15em .8em;font-size:.7em;font-weight:800;margin:0 .3em .3em 0}
.seq{list-style:none;padding:0;columns:2;font-size:.85em}.seq li span{color:var(--m)}
.tbl table{width:100%;border-collapse:collapse;font-size:.85em}.tbl th,.tbl td{border:1px solid var(--l);padding:.35em .6em;text-align:left;vertical-align:top}.tbl th{background:var(--n);color:#fff}
/* ouverture de module */
.slide.mod{background:linear-gradient(110deg,rgba(16,44,83,.97) 0%,rgba(16,44,83,.88) 52%,rgba(16,44,83,.4) 100%),var(--bgimg,none) center/cover,var(--n);color:#fff}
.slide.mod h1,.slide.mod .lead{color:#fff}.slide.mod .k{color:var(--y)}.mhead{max-width:62%;padding-top:4vh}.bigico{display:block;width:4em;height:4em;color:var(--y);margin-bottom:.6em}.bigico .ic{width:100%;height:100%}
.sit{margin-top:1em;max-width:46em;background:rgba(255,255,255,.12);border-left:.35em solid var(--y);border-radius:12px;padding:.6em 1em;font-size:.95em}.slide.mod .pill{background:var(--y);color:var(--n)}.links a{display:inline-block;background:#fff;color:var(--n);font-weight:800;border-radius:10px;padding:.4em .9em;margin:.3em .5em .3em 0;text-decoration:none;font-size:.8em}
.slide.cover{background:linear-gradient(120deg,rgba(16,44,83,.97) 0%,rgba(16,44,83,.86) 48%,rgba(16,44,83,.3) 100%),url(../images/ia/TB02.webp) center/cover,var(--n);color:#fff}
.cover h1{color:#fff;font-size:2.8em}.cover .logo{height:clamp(50px,11vh,110px);width:auto;margin-bottom:5vh;display:block}.cover .meta,.cover .meta2{font-size:1.1em;opacity:.95}.cover .meta2{color:var(--y);font-weight:700}
.cover .tag2{display:inline-block;background:var(--y);color:var(--n);font-weight:800;padding:.25em .8em;border-radius:99px;font-size:.7em;margin-bottom:.8em}
.slide.fin{background:var(--n);color:#fff}.fin h1,.fin .lead{color:#fff}.fin .k{color:var(--y)}
/* QCM */
.opts{max-width:60em}.opt{display:flex;align-items:center;gap:.6em;width:100%;text-align:left;margin:.4em 0;padding:.7em 1em;min-height:48px;border-radius:12px;border:2px solid var(--l);background:#fff;font:inherit;color:var(--i);cursor:pointer}.opt:hover{border-color:var(--b)}
.opt .l{flex:0 0 auto;width:1.6em;height:1.6em;border-radius:50%;background:var(--n);color:#fff;display:inline-flex;align-items:center;justify-content:center;font-weight:800;font-size:.8em}
.opt.good{border-color:var(--ok);background:#e9f7f0}.opt.bad{border-color:var(--ko);background:#fdeceb}.qexp{margin-top:.6em;font-weight:700}
/* QR : visible sur chaque diapo */
.qb{position:fixed;left:0;right:0;bottom:64px;height:84px;display:flex;align-items:center;justify-content:space-between;flex-direction:row-reverse;gap:12px;padding:6px max(14px,3vw);background:var(--n);color:#fff;font-size:clamp(12px,.9vw + .5vh,19px);z-index:15;border-top:3px solid var(--y)}
.qb:not(.qa){display:none}.slide.active .qb{display:flex}
.qb span{display:flex;flex-direction:column;line-height:1.3}.qb b{color:var(--y);font-size:1.05em}.qb a{color:#9ed0ea;font-weight:700}
.qb img{width:72px;height:72px;border-radius:8px;background:#fff;padding:2px;transition:width .2s,height .2s;flex:none}.qb span{flex:1}
body.qbig .slide.active .qb{height:auto;padding:14px 24px;font-size:20px;box-shadow:0 -12px 30px #0008}body.qbig .slide.active .qb img{width:min(34vh,300px);height:min(34vh,300px)}
.dk-bot{position:fixed;left:0;right:0;bottom:0;height:64px;z-index:20;display:flex;align-items:center;gap:8px;padding:0 10px;background:#fff;border-top:1px solid var(--l)}
.dk-bot button{min-width:48px;min-height:48px;border-radius:12px;border:0;background:var(--n);color:#fff;font:inherit;font-weight:800;font-size:16px;cursor:pointer;padding:0 14px}.dk-bot button.alt{background:#dbe7ee;color:var(--i)}
.dk-bot .prog{flex:1;height:8px;background:#dbe7ee;border-radius:99px;overflow:hidden;min-width:40px}.dk-bot .prog i{display:block;height:100%;width:0;background:var(--y);transition:width .3s}
.dk-bot .ph{font-size:13px;color:var(--m);white-space:nowrap}
#notes{position:fixed;left:0;right:0;bottom:64px;max-height:46vh;overflow:auto;z-index:25;background:#fffbe6;border-top:4px solid #e6a400;padding:14px max(16px,4vw);font-size:16px;display:none;box-shadow:0 -8px 24px rgba(0,0,0,.2)}#notes.on{display:block}#notes h4{margin:0 0 6px}
#ovw{position:fixed;inset:var(--bar) 0 64px 0;z-index:24;background:var(--bg);overflow:auto;padding:16px;display:none}#ovw.on{display:block}
#ovw ol{list-style:none;margin:0;padding:0;display:grid;gap:10px;grid-template-columns:repeat(auto-fill,minmax(220px,1fr))}
#ovw button{width:100%;text-align:left;min-height:64px;padding:10px 12px;border-radius:12px;border:1px solid var(--l);background:#fff;font:inherit;font-size:14px;color:var(--i);cursor:pointer}#ovw small{color:var(--m);display:block}
#help{position:fixed;inset:0;z-index:40;background:rgba(16,44,83,.94);color:#fff;display:none;align-items:center;justify-content:center;padding:20px}#help.on{display:flex}#help div{max-width:560px;font-size:16px}#help kbd{background:#fff;color:#000;border-radius:5px;padding:1px 7px;font-weight:700}
.black #stage,.black #notes{visibility:hidden}.slide .note{display:none}
@media(max-width:900px){.cols3,.cols5{grid-template-columns:1fr 1fr}.split{grid-template-columns:1fr}.mhead{max-width:100%}}
@media(max-width:760px){:root{--bar:46px}.dk-top a:not(.keep),.dk-top #qsc,.dk-top .sec{display:none}.dk-top{gap:6px}.dk-top button{white-space:nowrap;padding:4px 8px;font-size:13px}.dk-top .cnt{flex:1;text-align:right}.cols2,.cols3,.cols5{grid-template-columns:1fr}.dk-top img,.dk-top .back{display:none}.slide h1{font-size:1.9em}.slide h2{font-size:1.4em}.dk-bot .hide-s{display:none}.slide{padding-bottom:24px}
 #stage{bottom:64px}.slide.active{display:flex;flex-direction:column}.slide.active>*{flex:none}.slide .qb,body.qbig .slide.active .qb{position:static;order:99;margin:18px 0 0;height:auto;max-width:none;width:100%;flex-direction:row;padding:10px 12px;box-shadow:none;border-radius:12px;border-top:0;font-size:14px}.qb img{display:none}body.qbig .slide.active .qb img{display:block;width:60vw;height:60vw}}
@media print{html,body{height:auto;overflow:visible}.dk-top,.dk-bot,#notes,#ovw,#help,.qb{display:none!important}#stage{position:static}.slide{display:block!important;break-after:page;height:auto;overflow:visible}.frag{opacity:1!important;visibility:visible!important;transform:none!important}}
@media(prefers-reduced-motion:reduce){.slide.active{animation:none}.frag{transition:none}}
'''

JS = r'''(function(){'use strict';
document.addEventListener('DOMContentLoaded',function(){
var stage=document.getElementById('stage'),slides=[].slice.call(stage.querySelectorAll('.slide')),cur=0,ovw=document.getElementById('ovw'),notes=document.getElementById('notes');
var score=0,answered=0,sc=document.getElementById('qsc');
slides.filter(function(s){return s.classList.contains('qcm')}).forEach(function(s){var o=s.querySelector('.opts'),ok=+o.dataset.ok;
 o.querySelectorAll('.opt').forEach(function(b){b.addEventListener('click',function(){if(s.dataset.done)return;s.dataset.done='1';answered++;var j=+b.dataset.j,good=j===ok;if(good)score++;
  o.querySelectorAll('.opt').forEach(function(bb,k){if(k===ok)bb.classList.add('good');else if(k===j)bb.classList.add('bad');bb.disabled=true});
  var e=s.querySelector('.qexp');e.hidden=false;e.textContent=(good?'✓ Correct. ':'✗ Réponse : '+'ABCD'.charAt(ok)+'. ')+e.textContent;e.style.color=good?'#16794a':'#b3261e';
  if(sc)sc.textContent='Salle : '+score+' / '+answered})})});
var ol=ovw.querySelector('ol'),lastSec='';
slides.forEach(function(s,i){var li=document.createElement('li'),b=document.createElement('button');b.type='button';b.innerHTML='<small>'+(i+1)+' · '+(s.dataset.sec||'')+'</small>';b.appendChild(document.createTextNode(s.dataset.title||('Diapositive '+(i+1))));b.addEventListener('click',function(){ovw.classList.remove('on');go(i,true)});li.appendChild(b);ol.appendChild(li)});
var prog=document.querySelector('.prog i'),cnt=document.querySelector('.cnt'),sec=document.querySelector('.sec');
var tm=document.getElementById('timer'),tRun=false,tLeft=0,tInt=null,curMin=0,curSec='';
function fmt(s){var a=Math.abs(s),m=Math.floor(a/60),r=a%60;return(s<0?'+':'')+(m<10?'0':'')+m+':'+(r<10?'0':'')+r}
function tDraw(){tm.textContent=(tRun?'⏸ ':'⏱ ')+fmt(tLeft);tm.classList.toggle('over',tLeft<0)}
function tStart(){if(tInt)return;tRun=true;tInt=setInterval(function(){tLeft--;tDraw()},1000);tDraw()}
function tStop(){tRun=false;clearInterval(tInt);tInt=null;tDraw()}
tm.addEventListener('click',function(){tRun?tStop():tStart()});tm.addEventListener('dblclick',function(){tLeft=curMin*60;tDraw()});
function frags(s){return [].slice.call(s.querySelectorAll('.frag:not(.show)'))}
function go(i,all,back){i=Math.max(0,Math.min(slides.length-1,i));slides.forEach(function(s){s.classList.remove('active','back')});var s=slides[i];s.classList.add('active');if(back)s.classList.add('back');
 if(all||back)[].slice.call(s.querySelectorAll('.frag')).forEach(function(f){f.classList.add('show')});else if(!s.dataset.seen)[].slice.call(s.querySelectorAll('.frag')).forEach(function(f){f.classList.remove('show')});
 s.dataset.seen='1';s.scrollTop=0;cur=i;prog.style.width=(100*(i+1)/slides.length)+'%';cnt.textContent=(i+1)+' / '+slides.length;sec.textContent=s.dataset.sec||'';
 var m=0;for(var j=i;j>=0&&slides[j].dataset.sec===s.dataset.sec;j--){var mm=parseInt(slides[j].dataset.min,10);if(mm){m=mm;break}}
 if(m&&curSec!==s.dataset.sec){curMin=m;if(!tRun){tLeft=m*60;tDraw()}}curSec=s.dataset.sec;
 var n=s.querySelector('.note');notes.innerHTML='<h4>Notes formateur — '+(s.dataset.title||'')+'</h4>'+(n?n.innerHTML:'<p>Pas de note.</p>');
 if(location.hash!=='#'+(i+1))history.replaceState(null,'','#'+(i+1))}
function next(){var s=slides[cur],f=frags(s);if(f.length){f[0].classList.add('show');return}go(cur+1)}
function prev(){var s=slides[cur],f=[].slice.call(s.querySelectorAll('.frag.show'));if(f.length&&!s.dataset.noback){f[f.length-1].classList.remove('show');return}if(cur>0)go(cur-1,false,true)}
document.getElementById('bn').onclick=next;document.getElementById('bp').onclick=prev;
function tog(el,b){el.classList.toggle('on');if(b)b.setAttribute('aria-pressed',el.classList.contains('on'))}
var bn=document.getElementById('bnotes'),bo=document.getElementById('bovw');
bn.onclick=function(){tog(notes,bn)};bo.onclick=function(){tog(ovw,bo)};
document.getElementById('bhelp').onclick=function(){document.getElementById('help').classList.add('on')};document.getElementById('help').onclick=function(){this.classList.remove('on')};
function fs(){var d=document,e=d.documentElement;if(!d.fullscreenElement&&e.requestFullscreen){e.requestFullscreen().catch(function(){})}else if(d.exitFullscreen){d.exitFullscreen()}}
var bf=document.getElementById('bfs');bf.onclick=fs;if(!document.documentElement.requestFullscreen||window.matchMedia('(pointer:coarse)').matches||window.self!==window.top)bf.style.display='none';
function qtog(){document.body.classList.toggle('qbig')}document.getElementById('qbtn').onclick=qtog;
document.addEventListener('keydown',function(e){if(/INPUT|TEXTAREA|SELECT/.test((e.target||{}).tagName||'')&&e.key!=='Escape')return;var k=e.key;
 if(k==='ArrowRight'||k==='PageDown'||k===' '||k==='Enter'){if(e.target.tagName==='BUTTON'&&(k===' '||k==='Enter'))return;e.preventDefault();next()}
 else if(k==='ArrowLeft'||k==='PageUp'||k==='Backspace'){e.preventDefault();prev()}else if(k==='Home')go(0);else if(k==='End')go(slides.length-1);
 else if(k==='f'||k==='F')fs();else if(k==='n'||k==='N')tog(notes,bn);else if(k==='g'||k==='G')tog(ovw,bo);else if(k==='t'||k==='T')tm.click();
 else if(k==='q'||k==='Q')qtog();else if(k==='b'||k==='B'||k==='.')document.body.classList.toggle('black');else if(k==='?'||k==='h')document.getElementById('help').classList.toggle('on');
 else if(k==='Escape'){document.getElementById('help').classList.remove('on');ovw.classList.remove('on');notes.classList.remove('on');document.body.classList.remove('qbig')}});
var sx=0,sy=0,st=0;stage.addEventListener('touchstart',function(e){var t=e.changedTouches[0];sx=t.clientX;sy=t.clientY;st=Date.now()},{passive:true});
stage.addEventListener('touchend',function(e){var t=e.changedTouches[0],dx=t.clientX-sx,dy=t.clientY-sy;if(Math.abs(dx)>60&&Math.abs(dx)>Math.abs(dy)*1.6&&Date.now()-st<700){dx<0?next():prev()}},{passive:true});
var h=parseInt((location.hash||'').slice(1),10);go(h>=1&&h<=slides.length?h-1:0,false);
window.addEventListener('hashchange',function(){var n=parseInt(location.hash.slice(1),10);if(n>=1&&n<=slides.length&&n-1!==cur)go(n-1,true)});tDraw();
});})();'''

def page(body):
    return ('<!doctype html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><meta name="theme-color" content="#102c53"><meta name="robots" content="noindex,nofollow"><meta name="description" content="Mode animation plein écran : habilitation électrique A260E2A">'
            '<title>Mode animation — Habilitation électrique A260E2A</title><link rel="manifest" href="manifest.webmanifest"><link rel="icon" href="assets/img/logo-consulteam-groupe.png"><link rel="stylesheet" href="assets/deck.css"></head><body class="deck">'
            '<header class="dk-top"><a class="back" href="index.html">← Accueil</a><a class="keep" href="parcours.html" target="_blank" rel="noopener">Parcours</a><a href="cours/index.html" target="_blank" rel="noopener">Cours</a><a href="suivre.html" target="_blank" rel="noopener">Suivre</a>'
            '<img src="assets/img/logo-consulteam-groupe.png" alt="Consulteam Groupe" width="146" height="30"><span class="sec" aria-live="polite"></span><span id="qsc" class="cnt"></span><span class="cnt"></span>'
            '<button id="qbtn" type="button" title="Agrandir ou réduire le QR (touche Q)">QR (Q)</button><button id="timer" class="timer" type="button" title="Chrono de la séquence : clic = démarrer / pause, double-clic = remise à zéro">⏱ --:--</button></header>'
            '<main id="stage" aria-live="off">%s</main><div id="ovw" role="dialog" aria-label="Sommaire des diapositives"><ol></ol></div><aside id="notes" aria-label="Notes formateur"></aside>'
            '<div id="help" role="dialog" aria-label="Aide"><div><h2 style="color:#fff">Raccourcis</h2><p><kbd>→</kbd> <kbd>Espace</kbd> suivant / révéler · <kbd>←</kbd> précédent<br><kbd>G</kbd> sommaire · <kbd>N</kbd> notes formateur · <kbd>T</kbd> chrono · <kbd>Q</kbd> agrandir le QR · <kbd>F</kbd> plein écran · <kbd>B</kbd> écran noir · <kbd>Échap</kbd> fermer<br>Smartphone ou tablette : balayer à gauche ou à droite.</p><p>Toucher pour fermer.</p></div></div>'
            '<nav class="dk-bot" aria-label="Navigation du diaporama"><button id="bp" type="button" aria-label="Précédent">◀</button><div class="prog" aria-hidden="true"><i></i></div><button id="bn" type="button" aria-label="Suivant">▶</button>'
            '<button id="bovw" class="alt" type="button" aria-pressed="false" aria-label="Sommaire">☰<span class="hide-s"> Sommaire</span></button><button id="bnotes" class="alt" type="button" aria-pressed="false" aria-label="Notes formateur">✎<span class="hide-s"> Notes</span></button><button id="bfs" class="alt" type="button" aria-label="Plein écran">⛶</button><button id="bhelp" class="alt hide-s" type="button" aria-label="Aide">?</button></nav>'
            '<script src="assets/deck.js"></script></body></html>') % body
