/**
 * Generate ElevenLabs audio for Roberto Rezende - Aula 8 (Networking & Small Talk)
 * Voice: Roberto (male student) = Arthur, Sarah Lee (female) = Ellen
 */
const fs = require('fs');
const path = require('path');
const https = require('https');

const ELEVENLABS_API_KEY = process.env.ELEVENLABS_API_KEY;
if (!ELEVENLABS_API_KEY) { console.error('ERROR: ELEVENLABS_API_KEY not set'); process.exit(1); }

const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const OUTPUT_DIR = path.join(__dirname, '..', 'public', 'audio', 'roberto-rezende');

const audioEntries = [
  // VOCAB WORDS (Arthur - 10)
  { text: "Small talk", file: "aula8_small_talk.mp3", voice: ARTHUR },
  { text: "Break the ice", file: "aula8_break_the_ice.mp3", voice: ARTHUR },
  { text: "Networking", file: "aula8_networking.mp3", voice: ARTHUR },
  { text: "Common ground", file: "aula8_common_ground.mp3", voice: ARTHUR },
  { text: "Catch up", file: "aula8_catch_up.mp3", voice: ARTHUR },
  { text: "Get along", file: "aula8_get_along.mp3", voice: ARTHUR },
  { text: "Bring up", file: "aula8_bring_up.mp3", voice: ARTHUR },
  { text: "Keep in touch", file: "aula8_keep_in_touch.mp3", voice: ARTHUR },
  { text: "By the way", file: "aula8_by_the_way.mp3", voice: ARTHUR },
  { text: "How about", file: "aula8_how_about.mp3", voice: ARTHUR },

  // VOCAB EXAMPLES (alternate Arthur/Ellen - 10)
  { text: "Small talk is important for building business relationships.", file: "aula8_vocab_small_talk_example.mp3", voice: ARTHUR },
  { text: "I always try to break the ice before a meeting.", file: "aula8_vocab_break_the_ice_example.mp3", voice: ELLEN },
  { text: "Networking events are a great opportunity to meet new clients.", file: "aula8_vocab_networking_example.mp3", voice: ARTHUR },
  { text: "We found common ground when we discovered we both like engineering.", file: "aula8_vocab_common_ground_example.mp3", voice: ELLEN },
  { text: "Let me catch up with you after the presentation.", file: "aula8_vocab_catch_up_example.mp3", voice: ARTHUR },
  { text: "I get along well with my colleagues from Shanghai.", file: "aula8_vocab_get_along_example.mp3", voice: ELLEN },
  { text: "Do not bring up politics or religion at a business dinner.", file: "aula8_vocab_bring_up_example.mp3", voice: ARTHUR },
  { text: "Let us keep in touch after the conference.", file: "aula8_vocab_keep_in_touch_example.mp3", voice: ELLEN },
  { text: "By the way, have you tried the local food here?", file: "aula8_vocab_by_the_way_example.mp3", voice: ARTHUR },
  { text: "How about we grab a coffee after the session?", file: "aula8_vocab_how_about_example.mp3", voice: ELLEN },

  // DIALOGUE (Roberto=Arthur, Sarah=Ellen - 8 lines)
  { text: "Hi, I am Roberto from the Brazil office. This is a great event, is it not?", file: "aula8_dialogue_roberto1.mp3", voice: ARTHUR },
  { text: "It really is. I am Sarah from the Singapore office. Is this your first time at this conference?", file: "aula8_dialogue_sarah1.mp3", voice: ELLEN },
  { text: "No, I came last year too. The networking sessions are excellent, are they not?", file: "aula8_dialogue_roberto2.mp3", voice: ARTHUR },
  { text: "They are. By the way, what segment do you work in?", file: "aula8_dialogue_sarah2.mp3", voice: ELLEN },
  { text: "I handle diesel engines for agriculture. How about you?", file: "aula8_dialogue_roberto3.mp3", voice: ARTHUR },
  { text: "I am in the marine segment. We have a lot of common ground, do we not? Diesel is diesel.", file: "aula8_dialogue_sarah3.mp3", voice: ELLEN },
  { text: "Absolutely. We should keep in touch. Let me catch up with you after the keynote.", file: "aula8_dialogue_roberto4.mp3", voice: ARTHUR },
  { text: "Sounds great. By the way, have you tried the local food here? I heard it is amazing.", file: "aula8_dialogue_sarah4.mp3", voice: ELLEN },

  // LISTENING 1 (Arthur - Roberto's networking tips monologue)
  { text: "Good morning, everyone. I am Roberto Rezende from the Brazil office. I wanted to share a quick networking tip with the team. When you attend an event, the first thing you need to do is break the ice. Start with something simple. You could say, This is a great event, is it not? or Have you been here before? The goal is to find common ground. Ask about their work, their segment, their city. By the way, never bring up politics or salary at a business event. Stick to safe topics: travel, the conference, the industry. And always end the conversation by saying, Let us keep in touch. It was great meeting you. Small talk is not small. It builds relationships.", file: "aula8_listening1_networking_tips.mp3", voice: ARTHUR },

  // LISTENING 2 (Ellen - Amy's questions)
  { text: "Thank you, Roberto. That was very helpful. A few questions. First, you said we should break the ice with something simple. Can you give us two more examples of good opening questions? Second, you mentioned we should not bring up politics. What other topics should we avoid? Third, how do you keep in touch after the event? Do you exchange business cards or connect on LinkedIn? And finally, tag questions like is it not and do we not. Are they formal or informal? Should we use them with clients or only with colleagues?", file: "aula8_listening2_amy_questions.mp3", voice: ELLEN },

  // QUICKFIRE (Arthur - 6)
  { text: "This is a great event, is it not?", file: "aula8_quickfire1.mp3", voice: ARTHUR },
  { text: "Have you been to Brazil before? You would love it, would you not?", file: "aula8_quickfire2.mp3", voice: ARTHUR },
  { text: "We have a lot in common, do we not? We both work with diesel engines.", file: "aula8_quickfire3.mp3", voice: ARTHUR },
  { text: "By the way, how about we grab a coffee after the session?", file: "aula8_quickfire4.mp3", voice: ARTHUR },
  { text: "Let us keep in touch. It was great meeting you.", file: "aula8_quickfire5.mp3", voice: ARTHUR },
  { text: "The keynote was very interesting, was it not?", file: "aula8_quickfire6.mp3", voice: ARTHUR },

  // SURVIVAL (Arthur - 5)
  { text: "This is a great event, is it not?", file: "aula8_survival1.mp3", voice: ARTHUR },
  { text: "We have a lot in common, do we not?", file: "aula8_survival2.mp3", voice: ARTHUR },
  { text: "By the way, have you tried the local food?", file: "aula8_survival3.mp3", voice: ARTHUR },
  { text: "How about we grab a coffee after the session?", file: "aula8_survival4.mp3", voice: ARTHUR },
  { text: "Let us keep in touch after the conference.", file: "aula8_survival5.mp3", voice: ARTHUR },

  // ORDERING (Arthur)
  { text: "Hi, I am Roberto from Brazil. This is a great event, is it not? By the way, what segment do you work in? We have a lot in common. How about we grab a coffee? Let us keep in touch.", file: "order_l8_ordering.mp3", voice: ARTHUR },
];

const seen = new Set();
const uniqueEntries = [];
for (const entry of audioEntries) { if (!seen.has(entry.file)) { seen.add(entry.file); uniqueEntries.push(entry); } }

function generateAudio(text, voiceId) {
  return new Promise((resolve, reject) => {
    const payload = JSON.stringify({ text, model_id: "eleven_monolingual_v1", voice_settings: { stability: 0.5, similarity_boost: 0.75, style: 0.0, use_speaker_boost: true } });
    const options = { hostname: 'api.elevenlabs.io', port: 443, path: `/v1/text-to-speech/${voiceId}`, method: 'POST', headers: { 'Accept': 'audio/mpeg', 'Content-Type': 'application/json', 'xi-api-key': ELEVENLABS_API_KEY } };
    const req = https.request(options, (res) => {
      if (res.statusCode !== 200) { let body = ''; res.on('data', chunk => body += chunk); res.on('end', () => reject(new Error(`HTTP ${res.statusCode}: ${body}`))); return; }
      const chunks = []; res.on('data', chunk => chunks.push(chunk)); res.on('end', () => resolve(Buffer.concat(chunks)));
    });
    req.on('error', reject); req.write(payload); req.end();
  });
}
function sleep(ms) { return new Promise(resolve => setTimeout(resolve, ms)); }

async function main() {
  if (!fs.existsSync(OUTPUT_DIR)) fs.mkdirSync(OUTPUT_DIR, { recursive: true });
  const missing = uniqueEntries.filter(e => !fs.existsSync(path.join(OUTPUT_DIR, e.file)));
  console.log(`Total unique entries: ${uniqueEntries.length}`);
  console.log(`Already exist: ${uniqueEntries.length - missing.length}`);
  console.log(`Missing (to generate): ${missing.length}`);
  if (missing.length === 0) { console.log('All audio files already exist!'); return; }
  let generated = 0, errors = 0;
  for (const entry of missing) {
    const filepath = path.join(OUTPUT_DIR, entry.file);
    const voiceName = entry.voice === ARTHUR ? 'Arthur' : 'Ellen';
    console.log(`[${generated + errors + 1}/${missing.length}] Generating: ${entry.file} (${voiceName}) — "${entry.text.substring(0, 50)}..."`);
    try {
      const audioBuffer = await generateAudio(entry.text, entry.voice);
      fs.writeFileSync(filepath, audioBuffer);
      generated++;
      console.log(`  OK (${(audioBuffer.length / 1024).toFixed(1)} KB)`);
      await sleep(600);
    } catch (err) { errors++; console.error(`  FAILED: ${err.message}`); await sleep(2000); }
  }
  console.log(`\nDone! Generated: ${generated}, Errors: ${errors}`);
}
main().catch(console.error);
