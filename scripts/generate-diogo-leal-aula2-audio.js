const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const DIR = path.join(__dirname, '..', 'public', 'audio', 'diogo-leal');

const PHRASES = [
  // Vocab words (Arthur)
  { text: "Background", voice: ARTHUR, filename: "aula2_background" },
  { text: "Based", voice: ARTHUR, filename: "aula2_based" },
  { text: "Oversee", voice: ARTHUR, filename: "aula2_oversee" },
  { text: "Expertise", voice: ARTHUR, filename: "aula2_expertise" },
  { text: "Ambitious", voice: ARTHUR, filename: "aula2_ambitious" },
  { text: "Expand", voice: ARTHUR, filename: "aula2_expand" },
  { text: "Passionate", voice: ARTHUR, filename: "aula2_passionate" },
  { text: "Achieve", voice: ARTHUR, filename: "aula2_achieve" },

  // Speech card phrases (alternate)
  { text: "I am based in São Paulo and my background is in Information Technology.", voice: ARTHUR, filename: "aula2_based_saopaulo_background_it" },
  { text: "I oversee IT projects across Latin America and I am expanding into the American market.", voice: ELLEN, filename: "aula2_oversee_expanding_american_market" },
  { text: "I am passionate about technology and I want to achieve executive-level English.", voice: ARTHUR, filename: "aula2_passionate_achieve_english" },

  // Survival card (alternate)
  { text: "I am Diogo Leal. I am based in São Paulo.", voice: ARTHUR, filename: "aula2_surv_based_saopaulo" },
  { text: "My background is in Information Technology.", voice: ELLEN, filename: "aula2_surv_background_it" },
  { text: "I oversee IT projects across Latin America.", voice: ARTHUR, filename: "aula2_surv_oversee_latam" },
  { text: "I am expanding into the American market.", voice: ELLEN, filename: "aula2_surv_expanding_market" },
  { text: "I am passionate about technology and innovation.", voice: ARTHUR, filename: "aula2_surv_passionate_tech" },

  // Fill-in phrases
  { text: "I am based in São Paulo, Brazil.", voice: ELLEN, filename: "aula2_fill_based_saopaulo" },

  // Dialogue — Sarah (female) = Ellen
  { text: "Hi there! I am Sarah Mitchell, VP of Operations at Oracle. Where are you based?", voice: ELLEN, filename: "aula2_dlg_sarah_1" },
  { text: "São Paulo! What is your background?", voice: ELLEN, filename: "aula2_dlg_sarah_2" },
  { text: "That is impressive. What are you working on right now?", voice: ELLEN, filename: "aula2_dlg_sarah_3" },
  { text: "How exciting! What drives you professionally?", voice: ELLEN, filename: "aula2_dlg_sarah_4" },

  // Dialogue — Diogo (male) = Arthur
  { text: "Nice to meet you, Sarah. I am Diogo Leal. I am based in São Paulo.", voice: ARTHUR, filename: "aula2_dlg_diogo_1" },
  { text: "My background is in Information Technology. I oversee IT projects across Latin America.", voice: ARTHUR, filename: "aula2_dlg_diogo_2" },
  { text: "I am expanding our project scope to include the American market. I am also launching a new app.", voice: ARTHUR, filename: "aula2_dlg_diogo_3" },
  { text: "I am passionate about technology. My goal is to achieve a truly executive level of English.", voice: ARTHUR, filename: "aula2_dlg_diogo_4" },

  // Listening narrations (Ellen)
  { text: "Good morning, everyone. My name is Sarah Mitchell and I am the VP of Operations at Oracle Americas. I am based in Austin, Texas, but I oversee teams across the entire region. My background is in systems engineering, and I have been in the tech industry for eighteen years. I am passionate about building efficient global operations. Right now, I am expanding our partnerships with companies in Latin America.", voice: ELLEN, filename: "aula2_listening_sarah_intro" },
  { text: "Diogo Leal started his career in Information Technology over fifteen years ago. Today, he is based in São Paulo, Brazil, and oversees projects at Oracle that cover Latin America and the United States. His expertise is in project management, and he is expanding his scope to include the American market. Diogo is an ambitious professional. He is passionate about technology and innovation. Currently, he is also launching his own application for pet tutors.", voice: ELLEN, filename: "aula2_listening_executive_journey" },
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
  if (!API_KEY) { console.error('Set ELEVENLABS_API_KEY'); process.exit(1); }
  if (!fs.existsSync(DIR)) fs.mkdirSync(DIR, { recursive: true });
  console.log('Generating ' + PHRASES.length + ' audio files for Diogo Leal Aula 2...\n');
  for (const p of PHRASES) {
    const fname = p.filename + '.mp3';
    const outPath = path.join(DIR, fname);
    if (fs.existsSync(outPath)) { console.log('SKIP: ' + fname); continue; }
    try {
      const bytes = await gen(p.text, p.voice, outPath);
      console.log('OK [' + (p.voice === ELLEN ? 'ellen' : 'arthur') + ']: ' + fname + ' (' + (bytes / 1024).toFixed(1) + 'KB)');
      await new Promise(r => setTimeout(r, 500));
    } catch (e) { console.error('FAIL: ' + fname + ' — ' + e.message); }
  }
  console.log('\nDone!');
}
main().catch(e => { console.error(e); process.exit(1); });
