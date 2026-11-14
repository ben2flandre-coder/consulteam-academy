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
        raise SystemExit('ERREUR : FORMATEUR_CODE ou private/emails.txt absent : l’espace formateur ne doit jamais être publié vide ni en clair.')
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


def _data(clair, aad_ct=b'A260E2A', aad_key=b'A260E2A-key'):
    code=os.environ.get('FORMATEUR_CODE','')
    emails_path='/home/claude/work/private/emails.txt'
    emails=[e.strip() for e in open(emails_path).read().split() if '@' in e] if os.path.exists(emails_path) else []
    if not code or not emails: return None
    ck=os.urandom(32); iv=os.urandom(12); ct=AESGCM(ck).encrypt(iv,clair.encode('utf-8'),aad_ct)
    wraps=[]
    for e in emails:
        s=os.urandom(16); w=os.urandom(12)
        wraps.append({'s':b(s),'i':b(w),'k':b(AESGCM(kdf(code,e,s)).encrypt(w,ck,aad_key))})
    return json.dumps({'it':IT,'iv':b(iv),'ct':b(ct),'w':wraps})

def lock_document(full_html, title='Mode animation'):
    """Page autonome chiffrée : le document complet (diapositives, notes, réponses) n'existe qu'en chiffré ;
    après saisie du code et d'une adresse, il remplace la page. Les fichiers annexes (CSS, JS, images, QR) restent publics."""
    data=_data(full_html)
    if data is None:
        raise SystemExit('ERREUR : FORMATEUR_CODE ou private/emails.txt absent. Le mode animation ne doit jamais être publié en clair.')
    return TPL_DOC.replace('__TITLE__',title).replace('__DATA__',data)

TPL_DOC=r'''<!doctype html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow"><meta name="theme-color" content="#102c53"><title>__TITLE__ — espace formateur</title>
<style>body{margin:0;min-height:100vh;display:grid;place-items:center;background:#102c53;font:17px/1.5 Segoe UI,system-ui,sans-serif;color:#16273d}main{background:#fff;border-radius:16px;padding:28px;max-width:26rem;width:calc(100% - 32px);box-shadow:0 12px 40px #0006}h1{font-size:1.4rem;margin:.2rem 0 .6rem;color:#102c53}small{color:#8a520a;font-weight:800;letter-spacing:.12em}label{display:block;margin:.6rem 0}input{width:100%;padding:.6rem;border:2px solid #cbd5e1;border-radius:10px;font:inherit;box-sizing:border-box}button{margin-top:.4rem;padding:.7rem 1.2rem;border:0;border-radius:10px;background:#102c53;color:#fff;font:inherit;font-weight:800;cursor:pointer}#lm{min-height:1.5em;color:#b3261e;font-weight:700}</style></head>
<body><main><small>FORMATEUR</small><h1>__TITLE__</h1><p>Accès réservé au formateur : saisissez votre code, puis l’une de vos adresses e-mail.</p>
<form id="lk" autocomplete="off"><label>Code<input id="lc" type="password" required autocomplete="off"></label><label>Adresse e-mail<input id="le" type="email" required autocomplete="off"></label><button id="lb" type="submit">Ouvrir</button><p id="lm" role="status" aria-live="polite"></p></form></main>
<noscript>Cette page nécessite JavaScript.</noscript>
<script>(function(){var D=__DATA__;
function u(s){return Uint8Array.from(atob(s),function(c){return c.charCodeAt(0)})}
async function key(c,e,s){var m=await crypto.subtle.importKey('raw',new TextEncoder().encode(c+'\u0000'+e.trim().toLowerCase()),'PBKDF2',false,['deriveKey']);return crypto.subtle.deriveKey({name:'PBKDF2',salt:s,iterations:D.it,hash:'SHA-256'},m,{name:'AES-GCM',length:256},false,['decrypt'])}
document.getElementById('lk').addEventListener('submit',async function(ev){ev.preventDefault();var m=document.getElementById('lm'),btn=document.getElementById('lb');
if(!(window.crypto&&crypto.subtle)){m.textContent='Chiffrement indisponible dans ce contexte (ouvrir en https).';return}
btn.disabled=true;m.style.color='#16273d';m.textContent='Vérification…';var c=document.getElementById('lc').value,e=document.getElementById('le').value;
try{for(var i=0;i<D.w.length;i++){var w=D.w[i];try{var k=await key(c,e,u(w.s));var raw=await crypto.subtle.decrypt({name:'AES-GCM',iv:u(w.i),additionalData:new TextEncoder().encode('A260E2A-key')},k,u(w.k));
var ck=await crypto.subtle.importKey('raw',raw,'AES-GCM',false,['decrypt']);var pt=await crypto.subtle.decrypt({name:'AES-GCM',iv:u(D.iv),additionalData:new TextEncoder().encode('A260E2A')},ck,u(D.ct));
var h=new TextDecoder().decode(pt);document.open();document.write(h);document.close();return}catch(x){}}
m.style.color='#b3261e';m.textContent='Code ou adresse incorrects.'}finally{var c0=document.getElementById('lc'),b0=document.getElementById('lb');if(b0)b0.disabled=false;if(c0)c0.value=''}});})();</script></body></html>'''
