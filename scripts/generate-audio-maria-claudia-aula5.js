const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const DIR = path.join(__dirname, '..', 'public', 'audio', 'maria-claudia-curimbaba');

const PHRASES = [
  // ===== Vocab words (Ellen — female student) =====
  { text: "Striking", file: "aula5_striking.mp3", voice: ELLEN },
  { text: "Abstract", file: "aula5_abstract.mp3", voice: ELLEN },
  { text: "Exhibit", file: "aula5_exhibit.mp3", voice: ELLEN },
  { text: "Contemporary", file: "aula5_contemporary.mp3", voice: ELLEN },
  { text: "Vibrant", file: "aula5_vibrant.mp3", voice: ELLEN },
  { text: "Subtle", file: "aula5_subtle.mp3", voice: ELLEN },
  { text: "Composition", file: "aula5_composition.mp3", voice: ELLEN },
  { text: "Palette", file: "aula5_palette.mp3", voice: ELLEN },

  // ===== Vocab example sentences (alternate) =====
  { text: "The painting has a striking use of color.", file: "aula5_the_painting_has_a_striking.mp3", voice: ARTHUR },
  { text: "She prefers abstract art over realistic paintings.", file: "aula5_she_prefers_abstract.mp3", voice: ELLEN },
  { text: "The museum has a new exhibit on modern art.", file: "aula5_the_museum_has_a_new.mp3", voice: ARTHUR },
  { text: "Contemporary art often challenges traditional ideas.", file: "aula5_contemporary_art_often.mp3", voice: ELLEN },
  { text: "The artist uses vibrant colors like red and orange.", file: "aula5_the_artist_uses_vibrant.mp3", voice: ARTHUR },
  { text: "The subtle tones in the background create depth.", file: "aula5_the_subtle_tones.mp3", voice: ELLEN },
  { text: "The composition draws your eye to the center.", file: "aula5_the_composition_draws.mp3", voice: ARTHUR },
  { text: "The artist chose a warm palette of earth tones.", file: "aula5_the_artist_chose.mp3", voice: ELLEN },

  // ===== Expressions (alternate) =====
  { text: "I find it...", file: "aula5_expr_i_find_it.mp3", voice: ARTHUR },
  { text: "I find it fascinating how the artist uses light and shadow.", file: "aula5_expr_i_find_it_example.mp3", voice: ELLEN },
  { text: "What strikes me is...", file: "aula5_expr_what_strikes_me.mp3", voice: ARTHUR },
  { text: "What strikes me is the contrast between the warm and cool colors.", file: "aula5_expr_what_strikes_example.mp3", voice: ELLEN },
  { text: "In my opinion...", file: "aula5_expr_in_my_opinion.mp3", voice: ARTHUR },
  { text: "In my opinion, this is one of the most powerful pieces in the exhibit.", file: "aula5_expr_in_my_opinion_example.mp3", voice: ELLEN },

  // ===== Grammar context passage (Ellen) =====
  { text: "Maria Claudia is visiting a contemporary art exhibit in Houston with her counterpart David Chen. She stops in front of a large abstract painting with vibrant colors. I find it fascinating, she says. What strikes me is the bold composition. The artist uses a warm palette of reds and oranges. In my opinion, this is the most striking piece in the exhibit. David points to a smaller, more subtle painting nearby. I find it elegant, he says. The composition is simpler, but the colors are more refined. It is a beautiful old European oil painting.", file: "aula5_grammar_context_passage.mp3", voice: ELLEN },

  // ===== Fill-in sentences (alternate) =====
  { text: "I find it fascinating how the artist uses light.", file: "aula5_fill_i_find_it_fascinating.mp3", voice: ARTHUR },
  { text: "The painting has a striking use of color and texture.", file: "aula5_fill_striking_use.mp3", voice: ELLEN },
  { text: "She prefers abstract art over realistic paintings.", file: "aula5_fill_abstract_art.mp3", voice: ARTHUR },
  { text: "The museum has a new exhibit on modern art.", file: "aula5_fill_new_exhibit.mp3", voice: ELLEN },
  { text: "The artist uses vibrant colors like red and orange.", file: "aula5_fill_vibrant_colors.mp3", voice: ARTHUR },
  { text: "The subtle tones in the background create depth.", file: "aula5_fill_subtle_tones.mp3", voice: ELLEN },
  { text: "The composition draws your eye to the center of the painting.", file: "aula5_fill_composition_draws.mp3", voice: ARTHUR },
  { text: "The artist chose a warm palette of earth tones.", file: "aula5_fill_warm_palette.mp3", voice: ELLEN },

  // ===== Ordering =====
  { text: "Welcome to the exhibit. Let me show you around. This is a contemporary abstract painting from 2023. What strikes me is the vibrant palette the artist chose. I find it fascinating how the composition guides your eye. In my opinion, this is the most striking piece in the collection. Let me know which painting you find most interesting.", file: "aula5_order_gallery_sequence.mp3", voice: ELLEN },

  // ===== Survival (Ellen) =====
  { text: "I find it fascinating.", file: "aula5_surv_i_find_it.mp3", voice: ELLEN },
  { text: "What strikes me is the use of color.", file: "aula5_surv_what_strikes_me.mp3", voice: ELLEN },
  { text: "In my opinion, this is a beautiful piece.", file: "aula5_surv_in_my_opinion.mp3", voice: ELLEN },
  { text: "The artist uses a vibrant palette.", file: "aula5_surv_vibrant_palette.mp3", voice: ELLEN },
  { text: "The composition is very striking.", file: "aula5_surv_composition_striking.mp3", voice: ELLEN },

  // ===== Speech (Ellen) =====
  { text: "I find it fascinating how the artist uses light and shadow.", file: "aula5_speech_i_find_it.mp3", voice: ELLEN },
  { text: "What strikes me is the contrast between warm and cool colors.", file: "aula5_speech_what_strikes_me.mp3", voice: ELLEN },
  { text: "The exhibit features contemporary abstract paintings.", file: "aula5_speech_the_exhibit.mp3", voice: ELLEN },
  { text: "In my opinion, the composition is very powerful.", file: "aula5_speech_in_my_opinion.mp3", voice: ELLEN },
  { text: "The artist chose a vibrant palette of reds and oranges.", file: "aula5_speech_vibrant_palette.mp3", voice: ELLEN },

  // ===== Listening 1 (MC at gallery = Ellen) =====
  { text: "This is one of my favorite exhibits. I come to Houston for business, but I always make time for art. What strikes me about this painting is the vibrant palette. The artist uses bold reds, deep oranges, and touches of gold. I find it absolutely fascinating. The composition is very dynamic. Your eye moves from the center outward, following the brushstrokes. In my opinion, this is the most striking piece in the entire collection. It reminds me of Brazilian contemporary art. The colors are warm and full of energy. I would describe it as a large, beautiful, contemporary abstract painting.", file: "aula5_ic_listening1_favorite_painting.mp3", voice: ELLEN },

  // ===== Listening 2 (David = Arthur) =====
  { text: "I appreciate art, but I have different tastes. I find abstract art interesting, but I prefer more subtle compositions. Look at this small painting here. The palette is cooler. Blues, grays, and soft greens. I find it very elegant. The composition is simpler than the large abstract one, but in my opinion, it has more depth. It is a beautiful old European oil painting from the nineteenth century. What strikes me is how the artist creates light with just three or four colors. Contemporary art is exciting, but sometimes I find the older pieces more refined.", file: "aula5_ic_listening2_david_preferences.mp3", voice: ARTHUR },

  // ===== Dialogue (MC + David) =====
  { text: "David, look at this painting. I find it absolutely stunning. What do you think?", file: "aula5_ic_dlg_mc_1.mp3", voice: ELLEN },
  { text: "It is very striking. The vibrant colors really catch your eye. What strikes me is the bold composition.", file: "aula5_ic_dlg_david_1.mp3", voice: ARTHUR },
  { text: "Exactly. The artist uses a warm palette. Reds, oranges, and gold. In my opinion, it is the best piece in the exhibit.", file: "aula5_ic_dlg_mc_2.mp3", voice: ELLEN },
  { text: "I can see why you like it. But I find the smaller painting over there more interesting. The one with the subtle blue tones.", file: "aula5_ic_dlg_david_2.mp3", voice: ARTHUR },
  { text: "That one? I find it elegant, but a bit too quiet for my taste. I prefer vibrant compositions.", file: "aula5_ic_dlg_mc_3.mp3", voice: ELLEN },
  { text: "That is what makes art so interesting. We all see different things. Would you describe this as contemporary or modern?", file: "aula5_ic_dlg_david_3.mp3", voice: ARTHUR },
  { text: "It is contemporary. The artist is still active. In my opinion, contemporary abstract art is the most exciting movement right now.", file: "aula5_ic_dlg_mc_4.mp3", voice: ELLEN },
  { text: "I agree it is exciting. But I also find traditional European paintings very powerful. The composition and technique are remarkable.", file: "aula5_ic_dlg_david_4.mp3", voice: ARTHUR },
  { text: "You are right. Both styles have value. What strikes me is that we can appreciate both in the same exhibit.", file: "aula5_ic_dlg_mc_5.mp3", voice: ELLEN },
  { text: "Absolutely. This has been a wonderful gallery visit. I find these conversations about art as valuable as our business meetings.", file: "aula5_ic_dlg_david_5.mp3", voice: ARTHUR },

  // ===== Error correction =====
  { text: "It is a red big painting.", file: "aula5_ic_error_red_big.mp3", voice: ARTHUR },
  { text: "I find it is very beautiful.", file: "aula5_ic_error_find_it_is.mp3", voice: ELLEN },
  { text: "She has a old European painting.", file: "aula5_ic_error_a_old.mp3", voice: ARTHUR },
  { text: "The colors is very vibrant.", file: "aula5_ic_error_colors_is.mp3", voice: ELLEN },
  { text: "In my opinion is a great exhibit.", file: "aula5_ic_error_opinion_is.mp3", voice: ARTHUR },
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
  console.log('Generating ' + unique.length + ' AULA 5 audio files...');
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
