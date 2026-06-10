const https = require('https');
const fs = require('fs');
const path = require('path');

const ASH = 'VU16byTywsWv5JpI8rbc';
const RILEY = 'hA4zGnmTwX2NQiTRMt7o';
const API_KEY = process.env.ELEVENLABS_API_KEY;
const OUTPUT_DIR = path.join(__dirname, 'public', 'audio', 'natalie-viegas');

const entries = [
  // VOCAB (Riley - female student)
  { file: 'aula7_procurement.mp3', text: 'Procurement', voice: RILEY },
  { file: 'aula7_tender.mp3', text: 'Tender', voice: RILEY },
  { file: 'aula7_compliance.mp3', text: 'Compliance', voice: RILEY },
  { file: 'aula7_vendor.mp3', text: 'Vendor', voice: RILEY },
  { file: 'aula7_clause.mp3', text: 'Clause', voice: RILEY },
  { file: 'aula7_negotiate.mp3', text: 'Negotiate', voice: RILEY },
  { file: 'aula7_deadline.mp3', text: 'Deadline', voice: RILEY },
  { file: 'aula7_approval.mp3', text: 'Approval', voice: RILEY },
  { file: 'aula7_bid.mp3', text: 'Bid', voice: RILEY },
  { file: 'aula7_clarify.mp3', text: 'Clarify', voice: RILEY },

  // FILL-IN-THE-BLANK (alternate)
  { file: 'aula7_fill_submit_bid.mp3', text: 'If we submit the bid on time, the client will review it.', voice: RILEY },
  { file: 'aula7_fill_clarify_compliance.mp3', text: 'Could you please clarify the compliance requirements?', voice: ASH },
  { file: 'aula7_fill_vendor_agrees.mp3', text: 'If the vendor agrees to the terms, we will sign the contract.', voice: RILEY },
  { file: 'aula7_fill_mind_sending.mp3', text: 'Would you mind sending the tender documents by Friday?', voice: ASH },
  { file: 'aula7_fill_miss_deadline.mp3', text: 'If we miss the deadline, the procurement office will not approve our bid.', voice: RILEY },
  { file: 'aula7_fill_schedule_call.mp3', text: 'Could we schedule a call to negotiate the payment terms?', voice: ASH },

  // SPEECH (Riley - student)
  { file: 'aula7_speech_submit_bid.mp3', text: 'If we submit the bid on time, the procurement office will review it next week.', voice: RILEY },
  { file: 'aula7_speech_clarify_tender.mp3', text: 'Could you please clarify the compliance requirements for this tender?', voice: RILEY },
  { file: 'aula7_speech_mind_sending.mp3', text: 'Would you mind sending the updated tender documents before the deadline?', voice: RILEY },

  // ORDERING
  { file: 'aula7_order_l7.mp3', text: 'Thank you for joining the call. I would like to discuss the new tender. Could you clarify the compliance requirements for this tender? If we meet all the requirements, the procurement office will approve our proposal. Would you mind sending the updated bid by the deadline? If both parties agree, we will sign the contract this month.', voice: RILEY },

  // SURVIVAL (alternate)
  { file: 'aula7_surv_meet_deadline.mp3', text: 'If we meet the deadline, we will win the contract.', voice: RILEY },
  { file: 'aula7_surv_vendor_agrees.mp3', text: 'If the vendor agrees, we will negotiate the final terms.', voice: ASH },
  { file: 'aula7_surv_schedule_call.mp3', text: 'Could we schedule a call to discuss the procurement process?', voice: RILEY },

  // ORAL DRILLING
  { file: 'aula7_oral_procurement.mp3', text: 'If we win the procurement process, we will deploy by Q2.', voice: RILEY },
  { file: 'aula7_oral_tender.mp3', text: 'Could you please send the tender documents?', voice: ASH },
  { file: 'aula7_oral_complies.mp3', text: 'If the system complies, the client will give approval.', voice: RILEY },
  { file: 'aula7_oral_clarify_clause.mp3', text: 'Would you mind clarifying this clause?', voice: ASH },
  { file: 'aula7_oral_bid.mp3', text: 'If our bid is competitive, we will win the contract.', voice: RILEY },
  { file: 'aula7_oral_negotiate.mp3', text: 'Could we negotiate the deadline?', voice: ASH },

  // DIALOGUE (Dr. Silva=Ash, Natalie=Riley)
  { file: 'aula7_dlg_silva_1.mp3', text: 'Good morning, Natalie. Thank you for the call. I have reviewed your bid. Could you walk me through the compliance section?', voice: ASH },
  { file: 'aula7_dlg_natalie_1.mp3', text: 'Of course, Dr. Silva. If our system meets the ISO 27001 standards, it will fully comply with your security requirements.', voice: RILEY },
  { file: 'aula7_dlg_silva_2.mp3', text: 'Good. I have a concern about the clause on late delivery penalties. Can we discuss that?', voice: ASH },
  { file: 'aula7_dlg_natalie_2.mp3', text: 'Absolutely. Could you please clarify which specific clause concerns you? If we negotiate the terms, I believe we can find a solution that works for both sides.', voice: RILEY },
  { file: 'aula7_dlg_silva_3.mp3', text: 'It is the two percent penalty per week. Is the deadline realistic?', voice: ASH },
  { file: 'aula7_dlg_natalie_3.mp3', text: 'If we receive approval by the end of this month, we will deliver on time. Would you mind sending the final procurement guidelines so we can adjust the tender?', voice: RILEY },
  { file: 'aula7_dlg_silva_4.mp3', text: 'I will send them today. If the vendor accepts the revised clause, we can move forward.', voice: ASH },
  { file: 'aula7_dlg_natalie_4.mp3', text: 'Excellent. If both parties agree, we will sign the contract this month. Thank you for your time, Dr. Silva.', voice: RILEY },

  // ERROR SENTENCES
  { file: 'aula7_ic_error_if_will_submit.mp3', text: 'If we will submit the bid, the client will review it.', voice: RILEY },
  { file: 'aula7_ic_error_mind_to_send.mp3', text: 'Would you mind to send the documents?', voice: RILEY },
  { file: 'aula7_ic_error_if_will_miss.mp3', text: 'If we will miss the deadline, we lose the contract.', voice: RILEY },
  { file: 'aula7_ic_error_could_clarifying.mp3', text: 'Could you clarifying the compliance requirements?', voice: RILEY },

  // LISTENING
  { file: 'aula7_listening_1_client_call.mp3', text: 'Good afternoon. I am calling about our bid for the digital infrastructure tender. The deadline is October thirty-first. If we submit all the required documents on time, the procurement committee will review our proposal within two weeks. I have a few questions about the compliance requirements. Could you please clarify which security certifications are mandatory? If the system meets ISO 27001 standards, will that be sufficient? Also, would you mind sending the updated vendor qualification form? If we receive it by Friday, we will be able to include it in our submission. One more thing. If our bid is approved, we will begin deployment within thirty days. Could we schedule a follow-up call next week to discuss the timeline in more detail? Thank you for your time.', voice: RILEY },
  { file: 'aula7_listening_2_followup.mp3', text: 'Hi Dr. Silva, this is a quick follow-up on our conversation last week. I wanted to confirm that the penalty clause has been negotiated. We agreed to reduce it from two percent to one percent per week. If the revised clause is acceptable, we will update the tender documents and resubmit by Thursday. Could you please send the final procurement approval so we can move forward? Also, would you mind confirming whether the compliance review has been completed? If everything is approved, we will sign the contract next Monday and begin the implementation phase immediately. Thank you for your continued support.', voice: ASH },
];

function generateAudio(entry) {
  return new Promise((resolve, reject) => {
    const data = JSON.stringify({ text: entry.text, model_id: 'eleven_multilingual_v2', voice_settings: { stability: 0.5, similarity_boost: 0.75 } });
    const options = { hostname: 'api.elevenlabs.io', path: `/v1/text-to-speech/${entry.voice}`, method: 'POST', headers: { 'Content-Type': 'application/json', 'xi-api-key': API_KEY, 'Content-Length': Buffer.byteLength(data) } };
    const outPath = path.join(OUTPUT_DIR, entry.file);
    if (fs.existsSync(outPath)) { console.log(`SKIP (exists): ${entry.file}`); return resolve(); }
    const req = https.request(options, (res) => {
      if (res.statusCode !== 200) { let body=''; res.on('data',d=>body+=d); res.on('end',()=>{console.error(`ERROR ${res.statusCode} for ${entry.file}: ${body}`);resolve();}); return; }
      const ws = fs.createWriteStream(outPath); res.pipe(ws);
      ws.on('finish', () => { console.log(`OK: ${entry.file}`); resolve(); });
      ws.on('error', reject);
    });
    req.on('error', reject); req.write(data); req.end();
  });
}

async function main() {
  if (!API_KEY) { console.error('ERROR: ELEVENLABS_API_KEY not set.'); process.exit(1); }
  if (!fs.existsSync(OUTPUT_DIR)) fs.mkdirSync(OUTPUT_DIR, { recursive: true });
  console.log(`Generating ${entries.length} audio files for Natalie Viegas (Aula 7)...\n`);
  for (let i = 0; i < entries.length; i++) { console.log(`[${i+1}/${entries.length}] ${entries[i].file}`); await generateAudio(entries[i]); await new Promise(r => setTimeout(r, 200)); }
  console.log('\nDone!');
}
main().catch(console.error);
