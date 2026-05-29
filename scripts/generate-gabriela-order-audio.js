const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ELLEN_ID = 'BIvP0GN1cAtSRTxNHnWS'; // Ellen - Calm female voice (Gabriela is a girl)

const OUTPUT_DIR = path.join(__dirname, '..', 'public', 'audio', 'gabriela-pires');

const ORDER_AUDIOS = [
  {
    file: 'order_l1_self_introduction.mp3',
    key: '[order-l1]',
    text: 'Hi! My name is Gabriela Pires. I am 16 years old, and I am from São Paulo, Brazil. I am a student at high school. My favorite hobby is watching series like Gossip Girl. My dream is to travel to France in 2027!'
  },
  {
    file: 'order_l2_hotel_checkin.mp3',
    key: '[order-l2]',
    text: "Good evening! Can I have your name, please? Good evening. My name is Gabriela Pires. Can you spell your last name? Yes — P-I-R-E-S. Perfect. Welcome to Paris, Gabriela!"
  },
  {
    file: 'order_l3_presenting_my_world.mp3',
    key: '[order-l3]',
    text: 'This is my school in São Paulo. That is my best friend Helena over there. These are my classmates in the picture. Those are my favorite books on the shelf. This is my world — I love it.'
  },
  {
    file: 'order_l4_morning_routine.mp3',
    key: '[order-l4]',
    text: "I wake up at seven o'clock. I have breakfast with my family. I take the metro to school. I study and have classes until four. At night, I always watch a series before sleeping."
  },
  {
    file: 'order_l5_fan_talk.mp3',
    key: '[order-l5]',
    text: "My favorite series is Gossip Girl. I am obsessed with Blair Waldorf — she is so smart. I don't like Chuck Bass in season one — he is mean. I also love Friends because it makes me laugh. What about you? What do you like to watch?"
  },
  {
    file: 'order_l21_prediction_speech.mp3',
    key: '[order-l21]',
    text: "In February 2027, I will fly to Paris with my family. I think it will probably be cold and a little rainy. I will visit the Louvre and the Eiffel Tower for sure. I won't speak Portuguese — only English and a little French! I promise I will practice every day until then."
  },
  {
    file: 'order_l22_airport_checkin.mp3',
    key: '[order-l22]',
    text: 'Good morning! May I see your passport, please? Yes, here is my passport. I am flying to Paris. Do you have any luggage to check in? Yes, this one. And this is my carry-on bag. Perfect. Here is your boarding pass. Your gate is B12.'
  },
  {
    file: 'order_l23_immigration.mp3',
    key: '[order-l23]',
    text: "Bonjour. May I see your passport, please? Of course. Here it is. What is the purpose of your visit? I'm here as a tourist for ten days. Where is your accommodation? I am staying at a small hotel in Paris. Welcome to France. Have a great trip!"
  },
  {
    file: 'order_l24_self_reflection.mp3',
    key: '[order-l24]',
    text: "Looking back at Aula 1, I was very nervous. At first, I couldn't even say my name in English. Now I can introduce myself with confidence. I am still working on listening to fast English. My next goal is to survive Paris in English in 2027."
  }
];

async function generateAudio(text, outputPath) {
  const resp = await fetch(`https://api.elevenlabs.io/v1/text-to-speech/${ELLEN_ID}`, {
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
    if (fs.existsSync(outPath)) { console.log(`Skipping (exists): ${item.file}`); continue; }
    await generateAudio(item.text, outPath);
    await new Promise(r => setTimeout(r, 1000));
  }
  console.log('\nDone! All order audios generated.');
}

main().catch(console.error);
