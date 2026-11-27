const fs=require('node:fs'),path=require('node:path');
const sharp=require(process.argv[2]);
const root=path.resolve(__dirname,'..'),dir=path.join(__dirname,'render-visuals-2.0');
fs.mkdirSync(dir,{recursive:true});
(async()=>{
const files=fs.readdirSync(path.join(root,'assets/svg/v20')).filter(x=>x.endsWith('.svg')).sort();
const tiles=[];
for(let i=0;i<files.length;i++){
 const p=path.join(root,'assets/svg/v20',files[i]),dest=path.join(dir,files[i].replace('.svg','.png'));
 await sharp(p).png().toFile(dest);
 const tile=await sharp(dest).resize(550,310).png().toBuffer();tiles.push({input:tile,left:(i%3)*550,top:Math.floor(i/3)*310});
}
await sharp({create:{width:1650,height:Math.ceil(files.length/3)*310,channels:3,background:'#e2eaf2'}}).composite(tiles).png().toFile(path.join(dir,'contact.png'));
console.log(JSON.stringify({rendered:files.length,directory:dir}));
})().catch(e=>{console.error(e);process.exit(1)});
