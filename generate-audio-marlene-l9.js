const fs = require('fs');
const path = require('path');
const https = require('https');
const API_KEY = process.env.ELEVENLABS_API_KEY;
if (!API_KEY) { console.error('ERROR: Set ELEVENLABS_API_KEY'); process.exit(1); }
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const BASE_DIR = '/Users/helenmendes/alumni-plano-gerador/public';

const audioMap = {
  "Suitcase": "/audio/marlene-landucci/suitcase.mp3",
  "Baggage claim": "/audio/marlene-landucci/baggage_claim.mp3",
  "Taxi": "/audio/marlene-landucci/taxi.mp3",
  "Driver": "/audio/marlene-landucci/driver.mp3",
  "Address": "/audio/marlene-landucci/address.mp3",
  "Lost": "/audio/marlene-landucci/lost.mp3",
  "Receipt": "/audio/marlene-landucci/receipt.mp3",
  "Meter": "/audio/marlene-landucci/meter.mp3",
  "Where is my suitcase?": "/audio/marlene-landucci/where_is_my_suitcase.mp3",
  "Where is the baggage claim?": "/audio/marlene-landucci/where_is_the_baggage_claim.mp3",
  "I need a taxi, please.": "/audio/marlene-landucci/i_need_a_taxi_please.mp3",
  "Could you take me to this address?": "/audio/marlene-landucci/could_you_take_me_to_this_address.mp3",
  "My luggage is lost.": "/audio/marlene-landucci/my_luggage_is_lost.mp3",
  "Can I have a receipt, please?": "/audio/marlene-landucci/can_i_have_a_receipt_please.mp3",
  "Is the meter running?": "/audio/marlene-landucci/is_the_meter_running.mp3",
  "This is my suitcase. It is black and big.": "/audio/marlene-landucci/this_is_my_suitcase_black_and_big.mp3",
  "Excuse me, where is the baggage claim?": "/audio/marlene-landucci/excuse_me_where_is_the_baggage_claim.mp3",
  "It is downstairs, on the left.": "/audio/marlene-landucci/it_is_downstairs_on_the_left.mp3",
  "My suitcase is not here. I think it is lost.": "/audio/marlene-landucci/my_suitcase_is_not_here_lost.mp3",
  "I am sorry. Could you describe your suitcase?": "/audio/marlene-landucci/i_am_sorry_could_you_describe.mp3",
  "It is a big black suitcase with a red tag.": "/audio/marlene-landucci/it_is_a_big_black_suitcase_red_tag.mp3",
  "We will find it. Here is a form. What is your hotel address?": "/audio/marlene-landucci/we_will_find_it_form_hotel_address.mp3",
  "My hotel address is Via Roma 15, Rome.": "/audio/marlene-landucci/my_hotel_address_is_via_roma.mp3",
  "We will deliver it to your hotel.": "/audio/marlene-landucci/we_will_deliver_to_your_hotel.mp3",
  "Thank you. Here is my phone number.": "/audio/marlene-landucci/thank_you_here_is_my_phone_number.mp3",
  "[order-l9]": "/audio/marlene-landucci/order_l9_ordering.mp3",
  "[lp-listen-l9-1]": "/audio/marlene-landucci/lp_listen_l9_1_baggage_claim.mp3",
  "[lp-listen-l9-2]": "/audio/marlene-landucci/lp_listen_l9_2_taxi_ride.mp3",
  "Where is the taxi stand?": "/audio/marlene-landucci/where_is_the_taxi_stand.mp3",
  "How much is the taxi to the city center?": "/audio/marlene-landucci/how_much_is_the_taxi_to_city_center.mp3"
};

const ellenPhrases = new Set([
  "Where is my suitcase?", "Where is the baggage claim?", "I need a taxi, please.",
  "Could you take me to this address?", "My luggage is lost.", "Can I have a receipt, please?",
  "Is the meter running?", "This is my suitcase. It is black and big.",
  "Excuse me, where is the baggage claim?", "My suitcase is not here. I think it is lost.",
  "It is a big black suitcase with a red tag.", "My hotel address is Via Roma 15, Rome.",
  "Thank you. Here is my phone number.", "Where is the taxi stand?",
  "How much is the taxi to the city center?", "[order-l9]", "[lp-listen-l9-1]",
]);
const arthurPhrases = new Set([
  "It is downstairs, on the left.", "I am sorry. Could you describe your suitcase?",
  "We will find it. Here is a form. What is your hotel address?",
  "We will deliver it to your hotel.",
]);

var alt = false;
function getVoice(t) {
  if (t.trim().split(/\s+/).length <= 2) return { id: ELLEN, name: 'Ellen' };
  if (ellenPhrases.has(t)) return { id: ELLEN, name: 'Ellen' };
  if (arthurPhrases.has(t)) return { id: ARTHUR, name: 'Arthur' };
  if (t === '[lp-listen-l9-2]') return { id: ARTHUR, name: 'Arthur' };
  alt = !alt; return alt ? { id: ELLEN, name: 'Ellen' } : { id: ARTHUR, name: 'Arthur' };
}

function generateAudio(text, voiceId) {
  var t = text;
  if (text === '[lp-listen-l9-1]') t = "Attention passengers from flight four seven two. Your luggage is now available at baggage claim number three. Baggage claim three is downstairs, on the left. If your luggage is not there, please go to the lost baggage office. The office is next to baggage claim three. Please have your boarding pass and luggage tag ready. Thank you.";
  else if (text === '[lp-listen-l9-2]') t = "Good afternoon. Where would you like to go? Could you take me to Via Roma fifteen, please? Of course. It is about twenty minutes from here. Is the meter running? Yes, the meter is on. Do not worry. How much is the taxi to the city center? It is usually about thirty euros. Here we are. Via Roma fifteen. That is twenty-eight euros. Can I have a receipt, please? Of course. Here you go. Have a nice stay!";
  else if (text === '[order-l9]') t = "Marlene arrives at baggage claim. She waits for her suitcase. Her suitcase is not there. She goes to the lost baggage office. She describes her suitcase: it is big and black with a red tag. She fills out a form with her hotel address. She takes a taxi to the hotel. The driver asks: Where would you like to go? She says: Via Roma fifteen, please.";
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
    console.log('GEN [' + v.name + ']: "' + text.substring(0, 50) + '..." -> ' + fp);
    try { fs.writeFileSync(full, await generateAudio(text, v.id)); gen++; await new Promise(function(r) { setTimeout(r, 500); }); }
    catch (e) { console.error('ERR: ' + e.message); }
  }
  console.log('\nDone! Gen:' + gen + ' Skip:' + skip);
}
main();
