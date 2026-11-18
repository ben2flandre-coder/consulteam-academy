/* Accès formateur A26094A : un code et l'une des adresses e-mail autorisées déverrouillent le contenu, dans le navigateur.
   Le contenu est chiffré (AES-GCM) ; sa clé est elle-même enveloppée une fois par adresse autorisée (PBKDF2 600 000 itérations).
   Aucun code ni aucune adresse ne figure dans le site. */
(function(){
  var KEY='pz.k.a26094a.v2',AADK='A26094A-key',AAD='A26094A';
  var enc=new TextEncoder(),dec=new TextDecoder();
  function b2u(b){var s=atob(b),a=new Uint8Array(s.length);for(var i=0;i<s.length;i++)a[i]=s.charCodeAt(i);return a;}
  function u2b(a){var s='';for(var i=0;i<a.length;i++)s+=String.fromCharCode(a[i]);return btoa(s);}
  function wrapKey(code,email,salt,it){
    return crypto.subtle.importKey('raw',enc.encode(code.trim()+'\u0000'+email.trim().toLowerCase()),'PBKDF2',false,['deriveKey'])
      .then(function(m){return crypto.subtle.deriveKey({name:'PBKDF2',salt:salt,iterations:it,hash:'SHA-256'},m,{name:'AES-GCM',length:256},false,['decrypt']);});
  }
  function unwrap(pack,code,email){
    var i=0;
    function next(){
      if(i>=pack.w.length)return Promise.reject(new Error('no'));
      var w=pack.w[i++];
      return wrapKey(code,email,b2u(w.s),pack.it).then(function(k){
        return crypto.subtle.decrypt({name:'AES-GCM',iv:b2u(w.i),additionalData:enc.encode(AADK)},k,b2u(w.k));
      }).then(function(raw){return new Uint8Array(raw);},next);
    }
    return next();
  }
  function open(pack,raw){
    return crypto.subtle.importKey('raw',raw,'AES-GCM',false,['decrypt']).then(function(k){
      return crypto.subtle.decrypt({name:'AES-GCM',iv:b2u(pack.iv),additionalData:enc.encode(AAD)},k,b2u(pack.ct));
    }).then(function(p){return dec.decode(p);});
  }
  function saved(){try{var v=sessionStorage.getItem(KEY);return v?b2u(v):null;}catch(e){return null;}}
  function save(raw){try{sessionStorage.setItem(KEY,u2b(raw));}catch(e){}}
  function forget(){try{sessionStorage.removeItem(KEY);}catch(e){}}
  var CSS='body{margin:0;font:17px/1.55 "Segoe UI",system-ui,sans-serif;background:#f3f5f8;color:#16273d;display:grid;place-items:center;min-height:100vh}@media(prefers-color-scheme:dark){body{background:#0d1722;color:#e7eef6}}form{background:#fff;border:1px solid #cbd5e1;border-left:10px solid #f6b63d;border-radius:12px;padding:26px 28px;max-width:420px;width:calc(100% - 32px)}@media(prefers-color-scheme:dark){form{background:#15253a;border-color:#2b4160;border-left-color:#f6b63d}}h1{font:700 24px Bahnschrift,"Segoe UI",sans-serif;margin:0 0 6px;color:#102c53}@media(prefers-color-scheme:dark){h1{color:#a9d0f5}}p{margin:0 0 14px;color:#53657a}@media(prefers-color-scheme:dark){p{color:#a8b8c9}}label{display:block;margin:12px 0 4px;font-weight:600}input{font:inherit;padding:10px 12px;border:1px solid #8aa0b8;border-radius:8px;width:100%;box-sizing:border-box;background:#fff;color:#16273d}button{margin-top:16px;font:inherit;font-weight:700;padding:11px 18px;border:0;border-radius:8px;background:#102c53;color:#fff;cursor:pointer;width:100%}@media(prefers-color-scheme:dark){button{background:#f6b63d;color:#102c53}}#e{color:#b3261e;min-height:1.4em;margin:10px 0 0}@media(prefers-color-scheme:dark){#e{color:#ff9a8f}}a{color:inherit}';
  window.PzGate={
    isOpen:function(){return !!saved();},
    lock:forget,
    page:function(pack){
      function render(html){document.open();document.write(html);document.close();}
      function ask(){
        document.documentElement.lang='fr';
        document.body.innerHTML='<style>'+CSS+'</style><form id="f" autocomplete="off"><h1>Espace formateur</h1><p>Session A26094A. Saisissez votre adresse e-mail et votre code.</p><label for="m">Adresse e-mail</label><input id="m" type="email" required autocomplete="off"><label for="c">Code</label><input id="c" type="password" required autocomplete="off"><div id="e" role="status" aria-live="polite"></div><button type="submit">Ouvrir</button><p style="margin:14px 0 0;font-size:.9em"><a href="index.html">Retour à l’accueil de la session</a></p></form>';
        document.getElementById('f').onsubmit=function(ev){
          ev.preventDefault();var b=this.querySelector('button');b.disabled=true;b.textContent='Vérification…';
          unwrap(pack,document.getElementById('c').value,document.getElementById('m').value).then(function(raw){
            return open(pack,raw).then(function(h){save(raw);render(h);});
          }).catch(function(){b.disabled=false;b.textContent='Ouvrir';document.getElementById('e').textContent='Adresse ou code incorrect.';});
        };
      }
      if(!(window.crypto&&crypto.subtle)){document.body.textContent='Chiffrement indisponible dans ce contexte : ouvrez la page en https.';return;}
      var raw=saved();
      if(raw){open(pack,raw).then(render,function(){forget();ask();});}else ask();
    }
  };
})();
