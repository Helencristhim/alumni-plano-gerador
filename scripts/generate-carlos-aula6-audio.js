const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const DIR = path.join(__dirname, '..', 'public', 'audio', 'carlos-vinicius-vale-bassan');

// Carlos = male = ARTHUR for ALL his lines and single words
// Elena = female = ELLEN for her dialogue lines
// Michael = male = ARTHUR for his dialogue lines
// General/alternating phrases: alternate ARTHUR/ELLEN

const PHRASES = [
  // === VOCAB WORDS (Arthur — male student) ===
  { text: "Agree", voice: ARTHUR, prefix: "aula6" },
  { text: "Disagree", voice: ARTHUR, prefix: "aula6" },
  { text: "Persuade", voice: ARTHUR, prefix: "aula6" },
  { text: "Compromise", voice: ARTHUR, prefix: "aula6" },
  { text: "Justify", voice: ARTHUR, prefix: "aula6" },
  { text: "Acknowledge", voice: ARTHUR, prefix: "aula6" },
  { text: "Challenge", voice: ARTHUR, prefix: "aula6" },
  { text: "Concede", voice: ARTHUR, prefix: "aula6" },

  // === PRE-CLASS VOCAB EXPRESSIONS (alternating Arthur/Ellen) ===
  { text: "I see your point, but...", voice: ARTHUR, filename: "aula6_i_see_your_point_but" },
  { text: "That is a valid concern, however...", voice: ELLEN, filename: "aula6_that_is_a_valid_concern_however" },
  { text: "Would it be fair to say that...?", voice: ARTHUR, filename: "aula6_would_it_be_fair_to_say" },

  // === PRE-CLASS FILL-IN PHRASES (alternating Arthur/Ellen) ===
  { text: "We need to agree on a unified approach before the board meeting.", voice: ARTHUR, filename: "aula6_agree_unified_approach" },
  { text: "I have to disagree with that assessment based on our Q3 data.", voice: ELLEN, filename: "aula6_disagree_assessment_q3" },
  { text: "She managed to persuade the entire committee to support the merger.", voice: ARTHUR, filename: "aula6_persuade_committee_merger" },
  { text: "Both sides will need to compromise on the timeline to close this deal.", voice: ELLEN, filename: "aula6_compromise_timeline_deal" },
  { text: "Can you justify the additional investment with concrete numbers?", voice: ARTHUR, filename: "aula6_justify_additional_investment" },
  { text: "I acknowledge that the risks are significant, but the opportunity outweighs them.", voice: ELLEN, filename: "aula6_acknowledge_risks_opportunity" },
  { text: "I would like to challenge that assumption. Do we have enough evidence?", voice: ARTHUR, filename: "aula6_challenge_assumption_evidence" },
  { text: "I concede that the timeline is tight, but I still believe the strategy is sound.", voice: ELLEN, filename: "aula6_concede_timeline_strategy" },

  // === IN CLASS VOCAB EXAMPLES (alternating Arthur/Ellen) ===
  { text: "I am not entirely convinced that an aggressive acquisition is the right move.", voice: ARTHUR, filename: "aula6_not_entirely_convinced" },
  { text: "I tend to think that organic growth gives us more control over risk.", voice: ELLEN, filename: "aula6_tend_to_think_organic" },
  { text: "With respect, I would argue that the market window is closing.", voice: ARTHUR, filename: "aula6_with_respect_market_window" },

  // === IN CLASS GRAMMAR PRACTICE / CONTEXT (alternating Arthur/Ellen) ===
  { text: "I see your point about the acquisition cost, but I would argue that the long-term ROI justifies it.", voice: ARTHUR, filename: "aula6_see_point_acquisition_roi" },
  { text: "That is a valid concern about integration risk, however, our due diligence shows manageable exposure.", voice: ELLEN, filename: "aula6_valid_concern_integration" },
  { text: "Would it be fair to say that both strategies have merit, and the question is really about timing?", voice: ARTHUR, filename: "aula6_fair_to_say_both_merit" },

  // === SPEECH CARDS (Arthur — male student) ===
  { text: "I see your point, but I would argue we need more time to evaluate the risks.", voice: ARTHUR, filename: "aula6_fill_see_your_point" },
  { text: "I acknowledge that the data supports your position, but I am not entirely convinced.", voice: ARTHUR, filename: "aula6_fill_acknowledge_data" },
  { text: "With respect, I would argue that we should consider alternative strategies.", voice: ARTHUR, filename: "aula6_fill_with_respect" },
  { text: "I tend to think that a compromise would benefit both sides.", voice: ARTHUR, filename: "aula6_fill_tend_to_think" },
  { text: "Can you justify that recommendation with concrete evidence?", voice: ARTHUR, filename: "aula6_fill_justify_recommendation" },

  // === FILL-IN-THE-BLANK PHRASES (Arthur — male student practicing) ===
  { text: "I acknowledge that the data supports your position, but I am not entirely convinced.", voice: ARTHUR, filename: "aula6_blank_acknowledge_data" },
  { text: "Can you justify that recommendation with concrete evidence?", voice: ARTHUR, filename: "aula6_blank_justify_recommendation" },
  { text: "Both sides will need to compromise on the timeline to close this deal.", voice: ARTHUR, filename: "aula6_blank_compromise_timeline" },
  { text: "I concede that the timeline is tight, but I still believe the strategy is sound.", voice: ARTHUR, filename: "aula6_blank_concede_timeline" },
  { text: "I would like to challenge that assumption. Do we have enough evidence?", voice: ARTHUR, filename: "aula6_blank_challenge_assumption" },

  // === DIALOGUE — Elena = ELLEN (female, acquisition advocate) ===
  { text: "Elena, I appreciate your perspective on the acquisition opportunity. The target company has strong market position and complementary technology. However, I have concerns about the integration timeline and cultural fit. The premium they are asking is thirty percent above market value, and our track record with large acquisitions has been mixed.", voice: ELLEN, filename: "aula6_dialogue_elena_1" },
  { text: "I see your point, Michael, but I would argue that waiting means losing this window entirely. Their technology would take us three years to build organically. I acknowledge the premium is high, but the competitive advantage justifies it.", voice: ELLEN, filename: "aula6_dialogue_elena_2" },
  { text: "The synergies are projected at four hundred million over five years. I would challenge anyone who says we can achieve that through organic growth alone.", voice: ELLEN, filename: "aula6_dialogue_elena_3" },
  { text: "I acknowledge the benefits of a phased approach, though I still believe speed is critical. But I am willing to compromise if we set aggressive milestones for each phase.", voice: ELLEN, filename: "aula6_dialogue_elena_4" },

  // === DIALOGUE — Michael = ARTHUR (male, organic growth advocate) ===
  { text: "That is a valid concern, however, I tend to think that we should not let urgency override due diligence. Can you justify the premium with concrete synergy numbers?", voice: ARTHUR, filename: "aula6_dialogue_michael_1" },
  { text: "I concede that the synergy numbers are compelling. But I am not entirely convinced about the cultural integration. Their management style is very different from ours.", voice: ARTHUR, filename: "aula6_dialogue_michael_2" },
  { text: "That is actually a strong point, Carlos. A phased acquisition could reduce our exposure while still capturing the technology advantage. I could agree to that framework.", voice: ARTHUR, filename: "aula6_dialogue_michael_3" },

  // === DIALOGUE — Carlos = ARTHUR (male student) ===
  { text: "Would it be fair to say that we both agree on the strategic value, and the real question is about execution risk? Perhaps we could compromise on a phased approach.", voice: ARTHUR, filename: "aula6_dialogue_carlos_1" },
  { text: "I think we have found common ground. Let me summarize: we agree on the strategic value, we acknowledge the risks, and we are proposing a phased acquisition with clear milestones. I would argue this gives us the best of both positions.", voice: ARTHUR, filename: "aula6_dialogue_carlos_2" },

  // === ORAL DRILLING — Situations (Ellen — narrator) ===
  { text: "A colleague strongly disagrees with your strategy proposal. You want to respond diplomatically.", voice: ELLEN, filename: "aula6_oral_1_situation" },
  { text: "Your manager presents a plan you think has significant risks. You want to challenge it respectfully.", voice: ELLEN, filename: "aula6_oral_2_situation" },
  { text: "Two teams are in a deadlock over budget allocation. You want to find middle ground.", voice: ELLEN, filename: "aula6_oral_3_situation" },
  { text: "Someone makes an argument you partially agree with. You want to concede some points while maintaining your position.", voice: ELLEN, filename: "aula6_oral_4_situation" },
  { text: "A client is unhappy with your proposal. You need to acknowledge their concerns and persuade them.", voice: ELLEN, filename: "aula6_oral_5_situation" },
  { text: "Your team wants to take a conservative approach but you believe a bolder strategy is needed. You must persuade them.", voice: ELLEN, filename: "aula6_oral_6_situation" },

  // === ORAL DRILLING — Model answers (Arthur — male student) ===
  { text: "I see your point, but I would argue that the data supports a different approach. Would it be fair to say we look at the numbers together?", voice: ARTHUR, filename: "aula6_oral_1_model" },
  { text: "I acknowledge the potential benefits of this plan, however, I am not entirely convinced about the timeline. Can we justify the assumptions behind it?", voice: ARTHUR, filename: "aula6_oral_2_model" },
  { text: "I tend to think that both sides have valid points. Would it be fair to say we need a compromise? What if we split the budget seventy-thirty for Q3 and revisit in Q4?", voice: ARTHUR, filename: "aula6_oral_3_model" },
  { text: "I concede that the market data supports your point about timing. However, with respect, I would argue that we need to consider the integration risks before committing.", voice: ARTHUR, filename: "aula6_oral_4_model" },
  { text: "That is a valid concern about the cost. I acknowledge it is a significant investment. However, I would argue that the long-term savings justify the upfront expense. Let me show you the projected ROI.", voice: ARTHUR, filename: "aula6_oral_5_model" },
  { text: "I see your point about playing it safe. I tend to think that caution has its place. But I would argue that the competitive landscape demands a more aggressive stance. Can I justify this with the latest market analysis?", voice: ARTHUR, filename: "aula6_oral_6_model" },

  // === LISTENING 1 — Panel debate (Arthur — moderator) ===
  { text: "Ladies and gentlemen, thank you for joining this panel on corporate growth strategy. I will moderate today's debate between our two speakers. On one side, we have the case for aggressive acquisition. The argument is simple: in a fast-moving market, companies that acquire competitors gain immediate market share, talent, and technology. Waiting means falling behind. On the other side, we have the case for organic growth. The argument here is that acquisitions often destroy value through integration failures, cultural clashes, and overpayment. Building capability internally, while slower, creates a stronger foundation. Let us hear from both sides. The acquisition advocate argues that seventy percent of market leaders got there through strategic M and A. The organic growth advocate counters that sixty percent of acquisitions fail to deliver projected synergies. Both acknowledge that timing and execution matter more than the strategy itself.", voice: ARTHUR, filename: "aula6_listening_1_panel" },
  { text: "Ladies and gentlemen, thank you for joining this panel on corporate growth strategy. I will moderate today's debate between our two speakers. On one side, we have the case for aggressive acquisition. The argument is simple: in a fast-moving market, companies that acquire competitors gain immediate market share, talent, and technology. Waiting means falling behind. On the other side, we have the case for organic growth. The argument here is that acquisitions often destroy value through integration failures, cultural clashes, and overpayment. Building capability internally, while slower, creates a stronger foundation. Let us hear from both sides. The acquisition advocate argues that seventy percent of market leaders got there through strategic M and A. The organic growth advocate counters that sixty percent of acquisitions fail to deliver projected synergies. Both acknowledge that timing and execution matter more than the strategy itself.", voice: ARTHUR, filename: "aula6_listening_1_full" },

  // === LISTENING 2 — Mentor feedback (Ellen — mentor giving feedback to Carlos) ===
  { text: "Carlos, I want to give you some feedback on your persuasion skills. You have made real progress since we started working together. In today's board discussion, I noticed you did something very effective. When Elena pushed for the aggressive acquisition, instead of disagreeing directly, you acknowledged her point first and then presented your counter-argument. That is exactly the kind of hedging language that works in executive settings. One area to improve: when Michael challenged your compromise proposal, you got a bit defensive. Instead of justifying immediately, try conceding the valid parts of his criticism first, then redirecting. For example, say I concede that timeline is a concern, and then pivot to your solution. Also, practice using would it be fair to say more often. It is a powerful tool for finding common ground without forcing agreement.", voice: ELLEN, filename: "aula6_listening_2_mentor" },
  { text: "Carlos, I want to give you some feedback on your persuasion skills. You have made real progress since we started working together. In today's board discussion, I noticed you did something very effective. When Elena pushed for the aggressive acquisition, instead of disagreeing directly, you acknowledged her point first and then presented your counter-argument. That is exactly the kind of hedging language that works in executive settings. One area to improve: when Michael challenged your compromise proposal, you got a bit defensive. Instead of justifying immediately, try conceding the valid parts of his criticism first, then redirecting. For example, say I concede that timeline is a concern, and then pivot to your solution. Also, practice using would it be fair to say more often. It is a powerful tool for finding common ground without forcing agreement.", voice: ELLEN, filename: "aula6_listening_2_full" },

  // === ORDERING ===
  { text: "I see your point, but I would argue we need more data before committing. I tend to think a phased approach would reduce risk. Would it be fair to say we need another week? I acknowledge the urgency, but I am not entirely convinced. I concede the opportunity is real, but we must justify the investment.", voice: ARTHUR, filename: "aula6_order_l6" },
  { text: "I see your point, but I would argue we need more data before committing. I tend to think a phased approach would reduce risk. Would it be fair to say we need another week? I acknowledge the urgency, but I am not entirely convinced. I concede the opportunity is real, but we must justify the investment.", voice: ARTHUR, filename: "aula6_order_full" },
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

  console.log('Generating ' + unique.length + ' audio files for Aula 6...');
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
  audioMapEntries['[aula6-listening-1]'] = '/audio/carlos-vinicius-vale-bassan/aula6_listening_1_panel.mp3';
  audioMapEntries['[aula6-listening-2]'] = '/audio/carlos-vinicius-vale-bassan/aula6_listening_2_mentor.mp3';
  audioMapEntries['[order-l6]'] = '/audio/carlos-vinicius-vale-bassan/aula6_order_l6.mp3';

  // Full listening/order files used by data-src in players
  audioMapEntries['_listening_1_full'] = '/audio/carlos-vinicius-vale-bassan/aula6_listening_1_full.mp3';
  audioMapEntries['_listening_2_full'] = '/audio/carlos-vinicius-vale-bassan/aula6_listening_2_full.mp3';
  audioMapEntries['_order_full'] = '/audio/carlos-vinicius-vale-bassan/aula6_order_full.mp3';

  fs.writeFileSync(path.join(DIR, 'aula6_audioMap.json'), JSON.stringify(audioMapEntries, null, 2));
  console.log('\nDone! OK: ' + ok + ' | Skip: ' + skip + ' | Fail: ' + fail);
}

main().catch(e => { console.error(e); process.exit(1); });
