const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const GABY_ID = '5vkxOzoz40FrElmLP4P7';       // Female, Peruvian, conversational
const JUAN_MANUEL_ID = 'rBqbBncz61jpuaOTI1GW'; // Male, Peruvian, conversational

const OUTPUT_DIR = path.join(__dirname, '..', 'public', 'audio', 'juliana-marques');

// Juliana = female → Gaby for protagonist voice
// María = female → Gaby (different character but same gender)
// Male characters / alternation → Juan Manuel
// Rule: 1-2 words = Gaby (student gender), 3+ words general = alternate

const PHRASES = [
  // Vocab words (Gaby — student gender for short words)
  { text: "Hola", voice: "gaby", file: "hola.mp3" },
  { text: "Buenos días", voice: "gaby", file: "buenos_dias.mp3" },
  { text: "Mucho gusto", voice: "gaby", file: "mucho_gusto.mp3" },
  { text: "Me llamo", voice: "gaby", file: "me_llamo.mp3" },
  { text: "Soy arquitecta", voice: "gaby", file: "soy_arquitecta.mp3" },
  { text: "Trabajo con", voice: "gaby", file: "trabajo_con.mp3" },
  { text: "Evaluación", voice: "gaby", file: "evaluacion.mp3" },
  { text: "¿De dónde eres?", voice: "juan_manuel", file: "de_donde_eres.mp3" },

  // Vocab example sentences (alternate Gaby/Juan Manuel)
  { text: "Hola, buenos días.", voice: "gaby", file: "hola_buenos_dias.mp3" },
  { text: "Mucho gusto, me llamo Juliana.", voice: "gaby", file: "mucho_gusto_me_llamo_juliana.mp3" },
  { text: "Soy arquitecta. Trabajo con evaluación de inmuebles.", voice: "gaby", file: "soy_arquitecta_trabajo_con_evaluacion.mp3" },
  { text: "Soy de Brasil.", voice: "gaby", file: "soy_de_brasil.mp3" },
  { text: "Vivo en Curitiba.", voice: "juan_manuel", file: "vivo_en_curitiba.mp3" },
  { text: "Trabajo con evaluación de inmuebles.", voice: "juan_manuel", file: "trabajo_con_evaluacion_de_inmuebles.mp3" },

  // Presentation sentences (Gaby = Juliana's voice as protagonist)
  { text: "Me llamo Juliana Marques.", voice: "gaby", file: "me_llamo_juliana_marques.mp3" },
  { text: "Soy arquitecta y evaluadora.", voice: "gaby", file: "soy_arquitecta_y_evaluadora.mp3" },
  { text: "Soy miembro de la UPAV.", voice: "gaby", file: "soy_miembro_de_la_upav.mp3" },

  // Grammar examples (alternate)
  { text: "Yo soy Juliana.", voice: "gaby", file: "yo_soy_juliana.mp3" },
  { text: "Tú eres la coordinadora.", voice: "juan_manuel", file: "tu_eres_la_coordinadora.mp3" },
  { text: "Ella es de México.", voice: "gaby", file: "ella_es_de_mexico.mp3" },
  { text: "Nosotros somos evaluadores.", voice: "juan_manuel", file: "nosotros_somos_evaluadores.mp3" },
  { text: "Ellos son arquitectos.", voice: "gaby", file: "ellos_son_arquitectos.mp3" },

  // Speech card phrases (Gaby = student protagonist)
  { text: "Hola, me llamo Juliana. Soy de Brasil.", voice: "gaby", file: "hola_me_llamo_juliana_soy_de_brasil.mp3" },
  { text: "Soy arquitecta. Trabajo con evaluación.", voice: "gaby", file: "soy_arquitecta_trabajo_con_evaluacion_short.mp3" },
  { text: "Mucho gusto. Soy miembro de la UPAV.", voice: "gaby", file: "mucho_gusto_soy_miembro_upav.mp3" },

  // Listening (María's introduction — Gaby as María, slightly different delivery)
  { text: "Hola, me llamo María. Soy la coordinadora del grupo de mujeres de la UPAV. Soy de México. Soy arquitecta y evaluadora. Mucho gusto.", voice: "gaby", file: "listening1_maria_intro.mp3" },

  // Dialogue — Juliana lines (Gaby = student)
  { text: "Hola María, mucho gusto. Me llamo Juliana.", voice: "gaby", file: "dialogo_juliana_1.mp3" },
  { text: "Soy de Brasil. Vivo en Curitiba.", voice: "gaby", file: "dialogo_juliana_2.mp3" },
  { text: "Soy arquitecta. Trabajo con evaluación de inmuebles.", voice: "gaby", file: "dialogo_juliana_3.mp3" },
  { text: "Gracias, María. Mucho gusto.", voice: "gaby", file: "dialogo_juliana_4.mp3" },

  // Dialogue — María lines (Juan Manuel as different voice for contrast)
  // NOTE: Using Juan Manuel for María's lines to create contrast with Juliana's Gaby voice
  // Even though María is female, we need auditory distinction between the two characters
  { text: "¡Hola Juliana! Bienvenida al grupo. ¿De dónde eres?", voice: "juan_manuel", file: "dialogo_maria_1.mp3" },
  { text: "¡Qué bien! ¿Y a qué te dedicas?", voice: "juan_manuel", file: "dialogo_maria_2.mp3" },
  { text: "¡Excelente! Yo también soy evaluadora. ¡Bienvenida!", voice: "juan_manuel", file: "dialogo_maria_3.mp3" },
  { text: "El gusto es mío, Juliana.", voice: "juan_manuel", file: "dialogo_maria_4.mp3" },

  // Survival phrases (Gaby = student protagonist)
  { text: "¿Puede repetir, por favor?", voice: "gaby", file: "puede_repetir.mp3" },
  { text: "¿Cómo se dice esto en español?", voice: "gaby", file: "como_se_dice.mp3" },
  { text: "No entiendo.", voice: "gaby", file: "no_entiendo.mp3" },
  { text: "¿Puede hablar más despacio?", voice: "gaby", file: "puede_hablar_despacio.mp3" },
  { text: "¡Gracias!", voice: "gaby", file: "gracias.mp3" },

  // Ordering audio (full sequence)
  { text: "Hola, buenos días. Me llamo Juliana Marques. Soy de Brasil. Soy arquitecta. Trabajo con evaluación de inmuebles. Mucho gusto.", voice: "gaby", file: "order_l1_ordering.mp3" },
];

async function generateAudio(text, voiceId, outputPath) {
  const response = await fetch(`https://api.elevenlabs.io/v1/text-to-speech/${voiceId}`, {
    method: 'POST',
    headers: {
      'xi-api-key': API_KEY,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      text,
      model_id: 'eleven_multilingual_v2',
      voice_settings: {
        stability: 0.5,
        similarity_boost: 0.75,
        style: 0.0,
        use_speaker_boost: true,
      },
    }),
  });

  if (!response.ok) {
    const err = await response.text();
    throw new Error(`ElevenLabs error for "${text.substring(0, 40)}...": ${response.status} ${err}`);
  }

  const buffer = Buffer.from(await response.arrayBuffer());
  fs.writeFileSync(outputPath, buffer);
  return buffer.length;
}

async function main() {
  if (!API_KEY) {
    console.error('ELEVENLABS_API_KEY not set');
    process.exit(1);
  }

  if (!fs.existsSync(OUTPUT_DIR)) fs.mkdirSync(OUTPUT_DIR, { recursive: true });

  let generated = 0, skipped = 0, errors = 0;

  for (const phrase of PHRASES) {
    const outputPath = path.join(OUTPUT_DIR, phrase.file);

    if (fs.existsSync(outputPath)) {
      console.log(`SKIP (exists): ${phrase.file}`);
      skipped++;
      continue;
    }

    const voiceId = phrase.voice === 'gaby' ? GABY_ID : JUAN_MANUEL_ID;

    try {
      const size = await generateAudio(phrase.text, voiceId, outputPath);
      console.log(`OK: ${phrase.file} (${(size / 1024).toFixed(1)}KB) [${phrase.voice}]`);
      generated++;
      // Rate limiting
      await new Promise(r => setTimeout(r, 500));
    } catch (err) {
      console.error(`ERROR: ${phrase.file} — ${err.message}`);
      errors++;
    }
  }

  console.log(`\nDone! Generated: ${generated}, Skipped: ${skipped}, Errors: ${errors}`);
  console.log(`Total files in ${OUTPUT_DIR}: ${fs.readdirSync(OUTPUT_DIR).filter(f => f.endsWith('.mp3')).length}`);
}

main();
