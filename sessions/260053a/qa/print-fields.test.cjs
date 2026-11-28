/* Vérifie le cycle avant/après impression et la conservation d'une note longue. */
const fs=require('node:fs'),vm=require('node:vm'),assert=require('node:assert/strict'),path=require('node:path');
const root=path.join(__dirname,'..');
const html=fs.readFileSync(path.join(root,'formulaires.html'),'utf8');
assert.equal(/data-save=/.test(html),false,'aucune saisie individuelle restaurée au prochain participant');
const events={},mirrors=[],sources=[],excluded=[];
function classes(onRemove){const values=new Set();return{add:x=>values.add(x),remove:x=>{values.delete(x);if(onRemove)onRemove(x)},contains:x=>values.has(x)}}
function field(tag,value){const e={tagName:tag,value,classList:classes(),insertAdjacentElement:(_,p)=>mirrors.push(p)};sources.push(e);return e;}
const note='Observation longue\n'+('Correction puis nouvelle tentative. '.repeat(40))+'FIN';
const ta=field('TEXTAREA',note),select=field('SELECT','EC');select.options=[{text:'NO'},{text:'EC'}];select.selectedIndex=1;
const sibling={classList:classes()};excluded.push(sibling);
const body={},section={parentElement:{children:[]}},button={addEventListener:(name,fn)=>button[name]=fn,closest:()=>section};
section.parentElement.children=[section,sibling];section.parentElement.parentElement=body;body.children=[section.parentElement];
const document={documentElement:{classList:classes()},body,
 addEventListener:(name,fn)=>events[name]=fn,
 querySelector:()=>null,getElementById:()=>null,
 querySelectorAll:selector=>({'[data-print-section]':[button],'#forms textarea,#forms select':sources,'.print-value':mirrors.slice(),'.print-source':sources.filter(e=>e.classList.contains('print-source')),'.print-exclude':excluded.filter(e=>e.classList.contains('print-exclude'))}[selector]||[]),
 createElement:()=>({remove(){mirrors.splice(mirrors.indexOf(this),1)}})};
const window={addEventListener:(name,fn)=>events[name]=fn,print:()=>events.beforeprint()};
vm.runInNewContext(fs.readFileSync(path.join(root,'js/common.js'),'utf8'),{window,document,location:{pathname:'/sessions/260053a/formulaires.html'},localStorage:{getItem:()=>null,setItem:()=>{throw Error('stockage inattendu')},removeItem:()=>{}},URLSearchParams});
events.DOMContentLoaded();button.click();
assert.equal(mirrors.length,2);assert.equal(mirrors[0].textContent,note);assert.equal(mirrors[1].textContent,'EC');assert.equal(ta.classList.contains('print-source'),true);
assert.equal(sibling.classList.contains('print-exclude'),true);
events.beforeprint();assert.equal(mirrors.length,2,'pas de doublon après deux appels');
events.afterprint();assert.equal(mirrors.length,0);assert.equal(ta.classList.contains('print-source'),false);assert.equal(sibling.classList.contains('print-exclude'),false);
assert.equal(ta.value,note,'la saisie reste disponible dans l’onglet après impression');
console.log('Impression : notes complètes, sélection, isolation, nettoyage et absence de sauvegarde vérifiés.');
