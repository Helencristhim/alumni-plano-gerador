const https = require('https');
const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const DIR = path.join(__dirname, 'public/audio/elaine-mieko-pinho');

const entries = [
  { text: "I work as a lawyer in Indaiatuba.", file: "i_work_as_a_lawyer_in_indaiatuba.mp3", voice: ELLEN },
  { text: "Good morning. My name is Elaine Mieko Pinho. I am from Indaiatuba, a small city in Sao Paulo, Brazil. I am a lawyer and I also manage a family company. I usually travel with my family, but I want to travel alone too. I feel nervous when I need to speak English abroad, but I am not going to give up. I want to feel confident.", file: "good_morning_my_name_is_elaine_mieko_pinho_i_am_from_indaiatuba.mp3", voice: ELLEN },
  { text: "I am from Indaiatuba, in Sao Paulo.", file: "i_am_from_indaiatuba_in_sao_paulo.mp3", voice: ARTHUR },
  { text: "I am from Brazil. I live in a small city called Indaiatuba.", file: "i_am_from_brazil_i_live_in_a_small_city_called_indaiatuba.mp3", voice: ELLEN }
];

async function generate(entry) {
  const filePath = path.join(DIR, entry.file);
  return new Promise((resolve, reject) => {
    const data = JSON.stringify({
      text: entry.text,
      model_id: 'eleven_monolingual_v1',
      voice_settings: { stability: 0.5, similarity_boost: 0.75 }
    });
    const opts = {
      hostname: 'api.elevenlabs.io',
      path: `/v1/text-to-speech/${entry.voice}`,
      method: 'POST',
      headers: { 'xi-api-key': API_KEY, 'Content-Type': 'application/json', 'Accept': 'audio/mpeg' }
    };
    const req = https.request(opts, res => {
      const chunks = [];
      res.on('data', c => chunks.push(c));
      res.on('end', () => { fs.writeFileSync(filePath, Buffer.concat(chunks)); console.log('Generated:', entry.file); resolve(); });
    });
    req.on('error', reject);
    req.write(data);
    req.end();
  });
}

(async () => {
  for (const e of entries) {
    await generate(e);
    await new Promise(r => setTimeout(r, 500));
  }
  console.log('Done! 4 city-corrected audio files generated.');
})();
