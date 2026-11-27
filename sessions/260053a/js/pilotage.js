/* Navigation formateur : le contexte d'animation est indépendant de la vue montrée. */
(function(){'use strict';document.addEventListener('DOMContentLoaded',function(){
var key='h-260053a-pilotage',page=location.pathname.split('/').pop(),q=new URLSearchParams(location.search),active=/^(index|formateur|formulaires|animation)\.html$/.test(page)||q.get('e')==='f';
try{if(active)sessionStorage.setItem(key,'1');active=active||sessionStorage.getItem(key)==='1';}catch(e){}
if(!active)return;
var menu=document.createElement('details');menu.className='pilotage';menu.id='pilotage-formateur';
var summary=document.createElement('summary');summary.textContent='Pilotage';summary.title='Naviguer entre les espaces · touche P';menu.appendChild(summary);
var nav=document.createElement('nav');nav.setAttribute('aria-label','Navigation du formateur entre les espaces');
var title=document.createElement('strong');title.textContent='Changer d’espace, garder le fil';nav.appendChild(title);
var items=[['Accueil complet','index.html?e=f'],['Reprendre le diaporama','animation.html?reprendre=1'],['Cours complet','apprenant.html?e=f'],['Nœuds et animations','noeuds.html?e=f'],['Cas terrain','decisions.html?e=f'],['Observer les équipements','observations.html?e=f'],['Fiches réflexes','fiches.html?e=f'],['Livret apprenant','livret.html'],['Préparer et évaluer','formulaires.html?e=f'],['Ressources et vidéos','videos.html?e=f'],['Vue participant','apprenants.html?e=p'],['Programme et périmètre','programme.html?e=f']];
items.forEach(function(item){var a=document.createElement('a');a.textContent=item[0];a.href=item[1];nav.appendChild(a);});
var help=document.createElement('p');help.textContent='Le diaporama reprend à la dernière vue quittée. Cette barre accompagne votre animation ; elle n’apparaît pas dans un parcours participant ouvert seul.';nav.appendChild(help);menu.appendChild(nav);
var top=document.querySelector('.dk-top');if(top){menu.classList.add('pilotage-deck');top.insertBefore(menu,top.querySelector('.cnt'));}else document.body.appendChild(menu);
document.addEventListener('keydown',function(e){if(/INPUT|TEXTAREA|SELECT/.test((e.target||{}).tagName||''))return;if(e.key==='p'||e.key==='P'){e.preventDefault();menu.open=!menu.open;}if(e.key==='Escape'&&menu.open){menu.open=false;summary.focus();}});
document.addEventListener('click',function(e){if(menu.open&&!menu.contains(e.target))menu.open=false;});
});})();
