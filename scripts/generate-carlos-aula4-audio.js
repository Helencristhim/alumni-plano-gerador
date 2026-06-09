const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const DIR = path.join(__dirname, '..', 'public', 'audio', 'carlos-vinicius-vale-bassan');

// Carlos = male = ARTHUR for ALL his lines and single words
// David Chen = male = ARTHUR for his dialogue lines
// General/alternating phrases: alternate ARTHUR/ELLEN

const PHRASES = [
  // === VOCAB WORDS (Arthur — male student) ===
  { text: "Clarify", voice: ARTHUR, prefix: "aula4" },
  { text: "Paraphrase", voice: ARTHUR, prefix: "aula4" },
  { text: "Confirm", voice: ARTHUR, prefix: "aula4" },
  { text: "Summarize", voice: ARTHUR, prefix: "aula4" },
  { text: "Interpret", voice: ARTHUR, prefix: "aula4" },
  { text: "Follow up", voice: ARTHUR, prefix: "aula4" },
  { text: "Catch", voice: ARTHUR, prefix: "aula4" },
  { text: "Rephrase", voice: ARTHUR, prefix: "aula4" },

  // === PRE-CLASS VOCAB EXAMPLES (alternating Arthur/Ellen) ===
  { text: "Could you clarify what you mean by...?", voice: ARTHUR, prefix: "aula4" },
  { text: "If I understand correctly, you are saying that...", voice: ELLEN, prefix: "aula4" },
  { text: "So what you are saying is...", voice: ARTHUR, prefix: "aula4" },
  { text: "Could you clarify what the client wants?", voice: ELLEN, prefix: "aula4" },
  { text: "I would like to confirm whether the deal is still on track.", voice: ARTHUR, prefix: "aula4" },
  { text: "Can you tell me what the timeline looks like?", voice: ELLEN, prefix: "aula4" },
  { text: "Do you know if the board has approved the budget?", voice: ARTHUR, prefix: "aula4" },

  // === IN CLASS VOCAB EXAMPLES (alternating Arthur/Ellen) ===
  { text: "I need to clarify a few points before we proceed.", voice: ARTHUR, prefix: "aula4" },
  { text: "Let me paraphrase what you just said to make sure I understand.", voice: ELLEN, prefix: "aula4" },
  { text: "Can you confirm that the numbers are accurate?", voice: ARTHUR, prefix: "aula4" },
  { text: "To summarize, we are looking at three key risks.", voice: ELLEN, prefix: "aula4" },
  { text: "How do you interpret these results?", voice: ARTHUR, prefix: "aula4" },
  { text: "I will follow up with the legal team on that.", voice: ELLEN, prefix: "aula4" },
  { text: "Sorry, I did not catch that. Could you say it again?", voice: ARTHUR, prefix: "aula4" },
  { text: "Let me rephrase the question to be clearer.", voice: ELLEN, prefix: "aula4" },

  // === EXPRESSIONS (Arthur — male student) ===
  { text: "Could you clarify what you mean by synergy targets?", voice: ARTHUR, prefix: "aula4" },
  { text: "If I understand correctly, you are saying that the valuation needs to be revised.", voice: ARTHUR, prefix: "aula4" },
  { text: "So what you are saying is that we should postpone the closing date.", voice: ARTHUR, prefix: "aula4" },

  // === FILL-IN PHRASES (Arthur — male student practicing) ===
  { text: "David, could you clarify what you mean by the earn-out structure?", voice: ARTHUR, prefix: "aula4" },

  // === SPEECH CARDS (Arthur — male student) ===
  { text: "Sorry, I did not catch that. Could you repeat the last point?", voice: ARTHUR, prefix: "aula4" },
  { text: "Let me paraphrase to make sure we are aligned.", voice: ARTHUR, prefix: "aula4" },
  { text: "I will follow up with the CFO on the working capital figures.", voice: ARTHUR, prefix: "aula4" },

  // === SURVIVAL CARD (Arthur — male student) ===
  // "Could you clarify what you mean by...?" already above
  // "If I understand correctly, you are saying that..." already above
  // "So what you are saying is..." already above
  // "Sorry, I did not catch that. Could you say it again?" already above
  // "Let me paraphrase to make sure we are aligned." already above

  // === DIALOGUE — David Chen = ARTHUR (male colleague) ===
  { text: "Hey Carlos, thanks for jumping on. So, we have been looking at the target company, and honestly, the numbers are all over the place. The EBITDA looks solid on paper, but there are some red flags in the working capital adjustments.", voice: ARTHUR, filename: "aula4_dialogue_david_1" },
  { text: "Exactly. And on top of that, their customer concentration is pretty high. Like, seventy percent of revenue comes from just three accounts.", voice: ARTHUR, filename: "aula4_dialogue_david_2" },
  { text: "Sure. Seven-zero percent. Three clients make up almost all their revenue.", voice: ARTHUR, filename: "aula4_dialogue_david_3" },
  { text: "One hundred percent. That is the main risk factor I want to flag. We need to follow up with their sales team to understand the contract terms.", voice: ARTHUR, filename: "aula4_dialogue_david_4" },
  { text: "Perfect. I will send you the data room access tonight.", voice: ARTHUR, filename: "aula4_dialogue_david_5" },

  // === DIALOGUE — Carlos = ARTHUR (male student) ===
  { text: "If I understand correctly, you are saying that the reported EBITDA might not reflect the real picture?", voice: ARTHUR, filename: "aula4_dialogue_carlos_1" },
  { text: "Sorry, I did not catch the percentage. Could you rephrase that?", voice: ARTHUR, filename: "aula4_dialogue_carlos_2" },
  { text: "So what you are saying is that losing even one of those clients could significantly impact the valuation?", voice: ARTHUR, filename: "aula4_dialogue_carlos_3" },
  { text: "Got it. Let me summarize where we are. The EBITDA needs a closer look, customer concentration is a major risk, and we need to confirm the contract details with sales. I will follow up on that by Friday.", voice: ARTHUR, filename: "aula4_dialogue_carlos_4" },

  // === ORAL DRILLING — Situations (Ellen — narrator) ===
  { text: "Your colleague says the integration timeline is aggressive. You want to confirm.", voice: ELLEN, filename: "aula4_oral_1_situation" },
  { text: "The client mentions regulatory concerns. You did not understand which regulations.", voice: ELLEN, filename: "aula4_oral_2_situation" },
  { text: "David explains a complex tax structure. You want to confirm your understanding.", voice: ELLEN, filename: "aula4_oral_3_situation" },
  { text: "The VP mentions a change in strategy. You want to summarize.", voice: ELLEN, filename: "aula4_oral_4_situation" },
  { text: "A team member uses an idiom you do not know. You need clarification.", voice: ELLEN, filename: "aula4_oral_5_situation" },
  { text: "The CFO gives a long update on financials. You want to paraphrase the key point.", voice: ELLEN, filename: "aula4_oral_6_situation" },

  // === ORAL DRILLING — Model answers (Arthur — male student) ===
  { text: "Could you clarify what you mean by aggressive? Are we talking about the IT migration specifically?", voice: ARTHUR, filename: "aula4_oral_1_model" },
  { text: "Sorry, I did not catch which regulations you are referring to. Could you be more specific?", voice: ARTHUR, filename: "aula4_oral_2_model" },
  { text: "If I understand correctly, you are saying that the tax liability transfers to the acquirer after closing?", voice: ARTHUR, filename: "aula4_oral_3_model" },
  { text: "So to summarize, we are shifting from an asset deal to a stock deal. Is that correct?", voice: ARTHUR, filename: "aula4_oral_4_model" },
  { text: "That is an interesting point. Could you rephrase that? I want to make sure I follow.", voice: ARTHUR, filename: "aula4_oral_5_model" },
  { text: "Let me paraphrase to make sure I got it. The main issue is cash flow timing, not profitability. Is that right?", voice: ARTHUR, filename: "aula4_oral_6_model" },

  // === LISTENING 1 — Conference call (Arthur — David speaking) ===
  // This generates the [aula4-listening-1] key file
  { text: "So, Carlos, I just got off the phone with the target's CFO. He is saying that their adjusted EBITDA for last year was around forty-five million, but honestly, I think there is some creative accounting going on. The add-backs are pretty aggressive. And here is the thing, their biggest client, TechVenture, is up for contract renewal in Q2, and there is no guarantee they are going to renew. If they lose that account, we are looking at a fifteen to twenty percent revenue hit. On top of that, the CTO just resigned last week, which is never a good sign during due diligence. I think we need to seriously reconsider the valuation multiple.", voice: ARTHUR, filename: "aula4_listening_1_conference_call" },
  // This generates the full listening file used by data-src in the player
  { text: "So, Carlos, I just got off the phone with the target's CFO. He is saying that their adjusted EBITDA for last year was around forty-five million, but honestly, I think there is some creative accounting going on. The add-backs are pretty aggressive. And here is the thing, their biggest client, TechVenture, is up for contract renewal in Q2, and there is no guarantee they are going to renew. If they lose that account, we are looking at a fifteen to twenty percent revenue hit. On top of that, the CTO just resigned last week, which is never a good sign during due diligence. I think we need to seriously reconsider the valuation multiple.", voice: ARTHUR, filename: "aula4_listening_1_full" },

  // === LISTENING 2 — Debrief (Ellen — manager giving instructions) ===
  { text: "Hey Carlos, so that was an intense call with David. What are your main takeaways? I think we need to flag three things for the steering committee. First, the EBITDA adjustments need independent verification. Second, the customer concentration risk with TechVenture is real and material. And third, the CTO departure is a red flag for the tech integration. I want you to follow up with the target's finance team by Thursday and get the raw numbers. Can you also check if TechVenture has signed a letter of intent for renewal? That would change everything. Let me know if you need anything from my side.", voice: ELLEN, filename: "aula4_listening_2_debrief" },
  // Full listening file used by data-src in the player
  { text: "Hey Carlos, so that was an intense call with David. What are your main takeaways? I think we need to flag three things for the steering committee. First, the EBITDA adjustments need independent verification. Second, the customer concentration risk with TechVenture is real and material. And third, the CTO departure is a red flag for the tech integration. I want you to follow up with the target's finance team by Thursday and get the raw numbers. Can you also check if TechVenture has signed a letter of intent for renewal? That would change everything. Let me know if you need anything from my side.", voice: ELLEN, filename: "aula4_listening_2_full" },

  // === ORDERING ===
  { text: "Could you clarify what you mean by that? If I understand correctly, you are saying that we need to adjust the timeline. So what you are saying is the deal might not close this quarter. I did not catch the last part. Could you rephrase that? Let me summarize the key points.", voice: ARTHUR, filename: "aula4_order_l4" },
  // Order full version (used by audioMap text key)
  { text: "Could you clarify what you mean by that? If I understand correctly, you are saying that we need to adjust the timeline. So what you are saying is the deal might not close this quarter. I did not catch the last part. Could you rephrase that? Let me summarize the key points.", voice: ARTHUR, filename: "aula4_order_full" },

  // === ADDITIONAL SPEECH CARD / FILL-IN PHRASES (ensuring full coverage) ===
  { text: "Could you clarify what the main risk factors are?", voice: ARTHUR, prefix: "aula4" },
  { text: "If I understand correctly, the timeline has been moved to Q3.", voice: ARTHUR, prefix: "aula4" },
  { text: "So what you are saying is we need more due diligence on the tech stack.", voice: ARTHUR, prefix: "aula4" },
  { text: "Sorry, I did not catch that. Could you repeat the last point?", voice: ARTHUR, prefix: "aula4" },
  { text: "I will follow up with the CFO on the working capital figures.", voice: ARTHUR, prefix: "aula4" },
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

  console.log('Generating ' + unique.length + ' audio files for Aula 4...');
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
  audioMapEntries['[aula4-listening-1]'] = '/audio/carlos-vinicius-vale-bassan/aula4_listening_1_conference_call.mp3';
  audioMapEntries['[aula4-listening-2]'] = '/audio/carlos-vinicius-vale-bassan/aula4_listening_2_debrief.mp3';
  audioMapEntries['[order-l4]'] = '/audio/carlos-vinicius-vale-bassan/aula4_order_l4.mp3';

  // Full listening/order files used by data-src in players
  audioMapEntries['_listening_1_full'] = '/audio/carlos-vinicius-vale-bassan/aula4_listening_1_full.mp3';
  audioMapEntries['_listening_2_full'] = '/audio/carlos-vinicius-vale-bassan/aula4_listening_2_full.mp3';
  audioMapEntries['_order_full'] = '/audio/carlos-vinicius-vale-bassan/aula4_order_full.mp3';

  fs.writeFileSync(path.join(DIR, 'aula4_audioMap.json'), JSON.stringify(audioMapEntries, null, 2));
  console.log('\nDone! OK: ' + ok + ' | Skip: ' + skip + ' | Fail: ' + fail);
}

main().catch(e => { console.error(e); process.exit(1); });
