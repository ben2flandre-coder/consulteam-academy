/* Accès formateur : l'e-mail et le code déchiffrent le contenu dans le navigateur. */
(function(){
  var SALT='consulteam-a2600ey-formateur-v1',IT=250000,KEY='pz.k.a2600ey.v1';
  var enc=new TextEncoder(),dec=new TextDecoder();
  function b2u(b){var s=atob(b),a=new Uint8Array(s.length);for(var i=0;i<s.length;i++)a[i]=s.charCodeAt(i);return a;}
  function u2b(a){var s='';for(var i=0;i<a.length;i++)s+=String.fromCharCode(a[i]);return btoa(s);}
  function derive(email,code){
    return crypto.subtle.importKey('raw',enc.encode(email.trim().toLowerCase()+'|'+code.trim()),'PBKDF2',false,['deriveBits'])
      .then(function(k){return crypto.subtle.deriveBits({name:'PBKDF2',salt:enc.encode(SALT),iterations:IT,hash:'SHA-256'},k,256);})
      .then(function(b){return new Uint8Array(b);});
  }
  function decrypt(raw,pack){
    return crypto.subtle.importKey('raw',raw,'AES-GCM',false,['decrypt']).then(function(k){
      return crypto.subtle.decrypt({name:'AES-GCM',iv:b2u(pack.iv)},k,b2u(pack.ct));}).then(function(p){return dec.decode(p);});
  }
  function saved(){try{var v=sessionStorage.getItem(KEY);return v?b2u(v):null;}catch(e){return null;}}
  function save(raw){try{sessionStorage.setItem(KEY,u2b(raw));}catch(e){}}
  function forget(){try{sessionStorage.removeItem(KEY);}catch(e){}}
  function base(){return (document.currentScript&&document.currentScript.src)||'';}
  var SRC=base();
  function checkPack(){return fetch(SRC.replace(/gate\.js.*$/,'check.json')).then(function(r){return r.json();});}
  window.PzGate={
    /* vérifie e-mail + code (cours) : résout true/false et garde la clé pour la session */
    verify:function(email,code){
      return Promise.all([derive(email,code),checkPack()]).then(function(r){
        return decrypt(r[0],r[1]).then(function(t){if(t==='ok-a2600ey'){save(r[0]);return true;}return false;},function(){return false;});
      });
    },
    isOpen:function(){return !!saved();},
    lock:forget,
    /* page chiffrée : packs = {iv, ct} */
    page:function(pack){
      function render(html){document.open();document.write(html);document.close();}
      function ask(msg){
        document.documentElement.lang='fr';
        document.body.innerHTML='<style>body{margin:0;font:17px/1.55 "Segoe UI",system-ui,sans-serif;background:#f3f5f8;color:#16273d;display:grid;place-items:center;min-height:100vh}@media(prefers-color-scheme:dark){body{background:#0d1722;color:#e7eef6}}form{background:#fff;border:1px solid #cbd5e1;border-left:10px solid #f6b63d;border-radius:12px;padding:26px 28px;max-width:420px;width:calc(100% - 32px)}@media(prefers-color-scheme:dark){form{background:#15253a;border-color:#2b4160}}h1{font:700 24px Bahnschrift,"Segoe UI",sans-serif;margin:0 0 6px;color:#102c53}@media(prefers-color-scheme:dark){h1{color:#a9d0f5}}p{margin:0 0 14px;color:#53657a}label{display:block;margin:12px 0 4px;font-weight:600}input{font:inherit;padding:10px 12px;border:1px solid #8aa0b8;border-radius:8px;width:100%;box-sizing:border-box;background:transparent;color:inherit}button{margin-top:18px;background:#102c53;color:#fff;border:0;border-radius:8px;padding:11px 22px;font:700 16px Bahnschrift,"Segoe UI",sans-serif;cursor:pointer}#e{color:#b3261e;min-height:1.4em;margin-top:10px}a{color:#0b68ae}</style><form id="f"><div style="background:#102c53;margin:-26px -28px 18px;padding:14px 20px;border-radius:2px 2px 0 0"><img src="'+SRC.replace(/gate\.js.*$/,'img/logo-consulteam-groupe.png')+'" alt="Consul Team" style="height:40px;display:block"></div><h1>Espace formateur</h1><p>Accès réservé : e-mail et code.</p><label for="m">E-mail</label><input id="m" type="email" autocomplete="username" required><label for="c">Code</label><input id="c" type="password" autocomplete="current-password" required><button>Ouvrir</button><div id="e" role="alert">'+(msg||'')+'</div><p style="margin-top:14px"><a href="'+location.pathname.replace(/[^/]*$/,'')+'">Retour</a></p></form>';
        document.getElementById('f').onsubmit=function(ev){
          ev.preventDefault();var b=this.querySelector('button');b.disabled=true;b.textContent='Vérification…';
          derive(document.getElementById('m').value,document.getElementById('c').value).then(function(raw){
            return decrypt(raw,pack).then(function(h){save(raw);render(h);},function(){b.disabled=false;b.textContent='Ouvrir';document.getElementById('e').textContent='E-mail ou code incorrect.';});
          });
        };
        document.getElementById('m').focus();
      }
      var raw=saved();
      if(raw)decrypt(raw,pack).then(render,function(){forget();ask();});else ask();
    }
  };
})();
