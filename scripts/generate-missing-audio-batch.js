#!/usr/bin/env node
const fs = require('fs'), path = require('path'), https = require('https');
const API_KEY = process.env.ELEVENLABS_API_KEY;
if (!API_KEY) { console.error('ERROR: Set ELEVENLABS_API_KEY'); process.exit(1); }

const RILEY = 'hA4zGnmTwX2NQiTRMt7o';
const ASH = 'VU16byTywsWv5JpI8rbc';
const BASE = path.join(__dirname, '..', 'public', 'audio');

const PHRASES = [
  // === Natalie Viegas (female → Riley) — Aula 6 Error Correction ===
  ["The report was draft last week.", "natalie-viegas/aula6_error_draft.mp3", RILEY],
  ["Two recommendations have been make.", "natalie-viegas/aula6_error_make.mp3", RILEY],
  ["The findings were present to the board.", "natalie-viegas/aula6_error_present.mp3", RILEY],
  ["The changes will implement in Q4.", "natalie-viegas/aula6_error_implement.mp3", RILEY],
  ["The findings were analyzed. The changes will be implemented in Q4.", "natalie-viegas/aula6_error_combo.mp3", RILEY],

  // === Diogo Leal (male → Ash) ===
  ["What do you do?", "diogo-leal/what_do_you_do.mp3", ASH],
  ["The networking at this conference is great.", "diogo-leal/the_networking_at_this_conference.mp3", ASH],

  // === Nilo Patucci (male → Ash) ===
  ["Our headquarters is in Sao Paulo.", "nilo-mesquita-patucci/our_headquarters_is_in_sao_paulo.mp3", ASH],

  // === Roberto Rezende (male → Ash) ===
  ["Our projection for Q3 is more optimistic than Q2.", "roberto-rezende/aula7_projection_q3_optimistic.mp3", ASH],
];

function gen(text, file, voice) {
  return new Promise((resolve, reject) => {
    const fp = path.join(BASE, file);
    if (fs.existsSync(fp) && fs.statSync(fp).size > 1000) {
      console.log('  SKIP:', file);
      return resolve();
    }
    console.log('  GEN:', text.substring(0, 60) + (text.length > 60 ? '...' : ''), '→', file);
    const body = JSON.stringify({
      text: text,
      model_id: 'eleven_turbo_v2_5',
      voice_settings: { stability: 0.5, similarity_boost: 0.75 }
    });
    const opts = {
      hostname: 'api.elevenlabs.io',
      path: `/v1/text-to-speech/${voice}`,
      method: 'POST',
      headers: {
        'xi-api-key': API_KEY,
        'Content-Type': 'application/json',
        'Accept': 'audio/mpeg',
        'Content-Length': Buffer.byteLength(body)
      }
    };
    const req = https.request(opts, res => {
      if (res.statusCode !== 200) {
        let err = '';
        res.on('data', d => err += d);
        res.on('end', () => {
          console.error('  ERR', res.statusCode, file, err.substring(0, 200));
          reject(new Error('HTTP ' + res.statusCode));
        });
        return;
      }
      const chunks = [];
      res.on('data', d => chunks.push(d));
      res.on('end', () => {
        const buf = Buffer.concat(chunks);
        fs.writeFileSync(fp, buf);
        console.log('  OK:', file, buf.length, 'bytes');
        resolve();
      });
    });
    req.on('error', reject);
    req.write(body);
    req.end();
  });
}

async function main() {
  console.log(`Generating ${PHRASES.length} missing audio files for 4 students...\n`);
  let ok = 0, err = 0;
  for (let i = 0; i < PHRASES.length; i++) {
    try {
      await gen(PHRASES[i][0], PHRASES[i][1], PHRASES[i][2]);
      ok++;
      if (i < PHRASES.length - 1) await new Promise(r => setTimeout(r, 200));
    } catch (e) {
      err++;
      console.error('  FAILED:', PHRASES[i][1], e.message);
    }
  }
  console.log(`\nDone: ${ok} OK, ${err} errors`);
}

main().catch(console.error);
