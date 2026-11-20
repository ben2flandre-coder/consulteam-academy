/* Agrandissement au clic / au toucher des photos et schémas (lightbox) */
(function(){
var root,box,img,cap,cnt,list=[],idx=0,scale=1,fitW=0,open=false,lastFocus=null;
function cands(){
  var sel='main img, .slide img';var all=[].slice.call(document.querySelectorAll(sel)).filter(function(i){
    return !i.closest('button,.dk-top,.dk-bot,#ovw,#notes,#help,[data-nozoom]')&&!i.hasAttribute('data-nozoom')});
  return all;
}
function visible(i){var s=i.closest('.slide');return !s||s.classList.contains('active')}
function build(){
  root=document.createElement('div');root.id='zm';root.setAttribute('role','dialog');root.setAttribute('aria-modal','true');root.setAttribute('aria-label','Image agrandie');
  root.innerHTML='<div class="zm-bar"><span class="zm-cnt" aria-live="polite"></span><span class="zm-sp"></span>'+
  '<button type="button" data-a="prev" aria-label="Précédente">‹</button><button type="button" data-a="next" aria-label="Suivante">›</button>'+
  '<button type="button" data-a="out" aria-label="Réduire">−</button><button type="button" data-a="fit" aria-label="Ajuster">⤢</button><button type="button" data-a="in" aria-label="Agrandir">+</button>'+
  '<button type="button" data-a="close" aria-label="Fermer">✕</button></div><div class="zm-box"><img alt=""></div><p class="zm-cap"></p>';
  document.body.appendChild(root);
  box=root.querySelector('.zm-box');img=box.querySelector('img');cap=root.querySelector('.zm-cap');cnt=root.querySelector('.zm-cnt');
  root.addEventListener('click',function(e){
    var b=e.target.closest('button');
    if(b){var a=b.dataset.a;if(a==='close')close();else if(a==='prev')go(-1);else if(a==='next')go(1);else if(a==='in')zoom(scale*1.5);else if(a==='out')zoom(scale/1.5);else zoom(1);return}
    if(e.target===root||e.target===box)close();
  });
  img.addEventListener('dblclick',function(){zoom(scale>1.05?1:2.5)});
  ['touchstart','touchend','touchmove'].forEach(function(t){root.addEventListener(t,function(e){e.stopPropagation()},{passive:true})});
  document.addEventListener('keydown',function(e){
    if(!open)return;
    var k=e.key;
    if(k==='Escape'||k==='Esc'){close()}
    else if(k==='ArrowRight'||k==='ArrowDown'&&false){go(1)}
    else if(k==='ArrowLeft'){go(-1)}
    else if(k==='+'||k==='='){zoom(scale*1.5)}
    else if(k==='-'){zoom(scale/1.5)}
    else if(k==='0'){zoom(1)}
    else if(k==='Tab'){var f=[].slice.call(root.querySelectorAll('button'));var i=f.indexOf(document.activeElement);e.preventDefault();f[(i+(e.shiftKey?-1:1)+f.length)%f.length].focus();}
    else return;
    if(k!=='Tab')e.preventDefault();e.stopImmediatePropagation();
  },true);
}
function zoom(s){
  scale=Math.max(1,Math.min(6,s));
  if(scale===1){img.style.width='';img.style.maxWidth='100%';img.style.maxHeight='100%';box.classList.remove('z');box.scrollTo(0,0)}
  else{if(!fitW)fitW=img.getBoundingClientRect().width||box.clientWidth;img.style.maxWidth='none';img.style.maxHeight='none';img.style.width=(fitW*scale)+'px';box.classList.add('z')}
}
function show(i){
  idx=(i+list.length)%list.length;var el=list[idx];
  var fig=el.closest('figure'),fc=fig&&fig.querySelector('figcaption');
  img.onload=function(){fitW=0;zoom(1)};
  img.src=el.currentSrc||el.src;img.alt=el.alt||'';
  img.classList.toggle('svg',/\.svg(\?|$)/.test(el.src));
  cap.textContent=(el.alt||'')+(fc&&fc.textContent&&fc.textContent.indexOf(el.alt)<0?' — '+fc.textContent.trim():'');
  cnt.textContent=(idx+1)+' / '+list.length;
  root.querySelector('[data-a=prev]').style.visibility=root.querySelector('[data-a=next]').style.visibility=list.length>1?'visible':'hidden';
  zoom(1);
}
function go(d){show(idx+d)}
function openAt(el){
  if(!root)build();
  list=cands().filter(visible);idx=list.indexOf(el);if(idx<0){list=[el];idx=0}
  lastFocus=document.activeElement;open=true;root.classList.add('on');document.documentElement.classList.add('zm-lock');
  show(idx);root.querySelector('[data-a=close]').focus();
}
function close(){open=false;root.classList.remove('on');document.documentElement.classList.remove('zm-lock');img.removeAttribute('src');if(lastFocus&&lastFocus.focus)lastFocus.focus()}
document.addEventListener('DOMContentLoaded',function(){
  cands().forEach(function(i){
    i.classList.add('zm-able');i.tabIndex=0;i.setAttribute('role','button');
    i.setAttribute('aria-label','Agrandir : '+(i.alt||'image'));
    var f=i.closest('figure');if(f)f.classList.add('zm-fig');
  });
  document.addEventListener('click',function(e){var t=e.target;if(t.classList&&t.classList.contains('zm-able')){e.preventDefault();openAt(t)}});
  document.addEventListener('keydown',function(e){if(open)return;var t=e.target;if(t.classList&&t.classList.contains('zm-able')&&(e.key==='Enter'||e.key===' ')){e.preventDefault();e.stopPropagation();openAt(t)}},true);
});
})();
