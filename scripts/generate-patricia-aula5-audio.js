const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const DIR = path.join(__dirname, '..', 'public', 'audio', 'patricia-ruffo');
const PREFIX = 'aula5_';

const PHRASES = [
  { text: "Panel", voice: ARTHUR },
  { text: "Keynote", voice: ARTHUR },
  { text: "Moderator", voice: ARTHUR },
  { text: "Consensus", voice: ARTHUR },
  { text: "Delegate", voice: ARTHUR },
  { text: "Networking", voice: ARTHUR },
  { text: "Symposium", voice: ARTHUR },
  { text: "Abstract", voice: ARTHUR },
  { text: "Findings", voice: ARTHUR },
  { text: "Recommendation", voice: ARTHUR },
  { text: "Patricia was invited to join the panel discussion.", voice: ELLEN },
  { text: "The keynote speaker presented groundbreaking research.", voice: ELLEN },
  { text: "The moderator asked each delegate to share their findings.", voice: ELLEN },
  { text: "The team reached a consensus on the new methodology.", voice: ELLEN },
  { text: "Every delegate received a copy of the conference abstract.", voice: ELLEN },
  { text: "Networking at the symposium led to a new collaboration.", voice: ARTHUR },
  { text: "The symposium featured presentations from twelve countries.", voice: ELLEN },
  { text: "Her abstract was accepted for the main session.", voice: ARTHUR },
  { text: "The findings of our study have important implications.", voice: ELLEN },
  { text: "My recommendation is to replicate the study with a larger sample.", voice: ARTHUR },
  { text: "Welcome to the Abbott Science Summit. Dr. Ruffo, please begin with your keynote.", voice: ARTHUR },
  { text: "Thank you, Dr. Ruffo. Delegates, do you have any questions for the panel?", voice: ARTHUR },
  { text: "Dr. Santos, you mentioned earlier that you disagreed with the methodology. Could you elaborate?", voice: ARTHUR },
  { text: "Interesting. Dr. Ruffo, how would you respond to that counterargument?", voice: ARTHUR },
  { text: "Thank you. I would like to present our findings on glycemic control. Our study has shown a significant correlation between supplement dosage and glycemic response.", voice: ELLEN },
  { text: "I see your point, Dr. Santos, but based on the evidence, our methodology was peer-reviewed and our sample was carefully selected to eliminate bias.", voice: ELLEN },
  { text: "My recommendation is that we reach a consensus on extending the trial. If we had more time, we would be able to replicate the study with a larger sample.", voice: ELLEN },
  { text: "In conclusion, I would like to highlight that our findings have important implications for nutritional therapy. I propose that the delegates consider funding a larger symposium next year.", voice: ELLEN },
  { text: "I would like to present our findings to the panel.", voice: ELLEN },
  { text: "Based on the evidence, my recommendation is to continue the current approach.", voice: ELLEN },
  { text: "The delegates reached a consensus on the next steps.", voice: ELLEN },
  { text: "If we had more funding, we would replicate the study at a larger symposium.", voice: ELLEN },
  { text: "I would like to thank the moderator and all the delegates for their feedback.", voice: ELLEN },
  { text: "I would like to present our findings on glycemic control to the panel.", voice: ELLEN },
  { text: "My recommendation is that we reach a consensus on the methodology.", voice: ARTHUR },
  { text: "The delegates at the symposium discussed the implications of our research.", voice: ELLEN },
  { text: "The panel discussed the findings of the latest study.", voice: ARTHUR },
  { text: "The keynote speaker highlighted the importance of peer-reviewed research.", voice: ELLEN },
  { text: "The moderator asked each delegate to present their abstract.", voice: ARTHUR },
  { text: "We reached a consensus on the recommendation for future studies.", voice: ELLEN },
  { text: "Networking at the symposium helped us find new collaborators.", voice: ARTHUR },
  { text: "Her findings were presented at the keynote session.", voice: ELLEN },
  { text: "Good morning, delegates. Welcome to the Abbott Science Summit. My name is Patricia Ruffo, and I am honored to deliver the keynote presentation today. Over the past year, our team has made significant progress on glycemic control research. I reported to the stakeholders last month that we had completed the first phase of our trial. Dr. Nakamura said that the preliminary findings were very promising. He mentioned that the correlation between supplement dosage and glycemic response was significant. Today, I would like to present our complete findings and share my recommendations for the next phase. If we had more funding, we would replicate this study across five countries. I propose that this symposium consider establishing a consensus on international collaboration for nutritional research.", voice: ELLEN },
  { text: "Dr. Ruffo, I really enjoyed your keynote. Your findings on glycemic control were fascinating. I have been working on a similar project in Tokyo. Dr. Nakamura mentioned that your methodology was very innovative. I was wondering if you would be open to a collaboration. If we combined our data, we would have the largest sample in this field. Could you elaborate on how you selected your control group? I would argue that a multi-center approach could strengthen the results. My recommendation is that we set up a meeting next month to discuss the details.", voice: ARTHUR },
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
  console.log('Generating ' + unique.length + ' Aula 5 audio files...');
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
