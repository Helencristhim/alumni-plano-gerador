const fs = require('fs');
const path = require('path');
const https = require('https');

const ELEVENLABS_API_KEY = process.env.ELEVENLABS_API_KEY;
if (!ELEVENLABS_API_KEY) { console.error('ERROR: ELEVENLABS_API_KEY not set'); process.exit(1); }

const ASH = 'VU16byTywsWv5JpI8rbc';
const RILEY = 'hA4zGnmTwX2NQiTRMt7o';
const OUTPUT_DIR = path.join(__dirname, '..', 'public', 'audio', 'roberto-rezende');
if (!fs.existsSync(OUTPUT_DIR)) fs.mkdirSync(OUTPUT_DIR, { recursive: true });

const audios = [
  // Vocab words (ASH)
  { text: "Chairperson", file: "aula11_chairperson.mp3", voice: ASH },
  { text: "Minutes", file: "aula11_minutes.mp3", voice: ASH },
  { text: "Allocate", file: "aula11_allocate.mp3", voice: ASH },
  { text: "Adjourn", file: "aula11_adjourn.mp3", voice: ASH },
  { text: "Propose", file: "aula11_propose.mp3", voice: ASH },
  { text: "Delegate", file: "aula11_delegate.mp3", voice: ASH },
  { text: "Consensus", file: "aula11_consensus.mp3", voice: ASH },
  { text: "Table", file: "aula11_table.mp3", voice: ASH },
  { text: "Facilitate", file: "aula11_facilitate.mp3", voice: ASH },
  { text: "Stakeholder", file: "aula11_stakeholder.mp3", voice: ASH },
  // Vocab sentences (alternating)
  { text: "The chairperson should always keep the meeting on track.", file: "aula11_chairperson_sentence.mp3", voice: ASH },
  { text: "Could you take the minutes today?", file: "aula11_minutes_sentence.mp3", voice: RILEY },
  { text: "We should allocate fifteen minutes to each topic.", file: "aula11_allocate_sentence.mp3", voice: ASH },
  { text: "I would suggest we adjourn the budget discussion.", file: "aula11_adjourn_sentence.mp3", voice: RILEY },
  { text: "I would like to propose a new agenda item.", file: "aula11_propose_sentence.mp3", voice: ASH },
  { text: "We should delegate this task to the marketing team.", file: "aula11_delegate_sentence.mp3", voice: RILEY },
  { text: "We need to reach consensus before moving forward.", file: "aula11_consensus_sentence.mp3", voice: ASH },
  { text: "Should we table this discussion until next week?", file: "aula11_table_sentence.mp3", voice: RILEY },
  { text: "Would you like to facilitate the next section?", file: "aula11_facilitate_sentence.mp3", voice: ASH },
  { text: "All stakeholders should receive the agenda in advance.", file: "aula11_stakeholder_sentence.mp3", voice: RILEY },
  // Dialogue: Roberto=ASH, Wei Lin=RILEY, Amy=RILEY
  { text: "Good morning. I would like to propose the agenda for today. We should start with the Q3 targets.", file: "aula11_dialogue_roberto1.mp3", voice: ASH },
  { text: "That sounds good. Could we also allocate time to discuss the new stakeholders in agriculture?", file: "aula11_dialogue_weilin1.mp3", voice: RILEY },
  { text: "Absolutely. I would suggest we spend fifteen minutes on that. Amy, would you like to facilitate that section?", file: "aula11_dialogue_roberto2.mp3", voice: ASH },
  { text: "I would be happy to. Should I prepare a brief overview of the stakeholders?", file: "aula11_dialogue_amy1.mp3", voice: RILEY },
  { text: "That would be very helpful. We should also delegate the minutes. Wei Lin, could you take the minutes today?", file: "aula11_dialogue_roberto3.mp3", voice: ASH },
  { text: "Of course. Should we table the budget discussion for next week? We do not have the latest numbers yet.", file: "aula11_dialogue_weilin2.mp3", voice: RILEY },
  { text: "Good point. We could adjourn that item until we reach consensus on the targets first.", file: "aula11_dialogue_roberto4.mp3", voice: ASH },
  { text: "I agree. The chairperson should always prioritize the most urgent items. Well structured, Roberto.", file: "aula11_dialogue_amy2.mp3", voice: RILEY },
  // Listening 1
  { text: "Good morning, everyone. I would like to go over the proposed agenda for today's meeting. First, we should review the Q3 targets. I would suggest spending ten minutes on this. Second, I would like to propose a discussion on new agricultural stakeholders. Amy will facilitate this section. Third, we could allocate fifteen minutes to delegate responsibilities for the trade fair. Finally, I would recommend we table the budget discussion until next week, when we have the final numbers. The meeting should take approximately sixty minutes. Would anyone like to add anything before we begin?", file: "aula11_listening1_agenda_proposal.mp3", voice: ASH },
  // Listening 2
  { text: "Roberto, I have a few suggestions for the agenda. First, you should always send the agenda at least twenty-four hours before the meeting. This gives stakeholders time to prepare. Second, you could add time estimates next to each item. For example: Q3 targets, fifteen minutes. Third, I would recommend adding an any other business section at the end. This is where people can bring up topics that are not on the agenda. Finally, you should always end with a clear list of action items and who is responsible. Would you like me to help you draft the template?", file: "aula11_listening2_amy_suggestions.mp3", voice: RILEY },
  // Quick fire (alternating)
  { text: "We should start with the Q3 targets.", file: "aula11_quickfire1.mp3", voice: ASH },
  { text: "Could you take the minutes today?", file: "aula11_quickfire2.mp3", voice: RILEY },
  { text: "I would be happy to facilitate that section.", file: "aula11_quickfire3.mp3", voice: ASH },
  { text: "We should table that discussion until next week.", file: "aula11_quickfire4.mp3", voice: RILEY },
  { text: "Would you like to present first or second?", file: "aula11_quickfire5.mp3", voice: ASH },
  { text: "We could allocate fifteen minutes to that item.", file: "aula11_quickfire6.mp3", voice: RILEY },
  // Survival (alternating)
  { text: "I would like to propose the agenda for today.", file: "aula11_survival1.mp3", voice: ASH },
  { text: "Could we allocate fifteen minutes to this topic?", file: "aula11_survival2.mp3", voice: RILEY },
  { text: "We should table that discussion until next week.", file: "aula11_survival3.mp3", voice: ASH },
  { text: "Would you like to facilitate this section?", file: "aula11_survival4.mp3", voice: RILEY },
  { text: "I would suggest we delegate the minutes to Wei Lin.", file: "aula11_survival5.mp3", voice: ASH },
  // Ordering
  { text: "Good morning. I would like to propose the agenda. We should start with the Q3 targets. Could we also allocate time to discuss stakeholders? I would suggest we delegate the minutes. Should we table the budget item for next week?", file: "order_l11_ordering.mp3", voice: ASH }
];

function generateAudio(item) {
  return new Promise((resolve, reject) => {
    const filePath = path.join(OUTPUT_DIR, item.file);
    if (fs.existsSync(filePath)) { console.log(`SKIP: ${item.file}`); return resolve(); }
    const postData = JSON.stringify({ text: item.text, model_id: "eleven_multilingual_v2", voice_settings: { stability: 0.5, similarity_boost: 0.75 } });
    const options = { hostname: 'api.elevenlabs.io', path: `/v1/text-to-speech/${item.voice}`, method: 'POST', headers: { 'Content-Type': 'application/json', 'xi-api-key': ELEVENLABS_API_KEY, 'Accept': 'audio/mpeg' } };
    const req = https.request(options, (res) => {
      if (res.statusCode !== 200) { let b=''; res.on('data',c=>b+=c); res.on('end',()=>{console.error(`ERR ${res.statusCode}: ${item.file} ${b}`);reject(new Error(`HTTP ${res.statusCode}`))}); return; }
      const chunks = []; res.on('data', c => chunks.push(c)); res.on('end', () => { fs.writeFileSync(filePath, Buffer.concat(chunks)); console.log(`OK: ${item.file} (${item.voice===ASH?'ASH':'RILEY'})`); resolve(); });
    });
    req.on('error', reject); req.write(postData); req.end();
  });
}

async function main() {
  console.log(`Generating ${audios.length} audio files for Roberto Rezende Aula 11...\n`);
  for (let i = 0; i < audios.length; i++) { await generateAudio(audios[i]); if (i < audios.length - 1) await new Promise(r => setTimeout(r, 500)); }
  console.log(`\nDone! ${audios.length} files processed.`);
}
main().catch(e => { console.error(e); process.exit(1); });
