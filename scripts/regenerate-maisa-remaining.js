/**
 * Regenerate 2 remaining audio files with wrong "Maísa" pronunciation.
 * Uses ElevenLabs API:
 *   - Ellen (CwhRBWXzGAHq8TQ4Fs17) for phrases where Maísa speaks
 *   - Arthur (pNInz6obpgDQGcFmaJgB) for descriptions about Maísa
 */

const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const VOICE_ARTHUR = 'pNInz6obpgDQGcFmaJgB';
const VOICE_ELLEN = 'CwhRBWXzGAHq8TQ4Fs17';
const OUTPUT_DIR = path.join(__dirname, '..', 'public', 'audio', 'maisa-de-oliveira-santos');

const PHRASES = [
  {
    text: "My name is Maísa. I work in finance.",
    voice: VOICE_ELLEN,
    voiceName: "Ellen",
    filename: "my_name_is_maisa_i_work_in_finance_v2.mp3"
  },
  {
    text: "Maísa manages client portfolios at her firm.",
    voice: VOICE_ARTHUR,
    voiceName: "Arthur",
    filename: "maisa_manages_portfolios_v2.mp3"
  }
];

async function generateOne(text, voiceId, retries = 2) {
  const url = `https://api.elevenlabs.io/v1/text-to-speech/${voiceId}`;
  const body = JSON.stringify({
    text,
    model_id: 'eleven_monolingual_v1',
    voice_settings: { stability: 0.5, similarity_boost: 0.75 }
  });

  for (let attempt = 0; attempt <= retries; attempt++) {
    try {
      const res = await fetch(url, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'xi-api-key': API_KEY,
          'Accept': 'audio/mpeg'
        },
        body
      });

      if (res.status === 429) {
        console.log('  Rate limited, waiting 30s...');
        await new Promise(r => setTimeout(r, 30000));
        continue;
      }

      if (!res.ok) {
        const err = await res.text();
        throw new Error(`HTTP ${res.status}: ${err}`);
      }

      const buffer = Buffer.from(await res.arrayBuffer());
      return buffer;
    } catch (e) {
      if (attempt === retries) throw e;
      console.log(`  Retry ${attempt + 1}...`);
      await new Promise(r => setTimeout(r, 5000));
    }
  }
}

async function main() {
  if (!API_KEY) {
    console.error('ERROR: ELEVENLABS_API_KEY not set in environment.');
    process.exit(1);
  }

  if (!fs.existsSync(OUTPUT_DIR)) {
    fs.mkdirSync(OUTPUT_DIR, { recursive: true });
  }

  console.log(`\nRegenerating ${PHRASES.length} phrases with correct Maísa pronunciation...\n`);
  console.log(`Output directory: ${OUTPUT_DIR}\n`);

  let generated = 0;
  let skipped = 0;
  let failed = 0;

  for (let i = 0; i < PHRASES.length; i++) {
    const { text, voice, voiceName, filename } = PHRASES[i];
    const filepath = path.join(OUTPUT_DIR, filename);

    try {
      process.stdout.write(`[${i + 1}/${PHRASES.length}] ${voiceName}: "${text.substring(0, 60)}..." `);
      const buffer = await generateOne(text, voice);
      fs.writeFileSync(filepath, buffer);
      generated++;
      console.log(`OK (${(buffer.length / 1024).toFixed(1)}KB)`);
      await new Promise(r => setTimeout(r, 300));
    } catch (e) {
      console.log(`FAILED: ${e.message}`);
      failed++;
    }
  }

  console.log(`\n--- Results ---`);
  console.log(`Generated: ${generated}`);
  console.log(`Skipped:   ${skipped}`);
  console.log(`Failed:    ${failed}`);
  console.log(`Total:     ${PHRASES.length}`);
}

main();
