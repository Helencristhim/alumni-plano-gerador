const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR_ID = 'sfJopaWaOtauCD3HKX6Q'; // Arthur - Casual Conversational American Male

const OUTPUT_DIR = path.join(__dirname, '..', 'public', 'audio', 'milton-sayegh');

const ORDER_AUDIOS = [
  {
    file: 'order_l1_self_introduction.mp3',
    text: 'Good morning. My name is Milton Sayegh. I am from São Paulo, Brazil. I run a luxury jewelry export company. We operate in the United States and Brazil. It is a pleasure to meet you.'
  },
  {
    file: 'order_l2_company_profile.mp3',
    text: 'Our company specializes in premium Brazilian gemstones. We do not sell directly to consumers — we work through wholesale partners. We work with distributors in the United States. Our supply chain covers everything from sourcing to delivery. I would like to discuss a possible partnership.'
  },
  {
    file: 'order_l3_trade_show.mp3',
    text: 'Excuse me, are you exhibiting Brazilian jewelry? I am looking for luxury jewelry suppliers for our stores. We are showcasing our latest collection today. I like your pitch. Do you have a business card? Could I schedule a follow-up call next week?'
  },
  {
    file: 'order_l4_negotiation.mp3',
    text: 'Thank you for the proposal. I would like to discuss the pricing. Could you offer a discount for larger volumes? I could consider a 5% discount for that volume. Could we also discuss the delivery deadline? Should we put this in writing?'
  },
  {
    file: 'order_l5_board_meeting.mp3',
    text: 'Good evening, everyone. I am calling this meeting to order. Has everyone received the minutes from the last meeting? I would like to make a motion regarding the assessment fees. Maintenance costs have increased by 15% this year. Shall we vote on a resolution to approve the revised budget?'
  }
];

async function generateAudio(text, outputPath) {
  const resp = await fetch(`https://api.elevenlabs.io/v1/text-to-speech/${ARTHUR_ID}`, {
    method: 'POST',
    headers: { 'xi-api-key': API_KEY, 'Content-Type': 'application/json' },
    body: JSON.stringify({
      text: text,
      model_id: 'eleven_monolingual_v1',
      voice_settings: { stability: 0.5, similarity_boost: 0.75, style: 0, use_speaker_boost: true }
    })
  });
  if (!resp.ok) {
    const err = await resp.text();
    throw new Error(`ElevenLabs error for ${path.basename(outputPath)}: ${resp.status} — ${err}`);
  }
  const buffer = Buffer.from(await resp.arrayBuffer());
  fs.writeFileSync(outputPath, buffer);
  console.log(`Generated: ${path.basename(outputPath)} (${buffer.length} bytes)`);
}

async function main() {
  if (!API_KEY) { console.error('Set ELEVENLABS_API_KEY'); process.exit(1); }
  if (!fs.existsSync(OUTPUT_DIR)) fs.mkdirSync(OUTPUT_DIR, { recursive: true });
  for (const item of ORDER_AUDIOS) {
    const outPath = path.join(OUTPUT_DIR, item.file);
    if (fs.existsSync(outPath)) { console.log(`Skipping (exists): ${item.file}`); continue; }
    await generateAudio(item.text, outPath);
    await new Promise(r => setTimeout(r, 1000));
  }
  console.log('\nDone! All order audios generated.');
}

main().catch(console.error);
