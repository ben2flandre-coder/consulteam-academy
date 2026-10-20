/* Agrandissement des médias : clic sur une image, flèches ou boutons pour parcourir, Échap pour fermer. */
(function(){
  if(window.__pzLightbox)return;window.__pzLightbox=true;
  var box=null,list=[],idx=0,lastFocus=null;
  function zoomable(){
    return Array.prototype.filter.call(document.images,function(im){
      if(im.closest('.lb,header,nav,button,[data-nozoom]'))return false;
      if(im.closest('a[href]'))return false;
      var r=im.getBoundingClientRect();return r.width>=90&&r.height>=60;
    });
  }
  function capOf(im){
    var f=im.closest('figure'),c=f&&f.querySelector('figcaption');
    if(c)return c.textContent.trim();
    var a=im.closest('article');var h=a&&a.querySelector('h2,h3');
    return (h&&h.textContent.trim())||im.alt||'';
  }
  function show(i){
    idx=(i+list.length)%list.length;var im=list[idx];
    box.querySelector('img').src=im.currentSrc||im.src;box.querySelector('img').alt=im.alt||'';
    box.querySelector('.cap').textContent=(idx+1)+' / '+list.length+(capOf(im)?' · '+capOf(im):'');
  }
  function close(){if(!box)return;box.remove();box=null;document.removeEventListener('keydown',key);document.body.style.overflow='';if(lastFocus&&lastFocus.focus)lastFocus.focus();}
  function key(e){
    if(e.key==='Escape')close();
    else if(e.key==='ArrowRight')show(idx+1);
    else if(e.key==='ArrowLeft')show(idx-1);
  }
  function open(im){
    list=zoomable();idx=Math.max(0,list.indexOf(im));lastFocus=document.activeElement;
    box=document.createElement('div');box.className='lb';box.setAttribute('role','dialog');box.setAttribute('aria-modal','true');box.setAttribute('aria-label','Image agrandie');
    box.innerHTML='<button class="x" aria-label="Fermer">×</button>'+(list.length>1?'<button class="p" aria-label="Image précédente">‹</button><button class="n" aria-label="Image suivante">›</button>':'')+'<img alt=""><div class="cap"></div>';
    box.addEventListener('click',function(e){
      if(e.target.closest('.p')){show(idx-1);return;}
      if(e.target.closest('.n')){show(idx+1);return;}
      close();
    });
    document.body.appendChild(box);document.body.style.overflow='hidden';
    document.addEventListener('keydown',key);show(idx);box.querySelector('.x').focus();
  }
  document.addEventListener('click',function(e){
    var im=e.target;if(!im||im.tagName!=='IMG')return;
    if(im.closest('.lb,header,nav,button,[data-nozoom]')||im.closest('a[href]'))return;
    var r=im.getBoundingClientRect();if(r.width<90||r.height<60)return;
    e.preventDefault();open(im);
  });
  var st=document.createElement('style');
  st.textContent='img:not([data-nozoom]){cursor:zoom-in}.lb img{cursor:zoom-out}.lb{position:fixed;inset:0;z-index:2147483000;background:rgba(6,16,29,.93);display:flex;flex-direction:column;align-items:center;justify-content:center;padding:14px}.lb img{max-width:96vw;max-height:84vh;object-fit:contain;background:#fff;border-radius:6px}.lb .cap{color:#e7eef6;margin-top:10px;max-width:90vw;text-align:center;font:15px/1.4 system-ui,sans-serif}.lb button{position:absolute;background:rgba(255,255,255,.18);color:#fff;border:0;border-radius:50%;width:48px;height:48px;padding:0;font:28px/48px system-ui;cursor:pointer;text-align:center}.lb button:hover{background:rgba(255,255,255,.34)}.lb .x{top:14px;right:14px}.lb .p{left:14px;top:50%;margin-top:-24px}.lb .n{right:14px;top:50%;margin-top:-24px}@media print{.lb{display:none}}';
  document.head.appendChild(st);
})();
