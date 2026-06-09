var fs = require('fs');
var path = require('path');
var https = require('https');
var API_KEY = process.env.ELEVENLABS_API_KEY;
if (!API_KEY) { console.error('ERROR: Set ELEVENLABS_API_KEY'); process.exit(1); }
var ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
var ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
var BASE_DIR = '/Users/helenmendes/alumni-plano-gerador/public';

var audioMap = {
  "I would like to check in for my flight to Rome.": "/audio/marlene-landucci/i_would_like_check_in_flight_rome.mp3",
  "Could I have a window seat and a blanket?": "/audio/marlene-landucci/could_i_have_window_seat_blanket.mp3",
  "Do you have anything to declare? No, I do not.": "/audio/marlene-landucci/do_you_have_declare_no_i_do_not.mp3",
  "Where is the baggage claim? My suitcase is lost.": "/audio/marlene-landucci/where_is_baggage_claim_suitcase_lost.mp3",
  "Could you take me to Hotel Roma, please?": "/audio/marlene-landucci/could_you_take_me_hotel_roma.mp3",
  "Good morning! I would like to check in, please. Here is my passport.": "/audio/marlene-landucci/good_morning_check_in_passport_l10.mp3",
  "Certainly. Would you like a window or aisle seat?": "/audio/marlene-landucci/certainly_window_or_aisle_l10.mp3",
  "A window seat, please. Could I also check this suitcase?": "/audio/marlene-landucci/window_seat_check_suitcase_l10.mp3",
  "Of course. Here is your boarding pass. Gate B7. Boarding at ten fifteen.": "/audio/marlene-landucci/boarding_pass_gate_b7_l10.mp3",
  "Can I have a coffee and a snack, please?": "/audio/marlene-landucci/can_i_have_coffee_snack_l10.mp3",
  "Sure. Would you like milk?": "/audio/marlene-landucci/sure_would_you_like_milk_l10.mp3",
  "Yes, please. And could you bring me a blanket? It is cold.": "/audio/marlene-landucci/yes_please_blanket_cold_l10.mp3",
  "Here you go. We will be landing in about forty-five minutes.": "/audio/marlene-landucci/here_you_go_landing_45min_l10.mp3",
  "[order-l10]": "/audio/marlene-landucci/order_l10_ordering.mp3",
  "[lp-listen-l10-1]": "/audio/marlene-landucci/lp_listen_l10_1_full_journey.mp3",
  "[lp-listen-l10-2]": "/audio/marlene-landucci/lp_listen_l10_2_airport_review.mp3"
};

var ellenPhrases = [
  "I would like to check in for my flight to Rome.",
  "Could I have a window seat and a blanket?",
  "Do you have anything to declare? No, I do not.",
  "Where is the baggage claim? My suitcase is lost.",
  "Could you take me to Hotel Roma, please?",
  "Good morning! I would like to check in, please. Here is my passport.",
  "A window seat, please. Could I also check this suitcase?",
  "Can I have a coffee and a snack, please?",
  "Yes, please. And could you bring me a blanket? It is cold.",
  "[order-l10]", "[lp-listen-l10-1]"
];
var arthurPhrases = [
  "Certainly. Would you like a window or aisle seat?",
  "Of course. Here is your boarding pass. Gate B7. Boarding at ten fifteen.",
  "Sure. Would you like milk?",
  "Here you go. We will be landing in about forty-five minutes."
];

var alt = false;
function getVoice(t) {
  if (t.trim().split(/\s+/).length <= 2) return { id: ELLEN, name: 'Ellen' };
  if (ellenPhrases.indexOf(t) >= 0) return { id: ELLEN, name: 'Ellen' };
  if (arthurPhrases.indexOf(t) >= 0) return { id: ARTHUR, name: 'Arthur' };
  if (t === '[lp-listen-l10-2]') return { id: ARTHUR, name: 'Arthur' };
  alt = !alt; return alt ? { id: ELLEN, name: 'Ellen' } : { id: ARTHUR, name: 'Arthur' };
}

function generateAudio(text, voiceId) {
  var t = text;
  if (text === '[lp-listen-l10-1]') t = "Good morning everyone. Today I will tell you about my trip from Brazil to Rome. First, I checked in at the airport. I said: I would like to check in, please. The agent gave me my boarding pass. Gate B7. On the plane, I asked: Can I have a blanket, please? The flight attendant was very friendly. At immigration in Rome, the officer asked: What is the purpose of your visit? I said: I am on vacation. At baggage claim, my suitcase was not there! I said: Where is my suitcase? It is lost! They gave me a claim form. Then I took a taxi to my hotel. I said: Could you take me to Hotel Roma? What an adventure!";
  else if (text === '[lp-listen-l10-2]') t = "Attention passengers arriving on flight four seven two from Sao Paulo. Welcome to Rome Fiumicino Airport. Please proceed to immigration with your passport ready. After immigration, collect your luggage at baggage claim number five. If your luggage is missing, please report to the lost baggage office near exit C. Taxis are available outside the arrivals hall. The taxi to the city center costs approximately thirty-five euros. Thank you and enjoy your stay in Rome.";
  else if (text === '[order-l10]') t = "Marlene arrives at the airport. She checks in and gets her boarding pass. She goes through security. She boards the plane. On the plane she asks for a blanket and coffee. The plane lands in Rome. She goes through immigration. She goes to baggage claim. Her suitcase is not there, so she reports it. She takes a taxi to Hotel Roma.";
  return new Promise(function(resolve, reject) {
    var d = JSON.stringify({ text: t, model_id: 'eleven_monolingual_v1', voice_settings: { stability: 0.5, similarity_boost: 0.75 } });
    var o = { hostname: 'api.elevenlabs.io', path: '/v1/text-to-speech/' + voiceId, method: 'POST', headers: { 'Accept': 'audio/mpeg', 'Content-Type': 'application/json', 'xi-api-key': API_KEY, 'Content-Length': Buffer.byteLength(d) } };
    var req = https.request(o, function(res) {
      if (res.statusCode !== 200) { var b = ''; res.on('data', function(x) { b += x; }); res.on('end', function() { reject(new Error(res.statusCode + ': ' + b)); }); return; }
      var c = []; res.on('data', function(x) { c.push(x); }); res.on('end', function() { resolve(Buffer.concat(c)); });
    }); req.on('error', reject); req.write(d); req.end();
  });
}

async function main() {
  var dir = path.join(BASE_DIR, 'audio/marlene-landucci');
  if (!fs.existsSync(dir)) fs.mkdirSync(dir, { recursive: true });
  var gen = 0, skip = 0;
  var entries = Object.entries(audioMap);
  for (var i = 0; i < entries.length; i++) {
    var text = entries[i][0], fp = entries[i][1];
    var full = path.join(BASE_DIR, fp);
    if (fs.existsSync(full)) { skip++; continue; }
    var v = getVoice(text);
    console.log('GEN [' + v.name + ']: "' + text.substring(0, 50) + '..."');
    try { fs.writeFileSync(full, await generateAudio(text, v.id)); gen++; await new Promise(function(r) { setTimeout(r, 500); }); }
    catch (e) { console.error('ERR: ' + e.message); }
  }
  console.log('\nDone! Gen:' + gen + ' Skip:' + skip);
}
main();
