const fs = require('fs');
const path = require('path');
const API_KEY = process.env.ELEVENLABS_API_KEY;

const VOICES = {
  arthur: 'sfJopaWaOtauCD3HKX6Q',
  ellen: 'BIvP0GN1cAtSRTxNHnWS',
  josh: 'TxGEqnHWrfWFTfGW9XjX',
  rachel: '21m00Tcm4TlvDq8ikWAM',
};

const PHRASES = [
  // ============================================================
  // RAFAEL PELIZARO — AULA 4 (43 files, male student = arthur)
  // ============================================================
  // Vocab words (arthur)
  { text: "Negotiate", voice: "arthur", file: "rafael-pelizaro/l4_negotiate.mp3" },
  { text: "Proposal", voice: "arthur", file: "rafael-pelizaro/l4_proposal.mp3" },
  { text: "Terms", voice: "arthur", file: "rafael-pelizaro/l4_terms.mp3" },
  { text: "Discount", voice: "arthur", file: "rafael-pelizaro/l4_discount.mp3" },
  { text: "Contract", voice: "arthur", file: "rafael-pelizaro/l4_contract.mp3" },
  { text: "Clause", voice: "arthur", file: "rafael-pelizaro/l4_clause.mp3" },
  { text: "Counteroffer", voice: "arthur", file: "rafael-pelizaro/l4_counteroffer.mp3" },
  { text: "SLA", voice: "arthur", file: "rafael-pelizaro/l4_sla.mp3" },
  // Vocab sentences (alternate)
  { text: "We need to negotiate better terms with the cloud provider.", voice: "arthur", file: "rafael-pelizaro/l4_we_need_to_negotiate_better.mp3" },
  { text: "The vendor sent a proposal for the new infrastructure project.", voice: "ellen", file: "rafael-pelizaro/l4_the_vendor_sent_a_proposal.mp3" },
  { text: "The terms of the agreement include a 99.9 percent uptime guarantee.", voice: "arthur", file: "rafael-pelizaro/l4_the_terms_of_the_agreement.mp3" },
  { text: "They offered a 15 percent discount for a two-year commitment.", voice: "ellen", file: "rafael-pelizaro/l4_they_offered_a_15_percent.mp3" },
  { text: "We signed a three-year contract with the data center provider.", voice: "arthur", file: "rafael-pelizaro/l4_we_signed_a_three_year.mp3" },
  { text: "There is a penalty clause if they miss the delivery deadline.", voice: "ellen", file: "rafael-pelizaro/l4_there_is_a_penalty_clause.mp3" },
  { text: "Our team prepared a counteroffer with adjusted pricing.", voice: "arthur", file: "rafael-pelizaro/l4_our_team_prepared_a_counteroffer.mp3" },
  { text: "The SLA defines response times for critical support tickets.", voice: "ellen", file: "rafael-pelizaro/l4_the_sla_defines_response.mp3" },
  // Grammar sentences
  { text: "Can you send us the updated proposal by Friday?", voice: "arthur", file: "rafael-pelizaro/l4_can_you_send_us_the_updated.mp3" },
  { text: "Could you offer a better discount for a longer commitment?", voice: "ellen", file: "rafael-pelizaro/l4_could_you_offer_a_better.mp3" },
  { text: "We can offer a 10 percent discount if you sign today.", voice: "arthur", file: "rafael-pelizaro/l4_we_can_offer_a_10_percent.mp3" },
  { text: "We could consider extending the SLA if you increase the volume.", voice: "ellen", file: "rafael-pelizaro/l4_we_could_consider_extending.mp3" },
  // Fill-in
  { text: "Can you include a penalty clause in the contract?", voice: "arthur", file: "rafael-pelizaro/l4_fill_can_you_include.mp3" },
  { text: "Could you reduce the implementation timeline?", voice: "ellen", file: "rafael-pelizaro/l4_fill_could_you_reduce.mp3" },
  { text: "We can offer free onboarding if you sign a two-year contract.", voice: "arthur", file: "rafael-pelizaro/l4_fill_we_can_offer_free.mp3" },
  { text: "If you increase the volume, we could lower the unit price.", voice: "ellen", file: "rafael-pelizaro/l4_fill_if_you_increase.mp3" },
  { text: "Could you share the detailed SLA before we finalize?", voice: "arthur", file: "rafael-pelizaro/l4_fill_could_you_share.mp3" },
  // Dialogue (Rafael=arthur, David Chen=josh)
  { text: "Good morning, David. Thank you for meeting with us. I have reviewed your proposal for the cloud infrastructure project.", voice: "arthur", file: "rafael-pelizaro/l4_dialogue_rafael_1.mp3" },
  { text: "Good morning, Rafael. I am glad to hear that. What did you think of the terms?", voice: "josh", file: "rafael-pelizaro/l4_dialogue_david_2.mp3" },
  { text: "The overall scope looks good, but I have some questions about the pricing. Could you offer a discount for a two-year commitment instead of one year?", voice: "arthur", file: "rafael-pelizaro/l4_dialogue_rafael_3.mp3" },
  { text: "We could consider a 10 percent discount for a two-year contract. Would that work for your budget?", voice: "josh", file: "rafael-pelizaro/l4_dialogue_david_4.mp3" },
  { text: "That is a good start. Can you also include a penalty clause if the uptime drops below 99.9 percent?", voice: "arthur", file: "rafael-pelizaro/l4_dialogue_rafael_5.mp3" },
  { text: "We can add that to the SLA. Our standard penalty is a 5 percent credit per incident. Could you share your expected monthly volume so we can finalize the pricing?", voice: "josh", file: "rafael-pelizaro/l4_dialogue_david_6.mp3" },
  { text: "Of course. We expect around 500 terabytes per month. If we increase volume next year, could you lower the unit price?", voice: "arthur", file: "rafael-pelizaro/l4_dialogue_rafael_7.mp3" },
  { text: "Absolutely. We can include a volume-based pricing clause in the contract. I will send the updated proposal by Friday.", voice: "josh", file: "rafael-pelizaro/l4_dialogue_david_8.mp3" },
  // Listening 1 (arthur)
  { text: "Good morning, everyone. I am presenting the results of our vendor negotiation for the new cloud infrastructure. We received three proposals from different vendors. After reviewing the terms, we chose CloudScale Solutions. Their original proposal was 450 thousand dollars per year for 500 terabytes. We negotiated a 15 percent discount by committing to a two-year contract, bringing the annual cost to 382 thousand dollars. The SLA includes 99.9 percent uptime with a penalty clause of 5 percent credit per incident. We also negotiated a volume-based pricing clause. If we increase to 800 terabytes, the unit price drops by 12 percent. The contract includes a 90-day exit clause if the service quality declines. Overall, we saved 136 thousand dollars over two years compared to the original proposal.", voice: "arthur", file: "rafael-pelizaro/l4_listening1_vendor_negotiation.mp3" },
  // Listening 2 (ellen)
  { text: "Rafael, thank you for the vendor update. I have a few questions. First, you mentioned a 15 percent discount. Can you confirm that is locked in for the full two years? Second, the penalty clause covers uptime, but could you also negotiate penalties for response time? If a critical ticket takes more than 4 hours, we need compensation. And finally, the volume-based pricing sounds promising, but what happens if our volume decreases? Can you check if there is a minimum commitment clause?", voice: "ellen", file: "rafael-pelizaro/l4_listening2_procurement_questions.mp3" },
  // Survival (arthur)
  { text: "Could you offer a better discount for a longer commitment?", voice: "arthur", file: "rafael-pelizaro/l4_survival_could_you_offer.mp3" },
  { text: "Can you include a penalty clause in the SLA?", voice: "arthur", file: "rafael-pelizaro/l4_survival_can_you_include.mp3" },
  { text: "We can offer a two-year commitment if you lower the price.", voice: "arthur", file: "rafael-pelizaro/l4_survival_we_can_offer.mp3" },
  { text: "If you increase the volume, could you reduce the unit cost?", voice: "arthur", file: "rafael-pelizaro/l4_survival_if_you_increase.mp3" },
  { text: "I will send our counteroffer by the end of the week.", voice: "arthur", file: "rafael-pelizaro/l4_survival_i_will_send.mp3" },
  // Speech (arthur)
  { text: "Could you offer a 15 percent discount if we commit to a two-year contract?", voice: "arthur", file: "rafael-pelizaro/l4_speech_could_you_offer.mp3" },
  { text: "We can include a penalty clause for uptime below 99.9 percent.", voice: "arthur", file: "rafael-pelizaro/l4_speech_we_can_include.mp3" },
  { text: "If we increase the volume next year, can you lower the unit price?", voice: "arthur", file: "rafael-pelizaro/l4_speech_if_we_increase.mp3" },

  // ============================================================
  // ESTEPHANO ISHII — AULA 4+5 (37 files, male student = arthur)
  // ============================================================
  { text: "It is 3 o'clock.", voice: "arthur", file: "estephano-akihito-ishii/aula4_it_is_3_oclock.mp3" },
  { text: "We have class at 2 PM.", voice: "ellen", file: "estephano-akihito-ishii/aula4_we_have_class_at_2.mp3" },
  { text: "The meeting is on Thursday.", voice: "arthur", file: "estephano-akihito-ishii/aula4_meeting_on_thursday.mp3" },
  { text: "She studies in the evening.", voice: "ellen", file: "estephano-akihito-ishii/aula4_she_studies_evening.mp3" },
  { text: "He wake up at 7.", voice: "arthur", file: "estephano-akihito-ishii/aula4_he_wake_up_at_7.mp3" },
  { text: "He wakes up at 7.", voice: "arthur", file: "estephano-akihito-ishii/aula4_he_wakes_up_at_7.mp3" },
  // Aula5 vocab sentences
  { text: "My neighborhood is very safe.", voice: "arthur", file: "estephano-akihito-ishii/aula5_my_neighborhood_is_very_safe.mp3" },
  { text: "I live on Paulista Street.", voice: "arthur", file: "estephano-akihito-ishii/aula5_i_live_on_paulista_street.mp3" },
  { text: "My university is in a big building.", voice: "arthur", file: "estephano-akihito-ishii/aula5_my_university_is_in_a_big_building.mp3" },
  { text: "The metro station is near my house.", voice: "arthur", file: "estephano-akihito-ishii/aula5_the_metro_station_is_near_my_house.mp3" },
  { text: "The park is near the library.", voice: "ellen", file: "estephano-akihito-ishii/aula5_the_park_is_near_the_library.mp3" },
  { text: "The airport is far from here.", voice: "arthur", file: "estephano-akihito-ishii/aula5_the_airport_is_far_from_here.mp3" },
  { text: "The bank is between the pharmacy and the supermarket.", voice: "ellen", file: "estephano-akihito-ishii/aula5_the_bank_is_between_the_pharmacy.mp3" },
  { text: "I live in São Paulo.", voice: "arthur", file: "estephano-akihito-ishii/aula5_i_live_in_sao_paulo.mp3" },
  { text: "I study in Liberdade.", voice: "arthur", file: "estephano-akihito-ishii/aula5_i_study_in_liberdade.mp3" },
  { text: "My house is on Rua Augusta.", voice: "arthur", file: "estephano-akihito-ishii/aula5_my_house_is_on_rua_augusta.mp3" },
  { text: "The store is on the corner.", voice: "ellen", file: "estephano-akihito-ishii/aula5_the_store_is_on_the_corner.mp3" },
  { text: "I am at the university.", voice: "arthur", file: "estephano-akihito-ishii/aula5_i_am_at_the_university.mp3" },
  { text: "She is at the bus stop.", voice: "ellen", file: "estephano-akihito-ishii/aula5_she_is_at_the_bus_stop.mp3" },
  { text: "The supermarket is next to the metro station.", voice: "arthur", file: "estephano-akihito-ishii/aula5_the_supermarket_is_next_to_the_metro.mp3" },
  { text: "My apartment is on Rua Galvão Bueno.", voice: "arthur", file: "estephano-akihito-ishii/aula5_my_apartment_is_on_rua_galvao_bueno.mp3" },
  // Dialogue
  { text: "Where do you live, Estephano?", voice: "ellen", file: "estephano-akihito-ishii/aula5_where_do_you_live_estephano.mp3" },
  { text: "I live in Liberdade. It's a neighborhood in São Paulo.", voice: "arthur", file: "estephano-akihito-ishii/aula5_i_live_in_liberdade_neighborhood.mp3" },
  { text: "Is it near the university?", voice: "ellen", file: "estephano-akihito-ishii/aula5_is_it_near_the_university.mp3" },
  { text: "Yes, the metro station is near my building.", voice: "arthur", file: "estephano-akihito-ishii/aula5_yes_the_metro_station_is_near.mp3" },
  { text: "What is near your house?", voice: "ellen", file: "estephano-akihito-ishii/aula5_what_is_near_your_house.mp3" },
  { text: "There is a supermarket next to the metro station. And a park between my street and the avenue.", voice: "arthur", file: "estephano-akihito-ishii/aula5_there_is_a_supermarket_next_to.mp3" },
  { text: "Is the airport far?", voice: "ellen", file: "estephano-akihito-ishii/aula5_is_the_airport_far.mp3" },
  { text: "Yes, it's very far from Liberdade.", voice: "arthur", file: "estephano-akihito-ishii/aula5_yes_its_very_far_from_liberdade.mp3" },
  // Speech
  { text: "I live in Liberdade. The metro station is near my building.", voice: "arthur", file: "estephano-akihito-ishii/aula5_speech1_live_liberdade.mp3" },
  { text: "My apartment is on Rua Galvão Bueno. The supermarket is next to the station.", voice: "arthur", file: "estephano-akihito-ishii/aula5_speech2_apartment_rua.mp3" },
  // Listening
  { text: "I live in Liberdade, a neighborhood in São Paulo. My apartment is on Rua Galvão Bueno. The metro station is near my building. There is a supermarket next to the station. I study at a university in Liberdade. My university is in a big building on Paulista Street. The park is near the library. The airport is very far from my neighborhood.", voice: "arthur", file: "estephano-akihito-ishii/aula5_listening_context.mp3" },
  { text: "Excuse me, where is the pharmacy? Go straight on this street. Turn left at the corner. The pharmacy is next to the supermarket. And the bank? The bank is between the pharmacy and the post office. Is there a park near here? Yes, there is a park behind the library.", voice: "ellen", file: "estephano-akihito-ishii/aula5_listening_directions.mp3" },
  // Fill-in
  { text: "I live in a big neighborhood.", voice: "arthur", file: "estephano-akihito-ishii/aula5_i_live_in_a_big_neighborhood.mp3" },
  { text: "The station is between my house and the park.", voice: "ellen", file: "estephano-akihito-ishii/aula5_the_station_is_between_my_house.mp3" },
  { text: "My building is on the main street.", voice: "arthur", file: "estephano-akihito-ishii/aula5_my_building_is_on_the_main_street.mp3" },
  { text: "The library is near the university.", voice: "ellen", file: "estephano-akihito-ishii/aula5_the_library_is_near_the_university.mp3" },
  { text: "The hospital is far from my neighborhood.", voice: "arthur", file: "estephano-akihito-ishii/aula5_the_hospital_is_far_from.mp3" },
  // Ordering
  { text: "I live in Liberdade. My apartment is on Rua Galvão Bueno. The metro station is near my building. The supermarket is next to the station. The park is between my street and the avenue.", voice: "arthur", file: "estephano-akihito-ishii/order_l5_prepositions.mp3" },

  // ============================================================
  // CARLOS BASSAN — AULA 4 (14 files, male = arthur)
  // ============================================================
  { text: "I would like to confirm whether the deal is still on track.", voice: "arthur", file: "carlos-vinicius-vale-bassan/aula4_i_would_like_to_confirm_whether_the_deal_is_stil.mp3" },
  { text: "Let me paraphrase what you just said to make sure I understand.", voice: "arthur", file: "carlos-vinicius-vale-bassan/aula4_let_me_paraphrase_what_you_just_said.mp3" },
  { text: "I will follow up with the legal team on that.", voice: "arthur", file: "carlos-vinicius-vale-bassan/aula4_i_will_follow_up_with_the_legal_team.mp3" },
  { text: "Sorry, I did not catch that. Could you say it again?", voice: "arthur", file: "carlos-vinicius-vale-bassan/aula4_sorry_i_did_not_catch_that.mp3" },
  { text: "Could you clarify what you mean by synergy targets?", voice: "arthur", file: "carlos-vinicius-vale-bassan/aula4_could_you_clarify_what_you_mean_by_synergy_targe.mp3" },
  { text: "If I understand correctly, you are saying that the valuation needs to be revised.", voice: "ellen", file: "carlos-vinicius-vale-bassan/aula4_if_i_understand_correctly_valuation_revised.mp3" },
  { text: "So what you are saying is that we should postpone the closing date.", voice: "arthur", file: "carlos-vinicius-vale-bassan/aula4_so_what_you_are_saying_is_postpone_closing.mp3" },
  { text: "David, could you clarify what you mean by the earn-out structure?", voice: "arthur", file: "carlos-vinicius-vale-bassan/aula4_david_clarify_earnout.mp3" },
  { text: "Could you clarify what the main risk factors are?", voice: "arthur", file: "carlos-vinicius-vale-bassan/aula4_clarify_main_risk_factors.mp3" },
  { text: "If I understand correctly, the timeline has been moved to Q3.", voice: "arthur", file: "carlos-vinicius-vale-bassan/aula4_understand_correctly_timeline_q3.mp3" },
  { text: "So what you are saying is we need more due diligence on the tech stack.", voice: "arthur", file: "carlos-vinicius-vale-bassan/aula4_saying_is_more_due_diligence.mp3" },
  { text: "Sorry, I did not catch that. Could you repeat the last point?", voice: "ellen", file: "carlos-vinicius-vale-bassan/aula4_did_not_catch_repeat_last_point.mp3" },
  { text: "Let me paraphrase to make sure we are aligned.", voice: "arthur", file: "carlos-vinicius-vale-bassan/aula4_paraphrase_to_make_sure_aligned.mp3" },
  { text: "I will follow up with the CFO on the working capital figures.", voice: "arthur", file: "carlos-vinicius-vale-bassan/aula4_follow_up_cfo_working_capital.mp3" },

  // ============================================================
  // ROBERTO REZENDE — AULA 8 (11 files, male = arthur)
  // ============================================================
  { text: "Small talk is important for building business relationships.", voice: "arthur", file: "roberto-rezende/aula8_small_talk_is_important.mp3" },
  { text: "I always try to break the ice before a meeting.", voice: "arthur", file: "roberto-rezende/aula8_i_always_try_to_break.mp3" },
  { text: "Networking events are a great opportunity to meet new clients.", voice: "ellen", file: "roberto-rezende/aula8_networking_events_are.mp3" },
  { text: "We found common ground when we discovered we both like engineering.", voice: "arthur", file: "roberto-rezende/aula8_we_found_common_ground.mp3" },
  { text: "Let me catch up with you after the presentation.", voice: "ellen", file: "roberto-rezende/aula8_let_me_catch_up.mp3" },
  { text: "I get along well with my colleagues from Shanghai.", voice: "arthur", file: "roberto-rezende/aula8_i_get_along_well.mp3" },
  { text: "Do not bring up politics or religion at a business dinner.", voice: "ellen", file: "roberto-rezende/aula8_do_not_bring_up.mp3" },
  { text: "Let us keep in touch after the conference.", voice: "arthur", file: "roberto-rezende/aula8_let_us_keep_in_touch.mp3" },
  { text: "By the way, have you tried the local food here?", voice: "arthur", file: "roberto-rezende/aula8_by_the_way_have_you.mp3" },
  { text: "How about we grab a coffee after the session?", voice: "ellen", file: "roberto-rezende/aula8_how_about_we_grab.mp3" },
  { text: "Thank you, Roberto. That was very helpful. A few questions. First, you said we should break the ice with something simple. Can you give us two more examples of good opening questions? Second, you mentioned we should not bring up politics. What other topics should we avoid? Third, how do you keep in touch after the event? Do you exchange business cards or connect on LinkedIn? And finally, tag questions like is it not and do we not. Are they formal or informal? Should we use them with clients or only with colleagues?", voice: "ellen", file: "roberto-rezende/aula8_listening2_amy_smalltalk_questions.mp3" },

  // ============================================================
  // MARIA CLAUDIA — AULA 4 (11 files, female = ellen)
  // ============================================================
  { text: "Our revenue grew 12 percent compared to last quarter.", voice: "ellen", file: "maria-claudia-curimbaba/aula4_our_revenue_grew_12_percent.mp3" },
  { text: "The profit margin improved because we reduced expenses.", voice: "arthur", file: "maria-claudia-curimbaba/aula4_the_profit_margin_improved.mp3" },
  { text: "We are on track to stay within the Q3 budget.", voice: "ellen", file: "maria-claudia-curimbaba/aula4_we_are_on_track_to_stay.mp3" },
  { text: "The forecast for Q4 shows a 15 percent increase in revenue.", voice: "arthur", file: "maria-claudia-curimbaba/aula4_the_forecast_for_q4_shows.mp3" },
  { text: "Our expenses were lower than expected this quarter.", voice: "ellen", file: "maria-claudia-curimbaba/aula4_our_expenses_were_lower.mp3" },
  { text: "We achieved 8 percent growth compared to the same quarter last year.", voice: "arthur", file: "maria-claudia-curimbaba/aula4_we_achieved_8_percent_growth.mp3" },
  { text: "Our profit margin is 22 percent, which is higher than last year.", voice: "ellen", file: "maria-claudia-curimbaba/aula4_our_profit_margin_is_22.mp3" },
  { text: "The numbers show that Q3 was our strongest quarter this year.", voice: "arthur", file: "maria-claudia-curimbaba/aula4_the_numbers_show_q3.mp3" },
  { text: "Compared to last quarter...", voice: "ellen", file: "maria-claudia-curimbaba/aula4_expr_compared_to_last_quarter.mp3" },
  { text: "The numbers show that...", voice: "arthur", file: "maria-claudia-curimbaba/aula4_expr_the_numbers_show_that.mp3" },
  { text: "We are on track to...", voice: "ellen", file: "maria-claudia-curimbaba/aula4_expr_we_are_on_track_to.mp3" },

  // ============================================================
  // MARIA CLAUDIA — AULA 5 (5 files, female = ellen)
  // ============================================================
  { text: "The painting has a striking combination of red and gold.", voice: "ellen", file: "maria-claudia-curimbaba/aula5_the_painting_has.mp3" },
  { text: "I prefer abstract art because it makes me think.", voice: "ellen", file: "maria-claudia-curimbaba/aula5_i_prefer_abstract.mp3" },
  { text: "The museum has a new exhibit of contemporary Brazilian artists.", voice: "arthur", file: "maria-claudia-curimbaba/aula5_the_museum_has.mp3" },
  { text: "The artist used vibrant colors to express joy.", voice: "ellen", file: "maria-claudia-curimbaba/aula5_the_artist_used.mp3" },
  { text: "There is a subtle contrast between the background and the figure.", voice: "arthur", file: "maria-claudia-curimbaba/aula5_there_is_a_subtle.mp3" },

  // ============================================================
  // RAFAEL BRANDAO — AULA 3 (27 files, male = arthur)
  // ============================================================
  { text: "Headquarter", voice: "arthur", file: "rafael-de-andrade-brandao/aula3_headquarter.mp3" },
  { text: "Our main product is technology solutions for businesses.", voice: "arthur", file: "rafael-de-andrade-brandao/aula3_our_main_product_is_technology.mp3" },
  { text: "There is a meeting room on each floor.", voice: "ellen", file: "rafael-de-andrade-brandao/aula3_there_is_a_meeting_room.mp3" },
  { text: "There are fifty employees in our department.", voice: "arthur", file: "rafael-de-andrade-brandao/aula3_there_are_fifty_employees.mp3" },
  { text: "Is there a branch in Rio?", voice: "ellen", file: "rafael-de-andrade-brandao/aula3_is_there_a_branch_in_rio.mp3" },
  { text: "There are over two hundred employees.", voice: "arthur", file: "rafael-de-andrade-brandao/aula3_there_are_over_two_hundred.mp3" },
  { text: "TVT is a technology company.", voice: "arthur", file: "rafael-de-andrade-brandao/aula3_tvt_is_a_tech_company_short.mp3" },
  { text: "There are over two hundred employees at TVT.", voice: "arthur", file: "rafael-de-andrade-brandao/aula3_there_are_over_200_at_tvt.mp3" },
  { text: "Our main product is technology solutions.", voice: "arthur", file: "rafael-de-andrade-brandao/aula3_our_main_product_short.mp3" },
  { text: "We plan to expand to new markets.", voice: "arthur", file: "rafael-de-andrade-brandao/aula3_we_plan_to_expand_short.mp3" },
  { text: "Our headquarters is in São Paulo and we have branches in three cities.", voice: "arthur", file: "rafael-de-andrade-brandao/aula3_hq_sao_paulo_branches.mp3" },
  { text: "The revenue increased last year and the company is growing.", voice: "ellen", file: "rafael-de-andrade-brandao/aula3_revenue_increased_growing.mp3" },
  { text: "There are two hundred employees at TVT.", voice: "arthur", file: "rafael-de-andrade-brandao/aula3_err1_correct.mp3" },
  { text: "Our company has branches in three cities.", voice: "arthur", file: "rafael-de-andrade-brandao/aula3_err2_correct.mp3" },
  { text: "TVT is a technology company.", voice: "arthur", file: "rafael-de-andrade-brandao/aula3_err3_correct.mp3" },
  { text: "There is a strong demand for our products.", voice: "ellen", file: "rafael-de-andrade-brandao/aula3_err4_correct.mp3" },
  { text: "The company's revenue increased.", voice: "arthur", file: "rafael-de-andrade-brandao/aula3_err5_correct.mp3" },
  { text: "Our headquarters is in São Paulo. We have over two hundred employees.", voice: "arthur", file: "rafael-de-andrade-brandao/aula3_oral1.mp3" },
  { text: "Our main product is technology solutions for large businesses.", voice: "arthur", file: "rafael-de-andrade-brandao/aula3_oral2.mp3" },
  { text: "There are branches in three cities. We plan to expand to new markets.", voice: "arthur", file: "rafael-de-andrade-brandao/aula3_oral3.mp3" },
  { text: "The technology industry is growing fast. There is a strong demand.", voice: "ellen", file: "rafael-de-andrade-brandao/aula3_oral4.mp3" },
  { text: "Our revenue increased last year. We are expanding.", voice: "arthur", file: "rafael-de-andrade-brandao/aula3_oral5.mp3" },
  { text: "TVT is a company in the technology industry. There are over two hundred employees.", voice: "arthur", file: "rafael-de-andrade-brandao/aula3_oral6.mp3" },
  { text: "Our headquarters is in São Paulo.", voice: "arthur", file: "rafael-de-andrade-brandao/aula3_toolkit1.mp3" },
  { text: "There are over two hundred employees.", voice: "arthur", file: "rafael-de-andrade-brandao/aula3_toolkit2.mp3" },
  { text: "Our main product is technology solutions.", voice: "arthur", file: "rafael-de-andrade-brandao/aula3_toolkit3.mp3" },
  { text: "Could you tell me more about your company?", voice: "ellen", file: "rafael-de-andrade-brandao/aula3_toolkit5.mp3" },

  // ============================================================
  // RAFAEL BRANDAO — MAIN (6 additional, same aula3 content)
  // ============================================================
  { text: "The company is expanding to new markets.", voice: "arthur", file: "rafael-de-andrade-brandao/aula3_survival_the_company_expanding.mp3" },
  { text: "Could you tell me more about your company?", voice: "ellen", file: "rafael-de-andrade-brandao/aula3_survival_could_you_tell.mp3" },
  { text: "TVT is a technology company. Our headquarters is in São Paulo.", voice: "arthur", file: "rafael-de-andrade-brandao/aula3_speech_tvt_is_tech.mp3" },
  { text: "There are over two hundred employees. We have branches in three cities.", voice: "arthur", file: "rafael-de-andrade-brandao/aula3_speech_there_are_over.mp3" },
  // toolkit4 already in aula3 list above as aula3_toolkit4 — but referenced differently in main
  { text: "The company is expanding to new markets.", voice: "arthur", file: "rafael-de-andrade-brandao/aula3_toolkit4.mp3" },

  // ============================================================
  // NILO PATUCCI — 2 truncated files
  // ============================================================
  { text: "Let me introduce myself. I am Nilo Patussi, Chief Compliance Officer at Corinthians.", voice: "arthur", file: "nilo-mesquita-patucci/let_me_introduce_myself_i_am_nilo_patussi_chief_co.mp3" },
  { text: "I am Nilo Patussi, Chief Compliance Officer at Corinthians.", voice: "arthur", file: "nilo-mesquita-patucci/i_am_nilo_patussi_chief_compliance_officer_at_cori.mp3" },
];

const BASE_DIR = path.join(__dirname, '..', 'public', 'audio');

async function generate(text, voiceKey, filepath) {
  const fullpath = path.join(BASE_DIR, filepath);
  if (fs.existsSync(fullpath)) { console.log('SKIP:', filepath); return; }
  const dir = path.dirname(fullpath);
  if (!fs.existsSync(dir)) fs.mkdirSync(dir, { recursive: true });
  const voiceId = VOICES[voiceKey];
  if (!voiceId) { console.error('UNKNOWN VOICE:', voiceKey); return; }
  console.log('GEN:', filepath);
  try {
    const res = await fetch(`https://api.elevenlabs.io/v1/text-to-speech/${voiceId}`, {
      method: 'POST',
      headers: { 'xi-api-key': API_KEY, 'Content-Type': 'application/json' },
      body: JSON.stringify({
        text,
        model_id: 'eleven_multilingual_v2',
        voice_settings: { stability: 0.5, similarity_boost: 0.75, style: 0, use_speaker_boost: true }
      })
    });
    if (!res.ok) { console.error('FAIL:', filepath, res.status); return; }
    const buf = Buffer.from(await res.arrayBuffer());
    fs.writeFileSync(fullpath, buf);
    console.log('OK:', filepath, (buf.length/1024).toFixed(1)+'KB');
  } catch(e) { console.error('ERR:', filepath, e.message); }
}

(async () => {
  if (!API_KEY) { console.error('Set ELEVENLABS_API_KEY env var'); process.exit(1); }
  console.log(`Generating ${PHRASES.length} audio files for ${new Set(PHRASES.map(p=>p.file.split('/')[0])).size} students...`);
  let done = 0;
  for (const p of PHRASES) {
    await generate(p.text, p.voice, p.file);
    done++;
    if (done % 10 === 0) console.log(`Progress: ${done}/${PHRASES.length}`);
    await new Promise(r => setTimeout(r, 400));
  }
  console.log(`\nDone! ${done} files processed.`);
})();
