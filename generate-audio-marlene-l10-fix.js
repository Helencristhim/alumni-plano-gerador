var fs = require('fs');
var path = require('path');
var https = require('https');
var API_KEY = process.env.ELEVENLABS_API_KEY;
if (!API_KEY) { console.error('ERROR: Set ELEVENLABS_API_KEY'); process.exit(1); }
var ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
var ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
var BASE_DIR = '/Users/helenmendes/alumni-plano-gerador/public';

var missing = [
  { text: "Can I check in for my flight?", voice: ELLEN, file: "can_i_check_in_for_my_flight.mp3" },
  { text: "This is your boarding pass.", voice: ARTHUR, file: "this_is_your_boarding_pass.mp3" },
  { text: "Could I have headphones, please?", voice: ELLEN, file: "could_i_have_headphones_please.mp3" },
  { text: "This is my boarding pass.", voice: ELLEN, file: "this_is_my_boarding_pass.mp3" },
  { text: "Flight attendant", voice: ELLEN, file: "flight_attendant.mp3" },
  { text: "Hello. I would like to check in, please.", voice: ELLEN, file: "hello_i_would_like_check_in.mp3" },
  { text: "Good morning! May I see your passport and booking confirmation?", voice: ARTHUR, file: "good_morning_may_i_see_passport.mp3" },
  { text: "Yes, here they are. Could I have a window seat, please?", voice: ELLEN, file: "yes_here_they_are_window_seat.mp3" },
  { text: "Of course. You are in seat 12A. How many bags are you checking in?", voice: ARTHUR, file: "of_course_seat_12a_how_many_bags.mp3" },
  { text: "One suitcase. It is black and large.", voice: ELLEN, file: "one_suitcase_black_and_large.mp3" },
  { text: "Your gate is number 14. Boarding starts at 2:30.", voice: ARTHUR, file: "your_gate_14_boarding_230.mp3" },
  { text: "Where is gate fourteen?", voice: ELLEN, file: "where_is_gate_fourteen_l10.mp3" },
  { text: "Go straight and turn left after security. Have a good flight!", voice: ARTHUR, file: "go_straight_turn_left_good_flight.mp3" },
  { text: "Can I check in for my flight to Rome?", voice: ELLEN, file: "can_i_check_in_flight_to_rome.mp3" },
];

function gen(text, voiceId) {
  return new Promise(function(resolve, reject) {
    var d = JSON.stringify({ text: text, model_id: 'eleven_monolingual_v1', voice_settings: { stability: 0.5, similarity_boost: 0.75 } });
    var o = { hostname: 'api.elevenlabs.io', path: '/v1/text-to-speech/' + voiceId, method: 'POST', headers: { 'Accept': 'audio/mpeg', 'Content-Type': 'application/json', 'xi-api-key': API_KEY, 'Content-Length': Buffer.byteLength(d) } };
    var req = https.request(o, function(res) {
      if (res.statusCode !== 200) { var b = ''; res.on('data', function(x) { b += x; }); res.on('end', function() { reject(new Error(res.statusCode + ': ' + b)); }); return; }
      var c = []; res.on('data', function(x) { c.push(x); }); res.on('end', function() { resolve(Buffer.concat(c)); });
    }); req.on('error', reject); req.write(d); req.end();
  });
}

async function main() {
  var dir = path.join(BASE_DIR, 'audio/marlene-landucci');
  for (var i = 0; i < missing.length; i++) {
    var item = missing[i];
    var fp = path.join(dir, item.file);
    if (fs.existsSync(fp)) { console.log('SKIP: ' + item.file); continue; }
    console.log('GEN: ' + item.text.substring(0, 50) + '...');
    try { fs.writeFileSync(fp, await gen(item.text, item.voice)); await new Promise(function(r) { setTimeout(r, 500); }); }
    catch (e) { console.error('ERR: ' + e.message); }
  }
  console.log('\nAudioMap entries:');
  for (var i = 0; i < missing.length; i++) {
    console.log('  "' + missing[i].text + '": "/audio/marlene-landucci/' + missing[i].file + '",');
  }
}
main();
