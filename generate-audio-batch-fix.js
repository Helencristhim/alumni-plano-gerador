const fs = require('fs');
const path = require('path');
const https = require('https');

const ELEVENLABS_API_KEY = process.env.ELEVENLABS_API_KEY;
if (!ELEVENLABS_API_KEY) {
  console.error('ERROR: ELEVENLABS_API_KEY not set');
  process.exit(1);
}

const audios = JSON.parse(fs.readFileSync('/tmp/audios_to_generate.json', 'utf8'));

function generateAudio(text, voiceId, outputPath) {
  return new Promise((resolve, reject) => {
    const data = JSON.stringify({
      text: text,
      model_id: 'eleven_multilingual_v2',
      voice_settings: { stability: 0.5, similarity_boost: 0.75 }
    });

    const options = {
      hostname: 'api.elevenlabs.io',
      path: `/v1/text-to-speech/${voiceId}`,
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'xi-api-key': ELEVENLABS_API_KEY,
        'Accept': 'audio/mpeg'
      }
    };

    const req = https.request(options, (res) => {
      if (res.statusCode === 429) {
        reject(new Error('RATE_LIMIT'));
        return;
      }
      if (res.statusCode !== 200) {
        let body = '';
        res.on('data', c => body += c);
        res.on('end', () => reject(new Error(`HTTP ${res.statusCode}: ${body}`)));
        return;
      }
      const chunks = [];
      res.on('data', c => chunks.push(c));
      res.on('end', () => {
        fs.writeFileSync(outputPath, Buffer.concat(chunks));
        resolve();
      });
    });

    req.on('error', reject);
    req.write(data);
    req.end();
  });
}

async function main() {
  console.log(`\n=== GERANDO ${audios.length} AUDIOS ===\n`);

  let success = 0, skipped = 0, errors = 0;
  let currentSlug = '';

  for (let i = 0; i < audios.length; i++) {
    const a = audios[i];
    const dir = path.join(__dirname, 'public', 'audio', a.slug);
    const outPath = path.join(dir, a.filename);

    // Print slug header
    if (a.slug !== currentSlug) {
      currentSlug = a.slug;
      console.log(`\n--- ${a.slug} ---`);
    }

    // Skip if already exists
    if (fs.existsSync(outPath)) {
      skipped++;
      continue;
    }

    // Ensure directory
    if (!fs.existsSync(dir)) fs.mkdirSync(dir, { recursive: true });

    const shortText = a.text.length > 50 ? a.text.substring(0, 47) + '...' : a.text;
    process.stdout.write(`[${i+1}/${audios.length}] ${a.voiceName}: "${shortText}" `);

    let retries = 0;
    while (retries < 3) {
      try {
        await generateAudio(a.text, a.voice, outPath);
        console.log('OK');
        success++;
        break;
      } catch (err) {
        if (err.message === 'RATE_LIMIT' && retries < 2) {
          retries++;
          const wait = retries * 10;
          process.stdout.write(`(rate limit, waiting ${wait}s) `);
          await new Promise(r => setTimeout(r, wait * 1000));
        } else {
          console.log(`ERRO: ${err.message}`);
          errors++;
          break;
        }
      }
    }

    // Rate limit protection: 300ms between requests
    if (i < audios.length - 1) await new Promise(r => setTimeout(r, 300));
  }

  console.log(`\n=== RESULTADO ===`);
  console.log(`Sucesso: ${success}`);
  console.log(`Ja existiam: ${skipped}`);
  console.log(`Erros: ${errors}`);
  console.log(`Total: ${audios.length}`);
}

main();
