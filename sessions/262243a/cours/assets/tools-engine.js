/* ===================================================================
   Consul Team · ADONIS SANARY — Moteur des outils PMS & HSE
   Registres locaux (localStorage), calculateurs, audits et tableaux
   de bord. Aucune donnée ne quitte le navigateur. Conception et
   adaptation pédagogique : Benoît Deflandre.
   =================================================================== */
(() => {
  'use strict';
  const NS = 'adonisV4.';

  /* ---------- Utilitaires génériques ---------- */
  const uid = () => 'r' + Date.now().toString(36) + Math.random().toString(36).slice(2, 7);
  const todayISO = () => new Date().toISOString().slice(0, 10);
  const normalize = (s) => (s || '').toString().normalize('NFD').replace(/[̀-ͯ]/g, '').toLowerCase();
  const escapeHtml = (s) => (s == null ? '' : String(s)).replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));

  function loadArr(key) {
    try { const v = JSON.parse(localStorage.getItem(NS + key) || '[]'); return Array.isArray(v) ? v : []; }
    catch { return []; }
  }
  function saveArr(key, arr) { try { localStorage.setItem(NS + key, JSON.stringify(arr)); } catch { /* stockage indisponible */ } }
  function loadVal(key, fallback) {
    try { const raw = localStorage.getItem(NS + key); return raw == null ? fallback : JSON.parse(raw); }
    catch { return fallback; }
  }
  function saveVal(key, val) { try { localStorage.setItem(NS + key, JSON.stringify(val)); } catch { /* stockage indisponible */ } }

  function fmtDate(iso) {
    if (!iso) return '';
    const m = /^(\d{4})-(\d{2})-(\d{2})$/.exec(iso);
    return m ? `${m[3]}/${m[2]}/${m[1]}` : iso;
  }
  function daysUntil(iso) {
    if (!iso) return null;
    const target = new Date(iso + 'T00:00:00');
    if (isNaN(target)) return null;
    const now = new Date(); now.setHours(0, 0, 0, 0);
    return Math.round((target - now) / 86400000);
  }
  function csvCell(v) {
    const s = (v == null ? '' : String(v));
    return /[;"\n]/.test(s) ? '"' + s.replace(/"/g, '""') + '"' : s;
  }
  function downloadCSV(filename, columns, rows) {
    const head = columns.map((c) => csvCell(c.label)).join(';');
    const body = rows.map((r) => columns.map((c) => csvCell(r[c.name])).join(';')).join('\n');
    const csv = '﻿' + head + (body ? '\n' + body : '');
    const blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url; a.download = filename; document.body.appendChild(a); a.click(); a.remove();
    setTimeout(() => URL.revokeObjectURL(url), 1000);
  }
  function badge(text, cls) { return `<span class="badge badge-${cls || 'plain'}">${escapeHtml(text)}</span>`; }
  function badgeClass(map, value) { return (map && map[value]) || 'plain'; }
  function el(html) { const t = document.createElement('template'); t.innerHTML = html.trim(); return t.content.firstElementChild; }

  /* ---------- Rendu d'un champ de formulaire ---------- */
  function fieldHtml(key, f) {
    const id = `${key}-${f.name}`;
    let input;
    if (f.type === 'select') {
      const opts = f.options.map((o) => {
        const val = typeof o === 'object' ? o.value : o;
        const label = typeof o === 'object' ? o.label : o;
        return `<option value="${escapeHtml(val)}">${escapeHtml(label)}</option>`;
      }).join('');
      input = `<select id="${id}" name="${f.name}" ${f.required ? 'required' : ''}><option value="">— Choisir —</option>${opts}</select>`;
    } else if (f.type === 'textarea') {
      input = `<textarea id="${id}" name="${f.name}" rows="${f.rows || 3}" ${f.required ? 'required' : ''} placeholder="${escapeHtml(f.placeholder || '')}"></textarea>`;
    } else {
      input = `<input id="${id}" name="${f.name}" type="${f.type || 'text'}" ${f.required ? 'required' : ''} ${f.step != null ? `step="${f.step}"` : ''} ${f.min != null ? `min="${f.min}"` : ''} ${f.max != null ? `max="${f.max}"` : ''} placeholder="${escapeHtml(f.placeholder || '')}">`;
    }
    return `<label class="tool-field${f.wide ? ' wide' : ''}">${escapeHtml(f.label)}${f.required ? ' <span class="req">*</span>' : ''}${input}</label>`;
  }

  /* ---------- Registre générique (formulaire + tableau + CSV + recherche) ---------- */
  function mountRegister(cfg) {
    const mount = typeof cfg.mount === 'string' ? document.querySelector(cfg.mount) : cfg.mount;
    if (!mount) return null;
    const key = cfg.key;
    let data = loadArr(key);
    let editingId = null;
    const allFields = cfg.fields;
    const computedCols = cfg.computed || [];

    mount.innerHTML = `
      ${cfg.readOnly ? '' : `<form class="tool-form" novalidate>
        <div class="tool-form-grid">${allFields.map((f) => fieldHtml(key, f)).join('')}</div>
        <div class="tool-form-actions">
          <button type="submit" class="button primary tool-submit">${cfg.addLabel || 'Ajouter la ligne'}</button>
          <button type="button" class="button tool-cancel" hidden>Annuler la modification</button>
        </div>
      </form>
      <div class="tool-result" hidden></div>`}
      <div class="tool-toolbar">
        <p class="tool-count" aria-live="polite"></p>
        <div class="tool-actions">
          <label class="tool-search-label">Rechercher<input type="search" class="tool-search" placeholder="Filtrer les lignes…"></label>
          <button type="button" class="button small tool-csv">Exporter CSV ↓</button>
          <button type="button" class="button small tool-clear">Vider le registre</button>
        </div>
      </div>
      <div class="tablewrap"><table class="tool-table"><thead></thead><tbody></tbody></table></div>
      <p class="tool-empty" hidden>${cfg.emptyMessage || 'Aucune ligne enregistrée pour le moment. Utilisez le formulaire ci-dessus.'}</p>
    `;

    const form = mount.querySelector('.tool-form');
    const resultEl = mount.querySelector('.tool-result');
    const tbody = mount.querySelector('tbody');
    const thead = mount.querySelector('thead');
    const countEl = mount.querySelector('.tool-count');
    const emptyEl = mount.querySelector('.tool-empty');
    const searchEl = mount.querySelector('.tool-search');

    const tableCols = allFields.filter((f) => f.showInTable !== false).concat(computedCols.filter((c) => c.showInTable !== false));
    thead.innerHTML = '<tr>' + tableCols.map((f) => `<th>${escapeHtml(f.label)}</th>`).join('') + (cfg.readOnly ? '' : '<th>Actions</th>') + '</tr>';

    function readForm() {
      const rec = {};
      allFields.forEach((f) => { rec[f.name] = form.querySelector(`[name="${f.name}"]`).value.trim(); });
      computedCols.forEach((c) => { rec[c.name] = c.compute(rec); });
      return rec;
    }
    function writeForm(rec) {
      allFields.forEach((f) => { const i = form.querySelector(`[name="${f.name}"]`); if (i) i.value = rec[f.name] || ''; });
    }
    function clearForm() {
      if (!form) return;
      form.reset(); editingId = null;
      form.querySelector('.tool-submit').textContent = cfg.addLabel || 'Ajouter la ligne';
      form.querySelector('.tool-cancel').hidden = true;
    }

    function rowHtml(r) {
      const cells = tableCols.map((f) => {
        let val = r[f.name] || '';
        let display = f.type === 'date' ? fmtDate(val) : escapeHtml(val);
        if (cfg.badgeField === f.name && val) display = badge(val, badgeClass(cfg.badgeMap, val));
        return `<td data-label="${escapeHtml(f.label)}">${display || '<span class="muted">—</span>'}</td>`;
      }).join('');
      const extraActs = (cfg.rowActions || []).map((a, i) => `<button type="button" class="icon-btn" data-act="extra${i}">${escapeHtml(a.label)}</button>`).join('');
      const actionsCell = cfg.readOnly ? '' : `<td class="tool-row-actions" data-label="Actions">${extraActs}<button type="button" class="icon-btn" data-act="edit">Modifier</button><button type="button" class="icon-btn danger" data-act="del">Supprimer</button></td>`;
      return `<tr data-id="${r.id}">${cells}${actionsCell}</tr>`;
    }

    function render() {
      saveArr(key, data);
      const q = normalize(searchEl.value.trim());
      const rows = data.filter((r) => !q || allFields.some((f) => normalize(r[f.name]).includes(q)));
      tbody.innerHTML = rows.map(rowHtml).join('');
      emptyEl.hidden = data.length > 0;
      countEl.textContent = `${data.length} ligne${data.length > 1 ? 's' : ''} enregistrée${data.length > 1 ? 's' : ''}` + (q ? ` · ${rows.length} affichée${rows.length > 1 ? 's' : ''}` : '');
      if (window.AdonisTools) window.AdonisTools.refreshDashboards();
    }

    if (form) {
      form.addEventListener('input', (e) => { if (cfg.onFieldInput && e.target.name) cfg.onFieldInput(e.target.name, form); });
      form.addEventListener('submit', (e) => {
        e.preventDefault();
        const rec = readForm();
        if (editingId) {
          const idx = data.findIndex((d) => d.id === editingId);
          if (idx > -1) data[idx] = Object.assign({ id: editingId }, rec);
        } else {
          rec.id = uid();
          data.unshift(rec);
        }
        if (cfg.afterSave) cfg.afterSave(rec, resultEl);
        clearForm();
        render();
      });
      mount.querySelector('.tool-cancel').addEventListener('click', clearForm);
    }

    tbody.addEventListener('click', (e) => {
      const btn = e.target.closest('button[data-act]'); if (!btn) return;
      const tr = btn.closest('tr'); const id = tr.dataset.id;
      const rec = data.find((d) => d.id === id);
      if (btn.dataset.act === 'del') {
        if (confirm('Supprimer définitivement cette ligne ?')) { data = data.filter((d) => d.id !== id); render(); }
      } else if (btn.dataset.act === 'edit' && rec) {
        writeForm(rec); editingId = id;
        form.querySelector('.tool-submit').textContent = 'Enregistrer les modifications';
        form.querySelector('.tool-cancel').hidden = false;
        form.scrollIntoView({ behavior: 'smooth', block: 'start' });
      } else if (btn.dataset.act.startsWith('extra') && rec) {
        const idx = Number(btn.dataset.act.replace('extra', ''));
        const action = (cfg.rowActions || [])[idx];
        if (action) action.handler(rec);
      }
    });

    mount.querySelector('.tool-csv').addEventListener('click', () => downloadCSV(cfg.csvName || (key + '.csv'), tableCols, data));
    mount.querySelector('.tool-clear').addEventListener('click', () => {
      if (data.length && confirm('Vider entièrement ce registre ? Cette action est irréversible.')) { data = []; render(); }
    });
    searchEl.addEventListener('input', render);

    render();

    return {
      getAll: () => data,
      addRecord: (prefill) => {
        const rec = Object.assign({ id: uid() }, prefill);
        computedCols.forEach((c) => { if (rec[c.name] === undefined) rec[c.name] = c.compute(rec); });
        data.unshift(rec);
        render();
        return rec;
      },
      refresh: render
    };
  }

  /* ---------- Suggestion d'écart (suivi des températures) ---------- */
  function suggestEcart(seuil, mesureStr) {
    const mesure = parseFloat(String(mesureStr).replace(',', '.'));
    if (!seuil || isNaN(mesure)) return '';
    const s = seuil.replace(',', '.');
    let m;
    if ((m = s.match(/[≤<]=?\s*(-?\d+(\.\d+)?)/))) {
      const lim = parseFloat(m[1]);
      return mesure <= lim ? 'Conforme au seuil' : `Dépassement de ${(mesure - lim).toFixed(1)} °C`;
    }
    if ((m = s.match(/[≥>]=?\s*(-?\d+(\.\d+)?)/))) {
      const lim = parseFloat(m[1]);
      return mesure >= lim ? 'Conforme au seuil' : `Insuffisant de ${(lim - mesure).toFixed(1)} °C`;
    }
    const range = s.match(/(-?\d+(\.\d+)?)\s*(?:à|-|—|a)\s*(-?\d+(\.\d+)?)/);
    if (range) {
      const lo = parseFloat(range[1]), hi = parseFloat(range[3]);
      if (mesure >= lo && mesure <= hi) return 'Conforme au seuil';
      return mesure < lo ? `Sous le seuil bas (${(lo - mesure).toFixed(1)} °C)` : `Au-dessus du seuil haut (+${(mesure - hi).toFixed(1)} °C)`;
    }
    return '';
  }

  /* ---------- Historique compact (petites listes en lecture seule) ---------- */
  function renderHistoryList(mountSel, key, formatFn, limit) {
    const mount = document.querySelector(mountSel);
    if (!mount) return { push: () => {} };
    function render() {
      const items = loadArr(key).slice(0, limit || 8);
      mount.innerHTML = items.length
        ? `<ul class="tool-history">${items.map((it) => `<li>${formatFn(it)}</li>`).join('')}</ul>`
        : '<p class="muted small">Aucun historique pour le moment.</p>';
    }
    render();
    return {
      push: (item) => { const arr = loadArr(key); arr.unshift(item); saveArr(key, arr.slice(0, 50)); render(); if (window.AdonisTools) window.AdonisTools.refreshDashboards(); },
      all: () => loadArr(key)
    };
  }

  /* =========================================================
     PAGE OUTILS PMS
     ========================================================= */
  function initPMS() {
    if (!document.querySelector('[data-tool]') || !document.body.classList.contains('page-outils-pms')) return;

    const ncCfg = {
      key: 'pmsNC',
      mount: '[data-tool="pms-nc"]',
      csvName: 'registre-non-conformites-pms.csv',
      addLabel: 'Enregistrer la non-conformité',
      badgeField: 'statut',
      badgeMap: { Ouverte: 'bad', 'En cours': 'warn', 'Clôturée': 'good' },
      fields: [
        { name: 'date', label: 'Date du fait', type: 'date', required: true },
        { name: 'fait', label: 'Fait constaté', type: 'text', required: true, wide: true, placeholder: 'Ex. Chambre froide 2 relevée à 8°C ce matin' },
        { name: 'detection', label: 'Détection (qui / comment)', type: 'text' },
        { name: 'mesureImmediate', label: 'Mise en sécurité / mesure immédiate', type: 'text' },
        { name: 'cause', label: 'Cause à analyser', type: 'textarea' },
        { name: 'action', label: 'Action corrective', type: 'text' },
        { name: 'pilote', label: 'Pilote', type: 'text' },
        { name: 'echeance', label: 'Échéance', type: 'date' },
        { name: 'statut', label: 'Statut', type: 'select', required: true, options: ['Ouverte', 'En cours', 'Clôturée'] },
        { name: 'preuve', label: 'Preuve', type: 'text' },
        { name: 'verification', label: "Vérification de l'efficacité", type: 'select', options: ['À vérifier', 'Efficace', 'Insuffisante — à reprendre'] }
      ]
    };
    const ncRegister = mountRegister(ncCfg);

    mountRegister({
      key: 'pmsTemperature',
      mount: '[data-tool="pms-temperature"]',
      csvName: 'suivi-temperatures-pms.csv',
      addLabel: 'Enregistrer le relevé',
      badgeField: 'decision',
      badgeMap: { Conforme: 'good', 'Écart mineur — action immédiate': 'warn', 'Non conforme — produit écarté': 'bad' },
      onFieldInput(name, form) {
        const ecartInput = form.querySelector('[name="ecart"]');
        if (name === 'ecart') { ecartInput.dataset.auto = '0'; return; }
        if ((name === 'seuil' || name === 'mesure') && (!ecartInput.value || ecartInput.dataset.auto === '1')) {
          const v = suggestEcart(form.querySelector('[name="seuil"]').value, form.querySelector('[name="mesure"]').value);
          if (v) { ecartInput.value = v; ecartInput.dataset.auto = '1'; }
        }
      },
      fields: [
        { name: 'date', label: 'Date', type: 'date', required: true },
        { name: 'heure', label: 'Heure', type: 'time' },
        { name: 'zone', label: 'Zone / équipement', type: 'text', required: true, placeholder: 'Ex. Chambre froide 2' },
        { name: 'produit', label: 'Produit / opération', type: 'text' },
        { name: 'seuil', label: 'Seuil validé localement', type: 'text', placeholder: 'Ex. ≤ 4°C' },
        { name: 'mesure', label: 'Mesure relevée (°C)', type: 'number', step: '0.1' },
        { name: 'ecart', label: 'Écart constaté', type: 'text', placeholder: 'Suggéré automatiquement, à confirmer' },
        { name: 'decision', label: 'Décision', type: 'select', required: true, options: ['Conforme', 'Écart mineur — action immédiate', 'Non conforme — produit écarté'] },
        { name: 'preuve', label: 'Lot / preuve', type: 'text' },
        { name: 'visa', label: 'Visa', type: 'text' }
      ]
    });

    mountRegister({
      key: 'pmsReception',
      mount: '[data-tool="pms-reception"]',
      csvName: 'reception-tracabilite-pms.csv',
      addLabel: "Enregistrer la réception",
      badgeField: 'decision',
      badgeMap: { 'Accepté': 'good', 'Accepté sous réserve': 'warn', 'Refusé': 'bad' },
      fields: [
        { name: 'date', label: 'Date', type: 'date', required: true },
        { name: 'fournisseur', label: 'Fournisseur', type: 'text', required: true },
        { name: 'produit', label: 'Produit', type: 'text', required: true },
        { name: 'lot', label: 'Lot', type: 'text' },
        { name: 'dlc', label: 'DLC / DDM', type: 'date' },
        { name: 'etat', label: 'État constaté', type: 'select', options: ['Conforme visuellement', 'À surveiller', 'Anomalie constatée'] },
        { name: 'temperature', label: 'Température observée (°C)', type: 'number', step: '0.1' },
        { name: 'critere', label: 'Critère du site', type: 'text', placeholder: 'Ex. ≤ 4°C produits frais' },
        { name: 'decision', label: 'Décision', type: 'select', required: true, options: ['Accepté', 'Accepté sous réserve', 'Refusé'] },
        { name: 'action', label: 'Action', type: 'text' },
        { name: 'visa', label: 'Visa', type: 'text' }
      ]
    });

    mountRegister({
      key: 'pmsNettoyage',
      mount: '[data-tool="pms-nettoyage"]',
      csvName: 'plan-nettoyage-maintenance-pms.csv',
      addLabel: 'Ajouter la ligne',
      emptyMessage: 'Aucune ligne de plan pour le moment.',
      fields: [
        { name: 'zone', label: 'Zone / équipement', type: 'text', required: true },
        { name: 'operation', label: 'Produit utilisé / opération', type: 'text' },
        { name: 'frequence', label: 'Fréquence prévue', type: 'text', placeholder: 'Ex. Quotidien, hebdomadaire…' },
        { name: 'responsable', label: 'Responsable', type: 'text' },
        { name: 'controle', label: 'Méthode de contrôle', type: 'text' },
        { name: 'derniereRealisation', label: 'Dernière réalisation', type: 'date' },
        { name: 'preuve', label: 'Preuve (visa, photo, ticket…)', type: 'text' }
      ]
    });

    /* --- Calculateur de criticité HACCP (registre + calcul + justification) --- */
    mountRegister({
      key: 'pmsHaccpCalc',
      mount: '[data-tool="pms-haccp-calc"]',
      csvName: 'criticite-haccp-pms.csv',
      addLabel: 'Calculer et enregistrer',
      badgeField: 'classification',
      badgeMap: { 'Point critique — priorité 1': 'bad', 'Point sensible — surveillance renforcée': 'warn', 'Maîtrisé par les BPH': 'good' },
      rowActions: [{
        label: '→ Non-conformités',
        handler(rec) {
          if (!ncRegister) return;
          ncRegister.addRecord({
            date: todayISO(),
            fait: `Criticité HACCP : ${rec.point} — score ${rec.score}/27 (${rec.classification})`,
            detection: 'Calculateur de criticité HACCP',
            mesureImmediate: '', cause: rec.analyse || '', action: '',
            pilote: rec.pilote || '', echeance: rec.echeance || '',
            statut: 'Ouverte', preuve: '', verification: 'À vérifier'
          });
          alert("Ajouté au registre de non-conformités / plan d'actions PMS.");
        }
      }],
      fields: [
        { name: 'point', label: 'Point / danger observé', type: 'text', required: true, wide: true, placeholder: 'Ex. Maintien au chaud du buffet petit-déjeuner' },
        { name: 'frequence', label: 'Fréquence (survenue)', type: 'select', required: true, options: [{ value: '1', label: '1 — Rare' }, { value: '2', label: '2 — Occasionnelle' }, { value: '3', label: '3 — Fréquente' }] },
        { name: 'gravite', label: 'Gravité sanitaire', type: 'select', required: true, options: [{ value: '1', label: '1 — Mineure' }, { value: '2', label: '2 — Modérée' }, { value: '3', label: '3 — Grave' }] },
        { name: 'maitrise', label: 'Maîtrise actuelle', type: 'select', required: true, options: [{ value: '1', label: '1 — Bonne (mesures fiables)' }, { value: '2', label: '2 — Partielle' }, { value: '3', label: '3 — Faible ou inexistante' }] },
        { name: 'pilote', label: 'Pilote (si action à prévoir)', type: 'text' },
        { name: 'echeance', label: 'Échéance (si action à prévoir)', type: 'date' }
      ],
      computed: [
        { name: 'score', label: 'Score /27', showInTable: true, compute: (r) => (Number(r.frequence) || 0) * (Number(r.gravite) || 0) * (Number(r.maitrise) || 0) },
        {
          name: 'classification', label: 'Classement pédagogique', showInTable: true,
          compute: (r) => { const s = (Number(r.frequence) || 0) * (Number(r.gravite) || 0) * (Number(r.maitrise) || 0); return s >= 18 ? 'Point critique — priorité 1' : s >= 8 ? 'Point sensible — surveillance renforcée' : 'Maîtrisé par les BPH'; }
        },
        {
          name: 'analyse', label: 'Analyse', showInTable: false,
          compute: (r) => {
            const f = Number(r.frequence) || 0, g = Number(r.gravite) || 0, m = Number(r.maitrise) || 0, s = f * g * m;
            if (s >= 18) return `Score ${s}/27 : la combinaison fréquence/gravité/maîtrise place ce point en priorité, à traiter comme un point sensible renforcé avant validation par le référent PMS.`;
            if (s >= 8) return `Score ${s}/27 : au moins un facteur fragilise la situation. Surveillance renforcée et vérification régulière recommandées.`;
            return `Score ${s}/27 : les bonnes pratiques d'hygiène en place semblent suffisantes. Maintenir la surveillance de routine.`;
          }
        }
      ],
      afterSave(rec, resultEl) {
        resultEl.hidden = false;
        const cls = rec.classification === 'Point critique — priorité 1' ? 'bad' : rec.classification === 'Point sensible — surveillance renforcée' ? 'warn' : 'good';
        resultEl.innerHTML = `<p class="tool-result-score">Score : <b>${rec.score}/27</b> — ${badge(rec.classification, cls)}</p><p>${escapeHtml(rec.analyse)}</p><p class="small muted">Méthode et seuils pédagogiques Consul Team (Fréquence × Gravité × Maîtrise), non réglementaires — à confirmer et valider dans le PMS Adonis.</p>`;
      }
    });

    initAuditPMS(ncRegister);
    initDashboardPMS();
  }

  /* --- Audit interne PMS : grille en 10 catégories --- */
  const AUDIT_PMS = [
    { section: 'Hygiène du personnel et tenue', weight: 2, items: ['Tenue de travail dédiée, propre et changée régulièrement', 'Lavage des mains organisé (points d’eau, savon, essuie-mains, affichage)', 'Absence de bijoux ; protections de plaies visibles si besoin', 'Aptitude au poste et sensibilisation hygiène à jour'] },
    { section: 'Flux et organisation des locaux', weight: 2, items: ['Séparation des flux propre/sale respectée', 'Zones de stockage distinctes (sec, froid positif, froid négatif) identifiées', 'Locaux et équipements en bon état d’entretien général', 'Accès aux zones sensibles limité au personnel autorisé'] },
    { section: 'Réception des marchandises', weight: 2, items: ['Contrôle systématique à réception (aspect, température, DLC/DDM, emballage)', 'Bons de livraison conservés et exploitables', 'Procédure de refus formalisée en cas de non-conformité', 'Déchargement rapide, sans rupture de la chaîne du froid'] },
    { section: 'Maîtrise des températures (CCP)', weight: 3, items: ['Relevés de température réalisés selon la fréquence définie', 'Températures de stockage conformes aux seuils validés localement', 'Thermomètres/sondes étalonnés ou vérifiés périodiquement', 'Procédure d’action corrective formalisée en cas de dérive'] },
    { section: 'Nettoyage et désinfection', weight: 2, items: ['Plan de nettoyage-désinfection affiché et à jour', 'Traçabilité des opérations réalisées (fiches ou registre renseignés)', 'Produits et dosages conformes aux fiches techniques', 'Matériel de nettoyage dédié par zone'] },
    { section: 'Traçabilité', weight: 2, items: ['Étiquetage des denrées ouvertes/reconditionnées (date, contenu)', 'Conservation des étiquettes fournisseurs et lots pendant la durée requise', 'Capacité à retracer un produit de la réception au service', 'Gestion documentée des retraits/rappels le cas échéant'] },
    { section: 'Allergènes', weight: 2, items: ['Liste des 14 allergènes majeurs tenue à jour pour les plats proposés', 'Information client disponible et accessible', 'Prévention des contaminations croisées formalisée', 'Personnel sensibilisé à la gestion d’une demande allergène'] },
    { section: 'Maintenance et métrologie', weight: 2, items: ['Registre de maintenance des équipements sensibles tenu à jour', 'Vérification périodique des enceintes froides et de cuisson', 'Interventions correctives tracées et closes', 'Fréquences de maintenance définies pour les équipements clés'] },
    { section: 'Formation du personnel', weight: 2, items: ['Personnel formé à l’hygiène alimentaire selon le poste occupé', 'Attestations ou preuves de formation disponibles', 'Nouveaux arrivants sensibilisés avant prise de poste', 'Rappels ou briefings hygiène réalisés périodiquement'] },
    { section: 'Gestion des écarts et amélioration continue', weight: 2, items: ['Non-conformités enregistrées de façon systématique', 'Actions correctives tracées avec pilote et échéance', 'Vérification de l’efficacité des actions réalisée', 'Audit interne PMS réalisé au moins une fois par an'] }
  ];

  function buildAuditGrid(mount, bank, formIdPrefix) {
    let html = '';
    let idx = 0;
    bank.forEach((sec, si) => {
      html += `<fieldset class="audit-section"><legend>${si + 1}. ${escapeHtml(sec.section)}</legend>`;
      sec.items.forEach((label) => {
        const id = `${formIdPrefix}-${idx}`;
        html += `<label class="audit-item" data-weight="${sec.weight}"><span>${escapeHtml(label)}</span><select id="${id}" name="${id}"><option value="">—</option><option value="${sec.weight}">✅ Conforme (${sec.weight} pt${sec.weight > 1 ? 's' : ''})</option><option value="${Math.ceil(sec.weight / 2)}">⚡ Partiel (${Math.ceil(sec.weight / 2)} pt${Math.ceil(sec.weight / 2) > 1 ? 's' : ''})</option><option value="0">❌ Non conforme (0 pt)</option></select></label>`;
        idx++;
      });
      html += `</fieldset>`;
    });
    mount.innerHTML = html;
    return idx;
  }

  function initAuditPMS(ncRegister) {
    const mount = document.querySelector('[data-tool="pms-audit"]');
    if (!mount) return;
    mount.innerHTML = `<form id="pms-audit-form" class="audit-form" novalidate></form>
      <div class="tool-form-actions">
        <button type="button" class="button primary" id="pms-audit-run">Calculer le score</button>
        <button type="button" class="button" id="pms-audit-plan">Générer le plan d'actions à partir des écarts</button>
        <button type="button" class="button" id="pms-audit-reset">Réinitialiser la grille</button>
      </div>
      <div class="tool-result" id="pms-audit-result" hidden></div>
      <h3>Derniers résultats</h3>
      <div id="pms-audit-history"></div>`;
    const form = mount.querySelector('#pms-audit-form');
    const itemCount = buildAuditGrid(form, AUDIT_PMS, 'pms-audit-item');
    const resultEl = mount.querySelector('#pms-audit-result');
    const history = renderHistoryList('#pms-audit-history', 'pmsAuditHistorique', (it) => `${fmtDate(it.date)} — Score ${it.pct}% — ${escapeHtml(it.niveau)}`);

    function evaluate() {
      let total = 0, max = 0; const gaps = [];
      let flatIdx = 0;
      AUDIT_PMS.forEach((sec) => {
        sec.items.forEach((label) => {
          const sel = form.querySelector(`#pms-audit-item-${flatIdx}`);
          const val = sel && sel.value !== '' ? Number(sel.value) : null;
          max += sec.weight;
          if (val != null) { total += val; if (val < sec.weight) gaps.push({ section: sec.section, label, val, weight: sec.weight }); }
          else gaps.push({ section: sec.section, label, val: 0, weight: sec.weight, unanswered: true });
          flatIdx++;
        });
      });
      const pct = max ? Math.round((total / max) * 100) : 0;
      const niveau = pct >= 85 ? 'Niveau satisfaisant' : pct >= 60 ? 'Progrès à engager' : 'Plan d’action prioritaire';
      return { total, max, pct, niveau, gaps };
    }

    mount.querySelector('#pms-audit-run').addEventListener('click', () => {
      const { total, max, pct, niveau, gaps } = evaluate();
      resultEl.hidden = false;
      const cls = pct >= 85 ? 'good' : pct >= 60 ? 'warn' : 'bad';
      resultEl.innerHTML = `<p class="tool-result-score">Score : <b>${total}/${max}</b> (${pct}%) — ${badge(niveau, cls)}</p>` +
        (gaps.length ? `<p><b>${gaps.length}</b> point(s) non pleinement conformes :</p><ul class="tool-gaps">${gaps.slice(0, 40).map((g) => `<li>${escapeHtml(g.section)} — ${escapeHtml(g.label)}</li>`).join('')}</ul>` : '<p>Aucun écart signalé sur cette session de réponses.</p>') +
        `<p class="small muted">Grille pédagogique interne Consul Team — ne constitue pas un audit officiel ni une certification.</p>`;
      history.push({ date: todayISO(), pct, niveau });
    });

    mount.querySelector('#pms-audit-plan').addEventListener('click', () => {
      const { gaps } = evaluate();
      if (!gaps.length) { alert('Calculez le score : aucun écart à transférer pour le moment.'); return; }
      if (!ncRegister) return;
      gaps.forEach((g) => {
        ncRegister.addRecord({
          date: todayISO(), fait: `Audit PMS — ${g.section} : ${g.label}`,
          detection: 'Audit interne PMS', mesureImmediate: '', cause: '', action: '',
          pilote: '', echeance: '', statut: 'Ouverte', preuve: '', verification: 'À vérifier'
        });
      });
      alert(`${gaps.length} écart(s) transféré(s) vers le registre de non-conformités.`);
    });

    mount.querySelector('#pms-audit-reset').addEventListener('click', () => { form.reset(); resultEl.hidden = true; });
  }

  /* --- Tableau de bord PMS --- */
  function renderDashboardPMS() {
    const mount = document.querySelector('[data-tool="pms-dashboard"]');
    if (!mount) return;
    const temp = loadArr('pmsTemperature');
    const reception = loadArr('pmsReception');
    const nc = loadArr('pmsNC');
    const nettoyage = loadArr('pmsNettoyage');
    const audits = loadArr('pmsAuditHistorique');
    const tempEcarts = temp.filter((t) => t.decision && t.decision !== 'Conforme').length;
    const receptionReserves = reception.filter((r) => r.decision && r.decision !== 'Accepté').length;
    const ncOuvertes = nc.filter((n) => n.statut !== 'Clôturée').length;
    const urgentes = nc.filter((n) => n.statut !== 'Clôturée' && n.echeance && daysUntil(n.echeance) !== null && daysUntil(n.echeance) <= 7).length;
    const dernierAudit = audits[0];
    mount.innerHTML = `
      <div class="kpi-grid">
        <div class="kpi-card"><span class="kpi-value">${temp.length}</span><span class="kpi-label">Relevés de température</span><span class="kpi-sub">${tempEcarts ? tempEcarts + ' écart(s)' : 'aucun écart'}</span></div>
        <div class="kpi-card"><span class="kpi-value">${reception.length}</span><span class="kpi-label">Réceptions enregistrées</span><span class="kpi-sub">${receptionReserves ? receptionReserves + ' réserve/refus' : 'sans réserve'}</span></div>
        <div class="kpi-card${ncOuvertes ? ' kpi-alert' : ''}"><span class="kpi-value">${ncOuvertes}/${nc.length}</span><span class="kpi-label">Non-conformités ouvertes</span><span class="kpi-sub">sur le registre PMS</span></div>
        <div class="kpi-card${urgentes ? ' kpi-alert' : ''}"><span class="kpi-value">${urgentes}</span><span class="kpi-label">Actions à échéance ≤ 7 jours</span><span class="kpi-sub">à traiter en priorité</span></div>
        <div class="kpi-card"><span class="kpi-value">${dernierAudit ? dernierAudit.pct + '%' : '—'}</span><span class="kpi-label">Dernier audit interne</span><span class="kpi-sub">${dernierAudit ? fmtDate(dernierAudit.date) + ' · ' + escapeHtml(dernierAudit.niveau) : 'aucun audit réalisé'}</span></div>
        <div class="kpi-card"><span class="kpi-value">${nettoyage.length}</span><span class="kpi-label">Lignes du plan nettoyage</span><span class="kpi-sub">nettoyage / maintenance</span></div>
      </div>`;
  }
  function initDashboardPMS() { renderDashboardPMS(); }

  /* =========================================================
     PAGE OUTILS HSE
     ========================================================= */
  function initHSE() {
    if (!document.body.classList.contains('page-outils-hse')) return;

    const actionsCfg = {
      key: 'hseActions',
      mount: '[data-tool="hse-actions"]',
      csvName: 'plan-actions-prevention-hse.csv',
      addLabel: "Enregistrer l'action",
      badgeField: 'statut',
      badgeMap: { Ouverte: 'bad', 'En cours': 'warn', 'Clôturée': 'good' },
      fields: [
        { name: 'date', label: 'Date', type: 'date', required: true },
        { name: 'action', label: 'Action de prévention', type: 'text', required: true, wide: true },
        { name: 'source', label: 'Source du risque', type: 'text', wide: true },
        { name: 'pilote', label: 'Pilote', type: 'text' },
        { name: 'echeance', label: 'Échéance', type: 'date' },
        { name: 'statut', label: 'Statut', type: 'select', required: true, options: ['Ouverte', 'En cours', 'Clôturée'] },
        { name: 'preuve', label: 'Preuve', type: 'text' },
        { name: 'verification', label: "Vérification de l'efficacité", type: 'select', options: ['À vérifier', 'Efficace', 'Insuffisante — à reprendre'] }
      ]
    };
    const actionsRegister = mountRegister(actionsCfg);

    mountRegister({
      key: 'hseEvrp',
      mount: '[data-tool="hse-evrp"]',
      csvName: 'cotation-evrp-hse.csv',
      addLabel: 'Calculer et enregistrer la cotation',
      badgeField: 'priorite',
      badgeMap: { 'Priorité 1 — action immédiate': 'bad', 'Priorité 2 — action à programmer': 'warn', 'Priorité 3 — surveiller': 'good' },
      rowActions: [{
        label: '→ Plan d’actions',
        handler(rec) {
          if (!actionsRegister) return;
          actionsRegister.addRecord({
            date: todayISO(), action: rec.action || `Traiter : ${rec.danger}`,
            source: `EvRP : ${rec.danger} (${rec.unite}) — score ${rec.score}/64, ${rec.priorite}`,
            pilote: rec.pilote || '', echeance: rec.echeance || '', statut: 'Ouverte', preuve: '', verification: 'À vérifier'
          });
          alert("Ajouté au plan d'actions prévention.");
        }
      }],
      fields: [
        { name: 'unite', label: 'Unité de travail', type: 'text', required: true, placeholder: 'Ex. Étages — service des chambres' },
        { name: 'danger', label: 'Danger / situation dangereuse', type: 'text', required: true, wide: true },
        { name: 'personnes', label: 'Personnes exposées', type: 'text', placeholder: 'Ex. 3 agents d’étage' },
        { name: 'gravite', label: 'Gravité', type: 'select', required: true, options: [{ value: '1', label: '1 — Bénigne (soins mineurs)' }, { value: '2', label: '2 — Modérée (arrêt sans séquelle)' }, { value: '3', label: '3 — Grave (séquelles)' }, { value: '4', label: '4 — Très grave (mortel/invalidant)' }] },
        { name: 'probabilite', label: 'Probabilité', type: 'select', required: true, options: [{ value: '1', label: '1 — Improbable' }, { value: '2', label: '2 — Peu probable' }, { value: '3', label: '3 — Probable' }, { value: '4', label: '4 — Quasi certaine / fréquente' }] },
        { name: 'maitrise', label: 'Exposition / maîtrise', type: 'select', required: true, options: [{ value: '1', label: '1 — Rare, bien maîtrisée' }, { value: '2', label: '2 — Occasionnelle, mesures partielles' }, { value: '3', label: '3 — Fréquente, mesures limitées' }, { value: '4', label: '4 — Permanente, aucune maîtrise' }] },
        { name: 'justification', label: 'Justification de la cotation', type: 'textarea', required: true, wide: true, placeholder: 'Pourquoi cette gravité, cette probabilité, cette maîtrise ?' },
        { name: 'mesures', label: 'Mesures de prévention existantes', type: 'textarea', wide: true },
        { name: 'action', label: 'Action envisagée', type: 'text' },
        { name: 'pilote', label: 'Pilote', type: 'text' },
        { name: 'echeance', label: 'Échéance', type: 'date' }
      ],
      computed: [
        { name: 'score', label: 'Score /64', compute: (r) => (Number(r.gravite) || 0) * (Number(r.probabilite) || 0) * (Number(r.maitrise) || 0) },
        { name: 'priorite', label: 'Priorité', compute: (r) => { const s = (Number(r.gravite) || 0) * (Number(r.probabilite) || 0) * (Number(r.maitrise) || 0); return s >= 32 ? 'Priorité 1 — action immédiate' : s >= 16 ? 'Priorité 2 — action à programmer' : 'Priorité 3 — surveiller'; } }
      ],
      afterSave(rec, resultEl) {
        resultEl.hidden = false;
        const cls = rec.priorite.startsWith('Priorité 1') ? 'bad' : rec.priorite.startsWith('Priorité 2') ? 'warn' : 'good';
        resultEl.innerHTML = `<p class="tool-result-score">Score : <b>${rec.score}/64</b> — ${badge(rec.priorite, cls)}</p><p class="small muted">Méthode Gravité × Probabilité × Exposition/maîtrise, seuils pédagogiques Consul Team. L'évaluation des risques et sa transcription au DUERP relèvent de l'employeur.</p>`;
      }
    });

    mountRegister({
      key: 'hseObservation',
      mount: '[data-tool="hse-observation"]',
      csvName: 'observations-terrain-hse.csv',
      addLabel: "Enregistrer l'observation",
      badgeField: 'type',
      badgeMap: { 'Observation de poste': 'info', 'Situation dangereuse': 'warn', 'Presque-accident': 'bad' },
      fields: [
        { name: 'date', label: 'Date', type: 'date', required: true },
        { name: 'type', label: 'Type', type: 'select', required: true, options: ['Observation de poste', 'Situation dangereuse', 'Presque-accident'] },
        { name: 'zone', label: 'Zone', type: 'text' },
        { name: 'personnes', label: 'Personnes concernées (nombre)', type: 'text' },
        { name: 'faits', label: 'Faits objectivés', type: 'textarea', required: true, wide: true, placeholder: 'Décrire les faits sans jugement ni donnée médicale' },
        { name: 'mesureImmediate', label: 'Mesure immédiate', type: 'text' },
        { name: 'transmission', label: 'Transmission à', type: 'text' },
        { name: 'suite', label: 'Suite donnée', type: 'text' }
      ]
    });

    mountRegister({
      key: 'hseControles',
      mount: '[data-tool="hse-controles"]',
      csvName: 'controles-hse.csv',
      addLabel: 'Enregistrer le contrôle',
      badgeField: 'resultat',
      badgeMap: { Conforme: 'good', 'Écart mineur': 'warn', 'Non conforme': 'bad' },
      fields: [
        { name: 'date', label: 'Date', type: 'date', required: true },
        { name: 'zone', label: 'Zone / équipement', type: 'text', required: true },
        { name: 'point', label: 'Point contrôlé', type: 'text' },
        { name: 'resultat', label: 'Résultat', type: 'select', options: ['Conforme', 'Écart mineur', 'Non conforme'] },
        { name: 'ecart', label: 'Écart constaté', type: 'text' },
        { name: 'action', label: 'Action', type: 'text' },
        { name: 'pilote', label: 'Pilote', type: 'text' },
        { name: 'echeance', label: 'Échéance', type: 'date' },
        { name: 'preuve', label: 'Preuve', type: 'text' }
      ]
    });

    mountRegister({
      key: 'hseCoactivite',
      mount: '[data-tool="hse-coactivite"]',
      csvName: 'preparation-coactivite-hse.csv',
      addLabel: 'Enregistrer la préparation',
      emptyMessage: 'Aucune coactivité préparée pour le moment.',
      fields: [
        { name: 'date', label: 'Date', type: 'date', required: true },
        { name: 'entreprise', label: 'Entreprise extérieure', type: 'text', required: true },
        { name: 'travaux', label: 'Nature des travaux', type: 'text' },
        { name: 'zone', label: 'Zone', type: 'text' },
        { name: 'interferences', label: 'Interférences identifiées', type: 'textarea', wide: true },
        { name: 'balisage', label: 'Accès / balisage prévu', type: 'text' },
        { name: 'coordination', label: 'Coordination (contact, fréquence des échanges)', type: 'text', wide: true },
        { name: 'decision', label: 'Décision / point de vigilance', type: 'text', wide: true }
      ]
    });

    initEvaluationFormativeHSE();
    initDashboardHSE();
  }

  /* --- Évaluation formative HSE --- */
  const EVAL_HSE_ITEMS = [
    'Identifie la situation dangereuse ou le risque présent dans le cas proposé',
    'Applique la conduite à tenir adaptée (alerte, mise en sécurité, balisage)',
    'Utilise le vocabulaire et les repères HSE appropriés (EvRP, plan d’actions, coactivité)',
    'Respecte le périmètre H0/B0 sans réaliser de geste électrique interdit',
    'Formalise une observation terrain de façon factuelle, sans jugement',
    'Propose une mesure de prévention réaliste et proportionnée',
    'Sait à qui transmettre l’information et dans quel délai',
    'Distingue ce qui relève de l’employeur (DUERP, habilitation) de sa propre vigilance'
  ];
  function initEvaluationFormativeHSE() {
    const mount = document.querySelector('[data-tool="hse-evaluation"]');
    if (!mount) return;
    mount.innerHTML = `<form id="hse-eval-form" class="audit-form" novalidate>
        <div class="tool-form-grid">
          <label class="tool-field">Nom du stagiaire (optionnel)<input id="hse-eval-stagiaire" type="text"></label>
          <label class="tool-field wide">Cas / mise en situation observée<input id="hse-eval-cas" type="text" placeholder="Ex. Cas Adonis — chariot d'entretien"></label>
        </div>
        <fieldset class="audit-section"><legend>Critères observables</legend>
          ${EVAL_HSE_ITEMS.map((label, i) => `<label class="audit-item"><span>${escapeHtml(label)}</span><select id="hse-eval-item-${i}"><option value="">—</option><option value="2">✅ Acquis</option><option value="1">⚡ À renforcer</option><option value="0">❌ Non observé</option></select></label>`).join('')}
        </fieldset>
      </form>
      <div class="tool-form-actions">
        <button type="button" class="button primary" id="hse-eval-run">Calculer le résultat</button>
        <button type="button" class="button" id="hse-eval-csv">Exporter l'historique CSV ↓</button>
        <button type="button" class="button" id="hse-eval-reset">Réinitialiser la grille</button>
      </div>
      <div class="tool-result" id="hse-eval-result" hidden></div>
      <h3>Derniers résultats</h3>
      <div id="hse-eval-history"></div>`;
    const history = renderHistoryList('#hse-eval-history', 'hseEvaluationHistorique', (it) => `${fmtDate(it.date)} — ${it.stagiaire ? escapeHtml(it.stagiaire) + ' — ' : ''}${it.pct}% — ${escapeHtml(it.niveau)}`);
    const resultEl = mount.querySelector('#hse-eval-result');

    mount.querySelector('#hse-eval-run').addEventListener('click', () => {
      let total = 0; const max = EVAL_HSE_ITEMS.length * 2; const reprises = [];
      EVAL_HSE_ITEMS.forEach((label, i) => {
        const sel = mount.querySelector(`#hse-eval-item-${i}`);
        const v = sel.value !== '' ? Number(sel.value) : 0;
        total += v;
        if (v < 2) reprises.push(label);
      });
      const pct = Math.round((total / max) * 100);
      const niveau = pct >= 85 ? 'Acquis' : pct >= 50 ? 'En progression' : 'À retravailler avant validation terrain';
      const cls = pct >= 85 ? 'good' : pct >= 50 ? 'warn' : 'bad';
      resultEl.hidden = false;
      resultEl.innerHTML = `<p class="tool-result-score">Résultat : <b>${total}/${max}</b> (${pct}%) — ${badge(niveau, cls)}</p>` +
        (reprises.length ? `<p><b>Axes de reprise :</b></p><ul class="tool-gaps">${reprises.map((r) => `<li>${escapeHtml(r)}</li>`).join('')}</ul>` : '<p>Tous les critères observables sont acquis.</p>') +
        `<p class="small muted">Grille pédagogique formative — ne délivre ni habilitation, ni certification.</p>`;
      history.push({ date: todayISO(), stagiaire: mount.querySelector('#hse-eval-stagiaire').value.trim(), cas: mount.querySelector('#hse-eval-cas').value.trim(), score: total, pct, niveau });
    });
    mount.querySelector('#hse-eval-csv').addEventListener('click', () => {
      downloadCSV('historique-evaluation-formative-hse.csv',
        [{ name: 'date', label: 'Date' }, { name: 'stagiaire', label: 'Stagiaire' }, { name: 'cas', label: 'Cas' }, { name: 'score', label: 'Score' }, { name: 'pct', label: '%' }, { name: 'niveau', label: 'Niveau' }],
        history.all());
    });
    mount.querySelector('#hse-eval-reset').addEventListener('click', () => { mount.querySelector('#hse-eval-form').reset(); resultEl.hidden = true; });
  }

  /* --- Tableau de bord HSE --- */
  function renderDashboardHSE() {
    const mount = document.querySelector('[data-tool="hse-dashboard"]');
    if (!mount) return;
    const evrp = loadArr('hseEvrp');
    const actions = loadArr('hseActions');
    const observation = loadArr('hseObservation');
    const controles = loadArr('hseControles');
    const coactivite = loadArr('hseCoactivite');
    const evaluations = loadArr('hseEvaluationHistorique');
    const prio1 = evrp.filter((e) => e.priorite === 'Priorité 1 — action immédiate').length;
    const actionsOuvertes = actions.filter((a) => a.statut !== 'Clôturée').length;
    const urgentes = actions.filter((a) => a.statut !== 'Clôturée' && a.echeance && daysUntil(a.echeance) !== null && daysUntil(a.echeance) <= 7).length;
    const obs30 = observation.filter((o) => o.date && daysUntil(o.date) !== null && daysUntil(o.date) >= -30).length;
    const controlesNC = controles.filter((c) => c.resultat === 'Non conforme').length;
    const derniereEval = evaluations[0];
    mount.innerHTML = `
      <div class="kpi-grid">
        <div class="kpi-card${prio1 ? ' kpi-alert' : ''}"><span class="kpi-value">${evrp.length}</span><span class="kpi-label">Cotations EvRP réalisées</span><span class="kpi-sub">${prio1 ? prio1 + ' en priorité 1' : 'aucune priorité 1'}</span></div>
        <div class="kpi-card${urgentes ? ' kpi-alert' : ''}"><span class="kpi-value">${actionsOuvertes}/${actions.length}</span><span class="kpi-label">Actions prévention ouvertes</span><span class="kpi-sub">${urgentes} à échéance ≤ 7 jours</span></div>
        <div class="kpi-card"><span class="kpi-value">${obs30}</span><span class="kpi-label">Observations terrain (30 j)</span><span class="kpi-sub">${observation.length} au total</span></div>
        <div class="kpi-card${controlesNC ? ' kpi-alert' : ''}"><span class="kpi-value">${controlesNC}</span><span class="kpi-label">Contrôles non conformes</span><span class="kpi-sub">sur ${controles.length} contrôle(s)</span></div>
        <div class="kpi-card"><span class="kpi-value">${coactivite.length}</span><span class="kpi-label">Coactivités préparées</span><span class="kpi-sub">entreprises extérieures</span></div>
        <div class="kpi-card"><span class="kpi-value">${derniereEval ? derniereEval.pct + '%' : '—'}</span><span class="kpi-label">Dernière évaluation formative</span><span class="kpi-sub">${derniereEval ? fmtDate(derniereEval.date) + ' · ' + escapeHtml(derniereEval.niveau) : 'aucune évaluation'}</span></div>
      </div>`;
  }
  function initDashboardHSE() { renderDashboardHSE(); }

  /* ---------- Amorçage ---------- */
  window.AdonisTools = {
    refreshDashboards() { renderDashboardPMS(); renderDashboardHSE(); }
  };
  document.addEventListener('DOMContentLoaded', () => { initPMS(); initHSE(); });
})();
