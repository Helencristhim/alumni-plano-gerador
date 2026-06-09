const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const DIR = path.join(__dirname, '..', 'public', 'audio', 'carlos-vinicius-vale-bassan');

// Carlos = male = ARTHUR for ALL his lines and single words
// James = male = ARTHUR for his dialogue lines
// Lisa Park = female = ELLEN for her dialogue lines
// General/alternating phrases: alternate ARTHUR/ELLEN

const PHRASES = [
  // === VOCAB WORDS (Arthur — male student) ===
  { text: "Contribute", voice: ARTHUR, prefix: "aula5" },
  { text: "Interrupt", voice: ARTHUR, prefix: "aula5" },
  { text: "Propose", voice: ARTHUR, prefix: "aula5" },
  { text: "Address", voice: ARTHUR, prefix: "aula5" },
  { text: "Elaborate", voice: ARTHUR, prefix: "aula5" },
  { text: "Defer", voice: ARTHUR, prefix: "aula5" },
  { text: "Consensus", voice: ARTHUR, prefix: "aula5" },
  { text: "Wrap up", voice: ARTHUR, prefix: "aula5" },

  // === PRE-CLASS VOCAB EXPRESSIONS (alternating Arthur/Ellen) ===
  { text: "If I may jump in here...", voice: ARTHUR, prefix: "aula5" },
  { text: "I would like to add something to that point.", voice: ELLEN, prefix: "aula5" },
  { text: "Could we circle back to...?", voice: ARTHUR, prefix: "aula5" },

  // === PRE-CLASS FILL-IN PHRASES (Arthur — male student practicing) ===
  { text: "I would like to contribute an idea on the integration timeline.", voice: ARTHUR, filename: "aula5_contribute_idea_integration_timeline" },
  { text: "If I may, I would like to propose a different approach.", voice: ARTHUR, filename: "aula5_propose_different_approach" },
  { text: "Could we address the budget issue before moving on?", voice: ELLEN, filename: "aula5_address_budget_issue" },
  { text: "I think we should defer this decision until we have more data.", voice: ARTHUR, filename: "aula5_defer_decision_more_data" },
  { text: "Let me wrap up the main takeaways from this discussion.", voice: ELLEN, filename: "aula5_wrap_up_main_takeaways" },

  // === IN CLASS VOCAB EXAMPLES (alternating Arthur/Ellen) ===
  { text: "Let me elaborate on that point for a moment.", voice: ARTHUR, filename: "aula5_elaborate_on_that_point" },
  { text: "Can we reach a consensus on the next steps?", voice: ELLEN, filename: "aula5_reach_consensus_next_steps" },
  { text: "We need to wrap up soon, so let me summarize the action items.", voice: ARTHUR, filename: "aula5_wrap_up_summarize_action_items" },

  // === SPEECH CARDS (Arthur — male student) ===
  { text: "If I may jump in here, I think we are missing a key risk factor.", voice: ARTHUR, filename: "aula5_jump_in_missing_risk_factor" },
  { text: "I would like to add something to that point. The regulatory timeline is also a concern.", voice: ARTHUR, filename: "aula5_add_something_regulatory_timeline" },
  { text: "Could we circle back to the staffing question? I think it is connected to the budget issue.", voice: ARTHUR, filename: "aula5_circle_back_staffing_question" },
  { text: "I would like to propose that we revisit the integration plan.", voice: ARTHUR, filename: "aula5_propose_revisit_integration" },
  { text: "Can we try to reach a consensus before we leave?", voice: ARTHUR, filename: "aula5_reach_consensus_before_leave" },

  // === SURVIVAL CARD PHRASES (Arthur — male student) ===
  { text: "If I may, I would like to add something to that point.", voice: ARTHUR, filename: "aula5_if_i_may_add_something" },
  { text: "Could we address the timeline before we move on?", voice: ARTHUR, filename: "aula5_address_timeline_before_move_on" },
  { text: "Let me elaborate on why I think the deadline is unrealistic.", voice: ARTHUR, filename: "aula5_elaborate_deadline_unrealistic" },
  { text: "I think we should defer this to the next steering committee meeting.", voice: ARTHUR, filename: "aula5_defer_steering_committee" },

  // === DIALOGUE — James = ARTHUR (male colleague / meeting lead) ===
  { text: "Carlos, thanks for joining the integration planning call. So, Lisa and I have been going through the post-merger roadmap, and honestly, we are behind on several workstreams. The IT systems migration was supposed to be done by Q3, but the legacy platform is more complex than we anticipated. Lisa, do you want to jump in on the operations side?", voice: ARTHUR, filename: "aula5_dialogue_james_1" },
  { text: "That is a great point. Go ahead and elaborate.", voice: ARTHUR, filename: "aula5_dialogue_james_2" },
  { text: "I like that idea. Lisa, what do you think? Can we reach a consensus on this approach?", voice: ARTHUR, filename: "aula5_dialogue_james_3" },
  { text: "Fair enough. Carlos, can you contribute the strategy team's perspective on timing?", voice: ARTHUR, filename: "aula5_dialogue_james_4" },
  { text: "Perfect. That is a solid wrap up. Let us move forward with that plan.", voice: ARTHUR, filename: "aula5_dialogue_james_5" },

  // === DIALOGUE — Lisa Park = ELLEN (female colleague) ===
  { text: "Sure. Thanks, James. So on operations, we have identified three critical gaps in the supply chain. The biggest one is the warehouse management system. The two companies use completely different platforms, and we cannot run them in parallel for more than six months without significant cost overruns.", voice: ELLEN, filename: "aula5_dialogue_lisa_1" },
  { text: "I agree in principle, but I think we should defer the final decision until we have the cost analysis from finance. Could we circle back to this next week?", voice: ELLEN, filename: "aula5_dialogue_lisa_2" },

  // === DIALOGUE — Carlos = ARTHUR (male student) ===
  { text: "If I may jump in here, I think the IT and operations issues are connected. Could we address both together?", voice: ARTHUR, filename: "aula5_dialogue_carlos_1" },
  { text: "I would like to propose that we create a joint task force. If we align the IT migration with the warehouse consolidation, we could save both time and budget.", voice: ARTHUR, filename: "aula5_dialogue_carlos_2" },
  { text: "Of course. From our side, the window is narrow. I would like to add that the board expects a progress report by end of month. Let me wrap up what we have so far: joint task force proposal, pending cost analysis, and a follow-up meeting next week.", voice: ARTHUR, filename: "aula5_dialogue_carlos_3" },

  // === ORAL DRILLING — Situations (Ellen — narrator) ===
  { text: "The meeting is going off track. You want to refocus the discussion.", voice: ELLEN, filename: "aula5_oral_1_situation" },
  { text: "A colleague is dominating the conversation. You want to contribute your perspective.", voice: ELLEN, filename: "aula5_oral_2_situation" },
  { text: "The team is debating two options and cannot decide. You want to propose a compromise.", voice: ELLEN, filename: "aula5_oral_3_situation" },
  { text: "Your manager asks for your opinion on the integration timeline. You think it needs more time.", voice: ELLEN, filename: "aula5_oral_4_situation" },
  { text: "The discussion is running long and you need to close the meeting.", voice: ELLEN, filename: "aula5_oral_5_situation" },
  { text: "Someone raises a complex topic that requires more research. You want to postpone the decision.", voice: ELLEN, filename: "aula5_oral_6_situation" },

  // === ORAL DRILLING — Model answers (Arthur — male student) ===
  { text: "Could we circle back to the main agenda item? I think we need to address the budget first.", voice: ARTHUR, filename: "aula5_oral_1_model" },
  { text: "If I may jump in here, I would like to add a point from the strategy team's perspective.", voice: ARTHUR, filename: "aula5_oral_2_model" },
  { text: "I would like to propose a middle ground. What if we start with option A for Q3 and transition to option B in Q4?", voice: ARTHUR, filename: "aula5_oral_3_model" },
  { text: "If I may, I would like to elaborate on the timeline. Based on our analysis, we need at least two additional months for the tech migration.", voice: ARTHUR, filename: "aula5_oral_4_model" },
  { text: "We need to wrap up. Let me quickly go through the action items and make sure we have consensus on next steps.", voice: ARTHUR, filename: "aula5_oral_5_model" },
  { text: "That is a valid concern. I think we should defer this decision until the finance team has completed their analysis. Can we revisit this next week?", voice: ARTHUR, filename: "aula5_oral_6_model" },

  // === LISTENING 1 — Team meeting (Arthur — James leading the meeting) ===
  { text: "Alright team, let us get started. As you know, we are three months into the post-merger integration and we need to address some critical gaps. The IT migration is behind schedule. The original plan had us completing the systems cutover by September, but the legacy platform has more dependencies than we mapped. We also have a staffing issue. Two key project managers resigned last month, and we have not found replacements. On the positive side, the client retention numbers look strong. Ninety-two percent of the combined client base has confirmed they will stay. But we cannot be complacent. I need each workstream lead to contribute an updated timeline by Friday. And one more thing, the board wants a progress report by end of month, so we need to reach consensus on priorities today.", voice: ARTHUR, filename: "aula5_listening_1_team_meeting" },
  { text: "Alright team, let us get started. As you know, we are three months into the post-merger integration and we need to address some critical gaps. The IT migration is behind schedule. The original plan had us completing the systems cutover by September, but the legacy platform has more dependencies than we mapped. We also have a staffing issue. Two key project managers resigned last month, and we have not found replacements. On the positive side, the client retention numbers look strong. Ninety-two percent of the combined client base has confirmed they will stay. But we cannot be complacent. I need each workstream lead to contribute an updated timeline by Friday. And one more thing, the board wants a progress report by end of month, so we need to reach consensus on priorities today.", voice: ARTHUR, filename: "aula5_listening_1_full" },

  // === LISTENING 2 — Manager feedback (Ellen — manager giving feedback to Carlos) ===
  { text: "Carlos, good work in that meeting today. I noticed a few things I want to share. First, you did a great job when you jumped in to connect the IT and operations issues. That showed real strategic thinking. But I think you could have been more assertive when Lisa pushed back on the timeline. Instead of deferring immediately, you could have elaborated on why the window is narrow. Next time, propose a specific compromise rather than just agreeing to defer. Also, your wrap up at the end was solid. The board will appreciate that kind of structured summary. For next week's meeting, I want you to lead the first thirty minutes. Prepare talking points for each workstream and be ready to address pushback on the timeline.", voice: ELLEN, filename: "aula5_listening_2_manager_feedback" },
  { text: "Carlos, good work in that meeting today. I noticed a few things I want to share. First, you did a great job when you jumped in to connect the IT and operations issues. That showed real strategic thinking. But I think you could have been more assertive when Lisa pushed back on the timeline. Instead of deferring immediately, you could have elaborated on why the window is narrow. Next time, propose a specific compromise rather than just agreeing to defer. Also, your wrap up at the end was solid. The board will appreciate that kind of structured summary. For next week's meeting, I want you to lead the first thirty minutes. Prepare talking points for each workstream and be ready to address pushback on the timeline.", voice: ELLEN, filename: "aula5_listening_2_full" },

  // === ORDERING ===
  { text: "If I may jump in here, I think we need to address this issue. I would like to propose a different approach. Could we circle back to the main topic? Let me elaborate on that. I think we should defer this decision. Can we reach consensus before we leave?", voice: ARTHUR, filename: "aula5_order_l5" },
  { text: "If I may jump in here, I think we need to address this issue. I would like to propose a different approach. Could we circle back to the main topic? Let me elaborate on that. I think we should defer this decision. Can we reach consensus before we leave?", voice: ARTHUR, filename: "aula5_order_full" },
];

function toFilename(text, prefix) {
  const base = text.toLowerCase().replace(/[^a-z0-9 ]/g, '').replace(/ +/g, '_').substring(0, 50);
  return prefix ? prefix + '_' + base : base;
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
  if (!API_KEY) { console.error('Set ELEVENLABS_API_KEY'); process.exit(1); }
  if (!fs.existsSync(DIR)) fs.mkdirSync(DIR, { recursive: true });

  const seen = new Set();
  const unique = PHRASES.filter(p => {
    // Use filename as key if present (allows same text with different filenames)
    const k = p.filename ? p.filename : p.text.toLowerCase();
    if (seen.has(k)) return false;
    seen.add(k);
    return true;
  });

  console.log('Generating ' + unique.length + ' audio files for Aula 5...');
  let ok = 0, skip = 0, fail = 0;
  const audioMapEntries = {};

  for (const p of unique) {
    const fname = (p.filename || toFilename(p.text, p.prefix)) + '.mp3';
    const outPath = path.join(DIR, fname);
    if (fs.existsSync(outPath)) {
      console.log('SKIP: ' + fname);
      skip++;
    } else {
      try {
        const bytes = await gen(p.text, p.voice, outPath);
        console.log('OK [' + (p.voice === ELLEN ? 'ellen' : 'arthur') + ']: ' + fname + ' (' + (bytes/1024).toFixed(1) + 'KB)');
        ok++;
        await new Promise(r => setTimeout(r, 400));
      } catch(e) {
        console.error('FAIL: ' + fname + ' — ' + e.message);
        fail++;
      }
    }
    audioMapEntries[p.text] = '/audio/carlos-vinicius-vale-bassan/' + fname;
  }

  // Add listening + order keys (bracket notation used by JS player)
  audioMapEntries['[aula5-listening-1]'] = '/audio/carlos-vinicius-vale-bassan/aula5_listening_1_team_meeting.mp3';
  audioMapEntries['[aula5-listening-2]'] = '/audio/carlos-vinicius-vale-bassan/aula5_listening_2_manager_feedback.mp3';
  audioMapEntries['[order-l5]'] = '/audio/carlos-vinicius-vale-bassan/aula5_order_l5.mp3';

  // Full listening/order files used by data-src in players
  audioMapEntries['_listening_1_full'] = '/audio/carlos-vinicius-vale-bassan/aula5_listening_1_full.mp3';
  audioMapEntries['_listening_2_full'] = '/audio/carlos-vinicius-vale-bassan/aula5_listening_2_full.mp3';
  audioMapEntries['_order_full'] = '/audio/carlos-vinicius-vale-bassan/aula5_order_full.mp3';

  fs.writeFileSync(path.join(DIR, 'aula5_audioMap.json'), JSON.stringify(audioMapEntries, null, 2));
  console.log('\nDone! OK: ' + ok + ' | Skip: ' + skip + ' | Fail: ' + fail);
}

main().catch(e => { console.error(e); process.exit(1); });
