const fs = require('fs');
const path = require('path');
const https = require('https');
const API_KEY = process.env.ELEVENLABS_API_KEY;
if (!API_KEY) { console.error('ERROR: Set ELEVENLABS_API_KEY'); process.exit(1); }
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const BASE_DIR = '/Users/helenmendes/alumni-plano-gerador/public';

const audioMap = {
  "Passport": "/audio/marlene-landucci/passport.mp3",
  "Luggage": "/audio/marlene-landucci/luggage.mp3",
  "Check-in": "/audio/marlene-landucci/check_in.mp3",
  "Boarding pass": "/audio/marlene-landucci/boarding_pass.mp3",
  "Aisle": "/audio/marlene-landucci/aisle.mp3",
  "Window": "/audio/marlene-landucci/window.mp3",
  "Carry-on": "/audio/marlene-landucci/carry_on.mp3",
  "Departure": "/audio/marlene-landucci/departure.mp3",
  "Could I have a window seat, please?": "/audio/marlene-landucci/could_i_have_a_window_seat_please.mp3",
  "I would like to check in for my flight.": "/audio/marlene-landucci/i_would_like_to_check_in_for_my_flight.mp3",
  "Here is my passport and my ticket.": "/audio/marlene-landucci/here_is_my_passport_and_my_ticket.mp3",
  "Could I have an aisle seat, please?": "/audio/marlene-landucci/could_i_have_an_aisle_seat_please.mp3",
  "I would like to check this luggage.": "/audio/marlene-landucci/i_would_like_to_check_this_luggage.mp3",
  "Where is the departure gate?": "/audio/marlene-landucci/where_is_the_departure_gate.mp3",
  "Is this my boarding pass?": "/audio/marlene-landucci/is_this_my_boarding_pass.mp3",
  "I have one carry-on bag.": "/audio/marlene-landucci/i_have_one_carry_on_bag.mp3",
  "Good morning. I would like to check in, please.": "/audio/marlene-landucci/good_morning_i_would_like_to_check_in.mp3",
  "Of course. Could I see your passport?": "/audio/marlene-landucci/of_course_could_i_see_your_passport.mp3",
  "Here you go.": "/audio/marlene-landucci/here_you_go_l6.mp3",
  "Would you like a window seat or an aisle seat?": "/audio/marlene-landucci/would_you_like_a_window_or_aisle.mp3",
  "I would like a window seat, please.": "/audio/marlene-landucci/i_would_like_a_window_seat_please.mp3",
  "Do you have any luggage to check?": "/audio/marlene-landucci/do_you_have_any_luggage_to_check.mp3",
  "Yes, one suitcase and one carry-on.": "/audio/marlene-landucci/yes_one_suitcase_and_one_carry_on.mp3",
  "Here is your boarding pass. Gate fourteen. Have a nice flight!": "/audio/marlene-landucci/here_is_your_boarding_pass_gate_fourteen.mp3",
  "[order-l6]": "/audio/marlene-landucci/order_l6_ordering.mp3",
  "[lp-listen-l6-1]": "/audio/marlene-landucci/lp_listen_l6_1_check_in_announcement.mp3",
  "[lp-listen-l6-2]": "/audio/marlene-landucci/lp_listen_l6_2_security_instructions.mp3",
  "Could I see your boarding pass?": "/audio/marlene-landucci/could_i_see_your_boarding_pass.mp3",
  "I would like some water, please.": "/audio/marlene-landucci/i_would_like_some_water_please.mp3"
};

const ellenPhrases = new Set([
  "Could I have a window seat, please?", "I would like to check in for my flight.",
  "Here is my passport and my ticket.", "Could I have an aisle seat, please?",
  "I would like to check this luggage.", "Where is the departure gate?",
  "Is this my boarding pass?", "I have one carry-on bag.",
  "Good morning. I would like to check in, please.", "Here you go.",
  "I would like a window seat, please.", "Yes, one suitcase and one carry-on.",
  "I would like some water, please.", "[order-l6]", "[lp-listen-l6-1]",
]);
const arthurPhrases = new Set([
  "Of course. Could I see your passport?",
  "Would you like a window seat or an aisle seat?",
  "Do you have any luggage to check?",
  "Here is your boarding pass. Gate fourteen. Have a nice flight!",
  "Could I see your boarding pass?",
]);

let alt = false;
function getVoice(t) {
  if (t.trim().split(/\s+/).length <= 2) return { id: ELLEN, name: 'Ellen' };
  if (ellenPhrases.has(t)) return { id: ELLEN, name: 'Ellen' };
  if (arthurPhrases.has(t)) return { id: ARTHUR, name: 'Arthur' };
  if (t === '[lp-listen-l6-2]') return { id: ARTHUR, name: 'Arthur' };
  alt = !alt; return alt ? { id: ELLEN, name: 'Ellen' } : { id: ARTHUR, name: 'Arthur' };
}

function generateAudio(text, voiceId) {
  let t = text;
  if (text === '[lp-listen-l6-1]') t = "Attention passengers. Check-in for flight four seven two to Rome is now open at counter twelve. Please have your passport and ticket ready. If you have luggage to check, please go to the check-in counter. Carry-on bags must fit in the overhead compartment. Boarding begins at two fifteen at gate fourteen. Thank you.";
  else if (text === '[lp-listen-l6-2]') t = "Welcome to security. Please remove your jacket and belt. Put your carry-on bag on the belt. Laptops and tablets must come out of your bag. No liquids over one hundred milliliters. Please walk through the scanner. Could I see your boarding pass? Thank you. Have a nice flight.";
  else if (text === '[order-l6]') t = "Marlene arrives at the airport. She goes to the check-in counter. Good morning, I would like to check in please. Here is my passport. I would like a window seat. She checks her luggage. Here is your boarding pass. Gate fourteen. She goes through security. She waits at the departure gate.";
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
