"""Chiffrement de l'espace formateur (AES-GCM 256, clé de contenu enveloppée par e-mail).
Code lu dans l'environnement (FORMATEUR_CODE), e-mails dans private/emails.txt : ni l'un ni l'autre n'est écrit dans le site."""
import os,json,base64,hashlib
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
IT=600000
def b(x): return base64.b64encode(x).decode()
def kdf(code,email,salt):
    return hashlib.pbkdf2_hmac('sha256',(code+'\u0000'+email.strip().lower()).encode(),salt,IT,32)
def lock_body(clair,emails_path='/home/claude/work/private/emails.txt'):
    code=os.environ.get('FORMATEUR_CODE','')
    emails=[e.strip() for e in open(emails_path).read().split() if '@' in e] if os.path.exists(emails_path) else []
    head='<small>FORMATEUR</small><h1>Espace formateur</h1>'
    if not code or not emails:
        return head+'<div class="warn"><b>Espace verrouillé, contenu non généré.</b> La reconstruction du site s’est faite sans le code : le contenu formateur n’est pas inclus (jamais en clair).</div>'
    ck=os.urandom(32)
    iv=os.urandom(12); ct=AESGCM(ck).encrypt(iv,clair.encode('utf-8'),b'A260E2A')
    wraps=[]
    for e in emails:
        s=os.urandom(16); w=os.urandom(12)
        wraps.append({'s':b(s),'i':b(w),'k':b(AESGCM(kdf(code,e,s)).encrypt(w,ck,b'A260E2A-key'))})
    data=json.dumps({'it':IT,'iv':b(iv),'ct':b(ct),'w':wraps})
    return head+'''<p class="lead">Accès réservé au formateur : saisissez votre code, puis l’une de vos adresses e-mail.</p>
<form id="lk" class="note" autocomplete="off" style="display:grid;gap:.6rem;max-width:26rem"><label>Code<br><input id="lc" type="password" required autocomplete="off" style="width:100%;padding:.55rem;font:inherit"></label><label>Adresse e-mail<br><input id="le" type="email" required autocomplete="off" style="width:100%;padding:.55rem;font:inherit"></label><button type="submit" id="lb">Déverrouiller</button><div id="lm" role="status" aria-live="polite"></div></form><div id="zone"></div>
<script>(function(){var D=__DATA__;
function u(s){return Uint8Array.from(atob(s),function(c){return c.charCodeAt(0)})}
async function key(c,e,s){var m=await crypto.subtle.importKey('raw',new TextEncoder().encode(c+'\\u0000'+e.trim().toLowerCase()),'PBKDF2',false,['deriveKey']);return crypto.subtle.deriveKey({name:'PBKDF2',salt:s,iterations:D.it,hash:'SHA-256'},m,{name:'AES-GCM',length:256},false,['decrypt'])}
document.getElementById('lk').addEventListener('submit',async function(ev){ev.preventDefault();var m=document.getElementById('lm'),btn=document.getElementById('lb');
if(!(window.crypto&&crypto.subtle)){m.textContent='Chiffrement indisponible dans ce contexte (ouvrir en https).';return}
btn.disabled=true;m.textContent='Vérification…';var c=document.getElementById('lc').value,e=document.getElementById('le').value;
try{for(var i=0;i<D.w.length;i++){var w=D.w[i];try{var k=await key(c,e,u(w.s));var raw=await crypto.subtle.decrypt({name:'AES-GCM',iv:u(w.i),additionalData:new TextEncoder().encode('A260E2A-key')},k,u(w.k));
var ck=await crypto.subtle.importKey('raw',raw,'AES-GCM',false,['decrypt']);var pt=await crypto.subtle.decrypt({name:'AES-GCM',iv:u(D.iv),additionalData:new TextEncoder().encode('A260E2A')},ck,u(D.ct));
document.getElementById('zone').innerHTML=new TextDecoder().decode(pt);document.getElementById('lk').style.display='none';document.querySelector('.lead').style.display='none';return}catch(x){}}
m.textContent='Code ou adresse incorrects.'}finally{btn.disabled=false;document.getElementById('lc').value=''}});})();</script>'''.replace('__DATA__',data)
