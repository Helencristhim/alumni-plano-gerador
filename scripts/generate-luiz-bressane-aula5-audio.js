const fs = require('fs');
const path = require('path');
const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const DIR = path.join(__dirname, '..', 'public', 'audio', 'luiz-bressane');

const PHRASES = [
  { text: "Transition", voice: ARTHUR, filename: "aula5_transition" },
  { text: "Adjust", voice: ARTHUR, filename: "aula5_adjust" },
  { text: "Cross-examination", voice: ARTHUR, filename: "aula5_cross_examination" },
  { text: "Closing Argument", voice: ARTHUR, filename: "aula5_closing_argument" },
  { text: "Jury Selection", voice: ARTHUR, filename: "aula5_jury_selection" },
  { text: "Evidence", voice: ARTHUR, filename: "aula5_evidence" },
  { text: "Caseload", voice: ARTHUR, filename: "aula5_caseload" },
  { text: "Focus On", voice: ARTHUR, filename: "aula5_focus_on" },

  { text: "I am transitioning back to criminal cases after ten years.", voice: ELLEN, filename: "aula5_i_am_transitioning_back" },
  { text: "I am adjusting to the pace of jury trials again.", voice: ARTHUR, filename: "aula5_i_am_adjusting_to_the_pace" },
  { text: "I am preparing for a cross-examination tomorrow.", voice: ELLEN, filename: "aula5_i_am_preparing_for_cross" },
  { text: "I am working on my closing argument for Friday.", voice: ARTHUR, filename: "aula5_i_am_working_on_closing" },
  { text: "We are going through jury selection this week.", voice: ELLEN, filename: "aula5_we_are_going_through_jury" },
  { text: "I am reviewing the evidence for the homicide case.", voice: ARTHUR, filename: "aula5_i_am_reviewing_the_evidence" },
  { text: "My caseload is increasing since I returned to criminal law.", voice: ELLEN, filename: "aula5_my_caseload_is_increasing" },
  { text: "Right now, I am focusing on jury trial preparation.", voice: ARTHUR, filename: "aula5_right_now_i_am_focusing" },

  { text: "I am currently handling three homicide cases.", voice: ELLEN, filename: "aula5_fill_handling" },
  { text: "I am getting back into jury trials after ten years.", voice: ARTHUR, filename: "aula5_fill_getting_back" },
  { text: "Right now, I am focusing on trial preparation.", voice: ELLEN, filename: "aula5_fill_focusing" },
  { text: "Things are changing. I am transitioning from administration.", voice: ARTHUR, filename: "aula5_fill_transitioning" },
  { text: "We are reviewing all the evidence before the trial.", voice: ELLEN, filename: "aula5_fill_reviewing" },
  { text: "My caseload is growing every month.", voice: ARTHUR, filename: "aula5_fill_caseload" },

  { text: "I am transitioning back to criminal law. Right now, I am handling three homicide cases.", voice: ARTHUR, filename: "aula5_pron_1" },
  { text: "I am adjusting to the pace. I am preparing for a cross-examination.", voice: ELLEN, filename: "aula5_pron_2" },
  { text: "We are going through jury selection. I am working on my closing argument.", voice: ARTHUR, filename: "aula5_pron_3" },

  { text: "Luiz! How are things? What are you working on these days?", voice: ARTHUR, filename: "aula5_dlg_david_1" },
  { text: "Things are changing a lot. I am transitioning back to criminal cases.", voice: ELLEN, filename: "aula5_dlg_luiz_1" },
  { text: "Really? What were you doing before?", voice: ARTHUR, filename: "aula5_dlg_david_2" },
  { text: "I was in administration for ten years. Now I am getting back into jury trials.", voice: ELLEN, filename: "aula5_dlg_luiz_2" },
  { text: "That is a big change! Are you adjusting well?", voice: ARTHUR, filename: "aula5_dlg_david_3" },
  { text: "I am adjusting to the pace. Right now, I am focusing on a homicide case.", voice: ELLEN, filename: "aula5_dlg_luiz_3" },
  { text: "What does your preparation look like?", voice: ARTHUR, filename: "aula5_dlg_david_4" },
  { text: "I am reviewing evidence and preparing for cross-examination. I am also working on my closing argument.", voice: ELLEN, filename: "aula5_dlg_luiz_4" },
  { text: "How is your caseload? Are you handling many cases?", voice: ARTHUR, filename: "aula5_dlg_david_5" },
  { text: "My caseload is growing. I am currently handling three cases, and we are going through jury selection for one of them.", voice: ELLEN, filename: "aula5_dlg_luiz_5" },

  { text: "I am transitioning back to criminal law.", voice: ARTHUR, filename: "aula5_surv_1" },
  { text: "I am currently handling three homicide cases.", voice: ELLEN, filename: "aula5_surv_2" },
  { text: "Right now, I am focusing on trial preparation.", voice: ARTHUR, filename: "aula5_surv_3" },
  { text: "I am reviewing evidence and preparing for cross-examination.", voice: ELLEN, filename: "aula5_surv_4" },
  { text: "My caseload is growing since I returned.", voice: ARTHUR, filename: "aula5_surv_5" },

  { text: "I work as a public defender.", voice: ARTHUR, filename: "aula5_gram_simple" },
  { text: "I am working on a homicide case right now.", voice: ELLEN, filename: "aula5_gram_continuous" },
  { text: "I live in Sao Paulo.", voice: ARTHUR, filename: "aula5_gram_simple2" },
  { text: "I am living between two cities at the moment.", voice: ELLEN, filename: "aula5_gram_continuous2" },

  { text: "I am currently handling three homicide cases.", voice: ARTHUR, filename: "aula5_expr_handling" },
  { text: "I am getting back into jury trials after ten years.", voice: ELLEN, filename: "aula5_expr_getting_back" },
  { text: "Right now, I am focusing on trial preparation.", voice: ARTHUR, filename: "aula5_expr_focusing" },
  { text: "Things are changing. I am transitioning from administration to criminal law.", voice: ELLEN, filename: "aula5_expr_transitioning" },

  { text: "I am a public defender in Sao Paulo and things are changing in my career. I am transitioning back to criminal cases after spending ten years in administration. Right now, I am focusing on jury trials. I am currently handling three homicide cases. I am adjusting to the fast pace of criminal court. This week, we are going through jury selection for one of my cases. I am also preparing for a cross-examination and working on my closing argument. My caseload is growing, but I am enjoying the challenge.", voice: ARTHUR, filename: "aula5_listening_1" },

  { text: "I am Rachel, a public defender in Chicago. I am currently handling about forty cases. Right now, I am focusing on two murder trials. I am preparing for jury selection next week. My caseload is very heavy, but I am getting better at managing my time. I am also working on a policy project about indigent defense reform.", voice: ELLEN, filename: "aula5_listening_2" },

  { text: "Things are changing in my career. I am transitioning back to criminal law. I am currently handling three cases. I am preparing for cross-examination. I am focusing on jury trial preparation.", voice: ARTHUR, filename: "aula5_order_l5" },
];

async function gen(text, voiceId, outPath) {
  const r = await fetch('https://api.elevenlabs.io/v1/text-to-speech/' + voiceId, {
    method: 'POST',
    headers: { 'xi-api-key': API_KEY, 'Content-Type': 'application/json' },
    body: JSON.stringify({ text, model_id: 'eleven_turbo_v2_5', voice_settings: { stability: 0.5, similarity_boost: 0.75 } }),
  });
  if (!r.ok) throw new Error(r.status + ': ' + (await r.text()));
  const buf = Buffer.from(await r.arrayBuffer());
  fs.writeFileSync(outPath, buf);
  return buf.length;
}

async function main() {
  if (!API_KEY) { console.error('Set ELEVENLABS_API_KEY env var'); process.exit(1); }
  if (!fs.existsSync(DIR)) fs.mkdirSync(DIR, { recursive: true });
  console.log('Generating ' + PHRASES.length + ' audio files for Aula 5...');
  for (const p of PHRASES) {
    const fname = p.filename + '.mp3';
    const outPath = path.join(DIR, fname);
    if (fs.existsSync(outPath)) { console.log('SKIP: ' + fname); }
    else {
      try {
        const bytes = await gen(p.text, p.voice, outPath);
        console.log('OK [' + (p.voice === ELLEN ? 'ellen' : 'arthur') + ']: ' + fname + ' (' + (bytes/1024).toFixed(1) + 'KB)');
        await new Promise(r => setTimeout(r, 500));
      } catch(e) { console.error('FAIL: ' + fname + ' -- ' + e.message); }
    }
  }
  console.log('\nDone! Total MP3s: ' + fs.readdirSync(DIR).filter(f => f.endsWith('.mp3')).length);
}
main().catch(e => { console.error(e); process.exit(1); });
