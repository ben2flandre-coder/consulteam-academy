# Arbres de décision « Puis-je remplacer ? » : lampe, fusible, socle de prise.
# Périmètre BS : INRS ED 6127 (déc. 2020) §2.3-2.4 [S29] ; cas ED 325 n° 15 (lampe) et n° 20 (fusible) [S32] ; enchaînement hors tension / VAT / essai [R].
import json
LIM="Circuit terminal en basse tension, au plus 400 V et 32 A en courant alternatif, hors voisinage renforcé ?"
def common(prefix, obj, ident_q, ident_help, extra):
    T={}
    T[prefix+'0']={'q':"Votre titre d'habilitation en cours de validité comporte-t-il BS (ou BR, B1, B2 selon l'opération) et l'employeur vous a-t-il confié cette opération ?",'h':"Le titre est délivré par l'employeur, qui précise les opérations confiées [S29].",
      'o':[('Oui',prefix+'1'),('Non, ou je ne sais pas','STOP_hab')]}
    T[prefix+'1']={'q':ident_q,'h':ident_help,'o':[('Oui, remplacement à l\'identique',prefix+'2'),('Non, je change de type, de puissance ou j\'ajoute un point','STOP_modif')]}
    T[prefix+'2']={'q':LIM,'h':"Seuils de l'ED 6127 pour le BS : 400 V et 32 A en alternatif [S29].",'o':[('Oui',extra),('Non','STOP_limite')]}
    return T
NODES={}
NODES.update(common('l','lampe',"S'agit-il de remplacer à l'identique une lampe (même culot, même puissance maximale du luminaire) ?","Le remplacement d'une lampe fait partie des interventions élémentaires BS [S29].",'l3'))
NODES['l3']={'q':"Le local est-il humide ou mouillé, ou l'éclairage est-il provisoire ?",'h':"Cas ED 325 n° 15 : une lampe remplacée sans couper, sur un éclairage provisoire inadapté en sous-sol humide, a causé un décès [S32].",'o':[('Oui','l_mouille'),('Non','l4')]}
NODES['l_mouille']={'q':"Local mouillé : la lampe se remplace uniquement après coupure, avec un luminaire fermé ou une alimentation en très basse tension de sécurité. Le luminaire est-il de ce type et le circuit coupé ?",'o':[('Oui','l4'),('Non','STOP_mouille')]}
NODES['l4']={'q':"Le circuit est-il coupé en amont, le dispositif de coupure condamné et l'absence de tension vérifiée ?",'h':"Le BS n'intervient que hors tension [S29].",'o':[('Oui','OK_lampe'),('Non, pas encore','DO_coupure')]}
NODES.update(common('f','fusible',"S'agit-il de remplacer à l'identique un fusible basse tension (même type, même calibre) ?","Le remplacement à l'identique de fusibles BT est une intervention BS [S29]. Un fusible qui a fondu signale un défaut ou une surcharge : un calibre supérieur n'est jamais « l'identique ».",'f3'))
NODES['f3']={'q':"Le fusible a-t-il fondu sans cause connue (surcharge ou défaut non identifié) ?",'h':"Rechercher la panne relève d'un dépannage : symbole BR [S29].",'o':[('Oui, cause inconnue','STOP_panne'),('Non, cause identifiée et corrigée','f4')]}
NODES['f4']={'q':"Le circuit alimenté est-il à l'arrêt et déconnecté de sa charge (machine arrêtée, organe de coupure en amont ouvert) ?",'h':"Cas ED 325 n° 20 : un fusible de 200 A retiré sans arrêter la machine a provoqué un arc et des brûlures aux mains et au visage [S32]. Ne jamais séparer un circuit en charge avec un organe non prévu pour cela [S32].",'o':[('Oui','f5'),('Non','DO_arret')]}
NODES['f5']={'q':"Le circuit est-il condamné et l'absence de tension vérifiée sur tous les pôles ?",'h':"Cas ED 325 n° 26 : un pôle resté fermé n'avait pas été vérifié [S32].",'o':[('Oui','OK_fusible'),('Non, pas encore','DO_coupure')]}
NODES.update(common('p','prise',"S'agit-il de remplacer à l'identique un socle de prise de courant (même type, même calibre, même raccordement) ?","Le remplacement d'un socle de prise fait partie des interventions BS [S29]. Ajouter ou déplacer une prise modifie l'installation : ce sont des travaux (B1 ou B2) [S29].",'p3'))
NODES['p3']={'q':"Le circuit est-il coupé en amont, le dispositif de coupure condamné et l'absence de tension vérifiée (phase, neutre, terre) ?",'h':"Le BS n'intervient que hors tension [S29].",'o':[('Oui','p4'),('Non, pas encore','DO_coupure')]}
NODES['p4']={'q':"Le conducteur de protection est-il identifié et son raccordement conservé à l'identique ?",'h':"Cas ED 325 n° 9 et 17 : des conducteurs de protection et de phase intervertis ont rendu des masses dangereuses [S32].",'o':[('Oui','OK_prise'),('Non, repérage douteux','STOP_repere')]}
def R(kind,t,items=(),m=()): return {'k':kind,'t':t,'i':list(items),'m':list(m)}
RES={
'STOP_hab':R('stop',"Ne pas intervenir. Sans titre d'habilitation adapté, l'opération revient à une personne habilitée.",["Informer le responsable ou l'employeur","Signaler le matériel défectueux sans y toucher"],[5]),
'STOP_modif':R('stop',"Ce n'est plus un remplacement à l'identique : changer de type, de puissance ou ajouter un point modifie l'installation. Il faut un symbole adapté (BR pour un dépannage, B1 ou B2 pour des travaux) et, pour des travaux, un chargé de travaux [S29].",["Faire préciser l'opération par l'employeur","Vérifier le symbole du titre"],[9,10]),
'STOP_limite':R('stop',"Hors des limites du BS : consulter l'employeur et le chargé d'exploitation. Une intervention hors BS demande BR, B1 ou B2 selon l'opération [S29].",["Relever la tension et le courant du circuit","Vérifier l'absence de voisinage renforcé"],[5,10,18]),
'STOP_mouille':R('stop',"Ne pas remplacer : en local mouillé, il faut un luminaire fermé ou une alimentation en très basse tension de sécurité, et couper le circuit [S32]. Faire appel à un électricien habilité.",["Signaler l'éclairage inadapté","Ne jamais changer une lampe sous tension"],[8,23]),
'STOP_panne':R('stop',"Ne pas remettre un fusible au hasard : un fusible qui fond signale une surcharge ou un défaut. La recherche de panne relève du BR [S29].",["Ne pas augmenter le calibre","Faire diagnostiquer par une personne habilitée BR"],[10,23]),
'STOP_repere':R('stop',"Ne pas remettre sous tension. Une inversion phase et conducteur de protection rend les masses dangereuses [S32] : faire contrôler le raccordement par une personne habilitée.",["Repérer avant de déconnecter","Contrôler la continuité du conducteur de protection"],[15,23]),
'DO_coupure':R('do',"Avant de continuer : couper le circuit en amont, condamner le dispositif de coupure (cadenas ou étiquette), identifier le bon circuit, puis vérifier l'absence de tension avec un appareil adapté (voir les modules 5 et 6) [S29, R]. Revenez ensuite à la question.",["Identifier le circuit","Couper et condamner","Vérifier l'absence de tension"],[5,6,21]),
'DO_arret':R('do',"Arrêter d'abord l'installation ou la machine, puis ouvrir l'organe de coupure prévu à cet effet : on ne retire pas un fusible en charge [S32]. Revenez ensuite à la question.",["Arrêt de la machine","Ouverture de l'organe de coupure prévu"],[5,23]),
'OK_lampe':R('ok',"Vous pouvez remplacer la lampe, dans le cadre du BS [S29]. Déposer l'ancienne lampe, poser une lampe identique, puis remettre le circuit sous tension et vérifier l'éclairage [R].",["Lampe identique à celle d'origine","Ne remettre sous tension qu'après repose complète","Informer l'exploitant de la fin d'intervention"],[5,21]),
'OK_fusible':R('ok',"Vous pouvez remplacer le fusible à l'identique, dans le cadre du BS [S29]. Poser un fusible de même type et de même calibre, refermer le porte-fusible, puis remettre sous tension et constater que le circuit fonctionne [S29, R].",["Même type et même calibre","Remise sous tension par la procédure prévue","Signaler toute nouvelle fusion"],[5,21]),
'OK_prise':R('ok',"Vous pouvez remplacer le socle à l'identique, dans le cadre du BS [S29]. Raccorder phase, neutre et conducteur de protection comme à l'origine, refermer, puis remettre sous tension. Si un dispositif différentiel protège la prise, l'essayer avec son bouton test [S3, S4].",["Raccordement identique à l'origine","Conducteur de protection raccordé","Essai du différentiel au bouton test"],[5,21]),
}
START=[('Remplacer une lampe','l0'),('Remplacer un fusible','f0'),('Remplacer un socle de prise','p0')]
def page_html():
    return ('<small>AIDE À LA DÉCISION</small><h1>Puis-je remplacer ? Lampe, fusible, prise</h1><p class="lead">Trois arbres de décision pour les remplacements les plus courants du BS. Répondez aux questions : l\'arbre dit s\'il faut s\'arrêter, ce qu\'il faut faire avant, ou si le remplacement entre dans le cadre du BS.</p><div id="arb" class="card"></div><p class="expl">Sources : INRS ED 6127 (déc. 2020), §2.3 et §2.4 [S29] ; INRS ED 325, cas 9, 15, 17, 20 et 26 [S32] ; enchaînement des étapes [R]. Aide de formation : le périmètre de chaque titre reste fixé par l\'employeur ; limites détaillées dans la NF C 18-510. Contenu à valider par le formateur.</p>')
JS=r'''<script>
var NODES=%s,RES=%s,START=%s,arb=document.getElementById('arb'),hist=[],cur='start';
function show(id){cur=id;var n=NODES[id],r=RES[id],h='';
if(id==='start'){h='<h2>Que voulez-vous remplacer ?</h2><div class="opts">'+START.map(function(o){return '<button type="button" class="btn alt" data-n="'+o[1]+'" style="display:block;margin:.4rem 0;text-align:left">'+E(o[0])+'</button>'}).join('')+'</div>'}
else if(r){var t={stop:'Arrêtez-vous',do:'À faire avant de continuer',ok:'Remplacement possible'}[r.k];h+='<h2>'+t+'</h2><p>'+E(r.t)+'</p><ul>'+r.i.map(function(x){return '<li>'+E(x)+'</li>'}).join('')+'</ul>';
if(r.m.length)h+='<p>Modules à revoir : '+r.m.map(function(i){var m=module(i);return '<a href="parcours.html#m'+i+'">'+i+'. '+E(m?m.title:'')+'</a>'}).join(' · ')+'</p>'}
else{h+='<h2>'+E(n.q)+'</h2>'+(n.h?'<p class="expl">'+E(n.h)+'</p>':'')+'<div class="opts">'+n.o.map(function(o){return '<button type="button" class="btn alt" data-n="'+o[1]+'" style="display:block;margin:.4rem 0;text-align:left">'+E(o[0])+'</button>'}).join('')+'</div>'}
h+='<p class="no-print">'+(hist.length?'<button type="button" class="ghost" data-back="1">← Question précédente</button> ':'')+'<button type="button" class="ghost" data-reset="1">Recommencer</button></p>';arb.innerHTML=h}
arb.addEventListener('click',function(e){var b=e.target.closest('button');if(!b)return;if(b.dataset.back){show(hist.pop());return}if(b.dataset.reset){hist=[];show('start');return}hist.push(cur);show(b.dataset.n)});
show('start');</script>'''
def js(): return JS%(json.dumps(NODES,ensure_ascii=False),json.dumps(RES,ensure_ascii=False),json.dumps(START,ensure_ascii=False))
