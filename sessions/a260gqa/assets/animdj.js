(function(){
var tabs=[].slice.call(document.querySelectorAll(".dtab")),secs=[].slice.call(document.querySelectorAll(".djs"));if(!tabs.length)return;
var cur=null,st={};
function arts(s){return [].slice.call(s.querySelectorAll(".stp"))}
function show(s,k){var a=arts(s),all=s.getAttribute("data-all")==="1";st[s.id]=k;
a.forEach(function(x,j){x.hidden=!all&&j!==k});var pc=s.querySelector(".pc");pc.textContent="Étape "+(k+1)+" sur "+a.length;
s.querySelector(".pp").disabled=k===0;s.querySelector(".pn").disabled=k===a.length-1}
var panel=document.getElementById("dia-panel");
function tab(id,k){if(id==="dia"){secs.forEach(function(s){s.hidden=true});panel.hidden=false;tabs.forEach(function(t){t.setAttribute("aria-pressed",t.getAttribute("data-t")==="dia")});document.dispatchEvent(new Event("dia-open"));if(history.replaceState)history.replaceState(null,"","#dia");return}panel.hidden=true;secs.forEach(function(s){s.hidden=s.id!==id});tabs.forEach(function(t){t.setAttribute("aria-pressed",t.getAttribute("data-t")===id)});
var s=document.getElementById(id);cur=s;show(s,k||0);if(history.replaceState)history.replaceState(null,"","#"+id+(k?"-b"+(k+1):""))}
secs.forEach(function(s){var nav=s.querySelector(".pnav");nav.hidden=false;
nav.querySelector(".pp").onclick=function(){show(s,Math.max(0,(st[s.id]||0)-1));window.scrollTo(0,s.offsetTop)};
nav.querySelector(".pn").onclick=function(){show(s,Math.min(arts(s).length-1,(st[s.id]||0)+1));window.scrollTo(0,s.offsetTop)};
var pa=nav.querySelector(".pa");pa.onclick=function(){var on=s.getAttribute("data-all")!=="1";s.setAttribute("data-all",on?"1":"0");pa.setAttribute("aria-pressed",on);pa.textContent=on?"Un bloc à la fois":"Tout afficher";show(s,st[s.id]||0)};
s.querySelectorAll(".chips a").forEach(function(a,j){a.onclick=function(e){e.preventDefault();s.setAttribute("data-all","0");pa.setAttribute("aria-pressed","false");pa.textContent="Tout afficher";show(s,j)}})});
document.addEventListener("click",function(e){var l=e.target.closest&&e.target.closest('a[href^="#j"]');if(!l||l.closest(".chips"))return;var el=document.getElementById(l.getAttribute("href").slice(1));if(!el)return;var ar=el.closest(".stp");if(!ar)return;var s=ar.closest(".djs");e.preventDefault();tab(s.id,arts(s).indexOf(ar));setTimeout(function(){ar.scrollIntoView()},0)});
tabs.forEach(function(t){t.onclick=function(){tab(t.getAttribute("data-t"),0)}});
var m=/^#(j[12][ma]|dia)(?:-b(\d+))?$/.exec(location.hash||"");tab(m?m[1]:"j1m",m&&m[2]?+m[2]-1:0);
})();