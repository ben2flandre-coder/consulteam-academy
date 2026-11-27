/* L'affichage pleine largeur est natif ; l'immersion navigateur reste volontaire. */
(function(){'use strict';document.addEventListener('DOMContentLoaded',function(){
var host=document.querySelector('.top,.lv-bar');if(!host||!document.documentElement.requestFullscreen)return;
var b=document.createElement('button');b.type='button';b.className='expand-view';b.textContent='Agrandir';b.setAttribute('aria-label','Afficher la plateforme en plein écran');
b.addEventListener('click',function(){var p=document.fullscreenElement?document.exitFullscreen():document.documentElement.requestFullscreen();if(p&&p.catch)p.catch(function(){b.title='Le navigateur ne permet pas le plein écran dans ce contexte';});});
document.addEventListener('fullscreenchange',function(){b.textContent=document.fullscreenElement?'Réduire':'Agrandir';b.setAttribute('aria-label',document.fullscreenElement?'Quitter le plein écran':'Afficher la plateforme en plein écran');});
host.appendChild(b);
});})();
