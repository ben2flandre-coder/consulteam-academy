const fs=require('node:fs'),vm=require('node:vm'),assert=require('node:assert/strict'),path=require('node:path');
const root=path.join(__dirname,'..');
function run(page,search='',previous,blocked=false){const html=fs.readFileSync(path.join(root,page),'utf8');const script=html.match(/<script>([\s\S]*?)<\/script>/)[1];const state={mode:previous,participant:false};vm.runInNewContext(script,{URLSearchParams,location:{pathname:'/sessions/260053a/'+page,search},sessionStorage:{getItem:()=>{if(blocked)throw Error();return state.mode},setItem:(k,v)=>{state.mode=v}},document:{documentElement:{classList:{add:()=>state.participant=true}}}});return state}
for(const page of ['apprenants.html','apprenant.html','fiches.html','cordes.html','noeuds.html','approfondissement.html','complements.html','videos.html','programme.html','suivre.html'])assert.equal(run(page).participant,true,page);
for(const page of ['index.html','formateur.html','formulaires.html'])assert.equal(run(page).participant,false,page);
assert.equal(run('apprenant.html','',undefined,true).participant,true,'storage indisponible');
assert.equal(run('apprenant.html','?e=f').participant,false);assert.equal(run('apprenants.html','', 'f').participant,true);
assert.equal(run('index.html','', 'p').participant,false);
console.log('Parcours : 17 cas de navigation et de stockage contrôlés.');
