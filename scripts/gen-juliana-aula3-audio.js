const fs = require('fs');
const path = require('path');
const API_KEY = process.env.ELEVENLABS_API_KEY;
const GABY = '5vkxOzoz40FrElmLP4P7';
const JUAN = 'rBqbBncz61jpuaOTI1GW';
const DIR = path.join(__dirname, '..', 'public', 'audio', 'juliana-marques');

const P = [
  { text: "Trabajar", voice: "gaby", file: "aula3_trabajar.mp3" },
  { text: "Evaluar", voice: "juan", file: "aula3_evaluar.mp3" },
  { text: "Revisar", voice: "gaby", file: "aula3_revisar.mp3" },
  { text: "Visitar", voice: "juan", file: "aula3_visitar.mp3" },
  { text: "Preparar", voice: "gaby", file: "aula3_preparar.mp3" },
  { text: "Normalmente", voice: "juan", file: "aula3_normalmente.mp3" },
  { text: "Cada semana", voice: "gaby", file: "aula3_cada_semana.mp3" },
  { text: "Por la mañana", voice: "juan", file: "aula3_por_la_manana.mp3" },
  { text: "Por la mañana, trabajo en la oficina.", voice: "gaby", file: "aula3_por_la_manana_trabajo.mp3" },
  { text: "Normalmente evalúo inmuebles por la mañana.", voice: "juan", file: "aula3_normalmente_evaluo.mp3" },
  { text: "Reviso los documentos cada semana.", voice: "gaby", file: "aula3_reviso_documentos.mp3" },
  { text: "Cada semana visito inmuebles nuevos.", voice: "juan", file: "aula3_cada_semana_visito.mp3" },
  { text: "Preparo informes de evaluación.", voice: "gaby", file: "aula3_preparo_informes.mp3" },
  { text: "Trabajo como evaluadora de inmuebles.", voice: "juan", file: "aula3_trabajo_evaluadora.mp3" },
  { text: "Normalmente preparo los informes por la tarde.", voice: "gaby", file: "aula3_normalmente_preparo.mp3" },
  { text: "Cada semana evalúo tres o cuatro inmuebles.", voice: "juan", file: "aula3_cada_semana_evaluo.mp3" },
  { text: "Hola, soy Carmen. Normalmente trabajo por la mañana. Primero reviso los correos electrónicos. Después visito inmuebles. Por la tarde preparo informes. Cada semana evalúo cinco o seis propiedades.", voice: "juan", file: "aula3_listening_carmen_dia.mp3" },
  { text: "Carmen, ¿cómo es tu día normalmente?", voice: "gaby", file: "aula3_dialogo_juliana_1.mp3" },
  { text: "Normalmente trabajo por la mañana. Reviso correos y después visito inmuebles.", voice: "juan", file: "aula3_dialogo_carmen_1.mp3" },
  { text: "¿Cuántos inmuebles visitas cada semana?", voice: "gaby", file: "aula3_dialogo_juliana_2.mp3" },
  { text: "Cada semana visito cinco o seis. ¿Y tú?", voice: "juan", file: "aula3_dialogo_carmen_2.mp3" },
  { text: "Yo normalmente evalúo tres o cuatro. Por la tarde preparo los informes.", voice: "gaby", file: "aula3_dialogo_juliana_3.mp3" },
  { text: "¡Qué interesante! Yo también preparo informes por la tarde.", voice: "juan", file: "aula3_dialogo_carmen_3.mp3" },
  { text: "Sí, es una rutina similar. Me gusta trabajar por la mañana.", voice: "gaby", file: "aula3_dialogo_juliana_4.mp3" },
  { text: "A mí también. Por la mañana tengo más energía.", voice: "juan", file: "aula3_dialogo_carmen_4.mp3" },
  { text: "Yo trabajo por la mañana y preparo informes por la tarde.", voice: "gaby", file: "aula3_yo_trabajo_por_la_manana.mp3" },
  { text: "Normalmente reviso los documentos antes de visitar el inmueble.", voice: "gaby", file: "aula3_normalmente_reviso.mp3" },
  { text: "Cada semana visito inmuebles en diferentes zonas.", voice: "gaby", file: "aula3_cada_semana_visito_short.mp3" },
  { text: "Preparo informes de evaluación para los bancos.", voice: "gaby", file: "aula3_preparo_informes_evaluacion.mp3" },
  { text: "Por la mañana reviso correos. Después visito inmuebles. Normalmente evalúo tres propiedades. Por la tarde preparo los informes. Cada semana trabajo cinco días.", voice: "gaby", file: "aula3_order_l3_ordering.mp3" },
];

async function gen(t, v, o) {
  const r = await fetch('https://api.elevenlabs.io/v1/text-to-speech/' + v, {
    method: 'POST', headers: { 'xi-api-key': API_KEY, 'Content-Type': 'application/json' },
    body: JSON.stringify({ text: t, model_id: 'eleven_multilingual_v2', voice_settings: { stability: .5, similarity_boost: .75, style: 0, use_speaker_boost: true } })
  });
  if (!r.ok) throw new Error(r.status + ' ' + await r.text());
  const b = Buffer.from(await r.arrayBuffer());
  fs.writeFileSync(o, b);
  return b.length;
}

async function main() {
  if (!API_KEY) { console.error('No API key'); process.exit(1); }
  let g = 0, s = 0;
  for (const p of P) {
    const o = path.join(DIR, p.file);
    if (fs.existsSync(o)) { console.log('SKIP: ' + p.file); s++; continue; }
    try {
      const sz = await gen(p.text, p.voice === 'gaby' ? GABY : JUAN, o);
      console.log('OK: ' + p.file + ' (' + Math.round(sz / 1024) + 'KB) [' + p.voice + ']');
      g++;
      await new Promise(r => setTimeout(r, 500));
    } catch (e) { console.error('ERR: ' + p.file + ' ' + e.message); }
  }
  console.log('\nDone! Gen: ' + g + ' Skip: ' + s);
}
main();
