/* Atelier formatif : une réponse sélectionnée ne note pas la justification libre. */
(function(){'use strict';
document.addEventListener('DOMContentLoaded',function(){
  var host=document.getElementById('decision-cases');if(!host||!window.DecisionCases)return;
  var S=window.HStore||{get:function(){return null},set:function(){},del:function(){}};
  var views=[];
  function node(tag,cls,txt,parent){var n=document.createElement(tag);if(cls)n.className=cls;if(txt)n.textContent=txt;if(parent)parent.appendChild(n);return n;}
  DecisionCases.forEach(function(c,i){
    var saved={};try{saved=JSON.parse(S.get('decision-2-'+c.id)||'{}')}catch(e){}
    var box=document.getElementById(c.id)||node('section','decision-case',null,host);box.id=c.id;box.replaceChildren();
    node('span','eyebrow','Cas '+(i+1)+' · '+c.tag,box);node('h2','',c.title,box);
    var grid=node('div','decision-split',null,box);node('p','case-scene',c.scene,grid);
    var fig=node('figure','fig',null,grid),im=node('img','',null,fig);im.src='assets/svg/v20/'+c.image+'.svg';im.alt='Schéma de la situation : '+c.title;im.loading='lazy';
    var field=node('fieldset','case-options',null,box);node('legend','','Votre décision',field);
    c.options.forEach(function(o,j){var lb=node('label','',null,field),r=node('input','',null,lb);r.type='radio';r.name='decision-'+c.id;r.value=String(j);r.checked=String(saved.choice)===String(j);node('span','',o,lb);});
    var lb=node('label','f',null,box);node('span','','Justifier : quelle règle, quelle inconnue, quelle action ?',lb);var ta=node('textarea','',null,lb);ta.rows=3;ta.value=saved.reason||'';ta.id='reason-'+c.id;
    var status=node('p','case-status',null,box);status.setAttribute('role','status');
    var btn=node('button','btn','Comparer mon raisonnement',box);btn.type='button';
    var result=node('div','case-feedback',null,box);result.hidden=true;result.id='correction-'+c.id;btn.setAttribute('aria-controls',result.id);btn.setAttribute('aria-expanded','false');
    function answer(){var r=field.querySelector('input:checked');return r?Number(r.value):null;}
    function save(){S.set('decision-2-'+c.id,JSON.stringify({choice:answer(),reason:ta.value}));}
    function invalidate(){save();result.hidden=true;btn.setAttribute('aria-expanded','false');status.textContent='Réponse modifiée : comparer à nouveau le raisonnement.';}
    field.addEventListener('change',invalidate);ta.addEventListener('input',invalidate);
    btn.addEventListener('click',function(){var a=answer();
      if(a===null||!ta.value.trim()){status.textContent='Choisir une décision et écrire sa justification avant la comparaison.';if(a===null)field.querySelector('input').focus();else ta.focus();return;}
      save();result.replaceChildren();
      node('h3','',a===c.answer?'Choix cohérent avec le corrigé':'Décision à reprendre',result);
      node('p','',c.reason,result);node('h4','','Critères à discuter avec le formateur',result);
      var ul=node('ul','',null,result);c.checks.forEach(function(x){node('li','',x,ul);});
      node('p','case-variant','Si la situation change : '+c.variant,result);
      if(c.source_url){var p=node('p','source',null,result),aNode=node('a','',c.source_label,p);aNode.href=c.source_url;aNode.target='_blank';aNode.rel='noopener';}
      node('p','muted','La justification libre n’est pas notée automatiquement. La maîtrise pratique fait l’objet d’une observation séparée.',result);
      result.hidden=false;btn.setAttribute('aria-expanded','true');status.textContent='Corrigé affiché. Comparer les critères à votre justification.';
    });
    views.push({c:c,box:box,field:field,ta:ta,status:status,result:result,btn:btn,answer:answer});
  });
  document.getElementById('decision-print').addEventListener('click',function(){window.print();});
  document.getElementById('decision-export').addEventListener('click',function(){
    var data={version:'2.1',session:'260053A',nature:'Atelier formatif sans validation automatique de compétence',exporte:new Date().toISOString(),reponses:views.map(function(v){return{id:v.c.id,decision:v.answer()===null?null:v.c.options[v.answer()],justification:v.ta.value};})};
    var u=URL.createObjectURL(new Blob([JSON.stringify(data,null,2)],{type:'application/json'})),a=document.createElement('a');a.href=u;a.download='mes-decisions-260053a.json';a.click();setTimeout(function(){URL.revokeObjectURL(u);},1000);
  });
  document.getElementById('decision-reset').addEventListener('click',function(){views.forEach(function(v){S.del('decision-2-'+v.c.id);v.field.querySelectorAll('input').forEach(function(r){r.checked=false;});v.ta.value='';v.status.textContent='Réponse effacée.';v.result.hidden=true;v.btn.setAttribute('aria-expanded','false');});});
  if(location.hash){var id;try{id=decodeURIComponent(location.hash.slice(1));}catch(e){}var target=id&&document.getElementById(id);if(target)target.scrollIntoView();}
});})();
