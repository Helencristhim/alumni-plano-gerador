#!/usr/bin/env node
/**
 * Gera áudios ElevenLabs para Gabriela Pires (Aulas 1-5)
 * Voz alternada Arthur (vocabulário/drilling) + Ellen (diálogos/frases-modelo)
 * Usage: ELEVENLABS_API_KEY=... node scripts/generate-gabriela-audio.js
 */

const fs = require('fs');
const path = require('path');

const API_URL = 'https://api.elevenlabs.io/v1/text-to-speech';
const VOICES = {
  arthur: 'pNInz6obpgDQGcFmaJgB',  // male, vocab + drilling
  ellen: 'CwhRBWXzGAHq8TQ4Fs17',   // female, dialogues + model phrases
};
const API_KEY = process.env.ELEVENLABS_API_KEY;
const OUTPUT_DIR = path.join(__dirname, '..', 'public', 'audio', 'gabriela-pires');

if (!API_KEY) {
  console.error('Set ELEVENLABS_API_KEY env var');
  process.exit(1);
}
if (!fs.existsSync(OUTPUT_DIR)) fs.mkdirSync(OUTPUT_DIR, { recursive: true });

const audioMap = JSON.parse(fs.readFileSync(path.join(OUTPUT_DIR, 'audioMap.json'), 'utf-8'));
const D = require('./gabriela-data');

// Define qual voz usar para cada frase
function pickVoice(phrase) {
  // Diálogos (linhas com indicação de fala) e frases longas → Ellen (feminina, calma)
  // Vocabulário curto, drilling → Arthur (masculino, clear)
  // Mensagens da Gabriela (eu) → Ellen (faz sentido — ela é menina)
  // Mensagens das Sarahs/recepcionistas → Ellen
  // Para frases neutras, alternar para variedade
  const lower = phrase.toLowerCase();

  // Frases curtas de vocabulário → Arthur
  if (phrase.length < 35 && !phrase.includes('?') && !lower.startsWith('hi') && !lower.startsWith('hello') && !lower.startsWith('good')) {
    return VOICES.arthur;
  }
  // Senão Ellen
  return VOICES.ellen;
}

async function generateAudio(text, filename, voiceId) {
  const filePath = path.join(OUTPUT_DIR, filename);
  if (fs.existsSync(filePath)) return { path: filePath, skipped: true };

  const response = await fetch(`${API_URL}/${voiceId}`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json', 'xi-api-key': API_KEY, 'Accept': 'audio/mpeg' },
    body: JSON.stringify({
      text: text,
      model_id: 'eleven_monolingual_v1',
      voice_settings: { stability: 0.55, similarity_boost: 0.75 },
    }),
  });

  if (!response.ok) {
    const err = await response.text();
    console.error(`  [ERROR] ${filename}: ${response.status} ${err.substring(0, 100)}`);
    return null;
  }

  const buffer = Buffer.from(await response.arrayBuffer());
  fs.writeFileSync(filePath, buffer);
  return { path: filePath, skipped: false, size: buffer.length };
}

async function main() {
  const phrases = Object.keys(audioMap);
  console.log(`Gerando ${phrases.length} áudios para Gabriela Pires...`);
  console.log(`Output: ${OUTPUT_DIR}\n`);

  let success = 0, failed = 0, skipped = 0;
  for (let i = 0; i < phrases.length; i++) {
    const text = phrases[i];
    const filename = path.basename(audioMap[text]);
    const voiceId = pickVoice(text);
    const voiceName = voiceId === VOICES.arthur ? 'Arthur' : 'Ellen';

    process.stdout.write(`[${i+1}/${phrases.length}] (${voiceName}) "${text.substring(0, 55)}..." `);

    const r = await generateAudio(text, filename, voiceId);
    if (r === null) { failed++; console.log('FAIL'); }
    else if (r.skipped) { skipped++; console.log('skip'); }
    else { success++; console.log(`OK ${(r.size/1024).toFixed(1)}KB`); }

    if (i < phrases.length - 1) await new Promise(r => setTimeout(r, 120));
  }

  console.log(`\n--- Done ---`);
  console.log(`Generated: ${success} | Skipped: ${skipped} | Failed: ${failed}`);
}

main().catch(e => { console.error(e); process.exit(1); });
