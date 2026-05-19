const fs = require('fs');
const path = require('path');
const https = require('https');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR_ID = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN_ID = 'BIvP0GN1cAtSRTxNHnWS';
const OUTPUT_DIR = path.join(__dirname, '..', 'public', 'audio', 'maisa-de-oliveira-santos');
const PHRASES = JSON.parse(fs.readFileSync(path.join(__dirname, 'all-missing-audio.json'), 'utf8'));

if (!API_KEY) { console.error('ELEVENLABS_API_KEY not set'); process.exit(1); }

function sanitize(text) {
  return text.toLowerCase().replace(/[áàâã]/g,'a').replace(/[éèê]/g,'e').replace(/[íì]/g,'i')
    .replace(/[óòôõ]/g,'o').replace(/[úù]/g,'u').replace(/ç/g,'c')
    .replace(/[^a-z0-9\s]/g,'_').replace(/\s+/g,'_').replace(/_+/g,'_').replace(/^_|_$/g,'') + '.mp3';
}

function chooseVoice(text) {
  if (!text.includes(' ')) return ARTHUR_ID;
  if (/^(I |I'|My |We |Our |She |Her )/.test(text)) return ELLEN_ID;
  if (text.endsWith('?')) return ARTHUR_ID;
  return text.split('').reduce((a,c) => a + c.charCodeAt(0), 0) % 2 === 0 ? ARTHUR_ID : ELLEN_ID;
}

function gen(text, voiceId) {
  return new Promise((resolve, reject) => {
    const data = JSON.stringify({ text, model_id: 'eleven_monolingual_v1', voice_settings: { stability: 0.5, similarity_boost: 0.75, style: 0, use_speaker_boost: true } });
    const req = https.request({ hostname: 'api.elevenlabs.io', path: `/v1/text-to-speech/${voiceId}`, method: 'POST',
      headers: { 'Accept': 'audio/mpeg', 'Content-Type': 'application/json', 'xi-api-key': API_KEY, 'Content-Length': Buffer.byteLength(data) }
    }, res => {
      if (res.statusCode === 429) { console.log('  Rate limited, waiting 30s...'); setTimeout(() => resolve(gen(text, voiceId)), 30000); return; }
      if (res.statusCode !== 200) { let b=''; res.on('data',c=>b+=c); res.on('end',()=>reject(new Error(`HTTP ${res.statusCode}: ${b.slice(0,100)}`))); return; }
      const chunks = []; res.on('data', c => chunks.push(c)); res.on('end', () => resolve(Buffer.concat(chunks)));
    });
    req.on('error', reject); req.write(data); req.end();
  });
}

async function main() {
  if (!fs.existsSync(OUTPUT_DIR)) fs.mkdirSync(OUTPUT_DIR, { recursive: true });
  let generated = 0, skipped = 0, failed = 0;
  const newEntries = {};

  for (let i = 0; i < PHRASES.length; i++) {
    const text = PHRASES[i];
    const filename = sanitize(text);
    const filepath = path.join(OUTPUT_DIR, filename);
    const relPath = `/audio/maisa-de-oliveira-santos/${filename}`;

    if (fs.existsSync(filepath)) { skipped++; newEntries[text] = relPath; continue; }

    const voiceId = chooseVoice(text);
    try {
      process.stdout.write(`[${i+1}/${PHRASES.length}] ${text.slice(0,55)}...`);
      const buf = await gen(text, voiceId);
      fs.writeFileSync(filepath, buf);
      newEntries[text] = relPath;
      generated++;
      console.log(` OK ${(buf.length/1024).toFixed(0)}KB`);
      await new Promise(r => setTimeout(r, 120));
    } catch (err) {
      console.log(` FAIL`);
      try { await new Promise(r => setTimeout(r, 5000)); const buf = await gen(text, voiceId); fs.writeFileSync(filepath, buf); newEntries[text] = relPath; generated++; console.log('  Retry OK'); }
      catch(e) { failed++; }
    }
  }

  // Update audioMaps in both HTML files
  ['public/professor/maisa-de-oliveira-santos.html', 'public/aluno/maisa-de-oliveira-santos.html'].forEach(file => {
    let html = fs.readFileSync(file, 'utf8');
    const match = html.match(/var audioMap = ({[\s\S]*?});/);
    if (match) {
      const existing = JSON.parse(match[1]);
      const merged = { ...existing, ...newEntries };
      html = html.replace(/var audioMap = {[\s\S]*?};/, 'var audioMap = ' + JSON.stringify(merged) + ';');
      fs.writeFileSync(file, html);
      console.log(`Updated ${file.split('/').pop()}: ${Object.keys(merged).length} entries`);
    }
  });

  console.log(`\n===== DONE =====\nGenerated: ${generated}\nSkipped: ${skipped}\nFailed: ${failed}`);
}
main().catch(console.error);
