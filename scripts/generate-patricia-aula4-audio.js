const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const DIR = path.join(__dirname, '..', 'public', 'audio', 'patricia-ruffo');
const PREFIX = 'aula4_';

const PHRASES = [
  { text: "Report", voice: ARTHUR },
  { text: "Update", voice: ARTHUR },
  { text: "Summarize", voice: ARTHUR },
  { text: "Highlight", voice: ARTHUR },
  { text: "Deadline", voice: ARTHUR },
  { text: "Progress", voice: ARTHUR },
  { text: "Stakeholder", voice: ARTHUR },
  { text: "Milestone", voice: ARTHUR },
  { text: "Deliverable", voice: ARTHUR },
  { text: "Feedback", voice: ARTHUR },
  { text: "I need to report our findings to the team.", voice: ELLEN },
  { text: "Let me update you on the latest trial results.", voice: ARTHUR },
  { text: "I will summarize the key points of our research.", voice: ELLEN },
  { text: "I would like to highlight three important milestones.", voice: ARTHUR },
  { text: "The deadline for the final report is next Friday.", voice: ELLEN },
  { text: "We have made significant progress this quarter.", voice: ARTHUR },
  { text: "The stakeholders are expecting a detailed update.", voice: ELLEN },
  { text: "We reached an important milestone last month.", voice: ARTHUR },
  { text: "The deliverable is due by the end of the week.", voice: ELLEN },
  { text: "The feedback from the committee was very positive.", voice: ARTHUR },
  { text: "Good morning, team. Patricia, could you give us an update on the glycemic control project?", voice: ARTHUR },
  { text: "Thank you. What did the preliminary results show?", voice: ARTHUR },
  { text: "That is excellent progress. What are the next milestones?", voice: ARTHUR },
  { text: "Great. Please keep the stakeholders informed. When is the deadline for the final deliverable?", voice: ARTHUR },
  { text: "Of course. I reported to the team last week that we had completed the first phase of the trial.", voice: ELLEN },
  { text: "Dr. Nakamura said that the correlation between dosage and glycemic response was significant. He also mentioned that the sample size needed to be larger.", voice: ELLEN },
  { text: "The next milestone is to replicate the study with 300 participants. I told the research team that we would need additional funding.", voice: ELLEN },
  { text: "The deadline is December 15th. I will summarize our progress in a written report and highlight the key deliverables for the stakeholders.", voice: ELLEN },
  { text: "I would like to report that we have made significant progress.", voice: ELLEN },
  { text: "Let me update you on the latest developments.", voice: ARTHUR },
  { text: "Dr. Nakamura said that the results were very promising.", voice: ELLEN },
  { text: "The team mentioned that they would need more time to finish the deliverable.", voice: ARTHUR },
  { text: "I will summarize the key milestones and send my feedback by the deadline.", voice: ELLEN },
  { text: "I would like to report that we have completed the first milestone.", voice: ELLEN },
  { text: "Dr. Nakamura said that the preliminary results were significant.", voice: ARTHUR },
  { text: "The stakeholders mentioned that they expected a progress update by the deadline.", voice: ELLEN },
  { text: "I need to report our progress to the stakeholders.", voice: ARTHUR },
  { text: "She said that the deadline was next Friday.", voice: ELLEN },
  { text: "The team mentioned that they had reached an important milestone.", voice: ARTHUR },
  { text: "Let me summarize the key deliverables for this quarter.", voice: ELLEN },
  { text: "He told us that the feedback from the committee was positive.", voice: ARTHUR },
  { text: "I would like to highlight the progress we have made.", voice: ELLEN },
  { text: "Good morning, everyone. I would like to update you on the glycemic control project. Last month, we reached an important milestone. We completed the first phase of our clinical trial with 120 participants. Dr. Nakamura reported that the preliminary results showed a significant correlation between supplement dosage and glycemic response. He said that the methodology was solid, but he mentioned that we would need a larger sample to confirm our findings. The stakeholders have provided positive feedback so far. Our next deliverable is a comprehensive progress report, which is due by December 15th. I will summarize our findings and highlight the key milestones for the team.", voice: ELLEN },
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
  console.log('Generating ' + unique.length + ' Aula 4 audio files...');
  for (const p of unique) {
    const fname = toFilename(p.text) + '.mp3';
    const outPath = path.join(DIR, fname);
    if (fs.existsSync(outPath)) { console.log('SKIP: ' + fname); }
    else {
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
