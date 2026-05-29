const fs = require('fs');
const path = require('path');
const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const DIR = path.join(__dirname, '..', 'public', 'audio', 'percival-jr-aula5');

const PHRASES = [
  { text: "Could you repeat that, please?", voice: ARTHUR },
  { text: "I am not sure I understand.", voice: ELLEN },
  { text: "We are currently dealing with a compliance issue.", voice: ARTHUR },
  { text: "The main challenge right now is the tight deadline.", voice: ELLEN },
  { text: "Back to square one.", voice: ARTHUR },
  { text: "Priority", voice: ARTHUR },
  { text: "Issue", voice: ARTHUR },
  { text: "Update", voice: ARTHUR },
  { text: "Delay", voice: ARTHUR },
  { text: "However", voice: ARTHUR },
  { text: "In addition", voice: ARTHUR },
  { text: "Therefore", voice: ARTHUR },
  { text: "Furthermore", voice: ARTHUR },
  { text: "Compliance is our top priority right now.", voice: ARTHUR },
  { text: "We are dealing with a compliance issue.", voice: ELLEN },
  { text: "I need to provide an update to the board.", voice: ARTHUR },
  { text: "We are facing a delay in the audit.", voice: ELLEN },
  { text: "The project is on track. However, we need more time.", voice: ARTHUR },
  { text: "In addition, we are reviewing the risk matrix.", voice: ELLEN },
  { text: "The deadline changed. Therefore, we need a new action plan.", voice: ARTHUR },
  { text: "Furthermore, the stakeholders requested an extra review.", voice: ELLEN },
  { text: "First of all, we identified the issue.", voice: ARTHUR },
  { text: "Then, we developed an action plan.", voice: ELLEN },
  { text: "Finally, we presented the update to the board.", voice: ARTHUR },
  { text: "We found a problem in the audit. That is why we decided to start over.", voice: ELLEN },
  { text: "The compliance review is taking longer than expected. However, the team is making progress.", voice: ARTHUR },
  { text: "We met the deadline. In addition, we improved the process.", voice: ELLEN },
  { text: "Hi Percival! Can you give us an update on the audit project?", voice: ELLEN },
  { text: "Of course. First of all, we identified a compliance issue in the operations department.", voice: ARTHUR },
  { text: "What did you do about it?", voice: ELLEN },
  { text: "We developed an action plan. However, we are facing a delay because the stakeholders need more time to review the documents.", voice: ARTHUR },
  { text: "Is the project still on track?", voice: ELLEN },
  { text: "Yes, it is. The deadline is next month. Therefore, compliance is our top priority right now. In addition, I am preparing a full update for the executive board.", voice: ARTHUR },
  { text: "Any other challenges?", voice: ELLEN },
  { text: "We had to go back to square one on one part of the review. Furthermore, we discovered a new issue that requires attention. But overall, my team is handling it well.", voice: ARTHUR },
  { text: "This month, my team is conducting a full compliance review. First of all, we identified several issues in the operations department. Then, we developed an action plan. However, we are facing a delay because the stakeholders requested additional documentation. Therefore, compliance is our top priority right now. In addition, I am preparing an update for the executive board. Furthermore, we discovered a new risk that requires immediate attention.", voice: ARTHUR },
  { text: "What are your main priorities this month?", voice: ELLEN },
  { text: "My main priority is completing the compliance review on time.", voice: ARTHUR },
  { text: "Are you facing any delays?", voice: ELLEN },
  { text: "Yes, we are facing a delay. However, we are working hard to meet the deadline.", voice: ARTHUR },
];

function toFilename(t) { return t.toLowerCase().replace(/[^a-z0-9 ]/g,'').replace(/ +/g,'_').substring(0,60); }
async function gen(text, voiceId, outPath) {
  const r = await fetch('https://api.elevenlabs.io/v1/text-to-speech/'+voiceId,{method:'POST',headers:{'xi-api-key':API_KEY,'Content-Type':'application/json'},body:JSON.stringify({text,model_id:'eleven_turbo_v2_5',voice_settings:{stability:0.5,similarity_boost:0.75}})});
  if(!r.ok) throw new Error(r.status+': '+(await r.text()));
  const buf=Buffer.from(await r.arrayBuffer()); fs.writeFileSync(outPath,buf); return buf.length;
}
async function main() {
  if(!API_KEY){console.error('Set ELEVENLABS_API_KEY');process.exit(1);}
  if(!fs.existsSync(DIR)) fs.mkdirSync(DIR,{recursive:true});
  const seen=new Set(); const unique=PHRASES.filter(p=>{const k=p.text.toLowerCase();if(seen.has(k))return false;seen.add(k);return true;});
  console.log('Generating '+unique.length+' audio files for Percival JR — Aula 5...');
  for(const p of unique){
    const fname=toFilename(p.text)+'.mp3'; const outPath=path.join(DIR,fname);
    if(fs.existsSync(outPath)){console.log('SKIP: '+fname);}
    else{try{const bytes=await gen(p.text,p.voice,outPath);console.log('OK ['+(p.voice===ELLEN?'ellen':'arthur')+']: '+fname+' ('+(bytes/1024).toFixed(1)+'KB)');await new Promise(r=>setTimeout(r,500));}catch(e){console.error('FAIL: '+fname+' — '+e.message);}}
  }
  console.log('\nDone! Generated '+unique.length+' entries.');
}
main().catch(e=>{console.error(e);process.exit(1);});
