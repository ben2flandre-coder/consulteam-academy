/* Agrandissement des images au clic (clavier : Entrée/Espace, Échap pour fermer) */
(function(){
  'use strict';
  function eligible(img){
    if(!img||img.tagName!=='IMG') return false;
    var s=(img.getAttribute('src')||'').toLowerCase();
    if(s.indexOf('logo')>-1||img.classList.contains('no-zoom')) return false;
    if(img.closest('header,nav,footer,a,button,.qr-bloc,.video-card,.no-zoom')) return false;
    return true;
  }
  var ov,imgEl,capEl,last;
  function build(){
    ov=document.createElement('div');ov.className='zoom-overlay';ov.hidden=true;
    ov.setAttribute('role','dialog');ov.setAttribute('aria-modal','true');ov.setAttribute('aria-label','Image agrandie');
    ov.innerHTML='<button type="button" class="zoom-close" aria-label="Fermer l’image">✕</button><figure><img alt=""><figcaption></figcaption></figure>';
    document.body.appendChild(ov);
    imgEl=ov.querySelector('img');capEl=ov.querySelector('figcaption');
    ov.addEventListener('click',close);
  }
  function open(img){
    if(!ov) build();
    last=img;
    imgEl.src=img.currentSrc||img.src;imgEl.alt=img.alt||'';
    var fc=img.closest('figure');fc=fc&&fc.querySelector('figcaption');
    capEl.textContent=(fc&&fc.textContent.trim())||img.alt||'';
    ov.hidden=false;document.documentElement.classList.add('zoom-open');
    ov.querySelector('.zoom-close').focus();
  }
  function close(){
    if(!ov||ov.hidden) return;
    ov.hidden=true;document.documentElement.classList.remove('zoom-open');
    if(last&&last.focus) last.focus();
  }
  function init(){
    var list=document.querySelectorAll('img');
    for(var i=0;i<list.length;i++){
      var im=list[i];
      if(!eligible(im)) continue;
      im.classList.add('zoomable');im.setAttribute('tabindex','0');im.setAttribute('role','button');
      im.setAttribute('aria-label','Agrandir l’image : '+(im.alt||''));
    }
    document.addEventListener('click',function(e){
      if(e.target.classList&&e.target.classList.contains('zoomable')){e.preventDefault();open(e.target);}
    });
    document.addEventListener('keydown',function(e){
      if(e.key==='Escape') close();
      else if((e.key==='Enter'||e.key===' ')&&e.target.classList&&e.target.classList.contains('zoomable')){e.preventDefault();open(e.target);}
    });
  }
  if(document.readyState==='loading') document.addEventListener('DOMContentLoaded',init); else init();
})();
