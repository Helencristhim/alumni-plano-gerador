const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const DIR = path.join(__dirname, '..', 'public', 'audio', 'patricia-ruffo');
const PREFIX = 'aula2_';

// Patricia is female → Ellen for her lines
// Dr. Santos is male → Arthur for his lines
// Single words → Arthur
// Phrases alternate Arthur/Ellen
const PHRASES = [
  // Vocab words (Arthur — short, 1-2 words)
  { text: "Disagree", voice: ARTHUR },
  { text: "Evidence", voice: ARTHUR },
  { text: "Perspective", voice: ARTHUR },
  { text: "Outcome", voice: ARTHUR },
  { text: "Propose", voice: ARTHUR },
  { text: "Convince", voice: ARTHUR },
  { text: "Approach", voice: ARTHUR },
  { text: "Significant", voice: ARTHUR },
  { text: "Acknowledge", voice: ARTHUR },
  { text: "Counterargument", voice: ARTHUR },

  // Vocab example sentences (alternate Arthur/Ellen)
  { text: "I disagree with the proposed changes.", voice: ELLEN },
  { text: "The evidence supports our hypothesis.", voice: ARTHUR },
  { text: "From my perspective, the data is clear.", voice: ELLEN },
  { text: "The outcome of the trial was positive.", voice: ARTHUR },
  { text: "I propose we extend the deadline.", voice: ELLEN },
  { text: "The results will convince the committee.", voice: ARTHUR },
  { text: "We need a different approach to this problem.", voice: ELLEN },
  { text: "The improvement was significant.", voice: ARTHUR },
  { text: "I acknowledge that the timeline is tight.", voice: ELLEN },
  { text: "That is a strong counterargument.", voice: ARTHUR },

  // Dialogue — Dr. Santos = Arthur (male)
  { text: "I propose that we change the formula. The current approach is not showing significant results.", voice: ARTHUR },
  { text: "From my perspective, the outcome of the current trial is not convincing enough.", voice: ARTHUR },
  { text: "That is a valid counterargument. What do you propose instead?", voice: ARTHUR },
  { text: "That sounds reasonable. If we extend the trial, will we still meet the deadline?", voice: ARTHUR },

  // Dialogue — Patricia = Ellen (female)
  { text: "I see your point, Dr. Santos, but I would argue that we need more evidence before making changes.", voice: ELLEN },
  { text: "I acknowledge your concern, but if we change the formula now, we will lose six months of data.", voice: ELLEN },
  { text: "I propose that we extend the trial for three more months. If the results do not improve, I will agree to change the approach.", voice: ELLEN },
  { text: "Based on the evidence so far, I am convinced we will see significant improvement by December.", voice: ELLEN },

  // Survival Card (alternate)
  { text: "I see your point, but I would like to propose an alternative.", voice: ELLEN },
  { text: "Based on the evidence, I disagree with this approach.", voice: ARTHUR },
  { text: "If we change the methodology, the outcomes will be more significant.", voice: ELLEN },
  { text: "From my perspective, we should acknowledge the limitations first.", voice: ARTHUR },
  { text: "I understand your counterargument, but the data suggests otherwise.", voice: ELLEN },

  // Pronunciation phrases (Ellen — Patricia practicing)
  { text: "I see your point, but I would argue that we need more evidence.", voice: ELLEN },
  { text: "If we change the formula, the results will improve significantly.", voice: ELLEN },

  // Fill-in-the-blank phrases (alternate)
  { text: "I see your point, but I disagree with this approach.", voice: ELLEN },
  { text: "Based on the evidence, the outcome was significant.", voice: ARTHUR },
  { text: "If we propose a new approach, the committee will approve it.", voice: ELLEN },
  { text: "I acknowledge that there are limitations in our study.", voice: ARTHUR },
  { text: "Her counterargument was very convincing.", voice: ELLEN },
  { text: "From my perspective, we need more evidence.", voice: ARTHUR },

  // Listening 1 — conference presentation (Ellen formal, long passage)
  { text: "Good morning, everyone. I would like to address the proposed changes to our supplement formula. In my opinion, we should not change the formula at this point. Based on the evidence from the last six months, our current approach is showing gradual but significant improvement. If we change the formula now, we will lose valuable data. I acknowledge that the progress has been slow, but from my perspective, the outcomes are moving in the right direction. I propose that we extend the current trial for three more months before making any changes.", voice: ELLEN },
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
  const audioMap = {};

  console.log('Generating ' + unique.length + ' Aula 2 audio files...');
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
    audioMap[p.text] = '/audio/patricia-ruffo/' + fname;
  }

  fs.writeFileSync(path.join(DIR, 'audioMap-aula2.json'), JSON.stringify(audioMap, null, 2));
  console.log('\nDone! ' + unique.length + ' audio entries.');
  console.log('Run: ELEVENLABS_API_KEY=your_key node scripts/generate-patricia-aula2-audio.js');
}

main().catch(e => { console.error(e); process.exit(1); });
