const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';    // Male (Diogo + Marcus)
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';     // Female (Sarah)
const DIR = path.join(__dirname, '..', 'public', 'audio', 'diogo-leal');

const PHRASES = [
  // ===== PRE-CLASS (from main file audioMap) =====

  // Vocab words (ARTHUR — male student, single words)
  { text: "Connect", voice: ARTHUR, filename: "aula5_connect" },
  { text: "Follow up", voice: ARTHUR, filename: "aula5_follow_up" },
  { text: "Opportunity", voice: ARTHUR, filename: "aula5_opportunity" },
  { text: "Collaborate", voice: ARTHUR, filename: "aula5_collaborate" },
  { text: "Valuable", voice: ARTHUR, filename: "aula5_valuable" },
  { text: "Exchange", voice: ARTHUR, filename: "aula5_exchange" },
  { text: "Introduce", voice: ARTHUR, filename: "aula5_introduce" },
  { text: "Partnership", voice: ARTHUR, filename: "aula5_partnership" },

  // Pre-class vocab example sentences (alternate ARTHUR/ELLEN)
  { text: "I connected with several IT managers at the conference.", voice: ARTHUR, filename: "aula5_pc_connect_example" },
  { text: "I will follow up with Marcus about the partnership.", voice: ELLEN, filename: "aula5_pc_followup_example" },
  { text: "This conference is a great opportunity to meet new people.", voice: ARTHUR, filename: "aula5_pc_opportunity_example" },
  { text: "Our teams could collaborate on the cloud migration.", voice: ELLEN, filename: "aula5_pc_collaborate_example" },
  { text: "The networking session was really valuable for my career.", voice: ARTHUR, filename: "aula5_pc_valuable_example" },
  { text: "We exchanged business cards at the dinner.", voice: ELLEN, filename: "aula5_pc_exchange_example" },
  { text: "Let me introduce you to my colleague from Oracle.", voice: ARTHUR, filename: "aula5_pc_introduce_example" },
  { text: "We are exploring a partnership with TechBridge Asia.", voice: ELLEN, filename: "aula5_pc_partnership_example" },

  // Pre-class fill-in-the-blank sentences (alternate)
  { text: "I have connected with several managers at this conference.", voice: ARTHUR, filename: "aula5_fill_connected" },
  { text: "She has already followed up with the new contacts.", voice: ELLEN, filename: "aula5_fill_followed" },
  { text: "We have explored a valuable partnership opportunity.", voice: ARTHUR, filename: "aula5_fill_explored" },
  { text: "I have introduced my colleague to the TechBridge team.", voice: ELLEN, filename: "aula5_fill_introduced" },
  { text: "They have exchanged ideas about the cloud migration project.", voice: ARTHUR, filename: "aula5_fill_exchanged" },

  // Speech cards / pronunciation (ARTHUR — student protagonist)
  { text: "I have connected with many professionals at this event.", voice: ARTHUR, filename: "aula5_speech_connected" },
  { text: "Have you ever collaborated with a team from another country?", voice: ARTHUR, filename: "aula5_speech_collaborated" },
  { text: "I have already followed up with Marcus about the partnership.", voice: ARTHUR, filename: "aula5_speech_followed" },
  { text: "Let me introduce you to my colleague. She has worked in cloud for five years.", voice: ARTHUR, filename: "aula5_speech_introduce" },
  { text: "This conference has been a valuable opportunity for networking.", voice: ARTHUR, filename: "aula5_speech_valuable" },

  // Survival Card (alternate ARTHUR/ELLEN)
  { text: "I have connected with professionals from five countries.", voice: ARTHUR, filename: "aula5_surv_connected" },
  { text: "Have you ever attended a tech conference abroad?", voice: ELLEN, filename: "aula5_surv_attended" },
  { text: "Let me introduce you to my colleague from Oracle.", voice: ARTHUR, filename: "aula5_surv_introduce" },
  { text: "We have exchanged ideas about a possible partnership.", voice: ELLEN, filename: "aula5_surv_exchanged" },
  { text: "I will follow up with you after the event.", voice: ARTHUR, filename: "aula5_surv_followup" },

  // Ordering audio
  { text: "I have connected with many professionals at this event. Have you ever collaborated with a team from another country? Let me introduce you to my colleague. We have exchanged ideas about a possible partnership. I will follow up with you after the event.", voice: ARTHUR, filename: "aula5_pc_order_sequence" },

  // ===== IN CLASS (from aula5 standalone audioMap) =====

  // IN CLASS vocab card examples (alternate ARTHUR/ELLEN)
  { text: "I have connected with several project managers on LinkedIn.", voice: ARTHUR, filename: "aula5_ic_connect_linkedin" },
  { text: "I always follow up with new contacts within 24 hours.", voice: ELLEN, filename: "aula5_ic_follow_up_24h" },
  { text: "This conference is a great opportunity to meet new people.", voice: ARTHUR, filename: "aula5_ic_opportunity_conference" },
  { text: "We have collaborated on cloud projects for two years.", voice: ELLEN, filename: "aula5_ic_collaborate_cloud" },
  { text: "Sarah has been a very valuable contact for our team.", voice: ARTHUR, filename: "aula5_ic_valuable_contact" },
  { text: "We have exchanged contact information after every meeting.", voice: ELLEN, filename: "aula5_ic_exchange_info" },
  { text: "Sarah has introduced me to several important contacts.", voice: ARTHUR, filename: "aula5_ic_introduce_contacts" },
  { text: "We have built a strong partnership with their engineering team.", voice: ELLEN, filename: "aula5_ic_partnership_team" },

  // IN CLASS Present Perfect examples (alternate)
  { text: "I have worked at Oracle for three years.", voice: ARTHUR, filename: "aula5_ic_pp_oracle" },
  { text: "Have you ever attended a conference in Singapore?", voice: ELLEN, filename: "aula5_ic_pp_singapore" },
  { text: "She has managed international teams since 2020.", voice: ARTHUR, filename: "aula5_ic_pp_managed" },
  { text: "We have collaborated on cloud projects for two years.", voice: ELLEN, filename: "aula5_ic_pp_collaborated" },

  // Dialogue lines — Sarah (ELLEN=female), Diogo (ARTHUR=male protagonist), Marcus (ARTHUR=male)
  { text: "Diogo! Great to see you again. I want to introduce you to someone. This is Marcus Williams, VP of Engineering at FinTech Global in London.", voice: ELLEN, filename: "aula5_ic_dlg_sarah_1" },
  { text: "Nice to meet you, Marcus! I have heard great things about FinTech Global. Have you ever worked with teams in Brazil?", voice: ARTHUR, filename: "aula5_ic_dlg_diogo_1" },
  { text: "Not yet, but we have collaborated with companies in Latin America. Sarah has mentioned your cloud projects. Sounds like a great opportunity.", voice: ARTHUR, filename: "aula5_ic_dlg_marcus_1" },
  { text: "Yes! I have worked at Oracle for three years. We have built some valuable solutions for the healthcare sector. I think our teams could collaborate.", voice: ARTHUR, filename: "aula5_ic_dlg_diogo_2" },
  { text: "That sounds excellent. We have been looking for a partnership in Brazil. Let us exchange contact information.", voice: ARTHUR, filename: "aula5_ic_dlg_marcus_2" },
  { text: "I knew you two would connect! I have introduced so many people at these events. It is the best part of networking.", voice: ELLEN, filename: "aula5_ic_dlg_sarah_2" },
  { text: "Thank you, Sarah! Marcus, I will definitely follow up with you next week. This has been a really productive evening.", voice: ARTHUR, filename: "aula5_ic_dlg_diogo_3" },
  { text: "Looking forward to it, Diogo. I have already connected with you on LinkedIn. Let us make this partnership happen!", voice: ARTHUR, filename: "aula5_ic_dlg_marcus_3" },

  // Listening 1 — Networking Event (ELLEN — narrator/female perspective)
  { text: "Hi there! I do not think we have met. I am Laura Chen. I work as a Senior Data Analyst at SecureNet Solutions. I have worked in fintech for about eight years now. What about you? Oh, you are in cloud infrastructure? That is fantastic. We have been looking for partners in data security, actually. Our team has developed some really innovative solutions for the banking sector. Have you ever collaborated with companies in Southeast Asia? We have just opened an office in Singapore. You know, I think there could be a great opportunity for us to work together. Here, let me give you my business card. I have also connected with you on LinkedIn. Let us exchange some ideas next week!", voice: ELLEN, filename: "aula5_listening_1_networking" },

  // Listening 2 — Follow-Up Call (ARTHUR — male perspective)
  { text: "Hi Laura, this is James from the networking dinner last Thursday. I am calling to follow up on our conversation about data security. I have been thinking about what you said, and I believe our teams could really collaborate on this. Have you had a chance to talk to your team about it? Oh, you have already discussed it? That is great! I have also introduced the idea to my manager, and she is very interested. She has worked with fintech companies before, so she understands the value of this kind of partnership. What do you think about scheduling a video call next week? We could exchange some preliminary ideas and see if there is a real opportunity here. Perfect. I will follow up with a calendar invite today. It was great connecting with you, Laura. Talk soon!", voice: ARTHUR, filename: "aula5_listening_2_followup" },
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
  console.log('Generating', PHRASES.length, 'audio files for Diogo Leal Aula 5...');
  console.log('Directory:', DIR);

  let generated = 0, skipped = 0, errors = 0;

  for (const phrase of PHRASES) {
    const outFile = path.join(DIR, phrase.filename + '.mp3');
    if (fs.existsSync(outFile)) {
      skipped++;
      console.log('SKIP (exists):', phrase.filename);
      continue;
    }

    await generateAudio(phrase);

    if (fs.existsSync(outFile)) {
      generated++;
    } else {
      errors++;
    }

    await new Promise(r => setTimeout(r, 300)); // Rate limit
  }

  console.log('\n========================================');
  console.log('Done! Diogo Leal Aula 5 Audio Report:');
  console.log('Total phrases:', PHRASES.length);
  console.log('Generated:', generated);
  console.log('Skipped (already existed):', skipped);
  console.log('Errors:', errors);
  console.log('========================================');
}

main();
