'use strict';
// Adaptation isolée du socle : le support de base n'est pas modifié.
document.head.insertAdjacentHTML('beforeend','<style>@media(max-width:720px){header button{position:static;margin-left:auto}header div{order:2}header button{order:3}aside nav{max-height:210px;overflow:auto}}.pz-warn{background:#fde8e6;border-left:5px solid #b3261e;padding:10px 14px;border-radius:6px;color:#4a0f0a}.pz-gal{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:14px}.pz-gal figure{margin:0}.pz-gal img{width:100%;height:auto;border:1px solid #d5dfeb;border-radius:12px}@media print{.pz-gal figure{break-inside:avoid}}</style>');
// Ordre des réponses mélangé (Fisher-Yates) une fois par chargement ; l’indice juste suit.
(function(){const sh=a=>{for(let i=a.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[a[i],a[j]]=[a[j],a[i]]}return a};
D.questions.forEach(q=>{const good=q.options[q.correct];const fixed=q.options.findIndex(o=>/toutes les|aucune des|ci-dessus/i.test(o));if(fixed>=0)return;q.options=sh(q.options.slice());q.correct=q.options.indexOf(good)})})();

// Charte du site de la session : en-tête, navigation, titres, cartes.
document.head.insertAdjacentHTML('beforeend','<style>'+
':root{--navy:#102c53;--blue:#0b68ae;--amber:#f6b63d;--bg:#f3f5f8;--tint:#e8f1fb;--warm:#fff1d4;--line:#cbd5e1;--ff:Bahnschrift,"DIN Alternate","Segoe UI Semibold","Arial Narrow",system-ui,sans-serif}'+
'body{font-size:17px}'+
'header{position:sticky;top:0;z-index:30;background:#102c53!important;color:#fff;min-height:0;padding:10px 24px;gap:6px 24px;flex-wrap:wrap;border-bottom:6px solid transparent;border-image:repeating-linear-gradient(135deg,#f6b63d 0 14px,#102c53 14px 28px) 6}'+
'header img{width:auto!important;height:39px;max-width:none!important;background:none!important;padding:0!important}'+
'header div{flex:none!important}header b{font:700 18px/1.1 var(--ff);color:#fff}header span{color:#d6e8fa;font-size:13px}'+
'header nav.sitenav{display:flex;flex-wrap:wrap;gap:2px 6px;margin-left:auto}header nav.sitenav a{display:inline-block;color:#d6e8fa;text-decoration:none;padding:6px 11px;border-radius:6px;font-size:15px;font-weight:400}header nav.sitenav a:hover{background:#ffffff1f;color:#fff}header nav.sitenav a.on{background:#f6b63d;color:#102c53;font-weight:700}'+
'header button{background:#ffffff1f;color:#fff;border-color:#ffffff40}header button:hover{background:#ffffff38;color:#fff}'+
'aside nav a.active{background:#f6b63d;color:#102c53}aside nav a{font-family:var(--ff)}'+
'h1,h2,h3{font-family:var(--ff);color:var(--navy);letter-spacing:-.005em}main h2{display:flex;gap:12px;align-items:center}main h2::before{content:"";width:10px;height:26px;background:var(--amber);border-radius:2px;flex:none}'+
'.card{border-radius:10px;border-color:var(--line)}.modulecard{border-top:1px solid var(--line);border-left:8px solid var(--blue)}.grid a.card,.grid .card{transition:transform .15s,box-shadow .15s}'+
'button.primary,.button.primary{background:var(--navy);border-color:var(--navy);font-family:var(--ff)}.callout{border-left:7px solid var(--amber);background:var(--warm)}.tag{background:var(--navy);color:#fff;font-family:var(--ff)}.number{color:var(--navy)}.cover-rule{background:var(--amber)}'+
'body.night header{background:#102c53!important}body.night h1,body.night h2,body.night h3{color:#a9d0f5}body.night .tag{background:#244a77}'+
'@media(max-width:720px){header nav.sitenav{margin-left:0;width:100%}}'+
'</style>');
(function(){const h=document.querySelector('header');if(!h)return;const im=h.querySelector('img');if(im){im.src='../assets/img/logo-consulteam-groupe.png';im.alt='Consulteam Groupe'}
const L=[['../index.html','Accueil'],['../parcours.html','Parcours'],['#','Socle électrique',1],['../metiers.html','Cas par métier'],['../evaluation.html','Évaluation'],['../galerie.html','Galerie'],['../securite-ile.html','Sur l’île'],['../electricien.html','Électricien de métier'],['../animation.html','Mode animation'],['../formateur.html','Espace formateur']];
const n=document.createElement('nav');n.className='sitenav';n.setAttribute('aria-label','Site de la session');n.innerHTML=L.map(([u,t,on])=>'<a href="'+u+'"'+(on?' class="on" aria-current="page"':'')+'>'+t+'</a>').join('');
const b=h.querySelector('button');h.insertBefore(n,b||null)})();
const ezHome=home;
home=function(){ezHome();main.insertAdjacentHTML('afterbegin',`<section class="card"><p class="eyebrow">PAUL RICARD · ÎLE DES EMBIEZ · 24 ET 27 NOVEMBRE 2026</p><h2>Socle électrique : B0 · H0 · H0V · BS · BE Manœuvre</h2><p>Support complet de la formation initiale. Les cas par métier, la sécurité sur l’île et l’évaluation de la session sont sur le site de la session.</p><div class="row"><a class="button primary" href="../parcours.html">Parcours de la session</a><a class="button" href="../metiers.html">Cas par métier</a><a class="button" href="../securite-ile.html">Sur l’île</a><a class="button" href="../evaluation.html">Évaluation de la session</a><a class="button" href="../index.html">Accueil du site</a></div></section>`)};
trainer=function(){main.innerHTML=heading('ACCÈS RÉSERVÉ','Espace formateur','Le déroulé et les points de vigilance de la session sont dans l’espace formateur du site, protégé par e-mail et code.')+'<section class="card"><div class="row"><a class="button primary" href="../formateur.html">Ouvrir l’espace formateur</a><a class="button" href="#home">Retour au socle</a></div></section>'};
render();
