const fs=require('fs'),path=require('path');
const API_KEY=process.env.ELEVENLABS_API_KEY;
const GABY='5vkxOzoz40FrElmLP4P7',JUAN='rBqbBncz61jpuaOTI1GW';
const DIR=path.join(__dirname,'..','public','audio','juliana-marques');
const P=[
  { text: "[order-l5]", voice: "gaby", file: "aula5_order_l5_ordering.mp3" },
  { text: "Hola, mucho gusto. Me llamo Juliana. Soy brasilena.", voice: "juan", file: "aula5_hola_mucho_gusto_juliana.mp3" },
  { text: "Soy arquitecta. Me dedico a la evaluacion de inmuebles.", voice: "gaby", file: "aula5_soy_arquitecta_me_dedico.mp3" },
  { text: "Normalmente trabajo por la manana. Cada semana evaluo dos inmuebles.", voice: "juan", file: "aula5_normalmente_trabajo_evaluo.mp3" },
  { text: "Estoy contenta de estar aqui. Soy miembro de la UPAV.", voice: "gaby", file: "aula5_estoy_contenta_miembro.mp3" },
  { text: "Pueden escucharme bien?", voice: "juan", file: "aula5_pueden_escucharme.mp3" },
  { text: "En mi opinion, el mercado brasileno es muy interesante.", voice: "gaby", file: "aula5_en_mi_opinion_mercado.mp3" },
  { text: "Estoy de acuerdo con lo que dice Maria.", voice: "juan", file: "aula5_estoy_de_acuerdo.mp3" },
  { text: "Gracias por la reunion. Ha sido muy productiva.", voice: "gaby", file: "aula5_gracias_reunion_productiva.mp3" },
  { text: "Hola a todas. Bienvenidas a la primera reunion virtual del grupo de mujeres evaluadoras.", voice: "juan", file: "aula5_maria_bienvenidas.mp3" },
  { text: "Vamos a empezar presentandonos. Juliana, puedes empezar?", voice: "gaby", file: "aula5_maria_empezar.mp3" },
  { text: "Hola, mucho gusto. Me llamo Juliana Marques. Soy brasilena, de Curitiba.", voice: "juan", file: "aula5_juliana_presentacion1.mp3" },
  { text: "Soy arquitecta. Me dedico a la evaluacion de inmuebles. Soy miembro de la UPAV.", voice: "gaby", file: "aula5_juliana_presentacion2.mp3" },
  { text: "Hola Juliana! Que bien que estes aqui. Como es tu trabajo normalmente?", voice: "juan", file: "aula5_carmen_pregunta.mp3" },
  { text: "Normalmente trabajo por la manana. Cada semana evaluo dos o tres inmuebles. Preparo los informes por la tarde.", voice: "gaby", file: "aula5_juliana_rutina.mp3" },
  { text: "Que interesante! Yo soy Pilar, de Buenos Aires. Tambien soy evaluadora. Mi oficina esta en el centro de la ciudad.", voice: "juan", file: "aula5_pilar_intro.mp3" },
  { text: "Hola a todas. Bienvenidas a la primera reunion virtual del grupo de mujeres evaluadoras. Soy Maria, la coordinadora. Hoy tenemos tres participantes: Juliana de Brasil, Carmen de Chile y Pilar de Argentina. Todas somos evaluadoras de inmuebles. Juliana trabaja en Curitiba. Normalmente evalua dos inmuebles cada semana. Carmen tiene su oficina en Santiago. Pilar trabaja en Buenos Aires. El mercado inmobiliario en Latinoamerica es muy interesante. Gracias a todas por participar.", voice: "gaby", file: "aula5_listening1_reunion.mp3" },
  { text: "Hola, soy Pilar. Soy de Buenos Aires, Argentina. Soy evaluadora de inmuebles. Mi oficina esta en el centro de la ciudad. Es una oficina grande. Normalmente trabajo de lunes a viernes. Por la manana reviso los documentos. Por la tarde visito los inmuebles. Cada semana evaluo tres o cuatro propiedades. Mi ultimo proyecto fue un exito. El informe era largo, pero muy completo. Estoy contenta de estar en este grupo.", voice: "juan", file: "aula5_listening2_pilar.mp3" },
  { text: "Yo soy arquitecta.", voice: "gaby", file: "aula5_yo_soy_arquitecta.mp3" },
  { text: "Hoy estoy contenta.", voice: "juan", file: "aula5_hoy_estoy_contenta.mp3" },
];
async function gen(t,v,o){const r=await fetch('https://api.elevenlabs.io/v1/text-to-speech/'+v,{method:'POST',headers:{'xi-api-key':API_KEY,'Content-Type':'application/json'},body:JSON.stringify({text:t,model_id:'eleven_multilingual_v2',voice_settings:{stability:.5,similarity_boost:.75,style:0,use_speaker_boost:true}})});if(!r.ok)throw new Error(r.status);const b=Buffer.from(await r.arrayBuffer());fs.writeFileSync(o,b);return b.length}
async function main(){if(!API_KEY){console.error('No key');process.exit(1)}let g=0,s=0;for(const p of P){const o=path.join(DIR,p.file);if(fs.existsSync(o)){s++;continue}try{const sz=await gen(p.text,p.voice==='gaby'?GABY:JUAN,o);console.log('OK:'+p.file+'('+Math.round(sz/1024)+'KB)['+p.voice+']');g++;await new Promise(r=>setTimeout(r,500))}catch(e){console.error('ERR:'+p.file)}}console.log('Gen:'+g+' Skip:'+s)}
main();