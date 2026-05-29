const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const DIR = path.join(__dirname, '..', 'public', 'audio', 'pricila-adamo');

const PHRASES = [
  // ===== Vocab words (1-2 words -> Arthur) =====
  { text: "Chapter", voice: ARTHUR, file: "aula2_chapter.mp3" },
  { text: "Milestone", voice: ARTHUR, file: "aula2_milestone.mp3" },
  { text: "Overcome", voice: ARTHUR, file: "aula2_overcome.mp3" },
  { text: "Memorable", voice: ARTHUR, file: "aula2_memorable.mp3" },
  { text: "Decade", voice: ARTHUR, file: "aula2_decade.mp3" },
  { text: "Transform", voice: ARTHUR, file: "aula2_transform.mp3" },
  { text: "Reflect", voice: ARTHUR, file: "aula2_reflect.mp3" },
  { text: "Achievement", voice: ARTHUR, file: "aula2_achievement.mp3" },
  { text: "Challenge", voice: ARTHUR, file: "aula2_challenge.mp3" },
  { text: "Opportunity", voice: ARTHUR, file: "aula2_opportunity.mp3" },

  // ===== Vocab example sentences (alternate) =====
  { text: "My career as a dentist was an important chapter of my life.", voice: ARTHUR, file: "aula2_career_chapter.mp3" },
  { text: "Graduating from dental school was a major milestone.", voice: ELLEN, file: "aula2_graduating_milestone.mp3" },
  { text: "I overcame my fear of speaking English at the hospital in Canada.", voice: ARTHUR, file: "aula2_overcame_fear.mp3" },
  { text: "My trip to Canada was the most memorable experience of my life.", voice: ELLEN, file: "aula2_memorable_experience.mp3" },
  { text: "I worked as a dentist for over two decades.", voice: ARTHUR, file: "aula2_two_decades.mp3" },
  { text: "That trip to Canada transformed the way I see English.", voice: ELLEN, file: "aula2_transformed.mp3" },
  { text: "When I reflect on my career, I feel proud of what I built.", voice: ARTHUR, file: "aula2_reflect_career.mp3" },
  { text: "Running my own dental clinic was my greatest achievement.", voice: ELLEN, file: "aula2_greatest_achievement.mp3" },
  { text: "Speaking English at the hospital was a real challenge.", voice: ARTHUR, file: "aula2_real_challenge.mp3" },
  { text: "Retirement is an opportunity to explore the world.", voice: ELLEN, file: "aula2_opportunity_explore.mp3" },

  // ===== Survival / expression phrases =====
  { text: "When I was younger, I used to...", voice: ARTHUR, file: "aula2_when_i_was_younger.mp3" },
  { text: "One of the most memorable moments was when...", voice: ELLEN, file: "aula2_most_memorable_moments.mp3" },
  { text: "Looking back, I realize that...", voice: ARTHUR, file: "aula2_looking_back.mp3" },
  { text: "That experience changed my life because...", voice: ELLEN, file: "aula2_changed_my_life.mp3" },
  { text: "I have achieved a lot, but my best chapter is still ahead.", voice: ARTHUR, file: "aula2_best_chapter_ahead.mp3" },

  // ===== Dialogue: Mark = Arthur, Pricila = Ellen =====
  { text: "Hi Pricila! Tell me about your life. What chapters have you been through?", voice: ARTHUR, file: "aula2_dialogue_mark_1.mp3" },
  { text: "Well, I graduated from dental school in 1995. That was a major milestone for me.", voice: ELLEN, file: "aula2_dialogue_pricila_1.mp3" },
  { text: "That is impressive! What happened after that?", voice: ARTHUR, file: "aula2_dialogue_mark_2.mp3" },
  { text: "I opened my own clinic in Araras. I worked there for over two decades. It was my greatest achievement.", voice: ELLEN, file: "aula2_dialogue_pricila_2.mp3" },
  { text: "Have you ever had a memorable experience abroad?", voice: ARTHUR, file: "aula2_dialogue_mark_3.mp3" },
  { text: "Yes! In 2000, I traveled to Canada. My daughter got sick and I had to speak English at the hospital. I overcame my fear that day.", voice: ELLEN, file: "aula2_dialogue_pricila_3.mp3" },
  { text: "That sounds like it really transformed you. What is your next chapter?", voice: ARTHUR, file: "aula2_dialogue_mark_4.mp3" },
  { text: "Retirement! Looking back, I have achieved a lot. But my best chapter is still ahead. I want to explore Australia.", voice: ELLEN, file: "aula2_dialogue_pricila_4.mp3" },

  // ===== Listening 1: Pricila's life chapters (Ellen, full paragraph) =====
  { text: "My life has had many chapters. The first chapter was growing up in Araras, a small city in Sao Paulo state. I was always curious and loved learning. The second chapter started when I graduated from dental school in 1995. That was a major milestone. I opened my own clinic and worked there for over two decades. The third chapter was my journey with English. In 2000, I traveled to Canada. My daughter got sick and I had to speak English at the hospital. I overcame my fear that day. It was the most memorable experience of my life. It transformed the way I see English. Now I am starting a new chapter. Retirement is an opportunity to explore the world. Looking back, I have achieved a lot, but I believe my best chapter is still ahead.", voice: ELLEN, file: "aula2_listening_1_life_chapters.mp3" },

  // ===== Listening 2: Mark's career story (Arthur, full paragraph) =====
  { text: "My name is Mark and I am from Boston. I have had an interesting career. I graduated from university in 1998 and started working in marketing. In 2005, I moved to Brazil for a job opportunity. It was a real challenge because I did not speak Portuguese. But I overcame that obstacle and learned the language in two years. The most memorable decade of my career was the 2010s. I transformed my small team into a department of thirty people. That was my greatest achievement. Looking back, every challenge was an opportunity to grow. I have reflected on my journey many times, and I realize that the difficult moments were the ones that transformed me the most.", voice: ARTHUR, file: "aula2_listening_2_mark_story.mp3" },
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

  console.log('Generating ' + PHRASES.length + ' audio files for Pricila Adamo — Aula 2...');
  let generated = 0, skipped = 0;
  for (const p of PHRASES) {
    const outPath = path.join(DIR, p.file);
    if (fs.existsSync(outPath)) {
      console.log('SKIP: ' + p.file);
      skipped++;
    } else {
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
