const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const DIR = path.join(__dirname, '..', 'public', 'audio', 'maria-claudia-curimbaba');

// Voice rules:
// - Single words (1-2 words) = Ellen (female student)
// - Maria Claudia protagonist exercises = Ellen
// - Male character lines (David) = Arthur
// - General phrases = ALTERNATE Arthur/Ellen

const PHRASES = [
  // ===== Vocab words (1-2 words → Ellen, female student) =====
  { text: "Agenda", file: "aula3_agenda.mp3", voice: ELLEN },
  { text: "Minutes", file: "aula3_minutes.mp3", voice: ELLEN },
  { text: "Action item", file: "aula3_action_item.mp3", voice: ELLEN },
  { text: "Deadline", file: "aula3_deadline.mp3", voice: ELLEN },
  { text: "Adjourn", file: "aula3_adjourn.mp3", voice: ELLEN },
  { text: "Facilitate", file: "aula3_facilitate.mp3", voice: ELLEN },
  { text: "Follow up", file: "aula3_follow_up.mp3", voice: ELLEN },
  { text: "Wrap up", file: "aula3_wrap_up.mp3", voice: ELLEN },

  // ===== Vocab example sentences (alternate Arthur/Ellen) =====
  { text: "We need to review the agenda before the meeting starts.", file: "aula3_we_need_to_review_the_agenda.mp3", voice: ARTHUR },
  { text: "Please send the minutes to all participants by end of day.", file: "aula3_please_send_the_minutes.mp3", voice: ELLEN },
  { text: "Each action item must have a clear owner and deadline.", file: "aula3_each_action_item_must_have.mp3", voice: ARTHUR },
  { text: "The deadline for the procurement report is next Friday.", file: "aula3_the_deadline_for_the_procurement.mp3", voice: ELLEN },
  { text: "If there are no more questions, let's adjourn.", file: "aula3_if_there_are_no_more_questions.mp3", voice: ARTHUR },
  { text: "Maria Claudia will facilitate the quarterly review today.", file: "aula3_maria_claudia_will_facilitate.mp3", voice: ELLEN },
  { text: "I will follow up on the pending items next Monday.", file: "aula3_i_will_follow_up_on_the_pending.mp3", voice: ARTHUR },
  { text: "Let's wrap up this discussion and move to the next topic.", file: "aula3_lets_wrap_up_this_discussion.mp3", voice: ELLEN },

  // ===== Key expressions (alternate) =====
  { text: "Let's move on to...", file: "aula3_expr_lets_move_on_to.mp3", voice: ARTHUR },
  { text: "Let's move on to the procurement report and review the new deadlines.", file: "aula3_expr_lets_move_on_example.mp3", voice: ELLEN },
  { text: "Let's wrap up...", file: "aula3_expr_lets_wrap_up.mp3", voice: ARTHUR },
  { text: "Let's wrap up the budget discussion and assign action items to each team.", file: "aula3_expr_lets_wrap_up_example.mp3", voice: ELLEN },
  { text: "Please make sure to...", file: "aula3_expr_please_make_sure_to.mp3", voice: ARTHUR },
  { text: "Please make sure to send the updated numbers to Houston before Thursday.", file: "aula3_expr_please_make_sure_example.mp3", voice: ELLEN },

  // ===== Grammar context passage (narrative = Ellen) =====
  { text: "Maria Claudia is facilitating a quarterly review meeting with her team and counterparts from Houston. She opens the meeting by reviewing the agenda. Let's begin with the revenue update. Please look at the numbers on your screen. Let's move on to the procurement report. Take note of the new deadlines. Each action item must have an owner. Please send the minutes by end of day. Let's adjourn and follow up next week.", file: "aula3_grammar_context_passage.mp3", voice: ELLEN },

  // ===== Fill-in-the-blank sentences (alternate) =====
  { text: "Let's begin with the first item on the agenda.", file: "aula3_fill_lets_begin_with.mp3", voice: ARTHUR },
  { text: "Please send the minutes by end of day.", file: "aula3_fill_please_send_the_minutes.mp3", voice: ELLEN },
  { text: "Let's wrap up this discussion and move to the next topic.", file: "aula3_fill_lets_wrap_up.mp3", voice: ARTHUR },
  { text: "Take note of the action items.", file: "aula3_fill_take_note_of.mp3", voice: ELLEN },
  { text: "The deadline for the procurement report is next Friday.", file: "aula3_fill_the_deadline_for.mp3", voice: ARTHUR },
  { text: "Maria Claudia will facilitate the meeting today.", file: "aula3_fill_mc_will_facilitate.mp3", voice: ELLEN },
  { text: "Let's follow up on the pending items next Monday.", file: "aula3_fill_lets_follow_up.mp3", voice: ARTHUR },
  { text: "If there are no more questions, let's adjourn.", file: "aula3_fill_lets_adjourn.mp3", voice: ELLEN },

  // ===== Ordering audio (combined meeting sequence) =====
  { text: "Good morning, everyone. Let's get started. First, let's review the agenda for today. Let's begin with the revenue update from Q3. Please take note of the new procurement deadlines. Let's assign action items before we finish. Please send the minutes by end of day. Meeting adjourned.", file: "aula3_order_meeting_sequence.mp3", voice: ELLEN },

  // ===== Survival card phrases (Maria Claudia = Ellen) =====
  { text: "Let's begin with the first item on the agenda.", file: "aula3_surv_lets_begin.mp3", voice: ELLEN },
  { text: "Could we move on to the next topic?", file: "aula3_surv_could_we_move_on.mp3", voice: ELLEN },
  { text: "Please send the minutes by end of day.", file: "aula3_surv_please_send_minutes.mp3", voice: ELLEN },
  { text: "Let's assign action items before we adjourn.", file: "aula3_surv_lets_assign_action_items.mp3", voice: ELLEN },
  { text: "I will follow up on this by Friday.", file: "aula3_surv_i_will_follow_up.mp3", voice: ELLEN },

  // ===== Speech practice cards (Maria Claudia = Ellen) =====
  { text: "Let's begin with the first item on the agenda.", file: "aula3_speech_lets_begin.mp3", voice: ELLEN },
  { text: "Please send the minutes to all participants by end of day.", file: "aula3_speech_please_send_minutes.mp3", voice: ELLEN },
  { text: "Let's move on to the next topic on the agenda.", file: "aula3_speech_lets_move_on.mp3", voice: ELLEN },
  { text: "Take note of the action items and their deadlines.", file: "aula3_speech_take_note.mp3", voice: ELLEN },
  { text: "Let's adjourn. I will follow up on Friday.", file: "aula3_speech_lets_adjourn.mp3", voice: ELLEN },

  // ===== IN CLASS — Listening 1 (Maria Claudia opening quarterly review = Ellen) =====
  { text: "Good morning, everyone. Thank you for joining. Let's begin. First, let me go over the agenda. We have three items today: the Q3 revenue update, the procurement timeline for the Texas subsidiary, and action items from last month's meeting. Let's start with revenue. David, please share the Pittsburgh numbers. After that, we will move on to procurement. Please take note of any deadlines. Let's make sure every action item has an owner by the end of this meeting.", file: "aula3_ic_listening1_quarterly_review.mp3", voice: ELLEN },

  // ===== IN CLASS — Listening 2 (David reporting = Arthur) =====
  { text: "Thanks, Maria Claudia. Let me give you a quick update on Pittsburgh. Revenue is up eight percent compared to last quarter. The manufacturing division met all deadlines. However, we need to follow up on the logistics contract. The deadline is next Friday. I suggest we assign this as an action item. Also, please send me the updated procurement numbers from Sao Paulo. Let's wrap up this topic and move on to the next item.", file: "aula3_ic_listening2_david_report.mp3", voice: ARTHUR },

  // ===== IN CLASS — Dialogue lines =====
  { text: "Good morning, David. Let's get started. Did you review the agenda I sent yesterday?", file: "aula3_ic_dlg_mc_1.mp3", voice: ELLEN },
  { text: "Good morning, Maria Claudia. Yes, I did. Three items today, right? Revenue, procurement, and action items.", file: "aula3_ic_dlg_david_1.mp3", voice: ARTHUR },
  { text: "Exactly. Let's begin with revenue. Please share the Pittsburgh numbers.", file: "aula3_ic_dlg_mc_2.mp3", voice: ELLEN },
  { text: "Sure. Revenue is up eight percent. But we need to follow up on the logistics contract.", file: "aula3_ic_dlg_david_2.mp3", voice: ARTHUR },
  { text: "Good. Let's assign that as an action item. David, please make sure to send the updated report by Friday.", file: "aula3_ic_dlg_mc_3.mp3", voice: ELLEN },
  { text: "Will do. Should we move on to procurement?", file: "aula3_ic_dlg_david_3.mp3", voice: ARTHUR },
  { text: "Yes. Let's move on to the procurement timeline. Take note of the new deadlines.", file: "aula3_ic_dlg_mc_4.mp3", voice: ELLEN },
  { text: "Got it. If there are no other items, should we wrap up?", file: "aula3_ic_dlg_david_4.mp3", voice: ARTHUR },
  { text: "Let's review the action items first. David, logistics report by Friday. Sarah, procurement update by Wednesday. If there are no more questions, let's adjourn.", file: "aula3_ic_dlg_mc_5.mp3", voice: ELLEN },
  { text: "Sounds good. I will follow up with Sarah on the procurement numbers. Great meeting, Maria Claudia.", file: "aula3_ic_dlg_david_5.mp3", voice: ARTHUR },

  // ===== IN CLASS — Error correction sentences =====
  { text: "Let's to review the agenda.", file: "aula3_ic_error_lets_to_review.mp3", voice: ARTHUR },
  { text: "Please to send the minutes.", file: "aula3_ic_error_please_to_send.mp3", voice: ELLEN },
  { text: "She suggest we adjourn.", file: "aula3_ic_error_she_suggest.mp3", voice: ARTHUR },
  { text: "Let's not to skip any items.", file: "aula3_ic_error_lets_not_to.mp3", voice: ELLEN },
  { text: "Do not to forget the deadline.", file: "aula3_ic_error_do_not_to.mp3", voice: ARTHUR },
];

async function gen(text, voiceId, outPath) {
  const r = await fetch('https://api.elevenlabs.io/v1/text-to-speech/' + voiceId, {
    method: 'POST',
    headers: { 'xi-api-key': API_KEY, 'Content-Type': 'application/json' },
    body: JSON.stringify({
      text,
      model_id: 'eleven_multilingual_v2',
      voice_settings: { stability: 0.5, similarity_boost: 0.75 }
    }),
  });
  if (!r.ok) throw new Error(r.status + ': ' + (await r.text()));
  const buf = Buffer.from(await r.arrayBuffer());
  fs.writeFileSync(outPath, buf);
  return buf.length;
}

async function main() {
  if (!API_KEY) { console.error('Set ELEVENLABS_API_KEY env var'); process.exit(1); }
  if (!fs.existsSync(DIR)) fs.mkdirSync(DIR, { recursive: true });

  const seen = new Set();
  const unique = PHRASES.filter(p => {
    const k = p.file.toLowerCase();
    if (seen.has(k)) return false;
    seen.add(k);
    return true;
  });

  console.log('Generating ' + unique.length + ' AULA 3 audio files for Maria Claudia Curimbaba...');
  let generated = 0;
  let skipped = 0;

  for (const p of unique) {
    const outPath = path.join(DIR, p.file);
    if (fs.existsSync(outPath)) {
      console.log('SKIP: ' + p.file);
      skipped++;
    } else {
      try {
        const bytes = await gen(p.text, p.voice, outPath);
        console.log('OK [' + (p.voice === ELLEN ? 'ellen' : 'arthur') + ']: ' + p.file + ' (' + (bytes / 1024).toFixed(1) + 'KB)');
        generated++;
        await new Promise(r => setTimeout(r, 500));
      } catch (e) {
        console.error('FAIL: ' + p.file + ' — ' + e.message);
      }
    }
  }

  console.log('\nDone! Generated: ' + generated + ' | Skipped: ' + skipped + ' | Total: ' + unique.length);
}

main();
