const https = require('https');
const fs = require('fs');
const path = require('path');

const ASH = 'VU16byTywsWv5JpI8rbc';
const RILEY = 'hA4zGnmTwX2NQiTRMt7o';
const API_KEY = process.env.ELEVENLABS_API_KEY;
const OUTPUT_DIR = path.join(__dirname, 'public', 'audio', 'natalie-viegas');

const entries = [
  // ===== VOCAB WORDS (Riley - Natalie is female) =====
  { file: 'aula5_agenda.mp3', text: 'Agenda', voice: RILEY },
  { file: 'aula5_chair.mp3', text: 'Chair', voice: RILEY },
  { file: 'aula5_minutes.mp3', text: 'Minutes', voice: RILEY },
  { file: 'aula5_action_item.mp3', text: 'Action item', voice: RILEY },
  { file: 'aula5_adjourn.mp3', text: 'Adjourn', voice: RILEY },
  { file: 'aula5_facilitate.mp3', text: 'Facilitate', voice: RILEY },
  { file: 'aula5_consensus.mp3', text: 'Consensus', voice: RILEY },
  { file: 'aula5_follow_up.mp3', text: 'Follow-up', voice: RILEY },
  { file: 'aula5_objective.mp3', text: 'Objective', voice: RILEY },
  { file: 'aula5_recap.mp3', text: 'Recap', voice: RILEY },

  // ===== VOCAB EXAMPLE SENTENCES (alternate Riley/Ash) =====
  { file: 'aula5_let_me_share_the_agenda.mp3', text: 'Let me share the agenda before we begin.', voice: RILEY },
  { file: 'aula5_i_will_chair_the_quarterly.mp3', text: 'I will chair the quarterly review next Monday.', voice: ASH },
  { file: 'aula5_could_you_send_the_minutes.mp3', text: 'Could you send the minutes to the team after the meeting?', voice: RILEY },
  { file: 'aula5_we_have_three_action_items.mp3', text: 'We have three action items from today\'s meeting.', voice: ASH },
  { file: 'aula5_we_should_adjourn.mp3', text: 'If there are no other questions, we should adjourn.', voice: RILEY },
  { file: 'aula5_she_facilitates_sessions.mp3', text: 'She facilitates our weekly strategy sessions.', voice: ASH },
  { file: 'aula5_reach_a_consensus.mp3', text: 'We should reach a consensus before making a decision.', voice: RILEY },
  { file: 'aula5_send_a_follow_up.mp3', text: 'I will send a follow-up email with the key decisions.', voice: ASH },
  { file: 'aula5_objective_of_meeting.mp3', text: 'The objective of this meeting is to review our Q3 targets.', voice: RILEY },
  { file: 'aula5_recap_main_points.mp3', text: 'Let me recap the main points before we close.', voice: ASH },

  // ===== FILL-IN-THE-BLANK SENTENCES =====
  { file: 'aula5_fill_should_review.mp3', text: 'We should review the agenda before starting the meeting.', voice: RILEY },
  { file: 'aula5_fill_could_send.mp3', text: 'Could you send the minutes to the team by Friday?', voice: ASH },
  { file: 'aula5_fill_would_like_recap.mp3', text: 'I would like to recap the main action items.', voice: RILEY },
  { file: 'aula5_fill_should_facilitate.mp3', text: 'She should facilitate the next quarterly review.', voice: ASH },
  { file: 'aula5_fill_could_adjourn.mp3', text: 'We could adjourn the meeting if there are no more questions.', voice: RILEY },
  { file: 'aula5_fill_would_mind.mp3', text: 'Would you mind chairing the meeting on Monday?', voice: ASH },

  // ===== SPEECH CARDS (Riley - student voice) =====
  { file: 'aula5_speech_review_agenda.mp3', text: 'We should review the agenda before we start. Could you share the screen?', voice: RILEY },
  { file: 'aula5_speech_recap_action.mp3', text: 'I would like to recap the action items from today\'s meeting.', voice: RILEY },
  { file: 'aula5_speech_send_minutes.mp3', text: 'Would you mind sending the minutes? We should follow up by Friday.', voice: RILEY },

  // ===== ORDERING =====
  { file: 'order_l5_ordering.mp3', text: 'Share the agenda at the beginning. State the objective of the meeting. Discuss each item on the agenda. Recap action items and assign tasks. Adjourn the meeting.', voice: RILEY },

  // ===== SURVIVAL CARD (Pre-class) =====
  { file: 'aula5_surv_share_agenda.mp3', text: 'Let me share the agenda for today\'s meeting.', voice: RILEY },
  { file: 'aula5_surv_move_next.mp3', text: 'We should move to the next item.', voice: ASH },
  { file: 'aula5_surv_clarify.mp3', text: 'Could you clarify that point?', voice: RILEY },
  { file: 'aula5_surv_recap.mp3', text: 'I would like to recap the action items.', voice: ASH },
  { file: 'aula5_surv_adjourn.mp3', text: 'If there are no other questions, let us adjourn.', voice: RILEY },

  // ===== IN CLASS DIALOGUE (David=Ash, Natalie=Riley) =====
  { file: 'aula5_dlg_david_1.mp3', text: 'Good morning, Natalie. Are you chairing the meeting today?', voice: ASH },
  { file: 'aula5_dlg_natalie_1.mp3', text: 'Yes, I am. Let me share the agenda. We have three objectives today.', voice: RILEY },
  { file: 'aula5_dlg_david_2.mp3', text: 'Should we start with the budget review?', voice: ASH },
  { file: 'aula5_dlg_natalie_2.mp3', text: 'Good idea. We should discuss that first. Could you share the latest numbers?', voice: RILEY },
  { file: 'aula5_dlg_david_3.mp3', text: 'Of course. Would you like me to also present the Q3 forecast?', voice: ASH },
  { file: 'aula5_dlg_natalie_3.mp3', text: 'That would be great. After that, I would like to review our action items from last week.', voice: RILEY },
  { file: 'aula5_dlg_david_4.mp3', text: 'We should also follow up on the Ministry of Justice proposal.', voice: ASH },
  { file: 'aula5_dlg_natalie_4.mp3', text: 'Agreed. Let me recap: budget review, Q3 forecast, action items, and the Ministry proposal. If we cover everything, we could adjourn by eleven.', voice: RILEY },

  // ===== IN CLASS ORAL DRILLING =====
  { file: 'aula5_oral_share_agenda.mp3', text: 'Let me share the agenda for today\'s meeting.', voice: RILEY },
  { file: 'aula5_oral_should_review.mp3', text: 'We should review the Q3 targets first.', voice: RILEY },
  { file: 'aula5_oral_could_share.mp3', text: 'Could you share the latest numbers?', voice: RILEY },
  { file: 'aula5_oral_would_like.mp3', text: 'I would like to review the action items.', voice: RILEY },
  { file: 'aula5_oral_should_follow.mp3', text: 'We should follow up on the Ministry proposal.', voice: RILEY },
  { file: 'aula5_oral_recap_adjourn.mp3', text: 'Let me recap before we adjourn.', voice: RILEY },

  // ===== IN CLASS ORAL DRILLING 2 =====
  { file: 'aula5_oral2_chair_facilitate.mp3', text: 'I will chair the meeting and facilitate the discussion on budget.', voice: RILEY },
  { file: 'aula5_oral2_consensus_action.mp3', text: 'We should reach a consensus and define clear action items.', voice: RILEY },
  { file: 'aula5_oral2_minutes_followup.mp3', text: 'Could you send the minutes? I will send a follow-up email.', voice: RILEY },
  { file: 'aula5_oral2_objective_recap.mp3', text: 'The objective was to review Q3 targets. Let me recap the key points.', voice: RILEY },

  // ===== IN CLASS LISTENING PASSAGES =====
  { file: 'aula5_listening_1_team_meeting.mp3', text: 'Good morning, everyone. Thank you for joining today\'s meeting. I am Natalie Viegas, and I will be chairing this session. Let me share the agenda. We have four objectives today. First, we should review the Q3 budget. Second, we need to discuss the Ministry of Justice project update. Third, I would like to go over the action items from our last meeting. And finally, we could discuss the timeline for the new proposal. David, could you start with the budget numbers? After that, I would like everyone to share their updates. We should try to reach a consensus on the priorities for next quarter. If we stay on track, we could adjourn by eleven thirty.', voice: RILEY },
  { file: 'aula5_listening_2_wrap_up.mp3', text: 'Before we close, let me recap the key points from today\'s meeting. First, we reached a consensus on the Q3 budget allocation. David will send the updated numbers by Friday. Second, the Ministry project is on track. Natalie should follow up with the procurement team next week. Third, we agreed on three action items. David will prepare the Q3 forecast. Natalie will facilitate a stakeholder meeting next Wednesday. And Carlos will review the compliance documents. I will send the minutes to everyone by end of day. The next meeting is scheduled for Monday at nine. If there are no other questions, we should adjourn. Thank you all for a productive session.', voice: ASH },

  // ===== IN CLASS ERROR SENTENCES =====
  { file: 'aula5_ic_error_should_to.mp3', text: 'We should to review the agenda.', voice: RILEY },
  { file: 'aula5_ic_error_could_sharing.mp3', text: 'Could you sharing the screen?', voice: RILEY },
  { file: 'aula5_ic_error_would_likes.mp3', text: 'She would likes to recap.', voice: RILEY },
  { file: 'aula5_ic_error_should_facilitates.mp3', text: 'I should facilitates the meeting.', voice: RILEY },
];

function generateAudio(entry) {
  return new Promise((resolve, reject) => {
    const data = JSON.stringify({
      text: entry.text,
      model_id: 'eleven_multilingual_v2',
      voice_settings: { stability: 0.5, similarity_boost: 0.75 }
    });
    const options = {
      hostname: 'api.elevenlabs.io',
      path: `/v1/text-to-speech/${entry.voice}`,
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'xi-api-key': API_KEY, 'Content-Length': Buffer.byteLength(data) }
    };
    const outPath = path.join(OUTPUT_DIR, entry.file);
    if (fs.existsSync(outPath)) { console.log(`SKIP (exists): ${entry.file}`); return resolve(); }
    const req = https.request(options, (res) => {
      if (res.statusCode !== 200) { let body=''; res.on('data',d=>body+=d); res.on('end',()=>{console.error(`ERROR ${res.statusCode} for ${entry.file}: ${body}`);resolve();}); return; }
      const ws = fs.createWriteStream(outPath); res.pipe(ws);
      ws.on('finish', () => { console.log(`OK: ${entry.file}`); resolve(); });
      ws.on('error', reject);
    });
    req.on('error', reject); req.write(data); req.end();
  });
}

async function main() {
  if (!API_KEY) { console.error('ERROR: ELEVENLABS_API_KEY not set.'); process.exit(1); }
  if (!fs.existsSync(OUTPUT_DIR)) fs.mkdirSync(OUTPUT_DIR, { recursive: true });
  console.log(`Generating ${entries.length} audio files for Natalie Viegas (Aula 5)...\n`);
  for (let i = 0; i < entries.length; i++) {
    console.log(`[${i+1}/${entries.length}] ${entries[i].file}`);
    await generateAudio(entries[i]);
    await new Promise(r => setTimeout(r, 200));
  }
  console.log('\nDone!');
}
main().catch(console.error);
