const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const BASE = path.join(__dirname, '..', 'public', 'audio');

const PHRASES = [
  // Juliana Marques (Spanish - use Ellen for female student)
  { text: "Ella está en Madrid.", file: "juliana-marques/aula2_ella_esta_en_madrid.mp3", voice: ELLEN },
  { text: "Ellos evalúan las propiedades.", file: "juliana-marques/aula3_ellos_evaluan_propiedades.mp3", voice: ARTHUR },
  { text: "Juliana revisa los documentos.", file: "juliana-marques/aula3_juliana_revisa_documentos.mp3", voice: ELLEN },
  { text: "Nosotras preparamos los informes.", file: "juliana-marques/aula3_nosotras_preparamos_informes.mp3", voice: ELLEN },
  { text: "Tú visitas inmuebles cada semana.", file: "juliana-marques/aula3_tu_visitas_inmuebles.mp3", voice: ARTHUR },
  { text: "Mi hermana está embarazada, va a tener un bebé.", file: "juliana-marques/aula4_hermana_embarazada_bebe.mp3", voice: ELLEN },
  { text: "El informe es muy largo, tiene 50 páginas.", file: "juliana-marques/aula4_informe_largo_50_paginas.mp3", voice: ARTHUR },
  { text: "Voy a colgar. Hasta pronto.", file: "juliana-marques/aula7_voy_a_colgar_hasta_pronto.mp3", voice: ELLEN },

  // Elaine Mieko Pinho (alternate Arthur/Ellen)
  { text: "Could you drop off me at the main entrance, please?", file: "elaine-mieko-pinho/could_you_drop_off_me_at_the_main_entrance_please.mp3", voice: ELLEN },
  { text: "Could you take me to the Hilton Hotel, please? Elaine asks the driver.", file: "elaine-mieko-pinho/could_you_take_me_elaine_asks_the_driver.mp3", voice: ELLEN },
  { text: "Elaine pays and asks for a receipt.", file: "elaine-mieko-pinho/elaine_pays_and_asks_for_a_receipt.mp3", voice: ARTHUR },
  { text: "The traffic is heavy, but Miguel knows the way.", file: "elaine-mieko-pinho/the_traffic_is_heavy_but_miguel_knows_the_way.mp3", voice: ELLEN },

  // Milton Sayegh (male student, alternate)
  { text: "Milton travels overseas at least four times a year.", file: "milton-sayegh/milton_travels_overseas_at_least_four_times_a_year.mp3", voice: ARTHUR },
  { text: "Our company is expanding operations in the U.S.", file: "milton-sayegh/our_company_is_expanding_operations_in_the_us.mp3", voice: ELLEN },
  { text: "They are scheduling a follow-up meeting.", file: "milton-sayegh/they_are_scheduling_a_follow_up_meeting.mp3", voice: ARTHUR },

  // Sandra Hayasaki
  { text: "Look at the clock. What time is it?", file: "sandra-hayasaki/aula3_look_at_the_clock_what_time_is_it.mp3", voice: ARTHUR },
  { text: "One hour is sixty minutes.", file: "sandra-hayasaki/aula3_one_hour_is_sixty_minutes.mp3", voice: ELLEN },

  // Gabriela Pires
  { text: "I hate Mondays — they are so boring.", file: "gabriela-pires/i_hate_mondays_they_are_so_boring.mp3", voice: ELLEN },

  // Luiz Bressane
  { text: "Habeas corpus, which is guaranteed by the constitution, protects individuals from unlawful detention.", file: "luiz-bressane/aula3_habeas_corpus_which_is_guaranteed.mp3", voice: ARTHUR },

  // Rafael de Andrade Brandão
  { text: "We always have a meeting on Monday mornings to check our schedule.", file: "rafael-de-andrade-brandao/aula2_we_always_have_a_meeting_on_monday_to_check.mp3", voice: ELLEN },

  // Simone Quiles
  { text: "Simone works at Telefonica in the legal department.", file: "simone-quiles-de-santana-marques/fillin_simone_works_at_telefonica_legal.mp3", voice: ELLEN },
];

async function generate(p) {
  const filepath = path.join(BASE, p.file);
  if (fs.existsSync(filepath)) { console.log('SKIP ' + p.file); return; }
  console.log('GEN: ' + p.text.substring(0, 50) + '... → ' + p.file);
  const res = await fetch('https://api.elevenlabs.io/v1/text-to-speech/' + p.voice, {
    method: 'POST',
    headers: { 'xi-api-key': API_KEY, 'Content-Type': 'application/json' },
    body: JSON.stringify({ text: p.text, model_id: 'eleven_turbo_v2_5', voice_settings: { stability: 0.5, similarity_boost: 0.75 } })
  });
  if (!res.ok) { console.error('FAIL ' + p.file + ': ' + res.status); return; }
  const buf = Buffer.from(await res.arrayBuffer());
  fs.writeFileSync(filepath, buf);
  console.log('OK ' + p.file + ' (' + buf.length + ' bytes)');
}

(async () => {
  for (const p of PHRASES) await generate(p);
  console.log('\nDone! Generated ' + PHRASES.length + ' audio files.');
})();
