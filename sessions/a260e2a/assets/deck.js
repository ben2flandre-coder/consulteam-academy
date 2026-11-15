(function(){'use strict';
document.addEventListener('DOMContentLoaded',function(){
var stage=document.getElementById('stage'),slides=[].slice.call(stage.querySelectorAll('.slide')),cur=0,ovw=document.getElementById('ovw'),notes=document.getElementById('notes');
var score=0,answered=0,sc=document.getElementById('qsc');
slides.filter(function(s){return s.classList.contains('qcm')}).forEach(function(s){var o=s.querySelector('.opts'),ok=+o.dataset.ok;
 o.querySelectorAll('.opt').forEach(function(b){b.addEventListener('click',function(){if(s.dataset.done)return;s.dataset.done='1';answered++;var j=+b.dataset.j,good=j===ok;if(good)score++;
  o.querySelectorAll('.opt').forEach(function(bb,k){if(k===ok)bb.classList.add('good');else if(k===j)bb.classList.add('bad');bb.disabled=true});
  var e=s.querySelector('.qexp');e.hidden=false;e.textContent=(good?'✓ Correct. ':'✗ Réponse : '+'ABCD'.charAt(ok)+'. ')+e.textContent;e.style.color=good?'#16794a':'#b3261e';
  if(sc)sc.textContent='Salle : '+score+' / '+answered})})});
var ol=ovw.querySelector('ol'),lastSec='';
slides.forEach(function(s,i){var li=document.createElement('li'),b=document.createElement('button');b.type='button';b.innerHTML='<small>'+(i+1)+' · '+(s.dataset.sec||'')+'</small>';b.appendChild(document.createTextNode(s.dataset.title||('Diapositive '+(i+1))));b.addEventListener('click',function(){ovw.classList.remove('on');go(i,true)});li.appendChild(b);ol.appendChild(li)});
var prog=document.querySelector('.prog i'),cnt=document.querySelector('.cnt'),sec=document.querySelector('.sec');
var tm=document.getElementById('timer'),tRun=false,tLeft=0,tInt=null,curMin=0,curSec='';
function fmt(s){var a=Math.abs(s),m=Math.floor(a/60),r=a%60;return(s<0?'+':'')+(m<10?'0':'')+m+':'+(r<10?'0':'')+r}
function tDraw(){tm.textContent=(tRun?'⏸ ':'⏱ ')+fmt(tLeft);tm.classList.toggle('over',tLeft<0)}
function tStart(){if(tInt)return;tRun=true;tInt=setInterval(function(){tLeft--;tDraw()},1000);tDraw()}
function tStop(){tRun=false;clearInterval(tInt);tInt=null;tDraw()}
tm.addEventListener('click',function(){tRun?tStop():tStart()});tm.addEventListener('dblclick',function(){tLeft=curMin*60;tDraw()});
function frags(s){return [].slice.call(s.querySelectorAll('.frag:not(.show)'))}
function go(i,all,back){i=Math.max(0,Math.min(slides.length-1,i));slides.forEach(function(s){s.classList.remove('active','back')});var s=slides[i];s.classList.add('active');if(back)s.classList.add('back');
 if(all||back)[].slice.call(s.querySelectorAll('.frag')).forEach(function(f){f.classList.add('show')});else [].slice.call(s.querySelectorAll('.frag')).forEach(function(f){f.classList.remove('show')});
 s.dataset.seen='1';s.scrollTop=0;fit(s);cur=i;prog.style.width=(100*(i+1)/slides.length)+'%';cnt.textContent=(i+1)+' / '+slides.length;sec.textContent=s.dataset.sec||'';
 var m=0;for(var j=i;j>=0&&slides[j].dataset.sec===s.dataset.sec;j--){var mm=parseInt(slides[j].dataset.min,10);if(mm){m=mm;break}}
 if(m&&curSec!==s.dataset.sec){curMin=m;if(!tRun){tLeft=m*60;tDraw()}}curSec=s.dataset.sec;
 var n=s.querySelector('.note');notes.innerHTML='<h4>Notes formateur — '+(s.dataset.title||'')+'</h4>'+(n?n.innerHTML:'<p>Pas de note.</p>');
 if(location.hash!=='#'+(i+1))history.replaceState(null,'','#'+(i+1))}
function next(){var s=slides[cur],f=frags(s);if(f.length){f[0].classList.add('show');return}go(cur+1)}
function prev(){var s=slides[cur],f=[].slice.call(s.querySelectorAll('.frag.show'));if(f.length&&!s.dataset.noback){f[f.length-1].classList.remove('show');return}if(cur>0)go(cur-1,false,true)}
document.getElementById('bn').onclick=next;document.getElementById('bp').onclick=prev;
function tog(el,b){el.classList.toggle('on');if(b)b.setAttribute('aria-pressed',el.classList.contains('on'))}
var bn=document.getElementById('bnotes'),bo=document.getElementById('bovw');
bn.onclick=function(){tog(notes,bn)};bo.onclick=function(){tog(ovw,bo)};
document.getElementById('bhelp').onclick=function(){document.getElementById('help').classList.add('on')};document.getElementById('help').onclick=function(){this.classList.remove('on')};
function fs(){var d=document,e=d.documentElement;if(!d.fullscreenElement&&e.requestFullscreen){e.requestFullscreen().catch(function(){})}else if(d.exitFullscreen){d.exitFullscreen()}}
var bf=document.getElementById('bfs');bf.onclick=fs;if(!document.documentElement.requestFullscreen||window.matchMedia('(pointer:coarse)').matches||window.self!==window.top)bf.style.display='none';
function qtog(){document.body.classList.toggle('qbig')}document.getElementById('qbtn').onclick=qtog;
document.addEventListener('keydown',function(e){var hp=document.getElementById('help');if((ovw.classList.contains('on')||hp.classList.contains('on'))&&['Escape','g','G','?','h'].indexOf(e.key)<0)return;if(/INPUT|TEXTAREA|SELECT/.test((e.target||{}).tagName||'')&&e.key!=='Escape')return;var k=e.key;
 if(k==='ArrowRight'||k==='PageDown'||k===' '||k==='Enter'){if(e.target.tagName==='BUTTON'&&(k===' '||k==='Enter'))return;e.preventDefault();next()}
 else if(k==='ArrowLeft'||k==='PageUp'||k==='Backspace'){e.preventDefault();prev()}else if(k==='Home')go(0);else if(k==='End')go(slides.length-1);
 else if(k==='f'||k==='F')fs();else if(k==='n'||k==='N')tog(notes,bn);else if(k==='g'||k==='G')tog(ovw,bo);else if(k==='t'||k==='T')tm.click();
 else if(k==='q'||k==='Q')qtog();else if(k==='b'||k==='B'||k==='.')document.body.classList.toggle('black');else if(k==='?'||k==='h')document.getElementById('help').classList.toggle('on');
 else if(k==='Escape'){bn.setAttribute('aria-pressed','false');bo.setAttribute('aria-pressed','false');document.getElementById('help').classList.remove('on');ovw.classList.remove('on');notes.classList.remove('on');document.body.classList.remove('qbig')}});
var sx=0,sy=0,st=0;stage.addEventListener('touchstart',function(e){var t=e.changedTouches[0];sx=t.clientX;sy=t.clientY;st=Date.now()},{passive:true});
stage.addEventListener('touchend',function(e){var t=e.changedTouches[0],dx=t.clientX-sx,dy=t.clientY-sy;if(Math.abs(dx)>60&&Math.abs(dx)>Math.abs(dy)*1.6&&Date.now()-st<700){dx<0?next():prev()}},{passive:true});
function fit(s){s.style.fontSize='';if((window.innerWidth<=760||window.innerHeight<=520))return;var k=1;while(s.scrollHeight>s.clientHeight+2&&k>.6){k-=.04;s.style.fontSize='calc(var(--fs) * '+k.toFixed(2)+')'}}window.__fit=fit;window.addEventListener('resize',function(){fit(slides[cur])});var h=parseInt((location.hash||'').slice(1),10);go(h>=1&&h<=slides.length?h-1:0,false);
window.addEventListener('hashchange',function(){var n=parseInt(location.hash.slice(1),10);if(n>=1&&n<=slides.length&&n-1!==cur)go(n-1,true)});tDraw();
});})();
document.addEventListener('click',function(ev){var t=ev.target;
 var o=t.closest&&t.closest('.bopt');if(o){var br=o.closest('.branch');if(br.dataset.done)return;br.dataset.done='1';var ok=o.dataset.ok==='1';o.classList.add(ok?'good':'bad');
  [].forEach.call(br.querySelectorAll('.bopt'),function(b){if(b.dataset.ok==='1')b.classList.add('good');b.disabled=true});
  var x=br.querySelector('.bx');x.hidden=false;x.style.color=ok?'#16794a':'#b3261e';
  x.textContent=ok?'✓ Oui : la victime peut rester sous tension, on protège d’abord.':'✗ Non : toucher la victime expose à une seconde victime, et partir abandonne la victime et laisse la zone sans protection. On analyse, on écarte les tiers, on coupe sans s’exposer, on fait alerter par une personne désignée.';return}
 var m=t.closest&&t.closest('.mbtn');if(m){var w=m.closest('.metro'),on=w.classList.toggle('on');m.setAttribute('aria-pressed',on);m.textContent=(on?'■ Arrêter':'▶ Cadence 110 / min');w.querySelector('.mlab').textContent=on?(matchMedia('(prefers-reduced-motion:reduce)').matches?'110 battements par minute : le point reste fixe (animation réduite), caler sur 110 par minute':'110 battements par minute : caler les compressions sur le point rouge'):'Appuyer pour lancer le rythme'}
});
