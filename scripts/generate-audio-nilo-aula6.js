#!/usr/bin/env node
const fs=require('fs'),path=require('path'),https=require('https');
const API_KEY=process.env.ELEVENLABS_API_KEY,DIR=path.join(__dirname,'..','public','audio','nilo-mesquita-patucci');
const ASH='VU16byTywsWv5JpI8rbc',RILEY='hA4zGnmTwX2NQiTRMt7o';
if(!fs.existsSync(DIR))fs.mkdirSync(DIR,{recursive:true});
const E=[
["Diverse","aula6_diverse.mp3",ASH],
["Landmark","aula6_landmark.mp3",RILEY],
["Located","aula6_located.mp3",ASH],
["Vibrant","aula6_vibrant.mp3",RILEY],
["Population","aula6_population.mp3",ASH],
["District","aula6_district.mp3",RILEY],
["Heritage","aula6_heritage.mp3",ASH],
["Renowned","aula6_renowned.mp3",RILEY],
["Sao Paulo is a very diverse city with people from all over the world.","aula6_ex_diverse.mp3",ASH],
["The Ibirapuera Park is a famous landmark in Sao Paulo.","aula6_ex_landmark.mp3",RILEY],
["The stadium is located in the east side of the city.","aula6_ex_located.mp3",ASH],
["Sao Paulo has a vibrant nightlife and cultural scene.","aula6_ex_vibrant.mp3",RILEY],
["Sao Paulo has a population of over twelve million people.","aula6_ex_population.mp3",ASH],
["Liberdade is the Japanese district in Sao Paulo.","aula6_ex_district.mp3",RILEY],
["Brazil has a rich cultural heritage that includes music, dance, and football.","aula6_ex_heritage.mp3",ASH],
["Corinthians is renowned for its passionate fan base.","aula6_ex_renowned.mp3",RILEY],
["Nilo, I would love to learn more about your city. What is Sao Paulo like?","aula6_dia1.mp3",RILEY],
["Sao Paulo is a very diverse and vibrant city. There are many different cultures and there is always something happening.","aula6_dia2.mp3",ASH],
["That sounds incredible! Are there any famous landmarks I should visit?","aula6_dia3.mp3",RILEY],
["Absolutely! There is a beautiful park called Ibirapuera, and there are several renowned museums in the city center.","aula6_dia4.mp3",ASH],
["What about the cultural heritage? I have heard Brazilian culture is fascinating.","aula6_dia5.mp3",RILEY],
["There is a rich heritage of music, dance, and football. There are many festivals throughout the year, and the food is incredibly diverse.","aula6_dia6.mp3",ASH],
["And where is Corinthians located? Is it in the city center?","aula6_dia7.mp3",RILEY],
["The stadium is located in the eastern district of Sao Paulo. There are many loyal fans in that area. The population there is very passionate about football.","aula6_dia8.mp3",ASH],
["There is a famous stadium in Sao Paulo.","aula6_fill1.mp3",ASH],
["There are many compliance professionals in Brazil.","aula6_fill2.mp3",RILEY],
["There is a vibrant cultural scene in the city.","aula6_fill3.mp3",ASH],
["There are several renowned universities nearby.","aula6_fill4.mp3",RILEY],
["There is a diverse population in Sao Paulo.","aula6_fill5.mp3",ASH],
["There is a famous stadium in my city.","aula6_speech1.mp3",ASH],
["There are many diverse cultures in Sao Paulo.","aula6_speech2.mp3",ASH],
["The city is renowned for its vibrant heritage.","aula6_speech3.mp3",ASH],
["Good afternoon, everyone. Let me tell you about my home city, Sao Paulo. It is one of the largest and most diverse cities in the world. There are over twelve million people living there, and the population is incredibly multicultural. There is a vibrant cultural scene with renowned museums, theaters, and music venues. One of the most famous landmarks is Ibirapuera Park, which is located in the south of the city. There are several important districts, including Liberdade, which has a strong Japanese heritage. The city is also renowned for its football culture. Corinthians, where I work, is located in the eastern district, and there are millions of passionate fans across the city.","aula6_listening1.mp3",ASH],
["Hello, my name is Yuki Tanaka, and I am from Tokyo, Japan. Tokyo is a vibrant and diverse city with a population of nearly fourteen million people. There are many famous landmarks, including the Tokyo Tower and the Meiji Shrine. The city is located on the eastern coast of Japan. There is a rich cultural heritage that combines traditional Japanese customs with modern innovation. There are several renowned districts, such as Shibuya and Shinjuku, which are known for their energy and nightlife. Tokyo is also home to many diverse communities from around the world. There is always something new to discover in this incredible city.","aula6_listening2.mp3",RILEY],
["Approach a landmark. Describe the location. Mention the population. Talk about the heritage. Share what makes it vibrant.","aula6_order_l6.mp3",ASH],
];
function gen(t,f,v){return new Promise((r,j)=>{const fp=path.join(DIR,f);if(fs.existsSync(fp)&&fs.statSync(fp).size>1000){console.log('  SKIP:',f);return r();}const b=JSON.stringify({text:t,model_id:'eleven_turbo_v2_5',voice_settings:{stability:.5,similarity_boost:.75}});const o={hostname:'api.elevenlabs.io',path:`/v1/text-to-speech/${v}`,method:'POST',headers:{'xi-api-key':API_KEY,'Content-Type':'application/json','Accept':'audio/mpeg','Content-Length':Buffer.byteLength(b)}};const q=https.request(o,res=>{if(res.statusCode!==200){let e='';res.on('data',d=>e+=d);res.on('end',()=>{console.error('  ERR',res.statusCode,f,e.substring(0,200));j(new Error('HTTP '+res.statusCode));});return;}const c=[];res.on('data',d=>c.push(d));res.on('end',()=>{const buf=Buffer.concat(c);fs.writeFileSync(fp,buf);console.log('  OK:',f,buf.length,'bytes');r();});});q.on('error',j);q.write(b);q.end();});}
async function main(){console.log(`Generating ${E.length} audio files for Nilo Aula 6...`);let ok=0,err=0;for(let i=0;i<E.length;i++){try{await gen(E[i][0],E[i][1],E[i][2]);ok++;if(i<E.length-1)await new Promise(r=>setTimeout(r,150));}catch(e){err++;console.error('Failed:',E[i][1],e.message);}}console.log(`Done: ${ok} OK, ${err} errors`);}
main().catch(console.error);
