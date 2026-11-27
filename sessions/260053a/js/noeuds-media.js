/* Séquence photographique : aucun morphing ni tracé inventé entre deux vues. */
(function(){'use strict';
document.addEventListener('DOMContentLoaded',function(){
  document.querySelectorAll('[data-photo-sequence]').forEach(function(box){
    var frames=Array.prototype.slice.call(box.querySelectorAll('.kn-reference'));if(!frames.length)return;
    var index=0,playing=false,timer=0,delay=3500;
    var steps=document.createElement('div');steps.className='kn-steps';steps.setAttribute('role','group');steps.setAttribute('aria-label','Choisir une vue du cabestan');
    frames.forEach(function(f,i){var b=document.createElement('button');b.type='button';b.textContent=i+1;b.setAttribute('aria-label','Afficher la vue '+(i+1)+' sur '+frames.length);b.addEventListener('click',function(){stop();show(i)});steps.appendChild(b)});
    var controls=document.createElement('div');controls.className='kn-controls';controls.innerHTML='<button type="button" class="btn alt" data-a="prev">Précédente</button><button type="button" class="btn" data-a="play">Lecture des vues</button><button type="button" class="btn alt" data-a="next">Suivante</button><label>Temps par vue <select aria-label="Temps par vue"><option value="3500">3,5 secondes</option><option value="6000">6 secondes</option><option value="10000">10 secondes</option></select></label>';
    var status=document.createElement('p');status.className='muted';status.setAttribute('role','status');
    box.appendChild(steps);box.appendChild(controls);box.appendChild(status);box.classList.add('enhanced');
    function show(i){index=Math.max(0,Math.min(frames.length-1,i));frames.forEach(function(f,j){f.hidden=j!==index});steps.querySelectorAll('button').forEach(function(b,j){b.setAttribute('aria-current',j===index?'step':'false')});controls.querySelector('[data-a=prev]').disabled=index===0;controls.querySelector('[data-a=next]').disabled=index===frames.length-1;status.textContent='Vue '+(index+1)+' / '+frames.length+' · préparation à plat, avant installation sur support.'}
    function stop(){playing=false;clearTimeout(timer);controls.querySelector('[data-a=play]').textContent='Lecture des vues'}
    function schedule(){timer=setTimeout(function(){if(!playing)return;if(index===frames.length-1){stop();return}show(index+1);schedule()},delay)}
    controls.addEventListener('click',function(e){var b=e.target.closest('[data-a]');if(!b)return;var a=b.dataset.a;if(a==='prev'){stop();show(index-1)}if(a==='next'){stop();show(index+1)}if(a==='play'){if(playing){stop();return}if(index===frames.length-1)show(0);playing=true;b.textContent='Pause';schedule()}});
    controls.querySelector('select').addEventListener('change',function(e){delay=Number(e.target.value);if(playing){clearTimeout(timer);schedule()}});
    document.addEventListener('visibilitychange',function(){if(document.hidden)stop()});window.addEventListener('pagehide',stop);
    var panel=box.closest('[role=tabpanel]');if(panel&&window.MutationObserver)new MutationObserver(function(){if(panel.hidden)stop()}).observe(panel,{attributes:true,attributeFilter:['hidden']});
    if(window.IntersectionObserver)new IntersectionObserver(function(entries){if(!entries[0].isIntersecting)stop()}).observe(box);
    show(0);
  });
});})();
