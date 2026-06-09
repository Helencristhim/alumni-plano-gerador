const fs = require('fs');
const path = require('path');
const API_KEY = process.env.ELEVENLABS_API_KEY;
const GABY = '5vkxOzoz40FrElmLP4P7';
const JUAN = 'rBqbBncz61jpuaOTI1GW';
const DIR = path.join(__dirname, '..', 'public', 'audio', 'juliana-marques');

const P = [
  { text: "Oficina", voice: "gaby", file: "aula4_oficina.mp3" },
  { text: "Embarazada", voice: "juan", file: "aula4_embarazada.mp3" },
  { text: "Largo", voice: "gaby", file: "aula4_largo.mp3" },
  { text: "Éxito", voice: "juan", file: "aula4_exito.mp3" },
  { text: "Vaso", voice: "gaby", file: "aula4_vaso.mp3" },
  { text: "Constipado", voice: "juan", file: "aula4_constipado.mp3" },
  { text: "Escritura", voice: "gaby", file: "aula4_escritura.mp3" },
  { text: "Propina", voice: "juan", file: "aula4_propina.mp3" },
  { text: "Trabajo en una oficina grande.", voice: "gaby", file: "aula4_trabajo_en_oficina.mp3" },
  { text: "Mi hermana está embarazada.", voice: "juan", file: "aula4_hermana_embarazada.mp3" },
  { text: "El río es muy largo.", voice: "gaby", file: "aula4_rio_largo.mp3" },
  { text: "La película fue un éxito.", voice: "juan", file: "aula4_pelicula_exito.mp3" },
  { text: "Dame un vaso de agua, por favor.", voice: "gaby", file: "aula4_vaso_agua.mp3" },
  { text: "Estoy constipado, tengo la nariz tapada.", voice: "juan", file: "aula4_constipado_nariz.mp3" },
  { text: "La escritura de la casa está en el banco.", voice: "gaby", file: "aula4_escritura_casa.mp3" },
  { text: "Dejé una propina en el restaurante.", voice: "juan", file: "aula4_propina_restaurante.mp3" },
  { text: "Juliana llega a la oficina de su colega en Madrid. La oficina es grande y moderna. En la mesa hay un vaso de agua. Su colega Carmen le dice: Nuestro último proyecto fue un éxito. El informe es largo pero muy completo.", voice: "juan", file: "aula4_listening1_juliana_oficina.mp3" },
  { text: "¡Hola Juliana! Bienvenida a nuestra oficina. Es bastante grande, ¿verdad?", voice: "juan", file: "aula4_dialogo_carmen_1.mp3" },
  { text: "Sí, es muy grande. Mi oficina en Curitiba es más pequeña.", voice: "gaby", file: "aula4_dialogo_juliana_1.mp3" },
  { text: "Mira, allí está Rosa. Está embarazada, va a tener un bebé en octubre.", voice: "juan", file: "aula4_dialogo_carmen_2.mp3" },
  { text: "¡Qué bien! Felicidades para ella.", voice: "gaby", file: "aula4_dialogo_juliana_2.mp3" },
  { text: "Y aquí tenemos agua. Toma un vaso si quieres.", voice: "juan", file: "aula4_dialogo_carmen_3.mp3" },
  { text: "¡Gracias! Sí, quiero un vaso de agua.", voice: "gaby", file: "aula4_dialogo_juliana_3.mp3" },
  { text: "Nuestro último proyecto fue un éxito. El informe es largo pero muy completo.", voice: "juan", file: "aula4_dialogo_carmen_4.mp3" },
  { text: "Excelente. Quiero leer el informe completo.", voice: "gaby", file: "aula4_dialogo_juliana_4.mp3" },
  { text: "Mi oficina está en el centro de la ciudad. Es un espacio grande con muchas ventanas. En mi mesa tengo un vaso de agua y los documentos del último proyecto. Fue un éxito total. El informe es largo, tiene más de cien páginas. La escritura de la propiedad está en el banco.", voice: "gaby", file: "aula4_listening2_oficina_completo.mp3" },
  { text: "Oficina significa el lugar donde trabajas.", voice: "gaby", file: "aula4_oficina_significa.mp3" },
  { text: "Embarazada significa que va a tener un bebé.", voice: "juan", file: "aula4_embarazada_significa.mp3" },
  { text: "Largo significa que tiene mucha longitud.", voice: "gaby", file: "aula4_largo_significa.mp3" },
  { text: "Éxito significa cuando algo sale muy bien.", voice: "juan", file: "aula4_exito_significa.mp3" },
  { text: "Oficina, embarazada, largo, éxito, vaso, constipado, escritura, propina. Estas son palabras que parecen iguales en portugués pero significan algo diferente en español.", voice: "gaby", file: "aula4_order_l4_ordering.mp3" },
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
  let g = 0, s = 0, e = 0;
  for (const p of P) {
    const o = path.join(DIR, p.file);
    if (fs.existsSync(o)) { console.log('SKIP: ' + p.file); s++; continue; }
    try {
      const sz = await gen(p.text, p.voice === 'gaby' ? GABY : JUAN, o);
      console.log('OK: ' + p.file + ' (' + Math.round(sz / 1024) + 'KB) [' + p.voice + ']');
      g++;
      await new Promise(r => setTimeout(r, 500));
    } catch (err) { console.error('ERR: ' + p.file + ' ' + err.message); e++; }
  }
  console.log('\nGen: ' + g + ' Skip: ' + s + ' Err: ' + e);
  console.log('Total MP3s: ' + fs.readdirSync(DIR).filter(f => f.endsWith('.mp3')).length);
}
main();
