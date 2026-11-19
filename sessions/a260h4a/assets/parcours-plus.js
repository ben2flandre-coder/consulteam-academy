/* Consulteam · parcours-plus : un parcours lisible pour l'apprenant.
   Aperçu par jour, durée de lecture, objectif, renvois, suivi local (navigateur uniquement), barre de position.
   Lecture seule du contenu existant ; sans JavaScript la page reste complète. Config : window.PP. */
(function () {
  'use strict';
  var PP = window.PP || {};
  function ready(f) { if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', f); else f(); }
  function esc(t) { return String(t == null ? '' : t).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  var CSS = '' +
    '.pp-over{margin:18px 0 26px;padding:18px 18px 14px;border-radius:16px;background:#fff;border:1px solid #cfd9e6;box-shadow:0 2px 10px rgba(16,44,83,.07)}' +
    '.pp-over h2{margin:0 0 4px;font-size:clamp(20px,2.4vw,26px);border:0;padding:0}.pp-over h2:before{display:none}.pp-over .sub{margin:0 0 12px;color:#4a5b70;font-size:16px}' +
    '.pp-bar{height:12px;border-radius:99px;background:#dbe5f0;overflow:hidden;margin:6px 0 4px}.pp-bar i{display:block;height:100%;width:0;background:linear-gradient(90deg,#2e9e6a,#5cc08a);transition:width .4s}' +
    '.pp-top{display:flex;gap:12px;align-items:center;flex-wrap:wrap;margin:8px 0 14px}.pp-top .t{color:#4a5b70;font-size:15px}' +
    '.pp-go{display:inline-flex;gap:8px;align-items:center;background:#102c53;color:#fff!important;text-decoration:none;font-weight:700;padding:10px 16px;border-radius:12px;font-size:16px}.pp-go:hover{background:#1b4378}' +
    '.pp-days{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:14px}.pp-day{border:1px solid #cfd9e6;border-radius:14px;overflow:hidden;background:#f7fafd}.pp-day h3{margin:0;padding:10px 14px;background:#102c53;color:#fff;font-size:17px}' +
    '.pp-day ol{list-style:none;margin:0;padding:6px}.pp-step{display:flex;gap:10px;align-items:flex-start;padding:9px 8px;border-radius:10px;text-decoration:none;color:#14283f!important;border:1px solid transparent}.pp-step:hover{background:#fff;border-color:#9ec3da}' +
    '.pp-step .n{flex:none;width:30px;height:30px;border-radius:50%;background:#dbe5f0;color:#102c53;font:800 14px/30px system-ui,sans-serif;text-align:center}.pp-step.done .n{background:#2e9e6a;color:#fff}.pp-step.cur .n{background:#f6b63d;color:#102c53}' +
    '.pp-step b{display:block;font-size:16px;line-height:1.25}.pp-step small{display:block;color:#566a80;font-size:13.5px;margin-top:2px}.pp-step.sos .n{background:#c62828;color:#fff}' +
    '.pp-sosrow{margin-top:12px}' +
    '.pp-meta{display:flex;gap:8px;align-items:center;flex-wrap:wrap;margin:-4px 0 12px;font-size:14.5px;color:#4a5b70}.pp-meta .badge{background:#102c53;color:#fff;border-radius:99px;padding:3px 11px;font-weight:700}.pp-meta .badge.j{background:#5a6f88}' +
    '.pp-goal{margin:0 0 12px;padding:10px 14px;border-left:5px solid #2e9e6a;background:#eaf6f0;border-radius:8px;color:#12392a;font-size:17px}.pp-goal b{color:#17613f}' +
    '.pp-links{display:flex;gap:8px;flex-wrap:wrap;margin:0 0 14px}.pp-links a{display:inline-flex;gap:6px;align-items:center;text-decoration:none;font-weight:600;font-size:14.5px;padding:7px 12px;border-radius:99px;border:1px solid #9ec3da;background:#fff;color:#102c53!important}.pp-links a:hover{background:#eaf3f9}.pp-links a.s{background:#c62828;color:#fff!important;border-color:#c62828}.pp-links a.e{border-color:#d9a441;background:#fff7e3}' +
    '.pp-end{display:flex;gap:10px;align-items:center;flex-wrap:wrap;justify-content:space-between;margin:20px 0 6px;padding:12px 14px;border-radius:12px;background:#f0f5fa;border:1px dashed #9ec3da}.pp-end button{font:700 15px system-ui,sans-serif;border:2px solid #2e9e6a;background:#fff;color:#17613f;border-radius:10px;padding:9px 14px;cursor:pointer}.pp-end button[aria-pressed="true"]{background:#2e9e6a;color:#fff}' +
    '.pp-end a{font-weight:700;text-decoration:none;color:#102c53;padding:9px 14px;border-radius:10px;background:#f6b63d}.pp-end a:hover{background:#ffc94f}' +
    '.pp-sticky{position:fixed;left:0;right:0;top:0;z-index:2147481000;background:rgba(16,44,83,.97);color:#fff;display:none;gap:8px;align-items:center;padding:7px 12px;font:600 14px system-ui,sans-serif;box-shadow:0 4px 14px rgba(0,0,0,.3)}.pp-sticky.on{display:flex}' +
    '.pp-sticky .ti{flex:1;min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}.pp-sticky .dots{display:flex;gap:4px}.pp-sticky .dots a{width:26px;height:26px;border-radius:50%;background:#2a4a78;color:#fff;font:700 12px/26px system-ui;text-align:center;text-decoration:none}.pp-sticky .dots a.done{background:#2e9e6a}.pp-sticky .dots a.cur{background:#f6b63d;color:#102c53}.pp-sticky a.sos{background:#c62828;color:#fff;text-decoration:none;border-radius:99px;padding:5px 11px}' +
    'body.pp-on header.top{position:static!important}h2[id^="s"]{scroll-margin-top:60px}' +
    '@media(max-width:700px){.pp-sticky .dots{display:none}.pp-days{grid-template-columns:1fr}}' +
    '@media print{.pp-sticky,.pp-end,.pp-links,.pp-top{display:none!important}}';
  var st = document.createElement('style'); st.textContent = CSS; document.head.appendChild(st);
  var KEY = 'pp.' + (PP.code || 'x') + '.done';
  function load() { try { return JSON.parse(localStorage.getItem(KEY) || '{}'); } catch (e) { return {}; } }
  var MEM = null;
  function save(o) { MEM = o; try { localStorage.setItem(KEY, JSON.stringify(o)); } catch (e) { } }
  function done() { return MEM || (MEM = load()); }
  var ICON = { c: '📖', e: '✍', s: '🚑', v: '✅', m: '🧰' };

  ready(function () { if (PP.mode === 'modules') adi(); else statik(); });

  /* ---------- plateformes à page de texte (A2703AA, A260B4A) ---------- */
  function statik() {
    document.body.classList.add('pp-on');
    var secs = [].slice.call(document.querySelectorAll('h2[id^="s"]')).filter(function (h) { return /^s\d+$/.test(h.id); });
    if (!secs.length) return;
    var days = {}, dayOf = {};
    [].forEach.call(document.querySelectorAll('h2[id^="j"]'), function (h) {
      if (!/^j\d+$/.test(h.id)) return; days[h.id] = h.textContent.trim();
      var n = h.nextElementSibling; while (n && !(n.tagName === 'H2' && /^j\d+$/.test(n.id))) { if (n.tagName === 'H2' && /^s\d+$/.test(n.id)) dayOf[n.id] = h.id; n = n.nextElementSibling; }
    });
    var info = secs.map(function (h, i) {
      var words = 0, figs = 0, n = h.nextElementSibling, last = h;
      while (n && n.tagName !== 'H2') { words += (n.textContent || '').split(/\s+/).length; figs += n.querySelectorAll ? n.querySelectorAll('figure').length : 0; last = n; n = n.nextElementSibling; }
      var title = h.textContent.replace(/^\d+\s*·\s*/, '').trim();
      return { id: h.id, h: h, title: title, num: i + 1, min: Math.max(2, Math.round(words / 170)), figs: figs, day: dayOf[h.id], endBefore: n, last: last };
    });
    var N = info.length;
    function eff(x) { return 'lecture ≈ ' + x.min + ' min' + (x.figs ? ' · ' + x.figs + ' schéma' + (x.figs > 1 ? 's' : '') : ''); }
    function nextTodo() { var d = done(); for (var i = 0; i < N; i++) if (!d[info[i].id]) return info[i]; return null; }

    /* aperçu */
    var intro = document.querySelector('nav.sommaire'), over = document.createElement('section'); over.className = 'pp-over'; over.setAttribute('aria-label', 'Votre parcours en un coup d’œil');
    var dayKeys = Object.keys(days);
    var h = '<h2>Votre parcours en un coup d’œil</h2><p class="sub">' + N + ' séquences. Lisez dans l’ordre ou allez directement à ce qui vous manque : le suivi reste dans ce navigateur, rien n’est envoyé.</p><div class="pp-top"><a class="pp-go" id="pp-resume" href="#"></a><span class="t" id="pp-count"></span></div><div class="pp-bar" role="progressbar" aria-valuemin="0" aria-valuemax="' + N + '"><i></i></div><div class="pp-days">';
    dayKeys.forEach(function (dk) {
      h += '<div class="pp-day"><h3>' + esc(days[dk]) + '</h3><ol>';
      info.filter(function (x) { return x.day === dk; }).forEach(function (x) {
        h += '<li><a class="pp-step" data-id="' + x.id + '" href="#' + x.id + '"><span class="n">' + x.num + '</span><span><b>' + esc(x.title) + '</b><small>lecture ≈ ' + x.min + ' min' + (PP.goals && PP.goals[x.id] ? ' · ' + esc(PP.goals[x.id].short) : '') + '</small></span></a></li>';
      });
      h += '</ol></div>';
    });
    h += '</div><div class="pp-sosrow"><a class="pp-step sos" href="secours.html"><span class="n">🚑</span><span><b>Accident ou malaise : que faire ?</b><small>Protéger, examiner, alerter, secourir. Passer le SST ou le MAC SST est très fortement recommandé.</small></span></a></div>';
    over.innerHTML = h;
    if (intro) intro.parentNode.insertBefore(over, intro); else info[0].h.parentNode.insertBefore(over, info[0].h);
    if (intro) { intro.style.fontSize = '14px'; intro.setAttribute('aria-label', 'Accès direct aux séquences'); }

    /* par séquence */
    info.forEach(function (x, i) {
      var g = PP.goals && PP.goals[x.id], L = (PP.links && PP.links[x.id]) || [];
      var meta = document.createElement('div'); meta.className = 'pp-meta';
      meta.innerHTML = '<span class="badge">Séquence ' + x.num + ' sur ' + N + '</span>' + (x.day ? '<span class="badge j">' + esc((days[x.day] || '').split('·')[0].trim()) + '</span>' : '') + '<span>' + eff(x) + '</span>';
      var after = x.h; x.h.parentNode.insertBefore(meta, x.h.nextSibling); after = meta;
      if (g) { var go = document.createElement('p'); go.className = 'pp-goal'; go.innerHTML = '<b>À la fin, vous saurez :</b> ' + esc(g.goal); after.parentNode.insertBefore(go, after.nextSibling); after = go; }
      if (L.length) { var lk = document.createElement('div'); lk.className = 'pp-links'; lk.innerHTML = L.map(function (l) { return '<a class="' + l[0] + '" href="' + esc(l[2]) + '">' + (ICON[l[0]] || '') + ' ' + esc(l[1]) + '</a>'; }).join(''); after.parentNode.insertBefore(lk, after.nextSibling); }
      var nxt = info[i + 1], end = document.createElement('div'); end.className = 'pp-end';
      end.innerHTML = '<button type="button" data-id="' + x.id + '" aria-pressed="false">✔ J’ai terminé cette séquence</button>' + (nxt ? '<a href="#' + nxt.id + '">Séquence ' + nxt.num + ' : ' + esc(nxt.title.split(':')[0]) + ' →</a>' : '<a href="evaluation.html">Passer à l’évaluation →</a>');
      x.endBefore ? x.endBefore.parentNode.insertBefore(end, x.endBefore) : x.last.parentNode.insertBefore(end, x.last.nextSibling);
    });

    /* barre de position */
    var sk = document.createElement('div'); sk.className = 'pp-sticky'; sk.setAttribute('role', 'navigation'); sk.setAttribute('aria-label', 'Position dans le parcours');
    sk.innerHTML = '<span class="ti"></span><span class="dots">' + info.map(function (x) { return '<a href="#' + x.id + '" data-id="' + x.id + '" title="' + esc(x.title) + '">' + x.num + '</a>'; }).join('') + '</span><a class="sos" href="secours.html">🚑 Secours</a>';
    document.body.appendChild(sk);
    var curId = null;
    function paint() {
      var d = done(), c = 0; info.forEach(function (x) { if (d[x.id]) c++; });
      [].forEach.call(document.querySelectorAll('.pp-step[data-id],.pp-sticky .dots a'), function (a) { var id = a.getAttribute('data-id'); a.classList.toggle('done', !!d[id]); a.classList.toggle('cur', id === curId); });
      [].forEach.call(document.querySelectorAll('.pp-end button'), function (b) { var on = !!d[b.getAttribute('data-id')]; b.setAttribute('aria-pressed', on ? 'true' : 'false'); b.textContent = on ? '✔ Séquence terminée (annuler)' : '✔ J’ai terminé cette séquence'; });
      over.querySelector('.pp-bar i').style.width = (c / N * 100) + '%'; over.querySelector('.pp-bar').setAttribute('aria-valuenow', c);
      over.querySelector('#pp-count').textContent = c + ' séquence' + (c > 1 ? 's' : '') + ' terminée' + (c > 1 ? 's' : '') + ' sur ' + N;
      var nt = nextTodo(), rs = over.querySelector('#pp-resume');
      if (nt) { rs.textContent = (c ? '▶ Reprendre : séquence ' : '▶ Commencer : séquence ') + nt.num; rs.href = '#' + nt.id; } else { rs.textContent = '✅ Parcours terminé : passer à l’évaluation'; rs.href = 'evaluation.html'; }
    }
    [].forEach.call(document.querySelectorAll('.pp-end button'), function (b) { b.addEventListener('click', function () { var d = done(), id = b.getAttribute('data-id'); if (d[id]) delete d[id]; else d[id] = 1; save(d); paint(); }); });
    function onScroll() {
      var y = 90, cur = null; info.forEach(function (x) { if (x.h.getBoundingClientRect().top < y) cur = x; });
      var past = over.getBoundingClientRect().bottom < 0;
      sk.classList.toggle('on', past);
      if (cur && cur.id !== curId) { curId = cur.id; sk.querySelector('.ti').textContent = 'Séquence ' + cur.num + '/' + N + ' · ' + cur.title; paint(); }
      else if (!cur && curId) { curId = null; paint(); }
    }
    window.addEventListener('scroll', onScroll, { passive: true }); window.addEventListener('resize', onScroll);
    paint(); onScroll();
  }

  /* ---------- plateforme à modules (ADI) ---------- */
  function adi() {
    var out = document.getElementById('out'); if (!out || !PP.days) return;
    function build() {
      if (out.querySelector('.pp-over') || !out.querySelector('h2') || out.textContent.indexOf('Mon objectif') < 0) return;
      if (typeof A === 'undefined' || !A.modules) return;
      var by = {}; A.modules.forEach(function (m) { by[m.id] = m; });
      var nd = function (id) { try { return typeof nDone === 'function' ? nDone(id) : 0; } catch (e) { return 0; } };
      var total = 0, fin = 0;
      var h = '<section class="pp-over" aria-label="Votre formation jour par jour"><h2>Votre formation, jour par jour</h2><p class="sub">Voici l’ordre suivi en salle. Cliquez sur un module pour le lire ; la pastille verte indique un module terminé (le suivi reste dans ce navigateur).</p><div class="pp-days">';
      PP.days.forEach(function (d) {
        h += '<div class="pp-day"><h3>' + esc(d.t) + '</h3>' + (d.note ? '<p class="sub" style="margin:8px 12px 0;font-size:14px">' + esc(d.note) + '</p>' : '') + '<ol>';
        d.ids.forEach(function (id, i) {
          var m = by[id]; if (!m) return; var n = nd(id); total++; if (n === 5) fin++;
          h += '<li><a class="pp-step' + (n === 5 ? ' done' : '') + (id === 8 || id === 23 ? ' sos' : '') + '" href="#m' + id + '"><span class="n">' + (n === 5 ? '✓' : (i + 1)) + '</span><span><b>' + esc(m.title) + '</b><small>Module ' + id + (n && n < 5 ? ' · ' + n + ' phase(s) sur 5' : '') + (id === 8 ? ' · secours' : '') + '</small></span></a></li>';
        });
        h += '</ol></div>';
      });
      h += '</div><div class="pp-sosrow"><a class="pp-step sos" href="secours.html"><span class="n">🚑</span><span><b>Accident ou malaise : que faire ?</b><small>Protéger, examiner, alerter, secourir. Passer le SST ou le MAC SST est très fortement recommandé.</small></span></a></div></section>';
      var d = document.createElement('div'); d.innerHTML = h;
      var first = out.querySelector('h2'); first.parentNode.insertBefore(d.firstChild, first);
    }
    new MutationObserver(function () { build(); }).observe(out, { childList: true });
    build();
  }
})();
