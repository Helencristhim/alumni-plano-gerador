const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ELLEN_ID = 'BIvP0GN1cAtSRTxNHnWS'; // Ellen - Calm female voice with international accent

const OUTPUT_DIR = path.join(__dirname, '..', 'public', 'audio', 'elaine-mieko-pinho');

// Each ORDER exercise: all phrases in correct order, joined as a single monologue
const ORDER_AUDIOS = [
  {
    file: 'order_l1_self_introduction.mp3',
    text: 'My name is Elaine. I am from Brazil. I am a lawyer and I manage a company. I usually travel with my family. I feel nervous when I speak English abroad. I want to travel alone and feel confident.'
  },
  {
    file: 'order_l2_airport_steps.mp3',
    text: 'You arrive at the airport with your luggage. You go to the check-in counter and show your passport. You receive your boarding pass and check in your luggage. You go through security and find your gate. You hear the boarding announcement and get on the plane.'
  },
  {
    file: 'order_l3_on_the_plane.mp3',
    text: 'Find your seat and put your bag in the overhead bin. Sit down and fasten your seatbelt. Open your tray table when the crew says it is safe. Ask the flight attendant for food or drinks. Close your tray table and fasten your seatbelt for landing.'
  },
  {
    file: 'order_l4_immigration.mp3',
    text: 'You arrive at immigration and wait in line. The officer calls you and asks for your passport. You answer the officer\'s questions about your visit. You go through customs and walk through the green lane. You pick up your luggage and exit the airport.'
  },
  {
    file: 'order_l5_taxi_ride.mp3',
    text: 'You exit the airport and see taxis outside. You tell the driver your destination. You watch the meter during the ride. You arrive and ask the driver to drop you off. You pay the fare and ask for a receipt.'
  }
];

async function generateAudio(text, outputPath) {
  const resp = await fetch(`https://api.elevenlabs.io/v1/text-to-speech/${ELLEN_ID}`, {
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
    // Small delay between requests
    await new Promise(r => setTimeout(r, 1000));
  }
  console.log('\nDone! All order audios generated.');
}

main().catch(console.error);
