const fs = require('fs');
const path = require('path');
const API_KEY = process.env.ELEVENLABS_API_KEY;
const ELLEN_ID = 'BIvP0GN1cAtSRTxNHnWS';
const OUTPUT_DIR = path.join(__dirname, '..', 'public', 'audio', 'vanessa-maluf');

const ORDER_AUDIOS = [
  { file: 'order_l1_self_introduction.mp3', text: "Good morning, everyone. My name is Vanessa Maluf. I work for Braskem as a corporate lawyer. I handle contracts and compliance issues. Today, I'd like to clarify a few points about our new agreement." },
  { file: 'order_l2_meeting_sequence.mp3', text: "The chairperson sets the agenda and opens the meeting. Team members raise concerns about pending issues. The group discusses and defers non-urgent topics. Vanessa follows up on the contract review. Someone takes the minutes and the chairperson closes the meeting." },
  { file: 'order_l3_legal_presentation.mp3', text: "Good morning. I've worked in corporate law for eight years. Today, I'd like to put our position on the table. We need to enforce clause 7 of the binding agreement. The company's liability has been an issue since last quarter. I propose we draw up an amendment to resolve this dispute." },
  { file: 'order_l4_negotiation_strategy.mp3', text: "If the counterparty rejects our initial proposal, we stay calm. We propose a revised solution with adjusted terms. If they push back again, we escalate to senior management. If we can't reach an agreement, we go to arbitration. If they accept, we finalize the contract by the deadline." },
  { file: 'order_l5_assertive_communication.mp3', text: "Acknowledge the counterparty's concerns first. Articulate your position with an assertive tone. Convey your main point concisely. If they push back, propose an alternative solution. Take ownership of the outcome and follow up." }
];

async function generateAudio(text, outputPath) {
  const resp = await fetch(`https://api.elevenlabs.io/v1/text-to-speech/${ELLEN_ID}`, {
    method: 'POST',
    headers: { 'xi-api-key': API_KEY, 'Content-Type': 'application/json' },
    body: JSON.stringify({ text, model_id: 'eleven_monolingual_v1', voice_settings: { stability: 0.5, similarity_boost: 0.75, style: 0, use_speaker_boost: true } })
  });
  if (!resp.ok) throw new Error(`Error ${resp.status}: ${await resp.text()}`);
  const buffer = Buffer.from(await resp.arrayBuffer());
  fs.writeFileSync(outputPath, buffer);
  console.log(`Generated: ${path.basename(outputPath)} (${buffer.length} bytes)`);
}

async function main() {
  if (!API_KEY) { console.error('Set ELEVENLABS_API_KEY'); process.exit(1); }
  if (!fs.existsSync(OUTPUT_DIR)) fs.mkdirSync(OUTPUT_DIR, { recursive: true });
  for (const item of ORDER_AUDIOS) {
    const outPath = path.join(OUTPUT_DIR, item.file);
    if (fs.existsSync(outPath)) { console.log(`Skipping: ${item.file}`); continue; }
    await generateAudio(item.text, outPath);
    await new Promise(r => setTimeout(r, 1000));
  }
  console.log('\nDone!');
}
main().catch(console.error);
