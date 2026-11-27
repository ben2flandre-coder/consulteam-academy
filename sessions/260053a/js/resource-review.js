/* Visa déclaré par le relecteur, sans certification automatique du contenu. */
(function(){'use strict';document.addEventListener('DOMContentLoaded',function(){
var box=document.getElementById('video-review');if(!box)return;
function update(){var ids=['url','author','range','goal','limits','reviewer','date'],complete=ids.every(function(x){return document.getElementById('vr-'+x).value.trim();});
var u=document.getElementById('vr-url').value,valid=false;try{var parsed=new URL(u);valid=parsed.protocol==='https:';}catch(e){}
var ready=complete&&valid&&document.getElementById('vr-watched').checked,s=document.getElementById('vr-status');s.classList.toggle('ready',!!ready);
s.textContent=ready?'Visa de visionnage déclaré par '+document.getElementById('vr-reviewer').value+' le '+document.getElementById('vr-date').value+'. Vérifier la disponibilité du lien et la correspondance au matériel avant projection.':'Séquence non qualifiée pour la diffusion : compléter la revue et le visionnage avant projection.';}
box.addEventListener('input',update);box.addEventListener('change',update);document.getElementById('vr-print').addEventListener('click',function(){window.print();});update();
});})();
