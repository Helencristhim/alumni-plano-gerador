const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const DIR = path.join(__dirname, '..', 'public', 'audio', 'luiz-bressane');

const PHRASES = [
  // === VOCAB WORDS (Arthur) ===
  { text: "Schedule", voice: ARTHUR, filename: "aula2_schedule" },
  { text: "Routine", voice: ARTHUR, filename: "aula2_routine" },
  { text: "Split", voice: ARTHUR, filename: "aula2_split" },
  { text: "Flight", voice: ARTHUR, filename: "aula2_flight" },
  { text: "Overnight", voice: ARTHUR, filename: "aula2_overnight" },
  { text: "Neighborhood", voice: ARTHUR, filename: "aula2_neighborhood" },
  { text: "Handle", voice: ARTHUR, filename: "aula2_handle" },
  { text: "Colleague", voice: ARTHUR, filename: "aula2_colleague" },

  // === VOCAB EXAMPLE PHRASES (alternate) ===
  { text: "I have a busy schedule during the week.", voice: ELLEN, filename: "aula2_i_have_a_busy_schedule_during_the_week" },
  { text: "My morning routine starts at five thirty.", voice: ARTHUR, filename: "aula2_my_morning_routine_starts_at_five_thirty" },
  { text: "I split my time between Sao Paulo and Rio.", voice: ELLEN, filename: "aula2_i_split_my_time_between_sao_paulo_and_rio" },
  { text: "I take the flight to Rio every Friday.", voice: ARTHUR, filename: "aula2_i_take_the_flight_to_rio_every_friday" },
  { text: "I stay overnight in Sao Paulo on Tuesdays.", voice: ELLEN, filename: "aula2_i_stay_overnight_in_sao_paulo_on_tuesdays" },
  { text: "Barra Funda is a busy neighborhood.", voice: ARTHUR, filename: "aula2_barra_funda_is_a_busy_neighborhood" },
  { text: "I handle criminal cases at the courthouse.", voice: ELLEN, filename: "aula2_i_handle_criminal_cases_at_the_courthouse" },
  { text: "My colleague and I work on the same cases.", voice: ARTHUR, filename: "aula2_my_colleague_and_i_work_on_the_same_cases" },

  // === FILL-IN PHRASES (alternate) ===
  { text: "I always wake up early. My routine starts at five thirty.", voice: ELLEN, filename: "aula2_i_always_wake_up_early_my_routine" },
  { text: "I split my time between two cities every week.", voice: ARTHUR, filename: "aula2_i_split_my_time_between_two_cities" },
  { text: "I usually take the Friday flight to Rio de Janeiro.", voice: ELLEN, filename: "aula2_i_usually_take_the_friday_flight" },
  { text: "My schedule is very busy during the week.", voice: ARTHUR, filename: "aula2_my_schedule_is_very_busy" },
  { text: "I sometimes stay overnight when I have a long trial.", voice: ELLEN, filename: "aula2_i_sometimes_stay_overnight" },
  { text: "My colleague handles different cases at the courthouse.", voice: ARTHUR, filename: "aula2_my_colleague_handles_different_cases" },

  // === PRONUNCIATION PHRASES ===
  { text: "I split my time between Sao Paulo and Rio de Janeiro every week.", voice: ARTHUR, filename: "aula2_pron_i_split_my_time" },
  { text: "During the week, I usually handle criminal cases at the courthouse.", voice: ELLEN, filename: "aula2_pron_during_the_week" },
  { text: "On weekends, I spend most of my time with my family in Rio.", voice: ARTHUR, filename: "aula2_pron_on_weekends" },

  // === DIALOGUE LINES (Sarah=Ellen, Luiz=Arthur alternating) ===
  { text: "So, Luiz, where are you based? Sao Paulo or Rio?", voice: ELLEN, filename: "aula2_dlg_sarah_1" },
  { text: "I split my time between both cities. During the week, I work in Sao Paulo.", voice: ARTHUR, filename: "aula2_dlg_luiz_1" },
  { text: "That must be challenging. How often do you fly?", voice: ELLEN, filename: "aula2_dlg_sarah_2" },
  { text: "I usually take the flight to Rio every Friday. I stay overnight on Thursdays sometimes.", voice: ARTHUR, filename: "aula2_dlg_luiz_2" },
  { text: "What is your daily routine like in Sao Paulo?", voice: ELLEN, filename: "aula2_dlg_sarah_3" },
  { text: "I always wake up early. My morning routine starts at five thirty with exercise.", voice: ARTHUR, filename: "aula2_dlg_luiz_3" },
  { text: "And at work? What does a typical day look like?", voice: ELLEN, filename: "aula2_dlg_sarah_4" },
  { text: "I handle criminal cases at the courthouse. I spend most of my time preparing for trials.", voice: ARTHUR, filename: "aula2_dlg_luiz_4" },
  { text: "Do you have colleagues who also commute between cities?", voice: ELLEN, filename: "aula2_dlg_sarah_5" },
  { text: "Not many. My schedule is unusual, but I manage. On weekends, I usually spend time with my daughter in Rio.", voice: ARTHUR, filename: "aula2_dlg_luiz_5" },

  // === SURVIVAL CARD PHRASES ===
  { text: "I split my time between Sao Paulo and Rio de Janeiro.", voice: ARTHUR, filename: "aula2_surv_1" },
  { text: "During the week, I work at the Criminal Court.", voice: ELLEN, filename: "aula2_surv_2" },
  { text: "I usually take the flight to Rio on Fridays.", voice: ARTHUR, filename: "aula2_surv_3" },
  { text: "My schedule is busy, but I manage.", voice: ELLEN, filename: "aula2_surv_4" },
  { text: "On weekends, I spend time with my family.", voice: ARTHUR, filename: "aula2_surv_5" },

  // === GRAMMAR EXAMPLES ===
  { text: "Luiz always wakes up early.", voice: ARTHUR, filename: "aula2_gram_always" },
  { text: "He usually takes the flight on Fridays.", voice: ELLEN, filename: "aula2_gram_usually" },
  { text: "He sometimes stays overnight in Sao Paulo.", voice: ARTHUR, filename: "aula2_gram_sometimes" },
  { text: "He never works on Sundays.", voice: ELLEN, filename: "aula2_gram_never" },

  // === LISTENING 1 (long passage) ===
  { text: "My name is Luiz Bressane and I live in two cities. During the week, I work in Sao Paulo at the Criminal Court in Barra Funda. I usually arrive at the courthouse around eight in the morning. I always handle serious criminal cases, including jury trials. My schedule is very busy. I sometimes stay overnight when a trial runs late. On Fridays, I usually take the flight to Rio de Janeiro, where my family lives. On weekends, I spend time with my wife and my daughter. My morning routine always starts at five thirty with exercise. I rarely skip my workout.", voice: ARTHUR, filename: "aula2_listening_1" },

  // === ORDER EXERCISE ===
  { text: "During the week, I work in Sao Paulo. I usually arrive at the courthouse at eight. I handle criminal cases all day. On Fridays, I take the flight to Rio. On weekends, I spend time with my family.", voice: ARTHUR, filename: "aula2_order_l2" },

  // === EXPRESSIONS ===
  { text: "During the week, I work at the Criminal Court.", voice: ELLEN, filename: "aula2_expr_during" },
  { text: "On weekends, I usually spend time with my family.", voice: ARTHUR, filename: "aula2_expr_weekends" },
  { text: "I spend most of my time preparing for trials.", voice: ELLEN, filename: "aula2_expr_spend" },
  { text: "I travel back and forth between Sao Paulo and Rio.", voice: ARTHUR, filename: "aula2_expr_back_and_forth" },
];

function toFilename(text) {
  return text.toLowerCase().replace(/[^a-z0-9 ]/g, '').replace(/ +/g, '_').substring(0, 60);
}

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

  console.log('Generating ' + PHRASES.length + ' audio files for Luiz Bressane Aula 2...');
  for (const p of PHRASES) {
    const fname = (p.filename || toFilename(p.text)) + '.mp3';
    const outPath = path.join(DIR, fname);
    if (fs.existsSync(outPath)) {
      console.log('SKIP: ' + fname);
    } else {
      try {
        const bytes = await gen(p.text, p.voice, outPath);
        console.log('OK [' + (p.voice === ELLEN ? 'ellen' : 'arthur') + ']: ' + fname + ' (' + (bytes/1024).toFixed(1) + 'KB)');
        await new Promise(r => setTimeout(r, 500));
      } catch(e) { console.error('FAIL: ' + fname + ' -- ' + e.message); }
    }
  }
  console.log('\nDone! Aula 2 audio generation complete.');
  console.log('Total audio files in directory: ' + fs.readdirSync(DIR).filter(f => f.endsWith('.mp3')).length);
}

main().catch(e => { console.error(e); process.exit(1); });
