const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR_ID = 'sfJopaWaOtauCD3HKX6Q';
const OUTPUT_DIR = path.join(__dirname, '..', 'public', 'audio', 'carlos-vinicius-vale-bassan');

const ORDER_AUDIOS = [
  {
    file: 'order_l1_ordering.mp3',
    key: '[order-l1]',
    text: 'Good morning, everyone. Let me introduce myself. My name is Carlos Bassan, and I am a Senior Strategy Executive at Accenture. I lead the M&A advisory practice for the Americas region. I currently oversee post-merger integration across the Americas. Over the past decade, our practice has driven over two billion dollars in deal value. I would be happy to discuss our approach in more detail.'
  },
  {
    file: 'order_l2_ordering.mp3',
    key: '[order-l2]',
    text: 'I am Carlos Bassan from Accenture. I specialize in M&A advisory for the Americas. My team handles complex technology-driven transactions. We have a proven track record of delivering results. What sets us apart is our expertise in navigating regulatory challenges. I would love to discuss how we could help.'
  },
  {
    file: 'order_l3_ordering.mp3',
    key: '[order-l3]',
    text: 'Hi, I do not think we have met. I am Carlos from Accenture. What brings you here? That is really interesting. I can relate to that. We actually face a similar challenge in M&A. We should definitely connect. It was great talking to you.'
  }
];

async function generateAudio(text, outputPath) {
  const resp = await fetch(`https://api.elevenlabs.io/v1/text-to-speech/${ARTHUR_ID}`, {
    method: 'POST',
    headers: { 'xi-api-key': API_KEY, 'Content-Type': 'application/json' },
    body: JSON.stringify({
      text: text,
      model_id: 'eleven_monolingual_v1',
      voice_settings: { stability: 0.5, similarity_boost: 0.75, style: 0, use_speaker_boost: true }
    })
  });
  if (!resp.ok) {
    const err = await resp.text();
    throw new Error(`ElevenLabs error: ${resp.status} - ${err}`);
  }
  const buffer = Buffer.from(await resp.arrayBuffer());
  fs.writeFileSync(outputPath, buffer);
  console.log(`Generated: ${path.basename(outputPath)} (${buffer.length} bytes)`);
}

async function main() {
  if (!API_KEY) { console.error('Set ELEVENLABS_API_KEY'); process.exit(1); }
  if (!fs.existsSync(OUTPUT_DIR)) fs.mkdirSync(OUTPUT_DIR, { recursive: true });

  for (const item of ORDER_AUDIOS) {
    const outPath = path.join(OUTPUT_DIR, item.file);
    await generateAudio(item.text, outPath);
    await new Promise(r => setTimeout(r, 500));
  }
  console.log('Done! 3 ordering audio files generated.');
}

main().catch(err => { console.error(err); process.exit(1); });
