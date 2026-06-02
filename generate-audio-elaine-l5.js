const fs = require('fs');
const path = require('path');
const https = require('https');

const API_KEY = process.env.ELEVENLABS_API_KEY;
if (!API_KEY) { console.error('Missing ELEVENLABS_API_KEY'); process.exit(1); }

const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const BASE_DIR = '/Users/helenmendes/alumni-plano-gerador/public';

// Lesson 5 audioMap entries (Taxi/Transportation)
const audioMap = {
  "Driver": "/audio/elaine-mieko-pinho/driver.mp3",
  "Fare": "/audio/elaine-mieko-pinho/fare.mp3",
  "Destination": "/audio/elaine-mieko-pinho/destination.mp3",
  "Traffic": "/audio/elaine-mieko-pinho/traffic.mp3",
  "Drop off": "/audio/elaine-mieko-pinho/drop_off.mp3",
  "Pick up": "/audio/elaine-mieko-pinho/pick_up.mp3",
  "Meter": "/audio/elaine-mieko-pinho/meter.mp3",
  "Receipt": "/audio/elaine-mieko-pinho/receipt.mp3",
  "The driver took me to the hotel.": "/audio/elaine-mieko-pinho/the_driver_took_me_to_the_hotel.mp3",
  "The fare is about 70 dollars plus tolls.": "/audio/elaine-mieko-pinho/the_fare_is_about_70_dollars_plus_tolls.mp3",
  "What is your destination?": "/audio/elaine-mieko-pinho/what_is_your_destination.mp3",
  "The traffic is heavy today.": "/audio/elaine-mieko-pinho/the_traffic_is_heavy_today.mp3",
  "Could you drop me off at the main entrance?": "/audio/elaine-mieko-pinho/could_you_drop_me_off_at_the_main_entrance.mp3",
  "I will pick you up at 8 AM.": "/audio/elaine-mieko-pinho/i_will_pick_you_up_at_8_am.mp3",
  "The meter shows 72 dollars.": "/audio/elaine-mieko-pinho/the_meter_shows_72_dollars.mp3",
  "Could I have a receipt, please?": "/audio/elaine-mieko-pinho/could_i_have_a_receipt_please.mp3",
  "Could you take me to the Hilton Hotel, please?": "/audio/elaine-mieko-pinho/could_you_take_me_to_the_hilton_hotel_please.mp3",
  "How much is it to Manhattan?": "/audio/elaine-mieko-pinho/how_much_is_it_to_manhattan.mp3",
  "Go straight and turn left at the traffic light.": "/audio/elaine-mieko-pinho/go_straight_and_turn_left_at_the_traffic_light.mp3",
  "Could you drop me off here, please?": "/audio/elaine-mieko-pinho/could_you_drop_me_off_here_please.mp3",
  "Turn right here and then go straight.": "/audio/elaine-mieko-pinho/turn_right_here_and_then_go_straight.mp3",
  "Elaine walks out of JFK Airport with her luggage. She sees a line of yellow taxis and a sign for rideshare pick up. She decides to take a taxi.": "/audio/elaine-mieko-pinho/elaine_taxi_narrative_paragraph1.mp3",
  "Could you take me to the Hilton Hotel in Manhattan, please? she asks the driver. Sure! My name is Miguel. It is about 45 minutes with traffic, he says.": "/audio/elaine-mieko-pinho/elaine_taxi_narrative_paragraph2.mp3",
  "How much is it to Manhattan? Elaine asks. The fare is about 70 dollars plus tolls, Miguel explains.": "/audio/elaine-mieko-pinho/elaine_taxi_narrative_paragraph3.mp3",
  "Could you take me to the Hilton Hotel in Manhattan, please?": "/audio/elaine-mieko-pinho/could_you_take_me_to_the_hilton_hotel_in_manhattan.mp3",
  "Sure! My name is Miguel. It is about 45 minutes with traffic.": "/audio/elaine-mieko-pinho/sure_my_name_is_miguel_45_minutes.mp3",
  "The fare is about 70 dollars plus tolls.": "/audio/elaine-mieko-pinho/the_fare_is_about_70_dollars_plus_tolls_v2.mp3",
  "Could you drop me off at the main entrance, please?": "/audio/elaine-mieko-pinho/could_you_drop_me_off_at_main_entrance_please.mp3",
  "Here we are. The Hilton Hotel.": "/audio/elaine-mieko-pinho/here_we_are_the_hilton_hotel.mp3",
  "The meter shows 72 dollars.": "/audio/elaine-mieko-pinho/the_meter_shows_72_dollars_v2.mp3",
  "Thank you, Miguel! You were very kind.": "/audio/elaine-mieko-pinho/thank_you_miguel_you_were_very_kind.mp3",
  "Here is your receipt. Have a great day!": "/audio/elaine-mieko-pinho/here_is_your_receipt_have_a_great_day.mp3",
  "listening9_taxi_full": "/audio/elaine-mieko-pinho/listening9_taxi_ride_full.mp3",
  "listening10_rideshare_full": "/audio/elaine-mieko-pinho/listening10_rideshare_notification_full.mp3",
  "Your driver is arriving in 3 minutes. A white Toyota Camry, license plate TLC-4829. Your driver is Carlos. Estimated time to destination: 35 minutes. Fare estimate: 42 to 55 dollars.": "/audio/elaine-mieko-pinho/rideshare_app_notification.mp3",
  "Could you take me to Times Square, please?": "/audio/elaine-mieko-pinho/could_you_take_me_to_times_square_please.mp3",
  "How much is it to the airport?": "/audio/elaine-mieko-pinho/how_much_is_it_to_the_airport.mp3",
  "Go straight and turn right at the next corner.": "/audio/elaine-mieko-pinho/go_straight_and_turn_right_at_the_next_corner.mp3",
  "Could you drop me off at the corner, please?": "/audio/elaine-mieko-pinho/could_you_drop_me_off_at_the_corner_please.mp3",
  "The traffic is really bad right now.": "/audio/elaine-mieko-pinho/the_traffic_is_really_bad_right_now.mp3",
  "Is there a faster way to get there?": "/audio/elaine-mieko-pinho/is_there_a_faster_way_to_get_there.mp3",
  "You exit the airport and see taxis outside.": "/audio/elaine-mieko-pinho/you_exit_the_airport_and_see_taxis_outside.mp3",
  "You tell the driver your destination.": "/audio/elaine-mieko-pinho/you_tell_the_driver_your_destination.mp3",
  "You watch the meter during the ride.": "/audio/elaine-mieko-pinho/you_watch_the_meter_during_the_ride.mp3",
  "You arrive and ask the driver to drop you off.": "/audio/elaine-mieko-pinho/you_arrive_and_ask_the_driver_to_drop_you_off.mp3",
  "You pay the fare and ask for a receipt.": "/audio/elaine-mieko-pinho/you_pay_the_fare_and_ask_for_a_receipt.mp3",
  "Could you take me to the Hilton Hotel, please?": "/audio/elaine-mieko-pinho/could_you_take_me_to_the_hilton_hotel_please_v2.mp3",
  "How much is it to Manhattan?": "/audio/elaine-mieko-pinho/how_much_is_it_to_manhattan_v2.mp3",
  "Go straight and turn left at the traffic light.": "/audio/elaine-mieko-pinho/go_straight_turn_left_traffic_light_v2.mp3",
  "Could I have a receipt, please?": "/audio/elaine-mieko-pinho/could_i_have_a_receipt_please_v2.mp3",
};

// Voice assignment rules:
// - 1-2 words: Arthur
// - 3+ words: alternate Arthur/Ellen
// - Driver Miguel lines: Arthur
// - Elaine lines: Ellen
// - Narrative/listening keys: Ellen
function getVoice(text) {
  const words = text.trim().split(/\s+/).length;

  // Special keys for listening (full audio tracks)
  if (text.startsWith('listening')) return ELLEN;

  // 1-2 words = Arthur
  if (words <= 2) return ARTHUR;

  // Driver Miguel lines
  const miguelPhrases = [
    "Sure! My name is Miguel. It is about 45 minutes with traffic.",
    "Here we are. The Hilton Hotel.",
    "Here is your receipt. Have a great day!",
    "The meter shows 72 dollars.",
  ];
  for (const p of miguelPhrases) {
    if (text === p || text.startsWith(p)) return ARTHUR;
  }

  // Elaine lines (she asks / she says / Elaine)
  const elainePhrases = [
    "Could you take me to the Hilton Hotel in Manhattan, please?",
    "How much is it to Manhattan?",
    "Could you drop me off at the main entrance, please?",
    "Thank you, Miguel! You were very kind.",
    "Could you take me to the Hilton Hotel, please?",
    "Could I have a receipt, please?",
    "Could you take me to Times Square, please?",
    "Could you drop me off at the corner, please?",
    "Could you drop me off here, please?",
    "Could you drop me off at the main entrance?",
    "Is there a faster way to get there?",
    "How much is it to the airport?",
  ];
  for (const p of elainePhrases) {
    if (text === p) return ELLEN;
  }

  // Alternate for remaining 3+ word phrases
  return null; // will be assigned in alternation
}

function generateTTS(text, voiceId, filePath) {
  return new Promise((resolve, reject) => {
    // For listening keys, use the key as-is but generate with a descriptive text isn't useful
    // Skip listening keys - they need manual full-track generation
    if (text.startsWith('listening')) {
      console.log(`  [SKIP-LISTENING] "${text}" — needs full track, not TTS`);
      return resolve('skip-listening');
    }

    const body = JSON.stringify({
      text: text,
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
        'xi-api-key': API_KEY
      }
    };

    const req = https.request(options, (res) => {
      if (res.statusCode !== 200) {
        let errBody = '';
        res.on('data', d => errBody += d);
        res.on('end', () => reject(new Error(`HTTP ${res.statusCode}: ${errBody}`)));
        return;
      }
      const chunks = [];
      res.on('data', chunk => chunks.push(chunk));
      res.on('end', () => {
        const buffer = Buffer.concat(chunks);
        const dir = path.dirname(filePath);
        if (!fs.existsSync(dir)) fs.mkdirSync(dir, { recursive: true });
        fs.writeFileSync(filePath, buffer);
        resolve('generated');
      });
    });

    req.on('error', reject);
    req.write(body);
    req.end();
  });
}

function sleep(ms) { return new Promise(r => setTimeout(r, ms)); }

async function main() {
  const entries = Object.entries(audioMap);
  let generated = 0, skipped = 0, skippedListening = 0;
  let alternateIndex = 0; // for alternation on 3+ word phrases without explicit voice

  console.log(`\nTotal Lesson 5 entries: ${entries.length}\n`);

  for (const [text, audioPath] of entries) {
    const filePath = path.join(BASE_DIR, audioPath);

    // Skip if file exists and > 1KB
    if (fs.existsSync(filePath)) {
      const stat = fs.statSync(filePath);
      if (stat.size > 1024) {
        console.log(`  [SKIP] ${path.basename(audioPath)} (${(stat.size/1024).toFixed(1)}KB)`);
        skipped++;
        continue;
      }
    }

    // Determine voice
    let voice = getVoice(text);
    if (voice === null) {
      // Alternate Arthur/Ellen
      voice = (alternateIndex % 2 === 0) ? ARTHUR : ELLEN;
      alternateIndex++;
    }

    const voiceName = voice === ARTHUR ? 'Arthur' : 'Ellen';
    console.log(`  [GEN] ${path.basename(audioPath)} — voice: ${voiceName}`);

    try {
      const result = await generateTTS(text, voice, filePath);
      if (result === 'skip-listening') {
        skippedListening++;
      } else {
        generated++;
        await sleep(500);
      }
    } catch (err) {
      console.error(`  [ERROR] ${path.basename(audioPath)}: ${err.message}`);
    }
  }

  console.log(`\n--- REPORT ---`);
  console.log(`Generated: ${generated}`);
  console.log(`Skipped (exist >1KB): ${skipped}`);
  console.log(`Skipped (listening tracks): ${skippedListening}`);
  console.log(`Total entries: ${entries.length}`);
}

main().catch(console.error);
