const fs = require('fs');
const path = require('path');
const https = require('https');
const API_KEY = process.env.ELEVENLABS_API_KEY;
if (!API_KEY) { console.error('ERROR: Set ELEVENLABS_API_KEY'); process.exit(1); }
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const BASE_DIR = '/Users/helenmendes/alumni-plano-gerador/public';

const audioMap = {
  "Customs": "/audio/marlene-landucci/customs.mp3",
  "Declaration": "/audio/marlene-landucci/declaration.mp3",
  "Purpose": "/audio/marlene-landucci/purpose.mp3",
  "Vacation": "/audio/marlene-landucci/vacation.mp3",
  "Declare": "/audio/marlene-landucci/declare.mp3",
  "Stamp": "/audio/marlene-landucci/stamp_word.mp3",
  "Return": "/audio/marlene-landucci/return.mp3",
  "Citizen": "/audio/marlene-landucci/citizen.mp3",
  "What is the purpose of your visit?": "/audio/marlene-landucci/what_is_the_purpose_of_your_visit.mp3",
  "I am here on vacation.": "/audio/marlene-landucci/i_am_here_on_vacation.mp3",
  "Do you have anything to declare?": "/audio/marlene-landucci/do_you_have_anything_to_declare.mp3",
  "No, I do not have anything to declare.": "/audio/marlene-landucci/no_i_do_not_have_anything_to_declare.mp3",
  "How long do you plan to stay?": "/audio/marlene-landucci/how_long_do_you_plan_to_stay.mp3",
  "I plan to stay for two weeks.": "/audio/marlene-landucci/i_plan_to_stay_for_two_weeks.mp3",
  "Where do you come from?": "/audio/marlene-landucci/where_do_you_come_from.mp3",
  "I come from Brazil.": "/audio/marlene-landucci/i_come_from_brazil.mp3",
  "Do you have a return ticket?": "/audio/marlene-landucci/do_you_have_a_return_ticket.mp3",
  "Yes, I do. My return flight is on June twenty-third.": "/audio/marlene-landucci/yes_i_do_my_return_flight.mp3",
  "Where are you staying?": "/audio/marlene-landucci/where_are_you_staying.mp3",
  "I am staying at a hotel in the city center.": "/audio/marlene-landucci/i_am_staying_at_a_hotel.mp3",
  "Welcome to Italy. Enjoy your stay.": "/audio/marlene-landucci/welcome_to_italy_enjoy_your_stay.mp3",
  "Thank you very much!": "/audio/marlene-landucci/thank_you_very_much.mp3",
  "Does she have a visa?": "/audio/marlene-landucci/does_she_have_a_visa.mp3",
  "Do they need a declaration form?": "/audio/marlene-landucci/do_they_need_a_declaration_form.mp3",
  "[order-l8]": "/audio/marlene-landucci/order_l8_ordering.mp3",
  "[lp-listen-l8-1]": "/audio/marlene-landucci/lp_listen_l8_1_immigration_interview.mp3",
  "[lp-listen-l8-2]": "/audio/marlene-landucci/lp_listen_l8_2_customs_check.mp3"
};

const ellenPhrases = new Set([
  "I am here on vacation.", "No, I do not have anything to declare.",
  "I plan to stay for two weeks.", "I come from Brazil.",
  "Yes, I do. My return flight is on June twenty-third.",
  "I am staying at a hotel in the city center.", "Thank you very much!",
  "[order-l8]", "[lp-listen-l8-1]",
]);
const arthurPhrases = new Set([
  "What is the purpose of your visit?", "Do you have anything to declare?",
  "How long do you plan to stay?", "Where do you come from?",
  "Do you have a return ticket?", "Where are you staying?",
  "Welcome to Italy. Enjoy your stay.", "Does she have a visa?",
  "Do they need a declaration form?",
]);

let alt = false;
function getVoice(t) {
  if (t.trim().split(/\s+/).length <= 2) return { id: ELLEN, name: 'Ellen' };
  if (ellenPhrases.has(t)) return { id: ELLEN, name: 'Ellen' };
  if (arthurPhrases.has(t)) return { id: ARTHUR, name: 'Arthur' };
  if (t === '[lp-listen-l8-2]') return { id: ARTHUR, name: 'Arthur' };
  alt = !alt; return alt ? { id: ELLEN, name: 'Ellen' } : { id: ARTHUR, name: 'Arthur' };
}

function generateAudio(text, voiceId) {
  let t = text;
  if (text === '[lp-listen-l8-1]') t = "Good afternoon. Welcome to Italy. Could I see your passport, please? What is the purpose of your visit? I am here on vacation. How long do you plan to stay? I plan to stay for two weeks. Where are you staying? I am staying at a hotel near the Colosseum. Do you have a return ticket? Yes, I do. My return flight is on June twenty-third. Welcome to Italy. Enjoy your stay.";
  else if (text === '[lp-listen-l8-2]') t = "Welcome to customs. Do you have anything to declare? Please put your bags on the table. Do you have any food, plants, or animals? No, I do not. Do you have more than ten thousand euros in cash? No, I do not. Where do you come from? I come from Brazil. OK, everything looks good. You may go. Welcome to Italy!";
  else if (text === '[order-l8]') t = "The plane lands in Rome. Marlene walks to immigration. The officer asks: What is the purpose of your visit? She says: I am here on vacation. He asks: How long do you plan to stay? She says: Two weeks. He stamps her passport. She goes to customs. No, I do not have anything to declare. She collects her luggage. Welcome to Italy!";
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
  let gen = 0, skip = 0;
  for (const [text, fp] of Object.entries(audioMap)) {
    const full = path.join(BASE_DIR, fp);
    if (fs.existsSync(full)) { skip++; continue; }
    const v = getVoice(text);
    console.log(`GEN [${v.name}]: "${text.substring(0,50)}..." → ${fp}`);
    try { fs.writeFileSync(full, await generateAudio(text, v.id)); gen++; await new Promise(r => setTimeout(r, 500)); }
    catch (e) { console.error(`ERR: ${e.message}`); }
  }
  console.log(`\nDone! Gen:${gen} Skip:${skip}`);
}
main();
