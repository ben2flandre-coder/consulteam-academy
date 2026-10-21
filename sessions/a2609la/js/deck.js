(function(){
'use strict';
var S=window.HStore||{get:function(){return null},set:function(){}};
document.addEventListener('DOMContentLoaded',function(){
  var stage=document.getElementById('stage');
  /* QCM : une diapositive par question, générée depuis qcm-data.js */
  var host=document.getElementById('qcm-slides'),score=0,answered=0;
  if(host&&window.QCM){
    QCM.forEach(function(x,i){
      var s=document.createElement('section');s.className='slide';s.dataset.title='QCM '+(i+1)+'/10';s.dataset.q=i;s.dataset.sec='8 · QCM';if(i===0)s.dataset.min='25';
      s.innerHTML='<span class="k">QCM · question '+(i+1)+' sur '+QCM.length+'</span><h2></h2><div class="opts"></div><p class="qexp" aria-live="polite"></p><div class="note"><p>Laisser répondre (main levée ou individuellement), puis toucher la réponse. Reprendre oralement chaque erreur. Le QCM contribue à l’évaluation ; la maîtrise pratique est appréciée séparément. Seuil de réussite : à fixer avec l’organisme avant la session.</p></div>';
      s.querySelector('h2').textContent=x.q;
      var o=s.querySelector('.opts');
      x.o.forEach(function(c,j){var b=document.createElement('button');b.type='button';b.className='opt';b.innerHTML='<span class="l">'+String.fromCharCode(65+j)+'</span><span></span>';b.lastChild.textContent=c;
        b.addEventListener('click',function(){
          if(s.dataset.done)return;s.dataset.done='1';answered++;
          var ok=j===x.a;if(ok)score++;
          o.querySelectorAll('.opt').forEach(function(bb,k){if(k===x.a)bb.classList.add('good');else if(k===j)bb.classList.add('bad');bb.disabled=true});
          var e=s.querySelector('.qexp');e.textContent=(ok?'✓ Correct. ':'✗ Réponse : '+String.fromCharCode(65+x.a)+'. ')+x.e;e.style.color=ok?'var(--ok)':'var(--danger)';
          var r=document.getElementById('qcm-score');if(r)r.textContent=score+' / '+QCM.length+' (réponses collectives : '+answered+' question(s) traitée(s))';
        });o.appendChild(b)});
      host.appendChild(s);
    });
  }
  var slides=[].slice.call(stage.querySelectorAll('.slide'));
  var cur=0,ovw=document.getElementById('ovw'),notes=document.getElementById('notes');
  /* aperçu */
  var ol=ovw.querySelector('ol');
  slides.forEach(function(s,i){var li=document.createElement('li'),b=document.createElement('button');b.type='button';
    var t=s.dataset.title||(s.querySelector('h1,h2')||{}).textContent||('Diapositive '+(i+1));
    b.innerHTML='<small>'+(i+1)+' · '+(s.dataset.sec||'')+'</small>';b.appendChild(document.createTextNode(t));
    b.addEventListener('click',function(){ovw.classList.remove('on');go(i,true)});li.appendChild(b);ol.appendChild(li)});
  var prog=document.querySelector('.prog i'),cnt=document.querySelector('.cnt'),sec=document.querySelector('.sec');
  /* chrono */
  var tm=document.getElementById('timer'),tRun=false,tLeft=0,tInt=null;
  function fmt(s){var a=Math.abs(s),m=Math.floor(a/60),r=a%60;return(s<0?'+':'')+(m<10?'0':'')+m+':'+(r<10?'0':'')+r}
  function tDraw(){tm.textContent=(tRun?'⏸ ':'⏱ ')+fmt(tLeft);tm.classList.toggle('over',tLeft<0)}
  function tStart(){if(tInt)return;tRun=true;tInt=setInterval(function(){tLeft--;tDraw()},1000);tDraw()}
  function tStop(){tRun=false;clearInterval(tInt);tInt=null;tDraw()}
  tm.addEventListener('click',function(){tRun?tStop():tStart()});
  tm.addEventListener('dblclick',function(){tLeft=curMin*60;tDraw()});
  var curMin=0,curSec='';
  function frags(s){return [].slice.call(s.querySelectorAll('.frag'))}
  function go(i,showAll,back){
    i=Math.max(0,Math.min(slides.length-1,i));
    slides.forEach(function(s,k){s.classList.remove('active','back')});
    var s=slides[i];s.classList.add('active');if(back)s.classList.add('back');
    if(showAll||back)frags(s).forEach(function(f){f.classList.add('show')});
    else if(!s.dataset.seen)frags(s).forEach(function(f){f.classList.remove('show')});
    s.dataset.seen='1';s.scrollTop=0;
    var prev=cur;cur=i;
    prog.style.width=(100*(i+1)/slides.length)+'%';
    cnt.textContent=(i+1)+' / '+slides.length;
    sec.textContent=s.dataset.sec||'';
    var m=0;for(var j=i;j>=0&&slides[j].dataset.sec===s.dataset.sec;j--){var mm=parseInt(slides[j].dataset.min,10);if(mm){m=mm;break}}
    if(m&&(curSec!==s.dataset.sec)){curMin=m;if(!tRun){tLeft=m*60;tDraw()}}
    curSec=s.dataset.sec;
    /* notes */
    var n=s.querySelector('.note');notes.innerHTML='<h4>Notes formateur — '+(s.dataset.title||(s.querySelector('h1,h2')||{}).textContent||'')+'</h4>'+(n?n.innerHTML:'<p>Pas de note.</p>');
    if(location.hash!=='#'+(i+1))history.replaceState(null,'','#'+(i+1));
    S.set('h-deck-pos',String(i));
  }
  function next(){var s=slides[cur],f=frags(s).filter(function(x){return!x.classList.contains('show')});
    if(f.length){f[0].classList.add('show');return}go(cur+1)}
  function prev(){var s=slides[cur],f=frags(s).filter(function(x){return x.classList.contains('show')});
    if(f.length){f[f.length-1].classList.remove('show');return}
    if(cur>0){go(cur-1,false,true)}}
  document.getElementById('bn').addEventListener('click',next);
  document.getElementById('bp').addEventListener('click',prev);
  function tog(el,btn){el.classList.toggle('on');if(btn)btn.setAttribute('aria-pressed',el.classList.contains('on'))}
  var bnotes=document.getElementById('bnotes'),bovw=document.getElementById('bovw'),bfs=document.getElementById('bfs'),bhelp=document.getElementById('bhelp'),help=document.getElementById('help');
  bnotes.addEventListener('click',function(){tog(notes,bnotes)});
  bovw.addEventListener('click',function(){tog(ovw,bovw)});
  bhelp.addEventListener('click',function(){help.classList.add('on')});
  help.addEventListener('click',function(){help.classList.remove('on')});
  function fs(){var d=document,e=d.documentElement;if(!d.fullscreenElement&&e.requestFullscreen){e.requestFullscreen().catch(function(){})}else if(d.exitFullscreen){d.exitFullscreen()}}
  bfs.addEventListener('click',fs);
  if(!document.documentElement.requestFullscreen)bfs.style.display='none';
  document.addEventListener('keydown',function(e){
    if(/INPUT|TEXTAREA|SELECT/.test((e.target||{}).tagName||'')&&e.key!=='Escape')return;
    var k=e.key;
    if(k==='ArrowRight'||k==='PageDown'||k===' '||k==='Enter'){if(e.target.tagName==='BUTTON'&&(k===' '||k==='Enter'))return;e.preventDefault();next()}
    else if(k==='ArrowLeft'||k==='PageUp'||k==='Backspace'){e.preventDefault();prev()}
    else if(k==='Home')go(0);else if(k==='End')go(slides.length-1);
    else if(k==='f'||k==='F')fs();
    else if(k==='n'||k==='N')tog(notes,bnotes);
    else if(k==='g'||k==='G')tog(ovw,bovw);
    else if(k==='t'||k==='T')tm.click();
    else if(k==='b'||k==='B'||k==='.')document.body.classList.toggle('black');
    else if(k==='?'||k==='h')help.classList.toggle('on');
    else if(k==='Escape'){help.classList.remove('on');ovw.classList.remove('on');notes.classList.remove('on')}
  });
  /* balayage tactile */
  var sx=0,sy=0,st=0;
  stage.addEventListener('touchstart',function(e){var t=e.changedTouches[0];sx=t.clientX;sy=t.clientY;st=Date.now()},{passive:true});
  stage.addEventListener('touchend',function(e){var t=e.changedTouches[0],dx=t.clientX-sx,dy=t.clientY-sy;
    if(Math.abs(dx)>60&&Math.abs(dx)>Math.abs(dy)*1.6&&Date.now()-st<700){dx<0?next():prev()}},{passive:true});
  /* ateliers : état mémorisé */
  document.querySelectorAll('.atl').forEach(function(b,i){var k='h-atl-'+i,st=S.get(k)||'todo';b.dataset.s=st;lab(b);
    b.addEventListener('click',function(){var o={todo:'fait',fait:'nr',nr:'todo'};b.dataset.s=o[b.dataset.s];S.set(k,b.dataset.s);lab(b)})});
  function lab(b){var m={todo:'À faire',fait:'✓ Réalisé',nr:'⚠ Non réalisé / adapté'};var sm=b.querySelector('small');if(sm)sm.textContent=m[b.dataset.s]}
  /* départ */
  var h=parseInt((location.hash||'').slice(1),10),start=0;
  if(h>=1&&h<=slides.length)start=h-1;else{var p=parseInt(S.get('h-deck-pos'),10);if(p>=0&&p<slides.length&&location.search.indexOf('reprendre')>-1)start=p}
  go(start,false);
  window.addEventListener('hashchange',function(){var n=parseInt(location.hash.slice(1),10);if(n>=1&&n<=slides.length&&n-1!==cur)go(n-1,true)});
  tDraw();
});
})();
