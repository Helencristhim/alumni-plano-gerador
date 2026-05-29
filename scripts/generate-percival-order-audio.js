const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR_ID = 'sfJopaWaOtauCD3HKX6Q';

// Main file (percival-jr.html) has 5 unique orders
// Aula files each have 1 order that matches orders 2-5 from main
// We generate for the main file, then reuse for aula files

const SLUGS = {
  main: 'percival-jr',
  aula2: 'percival-jr-aula2',
  aula3: 'percival-jr-aula3',
  aula4: 'percival-jr-aula4',
  aula5: 'percival-jr-aula5'
};

const ORDER_AUDIOS = [
  {
    file: 'order_l1_self_introduction.mp3',
    slug: SLUGS.main,
    text: 'My name is Percival Junior. I work at EGEA Saneamento in São Paulo. I am responsible for risk and internal audit. I manage a team of specialists. My goal is to speak English fluently.'
  },
  {
    file: 'order_l2_arrival_sequence.mp3',
    slug: SLUGS.main,
    text: 'Percival arrived at JFK Airport. He went through customs and showed his passport. He took a taxi to the hotel and checked in. The receptionist gave him the room key. He took the elevator to the fifteenth floor.'
  },
  {
    file: 'order_l3_professional_intro.mp3',
    slug: SLUGS.main,
    text: 'My name is Percival Junior. I am the Director of Risk and Internal Audit at EGEA Saneamento. I lead a team of ten specialists. I report to the executive board every month. I wear many hats, but I enjoy my work.'
  },
  {
    file: 'order_l4_project_update.mp3',
    slug: SLUGS.main,
    text: 'Right now, I am leading an internal audit. My team is reviewing the internal controls. We are developing an action plan. It depends on the stakeholders. We are working hard to meet the deadline.'
  },
  {
    file: 'order_l5_compliance_update.mp3',
    slug: SLUGS.main,
    text: 'First of all, we identified a compliance issue. Then, we developed an action plan. However, we are facing a delay with the stakeholders. Therefore, compliance became our top priority. Finally, we presented the update to the board.'
  }
];

async function generateAudio(text, outputPath) {
  const resp = await fetch(`https://api.elevenlabs.io/v1/text-to-speech/${ARTHUR_ID}`, {
    method: 'POST',
    headers: { 'xi-api-key': API_KEY, 'Content-Type': 'application/json' },
    body: JSON.stringify({
      text,
      model_id: 'eleven_monolingual_v1',
      voice_settings: { stability: 0.5, similarity_boost: 0.75, style: 0, use_speaker_boost: true }
    })
  });
  if (!resp.ok) throw new Error(`Error ${resp.status}: ${await resp.text()}`);
  const buffer = Buffer.from(await resp.arrayBuffer());
  fs.writeFileSync(outputPath, buffer);
  console.log(`Generated: ${outputPath} (${buffer.length} bytes)`);
}

async function main() {
  if (!API_KEY) { console.error('Set ELEVENLABS_API_KEY'); process.exit(1); }

  // Generate main files
  for (const item of ORDER_AUDIOS) {
    const dir = path.join(__dirname, '..', 'public', 'audio', item.slug);
    if (!fs.existsSync(dir)) fs.mkdirSync(dir, { recursive: true });
    const outPath = path.join(dir, item.file);
    if (fs.existsSync(outPath)) { console.log(`Skipping: ${outPath}`); continue; }
    await generateAudio(item.text, outPath);
    await new Promise(r => setTimeout(r, 1000));
  }

  // Copy to aula directories (aula2=l2, aula3=l3, aula4=l4, aula5=l5)
  const copies = [
    { from: 'order_l2_arrival_sequence.mp3', toSlug: SLUGS.aula2, toFile: 'order_l1_arrival_sequence.mp3' },
    { from: 'order_l3_professional_intro.mp3', toSlug: SLUGS.aula3, toFile: 'order_l1_professional_intro.mp3' },
    { from: 'order_l4_project_update.mp3', toSlug: SLUGS.aula4, toFile: 'order_l1_project_update.mp3' },
    { from: 'order_l5_compliance_update.mp3', toSlug: SLUGS.aula5, toFile: 'order_l1_compliance_update.mp3' },
  ];

  for (const c of copies) {
    const src = path.join(__dirname, '..', 'public', 'audio', SLUGS.main, c.from);
    const destDir = path.join(__dirname, '..', 'public', 'audio', c.toSlug);
    if (!fs.existsSync(destDir)) fs.mkdirSync(destDir, { recursive: true });
    const dest = path.join(destDir, c.toFile);
    if (!fs.existsSync(dest)) {
      fs.copyFileSync(src, dest);
      console.log(`Copied: ${dest}`);
    }
  }

  console.log('\nDone!');
}

main().catch(console.error);
