/* Graphique lié aux mêmes contrôles et au même calcul que le support. */
(function(){'use strict';document.addEventListener('DOMContentLoaded',function(){
var form=document.getElementById('ta-form'),box=document.getElementById('measure-visual');
if(form&&box&&window.HeightTools){function draw(){var r=HeightTools.clearance(document.getElementById('ta1').value,document.getElementById('ta5').value,document.getElementById('ta-ref').value),bars=box.querySelector('.measure-bars'),state=document.getElementById('measure-state');
var valid=r.state==='geometry'||r.state==='insufficient';bars.hidden=!valid;box.dataset.state=r.state;
if(!valid){state.textContent=r.state==='reference'?'Choisir un même repère de mesure.':'Renseigner deux valeurs valides en mètres.';return;}
var max=Math.max(r.required,r.available),ref=document.getElementById('ta-ref').selectedOptions[0].textContent;
state.textContent=ref+' · '+(r.state==='insufficient'?'Espace insuffisant.':'Écart géométrique : '+r.delta.toFixed(2).replace('.',',')+' m.');
[['required',r.required],['available',r.available]].forEach(function(x){document.getElementById('measure-'+x[0]).style.width=(x[1]/max*100)+'%';document.getElementById('measure-'+x[0]+'-label').textContent=x[1].toFixed(2).replace('.',',')+' m';});
}form.addEventListener('input',draw);form.addEventListener('change',draw);draw();}
});})();
