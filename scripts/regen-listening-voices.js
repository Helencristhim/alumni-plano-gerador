#!/usr/bin/env node
const fs = require('fs');
const path = require('path');
const https = require('https');
const API_KEY = process.env.ELEVENLABS_API_KEY;
const DIR = path.join(__dirname, '..', 'public', 'audio', 'nilo-mesquita-patucci');

// Character-specific voices
const ERIC = 'cjVigY5qzO86Huf0OWal';      // American male, smooth trustworthy (James Mitchell)
const ALICE = 'Xb7hH8MSUJpSbSDYk0k2';     // British female, educator (Dr. Eleanor Hughes)
const MALENA = '1WXz8v08ntDcSTeVXMN2';     // Argentine female (Dr. Maria Fernandez)
const DANIEL = 'onwK4e9ZLuTAKqWW03F9';     // British male, broadcaster (Hans Weber - European)
const ETIENNE = 'JoZRi9NbCIuCH6R6e2Mt';    // South African male (Kwame Asante)

const entries = [
  ["Good evening, everyone, and welcome to the FIFA Leadership in Football program. Over the next three days, you will meet delegates from over thirty countries. Each of you has been selected because of your unique contribution to football governance in your country. Our goal is simple: to share best practices, build lasting relationships, and return home with concrete tools to improve governance in your federations. Tomorrow morning, we start with a panel on anti-corruption. I encourage you to participate actively. This is your program.", "listening_lab_1_welcome.mp3", ERIC],

  ["Thank you for having me. My research over the past decade has focused on governance structures in European football. What we have found is quite striking: clubs with strong compliance departments report forty percent fewer regulatory violations. The key factor is not the size of the department, but the independence of the compliance officer. When the compliance officer reports directly to the board, rather than to management, the results are significantly better. I would be happy to share our full report with anyone interested.", "listening_lab_2_research.mp3", ALICE],

  ["Nilo, it is wonderful to meet you. I have heard about the work Corinthians is doing in compliance. In Argentina, we are facing similar challenges. Our biggest issue right now is match-fixing investigations. We have a team of twelve people, but we struggle with coordination between the national federation and the provincial associations. How does your department handle coordination with the Brazilian Football Confederation? I would love to learn from your experience.", "listening_lab_3_argentina.mp3", MALENA],

  ["Colleagues, I would like to draw your attention to the latest FIFA regulatory framework update. As of January, all member associations must implement enhanced due diligence procedures for player transfers. This includes financial background checks, source of funds verification, and conflict of interest declarations. The deadline for implementation is December thirty-first. If your association has not yet started the implementation process, I strongly recommend you begin immediately. We at the Swiss Football League completed our implementation six months ahead of schedule, and I am available to share our methodology.", "listening_lab_4_swiss.mp3", DANIEL],

  ["I want to share a story from Ghana. Three years ago, we had almost no compliance infrastructure. Match-fixing was a serious problem, and public trust in football was very low. We started by hiring five dedicated compliance officers and training them at FIFA headquarters in Zurich. We then implemented a whistleblower hotline and anonymous reporting system. Today, we have investigated over fifty cases and achieved twelve successful prosecutions. The key lesson for all of us is this: compliance is not a cost. It is an investment in the future of football.", "listening_lab_5_ghana.mp3", ETIENNE],
];

function gen(text, filename, voiceId) {
  return new Promise((resolve, reject) => {
    const fp = path.join(DIR, filename);
    // Force regenerate (overwrite existing)
    const body = JSON.stringify({ text, model_id: 'eleven_turbo_v2_5', voice_settings: { stability: 0.5, similarity_boost: 0.75 } });
    const opts = { hostname: 'api.elevenlabs.io', path: `/v1/text-to-speech/${voiceId}`, method: 'POST', headers: { 'xi-api-key': API_KEY, 'Content-Type': 'application/json', 'Accept': 'audio/mpeg', 'Content-Length': Buffer.byteLength(body) } };
    const req = https.request(opts, res => {
      if (res.statusCode !== 200) { let e=''; res.on('data',d=>e+=d); res.on('end',()=>{ console.error('  ERR',res.statusCode,filename,e.substring(0,200)); reject(new Error('HTTP '+res.statusCode)); }); return; }
      const chunks = []; res.on('data', c => chunks.push(c)); res.on('end', () => { const buf = Buffer.concat(chunks); fs.writeFileSync(fp, buf); console.log('  OK:', filename, '(' + buf.length + ' bytes)'); resolve(); });
    });
    req.on('error', reject); req.write(body); req.end();
  });
}

async function main() {
  console.log('Regenerating 5 listening lab audios with character-specific voices...');
  console.log('  Ex1: Eric (American male) for James Mitchell');
  console.log('  Ex2: Alice (British female) for Dr. Eleanor Hughes');
  console.log('  Ex3: Malena (Argentine female) for Dr. Maria Fernandez');
  console.log('  Ex4: Daniel (British male) for Hans Weber');
  console.log('  Ex5: Etienne (South African male) for Kwame Asante');
  console.log('');
  let ok=0, err=0;
  for (let i=0; i<entries.length; i++) {
    try { await gen(entries[i][0], entries[i][1], entries[i][2]); ok++; if(i<entries.length-1) await new Promise(r=>setTimeout(r,200)); }
    catch(e) { err++; }
  }
  console.log(`\nDone: ${ok} OK, ${err} errors`);
}
main().catch(console.error);
