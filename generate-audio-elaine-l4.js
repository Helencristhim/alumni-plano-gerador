const fs = require('fs');
const path = require('path');
const https = require('https');

const API_KEY = process.env.ELEVENLABS_API_KEY;
if (!API_KEY) { console.error('ERROR: ELEVENLABS_API_KEY not set'); process.exit(1); }

const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';

const BASE_DIR = '/Users/helenmendes/alumni-plano-gerador/public';

// Full audioMap from elaine-mieko-pinho.html
const audioMap = {
  "Could you repeat that, please?": "/audio/elaine-mieko-pinho/could_you_repeat_that_please.mp3",
  "I am not sure I understand. Could you explain?": "/audio/elaine-mieko-pinho/i_am_not_sure_i_understand_could_you_explain.mp3",
  "Could you speak more slowly, please?": "/audio/elaine-mieko-pinho/could_you_speak_more_slowly_please.mp3",
  "I am not sure how to say this in English.": "/audio/elaine-mieko-pinho/i_am_not_sure_how_to_say_this_in_english.mp3",
  "Thank you for your patience.": "/audio/elaine-mieko-pinho/thank_you_for_your_patience.mp3",
  "Trip": "/audio/elaine-mieko-pinho/trip.mp3",
  "Abroad": "/audio/elaine-mieko-pinho/abroad.mp3",
  "Alone": "/audio/elaine-mieko-pinho/alone.mp3",
  "Confident": "/audio/elaine-mieko-pinho/confident.mp3",
  "Nervous": "/audio/elaine-mieko-pinho/nervous.mp3",
  "Manage": "/audio/elaine-mieko-pinho/manage.mp3",
  "Check in": "/audio/elaine-mieko-pinho/check_in.mp3",
  "Deal with": "/audio/elaine-mieko-pinho/deal_with.mp3",
  "I usually travel with my family.": "/audio/elaine-mieko-pinho/i_usually_travel_with_my_family.mp3",
  "I want to feel more confident when I travel abroad.": "/audio/elaine-mieko-pinho/i_want_to_feel_more_confident_when_i_travel_abroad.mp3",
  "I am not sure how to say what I need at the airport.": "/audio/elaine-mieko-pinho/i_am_not_sure_how_to_say_what_i_need_at_the_airport.mp3",
  "I live in a small city in Sao Paulo state.": "/audio/elaine-mieko-pinho/i_live_in_a_small_city_in_sao_paulo_state.mp3",
  "My name is Elaine. I am from Brazil.": "/audio/elaine-mieko-pinho/my_name_is_elaine_i_am_from_brazil.mp3",
  "I am a lawyer and I manage a company.": "/audio/elaine-mieko-pinho/i_am_a_lawyer_and_i_manage_a_company.mp3",
  "I love to travel, but I feel nervous when I need to speak English.": "/audio/elaine-mieko-pinho/i_love_to_travel_but_i_feel_nervous_when_i_need_to_speak_eng.mp3",
  "I want to travel alone and feel confident.": "/audio/elaine-mieko-pinho/i_want_to_travel_alone_and_feel_confident.mp3",
  "I work as a lawyer in Indaiatuba.": "/audio/elaine-mieko-pinho/i_work_as_a_lawyer_in_indaiatuba.mp3",
  "I manage a company with my family.": "/audio/elaine-mieko-pinho/i_manage_a_company_with_my_family.mp3",
  "I usually travel to Europe and the United States.": "/audio/elaine-mieko-pinho/i_usually_travel_to_europe_and_the_united_states.mp3",
  "I want to check in at a hotel by myself.": "/audio/elaine-mieko-pinho/i_want_to_check_in_at_a_hotel_by_myself.mp3",
  "I need to learn how to deal with problems when I travel.": "/audio/elaine-mieko-pinho/i_need_to_learn_how_to_deal_with_problems_when_i_travel.mp3",
  "Good morning. My name is Elaine Mieko Pinho. I am from Indaiatuba, a small city in Sao Paulo, Brazil. I am a lawyer and I also manage a family company. I usually travel with my family, but I want to travel alone too. I feel nervous when I need to speak English abroad, but I am not going to give up. I want to feel confident.": "/audio/elaine-mieko-pinho/good_morning_my_name_is_elaine_mieko_pinho_i_am_from_indaiatuba.mp3",
  "Good morning. My name is Elaine.": "/audio/elaine-mieko-pinho/good_morning_my_name_is_elaine.mp3",
  "I am from Indaiatuba, in Sao Paulo.": "/audio/elaine-mieko-pinho/i_am_from_indaiatuba_in_sao_paulo.mp3",
  "I am a lawyer and I manage a company.": "/audio/elaine-mieko-pinho/i_am_a_lawyer_and_i_manage_a_company_v2.mp3",
  "I love traveling, but I feel nervous speaking English.": "/audio/elaine-mieko-pinho/i_love_traveling_but_i_feel_nervous_speaking_english.mp3",
  "I want to travel alone and feel confident abroad.": "/audio/elaine-mieko-pinho/i_want_to_travel_alone_and_feel_confident_abroad.mp3",
  "Hi! I am Sarah. I work at the front desk. Are you checking in today?": "/audio/elaine-mieko-pinho/hi_i_am_sarah_i_work_at_the_front_desk_are_you_checking_in_t.mp3",
  "Yes, I have a reservation. My name is Elaine Pinho.": "/audio/elaine-mieko-pinho/yes_i_have_a_reservation_my_name_is_elaine_pinho.mp3",
  "Welcome, Ms. Pinho! Where are you from?": "/audio/elaine-mieko-pinho/welcome_ms_pinho_where_are_you_from.mp3",
  "I am from Brazil. I live in a small city called Indaiatuba.": "/audio/elaine-mieko-pinho/i_am_from_brazil_i_live_in_a_small_city_called_indaiatuba.mp3",
  "How nice! Is this your first trip to New York?": "/audio/elaine-mieko-pinho/how_nice_is_this_your_first_trip_to_new_york.mp3",
  "No, I usually travel with my family. But this time I am alone.": "/audio/elaine-mieko-pinho/no_i_usually_travel_with_my_family_but_this_time_i_am_alone.mp3",
  "That is brave! Do you need help with anything?": "/audio/elaine-mieko-pinho/that_is_brave_do_you_need_help_with_anything.mp3",
  "I am not sure how to say this, but could I get a room with a view?": "/audio/elaine-mieko-pinho/i_am_not_sure_how_to_say_this_but_could_i_get_a_room_with_a.mp3",
  "Attention, please. Flight AA 402 to New York is now boarding at Gate 12. All passengers, please have your boarding pass and passport ready.": "/audio/elaine-mieko-pinho/attention_please_flight_aa_402_to_new_york_is_now_boarding_at.mp3",
  "Could I have a window seat, please?": "/audio/elaine-mieko-pinho/could_i_have_a_window_seat_please.mp3",
  "I would like to check in, please.": "/audio/elaine-mieko-pinho/i_would_like_to_check_in_please.mp3",
  "Could you help me find my gate?": "/audio/elaine-mieko-pinho/could_you_help_me_find_my_gate.mp3",
  "I am not sure how to say this in English.": "/audio/elaine-mieko-pinho/i_am_not_sure_how_to_say_this_in_english_v2.mp3",
  "I need to deal with a problem with my reservation.": "/audio/elaine-mieko-pinho/i_need_to_deal_with_a_problem_with_my_reservation.mp3",
  "I feel nervous, but I am not going to give up.": "/audio/elaine-mieko-pinho/i_feel_nervous_but_i_am_not_going_to_give_up.mp3",
  "My name is Elaine. I am from Brazil.": "/audio/elaine-mieko-pinho/my_name_is_elaine_i_am_from_brazil_v2.mp3",
  "I work as a lawyer and I manage a company.": "/audio/elaine-mieko-pinho/i_work_as_a_lawyer_and_i_manage_a_company.mp3",
  "I usually travel with my family, but I want to be independent.": "/audio/elaine-mieko-pinho/i_usually_travel_with_my_family_but_i_want_to_be_independent.mp3",
  "I feel nervous abroad, but I am learning.": "/audio/elaine-mieko-pinho/i_feel_nervous_abroad_but_i_am_learning.mp3",
  "I want to check in at hotels and deal with problems by myself.": "/audio/elaine-mieko-pinho/i_want_to_check_in_at_hotels_and_deal_with_problems_by_mysel.mp3",
  "Boarding pass": "/audio/elaine-mieko-pinho/boarding_pass.mp3",
  "Gate": "/audio/elaine-mieko-pinho/gate.mp3",
  "Luggage": "/audio/elaine-mieko-pinho/luggage.mp3",
  "Passport": "/audio/elaine-mieko-pinho/passport.mp3",
  "Departure": "/audio/elaine-mieko-pinho/departure.mp3",
  "Arrival": "/audio/elaine-mieko-pinho/arrival.mp3",
  "Seat": "/audio/elaine-mieko-pinho/seat.mp3",
  "Delay": "/audio/elaine-mieko-pinho/delay.mp3",
  "Could I see your boarding pass, please?": "/audio/elaine-mieko-pinho/could_i_see_your_boarding_pass_please.mp3",
  "The flight departs from Gate 14.": "/audio/elaine-mieko-pinho/the_flight_departs_from_gate_14.mp3",
  "Could I check in two pieces of luggage?": "/audio/elaine-mieko-pinho/could_i_check_in_two_pieces_of_luggage.mp3",
  "Please have your passport ready.": "/audio/elaine-mieko-pinho/please_have_your_passport_ready.mp3",
  "The departure time is 10:30 AM.": "/audio/elaine-mieko-pinho/the_departure_time_is_10_30_am.mp3",
  "What is the arrival time in New York?": "/audio/elaine-mieko-pinho/what_is_the_arrival_time_in_new_york.mp3",
  "Could I have a window seat, please?": "/audio/elaine-mieko-pinho/could_i_have_a_window_seat_please_v2.mp3",
  "There is a two-hour delay on our flight.": "/audio/elaine-mieko-pinho/there_is_a_two_hour_delay_on_our_flight.mp3",
  "Elaine arrives at Guarulhos Airport in Sao Paulo. She walks to the check-in counter with her luggage. The attendant asks for her passport and boarding pass. Elaine feels a little nervous, but she remembers her English.": "/audio/elaine-mieko-pinho/elaine_arrives_at_guarulhos_airport_paragraph1.mp3",
  "Could I have a window seat, please? she asks. The attendant smiles and says, Of course! Your departure is at Gate 14. The flight departs at 10:30 AM.": "/audio/elaine-mieko-pinho/elaine_arrives_at_guarulhos_airport_paragraph2.mp3",
  "Could I have an aisle seat, please?": "/audio/elaine-mieko-pinho/could_i_have_an_aisle_seat_please.mp3",
  "Where is the gate for Flight 402?": "/audio/elaine-mieko-pinho/where_is_the_gate_for_flight_402.mp3",
  "Please have your passport and boarding pass ready.": "/audio/elaine-mieko-pinho/please_have_your_passport_and_boarding_pass_ready.mp3",
  "There is a one-hour delay on our flight.": "/audio/elaine-mieko-pinho/there_is_a_one_hour_delay_on_our_flight.mp3",
  "The departure time is 3:15 PM.": "/audio/elaine-mieko-pinho/the_departure_time_is_3_15_pm.mp3",
  "Could I check in three pieces of luggage?": "/audio/elaine-mieko-pinho/could_i_check_in_three_pieces_of_luggage.mp3",
  "You arrive at the airport with your luggage.": "/audio/elaine-mieko-pinho/you_arrive_at_the_airport_with_your_luggage.mp3",
  "You go to the check-in counter and show your passport.": "/audio/elaine-mieko-pinho/you_go_to_the_check_in_counter_and_show_your_passport.mp3",
  "You receive your boarding pass and check in your luggage.": "/audio/elaine-mieko-pinho/you_receive_your_boarding_pass_and_check_in_your_luggage.mp3",
  "You go through security and find your gate.": "/audio/elaine-mieko-pinho/you_go_through_security_and_find_your_gate.mp3",
  "You hear the boarding announcement and get on the plane.": "/audio/elaine-mieko-pinho/you_hear_the_boarding_announcement_and_get_on_the_plane.mp3",
  "Where is Gate 14?": "/audio/elaine-mieko-pinho/where_is_gate_14.mp3",
  "There is a two-hour delay on our flight.": "/audio/elaine-mieko-pinho/there_is_a_two_hour_delay_on_our_flight_v2.mp3",
  "Please have your passport and boarding pass ready.": "/audio/elaine-mieko-pinho/please_have_your_passport_and_boarding_pass_ready_v2.mp3",
  "Is there a delay on this flight?": "/audio/elaine-mieko-pinho/is_there_a_delay_on_this_flight.mp3",
  "Could I check in my luggage here?": "/audio/elaine-mieko-pinho/could_i_check_in_my_luggage_here.mp3",
  "What time does the flight depart?": "/audio/elaine-mieko-pinho/what_time_does_the_flight_depart.mp3",
  "Good morning. I would like to check in for my flight to New York.": "/audio/elaine-mieko-pinho/good_morning_i_would_like_to_check_in_for_my_flight.mp3",
  "Of course! May I see your passport and booking confirmation?": "/audio/elaine-mieko-pinho/of_course_may_i_see_your_passport_and_booking.mp3",
  "Here you go. My name is Elaine Pinho.": "/audio/elaine-mieko-pinho/here_you_go_my_name_is_elaine_pinho.mp3",
  "Thank you, Ms. Pinho. Would you like a window or aisle seat?": "/audio/elaine-mieko-pinho/thank_you_ms_pinho_would_you_like_a_window_or_aisle.mp3",
  "Could I have a window seat, please? I love to see the view.": "/audio/elaine-mieko-pinho/could_i_have_a_window_seat_i_love_the_view.mp3",
  "Of course! Do you have any luggage to check in?": "/audio/elaine-mieko-pinho/of_course_do_you_have_any_luggage_to_check_in.mp3",
  "Yes, I have two pieces of luggage.": "/audio/elaine-mieko-pinho/yes_i_have_two_pieces_of_luggage.mp3",
  "Here is your boarding pass. Your departure is at Gate 14 at 10:30 AM.": "/audio/elaine-mieko-pinho/here_is_your_boarding_pass_gate_14_10_30.mp3",
  "Attention, please. Flight AA 402 to New York JFK has a two-hour delay. New departure time is 12:30 PM. We apologize for the inconvenience. Please remain near Gate 14.": "/audio/elaine-mieko-pinho/attention_flight_aa_402_delay_announcement.mp3",
  "Where are the restrooms?": "/audio/elaine-mieko-pinho/where_are_the_restrooms.mp3",
  "Excuse me, where is Gate 14?": "/audio/elaine-mieko-pinho/excuse_me_where_is_gate_14.mp3",
  "Could I change my seat, please?": "/audio/elaine-mieko-pinho/could_i_change_my_seat_please.mp3",
  "Is this the right gate for the flight to New York?": "/audio/elaine-mieko-pinho/is_this_the_right_gate_for_new_york.mp3",
  "How long is the delay?": "/audio/elaine-mieko-pinho/how_long_is_the_delay.mp3",
  "Could I get something to eat near the gate?": "/audio/elaine-mieko-pinho/could_i_get_something_to_eat_near_the_gate.mp3",
  "Flight attendant": "/audio/elaine-mieko-pinho/flight_attendant.mp3",
  "Blanket": "/audio/elaine-mieko-pinho/blanket.mp3",
  "Pillow": "/audio/elaine-mieko-pinho/pillow.mp3",
  "Tray table": "/audio/elaine-mieko-pinho/tray_table.mp3",
  "Fasten": "/audio/elaine-mieko-pinho/fasten.mp3",
  "Seatbelt": "/audio/elaine-mieko-pinho/seatbelt.mp3",
  "Aisle": "/audio/elaine-mieko-pinho/aisle.mp3",
  "Overhead bin": "/audio/elaine-mieko-pinho/overhead_bin.mp3",
  "Could I have a blanket, please?": "/audio/elaine-mieko-pinho/could_i_have_a_blanket_please.mp3",
  "The flight attendant helped me with my bag.": "/audio/elaine-mieko-pinho/the_flight_attendant_helped_me_with_my_bag.mp3",
  "I need a pillow to rest my head.": "/audio/elaine-mieko-pinho/i_need_a_pillow_to_rest_my_head.mp3",
  "Please open your tray table for the meal.": "/audio/elaine-mieko-pinho/please_open_your_tray_table_for_the_meal.mp3",
  "Please fasten your seatbelt for takeoff.": "/audio/elaine-mieko-pinho/please_fasten_your_seatbelt_for_takeoff.mp3",
  "The seatbelt sign is on. Please remain seated.": "/audio/elaine-mieko-pinho/the_seatbelt_sign_is_on_please_remain_seated.mp3",
  "Excuse me, could I get through to the aisle?": "/audio/elaine-mieko-pinho/excuse_me_could_i_get_through_to_the_aisle.mp3",
  "Please put your bag in the overhead bin.": "/audio/elaine-mieko-pinho/please_put_your_bag_in_the_overhead_bin.mp3",
  "Could I have a blanket and a pillow, please?": "/audio/elaine-mieko-pinho/could_i_have_a_blanket_and_a_pillow_please.mp3",
  "I would like some water, please.": "/audio/elaine-mieko-pinho/i_would_like_some_water_please.mp3",
  "Where is the overhead bin for my bag?": "/audio/elaine-mieko-pinho/where_is_the_overhead_bin_for_my_bag.mp3",
  "Could you help me fasten my seatbelt?": "/audio/elaine-mieko-pinho/could_you_help_me_fasten_my_seatbelt.mp3",
  "I would like some orange juice, please.": "/audio/elaine-mieko-pinho/i_would_like_some_orange_juice_please.mp3",
  "Could I have some water, please?": "/audio/elaine-mieko-pinho/could_i_have_some_water_please.mp3",
  "I would like a coffee, please.": "/audio/elaine-mieko-pinho/i_would_like_a_coffee_please.mp3",
  "Excuse me, could you help me with the overhead bin?": "/audio/elaine-mieko-pinho/excuse_me_could_you_help_me_with_the_overhead_bin.mp3",
  "I would like some tea, please.": "/audio/elaine-mieko-pinho/i_would_like_some_tea_please.mp3",
  "Elaine is on her flight to New York. She finds her window seat and puts her bag in the overhead bin. A flight attendant walks by.": "/audio/elaine-mieko-pinho/elaine_on_flight_paragraph1.mp3",
  "Could I have a blanket and a pillow, please? Elaine asks. Of course! he says. My name is Mark. Let me know if you need anything.": "/audio/elaine-mieko-pinho/elaine_on_flight_paragraph2.mp3",
  "Good afternoon, everyone. This is your captain speaking. Please fasten your seatbelts. We are preparing for takeoff. The flight to New York JFK will take approximately nine hours. We hope you have a pleasant flight.": "/audio/elaine-mieko-pinho/captain_announcement_takeoff.mp3",
  "Hello! Welcome aboard. I am Mark. Can I help you find your seat?": "/audio/elaine-mieko-pinho/hello_welcome_aboard_i_am_mark.mp3",
  "Yes, please. I have seat 14A. It is a window seat.": "/audio/elaine-mieko-pinho/yes_please_i_have_seat_14a.mp3",
  "Right this way. Could I help you with your bag?": "/audio/elaine-mieko-pinho/right_this_way_could_i_help_with_bag.mp3",
  "Yes, could you put it in the overhead bin, please?": "/audio/elaine-mieko-pinho/yes_could_you_put_it_in_overhead_bin.mp3",
  "Of course! Is there anything else you need?": "/audio/elaine-mieko-pinho/of_course_is_there_anything_else.mp3",
  "Could I have a blanket and a pillow, please? It is a long flight.": "/audio/elaine-mieko-pinho/could_i_have_blanket_pillow_long_flight.mp3",
  "Here you go! Would you like something to drink?": "/audio/elaine-mieko-pinho/here_you_go_would_you_like_something_to_drink.mp3",
  "I would like some orange juice, please. Thank you, Mark!": "/audio/elaine-mieko-pinho/i_would_like_orange_juice_thank_you_mark.mp3",
  "I would like a chicken sandwich, please.": "/audio/elaine-mieko-pinho/i_would_like_a_chicken_sandwich_please.mp3",
  "Could I have an extra blanket, please?": "/audio/elaine-mieko-pinho/could_i_have_an_extra_blanket_please.mp3",
  "I would like some coffee with milk, please.": "/audio/elaine-mieko-pinho/i_would_like_some_coffee_with_milk_please.mp3",
  "Where are the restrooms on this plane?": "/audio/elaine-mieko-pinho/where_are_the_restrooms_on_this_plane.mp3",
  "Could I have a glass of water, please?": "/audio/elaine-mieko-pinho/could_i_have_a_glass_of_water_please.mp3",
  "I would like the pasta, please.": "/audio/elaine-mieko-pinho/i_would_like_the_pasta_please.mp3",
  "Could I get through to the aisle, please?": "/audio/elaine-mieko-pinho/could_i_get_through_to_the_aisle_please.mp3",
  "I would like to recline my seat, please.": "/audio/elaine-mieko-pinho/i_would_like_to_recline_my_seat_please.mp3",
  "Could I have some headphones, please?": "/audio/elaine-mieko-pinho/could_i_have_some_headphones_please.mp3",
  "I would like a blanket, please.": "/audio/elaine-mieko-pinho/i_would_like_a_blanket_please.mp3",
  "listening3_checkin_full": "/audio/elaine-mieko-pinho/listening3_checkin_counter_full.mp3",
  "listening5_plane_full": "/audio/elaine-mieko-pinho/listening5_on_the_plane_full.mp3",
  "Immigration": "/audio/elaine-mieko-pinho/immigration.mp3",
  "Customs": "/audio/elaine-mieko-pinho/customs.mp3",
  "Declaration": "/audio/elaine-mieko-pinho/declaration.mp3",
  "Purpose": "/audio/elaine-mieko-pinho/purpose.mp3",
  "Vacation": "/audio/elaine-mieko-pinho/vacation.mp3",
  "Return": "/audio/elaine-mieko-pinho/return.mp3",
  "Declare": "/audio/elaine-mieko-pinho/declare.mp3",
  "Officer": "/audio/elaine-mieko-pinho/officer.mp3",
  "The immigration officer checked my passport.": "/audio/elaine-mieko-pinho/the_immigration_officer_checked_my_passport.mp3",
  "You need to go through customs after immigration.": "/audio/elaine-mieko-pinho/you_need_to_go_through_customs_after_immigration.mp3",
  "I filled out the declaration form on the plane.": "/audio/elaine-mieko-pinho/i_filled_out_the_declaration_form_on_the_plane.mp3",
  "What is the purpose of your visit?": "/audio/elaine-mieko-pinho/what_is_the_purpose_of_your_visit.mp3",
  "I am here on vacation for two weeks.": "/audio/elaine-mieko-pinho/i_am_here_on_vacation_for_two_weeks.mp3",
  "When is your return flight?": "/audio/elaine-mieko-pinho/when_is_your_return_flight.mp3",
  "I have nothing to declare.": "/audio/elaine-mieko-pinho/i_have_nothing_to_declare.mp3",
  "The officer asked me about my luggage.": "/audio/elaine-mieko-pinho/the_officer_asked_me_about_my_luggage.mp3",
  "I am here on vacation.": "/audio/elaine-mieko-pinho/i_am_here_on_vacation.mp3",
  "I am staying for two weeks.": "/audio/elaine-mieko-pinho/i_am_staying_for_two_weeks.mp3",
  "I am staying at a hotel in Manhattan.": "/audio/elaine-mieko-pinho/i_am_staying_at_a_hotel_in_manhattan.mp3",
  "I do not have any prohibited items.": "/audio/elaine-mieko-pinho/i_do_not_have_any_prohibited_items.mp3",
  "I am here to visit my friend.": "/audio/elaine-mieko-pinho/i_am_here_to_visit_my_friend.mp3",
  "I am staying for ten days.": "/audio/elaine-mieko-pinho/i_am_staying_for_ten_days.mp3",
  "I am here for tourism.": "/audio/elaine-mieko-pinho/i_am_here_for_tourism.mp3",
  "My return flight is on March 15th.": "/audio/elaine-mieko-pinho/my_return_flight_is_on_march_15th.mp3",
  "Next, please. May I see your passport?": "/audio/elaine-mieko-pinho/next_please_may_i_see_your_passport.mp3",
  "Here you go.": "/audio/elaine-mieko-pinho/here_you_go.mp3",
  "What is the purpose of your visit to the United States?": "/audio/elaine-mieko-pinho/what_is_the_purpose_of_your_visit_to_the_us.mp3",
  "How long are you staying?": "/audio/elaine-mieko-pinho/how_long_are_you_staying.mp3",
  "Where are you staying?": "/audio/elaine-mieko-pinho/where_are_you_staying.mp3",
  "The officer stamps her passport. Welcome to the United States. Enjoy your stay.": "/audio/elaine-mieko-pinho/officer_stamps_passport_welcome.mp3",
  "Thank you!": "/audio/elaine-mieko-pinho/thank_you.mp3",
  "Welcome to the United States. All arriving passengers must proceed to immigration. Please have your passport and completed declaration form ready. If you have nothing to declare, please use the green lane. If you have items to declare, please use the red lane. Thank you.": "/audio/elaine-mieko-pinho/customs_announcement_jfk.mp3",
  "I am here on vacation. I am staying for two weeks.": "/audio/elaine-mieko-pinho/i_am_here_on_vacation_staying_two_weeks.mp3",
  "I have nothing to declare. I do not have any prohibited items.": "/audio/elaine-mieko-pinho/i_have_nothing_to_declare_no_prohibited.mp3",
  "I am staying at a hotel in Manhattan. My return flight is on March 15th.": "/audio/elaine-mieko-pinho/staying_hotel_manhattan_return_march.mp3",
  "What is the purpose of your visit? I am here on vacation.": "/audio/elaine-mieko-pinho/purpose_visit_vacation.mp3",
  "You arrive at immigration. The officer asks for your passport.": "/audio/elaine-mieko-pinho/you_arrive_at_immigration_officer_asks.mp3",
  "You answer the officer's questions about your visit.": "/audio/elaine-mieko-pinho/you_answer_officers_questions.mp3",
  "You go through customs and pick up your luggage.": "/audio/elaine-mieko-pinho/you_go_through_customs_pick_up_luggage.mp3",
  "You read your declaration form and walk through the green lane.": "/audio/elaine-mieko-pinho/you_read_declaration_form_green_lane.mp3",
  "You exit the airport with your luggage.": "/audio/elaine-mieko-pinho/you_exit_the_airport_with_your_luggage.mp3",
  "I am here on vacation for two weeks.": "/audio/elaine-mieko-pinho/i_am_here_on_vacation_for_two_weeks_v2.mp3",
  "I do not have anything to declare.": "/audio/elaine-mieko-pinho/i_do_not_have_anything_to_declare.mp3",
  "Where is the customs area?": "/audio/elaine-mieko-pinho/where_is_the_customs_area.mp3",
  "I am staying at a hotel near Times Square.": "/audio/elaine-mieko-pinho/i_am_staying_at_a_hotel_near_times_square.mp3",
  "My return flight is next Sunday.": "/audio/elaine-mieko-pinho/my_return_flight_is_next_sunday.mp3",
  "Could you repeat that, please? I did not understand.": "/audio/elaine-mieko-pinho/could_you_repeat_that_i_did_not_understand.mp3",
  "listening7_immigration_full": "/audio/elaine-mieko-pinho/listening7_immigration_dialogue_full.mp3",
  "listening8_customs_full": "/audio/elaine-mieko-pinho/listening8_customs_announcement_full.mp3"
};

// Lines that are Officer James = Arthur, Elaine lines = Ellen
// Officer James lines (immigration officer - male)
const officerJamesLines = [
  "Next, please. May I see your passport?",
  "What is the purpose of your visit to the United States?",
  "How long are you staying?",
  "Where are you staying?",
  "The officer stamps her passport. Welcome to the United States. Enjoy your stay."
];

// Elaine lines (female)
const elaineLines = [
  "Here you go.",
  "I am here on vacation. I am staying for two weeks.",
  "I have nothing to declare. I do not have any prohibited items.",
  "I am staying at a hotel in Manhattan. My return flight is on March 15th.",
  "Thank you!"
];

function countWords(text) {
  return text.trim().split(/\s+/).length;
}

let alternateCounter = 0;

function pickVoice(text) {
  // Check Officer James lines
  if (officerJamesLines.includes(text)) return ARTHUR;
  // Check Elaine lines
  if (elaineLines.includes(text)) return ELLEN;

  // Internal keys (listening identifiers) - use Arthur
  if (text.startsWith('listening')) return ARTHUR;

  const words = countWords(text);
  // 1-2 words = always Arthur
  if (words <= 2) return ARTHUR;

  // 3+ words = alternate Arthur/Ellen
  alternateCounter++;
  return (alternateCounter % 2 === 0) ? ARTHUR : ELLEN;
}

function generateAudio(text, voiceId, outputPath) {
  return new Promise((resolve, reject) => {
    const dir = path.dirname(outputPath);
    if (!fs.existsSync(dir)) fs.mkdirSync(dir, { recursive: true });

    const postData = JSON.stringify({
      text: text,
      model_id: 'eleven_monolingual_v1',
      voice_settings: { stability: 0.5, similarity_boost: 0.75 }
    });

    const options = {
      hostname: 'api.elevenlabs.io',
      port: 443,
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
        let body = '';
        res.on('data', d => body += d);
        res.on('end', () => reject(new Error(`HTTP ${res.statusCode}: ${body}`)));
        return;
      }
      const chunks = [];
      res.on('data', chunk => chunks.push(chunk));
      res.on('end', () => {
        const buffer = Buffer.concat(chunks);
        fs.writeFileSync(outputPath, buffer);
        resolve(buffer.length);
      });
    });

    req.on('error', reject);
    req.write(postData);
    req.end();
  });
}

function delay(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function main() {
  const entries = Object.entries(audioMap);
  let generated = 0;
  let skipped = 0;
  let errors = 0;

  console.log(`Total audioMap entries: ${entries.length}`);
  console.log('---');

  for (const [text, filePath] of entries) {
    const fullPath = path.join(BASE_DIR, filePath);

    // Skip if file exists and > 1KB
    if (fs.existsSync(fullPath)) {
      const stats = fs.statSync(fullPath);
      if (stats.size > 1024) {
        skipped++;
        continue;
      }
    }

    const voice = pickVoice(text);
    const voiceName = voice === ARTHUR ? 'Arthur' : 'Ellen';
    const shortText = text.length > 60 ? text.substring(0, 57) + '...' : text;

    console.log(`[${generated + 1}] Generating (${voiceName}): "${shortText}"`);
    console.log(`    -> ${filePath}`);

    try {
      const size = await generateAudio(text, voice, fullPath);
      console.log(`    OK (${(size / 1024).toFixed(1)} KB)`);
      generated++;
      await delay(500);
    } catch (err) {
      console.error(`    ERROR: ${err.message}`);
      errors++;
      await delay(1000);
    }
  }

  console.log('\n========== SUMMARY ==========');
  console.log(`Generated: ${generated}`);
  console.log(`Skipped (already exist): ${skipped}`);
  console.log(`Errors: ${errors}`);
  console.log(`Total entries: ${entries.length}`);
}

main().catch(err => { console.error('Fatal error:', err); process.exit(1); });
