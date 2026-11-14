'use strict';
// Adaptation isolée de la base : aucune modification du support de base.
document.head.insertAdjacentHTML('beforeend','<style>@media(max-width:720px){header button{position:static;margin-left:auto}header div{order:2}header button{order:3}aside nav{max-height:210px;overflow:auto}}.pz-warn{background:#fde8e6;border-left:5px solid #b3261e;padding:10px 14px;border-radius:6px;color:#4a0f0a}.pz-gal{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:14px}.pz-gal figure{margin:0}.pz-gal img{width:100%;height:auto;border:1px solid #d5dfeb;border-radius:12px}@media print{.pz-gal figure{break-inside:avoid}}</style>');
// Ordre des réponses mélangé (Fisher-Yates) une fois par chargement ; l’indice juste suit.
(function(){const sh=a=>{for(let i=a.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[a[i],a[j]]=[a[j],a[i]]}return a};
D.questions.forEach(q=>{const good=q.options[q.correct];const fixed=q.options.findIndex(o=>/toutes les|aucune des|ci-dessus/i.test(o));if(fixed>=0)return;q.options=sh(q.options.slice());q.correct=q.options.indexOf(good)})})();
D.sources.push(['INRS ED 6127 · L’habilitation électrique, démarche de prévention','https://www.inrs.fr/dam/inrs/CataloguePapier/ED/TI-ED-6127.pdf','BS, BR, BC : limites et recyclage ; édition de décembre 2020.']);
D.sources.push(['INRS ED 6109 · Consignations et déconsignations','https://www.inrs.fr/dam/inrs/CataloguePapier/ED/TI-ED-6109.pdf','Consignation électrique : séparation, condamnation, identification, VAT, mise à la terre et en court-circuit.']);
const e2Cases=[
 ['Tableau de répartition','On demande de remplacer un disjoncteur divisionnaire défectueux dans un tableau de bureau.','Hors du BS élémentaire si le remplacement n’entre pas dans le titre : vérifier le symbole, consigner, vérifier l’absence de tension sur tous les conducteurs actifs, puis remplacer par un appareil compatible. Voir le parcours, modules 19 à 22.',5],
 ['Équilibrage','Un tableau présente un neutre très chargé ; un collègue propose de déplacer des circuits d’une phase à l’autre.','Déplacer un circuit est une opération sur l’installation : elle suppose le symbole adapté et une préparation. Mesurer d’abord, sans modifier.',5],
 ['Centrale d’alarme incendie','Les batteries d’une centrale doivent être contrôlées ; l’alimentation secteur est accessible.','Identifier toutes les sources (secteur, batteries), appliquer la consignation de l’alimentation prévue et les consignes du fabricant ; ne pas se fier à l’extinction d’un voyant.',6],
 ['Pose en hauteur','Un détecteur doit être posé au plafond près d’un chemin de câbles alimenté.','Les risques s’ajoutent (hauteur et électricité) : consigner ou protéger le cheminement, vérifier l’absence de tension, organiser la pose avant de commencer.',4],
 ['Titre insuffisant','Un collègue au titre limité est invité à raccorder un nouveau départ.','Une opération non mentionnée sur le titre n’est pas autorisée : faire appel à un titulaire habilité ou faire évoluer le titre par l’employeur.',1]
];
const e2Cases0=cases;
cases=function(){e2Cases0();main.insertAdjacentHTML('beforeend',`<section class="card"><p class="eyebrow">COMPLÉMENTS A260E2A</p><h2>Cas tableau et sécurité incendie</h2><div class="grid">${e2Cases.map(([t,s,a,m])=>`<article class="card"><b>${E(t)}</b><p>${E(s)}</p><details><summary>Décision et justification</summary><p>${E(a)}</p><span class="muted">Séquence ${m}</span></details></article>`).join('')}</div></section>`)};
const e2Home=home;
home=function(){e2Home();main.insertAdjacentHTML('afterbegin',`<section class="card"><p class="eyebrow">A260E2A · LA SEYNE-SUR-MER · 14 AU 16 DÉCEMBRE 2026</p><h2>Cours de base de la formation initiale</h2><p>Ce cours reprend le socle et les habilitations B0, H0, H0V, BS, BE Manœuvre. Les modules par niveau (BR, BC, B1 à B2, H1 à HE) et l’appareillage d’un tableau sont dans le parcours.</p><div class="row"><a class="button primary" href="../parcours.html">Parcours par niveau</a><a class="button" href="../evaluation.html">Évaluation</a><a class="button" href="../galerie.html">Galerie</a><a class="button" href="../">Accueil de session</a></div></section>`)};
const e2Visuals=visuals;
visuals=function(){e2Visuals();main.insertAdjacentHTML('afterbegin','<section class="card"><h2>Galerie de la session</h2><p>Les images IA contrôlées et les schémas de la session sont dans la <a href="../galerie.html">galerie</a>.</p></section>')};
const e2Trainer=trainer;
trainer=function(){e2Trainer();main.insertAdjacentHTML('afterbegin','<div class="callout"><b>Espace formateur de la session</b> : <a href="../formateur.html">déroulé, matériel, points à valider</a>.</div>')};
['lightbox'].forEach(n=>{const sc=document.createElement('script');sc.src='../assets/'+n+'.js';document.head.appendChild(sc)});
render();
