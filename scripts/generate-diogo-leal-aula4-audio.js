const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ASH = 'sfJopaWaOtauCD3HKX6Q';    // Arthur — Male (Diogo = male student)
const RILEY = 'BIvP0GN1cAtSRTxNHnWS';   // Ellen — Female (Sarah = female character)
const DIR = path.join(__dirname, '..', 'public', 'audio', 'diogo-leal');

const PHRASES = [
  // Vocab words (Ash — male student, single words)
  { text: "Colleague", voice: ASH, filename: "aula4_colleague" },
  { text: "Conference", voice: ASH, filename: "aula4_conference" },
  { text: "Recommend", voice: ASH, filename: "aula4_recommend" },
  { text: "Mention", voice: ASH, filename: "aula4_mention" },
  { text: "Nowadays", voice: ASH, filename: "aula4_nowadays" },
  { text: "Industry", voice: ASH, filename: "aula4_industry" },
  { text: "Networking", voice: ASH, filename: "aula4_networking" },
  { text: "Impressed", voice: ASH, filename: "aula4_impressed" },

  // IN CLASS vocab card examples (alternate Ash/Riley)
  { text: "I introduced my colleague to the speaker after the presentation.", voice: ASH, filename: "aula4_ic_colleague_intro" },
  { text: "I am attending a tech conference in São Paulo next week.", voice: RILEY, filename: "aula4_ic_conference_sp" },
  { text: "I recommend the keynote session on cloud computing.", voice: ASH, filename: "aula4_ic_recommend_keynote" },
  { text: "She mentioned that the next conference is in Singapore.", voice: RILEY, filename: "aula4_ic_mention_singapore" },
  { text: "Nowadays, most conferences have a virtual option too.", voice: ASH, filename: "aula4_ic_nowadays_virtual" },
  { text: "The tech industry is growing very fast in Brazil.", voice: RILEY, filename: "aula4_ic_industry_brazil" },
  { text: "The coffee break is the best time for networking.", voice: ASH, filename: "aula4_ic_networking_coffee" },
  { text: "I was really impressed by the keynote speaker.", voice: RILEY, filename: "aula4_ic_impressed_keynote" },

  // Question formation examples (alternate)
  { text: "Do you work in tech?", voice: ASH, filename: "aula4_ic_question_tech" },
  { text: "What do you do at Oracle?", voice: RILEY, filename: "aula4_ic_question_oracle" },
  { text: "How long have you been in this industry?", voice: ASH, filename: "aula4_ic_question_howlong" },
  { text: "Where are you from?", voice: RILEY, filename: "aula4_ic_question_wherefrom" },

  // Dialogue lines — Diogo (Ash=male protagonist), Sarah (Riley=female character)
  { text: "Hi! Great conference, right? I am Diogo. I work at Oracle here in São Paulo.", voice: ASH, filename: "aula4_ic_dlg_diogo_1" },
  { text: "Nice to meet you, Diogo! I am Sarah. I am the CTO at TechBridge Asia in Singapore. Do you work in tech?", voice: RILEY, filename: "aula4_ic_dlg_sarah_1" },
  { text: "Yes, I am an IT Project Manager. What do you do at TechBridge?", voice: ASH, filename: "aula4_ic_dlg_diogo_2" },
  { text: "I lead the engineering team. We build cloud solutions for the healthcare industry. How long have you been at Oracle?", voice: RILEY, filename: "aula4_ic_dlg_sarah_2" },
  { text: "About three years. I really like the networking events like this one. Where are you from originally?", voice: ASH, filename: "aula4_ic_dlg_diogo_3" },
  { text: "I am from Taipei, but I live in Singapore nowadays. I am really impressed by the tech scene in Brazil!", voice: RILEY, filename: "aula4_ic_dlg_sarah_3" },
  { text: "Thank you! Do you recommend any sessions this afternoon?", voice: ASH, filename: "aula4_ic_dlg_diogo_4" },
  { text: "Yes! A colleague of mine mentioned the AI panel at two. Let me add you on LinkedIn!", voice: RILEY, filename: "aula4_ic_dlg_sarah_4" },

  // Pre-class vocab example sentences (alternate)
  { text: "I have a colleague from Singapore who works in cybersecurity.", voice: ASH, filename: "aula4_pc_colleague_example" },
  { text: "I am attending a tech conference in São Paulo next month.", voice: RILEY, filename: "aula4_pc_conference_example" },
  { text: "Can you recommend a good restaurant nearby?", voice: ASH, filename: "aula4_pc_recommend_example" },
  { text: "She mentioned that Oracle is expanding in Latin America.", voice: RILEY, filename: "aula4_pc_mention_example" },
  { text: "Nowadays, most conferences have a virtual option.", voice: ASH, filename: "aula4_pc_nowadays_example" },
  { text: "The tech industry is growing fast in Brazil.", voice: RILEY, filename: "aula4_pc_industry_example" },
  { text: "Networking at conferences is important for your career.", voice: ASH, filename: "aula4_pc_networking_example" },
  { text: "I am really impressed by your presentation.", voice: RILEY, filename: "aula4_pc_impressed_example" },

  // Pre-class fill-in-the-blank phrases (alternate)
  { text: "Do you have a colleague who works in the same industry?", voice: ASH, filename: "aula4_pc_fill_colleague" },
  { text: "What conference are you attending next month?", voice: RILEY, filename: "aula4_pc_fill_conference" },
  { text: "Can you recommend a good session for me?", voice: ASH, filename: "aula4_pc_fill_recommend" },
  { text: "She mentioned that the deadline is next Friday.", voice: RILEY, filename: "aula4_pc_fill_mention" },
  { text: "How long have you been in the tech industry?", voice: ASH, filename: "aula4_pc_fill_industry" },

  // Speech cards / pronunciation (Ash — student protagonist)
  { text: "Hi, I am Diogo. I work at Oracle as an IT Project Manager.", voice: ASH, filename: "aula4_pc_speech_intro" },
  { text: "What do you do? How long have you been in this industry?", voice: ASH, filename: "aula4_pc_speech_questions" },
  { text: "I am really impressed by your presentation. Can you recommend any sessions?", voice: ASH, filename: "aula4_pc_speech_impressed" },
  { text: "A colleague mentioned this conference. The networking has been great.", voice: ASH, filename: "aula4_pc_speech_colleague" },
  { text: "Nowadays, most companies use cloud solutions. Do you work in tech?", voice: ASH, filename: "aula4_pc_speech_nowadays" },

  // Survival Card (alternate Ash/Riley)
  { text: "What brings you to this conference?", voice: ASH, filename: "aula4_pc_surv_brings" },
  { text: "How long have you been in this industry?", voice: RILEY, filename: "aula4_pc_surv_howlong" },
  { text: "Can you recommend any good sessions?", voice: ASH, filename: "aula4_pc_surv_recommend" },
  { text: "A colleague mentioned your company. I am impressed!", voice: RILEY, filename: "aula4_pc_surv_colleague" },
  { text: "It was great networking with you. Let me add you on LinkedIn.", voice: ASH, filename: "aula4_pc_surv_linkedin" },

  // Listening 1 — Conference networking (full audio, ~90 seconds)
  { text: "Welcome back from the coffee break, everyone. Before we start the next panel, I want to remind you that the networking lounge is open until six PM. This is a great opportunity to connect with colleagues from different industries. Many of you have mentioned that you are impressed by the presentations today. If you want to recommend a session to a colleague, check the conference app. Nowadays, we also have a virtual networking room for online participants. Thank you, and enjoy the rest of the conference!", voice: RILEY, filename: "aula4_listening_1_conference" },

  // Listening 2 — Office kitchen small talk (full audio, ~60 seconds)
  { text: "Hey, are you new here? I do not think we have met. I am Mark from the marketing team. What do you do? Oh, you are in IT? That is great. How long have you been at Oracle? I have been here for about two years now. Do you recommend the coffee here, or should I walk to the cafe downstairs? By the way, a colleague mentioned that there is a team event next Friday. Are you going?", voice: ASH, filename: "aula4_listening_2_office" },

  // Ordering audio
  { text: "Hi, nice to meet you. What do you do? I work at Oracle as a project manager. How long have you been in this industry? It was great talking to you.", voice: ASH, filename: "aula4_pc_order_sequence" },
];

if (!fs.existsSync(DIR)) fs.mkdirSync(DIR, { recursive: true });

async function generateAudio(phrase) {
  const outFile = path.join(DIR, phrase.filename + '.mp3');
  if (fs.existsSync(outFile)) {
    console.log('SKIP (exists):', phrase.filename);
    return;
  }
  console.log('Generating:', phrase.filename, '(' + phrase.text.substring(0, 50) + '...)');

  try {
    const res = await fetch('https://api.elevenlabs.io/v1/text-to-speech/' + phrase.voice, {
      method: 'POST',
      headers: {
        'xi-api-key': API_KEY,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        text: phrase.text,
        model_id: 'eleven_turbo_v2_5',
        voice_settings: { stability: 0.5, similarity_boost: 0.75, style: 0.0, use_speaker_boost: true }
      })
    });

    if (!res.ok) {
      const err = await res.text();
      console.error('ERROR:', phrase.filename, res.status, err);
      return;
    }

    const buffer = Buffer.from(await res.arrayBuffer());
    fs.writeFileSync(outFile, buffer);
    console.log('OK:', phrase.filename, '(' + buffer.length + ' bytes)');
  } catch (e) {
    console.error('CATCH:', phrase.filename, e.message);
  }
}

async function main() {
  console.log('Generating', PHRASES.length, 'audio files for Diogo Leal Aula 4...');
  console.log('Directory:', DIR);

  for (const phrase of PHRASES) {
    await generateAudio(phrase);
    await new Promise(r => setTimeout(r, 300)); // Rate limit
  }

  console.log('\nDone! Generated audio for Aula 4.');
}

main();
