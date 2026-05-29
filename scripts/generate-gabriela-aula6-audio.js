#!/usr/bin/env node
/**
 * Generate ElevenLabs audio for Gabriela Pires - Aula 6
 * Voice alternation: Ellen (female, student phrases) + Arthur (male, agent/general)
 * Usage: ELEVENLABS_API_KEY=... node scripts/generate-gabriela-aula6-audio.js
 */

const fs = require('fs');
const path = require('path');

const API_URL = 'https://api.elevenlabs.io/v1/text-to-speech';
const VOICES = {
  arthur: 'sfJopaWaOtauCD3HKX6Q',
  ellen: 'BIvP0GN1cAtSRTxNHnWS',
};
const API_KEY = process.env.ELEVENLABS_API_KEY;
const OUTPUT_DIR = path.join(__dirname, '..', 'public', 'audio', 'gabriela-pires');

if (!API_KEY) {
  console.error('Set ELEVENLABS_API_KEY env var');
  process.exit(1);
}
if (!fs.existsSync(OUTPUT_DIR)) fs.mkdirSync(OUTPUT_DIR, { recursive: true });

// Phrases for Aula 6 with voice assignment
// Ellen = Gabriela's phrases (female student)
// Arthur = vocab words, agent dialogue, general phrases
const phrases = [
  // Vocab words (short) - Arthur
  { text: "O'clock", file: "oclock.mp3", voice: "arthur" },
  { text: "Quarter", file: "quarter.mp3", voice: "arthur" },
  { text: "Half past", file: "half_past.mp3", voice: "arthur" },
  { text: "Noon", file: "noon.mp3", voice: "arthur" },
  { text: "Midnight", file: "midnight.mp3", voice: "arthur" },
  { text: "Flight", file: "flight.mp3", voice: "arthur" },
  { text: "Ticket", file: "ticket.mp3", voice: "arthur" },
  { text: "Price", file: "price.mp3", voice: "arthur" },
  { text: "Departure", file: "departure.mp3", voice: "arthur" },
  { text: "Arrival", file: "arrival.mp3", voice: "arthur" },
  { text: "Change", file: "change.mp3", voice: "arthur" },
  { text: "Total", file: "total.mp3", voice: "arthur" },
  { text: "February 3rd", file: "february_3rd.mp3", voice: "ellen" },
  { text: "March 15th", file: "march_15th.mp3", voice: "arthur" },

  // Vocab examples - alternating
  { text: "It is three o'clock.", file: "it_is_three_oclock.mp3", voice: "arthur" },
  { text: "It is a quarter past two.", file: "it_is_a_quarter_past_two.mp3", voice: "ellen" },
  { text: "It is half past ten.", file: "it_is_half_past_ten.mp3", voice: "arthur" },
  { text: "We have lunch at noon.", file: "we_have_lunch_at_noon.mp3", voice: "ellen" },
  { text: "The flight arrives at midnight.", file: "the_flight_arrives_at_midnight.mp3", voice: "arthur" },
  { text: "My flight is at nine o'clock.", file: "my_flight_is_at_nine_oclock.mp3", voice: "ellen" },
  { text: "How much is the ticket?", file: "how_much_is_the_ticket.mp3", voice: "ellen" },
  { text: "What is the price?", file: "what_is_the_price.mp3", voice: "ellen" },

  // Grammar / time expressions - alternating
  { text: "What time is it?", file: "what_time_is_it.mp3", voice: "ellen" },
  { text: "It is a quarter to five.", file: "it_is_a_quarter_to_five.mp3", voice: "arthur" },
  { text: "My flight is on February 3rd.", file: "my_flight_is_on_february_3rd.mp3", voice: "ellen" },
  { text: "How much does this cost?", file: "how_much_does_this_cost.mp3", voice: "ellen" },
  { text: "Excuse me, what time is it?", file: "excuse_me_what_time_is_it.mp3", voice: "ellen" },
  { text: "The museum opens at ten o'clock.", file: "the_museum_opens_at_ten_oclock.mp3", voice: "arthur" },
  { text: "The Eiffel Tower visit is at a quarter past four.", file: "the_eiffel_tower_visit_is_at_a_quarter_past_four.mp3", voice: "arthur" },
  { text: "Lunch is at half past twelve.", file: "lunch_is_at_half_past_twelve.mp3", voice: "ellen" },
  { text: "The departure time is eight thirty.", file: "the_departure_time_is_eight_thirty.mp3", voice: "arthur" },
  { text: "The departure time is 8 AM.", file: "the_departure_time_is_8_am.mp3", voice: "arthur" },
  { text: "The arrival time is noon.", file: "the_arrival_time_is_noon.mp3", voice: "arthur" },
  { text: "Here is your change.", file: "here_is_your_change.mp3", voice: "arthur" },
  { text: "The total is twenty-six euros.", file: "the_total_is_twentysix_euros.mp3", voice: "arthur" },
  { text: "It is seven o'clock.", file: "it_is_seven_oclock.mp3", voice: "arthur" },
  { text: "It is a quarter past nine.", file: "it_is_a_quarter_past_nine.mp3", voice: "ellen" },
  { text: "It is half past twelve.", file: "it_is_half_past_twelve.mp3", voice: "arthur" },
  { text: "It is midnight.", file: "it_is_midnight.mp3", voice: "arthur" },
  { text: "It is noon.", file: "it_is_noon.mp3", voice: "ellen" },
  { text: "It is eight forty-five.", file: "it_is_eight_fortyfive.mp3", voice: "arthur" },
  { text: "The train departs at a quarter to nine.", file: "the_train_departs_at_a_quarter_to_nine.mp3", voice: "arthur" },

  // Dialogue - Agent (Arthur) and Gabriela (Ellen)
  { text: "Good afternoon! Welcome to the Louvre. How can I help you?", file: "good_afternoon_welcome_to_the_louvre.mp3", voice: "arthur" },
  { text: "One student ticket, please. How much is it?", file: "one_student_ticket_please_how_much_is_it.mp3", voice: "ellen" },
  { text: "It is 15 euros. Here is your ticket.", file: "it_is_15_euros_here_is_your_ticket.mp3", voice: "arthur" },
  { text: "Thank you! What time does the museum close?", file: "thank_you_what_time_does_the_museum_close.mp3", voice: "ellen" },
  { text: "We close at six o'clock.", file: "we_close_at_six_oclock.mp3", voice: "arthur" },
  { text: "And what time is the next guided tour?", file: "and_what_time_is_the_next_guided_tour.mp3", voice: "ellen" },
  { text: "The next tour starts at a quarter past three. It is in English.", file: "the_next_tour_starts_at_a_quarter_past_three_in_english.mp3", voice: "arthur" },
  { text: "Perfect! Thank you very much!", file: "perfect_thank_you_very_much.mp3", voice: "ellen" },
  { text: "Enjoy your visit!", file: "enjoy_your_visit.mp3", voice: "arthur" },
  { text: "The next tour starts at a quarter past three.", file: "the_next_tour_starts_at_a_quarter_past_three.mp3", voice: "arthur" },
  { text: "One ticket, please. How much is it?", file: "one_ticket_please_how_much_is_it.mp3", voice: "ellen" },
  { text: "It is ten euros.", file: "it_is_ten_euros.mp3", voice: "arthur" },
  { text: "Here you go. Thank you!", file: "here_you_go_thank_you.mp3", voice: "ellen" },
  { text: "What time does the next tour start?", file: "what_time_does_the_next_tour_start.mp3", voice: "ellen" },
  { text: "One student ticket, please. How much is it?", file: "one_student_ticket_please_how_much_is_it_dialogue.mp3", voice: "ellen" },

  // Listening 2 - flight conversation
  { text: "When is your flight to Paris?", file: "when_is_your_flight_to_paris.mp3", voice: "arthur" },
  { text: "My flight is on February 3rd, 2027.", file: "my_flight_is_on_february_3rd_2027.mp3", voice: "ellen" },
  { text: "What time does it depart?", file: "what_time_does_it_depart.mp3", voice: "arthur" },
  { text: "It departs at nine fifteen in the morning.", file: "it_departs_at_nine_fifteen_in_the_morning.mp3", voice: "ellen" },
  { text: "And what time does it arrive?", file: "and_what_time_does_it_arrive.mp3", voice: "arthur" },
  { text: "It arrives at eleven thirty at night.", file: "it_arrives_at_eleven_thirty_at_night.mp3", voice: "ellen" },
  { text: "That is a long flight!", file: "that_is_a_long_flight.mp3", voice: "arthur" },
  { text: "Yes! But I am so excited!", file: "yes_but_i_am_so_excited.mp3", voice: "ellen" },

  // Full listening text
  { text: "Gabriela is planning her trip to Paris. Her flight is on February 3rd, 2027. The departure time is 9:15 AM from São Paulo. She arrives in Paris at 11:30 PM. On February 4th, she visits the Louvre at 10 o'clock. Lunch is at half past twelve at a French café. The Eiffel Tower visit is at a quarter past four. A ticket to the Eiffel Tower costs 26 euros. On February 5th, she goes to Versailles. The train departs at a quarter to nine.", file: "gabriela_is_planning_her_trip_to_paris_full_listening.mp3", voice: "ellen" },

  // Speech practice / survival phrases - Ellen (Gabriela's voice)
  { text: "Excuse me, what time is it? It is half past ten.", file: "excuse_me_what_time_is_it_half_past_ten.mp3", voice: "ellen" },
  { text: "My flight is on February 3rd. What is the price?", file: "my_flight_is_on_february_3rd_what_is_the_price.mp3", voice: "ellen" },
  { text: "One ticket, please. How much does this cost?", file: "one_ticket_please_how_much_does_this_cost.mp3", voice: "ellen" },
  { text: "The museum opens at ten. It closes at six.", file: "the_museum_opens_at_ten_it_closes_at_six.mp3", voice: "arthur" },
  { text: "What time is your English class? My class is at three o'clock.", file: "what_time_is_your_english_class_my_class_is_at_three_oclock.mp3", voice: "ellen" },

  // Think response
  { text: "Hi, my name is Gabriela. My flight arrived on February 3rd. One ticket, please. How much is it? What time does the tower close?", file: "hi_my_name_is_gabriela_my_flight_arrived_on_february_3rd.mp3", voice: "ellen" },
];

async function generateAudio(text, filename, voiceId) {
  const filePath = path.join(OUTPUT_DIR, filename);
  if (fs.existsSync(filePath)) {
    return { path: filePath, skipped: true };
  }

  const response = await fetch(`${API_URL}/${voiceId}`, {
    method: 'POST',
    headers: {
      'xi-api-key': API_KEY,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      text: text,
      model_id: 'eleven_multilingual_v2',
      voice_settings: {
        stability: 0.5,
        similarity_boost: 0.75,
        style: 0.0,
        use_speaker_boost: true,
      },
    }),
  });

  if (!response.ok) {
    const err = await response.text();
    throw new Error(`ElevenLabs error for "${text.substring(0, 40)}...": ${response.status} - ${err}`);
  }

  const buffer = Buffer.from(await response.arrayBuffer());
  fs.writeFileSync(filePath, buffer);
  return { path: filePath, skipped: false };
}

async function main() {
  console.log(`Generating ${phrases.length} audio files for Aula 6...`);
  console.log(`Output: ${OUTPUT_DIR}\n`);

  let generated = 0, skipped = 0, errors = 0;

  for (const p of phrases) {
    try {
      const result = await generateAudio(p.text, p.file, VOICES[p.voice]);
      if (result.skipped) {
        skipped++;
        process.stdout.write('.');
      } else {
        generated++;
        process.stdout.write('+');
        // Rate limit
        await new Promise(r => setTimeout(r, 300));
      }
    } catch (err) {
      errors++;
      console.error(`\n  [ERROR] ${err.message}`);
    }
  }

  console.log(`\n\nDone: ${generated} generated, ${skipped} skipped, ${errors} errors`);
}

main().catch(console.error);
