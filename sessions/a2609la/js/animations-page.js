document.addEventListener('DOMContentLoaded',function(){
  var box=document.getElementById('anims'),embeds=document.querySelectorAll('.kn-embed');if(!box&&!embeds.length)return;var K=window.KnotAnim;
  function ficheSteps(P,F){var ev=K.crossings(P,false).map(function(x){return Math.max(x.i,x.j)/(P.length-1)}).sort(function(a,b){return a-b});
    return F.map(function(f){return{t:f.t,d:f.d,w:f.w,p:f.end?1:(f.p0!=null?f.p0:Math.min(.995,ev[f.ev]+.015))}})}
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
  function mount(k,s,full){var c=window.KNOTS[k];if(!c)return;
    if(full){var h=document.createElement('h2');h.textContent=c.title;s.appendChild(h);var intro=document.createElement('p');intro.innerHTML=c.intro||'';s.appendChild(intro)}else{var cap=document.createElement('p');cap.className='muted';cap.innerHTML='<strong>Animation : '+c.title+'.</strong> Tracé du trajet de la corde, repère visuel : elle ne montre ni la mise en tension ni les gestes de la main, et ne remplace pas la démonstration du formateur.';s.appendChild(cap)}
    var P=c.custom?c.custom.points:window.buildKnotPoints(c.kind,c.tail);
    var holder=document.createElement('div');holder.className='kn-pair';s.appendChild(holder);
    window.KnotAnim.create(holder,{title:c.title,points:P,occluder:c.occluder,flat:c.flat,ropeWidth:c.ropeWidth,palette:c.palette,caps:c.caps,fadeAt:c.fadeAt,steps:c.steps.length?c.steps:(c.fiche?ficheSteps(P,c.fiche):autoSteps(P,c)),startStep:0});
    var ph=(window.KNOT_PHOTOS||{})[k];if(ph&&ph.length){var g=document.createElement('div');g.className='kn-photos';var hd=document.createElement('p');hd.className='muted';hd.innerHTML='<strong>Planches pas à pas</strong> (toucher une planche pour l’agrandir) : dessins réalisés à partir du trajet de corde calculé, légendés selon la fiche. Elles ne remplacent pas la démonstration du formateur.';g.appendChild(hd);
      ph.forEach(function(x){var f=document.createElement('figure');f.className='photo';var im=document.createElement('img');im.src=x.src;im.alt=x.alt||x.cap;im.loading='lazy';im.addEventListener('error',function(){f.remove();if(!g.querySelector('figure'))g.remove()});var fc=document.createElement('figcaption');fc.textContent=x.cap;f.appendChild(im);f.appendChild(fc);g.appendChild(f)});holder.appendChild(g)}
  }
  if(box)Object.keys(window.KNOTS).forEach(function(k){var s=document.createElement('section');s.className='panel';s.id=k;box.appendChild(s);mount(k,s,true)});
  embeds.forEach(function(e){mount(e.dataset.knot,e,false)});
});
