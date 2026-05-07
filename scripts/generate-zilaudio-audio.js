#!/usr/bin/env node
/**
 * Generate ElevenLabs audio for all phrases in Ziláudio's material
 */
const fs = require('fs');
const path = require('path');
const https = require('https');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const VOICE_ID = 'pNInz6obpgDQGcFmaJgB'; // Arthur
const OUTPUT_DIR = path.join(__dirname, '..', 'public', 'audio', 'zilaudio');

const PHRASES = [
  "I have a reservation under the name Pereira",
  "Call the front desk",
  "Can I get a new room key?",
  "What time is checkout?",
  "Could I have some extra towels, please?",
  "Could I get a room with a view, please?",
  "Could I get a late checkout?",
  "The air conditioning is not working in my room",
  "Could I see the menu?",
  "I'll start with an appetizer",
  "Could I have the check, please?",
  "The standard tip is fifteen to twenty percent",
  "I'll have the grilled chicken with a side of salad",
  "What time does the tour start?",
  "What do you recommend?",
  "How much are the tickets?",
  "I'd like a table for two, please",
  "Good evening. Welcome to the Grand Hotel. Do you have a reservation?",
  "Let me check. Yes, a double room for three nights. Could I see your ID, please?",
  "Thank you. Here is your room key. Room 412. Checkout is at 11 AM.",
  "I'll check availability. The elevator is on your left.",
  "Of course. Here you go.",
  "Could I get a room with a view?",
  "Do you speak Portuguese?",
  "Excuse me, can you help me?",
  "I need help, please.",
  "Where is the bathroom?",
  "Excuse me, the room is too noisy. Could I get a different room, please?",
  "I don't understand. Could you repeat that, please?",
  "What time is checkout?",
  "I have a reservation under the name Pereira.",
  "Could I have some extra towels, please?",
  "The air conditioning is not working in my room.",
  "Could I get a late checkout?",
  "Could I get a room with a view?",
];

// Deduplicate
const unique = [...new Set(PHRASES.map(p => p.replace(/\.$/, '').trim()))];

function slugify(text) {
  return text.toLowerCase().replace(/[^a-z0-9]+/g, '_').replace(/^_|_$/g, '').substring(0, 60);
}

function generateAudio(text) {
  return new Promise((resolve, reject) => {
    const slug = slugify(text);
    const outPath = path.join(OUTPUT_DIR, slug + '.mp3');

    if (fs.existsSync(outPath)) {
      console.log('  SKIP (exists):', slug);
      resolve({ text, path: outPath, slug });
      return;
    }

    const body = JSON.stringify({
      text: text,
      model_id: 'eleven_monolingual_v1',
      voice_settings: { stability: 0.5, similarity_boost: 0.75 }
    });

    const options = {
      hostname: 'api.elevenlabs.io',
      path: '/v1/text-to-speech/' + VOICE_ID,
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'xi-api-key': API_KEY,
        'Accept': 'audio/mpeg'
      }
    };

    const req = https.request(options, (res) => {
      if (res.statusCode !== 200) {
        let err = '';
        res.on('data', d => err += d);
        res.on('end', () => { console.error('  ERROR:', res.statusCode, err.substring(0, 200)); reject(new Error(err)); });
        return;
      }
      const chunks = [];
      res.on('data', chunk => chunks.push(chunk));
      res.on('end', () => {
        const buffer = Buffer.concat(chunks);
        fs.writeFileSync(outPath, buffer);
        console.log('  OK:', slug, '(' + buffer.length + ' bytes)');
        resolve({ text, path: outPath, slug });
      });
    });
    req.on('error', reject);
    req.write(body);
    req.end();
  });
}

async function main() {
  if (!API_KEY) { console.error('ELEVENLABS_API_KEY not set'); process.exit(1); }
  if (!fs.existsSync(OUTPUT_DIR)) fs.mkdirSync(OUTPUT_DIR, { recursive: true });

  console.log('Generating ' + unique.length + ' audio files via ElevenLabs...\n');

  const audioMap = {};
  for (let i = 0; i < unique.length; i++) {
    console.log('[' + (i+1) + '/' + unique.length + '] ' + unique[i]);
    try {
      const result = await generateAudio(unique[i]);
      audioMap[unique[i]] = '/audio/zilaudio/' + result.slug + '.mp3';
      // Rate limit: 2 per second
      if (i < unique.length - 1) await new Promise(r => setTimeout(r, 500));
    } catch(e) {
      console.error('  FAILED:', e.message?.substring(0, 100));
    }
  }

  // Write audioMap JSON
  const mapPath = path.join(OUTPUT_DIR, 'audioMap.json');
  fs.writeFileSync(mapPath, JSON.stringify(audioMap, null, 2));
  console.log('\nDone! AudioMap saved to:', mapPath);
  console.log('Total files:', Object.keys(audioMap).length);
}

main();
