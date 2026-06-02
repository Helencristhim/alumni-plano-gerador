const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const RILEY_ID = 'hA4zGnmTwX2NQiTRMt7o';

const AUDIOS = [
  // Dienane (all female - Riley)
  { slug: 'dienane-brandao-de-mesquita', file: 'order_l1_s1_ordering.mp3', text: 'I am from Altamira.' },
  { slug: 'dienane-brandao-de-mesquita', file: 'order_l1_s2_ordering.mp3', text: 'She is a manager.' },
  { slug: 'dienane-brandao-de-mesquita', file: 'order_l1_s3_ordering.mp3', text: 'I am 50 years old.' },
  { slug: 'dienane-brandao-de-mesquita', file: 'order_l1_s4_ordering.mp3', text: 'My family is in Belém.' },
  { slug: 'dienane-brandao-de-mesquita', file: 'order_l1_s5_ordering.mp3', text: 'I work in HR.' },
  { slug: 'dienane-brandao-de-mesquita', file: 'order_l2_s1_ordering.mp3', text: 'I wake up at 5 AM.' },
  { slug: 'dienane-brandao-de-mesquita', file: 'order_l2_s2_ordering.mp3', text: 'She has breakfast at 6:30.' },
  { slug: 'dienane-brandao-de-mesquita', file: 'order_l2_s3_ordering.mp3', text: 'He drives to work.' },
  { slug: 'dienane-brandao-de-mesquita', file: 'order_l2_s4_ordering.mp3', text: 'I have lunch at noon.' },
  { slug: 'dienane-brandao-de-mesquita', file: 'order_l2_s5_ordering.mp3', text: 'In the evening I rest.' },
  { slug: 'dienane-brandao-de-mesquita', file: 'order_l3_s1_ordering.mp3', text: 'My mother lives in Belém.' },
  { slug: 'dienane-brandao-de-mesquita', file: 'order_l3_s2_ordering.mp3', text: 'Her husband is a teacher.' },
  { slug: 'dienane-brandao-de-mesquita', file: 'order_l3_s3_ordering.mp3', text: 'We have dinner together.' },
  { slug: 'dienane-brandao-de-mesquita', file: 'order_l3_s4_ordering.mp3', text: 'I have one brother.' },
  { slug: 'dienane-brandao-de-mesquita', file: 'order_l3_s5_ordering.mp3', text: 'My home is in Altamira.' },
  { slug: 'dienane-brandao-de-mesquita', file: 'order_l4_s1_ordering.mp3', text: 'I would like a coffee.' },
  { slug: 'dienane-brandao-de-mesquita', file: 'order_l4_s2_ordering.mp3', text: 'Can I have some water?' },
  { slug: 'dienane-brandao-de-mesquita', file: 'order_l4_s3_ordering.mp3', text: 'Can I see the menu?' },
  { slug: 'dienane-brandao-de-mesquita', file: 'order_l4_s4_ordering.mp3', text: 'I eat bread for breakfast.' },
  { slug: 'dienane-brandao-de-mesquita', file: 'order_l4_s5_ordering.mp3', text: 'Some rice and chicken.' },
  // Zilaudio (female - Riley)
  { slug: 'zilaudio', file: 'order_1_ordering.mp3', text: 'Good evening. Welcome to the Grand Hotel. Thank you. I have a reservation under the name Pereira. Let me check. Yes, a double room for three nights. That is correct. Could I get a room with a view? Of course. Here is your room key. Room 412.' },
  { slug: 'zilaudio', file: 'order_2_ordering.mp3', text: 'Hi! Welcome. How many in your party? Two, please. I would like a table for two. Are you ready to order? I will have the grilled chicken with a side of salad. Could I have the check, please?' },
];

async function generateAudio(text, outputPath) {
  const resp = await fetch(`https://api.elevenlabs.io/v1/text-to-speech/${RILEY_ID}`, {
    method: 'POST',
    headers: { 'xi-api-key': API_KEY, 'Content-Type': 'application/json' },
    body: JSON.stringify({
      text, model_id: 'eleven_monolingual_v1',
      voice_settings: { stability: 0.5, similarity_boost: 0.75, style: 0, use_speaker_boost: true }
    })
  });
  if (!resp.ok) throw new Error(`ElevenLabs ${resp.status}: ${(await resp.text()).substring(0, 200)}`);
  const buffer = Buffer.from(await resp.arrayBuffer());
  fs.writeFileSync(outputPath, buffer);
  console.log(`  Generated: ${path.basename(outputPath)} (${buffer.length} bytes)`);
}

async function main() {
  if (!API_KEY) { console.error('Set ELEVENLABS_API_KEY'); process.exit(1); }
  for (const item of AUDIOS) {
    const dir = path.join(__dirname, '..', 'public', 'audio', item.slug);
    if (!fs.existsSync(dir)) fs.mkdirSync(dir, { recursive: true });
    await generateAudio(item.text, path.join(dir, item.file));
    await new Promise(r => setTimeout(r, 600));
  }
  console.log(`\nDone! ${AUDIOS.length} files generated.`);
}
main().catch(console.error);
