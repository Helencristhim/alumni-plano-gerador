#!/usr/bin/env node
/**
 * Generate ElevenLabs audio files for Rafael Gasparelli Lima — Lesson 1
 *
 * Voice alternation rules:
 *   - Single words (1-2 words) = ALWAYS Arthur
 *   - Phrases (3+ words) = ALTERNATE Arthur/Ellen
 *   - Dialogue lines: use data-voice from HTML (all male characters = Arthur)
 *
 * Usage: ELEVENLABS_API_KEY=... node generate-rafael-audio.js
 */

const fs = require('fs');
const path = require('path');

const API_URL = 'https://api.elevenlabs.io/v1/text-to-speech';
const VOICES = {
  arthur: 'sfJopaWaOtauCD3HKX6Q',  // Male, neutral American
  ellen: 'BIvP0GN1cAtSRTxNHnWS'    // Female, calm American
};
const API_KEY = process.env.ELEVENLABS_API_KEY;
const OUTPUT_DIR = path.join(__dirname, '..', 'public', 'audio', 'rafael-gasparelli-lima');
const PROF_HTML = path.join(__dirname, '..', 'public', 'professor', 'rafael-gasparelli-lima.html');

if (!API_KEY) {
  console.error('ERROR: Set ELEVENLABS_API_KEY environment variable.');
  process.exit(1);
}

if (!fs.existsSync(OUTPUT_DIR)) {
  fs.mkdirSync(OUTPUT_DIR, { recursive: true });
}

// ===== AUDIO MAP — extracted from professor HTML =====
// Each entry: { text, filename, voice }
// voice is determined by alternation rules or dialogue data-voice

const audioEntries = [
  // --- Vocab cards (1-2 words = Arthur) ---
  { text: "Board of Directors", filename: "board_of_directors.mp3", voice: "arthur" },
  { text: "Headquarters", filename: "headquarters.mp3", voice: "arthur" },
  { text: "To manage", filename: "to_manage.mp3", voice: "arthur" },
  { text: "Industry", filename: "industry.mp3", voice: "arthur" },
  { text: "Meeting", filename: "meeting.mp3", voice: "arthur" },
  { text: "Role", filename: "role.mp3", voice: "arthur" },
  { text: "To report to", filename: "to_report_to.mp3", voice: "arthur" },
  { text: "Subsidiary", filename: "subsidiary.mp3", voice: "arthur" },

  // --- Short expressions (3 words but idiomatic = alternate) ---
  { text: "run a business", filename: "run_a_business.mp3", voice: "arthur" },
  { text: "be in charge of", filename: "be_in_charge_of.mp3", voice: "ellen" },
  { text: "work in an industry", filename: "work_in_an_industry.mp3", voice: "arthur" },

  // --- Vocab example sentences (3+ words = alternate Arthur/Ellen) ---
  { text: "I am a member of the board of directors.", filename: "i_am_a_member_of_the_board_of_directors.mp3", voice: "ellen" },
  { text: "Our headquarters is in São Paulo.", filename: "our_headquarters_is_in_sao_paulo.mp3", voice: "arthur" },
  { text: "I manage the legal department of the group.", filename: "i_manage_the_legal_department_of_the_group.mp3", voice: "ellen" },
  { text: "The iron industry is our main business.", filename: "the_iron_industry_is_our_main_business.mp3", voice: "arthur" },
  { text: "I have a meeting with my boss every Monday.", filename: "i_have_a_meeting_with_my_boss_every_monday.mp3", voice: "ellen" },
  { text: "My role includes legal and corporate duties.", filename: "my_role_includes_legal_and_corporate_duties.mp3", voice: "arthur" },
  { text: "I report to the CEO of the group.", filename: "i_report_to_the_ceo_of_the_group.mp3", voice: "ellen" },
  { text: "We have subsidiaries in agriculture and iron.", filename: "we_have_subsidiaries_in_agriculture_and_iron.mp3", voice: "arthur" },

  // --- Context / Grammar sentences (alternate) ---
  { text: "I work in a large economic group called Picunha.", filename: "i_work_in_a_large_economic_group.mp3", voice: "ellen" },
  { text: "Rafael manages the legal department.", filename: "rafael_manages_the_legal_department.mp3", voice: "arthur" },
  { text: "Our company operates in two industries: iron and agriculture.", filename: "our_company_operates_in_two_industries.mp3", voice: "ellen" },
  { text: "He doesn't use English very often at work.", filename: "he_doesnt_use_english_very_often.mp3", voice: "arthur" },
  { text: "Does Rafael travel to the United States every year?", filename: "does_rafael_travel_to_the_us_every_year.mp3", voice: "ellen" },

  // --- Pronunciation practice sentences (alternate) ---
  { text: "Good morning. My name is Rafael Gasparelli Lima.", filename: "good_morning_my_name_is_rafael.mp3", voice: "arthur" },
  { text: "I am a lawyer and director at Grupo Picunha in São Paulo.", filename: "i_am_a_lawyer_and_director_at_grupo_picunha.mp3", voice: "ellen" },
  { text: "Our company operates in the iron industry and agriculture.", filename: "our_company_operates_in_iron_and_agriculture.mp3", voice: "arthur" },
  { text: "I manage the legal department and serve on the board of directors.", filename: "i_manage_the_legal_dept_and_serve_on_board.mp3", voice: "ellen" },
  { text: "It is a pleasure to meet you.", filename: "it_is_a_pleasure_to_meet_you.mp3", voice: "arthur" },

  // --- Speech cards (alternate) ---
  { text: "My name is Rafael Gasparelli Lima. I am a lawyer and director.", filename: "my_name_is_rafael_i_am_a_lawyer.mp3", voice: "ellen" },
  { text: "Our headquarters is in São Paulo, but we operate in two industries.", filename: "our_hq_is_in_sp_but_we_operate_in_two.mp3", voice: "arthur" },
  { text: "I report to the CEO and serve on the board of directors.", filename: "i_report_to_ceo_and_serve_on_board.mp3", voice: "ellen" },
  { text: "Could you repeat that, please?", filename: "could_you_repeat_that_please.mp3", voice: "arthur" },
  { text: "I work at Grupo Picunha. We operate in iron and agriculture.", filename: "i_work_at_grupo_picunha_we_operate.mp3", voice: "ellen" },

  // --- Dialogue lines (all male characters: David=arthur, Rafael=arthur) ---
  { text: "Good morning, everyone. Welcome to the quarterly board call. We have a new member joining us today from São Paulo. Rafael, would you like to introduce yourself?", filename: "david_welcome_to_quarterly_board_call.mp3", voice: "arthur" },
  { text: "Good morning. My name is Rafael Gasparelli Lima. I am a lawyer and director at Grupo Picunha.", filename: "rafael_intro_board_call.mp3", voice: "arthur" },
  { text: "Welcome, Rafael. Can you tell us a bit about your company?", filename: "david_welcome_rafael.mp3", voice: "arthur" },
  { text: "Of course. Our company operates in two main industries: iron manufacturing and agriculture. Our headquarters is in São Paulo.", filename: "rafael_our_company_operates.mp3", voice: "arthur" },
  { text: "Interesting. What is your role exactly?", filename: "david_what_is_your_role.mp3", voice: "arthur" },
  { text: "I manage the legal department, and I also serve on the board of directors. I report to the CEO.", filename: "rafael_i_manage_legal_dept.mp3", voice: "arthur" },
  { text: "Great to have you on board. Do you travel to the U.S. often?", filename: "david_great_to_have_you.mp3", voice: "arthur" },
  { text: "Yes, I travel to the United States once a year. I want to improve my English for these meetings.", filename: "rafael_yes_i_travel_to_us.mp3", voice: "arthur" },
  { text: "Your English sounds good, Rafael. Welcome to the team.", filename: "david_your_english_sounds_good.mp3", voice: "arthur" },
  { text: "Thank you. It is a pleasure to meet everyone.", filename: "rafael_thank_you_pleasure.mp3", voice: "arthur" },

  // --- Quiz / Practice sentences (alternate) ---
  { text: "Rafael works at Grupo Picunha.", filename: "rafael_works_at_grupo_picunha.mp3", voice: "arthur" },
  { text: "The company operates in iron and agriculture.", filename: "the_company_operates_in_iron.mp3", voice: "ellen" },
  { text: "He doesn't use English at work every day.", filename: "he_doesnt_use_english_every_day.mp3", voice: "arthur" },
  { text: "Does he travel to the U.S. every year?", filename: "does_he_travel_to_us_every_year.mp3", voice: "ellen" },
  { text: "Rafael works in São Paulo.", filename: "rafael_works_in_sao_paulo.mp3", voice: "arthur" },
  { text: "He doesn't travel overseas.", filename: "he_doesnt_travel_overseas.mp3", voice: "ellen" },
  { text: "Does the company operate in agriculture?", filename: "does_the_company_operate.mp3", voice: "arthur" },

  // --- Survival card / additional sentences (alternate) ---
  { text: "Could you repeat that, please? I want to make sure I understand correctly.", filename: "could_you_repeat_that_i_want_to_make_sure.mp3", voice: "ellen" },
  { text: "I don't work on weekends.", filename: "i_dont_work_on_weekends.mp3", voice: "arthur" },
  { text: "Does your company have subsidiaries?", filename: "does_your_company_have_subsidiaries.mp3", voice: "ellen" },
  { text: "He doesn't report to the board.", filename: "he_doesnt_report_to_the_board.mp3", voice: "arthur" },
  { text: "When I wake up, I take my son to school.", filename: "when_i_wake_up_i_take_my_son.mp3", voice: "ellen" },

  // --- Full intro / listening (alternate) ---
  { text: "Good morning. My name is Rafael Gasparelli Lima. I am a lawyer and director at Grupo Picunha in São Paulo.", filename: "full_intro_rafael.mp3", voice: "arthur" },
  { text: "Our company operates in two main industries: iron manufacturing and agriculture.", filename: "our_company_two_main_industries.mp3", voice: "ellen" },

  // ============================================================
  // LESSON 2 — My Company in Detail
  // ============================================================

  // --- Lesson 2 Vocab cards (1-2 words = Arthur) ---
  { text: "Department", filename: "department.mp3", voice: "arthur" },
  { text: "To supply", filename: "to_supply.mp3", voice: "arthur" },
  { text: "Manufacturing", filename: "manufacturing.mp3", voice: "arthur" },
  { text: "Revenue", filename: "revenue.mp3", voice: "arthur" },
  { text: "Employee", filename: "employee.mp3", voice: "arthur" },
  { text: "Client", filename: "client.mp3", voice: "arthur" },
  { text: "Partnership", filename: "partnership.mp3", voice: "arthur" },
  { text: "To expand", filename: "to_expand.mp3", voice: "arthur" },

  // --- Lesson 2 Expressions (alternate) ---
  { text: "be based in", filename: "be_based_in.mp3", voice: "arthur" },
  { text: "focus on", filename: "focus_on.mp3", voice: "ellen" },
  { text: "deal with", filename: "deal_with.mp3", voice: "arthur" },

  // --- Lesson 2 Vocab example sentences (alternate) ---
  { text: "Rafael works in the legal department.", filename: "rafael_works_in_the_legal_department.mp3", voice: "ellen" },
  { text: "Our company supplies iron to other businesses.", filename: "our_company_supplies_iron.mp3", voice: "arthur" },
  { text: "The iron manufacturing division is the biggest.", filename: "the_iron_manufacturing_division.mp3", voice: "ellen" },
  { text: "Our revenue comes from two main industries.", filename: "our_revenue_comes_from_two.mp3", voice: "arthur" },
  { text: "The group has over five hundred employees.", filename: "the_group_has_over_five_hundred.mp3", voice: "ellen" },
  { text: "We have clients in Brazil and overseas.", filename: "we_have_clients_in_brazil.mp3", voice: "arthur" },
  { text: "We have partnerships with international firms.", filename: "we_have_partnerships_with_intl.mp3", voice: "ellen" },
  { text: "The company wants to expand operations overseas.", filename: "the_company_wants_to_expand.mp3", voice: "arthur" },

  // --- Lesson 2 Expression examples ---
  { text: "Our company is based in São Paulo.", filename: "our_company_is_based_in_sp.mp3", voice: "ellen" },
  { text: "The legal department focuses on contracts.", filename: "the_legal_dept_focuses_on.mp3", voice: "arthur" },
  { text: "I deal with corporate governance issues.", filename: "i_deal_with_corporate_governance.mp3", voice: "ellen" },

  // --- Lesson 2 Grammar / Fill-in sentences (alternate) ---
  { text: "The company manufactures iron products.", filename: "the_company_manufactures_iron.mp3", voice: "arthur" },
  { text: "Our agricultural division produces fruits and meat.", filename: "our_agricultural_division_produces.mp3", voice: "ellen" },
  { text: "Rafael deals with corporate governance issues.", filename: "rafael_deals_with_corporate.mp3", voice: "arthur" },
  { text: "The company doesn't export directly to the United States.", filename: "the_company_doesnt_export.mp3", voice: "ellen" },
  { text: "Does the legal department focus on contracts?", filename: "does_the_legal_dept_focus.mp3", voice: "arthur" },
  { text: "We have partnerships with international companies.", filename: "we_have_partnerships_intl_co.mp3", voice: "ellen" },
  { text: "Our company operates in two industries: iron and agriculture.", filename: "our_company_operates_two_industries.mp3", voice: "arthur" },

  // --- Lesson 2 Speech cards (alternate) ---
  { text: "Our company manufactures iron and supplies it to construction businesses.", filename: "our_company_manufactures_iron_supplies.mp3", voice: "ellen" },
  { text: "The group has over five hundred employees across Brazil.", filename: "the_group_has_500_employees_brazil.mp3", voice: "arthur" },
  { text: "The company doesn't export directly, but we want to expand.", filename: "the_company_doesnt_export_but.mp3", voice: "ellen" },
  { text: "Our revenue comes from iron manufacturing and agriculture.", filename: "our_revenue_from_iron_and_agri.mp3", voice: "arthur" },

  // --- Lesson 2 Ordering (alternate) ---
  { text: "Our company is called Grupo Picunha.", filename: "our_company_is_called_grupo.mp3", voice: "ellen" },
  { text: "We are based in São Paulo, Brazil.", filename: "we_are_based_in_sao_paulo.mp3", voice: "arthur" },
  { text: "The group operates in two industries: iron and agriculture.", filename: "the_group_operates_in_two.mp3", voice: "ellen" },
  { text: "We have over five hundred employees.", filename: "we_have_over_five_hundred.mp3", voice: "arthur" },
  { text: "We are looking to expand our operations overseas.", filename: "we_are_looking_to_expand.mp3", voice: "ellen" },

  // --- Lesson 2 Survival Card (alternate) ---
  { text: "We supply iron to construction companies across Brazil.", filename: "we_supply_iron_to_construction.mp3", voice: "arthur" },

  // --- Lesson 2 Dialogue: Sarah Mitchell (ellen) + Rafael (arthur) ---
  { text: "Good afternoon, Rafael. Thank you for joining this call. I would like to learn more about Grupo Picunha.", filename: "sarah_good_afternoon_rafael.mp3", voice: "ellen" },
  { text: "Good afternoon, Sarah. Thank you for your interest. Our company is based in São Paulo, Brazil.", filename: "rafael_good_afternoon_sarah.mp3", voice: "arthur" },
  { text: "What industries does the group operate in?", filename: "sarah_what_industries.mp3", voice: "ellen" },
  { text: "We operate in two main industries. Our first division manufactures and supplies iron to construction companies.", filename: "rafael_we_operate_two_main.mp3", voice: "arthur" },
  { text: "Interesting. And the second division?", filename: "sarah_interesting_second.mp3", voice: "ellen" },
  { text: "The second division focuses on agriculture. It produces fruits and meat for domestic and international markets.", filename: "rafael_second_division_focuses.mp3", voice: "arthur" },
  { text: "How many employees does the group have?", filename: "sarah_how_many_employees.mp3", voice: "ellen" },
  { text: "The group has over five hundred employees across both divisions.", filename: "rafael_group_has_500.mp3", voice: "arthur" },
  { text: "Does the company have any international partnerships?", filename: "sarah_does_company_have_intl.mp3", voice: "ellen" },
  { text: "Yes, we have partnerships with international firms. The company wants to expand operations overseas.", filename: "rafael_yes_partnerships.mp3", voice: "arthur" },
  { text: "That sounds very promising. I look forward to learning more.", filename: "sarah_that_sounds_promising.mp3", voice: "ellen" },
  { text: "Thank you, Sarah. We would be happy to share more details.", filename: "rafael_thank_you_sarah.mp3", voice: "arthur" },

  // --- Lesson 2 Grammar practice / Spot the Error ---
  { text: "Our division produces fruits and meat.", filename: "our_division_produces_fruits.mp3", voice: "ellen" },
  { text: "The CEO doesn't want to wait.", filename: "the_ceo_doesnt_want.mp3", voice: "arthur" },
  { text: "Does the company have international clients?", filename: "does_the_company_have_intl.mp3", voice: "ellen" },
  { text: "The company supplies iron to clients across Brazil.", filename: "the_company_supplies_iron_clients.mp3", voice: "arthur" },
  { text: "The group has many employees.", filename: "the_group_has_many_employees.mp3", voice: "ellen" },
  { text: "Does the division produce meat?", filename: "does_the_division_produce_meat.mp3", voice: "arthur" },

  // ============================================================
  // LESSON 3 — Daily Routine
  // ============================================================
  { text: "The company supply iron to clients.", filename: "the_company_supply_iron_error.mp3", voice: "arthur" },
  { text: "Commute", filename: "commute.mp3", voice: "arthur" },
  { text: "Schedule", filename: "schedule.mp3", voice: "arthur" },
  { text: "Deadline", filename: "deadline.mp3", voice: "arthur" },
  { text: "Lunch break", filename: "lunch_break.mp3", voice: "arthur" },
  { text: "To attend", filename: "to_attend.mp3", voice: "arthur" },
  { text: "Routine", filename: "routine.mp3", voice: "arthur" },
  { text: "Appointment", filename: "appointment.mp3", voice: "arthur" },
  { text: "Overtime", filename: "overtime.mp3", voice: "arthur" },
  { text: "wake up early", filename: "wake_up_early.mp3", voice: "ellen" },
  { text: "work out", filename: "work_out.mp3", voice: "arthur" },
  { text: "pick up someone", filename: "pick_up_someone.mp3", voice: "arthur" },
  { text: "Rafael's commute to the office takes about thirty minutes.", filename: "rafaels_commute_takes_thirty_min.mp3", voice: "ellen" },
  { text: "My schedule is very busy during the week.", filename: "my_schedule_is_very_busy.mp3", voice: "arthur" },
  { text: "I have an important deadline on Friday.", filename: "i_have_an_important_deadline.mp3", voice: "ellen" },
  { text: "I usually have lunch during my lunch break at 12.", filename: "i_usually_have_lunch_break.mp3", voice: "arthur" },
  { text: "I attend meetings every morning.", filename: "i_attend_meetings_every_morning.mp3", voice: "ellen" },
  { text: "My routine starts at 6 a.m.", filename: "my_routine_starts_at_6am.mp3", voice: "arthur" },
  { text: "I have an appointment with a client at 3 p.m.", filename: "i_have_an_appointment_3pm.mp3", voice: "ellen" },
  { text: "I rarely work overtime, but this week is different.", filename: "i_rarely_work_overtime_but.mp3", voice: "arthur" },
  { text: "I always wake up early to take my son to school.", filename: "i_always_wake_up_early_son.mp3", voice: "ellen" },
  { text: "Rafael works out twice a week. He trains jiu-jitsu.", filename: "rafael_works_out_twice.mp3", voice: "arthur" },
  { text: "I pick up my son from school at 5 p.m.", filename: "i_pick_up_my_son_5pm.mp3", voice: "ellen" },
  { text: "I always wake up at 6 a.m.", filename: "i_always_wake_up_at_6am.mp3", voice: "arthur" },
  { text: "Rafael usually takes his son to school before work.", filename: "rafael_usually_takes_son.mp3", voice: "arthur" },
  { text: "He often trains jiu-jitsu in the morning.", filename: "he_often_trains_jiujitsu.mp3", voice: "arthur" },
  { text: "I sometimes work late when there is an important case.", filename: "i_sometimes_work_late.mp3", voice: "ellen" },
  { text: "She rarely works overtime.", filename: "she_rarely_works_overtime.mp3", voice: "arthur" },
  { text: "I never work on weekends.", filename: "i_never_work_on_weekends.mp3", voice: "ellen" },
  { text: "My commute to the office takes about thirty minutes.", filename: "my_commute_takes_thirty_min.mp3", voice: "arthur" },
  { text: "I have a busy schedule with many deadlines.", filename: "i_have_a_busy_schedule.mp3", voice: "ellen" },
  { text: "I always wake up early and take my son to school.", filename: "i_always_wake_up_early_take_son.mp3", voice: "arthur" },
  { text: "I usually attend meetings in the morning.", filename: "i_usually_attend_meetings.mp3", voice: "ellen" },
  { text: "I rarely work overtime, but I sometimes work late.", filename: "i_rarely_work_overtime_sometimes.mp3", voice: "arthur" },
  { text: "I never work on weekends because I value family time.", filename: "i_never_work_weekends_family.mp3", voice: "ellen" },
  { text: "I rarely work overtime.", filename: "i_rarely_work_overtime.mp3", voice: "arthur" },
  { text: "I wake up at 6 a.m. and get ready.", filename: "i_wake_up_6am_get_ready.mp3", voice: "ellen" },
  { text: "I take my son to school.", filename: "i_take_my_son_to_school.mp3", voice: "arthur" },
  { text: "I train jiu-jitsu at the gym.", filename: "i_train_jiujitsu_at_gym.mp3", voice: "ellen" },
  { text: "I have lunch before going to the office.", filename: "i_have_lunch_before_office.mp3", voice: "arthur" },
  { text: "I attend meetings and work until the evening.", filename: "i_attend_meetings_work_evening.mp3", voice: "ellen" },
  { text: "Hey Rafael, how is your morning going?", filename: "mark_hey_rafael_morning.mp3", voice: "arthur" },
  { text: "Good, thanks. I always wake up at 6 and take my son to school first.", filename: "rafael_good_thanks_wake_up.mp3", voice: "arthur" },
  { text: "That is early. What do you do after that?", filename: "mark_that_is_early.mp3", voice: "arthur" },
  { text: "I usually train jiu-jitsu. I work out twice a week.", filename: "rafael_usually_train_jiujitsu.mp3", voice: "arthur" },
  { text: "Jiu-jitsu? That is impressive. What time do you get to the office?", filename: "mark_jiujitsu_impressive.mp3", voice: "arthur" },
  { text: "I usually get here around 9. My commute takes about thirty minutes.", filename: "rafael_usually_get_here_9.mp3", voice: "arthur" },
  { text: "Do you have a busy schedule today?", filename: "mark_busy_schedule_today.mp3", voice: "arthur" },
  { text: "Yes, I have meetings all morning. I rarely have a free hour before lunch.", filename: "rafael_meetings_all_morning.mp3", voice: "arthur" },
  { text: "I know the feeling. Do you ever work overtime?", filename: "mark_do_you_work_overtime.mp3", voice: "arthur" },
  { text: "I sometimes work late, but I never work on weekends. Family time is important.", filename: "rafael_sometimes_late_never_weekends.mp3", voice: "arthur" },
  { text: "I always wake up early.", filename: "i_always_wake_up_early.mp3", voice: "arthur" },
  { text: "He usually has lunch at 12.", filename: "he_usually_has_lunch_12.mp3", voice: "ellen" },
  { text: "He is never late for meetings.", filename: "he_is_never_late_meetings.mp3", voice: "arthur" },
  { text: "I always attend meetings in the morning.", filename: "i_always_attend_meetings.mp3", voice: "ellen" },
  { text: "Always I wake up at 6 a.m.", filename: "always_i_wake_up_error.mp3", voice: "arthur" },
  { text: "He never is late for meetings.", filename: "he_never_is_late_error.mp3", voice: "ellen" },
  { text: "I work overtime rarely.", filename: "i_work_overtime_rarely_error.mp3", voice: "arthur" },
  { text: "Rafael always wakes up at 6 a.m.", filename: "rafael_always_wakes_up_6am.mp3", voice: "arthur" },
  { text: "He usually takes his son to school.", filename: "he_usually_takes_son_school.mp3", voice: "arthur" },
  { text: "He sometimes trains jiu-jitsu in the evening.", filename: "he_sometimes_trains_evening.mp3", voice: "ellen" },
  { text: "He never works on weekends.", filename: "he_never_works_weekends.mp3", voice: "arthur" },
  { text: "I usually take my son to school before work.", filename: "i_usually_take_son_before_work.mp3", voice: "ellen" },
  { text: "I often train jiu-jitsu in the morning.", filename: "i_often_train_jiujitsu_morning.mp3", voice: "arthur" },

  // ============================================================
  // LESSON 4 — First Contact
  // ============================================================
  { text: "I manage the legal department and serve on the board of directors.", filename: "rafael_i_manage_legal_board.mp3", voice: "arthur" },
  { text: "Colleague", filename: "colleague.mp3", voice: "arthur" },
  { text: "To introduce", filename: "to_introduce.mp3", voice: "arthur" },
  { text: "Pleased to meet you", filename: "pleased_to_meet_you.mp3", voice: "ellen" },
  { text: "Business card", filename: "business_card.mp3", voice: "arthur" },
  { text: "To shake hands", filename: "to_shake_hands.mp3", voice: "arthur" },
  { text: "Available", filename: "available.mp3", voice: "arthur" },
  { text: "To arrange", filename: "to_arrange.mp3", voice: "arthur" },
  { text: "Contact information", filename: "contact_information.mp3", voice: "arthur" },
  { text: "Nice to meet you. I have heard great things about your work.", filename: "nice_to_meet_you_great_things.mp3", voice: "ellen" },
  { text: "I am looking forward to working with you.", filename: "looking_forward_working_correct.mp3", voice: "arthur" },
  { text: "Let us get in touch next week to discuss the project.", filename: "let_us_get_in_touch_next_week.mp3", voice: "ellen" },
  { text: "I have a meeting with my colleague from the legal team.", filename: "i_have_a_meeting_with_colleague.mp3", voice: "arthur" },
  { text: "Let me introduce you to our CEO.", filename: "let_me_introduce_you_to_ceo.mp3", voice: "ellen" },
  { text: "Pleased to meet you. I am Rafael.", filename: "pleased_to_meet_you_i_am_rafael.mp3", voice: "arthur" },
  { text: "Here is my business card.", filename: "here_is_my_business_card.mp3", voice: "ellen" },
  { text: "In business, we always shake hands.", filename: "in_business_we_always_shake.mp3", voice: "arthur" },
  { text: "Are you available for a meeting tomorrow?", filename: "are_you_available_for_meeting.mp3", voice: "ellen" },
  { text: "Can we arrange a meeting for next week?", filename: "can_we_arrange_meeting_survival.mp3", voice: "arthur" },
  { text: "Could you send me your contact information?", filename: "could_you_send_contact_info.mp3", voice: "ellen" },
  { text: "Can I ask what company you are with?", filename: "can_i_ask_what_company.mp3", voice: "arthur" },
  { text: "Could you tell me more about your company?", filename: "could_you_tell_more_survival.mp3", voice: "ellen" },
  { text: "I can speak English, but I want to improve.", filename: "i_can_speak_english_but.mp3", voice: "arthur" },
  { text: "Could I give you my business card?", filename: "could_i_give_card_survival.mp3", voice: "ellen" },
  { text: "Pleased to meet you. I am Rafael Gasparelli Lima.", filename: "pleased_to_meet_you_rafael.mp3", voice: "arthur" },
  { text: "Pleased to meet you. I work at Grupo Picunha.", filename: "pleased_to_meet_you_grupo.mp3", voice: "ellen" },
  { text: "Can we arrange a meeting to discuss a partnership?", filename: "can_we_arrange_meeting_partnership.mp3", voice: "arthur" },
  { text: "Can I help you with something?", filename: "can_i_help_you_with_something.mp3", voice: "ellen" },
  { text: "I can speak English.", filename: "i_can_speak_english.mp3", voice: "arthur" },
  { text: "Could we arrange a meeting?", filename: "could_we_arrange_a_meeting.mp3", voice: "ellen" },
  { text: "Could you to tell me your name?", filename: "could_you_to_tell_error.mp3", voice: "arthur" },
  { text: "Could you tell me your name?", filename: "could_you_tell_me_your_name.mp3", voice: "ellen" },
  { text: "Can you sending me an email?", filename: "can_you_sending_error.mp3", voice: "arthur" },
  { text: "Can you send me an email?", filename: "can_you_send_me_an_email.mp3", voice: "ellen" },
  { text: "I am look forward to work with you.", filename: "i_am_look_forward_error.mp3", voice: "arthur" },
  { text: "Good morning. I don't think we have met. I am Karen Williams, from Williams and Associates in New York.", filename: "karen_good_morning_intro.mp3", voice: "ellen" },
  { text: "Good morning, Karen. Pleased to meet you. I am Rafael Gasparelli Lima, from Grupo Picunha in São Paulo.", filename: "rafael_good_morning_karen.mp3", voice: "arthur" },
  { text: "Nice to meet you, Rafael. Could you tell me about your company?", filename: "karen_nice_to_meet_you.mp3", voice: "ellen" },
  { text: "Of course. We operate in iron manufacturing and agriculture. Could I give you my business card?", filename: "rafael_of_course_we_operate.mp3", voice: "arthur" },
  { text: "Thank you. Can I ask what your role is?", filename: "karen_thank_you_can_i_ask.mp3", voice: "ellen" },
  { text: "That is interesting. Are you available for a meeting next week?", filename: "karen_that_is_interesting.mp3", voice: "ellen" },
  { text: "Yes, I am. Can we arrange it for Tuesday morning?", filename: "rafael_yes_i_am_arrange.mp3", voice: "arthur" },
  { text: "Could you send me an email with your contact information?", filename: "could_you_send_email_survival.mp3", voice: "arthur" },
  { text: "Of course. I am looking forward to working with you.", filename: "rafael_of_course_looking_fwd.mp3", voice: "arthur" },
  { text: "Likewise. It was a pleasure meeting you, Rafael.", filename: "karen_likewise_pleasure.mp3", voice: "ellen" },
  { text: "The pleasure is mine. Let us get in touch soon.", filename: "rafael_pleasure_is_mine.mp3", voice: "arthur" },

  // ============================================================
  // LESSON 5 — The Office
  // ============================================================
  { text: "Office", filename: "office.mp3", voice: "arthur" },
  { text: "Conference room", filename: "conference_room.mp3", voice: "arthur" },
  { text: "Floor", filename: "floor.mp3", voice: "arthur" },
  { text: "Printer", filename: "printer.mp3", voice: "arthur" },
  { text: "Reception", filename: "reception.mp3", voice: "arthur" },
  { text: "Parking lot", filename: "parking_lot.mp3", voice: "arthur" },
  { text: "Elevator", filename: "elevator.mp3", voice: "arthur" },
  { text: "Cafeteria", filename: "cafeteria.mp3", voice: "arthur" },
  { text: "The legal department is on the fifth floor.", filename: "the_legal_dept_is_on_fifth.mp3", voice: "arthur" },
  { text: "My office is next to the conference room.", filename: "my_office_is_next_to_conf_room.mp3", voice: "ellen" },
  { text: "The reception desk is in front of the elevator.", filename: "the_reception_desk_in_front.mp3", voice: "arthur" },
  { text: "There is a conference room on every floor.", filename: "there_is_a_conf_room_every_floor.mp3", voice: "ellen" },
  { text: "There are three meeting rooms on my floor.", filename: "there_are_three_meeting_rooms.mp3", voice: "arthur" },
  { text: "Is there a cafeteria in the building?", filename: "tom_is_there_cafeteria.mp3", voice: "arthur" },
  { text: "There aren't any international offices yet.", filename: "there_arent_any_intl_offices.mp3", voice: "arthur" },
  { text: "My office is on the fifth floor.", filename: "my_office_is_on_fifth_floor.mp3", voice: "ellen" },
  { text: "The printer is next to my desk.", filename: "the_printer_is_next_to_desk.mp3", voice: "arthur" },
  { text: "The parking lot is behind the building.", filename: "the_parking_lot_is_behind.mp3", voice: "ellen" },
  { text: "The reception is in front of the elevator.", filename: "the_reception_in_front_elevator.mp3", voice: "arthur" },
  { text: "My office is on the fifth floor, next to the elevator.", filename: "my_office_fifth_floor_elevator.mp3", voice: "ellen" },
  { text: "There are over five hundred employees in this building.", filename: "there_are_500_employees_building.mp3", voice: "arthur" },
  { text: "Is there a cafeteria on this floor?", filename: "is_there_a_cafeteria_this_floor.mp3", voice: "ellen" },
  { text: "There is a conference room next to my office.", filename: "there_is_conf_room_next_office.mp3", voice: "arthur" },
  { text: "There are three meeting rooms on this floor.", filename: "there_are_three_rooms_this_floor.mp3", voice: "ellen" },
  { text: "The cafeteria is on the first floor.", filename: "the_cafeteria_on_first_floor.mp3", voice: "arthur" },
  { text: "Is there a parking lot? Yes, it is behind the building.", filename: "is_there_parking_lot_behind.mp3", voice: "ellen" },
  { text: "There is a modern building with ten floors.", filename: "there_is_modern_building_ten.mp3", voice: "arthur" },
  { text: "There are over five hundred employees working there every day.", filename: "there_are_500_employees_every_day.mp3", voice: "ellen" },
  { text: "Welcome to Grupo Picunha, Tom. Let me give you a tour of the building.", filename: "rafael_welcome_tom_tour.mp3", voice: "arthur" },
  { text: "Thank you, Rafael. This is a beautiful building. How many floors are there?", filename: "tom_thank_you_beautiful.mp3", voice: "arthur" },
  { text: "There are ten floors. This is the reception on the ground floor.", filename: "rafael_ten_floors_reception.mp3", voice: "arthur" },
  { text: "Yes, there is. The cafeteria is on the first floor, next to the lobby.", filename: "rafael_yes_cafeteria_first.mp3", voice: "arthur" },
  { text: "Great. Where is your office?", filename: "tom_where_is_your_office.mp3", voice: "arthur" },
  { text: "My office is on the fifth floor. The elevator is right here, next to the stairs.", filename: "rafael_office_fifth_elevator.mp3", voice: "arthur" },
  { text: "Are there many people on your floor?", filename: "tom_are_there_many_people.mp3", voice: "arthur" },
  { text: "Yes, there are about fifty employees on the fifth floor. There is a conference room next to my office and a printer in front of the elevator.", filename: "rafael_fifty_employees_conf.mp3", voice: "arthur" },
  { text: "Is there a parking lot?", filename: "tom_is_there_parking_lot.mp3", voice: "arthur" },
  { text: "Yes, there is a large parking lot behind the building.", filename: "rafael_yes_parking_lot_behind.mp3", voice: "arthur" },
  { text: "This is a great office. Thank you for the tour, Rafael.", filename: "tom_great_office_thank_you.mp3", voice: "arthur" },
  { text: "It has a conference room on this floor.", filename: "it_has_conf_room_error.mp3", voice: "ellen" },
  { text: "There is many employees in the building.", filename: "there_is_many_employees_error.mp3", voice: "arthur" },
  { text: "The cafeteria is in the first floor.", filename: "cafeteria_in_first_floor_error.mp3", voice: "ellen" },
  { text: "There are many employees in the building.", filename: "there_are_many_employees.mp3", voice: "arthur" },
  { text: "There is a conference room on this floor.", filename: "there_is_conf_room_this_floor.mp3", voice: "ellen" }
];

// ===== API CALL =====
async function generateAudio(text, filename, voiceName) {
  const filePath = path.join(OUTPUT_DIR, filename);

  // Skip if already exists (incremental generation)
  if (fs.existsSync(filePath)) {
    console.log(`  [skip] ${filename} already exists`);
    return filePath;
  }

  const voiceId = VOICES[voiceName] || VOICES.arthur;

  const response = await fetch(`${API_URL}/${voiceId}`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'xi-api-key': API_KEY,
      'Accept': 'audio/mpeg'
    },
    body: JSON.stringify({
      text: text,
      model_id: 'eleven_monolingual_v1',
      voice_settings: {
        stability: 0.5,
        similarity_boost: 0.75
      }
    })
  });

  if (!response.ok) {
    const err = await response.text();
    console.error(`  [ERROR] ${filename}: ${response.status} ${err}`);
    return null;
  }

  const buffer = Buffer.from(await response.arrayBuffer());
  fs.writeFileSync(filePath, buffer);
  console.log(`  Generated: ${filename} (${voiceName === 'ellen' ? 'Ellen' : 'Arthur'})`);
  return filePath;
}

// ===== MAIN =====
async function main() {
  console.log('='.repeat(60));
  console.log('  ElevenLabs Audio Generator — Rafael Gasparelli Lima');
  console.log('='.repeat(60));
  console.log(`  Total entries: ${audioEntries.length}`);
  console.log(`  Output: ${OUTPUT_DIR}`);
  console.log(`  Voices: Arthur (sfJopaWaOtauCD3HKX6Q) + Ellen (BIvP0GN1cAtSRTxNHnWS)`);
  console.log('='.repeat(60));
  console.log('');

  const audioMapResult = {};
  let success = 0;
  let skipped = 0;
  let failed = 0;

  for (let i = 0; i < audioEntries.length; i++) {
    const entry = audioEntries[i];
    const displayText = entry.text.length > 60 ? entry.text.substring(0, 57) + '...' : entry.text;

    console.log(`[${i + 1}/${audioEntries.length}] "${displayText}"`);

    const result = await generateAudio(entry.text, entry.filename, entry.voice);

    if (result) {
      audioMapResult[entry.text] = `/audio/rafael-gasparelli-lima/${entry.filename}`;

      // Also add lowercase variant for single/short entries
      const lower = entry.text.toLowerCase();
      if (lower !== entry.text) {
        audioMapResult[lower] = `/audio/rafael-gasparelli-lima/${entry.filename}`;
      }

      if (fs.existsSync(path.join(OUTPUT_DIR, entry.filename))) {
        const stat = fs.statSync(path.join(OUTPUT_DIR, entry.filename));
        if (stat.size > 0) {
          success++;
        }
      }
    } else {
      failed++;
    }

    // Rate limiting: 500ms between API calls
    if (i < audioEntries.length - 1) {
      await new Promise(r => setTimeout(r, 500));
    }
  }

  // Save audioMap.json
  const mapPath = path.join(OUTPUT_DIR, 'audioMap.json');
  fs.writeFileSync(mapPath, JSON.stringify(audioMapResult, null, 2));

  console.log('');
  console.log('='.repeat(60));
  console.log(`  DONE!`);
  console.log(`  Generated: ${success} | Skipped (existing): ${skipped} | Failed: ${failed}`);
  console.log(`  Audio map: ${mapPath}`);
  console.log('='.repeat(60));
}

main().catch(err => {
  console.error('Fatal error:', err);
  process.exit(1);
});
