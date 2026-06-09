#!/usr/bin/env node
/**
 * Generate ElevenLabs MP3 for Mark B2 Aulas 2-4 (missing phrases).
 * Reads missing-phrases.json, generates MP3s, outputs updated audioMap snippet.
 *
 * Usage: ELEVENLABS_API_KEY=sk_... node scripts/generate-mark-b2-aulas234-audio.js
 */
const fs = require('fs');
const path = require('path');
const https = require('https');

const API_KEY = process.env.ELEVENLABS_API_KEY;
if (!API_KEY) { console.error('ERROR: set ELEVENLABS_API_KEY'); process.exit(1); }

const VOICES = { arthur: 'sfJopaWaOtauCD3HKX6Q', ellen: 'BIvP0GN1cAtSRTxNHnWS' };
const MODEL_ID = 'eleven_multilingual_v2';
const ROOT = path.join(__dirname, '..');
const SLUG = 'mark-kazuyoshi-seki-omagari';
const OUT_DIR = path.join(ROOT, 'public', 'audio', SLUG);

if (!fs.existsSync(OUT_DIR)) fs.mkdirSync(OUT_DIR, { recursive: true });

function toFilename(text) {
  return text.toLowerCase().replace(/[^a-z0-9 ]/g, '').replace(/ +/g, '_').slice(0, 60);
}

function generateMP3(text, voiceId, outPath) {
  return new Promise((resolve, reject) => {
    if (fs.existsSync(outPath)) { console.log('  SKIP:', path.basename(outPath)); return resolve(); }
    const body = JSON.stringify({
      text, model_id: MODEL_ID,
      voice_settings: { stability: 0.5, similarity_boost: 0.75, style: 0, use_speaker_boost: true }
    });
    const opts = {
      hostname: 'api.elevenlabs.io',
      path: `/v1/text-to-speech/${voiceId}`,
      method: 'POST',
      headers: { 'xi-api-key': API_KEY, 'Content-Type': 'application/json', 'Accept': 'audio/mpeg', 'Content-Length': Buffer.byteLength(body) }
    };
    const req = https.request(opts, res => {
      if (res.statusCode !== 200) {
        let err = ''; res.on('data', d => err += d);
        res.on('end', () => { console.error('  ERR', res.statusCode, err.slice(0,150)); reject(new Error(res.statusCode)); });
        return;
      }
      const chunks = []; res.on('data', c => chunks.push(c));
      res.on('end', () => { fs.writeFileSync(outPath, Buffer.concat(chunks)); console.log('  OK:', path.basename(outPath)); resolve(); });
    });
    req.on('error', reject); req.write(body); req.end();
  });
}

// Also generate listening MP3s for aulas 2-4
const LISTENINGS = [
  { file: 'aula2_listening1.mp3', voice: 'arthur',
    text: "When I think about my personality, I realize that soccer has really shaped who I am. I used to be quite laid-back about everything, but being part of a competitive team has made me more driven. My coach once told me that my strongest trait is my ability to stay calm under pressure. I get along with everyone on the team because I try to be empathetic. I always try to understand how my teammates are feeling, especially when we lose a match. Some people might say I overthink things sometimes, but I think being thoughtful is actually a strength, not a weakness." },
  { file: 'aula2_listening2.mp3', voice: 'ellen',
    text: "I have always looked up to people who are ambitious but also kind. My older sister is someone I truly admire. She is incredibly driven, but she never forgets to be empathetic toward others. She has shaped my personality more than anyone else. Growing up, I was very laid-back, but she taught me that being ambitious does not mean being selfish. The most important trait she taught me is to always try to get along with people, even when you disagree with them." },
  { file: 'aula3_listening1.mp3', voice: 'arthur',
    text: "Family relationships are complicated, but they are also the most important bonds we have. I am very close with my siblings, especially my younger brother. We have a really close-knit relationship. Sure, he gets on my nerves sometimes, but I can always count on him when it matters. I take after my dad in many ways. He is my biggest role model. He taught me that being supportive does not mean agreeing with everything, it means being there even when things are difficult." },
  { file: 'aula3_listening2.mp3', voice: 'ellen',
    text: "I fell out with my best friend last year over something really silly. We did not speak for three months. It was one of the hardest experiences I have ever had. She is not just an acquaintance; she is more like a sibling to me. Eventually, we talked it through and realized that our bond was too strong to let one argument ruin everything. Now I know that you cannot take the people you count on for granted. Supportive relationships require effort from both sides." },
  { file: 'aula4_listening1.mp3', voice: 'arthur',
    text: "I recently realized how much time I spend scrolling through social media. My screen time was averaging six hours a day. Everything I saw was curated by algorithms designed to keep me engaged. The content was filtered to look perfect. I decided to log off for a whole week, and it completely changed my perception of reality. Without social media, I felt more authentic and more connected to the people around me. I think everyone should disconnect from time to time and think about their digital footprint." },
  { file: 'aula4_listening2.mp3', voice: 'ellen',
    text: "Social media has been designed to be addictive. The algorithms decide what is shown to us, and most of the content is filtered and curated to look better than reality. Our digital footprint is tracked by companies, and our screen time keeps increasing every year. But I believe that being authentic online is possible. We just need to be more conscious about what we post and consume. Sometimes logging off is the healthiest thing you can do. Disconnecting from the digital world helps us reconnect with the real one." }
];

async function main() {
  const phrases = JSON.parse(fs.readFileSync('/tmp/missing-phrases.json','utf8'));
  console.log(`\n=== Mark B2 Aulas 2-4 Audio ===`);
  console.log(`Phrases: ${phrases.length}, Listenings: ${LISTENINGS.length}\n`);

  const newEntries = {};
  for (const {phrase, voice} of phrases) {
    const fname = toFilename(phrase) + '.mp3';
    const outPath = path.join(OUT_DIR, fname);
    console.log(`[${voice}] "${phrase.slice(0,60)}..."`);
    try {
      await generateMP3(phrase, VOICES[voice], outPath);
      newEntries[phrase] = `/audio/${SLUG}/${fname}`;
    } catch(e) { console.error('  FAILED:', e.message); }
    await new Promise(r => setTimeout(r, 250));
  }

  for (const l of LISTENINGS) {
    const outPath = path.join(OUT_DIR, l.file);
    console.log(`\n[LISTENING] ${l.file}`);
    try { await generateMP3(l.text, VOICES[l.voice], outPath); } catch(e) { console.error('  FAILED:', e.message); }
    await new Promise(r => setTimeout(r, 400));
  }

  // Merge with existing audioMap
  const existingMap = JSON.parse(fs.readFileSync(path.join(ROOT, '_mark-b2-audiomap.json'),'utf8'));
  const merged = {...existingMap, ...newEntries};
  fs.writeFileSync(path.join(ROOT, '_mark-b2-audiomap.json'), JSON.stringify(merged, null, 2));

  let snippet = 'var audioMap = {\n';
  for (const [k, v] of Object.entries(merged)) {
    snippet += `  "${k.replace(/"/g, '\\"')}": "${v}",\n`;
  }
  snippet += '};\n';
  fs.writeFileSync(path.join(ROOT, '_mark-b2-audiomap-snippet.js'), snippet);

  console.log(`\nTotal audioMap: ${Object.keys(merged).length} entries`);
}

main().catch(e => { console.error(e); process.exit(1); });
