/**
 * Regenerate audio files for phrases containing "Maísa" with correct pronunciation.
 * Uses ElevenLabs API with appropriate voice per phrase:
 *   - Ellen (CwhRBWXzGAHq8TQ4Fs17) for phrases where Maísa speaks
 *   - Arthur (pNInz6obpgDQGcFmaJgB) for descriptions about Maísa
 *
 * New filenames use _v2 suffix to distinguish from old files.
 */

const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const VOICE_ARTHUR = 'pNInz6obpgDQGcFmaJgB';
const VOICE_ELLEN = 'CwhRBWXzGAHq8TQ4Fs17';
const OUTPUT_DIR = path.join(__dirname, '..', 'public', 'audio', 'maisa-de-oliveira-santos');

const PHRASES = [
  {
    text: "My name is Maísa. I work in finance. Nice to meet you.",
    voice: VOICE_ELLEN,
    voiceName: "Ellen",
    filename: "my_name_is_maisa_i_work_in_finance_nice_to_meet_you_v2.mp3"
  },
  {
    text: "Maísa is a financial professional in Sao Paulo.",
    voice: VOICE_ARTHUR,
    voiceName: "Arthur",
    filename: "maisa_is_a_financial_professional_in_sao_paulo_v2.mp3"
  },
  {
    text: "David and Maísa are colleagues at the same company.",
    voice: VOICE_ARTHUR,
    voiceName: "Arthur",
    filename: "david_and_maisa_are_colleagues_v2.mp3"
  },
  {
    text: "Nice to meet you! I am Maísa from the finance department.",
    voice: VOICE_ELLEN,
    voiceName: "Ellen",
    filename: "nice_to_meet_you_i_am_maisa_finance_dept_v2.mp3"
  },
  {
    text: "Hi David! I'm Maísa. I work in finance here in Sao Paulo. Nice to meet you.",
    voice: VOICE_ELLEN,
    voiceName: "Ellen",
    filename: "hi_david_im_maisa_finance_sao_paulo_v2.mp3"
  },
  {
    text: "Nice to meet you! I am Maísa. I am from the finance department. I am responsible for client portfolios.",
    voice: VOICE_ELLEN,
    voiceName: "Ellen",
    filename: "nice_to_meet_you_maisa_finance_portfolios_v2.mp3"
  },
  {
    text: "Maísa works at a financial company.",
    voice: VOICE_ARTHUR,
    voiceName: "Arthur",
    filename: "maisa_works_at_a_financial_company_v2.mp3"
  },
  {
    text: "Maísa is not from Rio de Janeiro. She is from Sao Paulo.",
    voice: VOICE_ARTHUR,
    voiceName: "Arthur",
    filename: "maisa_is_not_from_rio_sao_paulo_v2.mp3"
  },
  {
    text: "Hello! My name is Maísa. I am from the finance department. Nice to meet you! Are you here for the meeting?",
    voice: VOICE_ELLEN,
    voiceName: "Ellen",
    filename: "hello_maisa_finance_dept_meeting_v2.mp3"
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

    // Skip if already generated
    if (fs.existsSync(filepath)) {
      console.log(`[${i + 1}/${PHRASES.length}] SKIP (exists): ${filename}`);
      skipped++;
      continue;
    }

    try {
      process.stdout.write(`[${i + 1}/${PHRASES.length}] ${voiceName}: "${text.substring(0, 50)}..." `);
      const buffer = await generateOne(text, voice);
      fs.writeFileSync(filepath, buffer);
      generated++;
      console.log(`OK (${(buffer.length / 1024).toFixed(1)}KB)`);
      // Rate limit between requests
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

  // Print audioMap entries for copy-paste
  console.log(`\n--- AudioMap entries (copy to HTML) ---`);
  for (const { text, filename } of PHRASES) {
    console.log(`"${text}":"/audio/maisa-de-oliveira-santos/${filename}",`);
  }
}

main();
