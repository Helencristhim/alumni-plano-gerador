// Regenera os 8 áudios da Juliana que diziam "Curitiba" -> agora "São Paulo".
// Vozes preservadas do material original. Modelo eleven_multilingual_v2.
const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const GABY = '5vkxOzoz40FrElmLP4P7';        // Female, Peruvian (voz da Juliana / Maria)
const JUAN = 'rBqbBncz61jpuaOTI1GW';        // Male, Peruvian
const DIR = path.join(__dirname, '..', 'public', 'audio', 'juliana-marques');

const PHRASES = [
  { file: 'aula5_listening1_reunion.mp3', voice: GABY,
    text: 'Hola a todas. Bienvenidas a la primera reunión virtual del grupo de mujeres evaluadoras. Soy María, la coordinadora. Hoy tenemos tres participantes: Juliana de Brasil, Carmen de Chile y Pilar de Argentina. Todas somos evaluadoras de inmuebles. Juliana trabaja en São Paulo. Normalmente evalúa dos inmuebles cada semana. Carmen tiene su oficina en Santiago. Pilar trabaja en Buenos Aires. El mercado inmobiliario en Latinoamérica es muy interesante. Gracias a todas por participar.' },
  { file: 'aula5_juliana_presentacion1.mp3', voice: JUAN,
    text: 'Hola, mucho gusto. Me llamo Juliana Marques. Soy brasileña, de São Paulo.' },
  { file: 'aula4_dialogo_juliana_1.mp3', voice: GABY,
    text: '¡Sí, es muy grande! Mi oficina en São Paulo es más pequeña.' },
  { file: 'aula2_dialogo_juliana_2.mp3', voice: GABY,
    text: 'Soy brasileña, de São Paulo. ¿Y tú?' },
  { file: 'aula2_soy_brasilena_de_sao_paulo.mp3', voice: GABY,
    text: 'Soy brasileña, de São Paulo.' },
  { file: 'dialogo_juliana_2.mp3', voice: GABY,
    text: 'Soy de Brasil. Vivo en São Paulo.' },
  { file: 'vivo_en_sao_paulo.mp3', voice: JUAN,
    text: 'Vivo en São Paulo.' },
  { file: 'aula3_listening_carmen_dia.mp3', voice: JUAN,
    text: 'Yo trabajo en São Paulo. Normalmente llego a la oficina por la mañana. Primero reviso los documentos del día. Después visito los inmuebles. Cada semana evalúo dos o tres propiedades. Por la tarde preparo los informes.' },
];

async function gen(text, voiceId, out) {
  const res = await fetch(`https://api.elevenlabs.io/v1/text-to-speech/${voiceId}`, {
    method: 'POST',
    headers: { 'xi-api-key': API_KEY, 'Content-Type': 'application/json' },
    body: JSON.stringify({
      text,
      model_id: 'eleven_multilingual_v2',
      voice_settings: { stability: 0.5, similarity_boost: 0.75, style: 0.0, use_speaker_boost: true },
    }),
  });
  if (!res.ok) throw new Error(`${res.status} ${await res.text()}`);
  const buf = Buffer.from(await res.arrayBuffer());
  fs.writeFileSync(out, buf);
  return buf.length;
}

(async () => {
  if (!API_KEY) { console.error('ELEVENLABS_API_KEY not set'); process.exit(1); }
  for (const p of PHRASES) {
    try {
      const sz = await gen(p.text, p.voice, path.join(DIR, p.file));
      console.log(`OK: ${p.file} (${(sz/1024).toFixed(1)}KB)`);
      await new Promise(r => setTimeout(r, 500));
    } catch (e) { console.error(`ERR: ${p.file} -> ${e.message}`); process.exitCode = 1; }
  }
})();
