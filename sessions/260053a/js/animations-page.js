document.addEventListener('DOMContentLoaded',function(){
  var box=document.getElementById('anims');if(!box)return;var K=window.KnotAnim;
  function autoSteps(P,c){
    var S=K.arclen(P),L=S[S.length-1],cr=K.crossings(P,false),ev=[];
    cr.forEach(function(x){var a=x.i,b=x.j,second=Math.max(a,b),secOver=(x.over==='i')?(a>b):(b>a);
      ev.push({s:second*(L/(P.length-1))/1,over:secOver})});
    /* conversion indice -> longueur */
    ev=cr.map(function(x){var si=Math.max(x.i,x.j),over=(x.i>x.j)?(x.over==='i'):(x.over==='j');return{p:(si/(P.length-1)),over:over}}).sort(function(a,b){return a.p-b.p});
    var steps=[{t:'Départ : le brin dormant',d:'La corde part du côté « brin dormant » (la partie qui reste en place). Suivre son trajet avec la pastille rose.',p:0.02}];
    ev.forEach(function(e,i){steps.push({t:'La corde passe '+(e.over?'DESSUS':'DESSOUS')+' le brin déjà en place',d:(e.over?'Le bout passe par-dessus le brin déjà posé : le brin du dessous reste visible par transparence de l’ombre.':'Le bout passe en dessous du brin déjà posé : il se glisse dans la boucle formée.')+' (passage '+(i+1)+' sur '+ev.length+')',p:Math.min(0.995,e.p+0.012)})});
    steps.push({t:'Le bout libre est sorti',d:c.fin,p:1,w:'Serrer, aligner les brins, laisser un bout libre suffisant, puis faire contrôler par le binôme.'});
    return steps}
  Object.keys(window.KNOTS).forEach(function(k){var c=window.KNOTS[k];
    var s=document.createElement('section');s.className='panel';s.id=k;var h=document.createElement('h2');h.textContent=c.title;s.appendChild(h);
    var intro=document.createElement('p');intro.innerHTML=c.intro||'';s.appendChild(intro);box.appendChild(s);
    var P=window.buildKnotPoints(c.kind,c.tail);
    window.KnotAnim.create(s,{title:c.title,points:P,steps:c.steps.length?c.steps:autoSteps(P,c),startStep:0});
  });
});
