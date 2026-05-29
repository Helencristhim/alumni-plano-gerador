const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const DIR = path.join(__dirname, '..', 'public', 'audio', 'patricia-ruffo');
const PREFIX = 'aula3_';

const PHRASES = [
  // Vocab words (Arthur — single words)
  { text: "Hypothesis", voice: ARTHUR },
  { text: "Methodology", voice: ARTHUR },
  { text: "Correlation", voice: ARTHUR },
  { text: "Preliminary", voice: ARTHUR },
  { text: "Replicate", voice: ARTHUR },
  { text: "Variable", voice: ARTHUR },
  { text: "Sample", voice: ARTHUR },
  { text: "Bias", voice: ARTHUR },
  { text: "Peer-reviewed", voice: ARTHUR },
  { text: "Implication", voice: ARTHUR },

  // Vocab example sentences (alternate Ellen/Arthur)
  { text: "Our hypothesis is that functional ingredients reduce glycemic response.", voice: ELLEN },
  { text: "The methodology of this study was peer-reviewed.", voice: ARTHUR },
  { text: "There is a strong correlation between diet and glycemic control.", voice: ELLEN },
  { text: "The preliminary results are very promising.", voice: ARTHUR },
  { text: "We need to replicate this study with a larger sample.", voice: ELLEN },
  { text: "The main variable in our experiment was the dosage.", voice: ARTHUR },
  { text: "Our sample included 120 participants from three countries.", voice: ELLEN },
  { text: "We must eliminate bias from our research design.", voice: ARTHUR },
  { text: "This study was published in a peer-reviewed journal.", voice: ELLEN },
  { text: "The implications of our findings are significant for public health.", voice: ARTHUR },

  // Dialogue — Dr. Nakamura = Arthur (male)
  { text: "Thank you for attending my presentation. I would be happy to take your questions.", voice: ARTHUR },
  { text: "Of course. We used a double-blind trial with 200 participants. The main variable was the supplement dosage.", voice: ARTHUR },
  { text: "That is a great question. If we had a larger sample, the results would be more reliable.", voice: ARTHUR },
  { text: "If these results were replicated in a larger study, they would change how we approach nutritional therapy.", voice: ARTHUR },

  // Dialogue — Patricia = Ellen (female)
  { text: "Thank you, Dr. Nakamura. Could you elaborate on the methodology of your study?", voice: ELLEN },
  { text: "Interesting. Have you considered the possibility that the sample size could introduce bias?", voice: ELLEN },
  { text: "What are the implications of your preliminary findings?", voice: ELLEN },
  { text: "One more question. Have you found any correlation between age and the effectiveness of the supplement?", voice: ELLEN },

  // Survival card (alternate)
  { text: "Could you elaborate on your methodology?", voice: ELLEN },
  { text: "Have you considered the possibility that there is bias in the sample?", voice: ARTHUR },
  { text: "If you were to replicate this study, what would you change?", voice: ELLEN },
  { text: "Is there a correlation between the variables you studied?", voice: ARTHUR },

  // Pronunciation phrases (Ellen)
  { text: "Could you elaborate on the methodology of your study?", voice: ELLEN },
  { text: "If we had a larger sample, the results would be more reliable.", voice: ELLEN },
  { text: "What are the implications of your findings for public health?", voice: ELLEN },

  // Fill-in-the-blank phrases (alternate)
  { text: "The hypothesis was supported by the preliminary data.", voice: ELLEN },
  { text: "If we replicated this study, the results would be more significant.", voice: ARTHUR },
  { text: "There is a strong correlation between the two variables.", voice: ELLEN },
  { text: "We must eliminate bias from our sample selection.", voice: ARTHUR },
  { text: "The implications of this research are far-reaching.", voice: ELLEN },
  { text: "Our methodology was published in a peer-reviewed journal.", voice: ARTHUR },

  // Listening — conference presentation (Ellen formal)
  { text: "Good afternoon, everyone. Today I would like to present our preliminary findings on nutritional supplements and glycemic control. Our methodology involved a double-blind trial with 200 participants across three countries. We studied the correlation between supplement dosage and blood sugar levels. The main variable was the daily dosage of functional ingredients. Our sample was carefully selected to eliminate bias. The preliminary results suggest a significant correlation between higher dosages and improved glycemic control. However, we acknowledge that these findings need to be replicated in a peer-reviewed study before we can discuss their full implications.", voice: ELLEN },
];

function toFilename(text) {
  var clean = text.toLowerCase().replace(/[^a-z0-9 ]/g, '').replace(/ +/g, '_');
  return (PREFIX + clean).substring(0, 60);
}

async function gen(text, voiceId, outPath) {
  const r = await fetch('https://api.elevenlabs.io/v1/text-to-speech/' + voiceId, {
    method: 'POST',
    headers: { 'xi-api-key': API_KEY, 'Content-Type': 'application/json' },
    body: JSON.stringify({ text, model_id: 'eleven_turbo_v2_5', voice_settings: { stability: 0.5, similarity_boost: 0.75 } }),
  });
  if (!r.ok) throw new Error(r.status + ': ' + (await r.text()));
  const buf = Buffer.from(await r.arrayBuffer());
  fs.writeFileSync(outPath, buf);
  return buf.length;
}

async function main() {
  if (!API_KEY) { console.error('Set ELEVENLABS_API_KEY env var'); process.exit(1); }
  if (!fs.existsSync(DIR)) fs.mkdirSync(DIR, { recursive: true });

  const seen = new Set();
  const unique = PHRASES.filter(p => { const k = p.text.toLowerCase(); if (seen.has(k)) return false; seen.add(k); return true; });

  console.log('Generating ' + unique.length + ' Aula 3 audio files...');
  for (const p of unique) {
    const fname = toFilename(p.text) + '.mp3';
    const outPath = path.join(DIR, fname);
    if (fs.existsSync(outPath)) {
      console.log('SKIP: ' + fname);
    } else {
      try {
        const bytes = await gen(p.text, p.voice, outPath);
        console.log('OK [' + (p.voice === ELLEN ? 'ellen' : 'arthur') + ']: ' + fname + ' (' + (bytes/1024).toFixed(1) + 'KB)');
        await new Promise(r => setTimeout(r, 500));
      } catch(e) { console.error('FAIL: ' + fname + ' — ' + e.message); }
    }
  }
  console.log('\nDone! ' + unique.length + ' audio entries.');
}

main().catch(e => { console.error(e); process.exit(1); });
