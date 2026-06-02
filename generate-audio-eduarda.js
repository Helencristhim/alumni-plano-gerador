const fs = require('fs');
const path = require('path');
const https = require('https');

const ELEVENLABS_API_KEY = process.env.ELEVENLABS_API_KEY;
if (!ELEVENLABS_API_KEY) { console.error('ERROR: ELEVENLABS_API_KEY not set'); process.exit(1); }

const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const OUTPUT_DIR = path.join(__dirname, 'public', 'audio', 'eduarda-gabriel');

const audioMap = {
  "Could you repeat that, please?": "could_you_repeat_that_please.mp3",
  "I am not sure I understand. Could you explain?": "i_am_not_sure_i_understand_could_you_explain.mp3",
  "Let me think about that for a moment.": "let_me_think_about_that_for_a_moment.mp3",
  "In my experience, I would say...": "in_my_experience_i_would_say.mp3",
  "Could I add something to that?": "could_i_add_something_to_that.mp3",
  "Restructuring": "restructuring.mp3",
  "Deal": "deal.mp3",
  "Counterpart": "counterpart.mp3",
  "Advise": "advise.mp3",
  "Currently": "currently.mp3",
  "Contribute": "contribute.mp3",
  "Stakeholder": "stakeholder.mp3",
  "Walk Through": "walk_through.mp3",
  "Houlihan Lokey is one of the leading firms in restructuring.": "houlihan_lokey_is_one_of_the_leading_firms_in_restructuring.mp3",
  "Eduarda is working on a new deal in Sao Paulo.": "eduarda_is_working_on_a_new_deal_in_sao_paulo.mp3",
  "My counterpart in New York coordinates the creditor meetings.": "my_counterpart_in_new_york_coordinates_the_creditor_meetings.mp3",
  "We advise clients on Chapter 11 restructuring.": "we_advise_clients_on_chapter_11_restructuring.mp3",
  "I am currently focused on a major restructuring case.": "i_am_currently_focused_on_a_major_restructuring_case.mp3",
  "I want to contribute more actively in English calls.": "i_want_to_contribute_more_actively_in_english_calls.mp3",
  "The stakeholders approved the restructuring plan last week.": "the_stakeholders_approved_the_restructuring_plan_last_week.mp3",
  "Let me walk you through the deal structure.": "let_me_walk_you_through_the_deal_structure.mp3",
  "Eduarda works at Houlihan Lokey as an associate.": "eduarda_works_at_houlihan_lokey_as_an_associate.mp3",
  "She is currently working on a restructuring deal.": "she_is_currently_working_on_a_restructuring_deal.mp3",
  "Her counterpart coordinates the creditor meetings every week.": "her_counterpart_coordinates_the_creditor_meetings_every_week.mp3",
  "The team advises clients on complex financial transactions.": "the_team_advises_clients_on_complex_financial_transactions.mp3",
  "She wants to contribute to the discussion in English.": "she_wants_to_contribute_to_the_discussion_in_english.mp3",
  "The stakeholders are reviewing the new proposal today.": "the_stakeholders_are_reviewing_the_new_proposal_today.mp3",
  "I am an investment banking associate at Houlihan Lokey in Sao Paulo.": "i_am_an_investment_banking_associate_at_houlihan_lokey.mp3",
  "I am currently working on restructuring deals and Chapter 11 processes.": "i_am_currently_working_on_restructuring_deals_and_chapter_11.mp3",
  "My role involves advising clients and coordinating with counterparts.": "my_role_involves_advising_clients_and_coordinating.mp3",
  "Good morning. I am James from the New York office. Are you joining the restructuring call today?": "good_morning_i_am_james_from_the_new_york_office.mp3",
  "Yes, hi James. I am Eduarda from the Sao Paulo team.": "yes_hi_james_i_am_eduarda_from_the_sao_paulo_team.mp3",
  "Great to have you. What is your role on this deal?": "great_to_have_you_what_is_your_role_on_this_deal.mp3",
  "I am an associate. I am currently responsible for the financial analysis.": "i_am_an_associate_i_am_currently_responsible.mp3",
  "Excellent. Could you walk us through the latest numbers?": "excellent_could_you_walk_us_through_the_latest_numbers.mp3",
  "Of course. Let me share my screen. The restructuring plan shows three main scenarios.": "of_course_let_me_share_my_screen_the_restructuring_plan.mp3",
  "This is very helpful. Who are the main stakeholders on the Brazilian side?": "this_is_very_helpful_who_are_the_main_stakeholders.mp3",
  "The main stakeholders are the creditors and the company board. I advise them on the deal structure.": "the_main_stakeholders_are_the_creditors_and_the_company.mp3",
  "I am Eduarda Gabriel. I work at Houlihan Lokey.": "i_am_eduarda_gabriel_i_work_at_houlihan_lokey.mp3",
  "I am currently working on a restructuring deal.": "i_am_currently_working_on_a_restructuring_deal.mp3",
  "Could you walk me through the deal structure?": "could_you_walk_me_through_the_deal_structure.mp3",
  "I would like to contribute to this discussion.": "i_would_like_to_contribute_to_this_discussion.mp3",
  "The main stakeholders have approved the plan.": "the_main_stakeholders_have_approved_the_plan.mp3",
  "[order-l1]": "order_l1_self_introduction.mp3",
  "Good morning. I am Eduarda Gabriel, an associate at Houlihan Lokey in Sao Paulo.": "good_morning_i_am_eduarda_gabriel_an_associate.mp3",
  "I advise clients on restructuring and coordinate with our New York counterparts.": "i_advise_clients_on_restructuring_and_coordinate.mp3",
  "I am currently working on a Chapter 11 restructuring case.": "i_am_currently_working_on_a_chapter_11_case.mp3",
  "The main stakeholders are the creditors, the board, and the advisory team.": "the_main_stakeholders_are_the_creditors_the_board.mp3",
  "Could you walk me through the deal structure, please?": "could_you_walk_me_through_the_deal_structure_please.mp3",
  "I would like to contribute to this discussion. May I add something?": "i_would_like_to_contribute_may_i_add_something.mp3"
};

// James dialogue lines (male) -> Arthur
const jamesLines = [
  "Good morning. I am James from the New York office. Are you joining the restructuring call today?",
  "Great to have you. What is your role on this deal?",
  "Excellent. Could you walk us through the latest numbers?",
  "This is very helpful. Who are the main stakeholders on the Brazilian side?"
];

// Eduarda dialogue lines (female) -> Ellen
const eduardaDialogueLines = [
  "Yes, hi James. I am Eduarda from the Sao Paulo team.",
  "I am an associate. I am currently responsible for the financial analysis.",
  "Of course. Let me share my screen. The restructuring plan shows three main scenarios.",
  "The main stakeholders are the creditors and the company board. I advise them on the deal structure."
];

function countWords(text) {
  return text.replace(/\s*\(v2\)\s*$/, '').trim().split(/\s+/).length;
}

let phraseAlternator = 0;

function getVoice(text) {
  if (jamesLines.includes(text)) return { id: ARTHUR, name: 'Arthur' };
  if (eduardaDialogueLines.includes(text)) return { id: ELLEN, name: 'Ellen' };
  const words = countWords(text);
  if (words <= 2) return { id: ARTHUR, name: 'Arthur' };
  const voice = phraseAlternator % 2 === 0 ? { id: ARTHUR, name: 'Arthur' } : { id: ELLEN, name: 'Ellen' };
  phraseAlternator++;
  return voice;
}

function generateAudio(text, voiceId, outputPath) {
  return new Promise((resolve, reject) => {
    const ttsText = text.replace(/\s*\(v2\)\s*$/, '').trim();
    const postData = JSON.stringify({
      text: ttsText,
      model_id: 'eleven_monolingual_v1',
      voice_settings: { stability: 0.5, similarity_boost: 0.75 }
    });
    const options = {
      hostname: 'api.elevenlabs.io',
      path: '/v1/text-to-speech/' + voiceId + '?output_format=mp3_44100_128',
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'xi-api-key': ELEVENLABS_API_KEY,
        'Content-Length': Buffer.byteLength(postData)
      }
    };
    const req = https.request(options, (res) => {
      if (res.statusCode !== 200) {
        let body = '';
        res.on('data', (d) => body += d);
        res.on('end', () => reject(new Error('API ' + res.statusCode + ': ' + body)));
        return;
      }
      const chunks = [];
      res.on('data', (chunk) => chunks.push(chunk));
      res.on('end', () => {
        fs.writeFileSync(outputPath, Buffer.concat(chunks));
        resolve();
      });
    });
    req.on('error', reject);
    req.write(postData);
    req.end();
  });
}

function delay(ms) { return new Promise(resolve => setTimeout(resolve, ms)); }

async function main() {
  const entries = Object.entries(audioMap);
  const total = entries.length;
  let generated = 0, skipped = 0;
  console.log('Starting audio generation: ' + total + ' files');
  console.log('Output: ' + OUTPUT_DIR + '\n');
  for (let i = 0; i < entries.length; i++) {
    const [text, filename] = entries[i];
    const outputPath = path.join(OUTPUT_DIR, filename);
    if (fs.existsSync(outputPath)) {
      const stats = fs.statSync(outputPath);
      if (stats.size > 1000) {
        skipped++;
        const words = countWords(text);
        if (words > 2 && !jamesLines.includes(text) && !eduardaDialogueLines.includes(text)) phraseAlternator++;
        continue;
      }
    }
    const voice = getVoice(text);
    try {
      await generateAudio(text, voice.id, outputPath);
      generated++;
      console.log('Generated ' + (generated + skipped) + '/' + total + ': ' + filename + ' (' + voice.name + ')');
    } catch (err) {
      console.error('FAILED ' + filename + ': ' + err.message);
    }
    if (i < entries.length - 1) await delay(500);
  }
  console.log('\nDone! Generated: ' + generated + ', Skipped: ' + skipped);
}

main().catch(console.error);
