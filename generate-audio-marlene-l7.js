const fs = require('fs');
const path = require('path');
const https = require('https');
const API_KEY = process.env.ELEVENLABS_API_KEY;
if (!API_KEY) { console.error('ERROR: Set ELEVENLABS_API_KEY'); process.exit(1); }
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const BASE_DIR = '/Users/helenmendes/alumni-plano-gerador/public';

const audioMap = {
  "Seatbelt": "/audio/marlene-landucci/seatbelt.mp3",
  "Overhead": "/audio/marlene-landucci/overhead.mp3",
  "Tray table": "/audio/marlene-landucci/tray_table.mp3",
  "Blanket": "/audio/marlene-landucci/blanket.mp3",
  "Turbulence": "/audio/marlene-landucci/turbulence.mp3",
  "Landing": "/audio/marlene-landucci/landing.mp3",
  "Snack": "/audio/marlene-landucci/snack.mp3",
  "Headphones": "/audio/marlene-landucci/headphones.mp3",
  "Please fasten your seatbelt.": "/audio/marlene-landucci/please_fasten_your_seatbelt.mp3",
  "Could you put your bag in the overhead compartment?": "/audio/marlene-landucci/could_you_put_your_bag_in_the_overhead.mp3",
  "Can I have a blanket, please?": "/audio/marlene-landucci/can_i_have_a_blanket_please.mp3",
  "Could you open the tray table?": "/audio/marlene-landucci/could_you_open_the_tray_table.mp3",
  "We are experiencing some turbulence.": "/audio/marlene-landucci/we_are_experiencing_some_turbulence.mp3",
  "We will be landing in thirty minutes.": "/audio/marlene-landucci/we_will_be_landing_in_thirty_minutes.mp3",
  "Can I have a snack, please?": "/audio/marlene-landucci/can_i_have_a_snack_please.mp3",
  "Could I have some headphones?": "/audio/marlene-landucci/could_i_have_some_headphones.mp3",
  "Excuse me, can I have some water?": "/audio/marlene-landucci/excuse_me_can_i_have_some_water.mp3",
  "Of course. Here you go.": "/audio/marlene-landucci/of_course_here_you_go.mp3",
  "Could I have a coffee and a snack, please?": "/audio/marlene-landucci/could_i_have_a_coffee_and_a_snack.mp3",
  "Sure. Would you like milk or sugar?": "/audio/marlene-landucci/sure_would_you_like_milk_or_sugar.mp3",
  "Just milk, please. No sugar.": "/audio/marlene-landucci/just_milk_please_no_sugar.mp3",
  "Could you help me with my bag? It is very heavy.": "/audio/marlene-landucci/could_you_help_me_with_my_bag.mp3",
  "No problem. I will put it in the overhead compartment.": "/audio/marlene-landucci/no_problem_i_will_put_it_in_the_overhead.mp3",
  "Thank you so much!": "/audio/marlene-landucci/thank_you_so_much.mp3",
  "[order-l7]": "/audio/marlene-landucci/order_l7_ordering.mp3",
  "[lp-listen-l7-1]": "/audio/marlene-landucci/lp_listen_l7_1_safety_announcement.mp3",
  "[lp-listen-l7-2]": "/audio/marlene-landucci/lp_listen_l7_2_meal_service.mp3",
  "Can I have an extra pillow?": "/audio/marlene-landucci/can_i_have_an_extra_pillow.mp3",
  "Could you turn off the light, please?": "/audio/marlene-landucci/could_you_turn_off_the_light_please.mp3"
};

const ellenPhrases = new Set([
  "Can I have a blanket, please?", "Could I have some headphones?",
  "Can I have a snack, please?", "Excuse me, can I have some water?",
  "Could I have a coffee and a snack, please?", "Just milk, please. No sugar.",
  "Could you help me with my bag? It is very heavy.", "Thank you so much!",
  "Can I have an extra pillow?", "Could you turn off the light, please?",
  "[order-l7]", "[lp-listen-l7-1]",
]);
const arthurPhrases = new Set([
  "Please fasten your seatbelt.", "Could you put your bag in the overhead compartment?",
  "We are experiencing some turbulence.", "We will be landing in thirty minutes.",
  "Of course. Here you go.", "Sure. Would you like milk or sugar?",
  "No problem. I will put it in the overhead compartment.",
]);

let alt = false;
function getVoice(t) {
  if (t.trim().split(/\s+/).length <= 2) return { id: ELLEN, name: 'Ellen' };
  if (ellenPhrases.has(t)) return { id: ELLEN, name: 'Ellen' };
  if (arthurPhrases.has(t)) return { id: ARTHUR, name: 'Arthur' };
  if (t === '[lp-listen-l7-2]') return { id: ARTHUR, name: 'Arthur' };
  alt = !alt; return alt ? { id: ELLEN, name: 'Ellen' } : { id: ARTHUR, name: 'Arthur' };
}

function generateAudio(text, voiceId) {
  let t = text;
  if (text === '[lp-listen-l7-1]') t = "Ladies and gentlemen, welcome aboard flight four seven two to Rome. Please fasten your seatbelt. Put your tray table up. Put your bag in the overhead compartment or under the seat in front of you. Please turn off your electronic devices for takeoff. We will be flying for approximately eleven hours. If you need anything, press the call button. Thank you for flying with us.";
  else if (text === '[lp-listen-l7-2]') t = "Good afternoon, ladies and gentlemen. We will now begin our meal service. Today we have chicken with rice or pasta with vegetables. Would you like chicken or pasta? Can I get you something to drink? We have water, juice, coffee, and tea. If you would like a snack later, we have cookies, chips, and fruit. Please let us know if you need anything else.";
  else if (text === '[order-l7]') t = "Marlene boards the plane. She finds her seat. She puts her bag in the overhead compartment. She fastens her seatbelt. The plane takes off. She asks: Can I have a blanket please? The flight attendant brings a blanket. Later, she has a snack and coffee. The captain says: We will be landing in thirty minutes.";
  return new Promise((resolve, reject) => {
    const d = JSON.stringify({ text: t, model_id: 'eleven_monolingual_v1', voice_settings: { stability: 0.5, similarity_boost: 0.75 } });
    const o = { hostname: 'api.elevenlabs.io', path: `/v1/text-to-speech/${voiceId}`, method: 'POST', headers: { 'Accept': 'audio/mpeg', 'Content-Type': 'application/json', 'xi-api-key': API_KEY, 'Content-Length': Buffer.byteLength(d) } };
    const req = https.request(o, (res) => {
      if (res.statusCode !== 200) { let b = ''; res.on('data', x => b += x); res.on('end', () => reject(new Error(`HTTP ${res.statusCode}: ${b}`))); return; }
      const c = []; res.on('data', x => c.push(x)); res.on('end', () => resolve(Buffer.concat(c)));
    }); req.on('error', reject); req.write(d); req.end();
  });
}

async function main() {
  const dir = path.join(BASE_DIR, 'audio/marlene-landucci');
  if (!fs.existsSync(dir)) fs.mkdirSync(dir, { recursive: true });
  let gen = 0, skip = 0, err = 0;
  for (const [text, fp] of Object.entries(audioMap)) {
    const full = path.join(BASE_DIR, fp);
    if (fs.existsSync(full)) { skip++; continue; }
    const v = getVoice(text);
    console.log(`GEN [${v.name}]: "${text.substring(0,50)}..." → ${fp}`);
    try { fs.writeFileSync(full, await generateAudio(text, v.id)); gen++; await new Promise(r => setTimeout(r, 500)); }
    catch (e) { console.error(`ERR: ${e.message}`); err++; }
  }
  console.log(`\nDone! Gen:${gen} Skip:${skip} Err:${err}`);
}
main();
