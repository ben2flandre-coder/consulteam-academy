(function(){
'use strict';
/* Banque de questions. Chaque option : [texte, estLaBonne, pourquoi (si fausse)] — l'ordre des questions ET des options est tiré au hasard à chaque passage. */
var T={tms:'Comprendre les TMS',prep:'Évaluer et préparer',tr:'Transferts et aides techniques',aut:'Autonomie et dignité',sec:'Alerte et sécurité',cad:'Cadre et prévention'};
var MOD={tms:['cours/module-a-introduction.html','Module A — Introduction'],prep:['cours/module-e-evaluation.html','Module E — Évaluation'],tr:['cours/module-h-materiel.html','Module H — Matériel'],aut:['cours/module-g-metiers.html#aes','Module G — Métiers (aide à la personne)'],sec:['cours/module-f-prevention.html','Module F — Prévention'],cad:['cours/module-f-prevention.html','Module F — Prévention']};
var Q=[
{t:'tms',q:'Que signifie TMS ?',o:[['Troubles Musculo-Squelettiques',1],['Troubles Médicaux Sévères',0,'Ce n’est pas un sigle médical générique : il désigne des atteintes des muscles, tendons, nerfs et articulations liées à l’activité.'],['Traumatismes Musculaires Standards',0,'Un TMS n’est pas un traumatisme ponctuel : il s’installe progressivement sous l’effet de contraintes répétées.']],e:'Les TMS (Troubles Musculo-Squelettiques) touchent les muscles, tendons, nerfs et articulations. Ils s’installent progressivement.'},
{t:'tms',q:'Qu’est-ce qui explique l’apparition des TMS ?',o:[['Une combinaison de facteurs : efforts, répétition, postures contraignantes, organisation du travail, facteurs psychosociaux',1],['Uniquement le poids de la charge déplacée',0,'Le poids compte, mais ce n’est qu’un facteur parmi d’autres : répétitivité, postures, durée, organisation et contraintes psychosociales jouent aussi.'],['Uniquement l’âge ou la condition physique de la personne',0,'La situation de travail pèse lourd : on ne peut pas réduire les TMS à une fragilité individuelle.']],e:'Les TMS sont multifactoriels : on agit donc sur la situation de travail dans son ensemble (organisation, aménagement, aides techniques), pas seulement sur la personne.'},
{t:'prep',q:'Avant une mobilisation, quelle information doit guider le choix de la méthode ?',o:[['Les capacités, la compréhension et les appuis possibles du patient',1],['Le temps disponible',0,'Le temps contraint ne doit jamais dicter une méthode risquée : c’est l’évaluation de la personne qui oriente le choix.'],['La préférence habituelle du professionnel',0,'« On a toujours fait comme ça » n’est pas un critère : la méthode s’adapte à la personne et à la situation du moment.']],e:'Chaque mobilisation commence par l’évaluation des capacités réelles de la personne, de ses douleurs éventuelles et de son environnement.'},
{t:'prep',q:'Avant le transfert lit/fauteuil, quelle vérification fait partie de la préparation ?',o:[['Vérifier l’espace, les freins, les appuis et le matériel disponible',1],['Commencer le mouvement puis organiser l’espace',0,'Improviser l’espace en cours de mouvement expose à des contraintes et à des imprévus : on prépare avant d’agir.'],['Éviter de parler pour ne pas distraire le patient',0,'Expliquer ce qui va se passer fait partie de la sécurité : il aide la personne à participer.']],e:'La préparation de l’environnement limite les imprévus et sécurise les appuis, le matériel et les déplacements.'},
{t:'prep',q:'Vous devez repositionner un patient dans un lit médicalisé à hauteur réglable. Que faites-vous de la hauteur du lit ?',o:[['Je la règle à une hauteur de travail adaptée, freins mis, puis je la remets en position sécurisée',1],['Je laisse le lit en position basse, par sécurité',0,'Un lit trop bas oblige à se pencher : c’est une contrainte pour le dos du soignant. La position basse se remet après le soin, pas pendant.'],['Je n’y touche pas : on s’adapte au lit',0,'Régler le lit fait partie des moyens de prévention : c’est l’environnement qui s’adapte à l’activité, pas l’inverse.']],e:'Travailler à bonne hauteur évite de se pencher et de tordre le tronc. On remet ensuite le lit en position sécurisée, selon la procédure du service.'},
{t:'tr',q:'Quel est l’objectif prioritaire lors d’un transfert ?',o:[['Protéger le professionnel, sécuriser le patient et favoriser sa participation',1],['Effectuer le mouvement le plus vite possible',0,'La rapidité augmente le risque de chute, de douleur et d’effort excessif.'],['Faire le mouvement seul pour rester efficace',0,'Faire seul peut imposer des efforts inutiles : la prévention passe par l’aide humaine ou technique quand elle est nécessaire.']],e:'La prévention combine la sécurité du professionnel, celle de la personne accompagnée, son confort, sa dignité et son autonomie.'},
{t:'tr',q:'Si le patient ne peut pas participer suffisamment à un transfert, que faut-il faire ?',o:[['Demander une aide humaine ou choisir une aide technique adaptée',1],['Forcer progressivement le mouvement',0,'Forcer ne remplace jamais une méthode adaptée : on risque la douleur du patient et la blessure du soignant.'],['Le maintenir par les bras',0,'Porter une personne à bout de bras est précisément la contrainte qu’il faut supprimer.']],e:'L’absence de capacité suffisante impose de réévaluer la méthode. On ne compense jamais un risque par un effort supplémentaire.'},
{t:'tr',q:'Quel équipement peut convenir à une personne sans capacité de mise debout ?',o:[['Un lève-personne, si l’évaluation de la situation le confirme',1],['Une ceinture lombaire portée par le professionnel',0,'La ceinture lombaire du soignant n’apporte pas de protection démontrée et ne remplace pas une aide technique.'],['Une planche de transfert utilisée sans évaluation',0,'Une aide technique se choisit après évaluation : une planche suppose une capacité de participation que cette personne n’a pas.']],e:'L’aide technique se choisit en fonction des capacités du patient, de son état, de l’environnement et des procédures de l’établissement.'},
{t:'tr',q:'À quoi sert un drap de glisse lors d’une remontée dans le lit ?',o:[['À réduire les frottements pour limiter l’effort de traction',1],['À soulever plus facilement le patient du matelas',0,'Le drap ne sert pas à soulever : il fait glisser, ce qui supprime le port de charge.'],['À rendre inutile toute aide complémentaire',0,'Selon la situation, deux professionnels restent souvent nécessaires : le drap réduit l’effort, il ne le supprime pas.']],e:'Le drap de glisse réduit les frottements : l’effort devient une traction horizontale plutôt qu’un port de charge. Il se choisit et s’utilise selon la notice et les procédures.'},
{t:'aut',q:'Comment favoriser l’autonomie de la personne accompagnée ?',o:[['Expliquer, solliciter ses appuis possibles et respecter son rythme',1],['Faire le mouvement à sa place pour gagner du temps',0,'Tout faire à la place de la personne réduit ses capacités restantes et augmente l’effort du soignant.'],['Donner des consignes rapides sans vérifier sa compréhension',0,'Une consigne non comprise rend la participation impossible et le geste moins sûr.']],e:'La participation de la personne réduit les efforts inutiles et soutient ses capacités restantes, sans mettre quiconque en difficulté.'},
{t:'aut',q:'Quel principe protège la dignité du patient ?',o:[['Prévenir la personne, expliquer les étapes et préserver son intimité',1],['Choisir la technique la plus rapide',0,'La rapidité n’est pas un critère de dignité : elle peut même la compromettre.'],['Éviter de demander son accord pour aller plus vite',0,'Recueillir l’accord fait partie du soin : il respecte la personne et facilite sa participation.']],e:'La relation et la communication font partie de la sécurité. Elles permettent aussi de recueillir l’accord et la participation de la personne.'},
{t:'sec',q:'Quel comportement doit alerter pendant une mobilisation ?',o:[['Une douleur exprimée, une perte d’équilibre ou une compréhension insuffisante',1],['Un transfert qui prend plus de temps que prévu',0,'Prendre du temps n’est pas un signal d’alerte : c’est parfois la condition d’une mobilisation sûre.'],['Le souhait de préserver l’intimité du patient',0,'Préserver l’intimité est un droit de la personne, pas un signal de danger.']],e:'Ces signaux imposent d’interrompre ou d’adapter l’action, puis de solliciter le soutien nécessaire.'},
{t:'sec',q:'Un patient qui marche à votre bras perd l’équilibre. Que faites-vous ?',o:[['J’accompagne le mouvement vers une assise ou le sol, je protège sa tête et j’alerte',1],['Je le retiens de toutes mes forces pour éviter la chute',0,'Retenir un poids en chute par la force expose le soignant à une blessure grave, sans garantir de protéger la personne.'],['Je le lâche et je m’écarte immédiatement',0,'Abandonner la personne aggrave le risque de choc. Il faut l’accompagner et protéger, pas retenir ni lâcher.']],e:'Face à une perte d’équilibre : protéger, alerter, ne pas retenir par la force. La relève du sol se fait ensuite avec les moyens adaptés, jamais en portant la personne.'},
{t:'sec',q:'En fin de journée, vous ressentez une douleur au dos que vous reliez aux transferts. Que faire ?',o:[['La signaler (encadrement, médecine du travail) et interroger l’organisation et le matériel',1],['Attendre que ça passe, on s’habitue',0,'Un signal précoce permet d’agir avant que la douleur ne s’installe : l’ignorer favorise la chronicité.'],['Porter une ceinture lombaire pour continuer comme avant',0,'La ceinture ne traite pas la cause : c’est la situation de travail qu’il faut analyser et corriger.']],e:'Un signal précoce permet d’agir sur les causes (organisation, matériel, effectifs). Il peut aussi ouvrir la voie à une déclaration, selon la situation.'},
{t:'cad',q:'Qui doit évaluer les risques liés à la manutention et fournir les moyens de prévention ?',o:[['L’employeur, avec la participation des salariés',1],['Le seul salarié qui effectue les manutentions',0,'La prévention est une obligation de l’employeur (Code du travail, L.4121-1) : elle ne repose pas sur la seule vigilance du salarié.'],['Le patient ou sa famille',0,'Le patient n’a pas de responsabilité d’évaluation des risques professionnels.']],e:'L’employeur évalue les risques (DUERP), met en place les mesures de prévention, les moyens et la formation. Les salariés y contribuent par leur signalement et leur expertise du terrain.'},
{t:'cad',q:'La ceinture lombaire prévient-elle à elle seule les TMS ?',o:[['Non : son efficacité préventive n’est pas démontrée, elle ne remplace pas l’organisation et les aides techniques',1],['Oui, elle protège efficacement le dos',0,'Les connaissances disponibles ne démontrent pas d’effet protecteur : on ne s’en remet pas à un équipement individuel.'],['Oui, elle est recommandée pour tous',0,'Elle n’est pas une mesure de prévention recommandée : on agit d’abord sur la situation de travail.']],e:'La prévention efficace agit à la source : organisation, aménagement, aides techniques, formation. Un équipement individuel ne la remplace pas.'}
];

function shuffle(a){a=a.slice();for(var i=a.length-1;i>0;i--){var j=Math.floor(Math.random()*(i+1));var t=a[i];a[i]=a[j];a[j]=t;}return a;}
function esc(s){return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');}
var form=document.getElementById('quiz'),res=document.getElementById('resultat'),btnV=document.getElementById('btnValider'),btnR=document.getElementById('btnRecommencer'),prog=document.getElementById('progress');
var draw=[];
function build(){
  draw=shuffle(Q).map(function(q){return {q:q,o:shuffle(q.o)};});
  var h='';
  draw.forEach(function(d,i){
    h+='<fieldset class="q" id="q'+i+'"><legend><span class="tag">'+esc(T[d.q.t])+'</span><br>'+(i+1)+'. '+esc(d.q.q)+'</legend>';
    d.o.forEach(function(o,k){h+='<label><input type="radio" name="r'+i+'" value="'+k+'"><span>'+esc(o[0])+'</span></label>';});
    h+='<div class="verdict-zone" aria-live="polite"></div></fieldset>';
  });
  form.innerHTML=h;res.innerHTML='';res.style.display='none';
  btnV.style.display='inline-flex';btnR.style.display='none';updateProg();
}
function answered(){return draw.filter(function(d,i){return form.querySelector('input[name="r'+i+'"]:checked');}).length;}
function updateProg(){prog.textContent=answered()+' / '+draw.length+' réponses données';}
form.addEventListener('change',updateProg);
function valider(){
  var n=answered();
  if(n<draw.length&&!window.confirm('Il reste '+(draw.length-n)+' question(s) sans réponse. Elles seront comptées comme fausses. Valider quand même ?'))return;
  var score=0,bythem={};
  draw.forEach(function(d,i){
    var fs=document.getElementById('q'+i),sel=form.querySelector('input[name="r'+i+'"]:checked'),z=fs.querySelector('.verdict-zone');
    var good=d.o.findIndex(function(o){return o[1]===1;});
    var pick=sel?parseInt(sel.value,10):-1,ok=pick===good;
    bythem[d.q.t]=bythem[d.q.t]||{ok:0,n:0};bythem[d.q.t].n++;if(ok){score++;bythem[d.q.t].ok++;}
    fs.classList.add('done');
    var ls=fs.querySelectorAll('label');ls.forEach(function(l,k){var inp=l.querySelector('input');inp.disabled=true;if(k===good)l.classList.add('ok');else if(k===pick)l.classList.add('ko');});
    var v='<div class="verdict '+(ok?'good':'bad')+'">';
    if(ok){v+='<p class="lbl">Bonne réponse.</p><p>'+esc(d.q.e)+'</p>';}
    else{
      v+='<p class="lbl">'+(pick<0?'Question sans réponse.':'Pas tout à fait.')+'</p>';
      if(pick>=0)v+='<p><span class="lbl">Votre réponse :</span> '+esc(d.o[pick][0])+'<br><span class="lbl">Pourquoi ce n’est pas la bonne :</span> '+esc(d.o[pick][2]||'')+'</p>';
      v+='<p><span class="lbl">Bonne réponse :</span> '+esc(d.o[good][0])+'</p><p>'+esc(d.q.e)+'</p>';
    }
    z.innerHTML=v+'</div>';
  });
  var tot=draw.length,msg=score>=Math.ceil(tot*0.8)?'Excellent : vous maîtrisez les fondamentaux.':(score>=Math.ceil(tot*0.6)?'Bien : quelques points à reprendre ci-dessous.':'À consolider : reprenez les modules indiqués ci-dessous.');
  var h='<div class="score-box"><span class="score-value">'+score+' / '+tot+'</span><p>'+msg+'</p></div><div class="bilan"><h3>Bilan par thème</h3>';
  var weak=[];
  Object.keys(bythem).forEach(function(k){var b=bythem[k],pc=Math.round(100*b.ok/b.n);h+='<div class="theme-row"><span>'+esc(T[k])+'</span><div class="theme-bar" role="img" aria-label="'+pc+' %"><span style="width:'+pc+'%"></span></div><strong>'+b.ok+'/'+b.n+'</strong></div>';if(b.ok<b.n)weak.push(k);});
  if(weak.length){h+='<p style="margin-top:1rem"><strong>À revoir :</strong></p><ul class="list-styled">';var seen={};weak.forEach(function(k){var m=MOD[k];if(!seen[m[0]]){seen[m[0]]=1;h+='<li><a href="'+m[0]+'">'+esc(m[1])+'</a> <span style="color:#666">('+esc(T[k])+')</span></li>';}});h+='</ul>';}
  h+='<p class="no-print" style="margin-top:1rem"><button class="btn btn-outline" type="button" onclick="window.print()">Imprimer le bilan</button></p></div>';
  res.innerHTML=h;res.style.display='block';
  btnV.style.display='none';btnR.style.display='inline-flex';
  res.scrollIntoView({behavior:'smooth',block:'start'});
}
function recommencer(){build();window.scrollTo({top:0,behavior:'smooth'});}
btnV.addEventListener('click',valider);btnR.addEventListener('click',recommencer);
build();
})();
