(function(){
var H=["6e496109d427c835e34512420e2bebdec0e7ef7cf36a133bc83df790c92ec6fb", "eaadc7c305372c6836bc8106541f5d2d17ab6ef18cca82330cbfb90a34942a30", "38bcf7553ee4efaabd3b6f53e1f627007a5f55eb6bcf57915464ac9f1d65d2b5"];
var b=document.body;
function ok(){try{return sessionStorage.getItem("sstacc")==="1"}catch(e){return false}}
function open_(){b.classList.add("open");var g=document.querySelector(".gate");if(g)g.remove()}
if(ok()){open_();return}
function hex(buf){return Array.prototype.map.call(new Uint8Array(buf),function(x){return("0"+x.toString(16)).slice(-2)}).join("")}
function sha(s){return crypto.subtle.digest("SHA-256",new TextEncoder().encode("sst|"+s)).then(hex)}
var m=document.getElementById("main");
var g=document.createElement("section");g.className="gate";g.setAttribute("aria-labelledby","gt");
g.innerHTML='<h1 id="gt">🔒 Accès réservé</h1><p>Cet espace est destiné au formateur. Saisissez votre code d’accès ou votre adresse e-mail.</p><form><label for="gc">Code ou adresse e-mail</label><input id="gc" name="c" type="text" autocomplete="off" autocapitalize="off" spellcheck="false" required><button class="btn" type="submit">Entrer</button></form><p class="gerr" role="status" aria-live="polite"></p><p><small>Contrôle d’accès simple, adapté à un site statique : il limite l’affichage, il ne protège pas les fichiers.</small></p>';
m.insertBefore(g,m.firstChild);
g.querySelector("form").addEventListener("submit",function(e){e.preventDefault();
var v=document.getElementById("gc").value,err=g.querySelector(".gerr");
if(!(window.crypto&&crypto.subtle)){err.textContent="Contrôle impossible dans ce navigateur (connexion sécurisée requise).";return}
var a=v.toLowerCase().replace(/\s+/g,""),c=v.toLowerCase().replace(/[^a-z0-9]/g,"");
Promise.all([sha(a),sha(c)]).then(function(r){
if(H.indexOf(r[0])>-1||H.indexOf(r[1])>-1){try{sessionStorage.setItem("sstacc","1")}catch(x){}open_()}
else{err.textContent="Code ou adresse non reconnu.";document.getElementById("gc").select()}})})
})();