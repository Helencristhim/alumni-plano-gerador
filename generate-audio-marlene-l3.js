const fs = require('fs');
const path = require('path');
const https = require('https');

const API_KEY = process.env.ELEVENLABS_API_KEY;
if (!API_KEY) { console.error('ERROR: Set ELEVENLABS_API_KEY env variable'); process.exit(1); }

const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';

const BASE_DIR = '/Users/helenmendes/alumni-plano-gerador/public';
const AUDIO_DIR = path.join(BASE_DIR, 'audio/marlene-landucci');

// Only Aula 3 new entries
const audioMap = {
  "Number": "/audio/marlene-landucci/number.mp3",
  "Clock": "/audio/marlene-landucci/clock.mp3",
  "Price": "/audio/marlene-landucci/price.mp3",
  "Gate": "/audio/marlene-landucci/gate.mp3",
  "Hundred": "/audio/marlene-landucci/hundred.mp3",
  "Half": "/audio/marlene-landucci/half.mp3",
  "Quarter": "/audio/marlene-landucci/quarter.mp3",
  "Flight": "/audio/marlene-landucci/flight.mp3",
  "What is your phone number?": "/audio/marlene-landucci/what_is_your_phone_number.mp3",
  "The clock says ten thirty.": "/audio/marlene-landucci/the_clock_says_ten_thirty.mp3",
  "What is the price of this ticket?": "/audio/marlene-landucci/what_is_the_price_of_this_ticket.mp3",
  "Your gate is number fourteen.": "/audio/marlene-landucci/your_gate_is_number_fourteen.mp3",
  "The ticket costs one hundred dollars.": "/audio/marlene-landucci/the_ticket_costs_one_hundred_dollars.mp3",
  "It is half past ten.": "/audio/marlene-landucci/it_is_half_past_ten.mp3",
  "It is a quarter to three.": "/audio/marlene-landucci/it_is_a_quarter_to_three.mp3",
  "My flight is at two fifteen.": "/audio/marlene-landucci/my_flight_is_at_two_fifteen.mp3",
  "It is three o'clock.": "/audio/marlene-landucci/it_is_three_oclock.mp3",
  "The flight is at half past two.": "/audio/marlene-landucci/the_flight_is_at_half_past_two.mp3",
  "It costs fifty dollars.": "/audio/marlene-landucci/it_costs_fifty_dollars.mp3",
  "What time is your flight?": "/audio/marlene-landucci/what_time_is_your_flight.mp3",
  "Excuse me, what gate is flight 472?": "/audio/marlene-landucci/excuse_me_what_gate_is_flight_472.mp3",
  "Gate fourteen. Boarding at two thirty.": "/audio/marlene-landucci/gate_fourteen_boarding_at_two_thirty.mp3",
  "What time is it now?": "/audio/marlene-landucci/what_time_is_it_now.mp3",
  "It is one forty-five. You have forty-five minutes.": "/audio/marlene-landucci/it_is_one_forty_five_you_have_forty_five_minutes.mp3",
  "How much is a coffee?": "/audio/marlene-landucci/how_much_is_a_coffee.mp3",
  "Three dollars and fifty cents.": "/audio/marlene-landucci/three_dollars_and_fifty_cents.mp3",
  "Here you go. Thank you!": "/audio/marlene-landucci/here_you_go_thank_you.mp3",
  "You are welcome. Have a nice flight!": "/audio/marlene-landucci/you_are_welcome_have_a_nice_flight.mp3",
  "My flight is at three o'clock.": "/audio/marlene-landucci/my_flight_is_at_three_oclock.mp3",
  "The gate number is fourteen.": "/audio/marlene-landucci/the_gate_number_is_fourteen.mp3",
  "How much is this?": "/audio/marlene-landucci/how_much_is_this.mp3",
  "It is half past one.": "/audio/marlene-landucci/it_is_half_past_one.mp3",
  "I need to be at gate fourteen at two thirty.": "/audio/marlene-landucci/i_need_to_be_at_gate_fourteen.mp3",
  "[order-l3]": "/audio/marlene-landucci/order_l3_ordering.mp3",
  "[lp-listen-l3-1]": "/audio/marlene-landucci/lp_listen_l3_1_airport_announcements.mp3",
  "[lp-listen-l3-2]": "/audio/marlene-landucci/lp_listen_l3_2_shopping_prices.mp3",
  "The price is twenty-five dollars.": "/audio/marlene-landucci/the_price_is_twenty_five_dollars.mp3",
  "What time does the flight leave?": "/audio/marlene-landucci/what_time_does_the_flight_leave.mp3",
  "It leaves at a quarter past four.": "/audio/marlene-landucci/it_leaves_at_a_quarter_past_four.mp3",
  "How much is this souvenir?": "/audio/marlene-landucci/how_much_is_this_souvenir.mp3",
  "That is fifteen dollars.": "/audio/marlene-landucci/that_is_fifteen_dollars.mp3",
  "Can I have two, please?": "/audio/marlene-landucci/can_i_have_two_please.mp3",
  "That is thirty dollars total.": "/audio/marlene-landucci/that_is_thirty_dollars_total.mp3"
};

// Ellen phrases (Marlene is female - protagonist lines, survival, speech cards, single words)
const ellenPhrases = new Set([
  // Single words are handled by word count check
  // Marlene's dialogue lines (protagonist = female = Ellen)
  "Excuse me, what gate is flight 472?",
  "What time is it now?",
  "How much is a coffee?",
  "Here you go. Thank you!",
  // Speech card phrases (protagonist)
  "My flight is at three o'clock.",
  "How much is this?",
  "I need to be at gate fourteen at two thirty.",
  // Survival phrases (protagonist)
  "What is your phone number?",
  "What is the price of this ticket?",
  "My flight is at two fifteen.",
  "The flight is at half past two.",
  "How much is this souvenir?",
  "Can I have two, please?",
  // Listening keys
  "[lp-listen-l3-1]",
  "[order-l3]",
]);

// Staff lines (male character) = Arthur
const arthurPhrases = new Set([
  "Gate fourteen. Boarding at two thirty.",
  "It is one forty-five. You have forty-five minutes.",
  "Three dollars and fifty cents.",
  "You are welcome. Have a nice flight!",
  "Your gate is number fourteen.",
  "The gate number is fourteen.",
  "That is fifteen dollars.",
  "That is thirty dollars total.",
]);

let phraseAlternator = false;

function getVoice(text) {
  // Single words (1-2 words) = Ellen (female student)
  const wordCount = text.trim().split(/\s+/).length;
  if (wordCount <= 2) return { id: ELLEN, name: 'Ellen' };

  // Marlene's own phrases = Ellen
  if (ellenPhrases.has(text)) return { id: ELLEN, name: 'Ellen' };

  // Staff lines = Arthur (male character)
  if (arthurPhrases.has(text)) return { id: ARTHUR, name: 'Arthur' };

  // Listening 2 = Arthur (male shopkeeper)
  if (text === '[lp-listen-l3-2]') return { id: ARTHUR, name: 'Arthur' };

  // For remaining phrases, alternate Arthur/Ellen
  phraseAlternator = !phraseAlternator;
  return phraseAlternator ? { id: ELLEN, name: 'Ellen' } : { id: ARTHUR, name: 'Arthur' };
}

function generateAudio(text, voiceId) {
  // For listening/ordering keys, generate descriptive content
  let actualText = text;
  if (text === '[lp-listen-l3-1]') {
    actualText = "Attention all passengers. Flight four seven two to Rome is now boarding at gate fourteen. Boarding time is two thirty. Please have your boarding pass ready. The flight departs at a quarter to three. Gate fourteen is located in Terminal B. Thank you for flying with us. Have a nice flight.";
  } else if (text === '[lp-listen-l3-2]') {
    actualText = "Welcome to the duty free shop. We have many souvenirs today. This magnet is five dollars. This t-shirt is twenty-five dollars. The chocolate box is fifteen dollars. If you buy two items, you get ten percent off. How much is the perfume? The perfume is one hundred dollars. Cash or credit card? We accept both.";
  } else if (text === '[order-l3]') {
    actualText = "Marlene checks the clock. It is half past one. Excuse me, what gate is flight four seven two? Gate fourteen. She stops at a shop. How much is a coffee? Three dollars and fifty cents. She walks to gate fourteen and waits. Flight four seven two, now boarding at gate fourteen.";
  }

  return new Promise((resolve, reject) => {
    const postData = JSON.stringify({
      text: actualText,
      model_id: 'eleven_monolingual_v1',
      voice_settings: { stability: 0.5, similarity_boost: 0.75 }
    });

    const options = {
      hostname: 'api.elevenlabs.io',
      path: `/v1/text-to-speech/${voiceId}`,
      method: 'POST',
      headers: {
        'Accept': 'audio/mpeg',
        'Content-Type': 'application/json',
        'xi-api-key': API_KEY,
        'Content-Length': Buffer.byteLength(postData)
      }
    };

    const req = https.request(options, (res) => {
      if (res.statusCode !== 200) {
        let body = '';
        res.on('data', d => body += d);
        res.on('end', () => reject(new Error(`HTTP ${res.statusCode}: ${body}`)));
        return;
      }
      const chunks = [];
      res.on('data', chunk => chunks.push(chunk));
      res.on('end', () => resolve(Buffer.concat(chunks)));
    });

    req.on('error', reject);
    req.write(postData);
    req.end();
  });
}

async function main() {
  if (!fs.existsSync(AUDIO_DIR)) fs.mkdirSync(AUDIO_DIR, { recursive: true });

  const entries = Object.entries(audioMap);
  let generated = 0, skipped = 0, errors = 0;

  for (const [text, filePath] of entries) {
    const fullPath = path.join(BASE_DIR, filePath);

    if (fs.existsSync(fullPath)) {
      console.log(`SKIP (exists): ${filePath}`);
      skipped++;
      continue;
    }

    const voice = getVoice(text);
    console.log(`GEN [${voice.name}]: "${text.substring(0, 50)}..." → ${filePath}`);

    try {
      const buffer = await generateAudio(text, voice.id);
      fs.writeFileSync(fullPath, buffer);
      generated++;
      // Rate limit: wait 500ms between requests
      await new Promise(r => setTimeout(r, 500));
    } catch (err) {
      console.error(`ERROR: ${text} — ${err.message}`);
      errors++;
    }
  }

  console.log(`\nDone! Generated: ${generated}, Skipped: ${skipped}, Errors: ${errors}`);
}

main();
