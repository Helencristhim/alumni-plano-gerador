const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR_ID = 'sfJopaWaOtauCD3HKX6Q'; // Arthur - Casual Conversational American Male

const OUTPUT_DIR = path.join(__dirname, '..', 'public', 'audio', 'roberto-pires');

const ORDER_AUDIOS = [
  {
    file: 'order_l1_self_introduction.mp3',
    text: 'Hi, my name is Roberto Pires. I am from São Paulo, Brazil. I am a businessman. In August, I am going to Barcelona and Paris. I want to learn English for my trip.'
  },
  {
    file: 'order_l2_conversation.mp3',
    text: 'Excuse me, can you help me? Of course! What do you need? I do not understand this sign. Can you repeat that slowly, please? Thank you very much!'
  },
  {
    file: 'order_l3_market_transaction.mp3',
    text: 'How much is this scarf? It is twenty-five euros. That is too expensive. I will think about it. This one is only five euros. I will take it! Can I have the receipt, please?'
  },
  {
    file: 'order_l4_airport_journey.mp3',
    text: "Roberto arrived at the airport. He checked in and showed his passport. He walked through security. He looked at the departure board. He waited at gate B7 for his flight."
  },
  {
    file: 'order_l5_baggage_claim.mp3',
    text: "Roberto's flight arrived in Barcelona. He went to baggage claim. His bag was missing. He reported the problem at the airline desk. The airline found his bag and brought it to the hotel."
  },
  {
    file: 'order_l6_hotel_checkin.mp3',
    text: "Roberto walks into the hotel lobby. He says: I have a reservation under the name Pires. The receptionist checks the computer. She gives him the room key. He takes the elevator to the fifth floor."
  }
];

async function generateAudio(text, outputPath) {
  const resp = await fetch(`https://api.elevenlabs.io/v1/text-to-speech/${ARTHUR_ID}`, {
    method: 'POST',
    headers: {
      'xi-api-key': API_KEY,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      text: text,
      model_id: 'eleven_monolingual_v1',
      voice_settings: { stability: 0.5, similarity_boost: 0.75, style: 0, use_speaker_boost: true }
    })
  });
  if (!resp.ok) {
    const err = await resp.text();
    throw new Error(`ElevenLabs error for ${path.basename(outputPath)}: ${resp.status} — ${err}`);
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
    if (fs.existsSync(outPath)) {
      console.log(`Skipping (exists): ${item.file}`);
      continue;
    }
    await generateAudio(item.text, outPath);
    await new Promise(r => setTimeout(r, 1000));
  }
  console.log('\nDone! All order audios generated.');
}

main().catch(console.error);
