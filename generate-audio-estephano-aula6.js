const https = require('https');
const fs = require('fs');
const path = require('path');

const ASH = 'VU16byTywsWv5JpI8rbc';
const RILEY = 'hA4zGnmTwX2NQiTRMt7o';
const API_KEY = process.env.ELEVENLABS_API_KEY;
const OUTPUT_DIR = path.join(__dirname, 'public', 'audio', 'estephano-akihito-ishii');

const entries = [
  // SINGLE WORDS (Ash - student gender)
  { file: 'aula6_meal.mp3', text: 'Meal', voice: ASH },
  { file: 'aula6_dish.mp3', text: 'Dish', voice: ASH },
  { file: 'aula6_beverage.mp3', text: 'Beverage', voice: ASH },
  { file: 'aula6_appetizer.mp3', text: 'Appetizer', voice: ASH },
  { file: 'aula6_dessert.mp3', text: 'Dessert', voice: ASH },
  { file: 'aula6_order.mp3', text: 'Order', voice: ASH },
  { file: 'aula6_menu.mp3', text: 'Menu', voice: ASH },

  // VOCAB EXAMPLES (alternate Ash/Riley)
  { file: 'aula6_lunch_favorite_meal.mp3', text: 'Lunch is my favorite meal.', voice: ASH },
  { file: 'aula6_dish_delicious.mp3', text: 'This dish is delicious.', voice: RILEY },
  { file: 'aula6_water_best_beverage.mp3', text: 'Water is the best beverage.', voice: ASH },
  { file: 'aula6_salad_appetizer.mp3', text: 'I want a salad as an appetizer.', voice: RILEY },
  { file: 'aula6_chocolate_dessert.mp3', text: 'I love chocolate dessert.', voice: ASH },
  { file: 'aula6_order_pizza.mp3', text: 'I want to order a pizza.', voice: RILEY },
  { file: 'aula6_see_menu.mp3', text: 'Can I see the menu, please?', voice: ASH },

  // GRAMMAR/PRACTICE PHRASES (alternate)
  { file: 'aula6_some_water.mp3', text: 'I want some water.', voice: ASH },
  { file: 'aula6_some_apples.mp3', text: 'There are some apples.', voice: RILEY },
  { file: 'aula6_any_coffee.mp3', text: 'Is there any coffee?', voice: ASH },
  { file: 'aula6_no_bread.mp3', text: 'I don\'t have any bread.', voice: RILEY },
  { file: 'aula6_how_much_water.mp3', text: 'How much water do you want?', voice: ASH },
  { file: 'aula6_how_many_sandwiches.mp3', text: 'How many sandwiches do you want?', voice: RILEY },
  { file: 'aula6_some_rice.mp3', text: 'I want some rice with beans.', voice: ASH },
  { file: 'aula6_any_juice.mp3', text: 'Is there any juice?', voice: RILEY },
  { file: 'aula6_some_cookies.mp3', text: 'There are some cookies on the table.', voice: ASH },
  { file: 'aula6_any_milk.mp3', text: 'We don\'t have any milk.', voice: RILEY },

  // DIALOGUE (Maria=Riley female, Estephano=Ash male)
  { file: 'aula6_dialogue_maria_1.mp3', text: 'Good afternoon! What would you like to order?', voice: RILEY },
  { file: 'aula6_dialogue_estephano_1.mp3', text: 'Hi! Can I see the menu, please?', voice: ASH },
  { file: 'aula6_dialogue_maria_2.mp3', text: 'Of course. We have some sandwiches, salads, and rice with beans.', voice: RILEY },
  { file: 'aula6_dialogue_estephano_2.mp3', text: 'I want a chicken sandwich with some rice, please.', voice: ASH },
  { file: 'aula6_dialogue_maria_3.mp3', text: 'Would you like any beverage?', voice: RILEY },
  { file: 'aula6_dialogue_estephano_3.mp3', text: 'Is there any juice?', voice: ASH },
  { file: 'aula6_dialogue_maria_4.mp3', text: 'We have some orange juice and some water.', voice: RILEY },
  { file: 'aula6_dialogue_estephano_4.mp3', text: 'Some juice, please. And a chocolate dessert.', voice: ASH },

  // SPEECH CARDS (Ash - student)
  { file: 'aula6_speech1_order.mp3', text: 'Can I see the menu, please? I want a chicken sandwich with some rice. Is there any juice?', voice: ASH },
  { file: 'aula6_speech2_describe.mp3', text: 'I usually have lunch at the university cafeteria. I order some rice with beans and a beverage. My favorite dessert is chocolate cake.', voice: ASH },

  // ORDERING
  { file: 'order_l6_restaurant.mp3', text: 'Can I see the menu? I want a chicken sandwich. I want some rice. Is there any juice? Some juice, please.', voice: ASH },

  // LISTENING PASSAGES
  { file: 'aula6_listening_cafeteria.mp3', text: 'Welcome to the university cafeteria. Today we have some chicken sandwiches and some beef sandwiches. We also have rice with beans and a green salad. For beverages, we have some orange juice, some coffee, and water. We don\'t have any pizza today. For dessert, there is chocolate cake and some fruit. The meal costs fifteen reais. Please order at the counter.', voice: RILEY },
  { file: 'aula6_listening_restaurant.mp3', text: 'Good evening and welcome to Sabor Paulista restaurant. My name is Pedro. Let me tell you about our menu. For appetizers, we have some bruschetta and a tomato soup. Our main dishes are grilled chicken with rice, pasta with cheese, and a fish with vegetables. We don\'t have any steak tonight. For beverages, we have some natural juices, soft drinks, and water. How many people are dining tonight?', voice: ASH },

  // SURVIVAL/EXTRA
  { file: 'aula6_can_i_see_menu.mp3', text: 'Can I see the menu, please?', voice: ASH },
  { file: 'aula6_i_want_to_order.mp3', text: 'I want to order, please.', voice: ASH },
  { file: 'aula6_is_there_any.mp3', text: 'Is there any juice?', voice: RILEY },
  { file: 'aula6_i_want_some.mp3', text: 'I want some water, please.', voice: ASH },
  { file: 'aula6_how_much_is_it.mp3', text: 'How much is it?', voice: ASH },
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
  console.log(`Generating ${entries.length} audio files for Estephano (Aula 6)...\n`);
  for (const entry of entries) { await generateAudio(entry); await new Promise(r => setTimeout(r, 500)); }
  console.log('\nDone!');
}

main().catch(console.error);
