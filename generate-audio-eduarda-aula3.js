const fs = require('fs');
const path = require('path');
const https = require('https');
const ELEVENLABS_API_KEY = process.env.ELEVENLABS_API_KEY;
if (!ELEVENLABS_API_KEY) { console.error('ERROR: ELEVENLABS_API_KEY not set'); process.exit(1); }
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const OUTPUT_DIR = path.join(__dirname, 'public', 'audio', 'eduarda-gabriel');
const audioMap = {
  "Revenue": "aula3_revenue.mp3",
  "Decline": "aula3_decline.mp3",
  "Estimate": "aula3_estimate.mp3",
  "Forecast": "aula3_forecast.mp3",
  "Leverage": "aula3_leverage.mp3",
  "Margin": "aula3_margin.mp3",
  "Quarter": "aula3_quarter.mp3",
  "Benchmark": "aula3_benchmark.mp3",
  "Houlihan Lokey's restructuring revenue grew by twelve percent this year.": "aula3_ex_revenue.mp3",
  "The company's revenue declined by eight percent in Q2.": "aula3_ex_decline.mp3",
  "We estimate the deal value at approximately two hundred million dollars.": "aula3_ex_estimate.mp3",
  "The forecast shows a recovery in the second half of the year.": "aula3_ex_forecast.mp3",
  "The company's leverage ratio is higher than the industry benchmark.": "aula3_ex_leverage.mp3",
  "The operating margin improved from fifteen to twenty percent.": "aula3_ex_margin.mp3",
  "Revenue in the third quarter exceeded our forecast.": "aula3_ex_quarter.mp3",
  "We use industry benchmarks to evaluate the deal.": "aula3_ex_benchmark.mp3",
  "Revenue declined by eight percent in the third quarter.": "aula3_fill1.mp3",
  "We estimate the deal value at approximately two hundred million dollars.": "aula3_fill2.mp3",
  "The forecast shows a recovery in Q4.": "aula3_fill3.mp3",
  "The operating margin improved from fifteen to twenty percent.": "aula3_fill4.mp3",
  "Compared to the industry benchmark, our leverage is higher.": "aula3_fill5.mp3",
  "Revenue in the third quarter exceeded our forecast.": "aula3_fill6.mp3",
  "Revenue declined by eight percent in the third quarter.": "aula3_pron1.mp3",
  "We estimate the deal value at approximately two hundred million dollars.": "aula3_pron2.mp3",
  "Compared to the industry benchmark, our margin improved significantly.": "aula3_pron3.mp3",
  "Eduarda, could you walk us through the Q3 numbers?": "aula3_dial1.mp3",
  "Of course. Revenue in the third quarter was approximately one hundred and fifty million.": "aula3_dial2.mp3",
  "How does that compare to Q2?": "aula3_dial3.mp3",
  "Compared to Q2, revenue declined by eight percent. However, the operating margin improved.": "aula3_dial4.mp3",
  "What is the margin now?": "aula3_dial5.mp3",
  "The margin increased from fifteen to twenty percent. That is higher than the industry benchmark.": "aula3_dial6.mp3",
  "And the forecast for Q4?": "aula3_dial7.mp3",
  "We estimate a recovery. The forecast shows revenue growing by approximately five percent.": "aula3_dial8.mp3",
  "Revenue increased by fifteen percent in Q3.": "aula3_surv1.mp3",
  "Compared to last quarter, the margin is higher.": "aula3_surv2.mp3",
  "We estimate the deal value at approximately two hundred million.": "aula3_surv3.mp3",
  "The forecast shows a decline in the second half.": "aula3_surv4.mp3",
  "Let me walk you through the numbers.": "aula3_surv5.mp3",
  "[order-l3]": "aula3_order_l3.mp3",
  "One hundred and fifty million dollars, or one-five-zero million.": "aula3_oral1.mp3",
  "Revenue declined by ten percent, or twenty million dollars.": "aula3_oral2.mp3",
  "The margin increased by five percentage points, from fifteen to twenty percent.": "aula3_oral3.mp3",
  "Compared to Q2, Q3 revenue was lower. It declined by approximately seventeen percent.": "aula3_oral4.mp3",
  "We estimate the deal value at approximately two hundred million dollars.": "aula3_oral5.mp3",
  "The forecast shows revenue growing by approximately five percent in Q4.": "aula3_oral6.mp3"
};
const jamesLines = ["Eduarda, could you walk us through the Q3 numbers?","How does that compare to Q2?","What is the margin now?","And the forecast for Q4?"];
const eduardaLines = ["Of course. Revenue in the third quarter was approximately one hundred and fifty million.","Compared to Q2, revenue declined by eight percent. However, the operating margin improved.","The margin increased from fifteen to twenty percent. That is higher than the industry benchmark.","We estimate a recovery. The forecast shows revenue growing by approximately five percent."];
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
    const options = { hostname: 'api.elevenlabs.io', path: '/v1/text-to-speech/' + voiceId + '?output_format=mp3_44100_128', method: 'POST', headers: { 'Content-Type': 'application/json', 'xi-api-key': ELEVENLABS_API_KEY, 'Content-Length': Buffer.byteLength(postData) } };
    const req = https.request(options, (res) => {
      if (res.statusCode !== 200) { let b=''; res.on('data',d=>b+=d); res.on('end',()=>reject(new Error('API '+res.statusCode+': '+b))); return; }
      const chunks = []; res.on('data',c=>chunks.push(c)); res.on('end',()=>{ fs.writeFileSync(outputPath, Buffer.concat(chunks)); resolve(); });
    });
    req.on('error', reject); req.write(postData); req.end();
  });
}
async function main() {
  const entries = Object.entries(audioMap);
  let gen=0, skip=0;
  console.log('Generating '+entries.length+' Aula 3 audio files...');
  for (let i=0; i<entries.length; i++) {
    const [text, file] = entries[i];
    const out = path.join(OUTPUT_DIR, file);
    if (fs.existsSync(out) && fs.statSync(out).size>1000) { skip++; if(countWords(text)>2&&!jamesLines.includes(text)&&!eduardaLines.includes(text))alt++; continue; }
    const voice = getVoice(text);
    try { await generateAudio(text, voice.id, out); gen++; console.log('Generated '+(gen+skip)+'/'+entries.length+': '+file+' ('+voice.name+')'); }
    catch(err) { console.error('FAILED '+file+': '+err.message); }
    if (i<entries.length-1) await new Promise(r=>setTimeout(r,500));
  }
  console.log('Done! Generated: '+gen+', Skipped: '+skip);
}
main().catch(console.error);
