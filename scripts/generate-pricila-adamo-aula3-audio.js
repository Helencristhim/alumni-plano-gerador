const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const DIR = path.join(__dirname, '..', 'public', 'audio', 'pricila-adamo');

const PHRASES = [
  // Vocab words (Arthur)
  { text: "Goal", voice: ARTHUR, file: "aula3_goal.mp3" },
  { text: "Plan", voice: ARTHUR, file: "aula3_plan.mp3" },
  { text: "Dream", voice: ARTHUR, file: "aula3_dream.mp3" },
  { text: "Freedom", voice: ARTHUR, file: "aula3_freedom.mp3" },
  { text: "Purpose", voice: ARTHUR, file: "aula3_purpose.mp3" },
  { text: "Adventure", voice: ARTHUR, file: "aula3_adventure.mp3" },
  { text: "Lifestyle", voice: ARTHUR, file: "aula3_lifestyle.mp3" },
  { text: "Priority", voice: ARTHUR, file: "aula3_priority.mp3" },
  { text: "Bucket List", voice: ARTHUR, file: "aula3_bucket_list.mp3" },
  { text: "Embrace", voice: ARTHUR, file: "aula3_embrace.mp3" },

  // Vocab sentences (alternate)
  { text: "My goal is to travel to at least five countries after I retire.", voice: ARTHUR, file: "aula3_goal_sentence.mp3" },
  { text: "I am planning to visit Australia next year.", voice: ELLEN, file: "aula3_plan_sentence.mp3" },
  { text: "My dream is to speak English with the same richness I have in Portuguese.", voice: ARTHUR, file: "aula3_dream_sentence.mp3" },
  { text: "Retirement means freedom to do what I love.", voice: ELLEN, file: "aula3_freedom_sentence.mp3" },
  { text: "I need a new purpose now that I am leaving my career.", voice: ARTHUR, file: "aula3_purpose_sentence.mp3" },
  { text: "I want every trip to be a real adventure.", voice: ELLEN, file: "aula3_adventure_sentence.mp3" },
  { text: "I am going to change my lifestyle completely after retirement.", voice: ARTHUR, file: "aula3_lifestyle_sentence.mp3" },
  { text: "Health and travel are my top priorities right now.", voice: ELLEN, file: "aula3_priority_sentence.mp3" },
  { text: "Visiting Australia is at the top of my bucket list.", voice: ARTHUR, file: "aula3_bucket_list_sentence.mp3" },
  { text: "I want to embrace this new phase of my life with joy.", voice: ELLEN, file: "aula3_embrace_sentence.mp3" },

  // Expressions
  { text: "I am going to...", voice: ARTHUR, file: "aula3_expr_going_to.mp3" },
  { text: "I am planning to...", voice: ELLEN, file: "aula3_expr_planning_to.mp3" },
  { text: "One day, I hope to...", voice: ARTHUR, file: "aula3_expr_one_day.mp3" },
  { text: "My dream is to...", voice: ELLEN, file: "aula3_expr_my_dream.mp3" },
  { text: "The most important thing for me is...", voice: ARTHUR, file: "aula3_expr_most_important.mp3" },

  // Dialogue: Tom (Arthur) + Pricila (Ellen)
  { text: "Welcome to the travel agency! What can I help you with today?", voice: ARTHUR, file: "aula3_dialogue_tom_1.mp3" },
  { text: "I am going to retire soon, and I am planning to travel. Australia is at the top of my bucket list.", voice: ELLEN, file: "aula3_dialogue_pricila_1.mp3" },
  { text: "Australia is amazing! What is your goal for this trip?", voice: ARTHUR, file: "aula3_dialogue_tom_2.mp3" },
  { text: "My dream is to explore the country and feel confident speaking English abroad. I want freedom to go anywhere.", voice: ELLEN, file: "aula3_dialogue_pricila_2.mp3" },
  { text: "That is a wonderful purpose for traveling. How long are you planning to stay?", voice: ARTHUR, file: "aula3_dialogue_tom_3.mp3" },
  { text: "I think I will stay for about three weeks. I want to embrace every adventure.", voice: ELLEN, file: "aula3_dialogue_pricila_3.mp3" },
  { text: "Three weeks will be perfect. I am going to prepare a special itinerary for you.", voice: ARTHUR, file: "aula3_dialogue_tom_4.mp3" },
  { text: "Thank you! This is going to be the best chapter of my life. I am meeting my English teacher tomorrow to practice.", voice: ELLEN, file: "aula3_dialogue_pricila_4.mp3" },

  // Listening 1: Pricila's retirement vision (Ellen)
  { text: "I have been thinking about retirement for a long time. My goal is to completely change my lifestyle. I am going to travel more, read more, and spend more time doing things I love. My biggest dream is to visit Australia. I am planning to go next year. It is at the top of my bucket list. I want to see the Great Barrier Reef, visit Sydney, and explore Melbourne. Freedom is my priority now. I do not want to follow a schedule anymore. I want every day to be an adventure. I am also going to continue studying English. My purpose is to speak with confidence, not perfection. I want to embrace this new phase of my life with joy, not with pressure. I believe this will be the best chapter of my life.", voice: ELLEN, file: "aula3_listening_1_retirement_vision.mp3" },

  // Listening 2: Tom's travel advice (Arthur)
  { text: "I have been a travel agent for fifteen years, and I always tell my clients the same thing: the best trips are the ones where you embrace the unexpected. When you plan a trip to Australia, you are going to discover that it is much bigger than you think. My advice is to set clear goals but leave room for adventure. I think you will fall in love with Sydney. The Opera House, the harbour, the beaches. You are going to love Melbourne too. The coffee culture there is amazing. One thing I will say is that your priorities should include the Great Barrier Reef. It is a once in a lifetime experience. I am going to create an itinerary that gives you freedom to explore at your own pace. Your dream trip is going to become a reality.", voice: ARTHUR, file: "aula3_listening_2_tom_advice.mp3" },
];

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
  if (!API_KEY) { console.error('Set ELEVENLABS_API_KEY env var'); process.exit(1); }
  if (!fs.existsSync(DIR)) fs.mkdirSync(DIR, { recursive: true });
  console.log('Generating ' + PHRASES.length + ' audio files for Pricila Adamo — Aula 3...');
  let generated = 0, skipped = 0;
  for (const p of PHRASES) {
    const outPath = path.join(DIR, p.file);
    if (fs.existsSync(outPath)) { console.log('SKIP: ' + p.file); skipped++; }
    else {
      try {
        const bytes = await gen(p.text, p.voice, outPath);
        console.log('OK [' + (p.voice === ELLEN ? 'ellen' : 'arthur') + ']: ' + p.file + ' (' + (bytes/1024).toFixed(1) + 'KB)');
        generated++;
        await new Promise(r => setTimeout(r, 500));
      } catch(e) { console.error('FAIL: ' + p.file + ' — ' + e.message); }
    }
  }
  console.log('\nDone! Generated: ' + generated + ', Skipped: ' + skipped + ', Total: ' + PHRASES.length);
}

main().catch(e => { console.error(e); process.exit(1); });
