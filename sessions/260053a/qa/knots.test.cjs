const assert=require('node:assert/strict');
const K=require('../js/knot-anim.js');const G=require('../js/knots-geo.js');
require('../js/knots-tresse.js');require('../js/knots-sangle.js');
const report=[];
for(const [name,points,count] of [['arrêt simple',G.overhandOpen(1.5),3],['huit simple',G.huitOpen(1.5),4],['huit tressé',globalThis.KnotTresse().points,16],['sangle',globalThis.KnotSangle().points,12]]){
  assert(points.every(p=>Number.isFinite(p.x)&&Number.isFinite(p.y)&&Number.isFinite(p.z)),name);
  const crosses=K.crossings(points,false);assert.equal(crosses.length,count,name);
  const z=at=>{const i=Math.floor(at),u=at-i;return points[i].z+(points[i+1].z-points[i].z)*u};
  assert(crosses.every(c=>Math.abs(z(c.i)-z(c.j))>1e-4),'dessus/dessous '+name);
  report.push({tracé:name,points:points.length,croisements:crosses.length});
}
console.log(JSON.stringify({limite:'Contrôle géométrique du dessin ; aucune validation de geste ni d’usage en charge.',tracés:report},null,2));
