const fs = require('fs');
const path = require('path');
const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const DIR = path.join(__dirname, '..', 'public', 'audio', 'luiz-bressane');

const PHRASES = [
  // VOCAB WORDS
  { text: "Attend", voice: ARTHUR, filename: "aula4_attend" },
  { text: "Keynote", voice: ARTHUR, filename: "aula4_keynote" },
  { text: "Struggle", voice: ARTHUR, filename: "aula4_struggle" },
  { text: "Realize", voice: ARTHUR, filename: "aula4_realize" },
  { text: "Rely On", voice: ARTHUR, filename: "aula4_rely_on" },
  { text: "Session", voice: ARTHUR, filename: "aula4_session" },
  { text: "Follow Up", voice: ARTHUR, filename: "aula4_follow_up" },
  { text: "Subtitles", voice: ARTHUR, filename: "aula4_subtitles" },

  // VOCAB EXAMPLES
  { text: "I attended the Gartner Symposium in Orlando last year.", voice: ELLEN, filename: "aula4_i_attended_the_gartner_symposium" },
  { text: "The keynote speaker talked about artificial intelligence.", voice: ARTHUR, filename: "aula4_the_keynote_speaker_talked" },
  { text: "I struggled to understand the presentations without subtitles.", voice: ELLEN, filename: "aula4_i_struggled_to_understand" },
  { text: "At some point, I realized I could not follow the discussion.", voice: ARTHUR, filename: "aula4_at_some_point_i_realized" },
  { text: "I had to rely on my earbuds for real-time translation.", voice: ELLEN, filename: "aula4_i_had_to_rely_on" },
  { text: "The morning session was about technology and management.", voice: ARTHUR, filename: "aula4_the_morning_session_was" },
  { text: "I wanted to follow up with the speakers, but I could not.", voice: ELLEN, filename: "aula4_i_wanted_to_follow_up" },
  { text: "I needed subtitles to understand the conference talks.", voice: ARTHUR, filename: "aula4_i_needed_subtitles" },

  // FILL-IN
  { text: "I attended a big technology conference in Orlando.", voice: ELLEN, filename: "aula4_fill_attended" },
  { text: "The keynote was interesting but very fast.", voice: ARTHUR, filename: "aula4_fill_keynote" },
  { text: "I struggled to follow the speakers without subtitles.", voice: ELLEN, filename: "aula4_fill_struggled" },
  { text: "I realized that my English was not good enough.", voice: ARTHUR, filename: "aula4_fill_realized" },
  { text: "I relied on technology to understand the presentations.", voice: ELLEN, filename: "aula4_fill_relied" },
  { text: "I could not follow up because I felt insecure.", voice: ARTHUR, filename: "aula4_fill_follow_up" },

  // PRONUNCIATION
  { text: "I attended the Gartner Symposium in Orlando. I struggled to follow the keynote.", voice: ARTHUR, filename: "aula4_pron_1" },
  { text: "At some point, I realized I could not understand without subtitles.", voice: ELLEN, filename: "aula4_pron_2" },
  { text: "Looking back, I think it was a turning point for my English.", voice: ARTHUR, filename: "aula4_pron_3" },

  // DIALOGUE (Karen=Ellen, Luiz=Arthur)
  { text: "So, Luiz, tell me about your trip to Orlando. What happened?", voice: ELLEN, filename: "aula4_dlg_karen_1" },
  { text: "I attended the Gartner Symposium last year. It was a big technology conference.", voice: ARTHUR, filename: "aula4_dlg_luiz_1" },
  { text: "How was the experience? Did you enjoy it?", voice: ELLEN, filename: "aula4_dlg_karen_2" },
  { text: "The keynote was interesting, but I struggled to follow most of the sessions.", voice: ARTHUR, filename: "aula4_dlg_luiz_2" },
  { text: "What was the hardest part?", voice: ELLEN, filename: "aula4_dlg_karen_3" },
  { text: "I realized that the speakers talked very fast. I could not understand without help.", voice: ARTHUR, filename: "aula4_dlg_luiz_3" },
  { text: "What did you do to manage?", voice: ELLEN, filename: "aula4_dlg_karen_4" },
  { text: "I relied on my earbuds for translation. I also used Word to transcribe the talks.", voice: ARTHUR, filename: "aula4_dlg_luiz_4" },
  { text: "Did you try to network with other attendees?", voice: ELLEN, filename: "aula4_dlg_karen_5" },
  { text: "I wanted to follow up with some people, but I felt too insecure to start a conversation in English.", voice: ARTHUR, filename: "aula4_dlg_luiz_5" },

  // SURVIVAL
  { text: "I attended a conference in Orlando last year.", voice: ARTHUR, filename: "aula4_surv_1" },
  { text: "I struggled to follow the presentations.", voice: ELLEN, filename: "aula4_surv_2" },
  { text: "I realized I needed to improve my English.", voice: ARTHUR, filename: "aula4_surv_3" },
  { text: "I relied on technology to understand the speakers.", voice: ELLEN, filename: "aula4_surv_4" },
  { text: "Looking back, it was a turning point.", voice: ARTHUR, filename: "aula4_surv_5" },

  // GRAMMAR (irregular past)
  { text: "I went to Orlando.", voice: ARTHUR, filename: "aula4_gram_went" },
  { text: "The conference was very big.", voice: ELLEN, filename: "aula4_gram_was" },
  { text: "I had a difficult experience.", voice: ARTHUR, filename: "aula4_gram_had" },
  { text: "I felt frustrated at the end of the day.", voice: ELLEN, filename: "aula4_gram_felt" },
  { text: "I tried to understand but I could not.", voice: ARTHUR, filename: "aula4_gram_tried" },
  { text: "I heard the speakers but I did not understand.", voice: ELLEN, filename: "aula4_gram_heard" },
  { text: "I understood some words but not the full sentences.", voice: ARTHUR, filename: "aula4_gram_understood" },
  { text: "I said to myself: this time it did not work.", voice: ELLEN, filename: "aula4_gram_said" },

  // EXPRESSIONS
  { text: "I managed to understand some parts.", voice: ARTHUR, filename: "aula4_expr_managed" },
  { text: "I struggled to follow the keynote.", voice: ELLEN, filename: "aula4_expr_struggled" },
  { text: "At some point, I realized it was too fast.", voice: ARTHUR, filename: "aula4_expr_realized" },
  { text: "Looking back, I think it was a turning point.", voice: ELLEN, filename: "aula4_expr_looking_back" },

  // LISTENING 1 (long)
  { text: "Last year, I went to Orlando for the Gartner Symposium. It was a big international conference about technology and management. I attended several sessions and one keynote presentation. The keynote speaker talked about artificial intelligence and the future of work. I struggled to follow most of the talks because the speakers talked very fast. At some point, I realized I could not understand without help. I relied on my earbuds with real-time translation and I used Word to transcribe the presentations. I wanted to follow up with some of the speakers, but I felt too insecure to start a conversation in English. By the end of the day, I said to myself: I need to improve my English. Looking back, I think that experience was a turning point.", voice: ARTHUR, filename: "aula4_listening_1" },

  // LISTENING 2 (American attendee)
  { text: "I went to a conference in Chicago last month. It was a three-day event with about two thousand attendees. I attended the keynote on the first morning. The speaker was fantastic. After that, I went to several sessions about data analytics. I managed to network with a few people during the breaks. I followed up with three of them by email the next week. Conferences are exhausting, but they are great for making connections.", voice: ELLEN, filename: "aula4_listening_2" },

  // ORDER
  { text: "I went to Orlando for a conference. I attended the keynote presentation. I struggled to understand the speakers. I realized I needed help. I relied on earbuds with translation.", voice: ARTHUR, filename: "aula4_order_l4" },
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
  console.log('Generating ' + PHRASES.length + ' audio files for Luiz Bressane Aula 4...');
  for (const p of PHRASES) {
    const fname = p.filename + '.mp3';
    const outPath = path.join(DIR, fname);
    if (fs.existsSync(outPath)) { console.log('SKIP: ' + fname); }
    else {
      try {
        const bytes = await gen(p.text, p.voice, outPath);
        console.log('OK [' + (p.voice === ELLEN ? 'ellen' : 'arthur') + ']: ' + fname + ' (' + (bytes/1024).toFixed(1) + 'KB)');
        await new Promise(r => setTimeout(r, 500));
      } catch(e) { console.error('FAIL: ' + fname + ' -- ' + e.message); }
    }
  }
  console.log('\nDone! Total MP3s: ' + fs.readdirSync(DIR).filter(f => f.endsWith('.mp3')).length);
}
main().catch(e => { console.error(e); process.exit(1); });
