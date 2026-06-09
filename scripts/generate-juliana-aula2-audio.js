const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const GABY_ID = '5vkxOzoz40FrElmLP4P7';
const JUAN_MANUEL_ID = 'rBqbBncz61jpuaOTI1GW';

const OUTPUT_DIR = path.join(__dirname, '..', 'public', 'audio', 'juliana-marques');

const PHRASES = [
  { text: "Nacionalidad", voice: "gaby", file: "aula2_nacionalidad.mp3" },
  { text: "Brasileña", voice: "gaby", file: "aula2_brasilena.mp3" },
  { text: "Dedicarse a", voice: "juan_manuel", file: "aula2_dedicarse_a.mp3" },
  { text: "Especialidad", voice: "gaby", file: "aula2_especialidad.mp3" },
  { text: "Inmueble", voice: "juan_manuel", file: "aula2_inmueble.mp3" },
  { text: "Miembro", voice: "gaby", file: "aula2_miembro.mp3" },
  { text: "Congreso", voice: "juan_manuel", file: "aula2_congreso.mp3" },
  { text: "Presentarse", voice: "gaby", file: "aula2_presentarse.mp3" },
  { text: "Mi nacionalidad es brasileña.", voice: "gaby", file: "aula2_mi_nacionalidad_es_brasilena.mp3" },
  { text: "Me dedico a la evaluación de inmuebles.", voice: "gaby", file: "aula2_me_dedico_a_evaluacion.mp3" },
  { text: "Mi especialidad es la evaluación de inmuebles.", voice: "juan_manuel", file: "aula2_mi_especialidad.mp3" },
  { text: "Soy miembro del congreso de la UPAV.", voice: "gaby", file: "aula2_soy_miembro_congreso.mp3" },
  { text: "Quiero presentarme ante los colegas.", voice: "juan_manuel", file: "aula2_quiero_presentarme.mp3" },
  { text: "Soy brasileña, de Curitiba.", voice: "gaby", file: "aula2_soy_brasilena_de_curitiba.mp3" },
  { text: "Mi especialidad son los inmuebles.", voice: "juan_manuel", file: "aula2_mi_especialidad_inmuebles.mp3" },
  { text: "Estoy en el congreso de la UPAV.", voice: "gaby", file: "aula2_estoy_en_congreso.mp3" },
  { text: "Soy brasileña.", voice: "gaby", file: "aula2_soy_brasilena.mp3" },
  { text: "Estoy contenta de estar aquí.", voice: "gaby", file: "aula2_estoy_contenta.mp3" },
  { text: "Soy arquitecta y estoy en Madrid.", voice: "gaby", file: "aula2_soy_arquitecta_estoy_madrid.mp3" },
  { text: "Yo soy miembro de la UPAV. Estoy aquí para el congreso.", voice: "gaby", file: "aula2_soy_miembro_estoy_congreso.mp3" },
  { text: "Hola, me llamo Juliana. Soy brasileña. Soy arquitecta. Mi especialidad es la evaluación de inmuebles. Soy miembro de la UPAV. Estoy aquí para el congreso de Madrid.", voice: "gaby", file: "aula2_presentacion_completa.mp3" },
  { text: "Hola, soy Carmen. Soy de Chile. Soy evaluadora y miembro de la UPAV. Mi especialidad es la evaluación de terrenos. Estoy contenta de estar aquí en Madrid.", voice: "juan_manuel", file: "aula2_listening_carmen.mp3" },
  { text: "Hola Carmen, mucho gusto. Me llamo Juliana.", voice: "gaby", file: "aula2_dialogo_juliana_1.mp3" },
  { text: "¡Hola Juliana! Encantada. ¿De dónde eres?", voice: "juan_manuel", file: "aula2_dialogo_carmen_1.mp3" },
  { text: "Soy brasileña, de Curitiba. ¿Y tú?", voice: "gaby", file: "aula2_dialogo_juliana_2.mp3" },
  { text: "Soy de Santiago de Chile. ¿A qué te dedicas?", voice: "juan_manuel", file: "aula2_dialogo_carmen_2.mp3" },
  { text: "Soy arquitecta. Mi especialidad es la evaluación de inmuebles.", voice: "gaby", file: "aula2_dialogo_juliana_3.mp3" },
  { text: "¡Qué interesante! Yo también soy evaluadora. Mi especialidad es la evaluación de terrenos.", voice: "juan_manuel", file: "aula2_dialogo_carmen_3.mp3" },
  { text: "¡Qué bien! Estoy contenta de conocerte.", voice: "gaby", file: "aula2_dialogo_juliana_4.mp3" },
  { text: "¡Yo también! Estoy segura de que el congreso va a ser muy bueno.", voice: "juan_manuel", file: "aula2_dialogo_carmen_4.mp3" },
  { text: "Hola, soy Juliana Marques. Soy brasileña, de Curitiba. Soy arquitecta. Me dedico a la evaluación de inmuebles. Soy miembro de la UPAV. Estoy aquí para el congreso. Mucho gusto.", voice: "gaby", file: "aula2_order_l2_ordering.mp3" },
];

async function generateAudio(text, voiceId, outputPath) {
  const response = await fetch(`https://api.elevenlabs.io/v1/text-to-speech/${voiceId}`, {
    method: 'POST',
    headers: { 'xi-api-key': API_KEY, 'Content-Type': 'application/json' },
    body: JSON.stringify({
      text,
      model_id: 'eleven_multilingual_v2',
      voice_settings: { stability: 0.5, similarity_boost: 0.75, style: 0.0, use_speaker_boost: true },
    }),
  });
  if (!response.ok) throw new Error(`${response.status} ${await response.text()}`);
  const buffer = Buffer.from(await response.arrayBuffer());
  fs.writeFileSync(outputPath, buffer);
  return buffer.length;
}

async function main() {
  if (!API_KEY) { console.error('ELEVENLABS_API_KEY not set'); process.exit(1); }
  let generated = 0, skipped = 0, errors = 0;
  for (const phrase of PHRASES) {
    const outputPath = path.join(OUTPUT_DIR, phrase.file);
    if (fs.existsSync(outputPath)) { console.log(`SKIP: ${phrase.file}`); skipped++; continue; }
    const voiceId = phrase.voice === 'gaby' ? GABY_ID : JUAN_MANUEL_ID;
    try {
      const size = await generateAudio(phrase.text, voiceId, outputPath);
      console.log(`OK: ${phrase.file} (${(size/1024).toFixed(1)}KB) [${phrase.voice}]`);
      generated++;
      await new Promise(r => setTimeout(r, 500));
    } catch (err) { console.error(`ERROR: ${phrase.file} — ${err.message}`); errors++; }
  }
  console.log(`\nDone! Generated: ${generated}, Skipped: ${skipped}, Errors: ${errors}`);
}
main();
