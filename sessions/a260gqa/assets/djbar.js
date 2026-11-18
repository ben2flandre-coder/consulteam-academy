(function(){
var q=new URLSearchParams(location.search),d=q.get("dj"),e=parseInt(q.get("e"),10),D=window.__DJ||{};
var bar=document.getElementById("djbar");if(!bar||!D[d]||!(e>=1))return;
var S=D[d].ids,n=S.length;if(e>n)return;
var keys=Object.keys(D),here=S[e-1];
function href(k,i){var s=D[k].ids[i-1];return "m"+s[1]+".html?dj="+k+"&e="+i}
var h='<span class="pg">🧭 <b>'+D[d].t+'</b> · étape '+e+' sur '+n+' : '+here[0]+'</span>';
if(e>1)h+='<a href="'+href(d,e-1)+'">← Précédent</a>';
if(e<n)h+='<a class="nx" href="'+href(d,e+1)+'">Suivant →</a>';
else{var nk=keys[keys.indexOf(d)+1];h+=nk?'<a class="nx" href="'+href(nk,1)+'">Demi-journée suivante →</a>':'<a class="nx" href="valider.html">Se valider →</a>';h+='<a href="parcours.html#'+d+'">Fin de la demi-journée</a>'}
bar.innerHTML=h;bar.hidden=false;
})();