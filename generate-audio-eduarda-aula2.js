const fs = require('fs');
const path = require('path');
const https = require('https');

const ELEVENLABS_API_KEY = process.env.ELEVENLABS_API_KEY;
if (!ELEVENLABS_API_KEY) { console.error('ERROR: ELEVENLABS_API_KEY not set'); process.exit(1); }

const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const OUTPUT_DIR = path.join(__dirname, 'public', 'audio', 'eduarda-gabriel');

const audioMap = {
  "Interrupt": "aula2_interrupt.mp3",
  "Clarify": "aula2_clarify.mp3",
  "Elaborate": "aula2_elaborate.mp3",
  "Agenda": "aula2_agenda.mp3",
  "Follow Up": "aula2_follow_up.mp3",
  "Perspective": "aula2_perspective.mp3",
  "Proposal": "aula2_proposal.mp3",
  "Consensus": "aula2_consensus.mp3",
  "Sorry to interrupt, but I have an update on the deal.": "aula2_ex_interrupt.mp3",
  "Could you clarify what you mean by the recovery timeline?": "aula2_ex_clarify.mp3",
  "Could you elaborate on the restructuring proposal?": "aula2_ex_elaborate.mp3",
  "The first item on the agenda is the creditor proposal.": "aula2_ex_agenda.mp3",
  "I will follow up with the legal team on Friday.": "aula2_ex_follow_up.mp3",
  "From my perspective, the deal needs more time.": "aula2_ex_perspective.mp3",
  "The creditors submitted a new proposal yesterday.": "aula2_ex_proposal.mp3",
  "Do we have a consensus on the next steps?": "aula2_ex_consensus.mp3",
  "Do you agree with the restructuring proposal?": "aula2_fill_agree.mp3",
  "Does the team have a consensus on the timeline?": "aula2_fill_consensus.mp3",
  "Could I add something to the agenda?": "aula2_fill_add.mp3",
  "If I may, I would like to elaborate on that.": "aula2_fill_elaborate.mp3",
  "I will follow up with the legal team before the next call.": "aula2_fill_follow_up.mp3",
  "From my perspective, the proposal needs more time.": "aula2_fill_perspective.mp3",
  "If I may, I would like to share my perspective on the deal.": "aula2_pron1.mp3",
  "Sorry to interrupt, but I think we need to clarify the timeline.": "aula2_pron2.mp3",
  "Do we have a consensus on the proposal, or should I follow up?": "aula2_pron3.mp3",
  "Alright, let us go through the agenda. First item — the creditor proposal.": "aula2_dial1.mp3",
  "If I may, I would like to share an update from the Brazilian side.": "aula2_dial2.mp3",
  "Please go ahead, Eduarda.": "aula2_dial3.mp3",
  "The creditors are asking us to elaborate on the recovery timeline.": "aula2_dial4.mp3",
  "I see. Do we have a consensus on the timeline internally?": "aula2_dial5.mp3",
  "Not yet. I think we need to clarify our position before the next call.": "aula2_dial6.mp3",
  "Good point. Could you follow up with the legal team on that?": "aula2_dial7.mp3",
  "Of course. I will follow up and share my perspective by Friday.": "aula2_dial8.mp3",
  "Could I add something to this point?": "aula2_surv1.mp3",
  "If I may, I would like to share my perspective.": "aula2_surv2.mp3",
  "Sorry to interrupt, but I think we need to clarify this.": "aula2_surv3.mp3",
  "Going back to what you said about the deal...": "aula2_surv4.mp3",
  "Do we have a consensus on this proposal?": "aula2_surv5.mp3",
  "[order-l2]": "aula2_order_l2.mp3",
  "Sorry to interrupt, but I would like to share a different perspective.": "aula2_oral1.mp3",
  "Could you clarify what you mean by that?": "aula2_oral2.mp3",
  "If I may, I would like to add something to this point.": "aula2_oral3.mp3",
  "Before we end, could I suggest we follow up on the timeline next week?": "aula2_oral4.mp3",
  "Yes, from my perspective, we have reached a consensus on this.": "aula2_oral5.mp3",
  "Going back to what you said about the proposal, I think we need to elaborate on the numbers.": "aula2_oral6.mp3"
};

const jamesLines = ["Alright, let us go through the agenda. First item — the creditor proposal.","Please go ahead, Eduarda.","I see. Do we have a consensus on the timeline internally?","Good point. Could you follow up with the legal team on that?"];
const eduardaLines = ["If I may, I would like to share an update from the Brazilian side.","The creditors are asking us to elaborate on the recovery timeline.","Not yet. I think we need to clarify our position before the next call.","Of course. I will follow up and share my perspective by Friday."];

function countWords(t) { return t.trim().split(/\s+/).length; }
let alt = 0;
function getVoice(text) {
  if (jamesLines.includes(text)) return { id: ARTHUR, name: 'Arthur' };
  if (eduardaLines.includes(text)) return { id: ELLEN, name: 'Ellen' };
  if (countWords(text) <= 2) return { id: ARTHUR, name: 'Arthur' };
  const v = alt % 2 === 0 ? { id: ARTHUR, name: 'Arthur' } : { id: ELLEN, name: 'Ellen' };
  alt++;
  return v;
}

function generateAudio(text, voiceId, outputPath) {
  return new Promise((resolve, reject) => {
    const postData = JSON.stringify({ text: text, model_id: 'eleven_monolingual_v1', voice_settings: { stability: 0.5, similarity_boost: 0.75 } });
    const options = {
      hostname: 'api.elevenlabs.io',
      path: '/v1/text-to-speech/' + voiceId + '?output_format=mp3_44100_128',
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'xi-api-key': ELEVENLABS_API_KEY, 'Content-Length': Buffer.byteLength(postData) }
    };
    const req = https.request(options, (res) => {
      if (res.statusCode !== 200) { let b = ''; res.on('data', d => b += d); res.on('end', () => reject(new Error('API ' + res.statusCode + ': ' + b))); return; }
      const chunks = [];
      res.on('data', c => chunks.push(c));
      res.on('end', () => { fs.writeFileSync(outputPath, Buffer.concat(chunks)); resolve(); });
    });
    req.on('error', reject);
    req.write(postData);
    req.end();
  });
}

async function main() {
  const entries = Object.entries(audioMap);
  let gen = 0, skip = 0;
  console.log('Generating ' + entries.length + ' Aula 2 audio files...');
  for (let i = 0; i < entries.length; i++) {
    const [text, file] = entries[i];
    const out = path.join(OUTPUT_DIR, file);
    if (fs.existsSync(out) && fs.statSync(out).size > 1000) { skip++; if (countWords(text) > 2 && !jamesLines.includes(text) && !eduardaLines.includes(text)) alt++; continue; }
    const voice = getVoice(text);
    try {
      await generateAudio(text, voice.id, out);
      gen++;
      console.log('Generated ' + (gen + skip) + '/' + entries.length + ': ' + file + ' (' + voice.name + ')');
    } catch (err) { console.error('FAILED ' + file + ': ' + err.message); }
    if (i < entries.length - 1) await new Promise(r => setTimeout(r, 500));
  }
  console.log('Done! Generated: ' + gen + ', Skipped: ' + skip);
}
main().catch(console.error);
