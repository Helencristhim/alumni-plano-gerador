const fs = require('fs');
const path = require('path');
const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR_ID = 'sfJopaWaOtauCD3HKX6Q';
const OUTPUT_DIR = path.join(__dirname, '..', 'public', 'audio', 'rafael-gasparelli-lima');

const ORDER_AUDIOS = [
  { file: 'order_l1_self_introduction.mp3', text: "Good morning. My name is Rafael Gasparello Lima. I am a lawyer and director at Grupo Picunha in São Paulo. Our company operates in the iron industry and agriculture. I manage the legal department and serve on the board of directors. It is a pleasure to meet you." },
  { file: 'order_l2_company_profile.mp3', text: "Our company is called Grupo Picunha. We are based in São Paulo, Brazil. The group operates in two industries: iron and agriculture. We have over five hundred employees. We are looking to expand our operations overseas." },
  { file: 'order_l3_daily_routine.mp3', text: "I wake up at 6 a.m. and get ready. I take my son to school. I train jiu-jitsu at the gym. I have lunch before going to the office. I attend meetings and work until the evening." },
  { file: 'order_l4_networking.mp3', text: "Good morning. My name is Rafael Gasparello Lima. Pleased to meet you. I work at Grupo Picunha. Could I give you my business card? Can we arrange a meeting to discuss a partnership? I am looking forward to working with you." },
  { file: 'order_l5_office_tour.mp3', text: "Welcome to Grupo Picunha. This is the reception. The elevator is next to the stairs, on your right. My office is on the fifth floor. There is a conference room next to my office. The cafeteria is on the first floor if you need coffee." }
];

async function generateAudio(text, outputPath) {
  const resp = await fetch(`https://api.elevenlabs.io/v1/text-to-speech/${ARTHUR_ID}`, {
    method: 'POST',
    headers: { 'xi-api-key': API_KEY, 'Content-Type': 'application/json' },
    body: JSON.stringify({ text, model_id: 'eleven_monolingual_v1', voice_settings: { stability: 0.5, similarity_boost: 0.75, style: 0, use_speaker_boost: true } })
  });
  if (!resp.ok) throw new Error(`Error ${resp.status}: ${await resp.text()}`);
  const buffer = Buffer.from(await resp.arrayBuffer());
  fs.writeFileSync(outputPath, buffer);
  console.log(`Generated: ${path.basename(outputPath)} (${buffer.length} bytes)`);
}

async function main() {
  if (!API_KEY) { console.error('Set ELEVENLABS_API_KEY'); process.exit(1); }
  if (!fs.existsSync(OUTPUT_DIR)) fs.mkdirSync(OUTPUT_DIR, { recursive: true });
  for (const item of ORDER_AUDIOS) {
    const outPath = path.join(OUTPUT_DIR, item.file);
    if (fs.existsSync(outPath)) { console.log(`Skipping: ${item.file}`); continue; }
    await generateAudio(item.text, outPath);
    await new Promise(r => setTimeout(r, 1000));
  }
  console.log('\nDone!');
}
main().catch(console.error);
