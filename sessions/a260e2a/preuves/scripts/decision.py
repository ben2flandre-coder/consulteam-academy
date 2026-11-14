# Arbre de décision « Quel symbole pour quelle opération ? » — INRS ED 6127 (déc. 2020) §2.3 p. 10-11, §2.4 p. 11-12 [S29].
import json
NODES={
'start':{'q':"L'opération touche-t-elle des parties actives, leurs isolants, la continuité des masses ou les conducteurs de protection ?",'h':"C'est la définition d'une opération d'ordre électrique (NF C 18-510, citée par l'ED 6127).",
 'o':[('Oui, c\'est une opération d\'ordre électrique','nat'),('Non, aucune opération électrique','nonelec')]},
'nonelec':{'q':"Que fait la personne près de l'installation ?",'o':[('Elle utilise normalement du matériel électrique (ordinateur, aspirateur, perceuse…)','r_sens'),('Elle accède à une zone à risque électrique sans opération électrique (peinture, maçonnerie, nettoyage…)','r_b0')]},
'nat':{'q':"Quelle est la nature de l'opération ?",'o':[
 ('Manœuvrer un matériel : réarmer un disjoncteur, mettre hors ou sous tension','dom_man'),
 ('Mesurer, vérifier ou essayer seulement','dom_mve'),
 ('Consigner un ouvrage ou une installation','dom_c'),
 ('Remplacer à l\'identique un fusible, une lampe, un socle de prise, un interrupteur, raccorder à un circuit en attente, réarmer','r_bs'),
 ('Entretien, dépannage, recherche de panne, remplacement de matériels défectueux, mise en service partielle','r_br'),
 ('Travaux : création ou modification d\'une installation, remplacement d\'un coffret ou d\'une armoire','role'),
 ('Travaux en fouilles autour de canalisations isolées enterrées','r_bf'),
 ('Autre (photovoltaïque, batteries, essais particuliers…)','r_autre')]},
'dom_man':{'q':"Quel domaine de tension ?",'o':[('Basse tension','r_bem'),('Haute tension','r_hem')]},
'dom_mve':{'q':"Quel domaine de tension ?",'o':[('Basse tension','r_bemve'),('Haute tension','r_hemve')]},
'dom_c':{'q':"Quel domaine de tension ?",'o':[('Basse tension','r_bc'),('Haute tension','r_hc')]},
'role':{'q':"Quel est le rôle de la personne ?",'o':[('Exécutant (elle exécute les travaux)','vois_1'),('Chargé de travaux (elle prépare, dirige, balise et vérifie la bonne exécution)','vois_2')]},
'vois_1':{'q':"Les travaux ont-ils lieu au voisinage renforcé de pièces nues sous tension ?",'o':[('Non','dom_1'),('Oui','dom_1v')]},
'vois_2':{'q':"Les travaux ont-ils lieu au voisinage renforcé de pièces nues sous tension ?",'o':[('Non','dom_2'),('Oui','dom_2v')]},
'dom_1':{'q':"Quel domaine de tension ?",'o':[('Basse tension','r_b1'),('Haute tension','r_h1')]},
'dom_1v':{'q':"Quel domaine de tension ?",'o':[('Basse tension','r_b1v'),('Haute tension','r_h1v')]},
'dom_2':{'q':"Quel domaine de tension ?",'o':[('Basse tension','r_b2'),('Haute tension','r_h2')]},
'dom_2v':{'q':"Quel domaine de tension ?",'o':[('Basse tension','r_b2v'),('Haute tension','r_h2v')]},
}
def R(sym,txt,verif,mod,s='S29'): return {'r':sym,'t':txt,'v':verif,'m':mod,'s':s}
RES={
'r_sens':R('Pas d\'habilitation','Sensibilisation au risque électrique : pas d\'habilitation requise pour l\'utilisation normale du matériel électrique.',['Le matériel est-il en bon état et utilisé normalement ?'],[2]),
'r_b0':R('B0 · H0 · H0V','Opérations d\'ordre non électrique en zone à risque. Le symbole est suivi de « Exécutant » ou « Chargé de chantier ». L\'habilitation n\'est obligatoire que pour le chargé de chantier ; au voisinage, seules les opérations concourant à l\'exploitation et à la maintenance sont autorisées.',['Rôle : exécutant ou chargé de chantier ?','Zone de travail repérée et balisée ?','Voisinage : H0V si voisinage renforcé'],[4,18]),
'r_bs':R('BS','Intervention élémentaire sur circuits terminaux : maxi 400 V et 32 A en courant alternatif. Remplacement à l\'identique de fusibles BT, d\'une lampe, d\'un socle de prise, d\'un interrupteur ; raccordement à un circuit en attente protégé ; réarmement d\'un dispositif de protection. Uniquement hors tension et hors voisinage renforcé.',['Remplacement à l\'identique ?','Circuit hors tension, absence de tension vérifiée ?','Pas de voisinage renforcé ?','Tension et courant dans les limites ?'],[5,6,21]),
'r_br':R('BR','Intervention générale d\'entretien et de dépannage sur un matériel ou une partie d\'installation de faible étendue : recherche de panne, remplacement de matériels défectueux, mise en service partielle ; connexion et déconnexion en présence de tension sous conditions (maxi 500 V et 63 A, hors charge).',['Faible étendue ?','Consignation pour son propre compte nécessaire ?','Connexion ou déconnexion en présence de tension : conditions respectées ?'],[10,21,22]),
'r_bem':R('BE Manœuvre','Manœuvre de matériel électrique en basse tension : réarmer un disjoncteur, mettre hors ou sous tension. Le symbole BE doit être complété par l\'attribut Manœuvre.',['Attribut Manœuvre sur le titre ?','Fiche de manœuvre disponible ?'],[6,7]),
'r_hem':R('HE Manœuvre','Manœuvre de matériel électrique en haute tension. Le symbole HE doit être complété par l\'attribut Manœuvre.',['Attribut Manœuvre sur le titre ?','Domaine HTA ou HTB précisé ?','Fiche de manœuvre disponible ?'],[14]),
'r_bemve':R('BE Mesurage · Vérification · Essai','Opérations spécifiques en basse tension : le symbole BE doit être complété par un attribut (Mesurage, Vérification ou Essai). Les détails sont dans la NF C 18-510.',['Quel attribut exact ?','L\'opération reste-t-elle un mesurage, une vérification ou un essai ?'],[15]),
'r_hemve':R('HE Mesurage · Vérification · Essai','Opérations spécifiques en haute tension : le symbole HE doit être complété par un attribut (Mesurage, Vérification ou Essai).',['Quel attribut exact ?','Domaine HTA ou HTB précisé ?'],[15]),
'r_bc':R('BC','Consignation d\'un ouvrage ou d\'une installation électrique en basse tension.',['Chargé d\'exploitation identifié ?','Attestation de consignation en une ou deux étapes ?'],[11]),
'r_hc':R('HC','Consignation d\'un ouvrage ou d\'une installation électrique en haute tension.',['Chargé d\'exploitation identifié ?','Réquisition nécessaire ?','Domaine HTA ou HTB précisé ?'],[13]),
'r_b1':R('B1','Exécutant de travaux d\'ordre électrique en basse tension, hors voisinage renforcé.',['Consignation faite et attestation reçue ?'],[9]),
'r_b1v':R('B1V','Exécutant de travaux en basse tension au voisinage renforcé.',['V sur le titre ?','Protections collectives en place ?'],[9,18]),
'r_h1':R('H1','Exécutant de travaux d\'ordre électrique en haute tension, hors voisinage renforcé.',['Domaine HTA ou HTB précisé ?'],[12]),
'r_h1v':R('H1V','Exécutant de travaux en haute tension au voisinage renforcé.',['V sur le titre ?','Domaine HTA ou HTB précisé ?'],[12,18]),
'r_b2':R('B2','Chargé de travaux d\'ordre électrique en basse tension : préparer, diriger, baliser et vérifier la bonne exécution.',['Documents de travaux prêts ?'],[9]),
'r_b2v':R('B2V','Chargé de travaux en basse tension au voisinage renforcé. Pour les essais au voisinage renforcé en basse tension : B2V Essai.',['V sur le titre ?','Zone balisée et surveillée ?'],[9,18]),
'r_h2':R('H2','Chargé de travaux d\'ordre électrique en haute tension.',['Domaine HTA ou HTB précisé ?'],[12]),
'r_h2v':R('H2V','Chargé de travaux en haute tension au voisinage renforcé. H2V Essai pour les essais.',['V sur le titre ?','Domaine HTA ou HTB précisé ?'],[12,18]),
'r_bf':R('BF-HF','Travaux en fouilles dans l\'environnement des canalisations isolées enterrées. Seules opérations autorisées : dégagement d\'une canalisation enterrée ; sur canalisations rendues visibles, ouverture de fourreau, nettoyage à des fins d\'identification, ripage, soutènement, protection de câbles. Symbole prévu par l\'amendement A1 à la norme.',['Canalisation réellement isolée et enterrée ?','Opération dans la liste autorisée ?'],[]),
'r_autre':R('Voir NF C 18-510','Essais, vérifications, mesures particulières, installations photovoltaïques, batteries : l\'ED 6127 renvoie à la NF C 18-510, qui n\'est pas lue dans cette plateforme.',['Faire préciser l\'opération par l\'employeur','Consulter la norme'],[]),
}
def page_html():
    return ('<small>AIDE À LA DÉCISION</small><h1>Quel symbole pour quelle opération ?</h1><p class="lead">Répondez aux questions : l\'arbre propose le ou les symboles d\'habilitation à discuter avec l\'employeur, d\'après le tableau de choix de l\'INRS ED 6127. C\'est une aide de formation : le choix du symbole appartient à l\'employeur, qui tient compte de l\'activité et de l\'environnement électrique.</p><div id="arb" class="card"></div><p class="expl">Source : INRS ED 6127 (déc. 2020), §2.3 et §2.4 [S29]. Les limites détaillées sont dans la NF C 18-510 (payante, non reproduite) ; le référentiel INRS fait foi pour la formation.</p>')
JS=r'''<script>
var NODES=%s,RES=%s,arb=document.getElementById('arb'),hist=[];
function show(id){var n=NODES[id],r=RES[id],h='';
if(r){h+='<h2>Symbole proposé : '+E(r.r)+'</h2><p>'+E(r.t)+'</p><h3>À vérifier</h3><ul>'+r.v.map(function(x){return '<li>'+E(x)+'</li>'}).join('')+'</ul>';
if(r.m.length)h+='<p>Modules à revoir : '+r.m.map(function(i){var m=module(i);return '<a href="parcours.html#m'+i+'">'+i+'. '+E(m?m.title:'')+'</a>'}).join(' · ')+'</p>';
h+='<p class="expl">Source : INRS ED 6127, §2.3 et §2.4 [S29].</p>'}
else{h+='<h2>'+E(n.q)+'</h2>'+(n.h?'<p class="expl">'+E(n.h)+'</p>':'')+'<div class="opts">'+n.o.map(function(o){return '<button type="button" class="btn alt" data-n="'+o[1]+'" style="display:block;margin:.4rem 0;text-align:left">'+E(o[0])+'</button>'}).join('')+'</div>'}
h+='<p class="no-print">'+(hist.length?'<button type="button" class="ghost" data-back="1">← Question précédente</button> ':'')+'<button type="button" class="ghost" data-n="start" data-reset="1">Recommencer</button></p>';arb.innerHTML=h}
arb.addEventListener('click',function(e){var b=e.target.closest('button');if(!b)return;if(b.dataset.back){show(hist.pop());return}if(b.dataset.reset){hist=[];show('start');return}var cur=arb.dataset.cur;hist.push(cur||'start');arb.dataset.cur=b.dataset.n;show(b.dataset.n)});
var _s=show;show=function(id){arb.dataset.cur=id;_s(id)};show('start');</script>'''
def js(): return JS%(json.dumps(NODES,ensure_ascii=False),json.dumps(RES,ensure_ascii=False))
