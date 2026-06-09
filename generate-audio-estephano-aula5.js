const https = require('https');
const fs = require('fs');
const path = require('path');

const ASH = 'VU16byTywsWv5JpI8rbc';
const RILEY = 'hA4zGnmTwX2NQiTRMt7o';
const API_KEY = process.env.ELEVENLABS_API_KEY;
const OUTPUT_DIR = path.join(__dirname, 'public', 'audio', 'estephano-akihito-ishii');

const entries = [
  // SINGLE WORDS (Ash - student gender)
  { file: 'aula5_neighborhood.mp3', text: 'Neighborhood', voice: ASH },
  { file: 'aula5_street.mp3', text: 'Street', voice: ASH },
  { file: 'aula5_building.mp3', text: 'Building', voice: ASH },
  { file: 'aula5_station.mp3', text: 'Station', voice: ASH },
  { file: 'aula5_near.mp3', text: 'Near', voice: ASH },
  { file: 'aula5_far.mp3', text: 'Far', voice: ASH },
  { file: 'aula5_between.mp3', text: 'Between', voice: ASH },

  // VOCAB EXAMPLES (alternate Ash/Riley)
  { file: 'aula5_my_neighborhood.mp3', text: 'My neighborhood is very safe.', voice: ASH },
  { file: 'aula5_live_on_paulista.mp3', text: 'I live on Paulista Street.', voice: RILEY },
  { file: 'aula5_big_building.mp3', text: 'My university is in a big building.', voice: ASH },
  { file: 'aula5_metro_station.mp3', text: 'The metro station is near my house.', voice: RILEY },
  { file: 'aula5_park_near.mp3', text: 'The park is near the library.', voice: ASH },
  { file: 'aula5_airport_far.mp3', text: 'The airport is far from here.', voice: RILEY },
  { file: 'aula5_bank_between.mp3', text: 'The bank is between the pharmacy and the supermarket.', voice: ASH },

  // GRAMMAR/PRACTICE PHRASES (alternate)
  { file: 'aula5_live_in_sp.mp3', text: 'I live in São Paulo.', voice: ASH },
  { file: 'aula5_study_in_liberdade.mp3', text: 'I study in Liberdade.', voice: RILEY },
  { file: 'aula5_house_on_rua.mp3', text: 'My house is on Rua Augusta.', voice: ASH },
  { file: 'aula5_at_university.mp3', text: 'I am at the university.', voice: RILEY },
  { file: 'aula5_at_bus_stop.mp3', text: 'She is at the bus stop.', voice: ASH },
  { file: 'aula5_store_on_corner.mp3', text: 'The store is on the corner.', voice: RILEY },
  { file: 'aula5_next_to_metro.mp3', text: 'The supermarket is next to the metro station.', voice: ASH },
  { file: 'aula5_far_from_liberdade.mp3', text: 'The airport is very far from Liberdade.', voice: RILEY },

  // DIALOGUE (both male = Ash)
  { file: 'aula5_dialogue_lucas_1.mp3', text: 'Where do you live, Estephano?', voice: ASH },
  { file: 'aula5_dialogue_estephano_1.mp3', text: 'I live in Liberdade. It\'s a neighborhood in São Paulo.', voice: ASH },
  { file: 'aula5_dialogue_lucas_2.mp3', text: 'Is it near the university?', voice: ASH },
  { file: 'aula5_dialogue_estephano_2.mp3', text: 'Yes, the metro station is near my building.', voice: ASH },
  { file: 'aula5_dialogue_lucas_3.mp3', text: 'What is near your house?', voice: ASH },
  { file: 'aula5_dialogue_estephano_3.mp3', text: 'There is a supermarket next to the metro station. And a park between my street and the avenue.', voice: ASH },
  { file: 'aula5_dialogue_lucas_4.mp3', text: 'Is the airport far?', voice: ASH },
  { file: 'aula5_dialogue_estephano_4.mp3', text: 'Yes, it\'s very far from Liberdade.', voice: ASH },

  // SPEECH CARDS (Ash - student)
  { file: 'aula5_speech1_location.mp3', text: 'I live in Liberdade. My apartment is on Rua Galvão Bueno. The metro station is near my building.', voice: ASH },
  { file: 'aula5_speech2_places.mp3', text: 'The supermarket is next to the station. The park is far from my house. My university is between a coffee shop and a bookstore.', voice: ASH },

  // ORDERING
  { file: 'order_l5_neighborhood.mp3', text: 'I live in São Paulo. My neighborhood is Liberdade. My apartment is on Rua Galvão Bueno. The metro station is near my building. The park is far from my house.', voice: ASH },

  // LISTENING PASSAGES
  { file: 'aula5_listening_neighborhood.mp3', text: 'Hi! My name is Camila. I live in Pinheiros, a neighborhood in São Paulo. My apartment is on Rua dos Pinheiros. It\'s a very nice street. The metro station is near my building, about 5 minutes on foot. There is a supermarket next to the station. My favorite coffee shop is between the bookstore and the pharmacy. The park is far from my house, but I go there on weekends. I love my neighborhood!', voice: RILEY },
  { file: 'aula5_listening_campus.mp3', text: 'Welcome to our university campus. The main building is on Avenida Paulista. The library is near the main building. The cafeteria is between the library and the sports center. The parking lot is far from the classrooms. The bus stop is at the main entrance. There is a pharmacy next to the bus stop. The nearest metro station is about 10 minutes from here.', voice: ASH },

  // SURVIVAL/EXTRA
  { file: 'aula5_where_do_you_live.mp3', text: 'Where do you live?', voice: RILEY },
  { file: 'aula5_i_live_in_liberdade.mp3', text: 'I live in Liberdade.', voice: ASH },
  { file: 'aula5_is_it_near.mp3', text: 'Is it near here?', voice: RILEY },
  { file: 'aula5_it_is_far.mp3', text: 'It is far from here.', voice: ASH },
  { file: 'aula5_next_to_station.mp3', text: 'It is next to the metro station.', voice: ASH },
];

function generateAudio(entry) {
  return new Promise((resolve, reject) => {
    const data = JSON.stringify({
      text: entry.text,
      model_id: 'eleven_multilingual_v2',
      voice_settings: { stability: 0.5, similarity_boost: 0.75 }
    });
    const options = {
      hostname: 'api.elevenlabs.io',
      path: `/v1/text-to-speech/${entry.voice}`,
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'xi-api-key': API_KEY, 'Content-Length': Buffer.byteLength(data) }
    };
    const outPath = path.join(OUTPUT_DIR, entry.file);
    if (fs.existsSync(outPath)) { console.log(`SKIP (exists): ${entry.file}`); return resolve(); }
    const req = https.request(options, (res) => {
      if (res.statusCode !== 200) { let body = ''; res.on('data', d => body += d); res.on('end', () => { console.error(`ERROR ${res.statusCode} for ${entry.file}: ${body}`); resolve(); }); return; }
      const ws = fs.createWriteStream(outPath);
      res.pipe(ws);
      ws.on('finish', () => { console.log(`OK: ${entry.file}`); resolve(); });
      ws.on('error', reject);
    });
    req.on('error', reject);
    req.write(data);
    req.end();
  });
}

async function main() {
  if (!API_KEY) { console.error('ERROR: ELEVENLABS_API_KEY not set.'); process.exit(1); }
  if (!fs.existsSync(OUTPUT_DIR)) fs.mkdirSync(OUTPUT_DIR, { recursive: true });
  console.log(`Generating ${entries.length} audio files for Estephano (Aula 5)...\n`);
  for (const entry of entries) { await generateAudio(entry); await new Promise(r => setTimeout(r, 500)); }
  console.log('\nDone!');
}

main().catch(console.error);
