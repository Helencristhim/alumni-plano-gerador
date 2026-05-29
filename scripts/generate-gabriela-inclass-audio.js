const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const OUTPUT_DIR = path.join(__dirname, '..', 'public', 'audio', 'gabriela-pires');
const PHRASES = JSON.parse(fs.readFileSync(path.join(__dirname, 'gabriela-missing-inclass.json'), 'utf8'));

const VOICE_ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const VOICE_ELLEN = 'BIvP0GN1cAtSRTxNHnWS';

async function generateOne(text, voiceId, retries = 2) {
  const url = `https://api.elevenlabs.io/v1/text-to-speech/${voiceId}`;
  for (let attempt = 0; attempt <= retries; attempt++) {
    try {
      const res = await fetch(url, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', 'xi-api-key': API_KEY, 'Accept': 'audio/mpeg' },
        body: JSON.stringify({ text, model_id: 'eleven_monolingual_v1', voice_settings: { stability: 0.5, similarity_boost: 0.75 } })
      });
      if (res.status === 429) {
        console.log('  Rate limited, waiting 30s...');
        await new Promise(r => setTimeout(r, 30000));
        continue;
      }
      if (!res.ok) throw new Error(`HTTP ${res.status}: ${await res.text()}`);
      return Buffer.from(await res.arrayBuffer());
    } catch (e) {
      if (attempt === retries) throw e;
      console.log(`  Retry ${attempt + 1}...`);
      await new Promise(r => setTimeout(r, 2000));
    }
  }
}

async function main() {
  if (!API_KEY) { console.error('Set ELEVENLABS_API_KEY env var'); process.exit(1); }
  if (!fs.existsSync(OUTPUT_DIR)) fs.mkdirSync(OUTPUT_DIR, { recursive: true });

  const toGenerate = PHRASES.filter(p => !fs.existsSync(path.join(OUTPUT_DIR, p.file)));
  console.log(`\n=== Gabriela IN CLASS: ${toGenerate.length} audio files to generate ===\n`);

  let success = 0, fail = 0;
  for (let i = 0; i < toGenerate.length; i++) {
    const p = toGenerate[i];
    const voiceId = p.voice === 'ellen' ? VOICE_ELLEN : VOICE_ARTHUR;
    const voiceName = p.voice === 'ellen' ? 'Ellen' : 'Arthur';
    process.stdout.write(`[${i + 1}/${toGenerate.length}] ${voiceName}: "${p.text.substring(0, 60)}..." `);
    try {
      const buf = await generateOne(p.text, voiceId);
      fs.writeFileSync(path.join(OUTPUT_DIR, p.file), buf);
      console.log(`OK (${(buf.length / 1024).toFixed(0)}KB)`);
      success++;
    } catch (e) {
      console.log(`FAIL: ${e.message}`);
      fail++;
    }
    await new Promise(r => setTimeout(r, 200));
  }
  console.log(`\nDone! ${success} generated, ${fail} failed.`);
}

main();
