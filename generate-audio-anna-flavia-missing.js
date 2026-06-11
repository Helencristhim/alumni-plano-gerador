const fs = require('fs');
const path = require('path');
const https = require('https');
const ELEVENLABS_API_KEY = process.env.ELEVENLABS_API_KEY;
if (!ELEVENLABS_API_KEY) { console.error('ERROR: ELEVENLABS_API_KEY not set'); process.exit(1); }
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const OUTPUT_DIR = path.join(__dirname, 'public', 'audio', 'anna-flavia-miranda-da-silva');

const missing = [
  { text: "I ___ at six thirty every day.", file: "aula2_fill_wake.mp3", voice: ELLEN },
  { text: "I do not work on weekends.", file: "aula2_i_dont_work.mp3", voice: ARTHUR },
  { text: "She does not commute by bus.", file: "aula2_she_doesnt.mp3", voice: ELLEN },
  { text: "I do not work on weekends.", file: "aula2_surv_dont.mp3", voice: ARTHUR },
  { text: "Do you have a meeting today?", file: "aula2_surv_meeting.mp3", voice: ELLEN },
  { text: "What time do you leave the office?", file: "aula2_surv_whattime.mp3", voice: ARTHUR },
  { text: "There are not ___ windows in this room.", file: "aula3_fill_any.mp3", voice: ELLEN },
  { text: "There ___ two printers in the office.", file: "aula3_fill_are.mp3", voice: ARTHUR },
  { text: "___ there any folders on the shelf?", file: "aula3_fill_arethere.mp3", voice: ELLEN },
  { text: "There ___ a computer on my desk.", file: "aula3_fill_is.mp3", voice: ARTHUR },
  { text: "There ___ not a printer near my desk.", file: "aula3_fill_isnot.mp3", voice: ELLEN },
  { text: "___ there a whiteboard on the wall?", file: "aula3_fill_isthere.mp3", voice: ARTHUR },
  { text: "There are many folders on the shelf.", file: "aula3_there_are_folders.mp3", voice: ELLEN },
  { text: "There is a computer on my desk.", file: "aula3_there_is_computer.mp3", voice: ARTHUR },
  { text: "___ department is finance.", file: "aula4_fill_her.mp3", voice: ELLEN },
  { text: "___ name is Carlos. He is my colleague.", file: "aula4_fill_his.mp3", voice: ARTHUR },
  { text: "___ manager is very experienced.", file: "aula4_fill_my.mp3", voice: ELLEN },
  { text: "___ team is small but organized.", file: "aula4_fill_our.mp3", voice: ARTHUR },
  { text: "___ desks are on the third floor.", file: "aula4_fill_their.mp3", voice: ELLEN },
  { text: "___ office is on the third floor.", file: "aula4_fill_your.mp3", voice: ARTHUR },
  { text: "___ there any meeting rooms?", file: "aula5_fill_are.mp3", voice: ELLEN },
  { text: "She ___ not commute by bus.", file: "aula5_fill_does.mp3", voice: ARTHUR },
  { text: "___ name is Marina. She is friendly.", file: "aula5_fill_her.mp3", voice: ELLEN },
  { text: "There ___ a computer on my desk.", file: "aula5_fill_is.mp3", voice: ARTHUR },
  { text: "___ manager is Ricardo.", file: "aula5_fill_my.mp3", voice: ELLEN },
  { text: "I ___ at Usina Cururique in the financial area.", file: "aula5_fill_work.mp3", voice: ARTHUR },
  { text: "Our team has five people in the finance department.", file: "aula5_people_3.mp3", voice: ELLEN },
  { text: "I am available on Monday afternoon.", file: "aula6_available_monday.mp3", voice: ARTHUR },
  { text: "Could you confirm the meeting time?", file: "aula6_confirm_meeting.mp3", voice: ELLEN },
  { text: "Could you please send me the report?", file: "aula6_could_send.mp3", voice: ARTHUR },
  { text: "Please find the ___ below.", file: "aula6_fill_attachment.mp3", voice: ELLEN },
  { text: "I am ___ on Monday afternoon.", file: "aula6_fill_available.mp3", voice: ARTHUR },
  { text: "Could you ___ the meeting time?", file: "aula6_fill_confirm.mp3", voice: ELLEN },
  { text: "I will ___ to your email today.", file: "aula6_fill_reply.mp3", voice: ARTHUR },
  { text: "I am writing to ___ information.", file: "aula6_fill_request.mp3", voice: ELLEN },
  { text: "Could you please ___ me the report?", file: "aula6_fill_send.mp3", voice: ARTHUR },
  { text: "Please find the attachment below.", file: "aula6_please_find.mp3", voice: ELLEN },
  { text: "I work at Usina Cururique", file: "fill_i_work.mp3", voice: ARTHUR },
  { text: "I work at Usina Cururique.", file: "i_work_at_usina_cururique.mp3", voice: ELLEN },
  { text: "My name is Anna Flavia", file: "my_name_is_anna_flavia.mp3", voice: ARTHUR },
  { text: "She works in the financial area", file: "she_works_in_the_financial.mp3", voice: ELLEN },
  { text: "We export sugar", file: "we_export_sugar_short.mp3", voice: ARTHUR },
];

function generateAudio(text, voiceId, outputPath) {
  return new Promise((resolve, reject) => {
    const postData = JSON.stringify({ text, model_id: 'eleven_multilingual_v2', voice_settings: { stability: 0.5, similarity_boost: 0.75 } });
    const options = { hostname: 'api.elevenlabs.io', path: '/v1/text-to-speech/' + voiceId + '?output_format=mp3_44100_128', method: 'POST', headers: { 'Content-Type': 'application/json', 'xi-api-key': ELEVENLABS_API_KEY, 'Content-Length': Buffer.byteLength(postData) } };
    const req = https.request(options, (res) => { if (res.statusCode !== 200) { let b = ''; res.on('data', d => b += d); res.on('end', () => reject(new Error('API ' + res.statusCode + ': ' + b))); return; } const chunks = []; res.on('data', c => chunks.push(c)); res.on('end', () => { fs.writeFileSync(outputPath, Buffer.concat(chunks)); resolve(); }); });
    req.on('error', reject); req.write(postData); req.end();
  });
}

async function main() {
  console.log('Generating ' + missing.length + ' missing audio files...');
  let gen = 0;
  for (let i = 0; i < missing.length; i++) {
    const { text, file, voice } = missing[i];
    const out = path.join(OUTPUT_DIR, file);
    if (fs.existsSync(out) && fs.statSync(out).size > 1000) { continue; }
    try {
      await generateAudio(text, voice, out);
      gen++;
      console.log('Generated ' + gen + '/' + missing.length + ': ' + file);
    } catch (err) { console.error('FAILED ' + file + ': ' + err.message); }
    if (i < missing.length - 1) await new Promise(r => setTimeout(r, 500));
  }
  console.log('Done! Generated: ' + gen);
}
main().catch(console.error);
