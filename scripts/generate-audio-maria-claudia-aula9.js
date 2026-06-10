const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const DIR = path.join(__dirname, '..', 'public', 'audio', 'maria-claudia-curimbaba');

const PHRASES = [
  // ===== Vocab (Ellen) =====
  { text: "Mingle", file: "aula9_mingle.mp3", voice: ELLEN },
  { text: "Curator", file: "aula9_curator.mp3", voice: ELLEN },
  { text: "Collector", file: "aula9_collector.mp3", voice: ELLEN },
  { text: "Vernissage", file: "aula9_vernissage.mp3", voice: ELLEN },
  { text: "Stunning", file: "aula9_stunning.mp3", voice: ELLEN },
  { text: "Perspective", file: "aula9_perspective.mp3", voice: ELLEN },
  { text: "Networking", file: "aula9_networking.mp3", voice: ELLEN },
  { text: "Impression", file: "aula9_impression.mp3", voice: ELLEN },

  // ===== Vocab examples (alternate) =====
  { text: "At the gallery opening, Maria Claudia likes to mingle with artists and collectors.", file: "aula9_at_the_gallery_opening.mp3", voice: ARTHUR },
  { text: "The curator selected twenty pieces for the contemporary exhibit.", file: "aula9_the_curator_selected.mp3", voice: ELLEN },
  { text: "The collector purchased three paintings from the Brazilian artist.", file: "aula9_the_collector_purchased.mp3", voice: ARTHUR },
  { text: "The vernissage attracted over two hundred guests from the business community.", file: "aula9_the_vernissage_attracted.mp3", voice: ELLEN },
  { text: "The sculpture in the center of the gallery is absolutely stunning.", file: "aula9_the_sculpture_is.mp3", voice: ARTHUR },
  { text: "Art gives us a fresh perspective on everyday life.", file: "aula9_art_gives_us.mp3", voice: ELLEN },
  { text: "Gallery openings are excellent opportunities for networking.", file: "aula9_gallery_openings_are.mp3", voice: ARTHUR },
  { text: "My first impression of the exhibit was very positive.", file: "aula9_my_first_impression.mp3", voice: ELLEN },

  // ===== Expressions (alternate) =====
  { text: "I think, believe, feel that...", file: "aula9_expr_i_think_believe.mp3", voice: ARTHUR },
  { text: "I believe that contemporary art reflects the energy of modern business.", file: "aula9_expr_believe_example.mp3", voice: ELLEN },
  { text: "What is your take on...?", file: "aula9_expr_what_is_your_take.mp3", voice: ARTHUR },
  { text: "What is your take on this abstract piece?", file: "aula9_expr_take_example.mp3", voice: ELLEN },
  { text: "If you ask me...", file: "aula9_expr_if_you_ask_me.mp3", voice: ARTHUR },
  { text: "If you ask me, this is the highlight of the entire collection.", file: "aula9_expr_ask_me_example.mp3", voice: ELLEN },

  // ===== Grammar context passage (Ellen) =====
  { text: "Maria Claudia is attending a gallery vernissage in Houston with colleagues and business partners. She mingles with the curator, who explains the theme of the exhibit. I think this collection represents the best of contemporary Brazilian art, the curator says. Maria Claudia looks at a stunning abstract sculpture. I believe it captures the energy of Sao Paulo, she replies. A collector approaches and asks, What is your take on the large painting in the corner? Maria Claudia considers her perspective. If you ask me, I feel it is the most powerful piece here. The composition is bold and the palette is vibrant. The collector agrees: That is a great point. My first impression was the same.", file: "aula9_grammar_context_passage.mp3", voice: ELLEN },

  // ===== Fill-in (alternate) =====
  { text: "Maria Claudia likes to mingle with artists at gallery openings.", file: "aula9_fill_mingle.mp3", voice: ARTHUR },
  { text: "The curator selected twenty pieces for the exhibit.", file: "aula9_fill_curator.mp3", voice: ELLEN },
  { text: "The collector purchased three paintings from the Brazilian artist.", file: "aula9_fill_collector.mp3", voice: ARTHUR },
  { text: "The vernissage attracted over two hundred guests.", file: "aula9_fill_vernissage.mp3", voice: ELLEN },
  { text: "The sculpture is absolutely stunning.", file: "aula9_fill_stunning.mp3", voice: ARTHUR },
  { text: "Art gives us a fresh perspective on everyday life.", file: "aula9_fill_perspective.mp3", voice: ELLEN },
  { text: "Gallery openings are great for networking.", file: "aula9_fill_networking.mp3", voice: ARTHUR },
  { text: "My first impression of the exhibit was very positive.", file: "aula9_fill_impression.mp3", voice: ELLEN },

  // ===== Ordering =====
  { text: "Welcome to the vernissage. It is wonderful to see you here. Have you had a chance to see the main exhibit? What is your take on the large abstract painting? I believe it is the most striking piece in the collection. If you ask me, the artist has a unique perspective. It was a pleasure meeting you. Let us stay in touch.", file: "aula9_order_gallery_sequence.mp3", voice: ELLEN },

  // ===== Survival (Ellen) =====
  { text: "I believe this is a stunning piece of art.", file: "aula9_surv_believe_stunning.mp3", voice: ELLEN },
  { text: "What is your take on the exhibit?", file: "aula9_surv_your_take.mp3", voice: ELLEN },
  { text: "If you ask me, the composition is remarkable.", file: "aula9_surv_ask_me.mp3", voice: ELLEN },
  { text: "It was a pleasure meeting you tonight.", file: "aula9_surv_pleasure_meeting.mp3", voice: ELLEN },
  { text: "Gallery openings are great for networking.", file: "aula9_surv_networking.mp3", voice: ELLEN },

  // ===== Speech (Ellen) =====
  { text: "I believe that contemporary art reflects the energy of modern business.", file: "aula9_speech_believe_contemporary.mp3", voice: ELLEN },
  { text: "What is your take on this abstract piece?", file: "aula9_speech_your_take.mp3", voice: ELLEN },
  { text: "If you ask me, this is the highlight of the collection.", file: "aula9_speech_ask_me.mp3", voice: ELLEN },
  { text: "My first impression of the exhibit was very positive.", file: "aula9_speech_first_impression.mp3", voice: ELLEN },
  { text: "Gallery openings are excellent opportunities for networking.", file: "aula9_speech_networking.mp3", voice: ELLEN },

  // ===== Listening 1 (MC at gallery = Ellen) =====
  { text: "Good evening, everyone. Welcome to this beautiful vernissage. I have been looking forward to this exhibit for weeks. The curator has done a remarkable job selecting these pieces. I think the theme, Contemporary Voices of Brazil, is both timely and powerful. What strikes me most is the large abstract painting near the entrance. I believe it captures the energy and complexity of modern Sao Paulo. The palette is warm and vibrant, with bold reds and deep oranges. If you ask me, it is the highlight of the entire collection. I also love the sculpture in the center. It is absolutely stunning. Art like this gives us a fresh perspective on our daily lives. Tonight is not just about art, though. It is also about networking and building connections. I feel that events like this bring together business and creativity in a unique way.", file: "aula9_ic_listening1_mc_gallery.mp3", voice: ELLEN },

  // ===== Listening 2 (David/collector = Arthur) =====
  { text: "I appreciate Maria Claudia's perspective, but I see things a bit differently. I consider myself a traditional art collector. I believe that the older European paintings have a depth that contemporary art sometimes lacks. Do not get me wrong, I think the exhibit is well curated. But if you ask me, the small landscape painting in the back room is the real gem. The composition is subtle, the colors are muted, and the technique is extraordinary. What is your take on it? I feel that networking at events like this is valuable, but my first impression tonight was about the art itself. I think we should appreciate both styles. Contemporary and traditional art offer different perspectives, and I believe a great collection includes both.", file: "aula9_ic_listening2_collector.mp3", voice: ARTHUR },

  // ===== Dialogue =====
  { text: "Good evening. I do not think we have met. I am Maria Claudia from Sao Paulo. Are you a collector?", file: "aula9_ic_dlg_mc_1.mp3", voice: ELLEN },
  { text: "Good evening, Maria Claudia. Yes, I am. I have been collecting contemporary art for about ten years. What is your take on the exhibit?", file: "aula9_ic_dlg_collector_1.mp3", voice: ARTHUR },
  { text: "I think it is exceptional. I believe the curator made excellent choices. Have you seen the large abstract painting near the entrance?", file: "aula9_ic_dlg_mc_2.mp3", voice: ELLEN },
  { text: "I have. It is very striking. But if you ask me, I find the smaller pieces more interesting. I feel they show more technique.", file: "aula9_ic_dlg_collector_2.mp3", voice: ARTHUR },
  { text: "I see your point, but I believe abstract art has its own kind of technique. The composition requires great skill.", file: "aula9_ic_dlg_mc_3.mp3", voice: ELLEN },
  { text: "That is a great point. I had not considered that perspective. What do you think about the sculpture in the center?", file: "aula9_ic_dlg_collector_3.mp3", voice: ARTHUR },
  { text: "I think it is absolutely stunning. My first impression was that it looks like the skyline of Sao Paulo.", file: "aula9_ic_dlg_mc_4.mp3", voice: ELLEN },
  { text: "Interesting. I can see that now. Do you attend many vernissages? Gallery openings are great for networking.", file: "aula9_ic_dlg_collector_4.mp3", voice: ARTHUR },
  { text: "Yes, I believe that art and business are deeply connected. I always try to mingle with artists and curators at these events.", file: "aula9_ic_dlg_mc_5.mp3", voice: ELLEN },
  { text: "I completely agree. It was a pleasure meeting you, Maria Claudia. Let us stay in touch.", file: "aula9_ic_dlg_collector_5.mp3", voice: ARTHUR },

  // ===== Error correction =====
  { text: "I am think this painting is beautiful.", file: "aula9_ic_error_am_think.mp3", voice: ARTHUR },
  { text: "I am agree with your opinion.", file: "aula9_ic_error_am_agree.mp3", voice: ELLEN },
  { text: "What is your take about this piece?", file: "aula9_ic_error_take_about.mp3", voice: ARTHUR },
  { text: "I am believe the exhibit is wonderful.", file: "aula9_ic_error_am_believe.mp3", voice: ELLEN },
  { text: "If you ask to me, this is the best painting.", file: "aula9_ic_error_ask_to_me.mp3", voice: ARTHUR },
];

async function gen(text, voiceId, outPath) {
  const r = await fetch('https://api.elevenlabs.io/v1/text-to-speech/' + voiceId, {
    method: 'POST',
    headers: { 'xi-api-key': API_KEY, 'Content-Type': 'application/json' },
    body: JSON.stringify({ text, model_id: 'eleven_multilingual_v2', voice_settings: { stability: 0.5, similarity_boost: 0.75 } }),
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
  const unique = PHRASES.filter(p => { const k = p.file.toLowerCase(); if (seen.has(k)) return false; seen.add(k); return true; });
  console.log('Generating ' + unique.length + ' AULA 9 audio files...');
  let generated = 0, skipped = 0;
  for (const p of unique) {
    const outPath = path.join(DIR, p.file);
    if (fs.existsSync(outPath)) { console.log('SKIP: ' + p.file); skipped++; }
    else {
      try {
        const bytes = await gen(p.text, p.voice, outPath);
        console.log('OK [' + (p.voice === ELLEN ? 'ellen' : 'arthur') + ']: ' + p.file + ' (' + (bytes / 1024).toFixed(1) + 'KB)');
        generated++;
        await new Promise(r => setTimeout(r, 500));
      } catch (e) { console.error('FAIL: ' + p.file + ' — ' + e.message); }
    }
  }
  console.log('\nDone! Generated: ' + generated + ' | Skipped: ' + skipped + ' | Total: ' + unique.length);
}
main();
