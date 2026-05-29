const fs = require('fs');
const path = require('path');
const API_KEY = process.env.ELEVENLABS_API_KEY;
const ELLEN_ID = 'BIvP0GN1cAtSRTxNHnWS';
const OUTPUT_DIR = path.join(__dirname, '..', 'public', 'audio', 'patricia-ruffo');

const ORDER_AUDIOS = [
  { file: 'order_l1_self_introduction.mp3', text: "Good morning, everyone. Let me introduce myself. My name is Patricia Ruffo, and I am a clinical nutritionist. I am responsible for clinical research at Abbott. I have been collaborating with universities for over ten years. I am happy to answer any questions about my work." },
  { file: 'order_l2_debate.mp3', text: "I see your point, Dr. Santos. However, I would argue that we need more evidence. Based on the data, our current approach is showing progress. If we change the formula now, we will lose six months of data. I propose that we extend the trial for three more months." },
  { file: 'order_l3_conference_questions.mp3', text: "Thank you for your presentation, Dr. Nakamura. I have a question about your methodology. Could you elaborate on how you selected your sample? If you were to replicate this study, what would you change? What are the implications of your findings for clinical practice?" },
  { file: 'order_l4_project_update.mp3', text: "Good morning, everyone. I would like to update you on our project. Last month, we reached an important milestone. Dr. Nakamura reported that the preliminary results were significant. The next deliverable is due by December 15th. I will summarize the key points and send my feedback by the deadline." },
  { file: 'order_l5_summit_presentation.mp3', text: "Good morning, everyone. Welcome to the Abbott Science Summit. I would like to present our findings on glycemic control to the panel. My recommendation is that we reach a consensus on the methodology. Based on the evidence, my recommendation is to continue the current approach. I would like to thank the moderator and all the delegates for their feedback." }
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
