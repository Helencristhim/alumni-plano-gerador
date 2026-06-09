const fs = require('fs');
const path = require('path');
const https = require('https');

const ELEVENLABS_API_KEY = process.env.ELEVENLABS_API_KEY;
if (!ELEVENLABS_API_KEY) {
  console.error('ERROR: ELEVENLABS_API_KEY not set');
  process.exit(1);
}

// New voices (Riley/Ash) — Arthur/Ellen discontinued
const RILEY = 'hA4zGnmTwX2NQiTRMt7o';  // Female neutral
const ASH = 'VU16byTywsWv5JpI8rbc';      // Male neutral

const OUTPUT_DIR = path.join(__dirname, '..', 'public', 'audio', 'helen-mendes-teste');

const audioMap = {
  // Vocabulary words (student=female → Riley for single words)
  "Agenda": "agenda.mp3",
  "Minutes": "minutes.mp3",
  "Action items": "action_items.mp3",
  "Follow up": "follow_up.mp3",
  "Chair": "chair.mp3",
  "Stakeholder": "stakeholder.mp3",
  "Deadline": "deadline.mp3",
  "Adjourn": "adjourn.mp3",

  // Example sentences
  "Let's review the agenda before we start.": "lets_review_the_agenda_before_we_start.mp3",
  "Who is taking the minutes today?": "who_is_taking_the_minutes_today.mp3",
  "We need to assign action items before we adjourn.": "we_need_to_assign_action_items_before_we_adjourn.mp3",
  "I will follow up with the marketing team next week.": "i_will_follow_up_with_the_marketing_team_next_week.mp3",
  "Helen will chair today's meeting.": "helen_will_chair_todays_meeting.mp3",
  "All stakeholders should attend the quarterly review.": "all_stakeholders_should_attend_the_quarterly_review.mp3",
  "The deadline for the proposal is next Friday.": "the_deadline_for_the_proposal_is_next_friday.mp3",
  "Let's adjourn the meeting. Thank you, everyone.": "lets_adjourn_the_meeting_thank_you_everyone.mp3",

  // Grammar/modal sentences
  "Could we move to the next item?": "could_we_move_to_the_next_item.mp3",
  "Would you mind sharing your screen?": "would_you_mind_sharing_your_screen.mp3",
  "Shall we table this for the next meeting?": "shall_we_table_this_for_the_next_meeting.mp3",
  "We should review the budget before Friday.": "we_should_review_the_budget_before_friday.mp3",

  // Fill-in-the-blank phrases
  "Shall we move to the next item on the agenda?": "shall_we_move_to_the_next_item_on_the_agenda.mp3",
  "I would like to add a point about the deadline.": "i_would_like_to_add_a_point_about_the_deadline.mp3",
  "Could you send the minutes by end of day?": "could_you_send_the_minutes_by_end_of_day.mp3",
  "We should discuss the budget before we adjourn.": "we_should_discuss_the_budget_before_we_adjourn.mp3",

  // Speech card phrases
  "Could we go through the agenda quickly?": "could_we_go_through_the_agenda_quickly.mp3",
  "I'd like to raise a point about the deadline.": "id_like_to_raise_a_point_about_the_deadline.mp3",
  "Let's assign the action items before we wrap up.": "lets_assign_the_action_items_before_we_wrap_up.mp3",

  // Survival phrases
  "Could we go back to the previous point?": "could_we_go_back_to_the_previous_point.mp3",
  "I'd like to add something here.": "id_like_to_add_something_here.mp3",
  "Let's move on to the next item.": "lets_move_on_to_the_next_item.mp3",
  "Could you send the minutes after the meeting?": "could_you_send_the_minutes_after_the_meeting.mp3",
  "Shall we schedule a follow-up?": "shall_we_schedule_a_followup.mp3",

  // Dialogue — David lines (male → Ash)
  "Good morning, Helen. Shall we start?": "good_morning_helen_shall_we_start.mp3",
  "The first item is the project deadline.": "the_first_item_is_the_project_deadline.mp3",
  "We are on track, but we should discuss the budget.": "we_are_on_track_but_we_should_discuss_the_budget.mp3",
  "Of course. The total is within our forecast.": "of_course_the_total_is_within_our_forecast.mp3",

  // Dialogue — Helen lines (female → Riley)
  "Yes, let's review the agenda first.": "yes_lets_review_the_agenda_first.mp3",
  "Right. Could you give us an update on the timeline?": "right_could_you_give_us_an_update_on_the_timeline.mp3",
  "I agree. Would you mind sharing the numbers?": "i_agree_would_you_mind_sharing_the_numbers.mp3",
  "Great. Let's assign the action items and adjourn.": "great_lets_assign_the_action_items_and_adjourn.mp3",

  // Ordering exercise combined audio
  "[order-l1]": "order_l1_ordering.mp3"
};

// David's lines → Ash (male)
const davidLines = [
  "Good morning, Helen. Shall we start?",
  "The first item is the project deadline.",
  "We are on track, but we should discuss the budget.",
  "Of course. The total is within our forecast."
];

// Helen's dialogue lines → Riley (student is female)
const helenDialogueLines = [
  "Yes, let's review the agenda first.",
  "Right. Could you give us an update on the timeline?",
  "I agree. Would you mind sharing the numbers?",
  "Great. Let's assign the action items and adjourn."
];

let phraseAlternator = 0;

function getVoice(text) {
  if (davidLines.includes(text)) return { id: ASH, name: 'Ash' };
  if (helenDialogueLines.includes(text)) return { id: RILEY, name: 'Riley' };

  // Single words (1-2) → Riley (student gender = female)
  const words = text.replace(/\[.*\]/, '').trim().split(/ +/).length;
  if (words <= 2) return { id: RILEY, name: 'Riley' };

  // Phrases → alternate Riley/Ash
  const voice = phraseAlternator % 2 === 0
    ? { id: RILEY, name: 'Riley' }
    : { id: ASH, name: 'Ash' };
  phraseAlternator++;
  return voice;
}

function generateAudio(text, voiceId, outputPath) {
  return new Promise((resolve, reject) => {
    const ttsText = text.replace(/\[.*\]/, '').trim();

    // For ordering combined audio, use a full meeting sequence
    const finalText = text === '[order-l1]'
      ? "Good morning, everyone. Let's start. The first item on the agenda is the project update. Could you give us the latest numbers? I'd like to add a point about the deadline. Let's assign the action items. Thank you, everyone. Meeting adjourned."
      : ttsText;

    const postData = JSON.stringify({
      text: finalText,
      model_id: 'eleven_monolingual_v1',
      voice_settings: {
        stability: 0.5,
        similarity_boost: 0.75
      }
    });

    const options = {
      hostname: 'api.elevenlabs.io',
      path: `/v1/text-to-speech/${voiceId}?output_format=mp3_44100_128`,
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
        res.on('end', () => reject(new Error(`API ${res.statusCode}: ${body}`)));
        return;
      }
      const chunks = [];
      res.on('data', (chunk) => chunks.push(chunk));
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

async function main() {
  if (!fs.existsSync(OUTPUT_DIR)) {
    fs.mkdirSync(OUTPUT_DIR, { recursive: true });
  }

  const entries = Object.entries(audioMap);
  console.log(`\nGenerating ${entries.length} audio files for helen-mendes-teste...\n`);

  let generated = 0;
  let skipped = 0;

  for (const [text, filename] of entries) {
    const outputPath = path.join(OUTPUT_DIR, filename);

    if (fs.existsSync(outputPath)) {
      console.log(`  SKIP: ${filename} (already exists)`);
      skipped++;
      continue;
    }

    const voice = getVoice(text);
    console.log(`  [${voice.name}] ${text.substring(0, 60)}...`);

    try {
      const size = await generateAudio(text, voice.id, outputPath);
      console.log(`    → ${filename} (${(size / 1024).toFixed(1)} KB)`);
      generated++;
      // Rate limit: wait 500ms between requests
      await new Promise(r => setTimeout(r, 500));
    } catch (err) {
      console.error(`    ERROR: ${err.message}`);
    }
  }

  console.log(`\nDone! Generated: ${generated}, Skipped: ${skipped}, Total: ${entries.length}`);
}

main();
