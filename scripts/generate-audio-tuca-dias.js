const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const DIR = path.join(__dirname, '..', 'public', 'audio', 'tuca-dias');

// Tuca is female → Ellen for her lines and single vocab words
// David is male → Arthur for his lines
// General phrases without character → ALTERNATE Arthur/Ellen
const PHRASES = [
  // ===== Emergency / Survival phrases (Tuca = female student → Ellen for her lines, alternate for general) =====
  { text: "Could you repeat that, please?", voice: ELLEN, file: "could_you_repeat_that_please.mp3" },
  { text: "I am not sure I understand. Could you explain?", voice: ARTHUR, file: "i_am_not_sure_i_understand_could_you_explain.mp3" },
  { text: "Let me think about that for a moment.", voice: ELLEN, file: "let_me_think_about_that_for_a_moment.mp3" },
  { text: "I am from Brazil. I have a coffee farm.", voice: ELLEN, file: "i_am_from_brazil_i_have_a_coffee_farm.mp3" },
  { text: "Could you speak a little slower, please?", voice: ARTHUR, file: "could_you_speak_a_little_slower_please.mp3" },

  // ===== Vocabulary words (1-2 words → Ellen, student is female) =====
  { text: "Journey", voice: ELLEN, file: "journey.mp3" },
  { text: "Destination", voice: ELLEN, file: "destination.mp3" },
  { text: "Local", voice: ELLEN, file: "local.mp3" },
  { text: "Culture", voice: ELLEN, file: "culture.mp3" },
  { text: "Adventure", voice: ELLEN, file: "adventure.mp3" },
  { text: "Explore", voice: ELLEN, file: "explore.mp3" },
  { text: "Border", voice: ELLEN, file: "border.mp3" },
  { text: "Route", voice: ELLEN, file: "route.mp3" },
  { text: "Experience", voice: ELLEN, file: "experience.mp3" },
  { text: "International", voice: ELLEN, file: "international.mp3" },

  // ===== Vocabulary example sentences (alternate Arthur/Ellen) =====
  { text: "My journey to Morocco was unforgettable.", voice: ARTHUR, file: "my_journey_to_morocco_was_unforgettable.mp3" },
  { text: "Our destination was a small village in the mountains.", voice: ELLEN, file: "our_destination_was_a_small_village_in_the_mountains.mp3" },
  { text: "I always try to eat local food when I travel.", voice: ARTHUR, file: "i_always_try_to_eat_local_food_when_i_travel.mp3" },
  { text: "I love learning about the culture of new places.", voice: ELLEN, file: "i_love_learning_about_the_culture_of_new_places.mp3" },
  { text: "Traveling is always an adventure.", voice: ARTHUR, file: "traveling_is_always_an_adventure.mp3" },
  { text: "I want to explore the streets of Tokyo.", voice: ELLEN, file: "i_want_to_explore_the_streets_of_tokyo.mp3" },
  { text: "We crossed the border between Spain and Portugal.", voice: ARTHUR, file: "we_crossed_the_border_between_spain_and_portugal.mp3" },
  { text: "What is the best route to the airport?", voice: ELLEN, file: "what_is_the_best_route_to_the_airport.mp3" },
  { text: "That was an amazing experience.", voice: ARTHUR, file: "that_was_an_amazing_experience.mp3" },
  { text: "She works for an international company.", voice: ELLEN, file: "she_works_for_an_international_company.mp3" },

  // ===== Fill-in-the-blank / practice phrases (alternate Arthur/Ellen) =====
  { text: "I travel to new places every year.", voice: ARTHUR, file: "i_travel_to_new_places_every_year.mp3" },
  { text: "Last year I went to Mexico City.", voice: ELLEN, file: "last_year_i_went_to_mexico_city.mp3" },
  { text: "I grow coffee in Sao Sebastiao da Grama.", voice: ARTHUR, file: "i_grow_coffee_in_sao_sebastiao_da_grama.mp3" },
  { text: "I visited the old market and tried local food.", voice: ELLEN, file: "i_visited_the_old_market_and_tried_local_food.mp3" },
  { text: "The most interesting thing was the local culture.", voice: ARTHUR, file: "the_most_interesting_thing_was_the_local_culture.mp3" },
  { text: "I usually travel with my family.", voice: ELLEN, file: "i_usually_travel_with_my_family.mp3" },
  { text: "Last summer I explored the south of France.", voice: ARTHUR, file: "last_summer_i_explored_the_south_of_france.mp3" },
  { text: "The journey took about twelve hours.", voice: ELLEN, file: "the_journey_took_about_twelve_hours.mp3" },
  { text: "I live in a small town in Sao Paulo state.", voice: ARTHUR, file: "i_live_in_a_small_town_in_sao_paulo_state.mp3" },
  { text: "I met wonderful people on my last trip.", voice: ELLEN, file: "i_met_wonderful_people_on_my_last_trip.mp3" },

  // ===== Reading / Context text sentences (alternate Arthur/Ellen — Anna story) =====
  { text: "Anna arrived in Marrakech after a long journey from London.", voice: ARTHUR, file: "anna_arrived_in_marrakech_after_a_long_journey.mp3" },
  { text: "Her destination was a small riad in the old city.", voice: ELLEN, file: "her_destination_was_a_small_riad.mp3" },
  { text: "She explored the local markets and tried traditional food.", voice: ARTHUR, file: "she_explored_the_local_markets.mp3" },
  { text: "The culture was very different from home.", voice: ELLEN, file: "the_culture_was_very_different_from_home.mp3" },
  { text: "Every day was a new adventure.", voice: ARTHUR, file: "every_day_was_a_new_adventure.mp3" },
  { text: "She crossed the border into the desert.", voice: ELLEN, file: "she_crossed_the_border_into_the_desert.mp3" },
  { text: "The experience changed her life.", voice: ARTHUR, file: "the_experience_changed_her_life.mp3" },

  // ===== Speech / Pronunciation cards (Tuca = female → Ellen for her own lines) =====
  { text: "I am Tuca. I am from Brazil.", voice: ELLEN, file: "i_am_tuca_i_am_from_brazil.mp3" },
  { text: "I have a coffee farm in Sao Paulo state.", voice: ELLEN, file: "i_have_a_coffee_farm_in_sao_paulo_state.mp3" },
  { text: "I love traveling and meeting new people.", voice: ELLEN, file: "i_love_traveling_and_meeting_new_people.mp3" },
  { text: "Last year I visited Morocco. It was incredible.", voice: ELLEN, file: "last_year_i_visited_morocco_it_was_incredible.mp3" },
  { text: "I usually travel once or twice a year.", voice: ELLEN, file: "i_usually_travel_once_or_twice_a_year.mp3" },

  // ===== Dialogue — David = Arthur (male character) =====
  { text: "Hi! I am David. I am from California.", voice: ARTHUR, file: "hi_i_am_david_i_am_from_california.mp3" },
  { text: "What brings you to Morocco?", voice: ARTHUR, file: "what_brings_you_to_morocco.mp3" },
  { text: "That sounds great! What do you do back home?", voice: ARTHUR, file: "that_sounds_great_what_do_you_do_back_home.mp3" },
  { text: "I am a photographer. I travel a lot for work. How about you?", voice: ARTHUR, file: "i_am_a_photographer_i_travel_a_lot.mp3" },
  { text: "Wow, that is fascinating! I visited a coffee farm in Colombia last year.", voice: ARTHUR, file: "wow_that_is_fascinating_i_visited_a_coffee_farm.mp3" },
  { text: "What is your favorite destination so far?", voice: ARTHUR, file: "what_is_your_favorite_destination_so_far.mp3" },
  { text: "I think Japan. The culture is so different and beautiful.", voice: ARTHUR, file: "i_think_japan_the_culture_is_so_different.mp3" },
  { text: "You should! The local food is incredible.", voice: ARTHUR, file: "you_should_the_local_food_is_incredible.mp3" },
  { text: "I definitely will. Nice talking to you, Tuca!", voice: ARTHUR, file: "i_definitely_will_nice_talking.mp3" },

  // ===== Dialogue — Tuca = Ellen (female character) =====
  { text: "Nice to meet you, David! I am Tuca, from Brazil.", voice: ELLEN, file: "nice_to_meet_you_david_i_am_tuca_from_brazil.mp3" },
  { text: "I love exploring new cultures. This is my first time here.", voice: ELLEN, file: "i_love_exploring_new_cultures_this_is_my_first_time.mp3" },
  { text: "I have a coffee farm in Brazil. I grow specialty coffee.", voice: ELLEN, file: "i_have_a_coffee_farm_in_brazil.mp3" },
  { text: "Really? I went to Colombia too! The coffee culture there is amazing.", voice: ELLEN, file: "really_i_went_to_colombia_too.mp3" },
  { text: "Japan is on my list! I want to explore Tokyo and Kyoto.", voice: ELLEN, file: "japan_is_on_my_list.mp3" },

  // ===== Listening 1 — Tuca's self-introduction (Ellen — long passage) =====
  { text: "Hello, my name is Tuca Dias. I am sixty-one years old and I live in Sao Sebastiao da Grama, a small town in Sao Paulo state, Brazil. I have a coffee farm where I grow specialty coffee. I love traveling. Last year, I went to Mexico City with my family. We explored the local markets, visited amazing museums, and tried incredible food. The culture was so rich and different. I usually travel once or twice a year. My favorite destinations are places with interesting culture and good food. I met wonderful people on my last trip. The most interesting thing about traveling is learning about different cultures. Next, I want to visit Japan and walk the Mont Blanc trail in the Alps.", voice: ELLEN, file: "listening_tuca_introduction.mp3" },

  // ===== Listening 2 — Airport announcement (Arthur — neutral male PA voice) =====
  { text: "Attention, please. Flight AA 1045 to Mexico City is now boarding at Gate 12. All passengers, please proceed to the gate with your boarding pass and identification ready. Thank you.", voice: ARTHUR, file: "listening_airport_announcement.mp3" },

  // ===== Additional speech/practice phrases (Tuca context → Ellen) =====
  { text: "I grow specialty coffee in a small town.", voice: ELLEN, file: "i_grow_specialty_coffee_in_a_small_town.mp3" },
  { text: "Last year I went to Mexico City with my family.", voice: ELLEN, file: "last_year_i_went_to_mexico_city_with_my_family.mp3" },
  { text: "We explored the local markets and tried amazing food.", voice: ELLEN, file: "we_explored_the_local_markets_and_tried_amazing_food.mp3" },
  { text: "The culture was very rich and different from Brazil.", voice: ELLEN, file: "the_culture_was_very_rich_and_different.mp3" },

  // ===== AULA 2 — AT THE AIRPORT =====

  // Vocabulary words (1-2 words → Ellen, student is female)
  { text: "Boarding pass", voice: ELLEN, file: "boarding_pass.mp3" },
  { text: "Check-in", voice: ELLEN, file: "check_in.mp3" },
  { text: "Gate", voice: ELLEN, file: "gate.mp3" },
  { text: "Departure", voice: ELLEN, file: "departure.mp3" },
  { text: "Luggage", voice: ELLEN, file: "luggage.mp3" },
  { text: "Delay", voice: ELLEN, file: "delay.mp3" },
  { text: "Announcement", voice: ELLEN, file: "announcement.mp3" },
  { text: "Terminal", voice: ELLEN, file: "terminal.mp3" },
  { text: "Carry-on", voice: ELLEN, file: "carry_on.mp3" },
  { text: "Security", voice: ELLEN, file: "security.mp3" },

  // Vocabulary example sentences (alternate Arthur/Ellen)
  { text: "Please have your boarding pass ready before you reach the gate.", voice: ARTHUR, file: "please_have_your_boarding_pass_ready.mp3" },
  { text: "The check-in counter closes 45 minutes before departure.", voice: ELLEN, file: "the_check_in_counter_closes.mp3" },
  { text: "All passengers for Flight AM 742, please proceed to Gate 22.", voice: ARTHUR, file: "all_passengers_flight_am742_gate22.mp3" },
  { text: "The departure time has been changed to 11:15.", voice: ELLEN, file: "the_departure_time_has_been_changed.mp3" },
  { text: "You can pick up your luggage at the baggage claim area.", voice: ARTHUR, file: "you_can_pick_up_your_luggage.mp3" },
  { text: "There is a 30-minute delay due to weather conditions.", voice: ELLEN, file: "there_is_a_30_minute_delay.mp3" },
  { text: "Listen to the announcement for your gate number.", voice: ARTHUR, file: "listen_to_the_announcement.mp3" },
  { text: "Terminal 3 is for international flights.", voice: ELLEN, file: "terminal_3_is_for_international.mp3" },
  { text: "Your carry-on must fit under the seat in front of you.", voice: ARTHUR, file: "your_carry_on_must_fit.mp3" },
  { text: "Please remove your laptop at the security checkpoint.", voice: ELLEN, file: "please_remove_your_laptop.mp3" },

  // Grammar example sentences (alternate Arthur/Ellen)
  { text: "I am waiting at the gate.", voice: ARTHUR, file: "i_am_waiting_at_the_gate.mp3" },
  { text: "She is checking in right now.", voice: ELLEN, file: "she_is_checking_in_right_now.mp3" },
  { text: "They are boarding the plane.", voice: ARTHUR, file: "they_are_boarding_the_plane.mp3" },
  { text: "We are going to fly to Mexico City.", voice: ELLEN, file: "we_are_going_to_fly_to_mexico_city.mp3" },
  { text: "I am going to wait at the gate.", voice: ARTHUR, file: "i_am_going_to_wait_at_the_gate.mp3" },
  { text: "He is not going to check any luggage.", voice: ELLEN, file: "he_is_not_going_to_check_luggage.mp3" },
  { text: "Are you going to fly today?", voice: ARTHUR, file: "are_you_going_to_fly_today.mp3" },

  // Dialogue — Mark = Arthur (male airport agent)
  { text: "Good morning! Where are you flying to today?", voice: ARTHUR, file: "good_morning_where_are_you_flying.mp3" },
  { text: "Great! Can I see your passport and boarding pass, please?", voice: ARTHUR, file: "can_i_see_your_passport_and_boarding_pass.mp3" },
  { text: "Perfect. Are you checking any luggage today?", voice: ARTHUR, file: "are_you_checking_any_luggage_today.mp3" },
  { text: "Your luggage is all set. Your flight is departing from Gate 22.", voice: ARTHUR, file: "your_luggage_is_all_set.mp3" },
  { text: "There is a small delay. They are boarding at 11:15 instead of 10:45.", voice: ARTHUR, file: "there_is_a_small_delay.mp3" },

  // Dialogue — Tuca = Ellen (female character)
  { text: "Good morning! I am going to Mexico City.", voice: ELLEN, file: "good_morning_i_am_going_to_mexico_city.mp3" },
  { text: "Here you go. I checked in online last night.", voice: ELLEN, file: "here_you_go_i_checked_in_online.mp3" },
  { text: "Yes, I have one suitcase. And this is my carry-on.", voice: ELLEN, file: "yes_i_have_one_suitcase.mp3" },
  { text: "Thank you! Is the flight on time?", voice: ELLEN, file: "thank_you_is_the_flight_on_time.mp3" },
  { text: "No problem. I am going to wait at the gate. Thank you!", voice: ELLEN, file: "no_problem_i_am_going_to_wait.mp3" },

  // Listening 1 — Boarding announcement (Arthur — PA voice)
  { text: "Attention all passengers. Flight AM 742 to Mexico City is now ready for boarding at Gate 22. We are boarding rows 20 through 35 first. Please have your boarding pass and identification ready. Thank you.", voice: ARTHUR, file: "listening_l2_boarding_announcement.mp3" },

  // Listening 2 — Gate change announcement (Arthur — PA voice)
  { text: "Attention, passengers on Flight AM 742 to Mexico City. There has been a gate change. Your flight is now departing from Gate 18, not Gate 22. Please proceed to Gate 18 immediately. Boarding is in progress. Thank you.", voice: ARTHUR, file: "listening_l2_gate_change.mp3" },

  // Speech / Pronunciation cards (Tuca's lines → Ellen)
  { text: "I would like to check in for my flight, please.", voice: ELLEN, file: "i_would_like_to_check_in.mp3" },
  { text: "Excuse me, where is Gate 22?", voice: ELLEN, file: "excuse_me_where_is_gate_22.mp3" },
  { text: "Is there a delay on Flight AM 742?", voice: ELLEN, file: "is_there_a_delay_on_flight_am742.mp3" },
  { text: "Can I take this bag as a carry-on?", voice: ELLEN, file: "can_i_take_this_bag_as_carry_on.mp3" },
  { text: "My boarding pass says Gate 22 but I heard an announcement about a change.", voice: ELLEN, file: "my_boarding_pass_says_gate_22.mp3" },
  { text: "Where is the nearest security checkpoint?", voice: ELLEN, file: "where_is_the_nearest_security.mp3" },

  // Fill-in-the-blank / practice phrases (alternate)
  { text: "I am going to fly to Mexico City next month.", voice: ELLEN, file: "i_am_going_to_fly_to_mexico_city_next_month.mp3" },
  { text: "I am checking in for my flight.", voice: ARTHUR, file: "i_am_checking_in_for_my_flight.mp3" },
  { text: "The plane is departing in one hour.", voice: ELLEN, file: "the_plane_is_departing_in_one_hour.mp3" },
  { text: "We are going to arrive at 3 PM.", voice: ARTHUR, file: "we_are_going_to_arrive_at_3pm.mp3" },
  { text: "She is looking for her boarding pass.", voice: ELLEN, file: "she_is_looking_for_her_boarding_pass.mp3" },

  // Error sentences (for spot the error)
  { text: "They going to miss the flight.", voice: ARTHUR, file: "they_going_to_miss_the_flight.mp3" },
  { text: "I am go to the airport now.", voice: ELLEN, file: "i_am_go_to_the_airport_now.mp3" },

  // ===== LESSON 3: Have You Ever? — Present Perfect for Life Experiences =====

  // Vocabulary words (1-2 words → Ellen, student is female)
  { text: "Cuisine", voice: ELLEN, file: "cuisine.mp3" },
  { text: "Nomadic", voice: ELLEN, file: "nomadic.mp3" },
  { text: "Diverse", voice: ELLEN, file: "diverse.mp3" },
  { text: "Unforgettable", voice: ELLEN, file: "unforgettable.mp3" },
  { text: "Encounter", voice: ELLEN, file: "encounter.mp3" },
  { text: "Fascinating", voice: ELLEN, file: "fascinating.mp3" },
  { text: "Connection", voice: ELLEN, file: "connection.mp3" },
  { text: "Humble", voice: ELLEN, file: "humble.mp3" },

  // Vocabulary example sentences (alternate Arthur/Ellen)
  { text: "The cuisine in Thailand is spicy and diverse.", voice: ARTHUR, file: "the_cuisine_in_thailand_is_spicy_and_diverse.mp3" },
  { text: "Some people live a nomadic lifestyle, always moving.", voice: ELLEN, file: "some_people_live_a_nomadic_lifestyle.mp3" },
  { text: "Brazil is a very diverse country with many cultures.", voice: ARTHUR, file: "brazil_is_a_very_diverse_country.mp3" },
  { text: "Meeting that family was an unforgettable experience.", voice: ELLEN, file: "meeting_that_family_was_unforgettable.mp3" },
  { text: "I had a wonderful encounter with a local artist.", voice: ARTHUR, file: "i_had_a_wonderful_encounter.mp3" },
  { text: "The history of that city is absolutely fascinating.", voice: ELLEN, file: "the_history_of_that_city_is_fascinating.mp3" },
  { text: "I felt a deep connection with the people there.", voice: ARTHUR, file: "i_felt_a_deep_connection.mp3" },
  { text: "The family was humble but incredibly generous.", voice: ELLEN, file: "the_family_was_humble_but_generous.mp3" },

  // Fill-in-the-blank / grammar practice phrases (alternate Arthur/Ellen)
  { text: "Have you ever been to Spain?", voice: ARTHUR, file: "have_you_ever_been_to_spain.mp3" },
  { text: "I have never tried Japanese food.", voice: ELLEN, file: "i_have_never_tried_japanese_food.mp3" },
  { text: "She has visited more than 30 countries.", voice: ARTHUR, file: "she_has_visited_more_than_30_countries.mp3" },
  { text: "We have always wanted to go to Patagonia.", voice: ELLEN, file: "we_have_always_wanted_to_go_to_patagonia.mp3" },
  { text: "I have been to Morocco, but I have never been to Egypt.", voice: ARTHUR, file: "i_have_been_to_morocco_never_egypt.mp3" },
  { text: "Have you ever had an encounter that changed your life?", voice: ELLEN, file: "have_you_ever_had_an_encounter.mp3" },

  // Expressions
  { text: "It is been on my bucket list.", voice: ARTHUR, file: "its_been_on_my_bucket_list.mp3" },
  { text: "I have always wanted to visit Japan.", voice: ELLEN, file: "i_have_always_wanted_to_visit_japan.mp3" },
  { text: "That was a once-in-a-lifetime experience.", voice: ARTHUR, file: "that_was_a_once_in_a_lifetime_experience.mp3" },

  // Collocations
  { text: "Have an experience", voice: ELLEN, file: "have_an_experience.mp3" },
  { text: "Make a connection", voice: ARTHUR, file: "make_a_connection.mp3" },
  { text: "Try local cuisine", voice: ELLEN, file: "try_local_cuisine.mp3" },

  // Phrasal verb
  { text: "I ended up staying three more days.", voice: ARTHUR, file: "i_ended_up_staying_three_more_days.mp3" },

  // Dialogue — Carlos (male) = Arthur, Tuca (female) = Ellen
  { text: "This is a wonderful event. Have you been to one like this before?", voice: ARTHUR, file: "dialogue_l3_carlos_line1.mp3" },
  { text: "No, this is my first time. But I have always wanted to attend a cultural festival.", voice: ELLEN, file: "dialogue_l3_tuca_line2.mp3" },
  { text: "Where are you from? Have you traveled much?", voice: ARTHUR, file: "dialogue_l3_carlos_line3.mp3" },
  { text: "I am from Brazil. I have visited about 20 countries so far.", voice: ELLEN, file: "dialogue_l3_tuca_line4.mp3" },
  { text: "That is impressive! Have you ever been to Spain?", voice: ARTHUR, file: "dialogue_l3_carlos_line5.mp3" },
  { text: "No, I have never been to Spain, but it is on my bucket list!", voice: ELLEN, file: "dialogue_l3_tuca_line6.mp3" },
  { text: "You should visit! The cuisine is unforgettable. I have tried food from many countries, but Spanish food is special.", voice: ARTHUR, file: "dialogue_l3_carlos_line7.mp3" },
  { text: "I have always been fascinated by diverse cultures. That is why I travel.", voice: ELLEN, file: "dialogue_l3_tuca_line8.mp3" },
  { text: "Have you ever had an encounter that changed your perspective?", voice: ARTHUR, file: "dialogue_l3_carlos_line9.mp3" },
  { text: "Yes! I once ended up staying three extra days in Morocco because I made such a wonderful connection with a local family.", voice: ELLEN, file: "dialogue_l3_tuca_line10.mp3" },

  // Listening 1 — Sofia's travels (Ellen — female narrator)
  { text: "My name is Sofia. I have traveled to 30 countries in the last ten years. The most unforgettable experience I have ever had was in Peru. I have tried the local cuisine in every country I have visited. I have never been disappointed. The most fascinating encounter I have ever had was with a nomadic family in Mongolia. They were so humble and generous. I have always believed that travel creates connections that nothing else can.", voice: ELLEN, file: "listening_l3_sofia_travel.mp3" },

  // Listening 2 — Interview (Arthur — male interviewer + traveler)
  { text: "Interviewer: Have you ever been somewhere that completely surprised you? Traveler: Yes, I have. I visited Japan last year and it was nothing like I expected. Interviewer: What was so different? Traveler: The people were incredibly humble and the cuisine was diverse beyond anything I had imagined. I ended up staying two extra weeks. It has been the most unforgettable trip of my life so far.", voice: ARTHUR, file: "listening_l3_interview.mp3" },

  // Speech / Pronunciation cards (Tuca's practice lines → Ellen)
  { text: "I have visited about 20 countries so far.", voice: ELLEN, file: "i_have_visited_about_20_countries.mp3" },
  { text: "Have you ever tried local cuisine in Asia?", voice: ELLEN, file: "have_you_ever_tried_local_cuisine.mp3" },
  { text: "I have never been to a cultural festival before.", voice: ELLEN, file: "i_have_never_been_to_a_cultural_festival.mp3" },
  { text: "I have always wanted to attend a cultural festival.", voice: ELLEN, file: "i_have_always_wanted_to_attend.mp3" },
  { text: "I ended up making a wonderful connection with a local family.", voice: ELLEN, file: "i_ended_up_making_a_wonderful_connection.mp3" },
];

// Note: "[order-l1]" is a special key for ordering exercise audio — generated separately if needed
// The audioMap entry for it points to "order_l1_airport_conversation.mp3"
// This would be a composite audio; skipping programmatic generation as it requires manual composition

function toFilename(text) {
  return text.toLowerCase().replace(/[^a-z0-9 ]/g, '').replace(/ +/g, '_').substring(0, 60);
}

async function gen(text, voiceId, outPath) {
  const r = await fetch('https://api.elevenlabs.io/v1/text-to-speech/' + voiceId, {
    method: 'POST',
    headers: { 'xi-api-key': API_KEY, 'Content-Type': 'application/json' },
    body: JSON.stringify({ text, model_id: 'eleven_turbo_v2_5', voice_settings: { stability: 0.5, similarity_boost: 0.75 } }),
  });
  if (!r.ok) throw new Error(r.status + ': ' + (await r.text()));
  const buf = Buffer.from(await r.arrayBuffer());
  fs.writeFileSync(outPath, buf);
  return buf.length;
}

async function main() {
  if (!API_KEY) { console.error('ERROR: Set ELEVENLABS_API_KEY env var.\n  Usage: ELEVENLABS_API_KEY=sk-xxx node scripts/generate-audio-tuca-dias.js'); process.exit(1); }
  if (!fs.existsSync(DIR)) fs.mkdirSync(DIR, { recursive: true });

  // Deduplicate by file name (some phrases map to the same file)
  const seen = new Set();
  const unique = PHRASES.filter(p => {
    const key = p.file;
    if (seen.has(key)) return false;
    seen.add(key);
    return true;
  });

  const audioMap = {};
  let generated = 0;
  let skipped = 0;

  console.log('Generating ' + unique.length + ' audio files for Tuca Dias...\n');

  for (const p of unique) {
    const outPath = path.join(DIR, p.file);
    if (fs.existsSync(outPath)) {
      console.log('SKIP (exists): ' + p.file);
      skipped++;
    } else {
      try {
        const bytes = await gen(p.text, p.voice, outPath);
        const voiceName = p.voice === ELLEN ? 'ellen' : 'arthur';
        console.log('OK [' + voiceName + ']: ' + p.file + ' (' + (bytes / 1024).toFixed(1) + 'KB)');
        generated++;
        await new Promise(r => setTimeout(r, 500));
      } catch (e) {
        console.error('FAIL: ' + p.file + ' — ' + e.message);
      }
    }
    audioMap[p.text] = '/audio/tuca-dias/' + p.file;
  }

  fs.writeFileSync(path.join(DIR, 'audioMap.json'), JSON.stringify(audioMap, null, 2));
  console.log('\nDone! Generated: ' + generated + ', Skipped: ' + skipped + ', Total entries: ' + Object.keys(audioMap).length);
  console.log('Audio files saved to: ' + DIR);
  console.log('audioMap.json saved to: ' + path.join(DIR, 'audioMap.json'));
}

main().catch(e => { console.error(e); process.exit(1); });
