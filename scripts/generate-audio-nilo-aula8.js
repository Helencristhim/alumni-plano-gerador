#!/usr/bin/env node
const fs=require('fs'),path=require('path'),https=require('https');
const API_KEY=process.env.ELEVENLABS_API_KEY,DIR=path.join(__dirname,'..','public','audio','nilo-mesquita-patucci');
const ASH='VU16byTywsWv5JpI8rbc',RILEY='hA4zGnmTwX2NQiTRMt7o';
if(!fs.existsSync(DIR))fs.mkdirSync(DIR,{recursive:true});
const E=[
["Policy","aula8_policy.mp3",ASH],
["Implement","aula8_implement.mp3",RILEY],
["Reform","aula8_reform.mp3",ASH],
["Stakeholder","aula8_stakeholder.mp3",RILEY],
["Elect","aula8_elect.mp3",ASH],
["Suspend","aula8_suspend.mp3",RILEY],
["Appoint","aula8_appoint.mp3",ASH],
["Resolution","aula8_resolution.mp3",RILEY],
];
// Read the HTML to extract all aula8_ audioMap entries for examples, dialogue, etc.
const html=fs.readFileSync(path.join(__dirname,'..','public','professor','nilo-mesquita-patucci-aula8.html'),'utf8');
const mapMatch=html.match(/var audioMap = \{([\s\S]*?)\};/);
if(mapMatch){
  const entries=[...mapMatch[1].matchAll(/"([^"]+)":\s*"\/audio\/nilo-mesquita-patucci\/(aula8_[^"]+)"/g)];
  entries.forEach(m=>{
    const text=m[1], file=m[2];
    if(!E.find(e=>e[1]===file)){
      // Determine voice: dialogue lines with Riley character or female = RILEY, else ASH
      const voice=file.includes('dia1')||file.includes('dia3')||file.includes('dia5')||file.includes('dia7')||file.includes('listening1')?RILEY:ASH;
      E.push([text,file,voice]);
    }
  });
}
function gen(t,f,v){return new Promise((r,j)=>{const fp=path.join(DIR,f);if(fs.existsSync(fp)&&fs.statSync(fp).size>1000){console.log('  SKIP:',f);return r();}const b=JSON.stringify({text:t,model_id:'eleven_turbo_v2_5',voice_settings:{stability:.5,similarity_boost:.75}});const o={hostname:'api.elevenlabs.io',path:`/v1/text-to-speech/${v}`,method:'POST',headers:{'xi-api-key':API_KEY,'Content-Type':'application/json','Accept':'audio/mpeg','Content-Length':Buffer.byteLength(b)}};const q=https.request(o,res=>{if(res.statusCode!==200){let e='';res.on('data',d=>e+=d);res.on('end',()=>{console.error('  ERR',res.statusCode,f,e.substring(0,200));j(new Error('HTTP '+res.statusCode));});return;}const c=[];res.on('data',d=>c.push(d));res.on('end',()=>{const buf=Buffer.concat(c);fs.writeFileSync(fp,buf);console.log('  OK:',f,buf.length,'bytes');r();});});q.on('error',j);q.write(b);q.end();});}
async function main(){console.log(`Generating ${E.length} audio files for Nilo Aula 8...`);let ok=0,err=0;for(let i=0;i<E.length;i++){try{await gen(E[i][0],E[i][1],E[i][2]);ok++;if(i<E.length-1)await new Promise(r=>setTimeout(r,150));}catch(e){err++;console.error('Failed:',E[i][1],e.message);}}console.log(`Done: ${ok} OK, ${err} errors`);}
main().catch(console.error);
