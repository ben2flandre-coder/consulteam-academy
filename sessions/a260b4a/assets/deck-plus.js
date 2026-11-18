/* Consulteam · deck-plus : continuité, secours et renvois pour les diaporamas d'animation.
   Se greffe sur le diaporama existant (lecture seule du DOM, aucune dépendance).
   Configuration : window.DP (voir le bloc <script> placé avant ce fichier dans chaque animation). */
(function () {
  'use strict';
  var DP = window.DP || {};
  function ready(f) { if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', f); else f(); }
  ready(function () { setTimeout(init, 0); });

  function init() {
    var S = [].slice.call(document.querySelectorAll('.slide'));
    if (!S.length) return;
    var N = S.length, jp = document.getElementById('jp'), ovw = document.getElementById('ovw');
    var ICON = { c: '📖', e: '✍', s: '🚑', v: '✅', m: '🧰', x: '↗' };
    var CLS = { c: 'dp-c', e: 'dp-e', s: 'dp-s', v: 'dp-v', m: 'dp-m' };

    function esc(t) { return String(t == null ? '' : t).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
    function title(k) {
      var s = S[k], h = s.querySelector('h2,h1'), t = h ? h.textContent : '';
      t = (t || s.getAttribute('data-title') || '').replace(/\s+/g, ' ').trim();
      return t || ('Diapositive ' + (k + 1));
    }
    function cur() {
      for (var k = 0; k < N; k++) if (S[k].classList.contains('on') || S[k].classList.contains('active')) return k;
      return 0;
    }
    function goto_(k) {
      k = Math.max(0, Math.min(N - 1, k));
      if (jp && jp.options && jp.options.length >= N) { jp.value = k; jp.dispatchEvent(new Event('change')); return; }
      if (ovw) { var b = ovw.querySelectorAll('ol li button')[k]; if (b) { b.click(); return; } }
      try { location.hash = '#' + (k + 1); } catch (e) { }
    }

    /* ---------- configuration automatique (ADI : modules Mn) ---------- */
    if (DP.auto === 'modules') {
      var seq = [], last = '';
      S.forEach(function (s, k) {
        var sec = s.getAttribute('data-sec') || '';
        var m = sec.match(/M(\d+)/), lab = sec.replace(/^J\d\s*·\s*/, '').replace(/^M\d+\s*·\s*/, '');
        var key = sec;
        if (key !== last) {
          var mod = m ? m[1] : null, o = { a: k + 1, b: k + 1, n: mod ? 'Module ' + mod : lab, t: lab, links: [] };
          if (mod) {
            o.links.push(['c', 'Cours du module ' + mod, 'parcours.html#m' + mod]);
            o.links.push(['e', 'Questions guidées', 'parcours.html#m' + mod + '/faire']);
            o.links.push(['v', 'Évaluer ce module', 'evaluation.html#m' + mod]);
          }
          if (mod === '8') o.links.unshift(['s', 'Fiche Secours', 'secours.html']);
          if (mod === '23') o.links.unshift(['s', 'Fiche Secours', 'secours.html']);
          seq.push(o); last = key;
        } else seq[seq.length - 1].b = k + 1;
      });
      DP.seq = seq;
      var firstS = 0; seq.forEach(function (o) { if (/M8\b/.test(S[o.a - 1].getAttribute('data-sec') || '') && !firstS) firstS = o.a; });
      var lastS = 0; seq.forEach(function (o) { if (/M(8|23)\b/.test(S[o.a - 1].getAttribute('data-sec') || '')) lastS = o.b; });
      DP.secours = { a: firstS || 1, b: lastS || firstS || 1, links: [['s', 'Fiche « Accident : que faire ? »', 'secours.html'], ['c', 'Module 8 · Accident, incendie, alerte', 'parcours.html#m8'], ['c', 'Module 23 · Études de cas', 'parcours.html#m23'], ['v', 'Évaluer le module 8', 'evaluation.html#m8']] };
      DP.ex = {}; DP.hint = false;
      S.forEach(function (s, k) { if (s.classList.contains('qcm')) DP.ex[k + 1] = true; });
    }
    var SEQ = DP.seq || [], SEC = DP.secours || null, EX = DP.ex || {};
    function seqOf(k) { var p = k + 1; for (var q = 0; q < SEQ.length; q++) if (p >= SEQ[q].a && p <= SEQ[q].b) return q; return -1; }
    function isSec(k) { return SEC && k + 1 >= SEC.a && k + 1 <= SEC.b; }
    function exOf(k) { return !!EX[k + 1] || S[k].classList.contains('ex') || S[k].classList.contains('qcm'); }

    /* ---------- CSS ---------- */
    var css = '' +
      '.dp-dock{display:inline-flex;gap:6px;align-items:center;flex-wrap:wrap;font:600 14px/1.2 system-ui,sans-serif;color:#fff}' +
      '.dp-dock button{font:inherit;color:#fff;border:0;border-radius:8px;padding:6px 10px;cursor:pointer;white-space:nowrap;background:#1f4d6b;transition:transform .15s,background .15s}' +
      '.dp-dock button:hover{transform:translateY(-1px);background:#2a6489}' +
      '.dp-dock .dp-sec{background:#c62828;animation:dp-pulse 2.6s infinite}.dp-dock .dp-sec:hover{background:#e53935}.dp-dock .dp-cs{background:#2b6b53}.dp-dock .dp-cs.e{background:#9a6a12}.dp-dock .dp-cs:hover{filter:brightness(1.15)}' +
      '.dp-hint{position:fixed;left:14px;bottom:16px;z-index:60;max-width:min(430px,60vw);border:1px solid #2f6585;border-radius:999px;padding:8px 14px;background:rgba(10,28,44,.93);color:#cfe6f3;font:600 13px/1.2 system-ui,sans-serif;cursor:pointer;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;box-shadow:0 6px 20px rgba(0,0,0,.4)}.dp-hint b{color:#ffcf6b}.dp-hint:hover{background:#14384f}' +
      '.dp-rail{position:fixed;left:0;right:0;bottom:0;height:7px;z-index:59;display:flex;gap:2px;background:transparent}.dp-rail i{display:block;flex:1 1 0;background:#2a5875;position:relative;cursor:pointer;transition:background .25s,height .15s;height:5px;align-self:flex-end}.dp-rail i:hover{height:7px;background:#3f7ba0}.dp-rail i.done{background:#5cc08a}.dp-rail i.cur{background:#f6b63d;height:7px}.dp-rail i.sec{box-shadow:inset 0 -3px 0 #ff5a50}' +
      '.dp-ban{position:fixed;left:50%;bottom:92px;transform:translate(-50%,30px);opacity:0;z-index:70;pointer-events:none;background:linear-gradient(90deg,#102a3a,#1d4f6e);border:2px solid #e8a33d;border-radius:14px;padding:12px 22px;color:#fff;font:700 clamp(17px,2vw,26px)/1.25 system-ui,sans-serif;text-align:center;max-width:90vw;box-shadow:0 10px 30px rgba(0,0,0,.45)}.dp-ban small{display:block;color:#ffcf6b;font-weight:600;font-size:.62em;letter-spacing:.08em;text-transform:uppercase;margin-bottom:2px}.dp-ban.sec{border-color:#ff5a50;background:linear-gradient(90deg,#4a1212,#8a1f1f)}.dp-ban.on{animation:dp-ban 2.8s ease both}' +
      '@keyframes dp-ban{0%{opacity:0;transform:translate(-50%,30px)}12%{opacity:1;transform:translate(-50%,0)}78%{opacity:1;transform:translate(-50%,0)}100%{opacity:0;transform:translate(-50%,14px)}}' +
      '@keyframes dp-pulse{0%{box-shadow:0 0 0 0 rgba(255,90,80,.65)}70%{box-shadow:0 0 0 12px rgba(255,90,80,0)}100%{box-shadow:0 0 0 0 rgba(255,90,80,0)}}' +
      '@keyframes dp-in{from{opacity:0;transform:translateY(16px)}to{opacity:1;transform:none}}' +
      '.dp-anim .slide.on>*:not(.qb):not(.note):not(aside):not(.notes):not(.pn):not(.frag):not(.dp-ribbon){animation:dp-in .45s ease both}.dp-anim .slide.active>*:not(.qb):not(.note):not(.frag):not(.dp-ribbon){animation:dp-in .45s ease both}' +
      '.dp-anim .slide.on>*:nth-child(2),.dp-anim .slide.active>*:nth-child(2){animation-delay:.05s}.dp-anim .slide.on>*:nth-child(3),.dp-anim .slide.active>*:nth-child(3){animation-delay:.12s}.dp-anim .slide.on>*:nth-child(4),.dp-anim .slide.active>*:nth-child(4){animation-delay:.2s}.dp-anim .slide.on>*:nth-child(5),.dp-anim .slide.active>*:nth-child(5){animation-delay:.28s}' +
      '.dp-ribbon{position:absolute;top:6px;right:0;z-index:4;display:flex;gap:8px;align-items:center;padding:6px 14px;border-radius:999px;font:700 14px/1 system-ui,sans-serif;color:#fff;cursor:pointer;border:0}.dp-ribbon.s{background:#c62828;animation:dp-pulse 2.6s infinite}.dp-ribbon.e{background:#b57a10}' +
      'body.dp-hasqr .dp-ribbon{right:310px}@media(max-width:860px){body.dp-hasqr .dp-ribbon{right:0;top:-4px}}' +
      '.slide.dp-sec{box-shadow:inset 6px 0 0 #ff5a50}.slide.dp-ex{box-shadow:inset 6px 0 0 #e8a33d}' +
      '.dp-dr{position:fixed;top:0;right:0;bottom:0;width:var(--dpw,min(560px,48vw));z-index:80;background:#fff;color:#102a3a;display:none;flex-direction:column;box-shadow:-10px 0 40px rgba(0,0,0,.5);border-left:4px solid #e8a33d}.dp-dr.on{display:flex}' +
      '.dp-dr header{display:flex;gap:8px;align-items:center;padding:8px 10px;background:#102a3a;color:#fff;font:600 14px system-ui,sans-serif}.dp-dr header b{flex:1;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}.dp-dr header a,.dp-dr header button{color:#fff;background:#1f4d6b;border:0;border-radius:8px;padding:6px 10px;cursor:pointer;text-decoration:none;font:inherit}.dp-dr iframe{flex:1;border:0;width:100%;background:#fff}' +
      '.dp-tabs{display:flex;gap:6px;flex-wrap:wrap;padding:6px 10px;background:#eaf3f9}.dp-tabs button{border:1px solid #9ec3da;background:#fff;color:#102a3a;border-radius:999px;padding:5px 11px;cursor:pointer;font:600 13px system-ui}.dp-tabs button.on{background:#102a3a;color:#fff}' +
      'body.dp-open{--dpw:min(560px,48vw)}body.dp-open:not(.dp-adi) main{margin-right:var(--dpw)}body.dp-open:not(.dp-adi) .dk{right:var(--dpw)}.dp-dock.inbar{flex-wrap:nowrap}body.dp-open .dp-ban{left:calc((100vw - var(--dpw))/2)}' +
      '.dp-plan{position:fixed;inset:0;z-index:90;background:rgba(5,15,25,.88);display:none;overflow:auto;padding:70px 20px 40px;color:#fff;font:15px/1.4 system-ui,sans-serif}.dp-plan.on{display:block}.dp-plan .wrap{max-width:1120px;margin:auto}.dp-plan h3{margin:0 0 4px;font-size:22px}.dp-plan .top{display:flex;gap:10px;align-items:center;justify-content:space-between;margin-bottom:14px}.dp-plan .top button{background:#1f4d6b;color:#fff;border:0;border-radius:10px;padding:8px 14px;cursor:pointer;font:600 14px system-ui}' +
      '.dp-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:12px}.dp-card{background:#102a3a;border:1px solid #2f6585;border-radius:12px;padding:12px 14px}.dp-card.cur{border-color:#f6b63d;box-shadow:0 0 0 2px #f6b63d}.dp-card.sec{border-color:#ff5a50;background:#3a1414}.dp-card h4{margin:0 0 4px;font-size:16px}.dp-card small{color:#9ed0ea}.dp-card .row{display:flex;gap:6px;flex-wrap:wrap;margin-top:8px}.dp-card .row button,.dp-card .row a{background:#1f4d6b;color:#fff;border:0;border-radius:8px;padding:6px 10px;cursor:pointer;text-decoration:none;font:600 13px system-ui}.dp-card .row .go{background:#e8a33d;color:#102a3a}.dp-card .row .s{background:#c62828}.dp-card .row .c{background:#2b6b53}.dp-card .row .e{background:#9a6a12}.dp-card .row .v{background:#4b5d9e}.dp-card .row .m{background:#7a4a8c}' +
      '.dp-exl{margin-top:18px}.dp-exl h4{margin:0 0 6px}.dp-exl button{background:#14384f;color:#fff;border:1px solid #2f6585;border-radius:8px;padding:6px 10px;margin:3px;cursor:pointer;font:600 13px system-ui}' +
      '@media(max-width:860px){.dp-hint{display:none}.dp-dock{width:100%}body.dp-adi .dp-dock{position:fixed;right:8px;bottom:78px;width:auto;z-index:61;background:rgba(10,28,44,.93);padding:5px;border-radius:12px;border:1px solid #2f6585}body.dp-adi .dp-dock button{font-size:0;padding:8px 10px}body.dp-adi .dp-dock button::first-letter{font-size:18px}.dp-dock button{padding:6px 8px;font-size:13px}body.dp-open{--dpw:100vw}.dp-dr{width:100vw}}' +
      '@media(prefers-reduced-motion:reduce){.dp-dock .dp-sec,.dp-ribbon.s{animation:none}.dp-anim .slide.on>*,.dp-anim .slide.active>*{animation:none}.dp-ban.on{animation:none;opacity:1;transform:translate(-50%,0)}}' +
      '@media print{.dp-dock,.dp-rail,.dp-ban,.dp-dr,.dp-plan,.dp-ribbon{display:none!important}}';
    var st = document.createElement('style'); st.id = 'dp-css'; st.textContent = css; document.head.appendChild(st);
    if (DP.anim !== false) document.body.classList.add('dp-anim');
    if (DP.auto === 'modules') document.body.classList.add('dp-adi');

    /* ---------- titres de la liste de navigation (#jp) ---------- */
    if (jp && jp.options && jp.options.length >= N) {
      for (var k = 0; k < N; k++) {
        var q = seqOf(k), pre = (isSec(k) ? '🚑 ' : (exOf(k) ? '✍ ' : '')), tag = q >= 0 && DP.auto !== 'modules' && SEQ[q].n ? '[' + SEQ[q].n + '] ' : '';
        jp.options[k].textContent = (k + 1) + '. ' + pre + tag + title(k);
      }
    }
    /* ---------- bandeaux sur les diapositives ---------- */
    S.forEach(function (s, k) {
      if (getComputedStyle(s).position === 'static') s.style.position = 'relative';
      if (s.querySelector('.qb')) document.body.classList.add('dp-hasqr');
      if (isSec(k)) { s.classList.add('dp-sec'); var r = document.createElement('button'); r.type = 'button'; r.className = 'dp-ribbon s'; r.innerHTML = '🚑 Secours · fiche détaillée'; r.onclick = function () { openDr(SEC.links); }; s.insertBefore(r, s.firstChild); }
      else if (exOf(k)) { s.classList.add('dp-ex'); var l = (EX[k + 1] && EX[k + 1] !== true) ? EX[k + 1] : null; var r2 = document.createElement('button'); r2.type = 'button'; r2.className = 'dp-ribbon e'; r2.innerHTML = '✍ À vous · exercice' + (l ? ' · TD associé' : ''); r2.onclick = function () { var q = seqOf(k); openDr((l ? l : []).concat(q >= 0 ? SEQ[q].links.filter(function (x) { return x[0] === 'e' || x[0] === 'c'; }) : [])); }; s.insertBefore(r2, s.firstChild); }
    });

    /* ---------- barre d'outils (dans l'entête du diaporama) + pastille de suite ---------- */
    var dock = document.createElement('div'); dock.className = 'dp-dock'; dock.setAttribute('role', 'toolbar'); dock.setAttribute('aria-label', 'Plan, secours et renvois');
    var bar = document.querySelector('.dk, .dk-top'), anchor = document.getElementById('jp') || document.querySelector('.dk-top .sec, .dk .sec');
    if (bar) { if (anchor && anchor.parentNode === bar) bar.insertBefore(dock, anchor.nextSibling); else bar.appendChild(dock); dock.classList.add('inbar'); } else document.body.appendChild(dock);
    if (bar && !window.pad && DP.auto !== 'modules') {
      var mn = document.querySelector('main'); var pad0 = mn ? parseFloat(getComputedStyle(mn).paddingTop) || 0 : 0;
      var isFix = mn && getComputedStyle(mn).position === 'fixed';
      var fixPad = function () { if (!mn) return; var bh = bar.getBoundingClientRect().height; if (isFix) mn.style.top = bh + 'px'; else mn.style.paddingTop = Math.max(pad0, bh + 14) + 'px'; };
      fixPad(); window.addEventListener('resize', fixPad); try { new ResizeObserver(fixPad).observe(bar); } catch (e) { }
    }
    var hint = document.createElement('button'); hint.type = 'button'; hint.className = 'dp-hint'; hint.hidden = true; document.body.appendChild(hint);
    var rail = null;
    if (!DP.noRail && SEQ.length) {
      rail = document.createElement('div'); rail.className = 'dp-rail'; rail.setAttribute('aria-hidden', 'true');
      SEQ.forEach(function (o, q) { var i = document.createElement('i'); i.style.flexGrow = (o.b - o.a + 1); i.title = o.t || o.n; if (SEC && o.a >= SEC.a && o.b <= SEC.b) i.className = 'sec'; i.onclick = function () { goto_(o.a - 1); }; rail.appendChild(i); });
      document.body.appendChild(rail);
    }
    var ban = document.createElement('div'); ban.className = 'dp-ban'; ban.setAttribute('aria-live', 'polite'); document.body.appendChild(ban);

    /* ---------- volet latéral ---------- */
    var dr = document.createElement('aside'); dr.className = 'dp-dr'; dr.setAttribute('aria-label', 'Cours ou exercice lié à cette diapositive');
    dr.innerHTML = '<header><b>Cours et exercices</b><a target="_blank" rel="noopener" id="dp-ext">Ouvrir dans un onglet ↗</a><button type="button" id="dp-x" aria-label="Fermer">✕</button></header><div class="dp-tabs" id="dp-tabs"></div><iframe title="Page liée" id="dp-fr"></iframe>';
    document.body.appendChild(dr);
    var fr = dr.querySelector('#dp-fr'), tabs = dr.querySelector('#dp-tabs'), ext = dr.querySelector('#dp-ext'), lastLinks = [];
    function load(u) {
      ext.href = u; fr.src = u;
      fr.onload = function () { try { var d = fr.contentDocument; if (d && !d.getElementById('dp-in')) { var s = d.createElement('style'); s.id = 'dp-in'; s.textContent = 'header.top,.skip{display:none!important}body{padding-top:0!important}'; d.head.appendChild(s); } } catch (e) { } };
    }
    function openDr(links, idx) {
      links = (links || []).filter(Boolean); if (!links.length) return;
      lastLinks = links; var i = idx || 0;
      tabs.innerHTML = '';
      links.forEach(function (l, j) { var b = document.createElement('button'); b.type = 'button'; b.textContent = (ICON[l[0]] || '') + ' ' + l[1]; if (j === i) b.className = 'on'; b.onclick = function () { openDr(links, j); }; tabs.appendChild(b); });
      load(links[i][2]);
      dr.classList.add('on'); document.body.classList.add('dp-open');
    }
    function closeDr() { dr.classList.remove('on'); document.body.classList.remove('dp-open'); fr.removeAttribute('src'); }
    dr.querySelector('#dp-x').onclick = closeDr;

    /* ---------- plan ---------- */
    var plan = document.createElement('div'); plan.className = 'dp-plan'; plan.setAttribute('role', 'dialog'); plan.setAttribute('aria-label', 'Plan de la séance');
    document.body.appendChild(plan);
    function drawPlan() {
      var c = cur(), qc = seqOf(c), h = '<div class="wrap"><div class="top"><h3>Plan de la séance · ' + N + ' diapositives</h3><button type="button" id="dp-pc">Fermer (Échap)</button></div><div class="dp-grid">';
      if (SEC) h += '<div class="dp-card sec"><h4>🚑 Secours : Accident, que faire ?</h4><small>Diapositives ' + SEC.a + ' à ' + SEC.b + '</small><div class="row"><button class="go" data-g="' + (SEC.a - 1) + '">Aller aux diapositives</button>' + SEC.links.map(function (l, j) { return '<button class="' + l[0] + '" data-sl="' + j + '">' + ICON[l[0]] + ' ' + esc(l[1]) + '</button>'; }).join('') + '</div></div>';
      SEQ.forEach(function (o, q) {
        var inSec = SEC && o.a >= SEC.a && o.b <= SEC.b; if (inSec && DP.auto !== 'modules') return;
        h += '<div class="dp-card' + (q === qc ? ' cur' : '') + '"><h4>' + esc(o.n) + '</h4><small>' + (o.t && o.t !== o.n ? esc(o.t) + ' · ' : '') + 'diapos ' + o.a + ' à ' + o.b + '</small><div class="row"><button class="go" data-g="' + (o.a - 1) + '">Y aller</button>' + (o.links || []).map(function (l, j) { return '<button class="' + l[0] + '" data-q="' + q + '" data-l="' + j + '">' + ICON[l[0]] + ' ' + esc(l[1]) + '</button>'; }).join('') + '</div></div>';
      });
      h += '</div>';
      var ex = []; for (var k = 0; k < N; k++) if (exOf(k)) ex.push(k);
      if (ex.length) h += '<div class="dp-exl"><h4>✍ Exercices et cas (' + ex.length + ')</h4>' + ex.map(function (k) { return '<button data-g="' + k + '">' + (k + 1) + ' · ' + esc(title(k)).slice(0, 60) + '</button>'; }).join('') + '</div>';
      h += '</div>'; plan.innerHTML = h;
      plan.querySelector('#dp-pc').onclick = function () { plan.classList.remove('on'); };
      [].forEach.call(plan.querySelectorAll('[data-g]'), function (b) { b.onclick = function () { plan.classList.remove('on'); goto_(+b.getAttribute('data-g')); }; });
      [].forEach.call(plan.querySelectorAll('[data-sl]'), function (b) { b.onclick = function () { plan.classList.remove('on'); openDr(SEC.links, +b.getAttribute('data-sl')); }; });
      [].forEach.call(plan.querySelectorAll('[data-q]'), function (b) { b.onclick = function () { var o = SEQ[+b.getAttribute('data-q')]; plan.classList.remove('on'); openDr(o.links, +b.getAttribute('data-l')); }; });
    }
    function togglePlan() { if (plan.classList.contains('on')) plan.classList.remove('on'); else { drawPlan(); plan.classList.add('on'); } }

    /* ---------- mise à jour ---------- */
    var lastQ = -2, lastK = -1, bt = null;
    function nextEx(k) { for (var j = k + 1; j < N; j++) if (exOf(j)) return j; return -1; }
    function refresh() {
      var k = cur(); if (k === lastK) return; lastK = k;
      var q = seqOf(k), o = q >= 0 ? SEQ[q] : null, sec = isSec(k);
      var x = EX[k + 1], hasX = !!(x && x !== true);
      var h = '<button type="button" id="dp-p" title="Plan cliquable (touche P)">☰ Plan</button><button type="button" id="dp-sc" class="dp-sec" title="Secours : accident, que faire ? (touche S)">🚑 Secours</button>';
      var L = (sec && SEC ? SEC.links : (o && o.links)) || [];
      if (hasX) L = x.concat(L);
      if (L.length) h += '<button type="button" id="dp-cs" class="dp-cs' + (exOf(k) ? ' e' : '') + '" title="Cours, exercices et fiches liés à cette diapositive (touche L)">' + (exOf(k) ? '✍ Exercice / TD' : '📖 Cours / TD') + '</button>';
      dock.innerHTML = h;
      dock.querySelector('#dp-p').onclick = togglePlan;
      dock.querySelector('#dp-sc').onclick = function () { if (SEC) { if (!isSec(cur())) goto_(SEC.a - 1); else openDr(SEC.links); } };
      var cs = dock.querySelector('#dp-cs'); if (cs) cs.onclick = function () { openDr(L); };
      /* pastille de suite */
      var ne = nextEx(k), hh = '', hg = -1;
      if (DP.hint !== false && o) {
        if (ne > k && ne - k <= 6 && !exOf(k)) { hh = 'Exercice dans ' + (ne - k) + ' diapo' + (ne - k > 1 ? 's' : '') + ' : <b>' + esc(title(ne)).slice(0, 40) + '</b> ›'; hg = ne; }
        else if (o.b === k + 1 && q < SEQ.length - 1) { hh = 'Suite : <b>' + esc(SEQ[q + 1].n) + '</b> ›'; hg = o.b; }
      }
      hint.hidden = !hh; hint.innerHTML = hh; hint.onclick = function () { if (hg >= 0) goto_(hg); };
      if (rail) [].forEach.call(rail.children, function (i, j) { i.classList.toggle('cur', j === q); i.classList.toggle('done', j < q); });
      /* bandeau de transition */
      if (q !== lastQ && o) {
        if (lastQ !== -2) {
          ban.className = 'dp-ban' + (sec ? ' sec' : ''); void ban.offsetWidth;
          ban.innerHTML = '<small>' + (sec ? 'Prévention et secours' : 'Séquence ' + (q + 1) + ' sur ' + SEQ.length) + '</small>' + esc(o.t || o.n);
          ban.className = 'dp-ban on' + (sec ? ' sec' : '');
        }
        lastQ = q;
      }
    }
    new MutationObserver(function () { refresh(); }).observe(document.body, { attributes: true, subtree: true, attributeFilter: ['class'] });
    refresh(); setInterval(refresh, 800);

    document.addEventListener('keydown', function (e) {
      var t = (e.target && e.target.tagName) || ''; if (/INPUT|TEXTAREA|SELECT/.test(t) && e.key !== 'Escape') return;
      if (e.ctrlKey || e.metaKey || e.altKey) return;
      var k = e.key;
      if (k === 'p' || k === 'P') { e.preventDefault(); togglePlan(); }
      else if (k === 's' || k === 'S') { e.preventDefault(); document.getElementById('dp-sc') && document.getElementById('dp-sc').click(); }
      else if (k === 'l' || k === 'L') { e.preventDefault(); if (dr.classList.contains('on')) closeDr(); else { var kk = cur(), q = seqOf(kk), o = q >= 0 ? SEQ[q] : null, xx = EX[kk + 1], base = isSec(kk) ? SEC.links : (o ? o.links : []); openDr((xx && xx !== true ? xx : []).concat(base)); } }
      else if (k === 'Escape') { if (plan.classList.contains('on')) plan.classList.remove('on'); else if (dr.classList.contains('on')) closeDr(); }
    }, true);
    window.DPlus = { goto: goto_, open: openDr, plan: togglePlan };
  }
})();
