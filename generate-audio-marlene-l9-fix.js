var fs = require('fs');
var path = require('path');
var https = require('https');
var API_KEY = process.env.ELEVENLABS_API_KEY;
if (!API_KEY) { console.error('ERROR: Set ELEVENLABS_API_KEY'); process.exit(1); }
var ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
var ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
var BASE_DIR = '/Users/helenmendes/alumni-plano-gerador/public';

var missing = [
  { text: "His name is Marco.", voice: ARTHUR, file: "his_name_is_marco.mp3" },
  { text: "Excuse me. My suitcase is not on the belt. I think it is lost.", voice: ELLEN, file: "excuse_me_suitcase_not_on_belt.mp3" },
  { text: "I am sorry to hear that. Can I see your boarding pass?", voice: ARTHUR, file: "i_am_sorry_can_i_see_boarding_pass.mp3" },
  { text: "Yes, here it is. My name is Marlene Landucci.", voice: ELLEN, file: "yes_here_it_is_my_name_marlene.mp3" },
  { text: "What does your suitcase look like?", voice: ARTHUR, file: "what_does_your_suitcase_look_like.mp3" },
  { text: "It is black and large. It has my name on the tag.", voice: ELLEN, file: "it_is_black_and_large_name_on_tag.mp3" },
  { text: "What is the address of your hotel? We will deliver it.", voice: ARTHUR, file: "what_is_address_hotel_deliver.mp3" },
  { text: "My hotel is Hotel Roma. The address is Via Veneto 42.", voice: ELLEN, file: "my_hotel_is_hotel_roma_via_veneto.mp3" },
  { text: "Here is your claim ticket. We will call when we find your suitcase.", voice: ARTHUR, file: "here_is_claim_ticket_we_will_call.mp3" },
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
