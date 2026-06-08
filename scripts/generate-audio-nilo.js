#!/usr/bin/env node
/**
 * Generate ElevenLabs audio for Nilo Mesquita Patucci
 * Voices: Ash (male, neutral) for Nilo/male, Riley (female, neutral) for female characters
 */
const fs = require('fs');
const path = require('path');
const https = require('https');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const SLUG = 'nilo-mesquita-patucci';
const AUDIO_DIR = path.join(__dirname, '..', 'public', 'audio', SLUG);

// Voice IDs (updated Jun 2026)
const ASH = 'VU16byTywsWv5JpI8rbc';   // Male neutral
const RILEY = 'hA4zGnmTwX2NQiTRMt7o'; // Female neutral

// Create audio dir
if (!fs.existsSync(AUDIO_DIR)) fs.mkdirSync(AUDIO_DIR, { recursive: true });

// Audio entries: [text, filename, voiceId]
const entries = [
  // Survival phrases (Ash - student is male)
  ["Could you repeat that, please?", "could_you_repeat_that_please.mp3", ASH],
  ["I am not sure I understand. Could you explain?", "i_am_not_sure_i_understand_could_you_explain.mp3", ASH],
  ["Let me think about that for a moment.", "let_me_think_about_that_for_a_moment.mp3", ASH],
  ["That is a great question.", "that_is_a_great_question.mp3", ASH],
  ["In my experience, I would say...", "in_my_experience_i_would_say.mp3", ASH],
  // Vocab words (Ash - student is male)
  ["Introduce", "introduce.mp3", ASH],
  ["Represent", "represent.mp3", ASH],
  ["Oversee", "oversee.mp3", ASH],
  ["Compliance", "compliance.mp3", ASH],
  ["Governance", "governance.mp3", ASH],
  ["Background", "background.mp3", ASH],
  ["Currently", "currently.mp3", ASH],
  ["Responsible", "responsible.mp3", ASH],
  // Vocab example sentences (Ash - student protagonist)
  ["Let me introduce myself. I am Nilo Patucci, Chief Compliance Officer at Corinthians.", "let_me_introduce_myself_i_am_nilo_patucci_chief_co.mp3", ASH],
  ["I represent Brazil in the FIFA Leadership in Football program.", "i_represent_brazil_in_the_fifa_leadership_in_footb.mp3", ASH],
  ["I oversee all compliance and governance operations at the club.", "i_oversee_all_compliance_and_governance_operations.mp3", ASH],
  ["Compliance means following rules and regulations in an organization.", "compliance_means_following_rules_and_regulations_i.mp3", RILEY], // alternating
  ["Good governance is essential for the future of football.", "good_governance_is_essential_for_the_future_of_foo.mp3", ASH],
  ["My background is in law, specifically labor law and sports law.", "my_background_is_in_law_specifically_labor_law_and.mp3", ASH],
  ["I am currently preparing for the FIFA program in Miami.", "i_am_currently_preparing_for_the_fifa_program_in_m.mp3", ASH],
  ["I am responsible for the entire compliance department at Corinthians.", "i_am_responsible_for_the_entire_compliance_departm.mp3", ASH],
  // Fill-in data-phrase (Ash)
  ["Let me introduce myself at the FIFA event.", "let_me_introduce_myself_at_the_fifa_event.mp3", ASH],
  ["I represent Brazil as the only delegate in this program.", "i_represent_brazil_as_the_only_delegate_in_this_pr.mp3", ASH],
  ["I am responsible for the governance framework at the club.", "i_am_responsible_for_the_governance_framework_at_t.mp3", ASH],
  ["I oversee the compliance operations at Corinthians.", "i_oversee_the_compliance_operations_at_corinthians.mp3", ASH],
  ["My background includes fifteen years in sports law.", "my_background_includes_fifteen_years_in_sports_law.mp3", ASH],
  // Ordering
  ["Good afternoon, everyone. My name is Nilo Patucci. I am the Chief Compliance Officer at Sport Club Corinthians Paulista, and I represent Brazil in the FIFA program.", "order_l1_ordering.mp3", ASH],
  // Speech card phrases (Ash)
  ["I am Nilo Patucci, Chief Compliance Officer at Corinthians.", "i_am_nilo_patucci_chief_compliance_officer_at_cori.mp3", ASH],
  ["I have been working in sports law for over fifteen years.", "i_have_been_working_in_sports_law_for_over_fifteen.mp3", ASH],
  // Survival card lesson phrases (Ash)
  ["Let me introduce myself.", "let_me_introduce_myself.mp3", ASH],
  ["I am responsible for compliance at Corinthians.", "i_am_responsible_for_compliance_at_corinthians.mp3", ASH],
  ["I represent Brazil in the FIFA program.", "i_represent_brazil_in_the_fifa_program.mp3", ASH],
  ["I have been working in law for over fifteen years.", "i_have_been_working_in_law_for_over_fifteen_years.mp3", ASH],
  // Dialogue - Sarah (Riley)
  ["Welcome to the FIFA Leadership in Football program! I am Sarah Mitchell, the program coordinator.", "welcome_to_the_fifa_leadership_in_football_program.mp3", RILEY],
  ["Corinthians! That is impressive. What is your background in football governance?", "corinthians_that_is_impressive_what_is_your_backgr.mp3", RILEY],
  ["Fascinating! And you are the only representative from Brazil, correct?", "fascinating_and_you_are_the_only_representative_fr.mp3", RILEY],
  ["What do you hope to achieve during the program?", "what_do_you_hope_to_achieve_during_the_program.mp3", RILEY],
  // Dialogue - Nilo (Ash)
  ["Thank you! Let me introduce myself. I am Nilo Patucci, Chief Compliance Officer at Corinthians.", "thank_you_let_me_introduce_myself_i_am_nilo_patucc.mp3", ASH],
  ["I have been working in sports law for over fifteen years. I currently oversee all compliance operations at the club.", "i_have_been_working_in_sports_law_for_over_fifteen_i_c.mp3", ASH],
  ["Yes, I represent Brazil in this program. It is a great honor and responsibility.", "yes_i_represent_brazil_in_this_program_it_is_a_gre.mp3", ASH],
  ["I want to learn from the best practices in governance worldwide and bring that knowledge back to Brazilian football.", "i_want_to_learn_from_the_best_practices_in_governa.mp3", ASH],
  // Grammar examples (alternating)
  ["I work at Corinthians.", "i_work_at_corinthians.mp3", ASH],
  ["He oversees the compliance department.", "he_oversees_the_compliance_department.mp3", ASH],
  ["She represents her country at FIFA.", "she_represents_her_country_at_fifa.mp3", RILEY],
  ["I have worked in law for fifteen years.", "i_have_worked_in_law_for_fifteen_years.mp3", ASH],
  ["He has represented Brazil since 2025.", "he_has_represented_brazil_since_2025.mp3", ASH],
  ["She has overseen three major projects.", "she_has_overseen_three_major_projects.mp3", RILEY],
  // Listening 1 (Ash - student protagonist)
  ["Good afternoon, everyone. My name is Nilo Patucci. I am the Chief Compliance Officer at Sport Club Corinthians Paulista, based in Sao Paulo, Brazil. I have been working in sports law and governance for over fifteen years. I am currently the only representative from Brazil in the FIFA Leadership in Football program. My background is in labor law and sports law, and I oversee all compliance and governance operations at the club.", "listening1_self_intro.mp3", ASH],
  // Listening 2 (Riley - female character)
  ["Hello everyone, and welcome to the FIFA Leadership Program reception. My name is Dr. Rebecca Torres. I work with football associations across Latin America on governance and compliance. I have overseen regulatory reforms in three different countries. Currently, I am leading a project on anti-corruption measures in football. I am always excited to meet colleagues who share the same passion for integrity in sport.", "listening2_networking.mp3", RILEY],
];

function generateAudio(text, filename, voiceId) {
  return new Promise((resolve, reject) => {
    const filePath = path.join(AUDIO_DIR, filename);
    if (fs.existsSync(filePath) && fs.statSync(filePath).size > 1000) {
      console.log(`  SKIP (exists): ${filename}`);
      return resolve();
    }
    const body = JSON.stringify({
      text: text,
      model_id: 'eleven_turbo_v2_5',
      voice_settings: { stability: 0.5, similarity_boost: 0.75 }
    });
    const options = {
      hostname: 'api.elevenlabs.io',
      path: `/v1/text-to-speech/${voiceId}`,
      method: 'POST',
      headers: {
        'xi-api-key': API_KEY,
        'Content-Type': 'application/json',
        'Accept': 'audio/mpeg',
        'Content-Length': Buffer.byteLength(body)
      }
    };
    const req = https.request(options, (res) => {
      if (res.statusCode !== 200) {
        let errData = '';
        res.on('data', d => errData += d);
        res.on('end', () => {
          console.error(`  ERROR ${res.statusCode}: ${filename} - ${errData.substring(0,200)}`);
          reject(new Error(`HTTP ${res.statusCode}`));
        });
        return;
      }
      const chunks = [];
      res.on('data', chunk => chunks.push(chunk));
      res.on('end', () => {
        const buf = Buffer.concat(chunks);
        fs.writeFileSync(filePath, buf);
        console.log(`  OK: ${filename} (${buf.length} bytes)`);
        resolve();
      });
    });
    req.on('error', reject);
    req.write(body);
    req.end();
  });
}

async function main() {
  console.log(`Generating ${entries.length} audio files for ${SLUG}...`);
  console.log(`Audio dir: ${AUDIO_DIR}`);
  let ok = 0, err = 0;
  for (let i = 0; i < entries.length; i++) {
    const [text, filename, voice] = entries[i];
    try {
      await generateAudio(text, filename, voice);
      ok++;
      // Rate limiting: 100ms between requests
      if (i < entries.length - 1) await new Promise(r => setTimeout(r, 150));
    } catch (e) {
      err++;
      console.error(`  FAILED: ${filename} - ${e.message}`);
    }
  }
  console.log(`\nDone: ${ok} OK, ${err} errors, ${entries.length} total`);
}

main().catch(console.error);
