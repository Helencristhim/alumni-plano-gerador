const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const DIR = path.join(__dirname, '..', 'public', 'audio', 'luiz-bressane');

if (!API_KEY) { console.error('ERROR: Set ELEVENLABS_API_KEY'); process.exit(1); }
if (!fs.existsSync(DIR)) fs.mkdirSync(DIR, { recursive: true });

// Voice rules:
// - Single words (1-2 words) = ALWAYS Arthur
// - Phrases (3+ words) = ALTERNATE Arthur/Ellen
// - Dialogue: Sarah Chen (female journalist) = Ellen, Luiz (male) = Arthur
// - Listening 1 (Luiz narrating) = Arthur, Listening 2 (female narrator) = Ellen
// - [order-l2] = Arthur

const PHRASES = [
  // === VOCAB WORDS (1-2 words — ALWAYS Arthur) ===
  { text: "Prosecute", file: "aula2_prosecute.mp3", voice: ARTHUR },
  { text: "Sentence", file: "aula2_sentence.mp3", voice: ARTHUR },
  { text: "Appeal", file: "aula2_appeal.mp3", voice: ARTHUR },
  { text: "Dismiss", file: "aula2_dismiss.mp3", voice: ARTHUR },
  { text: "Witness", file: "aula2_witness.mp3", voice: ARTHUR },
  { text: "Custody", file: "aula2_custody.mp3", voice: ARTHUR },
  { text: "Bail", file: "aula2_bail.mp3", voice: ARTHUR },
  { text: "Statute", file: "aula2_statute.mp3", voice: ARTHUR },
  { text: "Allegation", file: "aula2_allegation.mp3", voice: ARTHUR },
  { text: "Indict", file: "aula2_indict.mp3", voice: ARTHUR },
  { text: "Convict", file: "aula2_convict.mp3", voice: ARTHUR },
  { text: "Circumstantial", file: "aula2_circumstantial.mp3", voice: ARTHUR },
  { text: "Mitigate", file: "aula2_mitigate.mp3", voice: ARTHUR },

  // === VOCAB EXAMPLE SENTENCES (3+ words — alternate Ellen/Arthur) ===
  { text: "The district attorney decided to prosecute the suspect for fraud.", file: "aula2_the_district_attorney_decided_to_prosecute.mp3", voice: ELLEN },
  { text: "The judge handed down a sentence of fifteen years in prison.", file: "aula2_the_judge_handed_down_a_sentence_of_fifteen.mp3", voice: ARTHUR },
  { text: "The defense filed an appeal after the guilty verdict.", file: "aula2_the_defense_filed_an_appeal_after_the_guilty.mp3", voice: ELLEN },
  { text: "The judge dismissed the case due to lack of evidence.", file: "aula2_the_judge_dismissed_the_case_due_to_lack.mp3", voice: ARTHUR },
  { text: "The key witness testified that she saw the defendant at the scene.", file: "aula2_the_key_witness_testified_that_she_saw.mp3", voice: ELLEN },
  { text: "The suspect was taken into custody after the arrest warrant was issued.", file: "aula2_the_suspect_was_taken_into_custody.mp3", voice: ARTHUR },
  { text: "The defendant posted bail and was released pending trial.", file: "aula2_the_defendant_posted_bail_and_was_released.mp3", voice: ELLEN },
  { text: "The new statute came into effect last January.", file: "aula2_the_new_statute_came_into_effect.mp3", voice: ARTHUR },
  { text: "The allegations against the company were never proven in court.", file: "aula2_the_allegations_against_the_company.mp3", voice: ELLEN },
  { text: "The grand jury voted to indict the former executive.", file: "aula2_the_grand_jury_voted_to_indict.mp3", voice: ARTHUR },
  { text: "The jury convicted the defendant on all three counts.", file: "aula2_the_jury_convicted_the_defendant.mp3", voice: ELLEN },
  { text: "The prosecution relied heavily on circumstantial evidence.", file: "aula2_the_prosecution_relied_heavily_on.mp3", voice: ARTHUR },
  { text: "The defense argued that the circumstances mitigated the severity of the crime.", file: "aula2_the_defense_argued_that_the_circumstances.mp3", voice: ELLEN },

  // === GRAMMAR IN CONTEXT SENTENCES (alternate Arthur/Ellen) ===
  { text: "The prosecution prosecuted the case aggressively, but the jury acquitted the defendant.", file: "aula2_the_prosecution_prosecuted_the_case.mp3", voice: ARTHUR },
  { text: "After the witness changed her testimony, the judge dismissed the indictment.", file: "aula2_after_the_witness_changed_her_testimony.mp3", voice: ELLEN },
  { text: "The defendant received a reduced sentence because the evidence was circumstantial.", file: "aula2_the_defendant_received_a_reduced_sentence.mp3", voice: ARTHUR },

  // === GRAMMAR PRACTICE — Past Simple vs Present Perfect (alternate Ellen/Arthur) ===
  { text: "I started my career as a legal intern in 2003.", file: "aula2_i_started_my_career_as_a_legal_intern.mp3", voice: ELLEN },
  { text: "I have prosecuted over two hundred cases since then.", file: "aula2_i_have_prosecuted_over_two_hundred_cases.mp3", voice: ARTHUR },
  { text: "Last year, the court dismissed three of my cases.", file: "aula2_last_year_the_court_dismissed_three.mp3", voice: ELLEN },
  { text: "I have worked on several high-profile indictments throughout my career.", file: "aula2_i_have_worked_on_several_high_profile.mp3", voice: ARTHUR },
  { text: "In 2018, I handled a landmark bail reform case.", file: "aula2_in_2018_i_handled_a_landmark_bail_reform.mp3", voice: ELLEN },
  { text: "I have never lost an appeal at the federal level.", file: "aula2_i_have_never_lost_an_appeal.mp3", voice: ARTHUR },
  { text: "The defendant was convicted, but we appealed the sentence successfully.", file: "aula2_the_defendant_was_convicted_but_we_appealed.mp3", voice: ELLEN },
  { text: "I represented a witness who later became a key figure in the investigation.", file: "aula2_i_represented_a_witness_who_later_became.mp3", voice: ARTHUR },

  // === DIALOGUE — Sarah Chen (female journalist) = Ellen, Luiz (male defender) = Arthur ===
  { text: "Mr. Bressane, thank you for agreeing to this interview. I am Sarah Chen, a journalist with The Atlantic.", file: "aula2_dl_sarah_intro.mp3", voice: ELLEN },
  { text: "It is my pleasure, Ms. Chen. I have been looking forward to sharing my perspective.", file: "aula2_dl_luiz_intro.mp3", voice: ARTHUR },
  { text: "When did you first become interested in criminal defense?", file: "aula2_dl_sarah_when_interested.mp3", voice: ELLEN },
  { text: "I studied law at the University of Sao Paulo and graduated in 2002. I knew from my first year that I wanted to defend people who could not afford a lawyer.", file: "aula2_dl_luiz_studied_law.mp3", voice: ARTHUR },
  { text: "What was your first major case?", file: "aula2_dl_sarah_first_case.mp3", voice: ELLEN },
  { text: "In 2005, I defended a man who was indicted for a crime he did not commit. The evidence was entirely circumstantial. We mitigated the charges, and eventually the case was dismissed.", file: "aula2_dl_luiz_first_case.mp3", voice: ARTHUR },
  { text: "That must have been a defining moment. How has that experience shaped your career?", file: "aula2_dl_sarah_defining_moment.mp3", voice: ELLEN },
  { text: "It taught me that the justice system is imperfect. Since then, I have prosecuted — well, I should say, I have defended — hundreds of clients. I have also worked to reform bail statutes in my state.", file: "aula2_dl_luiz_taught_me.mp3", voice: ARTHUR },
  { text: "Have you ever had a case where the sentence seemed unjust?", file: "aula2_dl_sarah_unjust_sentence.mp3", voice: ELLEN },
  { text: "Yes, several times. Last year, a client was convicted based on a single witness testimony. We filed an appeal, and the higher court reduced the sentence significantly.", file: "aula2_dl_luiz_unjust_sentence.mp3", voice: ARTHUR },

  // === LISTENING 1 — Luiz narrating (male) = Arthur ===
  { text: "My name is Luiz Bressane. I started working as a public defender in Sao Paulo in 2003. In my first year, I handled mostly minor custody disputes and bail hearings. In 2005, I took on a landmark case involving a wrongful indictment. The evidence was entirely circumstantial, and the judge ultimately dismissed the charges. That case changed my career. Since then, I have defended hundreds of clients and I have worked to reform bail statutes in my state. I have never stopped believing that everyone deserves a fair trial. Over the past twenty years, I have seen the justice system evolve, but there is still much work to be done.", file: "aula2_listening1_career_path.mp3", voice: ARTHUR },

  // === LISTENING 2 — Female narrator = Ellen ===
  { text: "Today we are going to hear from three legal professionals about moments that defined their careers. First, attorney Maria Santos from Rio de Janeiro. In 2010, she prosecuted a high-profile corruption case that lasted four years. The defendant was eventually convicted on all counts. Next, Judge Carlos Rivera from Buenos Aires. He dismissed a controversial indictment in 2015 after new witness testimony emerged. The allegations were dropped, and the suspect was released from custody. Finally, Professor Elena Vasquez from Madrid, who has studied how circumstantial evidence is used across different legal systems. She found that countries with strong bail reform statutes tend to have lower rates of wrongful conviction. Her research has helped mitigate sentencing disparities in several European countries.", file: "aula2_listening2_three_professionals.mp3", voice: ELLEN },

  // === IN CLASS GRAMMAR EXAMPLES (alternate Ellen/Arthur) ===
  { text: "I prosecuted my first case in 2005, and I have handled over two hundred since then.", file: "aula2_ic_past_simple_prosecuted.mp3", voice: ELLEN },
  { text: "The witness testified last week, but the jury has not reached a verdict yet.", file: "aula2_ic_past_simple_testified.mp3", voice: ARTHUR },
  { text: "The judge dismissed the indictment in March, and no one has filed an appeal since.", file: "aula2_ic_past_dismissed_no_appeal.mp3", voice: ELLEN },
  { text: "I graduated from law school in 2002, and I have been practicing ever since.", file: "aula2_ic_graduated_practicing.mp3", voice: ARTHUR },

  // === SURVIVAL IC (alternate Ellen/Arthur) ===
  { text: "The defendant posted bail yesterday and has already left the country.", file: "aula2_survival_ic_posted_bail.mp3", voice: ELLEN },
  { text: "The grand jury indicted the suspect, but the case was dismissed last month.", file: "aula2_survival_ic_indicted_dismissed.mp3", voice: ARTHUR },
  { text: "I have defended clients in over fifty custody hearings throughout my career.", file: "aula2_survival_ic_fifty_custody.mp3", voice: ELLEN },
  { text: "The witness changed her testimony, and the judge reduced the sentence.", file: "aula2_survival_ic_changed_testimony.mp3", voice: ARTHUR },
  { text: "Circumstantial evidence alone has never been enough to convict in my experience.", file: "aula2_survival_ic_circumstantial_never.mp3", voice: ELLEN },

  // === ORDER EXERCISE — narration = Arthur ===
  { text: "I started my career as a legal intern in Sao Paulo in 2003. In my first year, I handled mostly minor custody disputes. In 2005, I took on my first major case, a wrongful indictment. The evidence was entirely circumstantial, and the judge dismissed the charges. Since then, I have defended hundreds of clients. I have also worked to reform bail statutes in my state. I have never lost an appeal at the federal level. Over twenty years later, I continue to advocate for justice.", file: "aula2_order_l2_career_narration.mp3", voice: ARTHUR },
];

async function generate(text, voiceId, filePath) {
  const resp = await fetch(`https://api.elevenlabs.io/v1/text-to-speech/${voiceId}`, {
    method: 'POST',
    headers: {
      'xi-api-key': API_KEY,
      'Content-Type': 'application/json',
      'Accept': 'audio/mpeg'
    },
    body: JSON.stringify({
      text: text,
      model_id: 'eleven_multilingual_v2',
      voice_settings: { stability: 0.5, similarity_boost: 0.75 }
    })
  });
  if (!resp.ok) {
    const err = await resp.text();
    throw new Error(`ElevenLabs API error ${resp.status}: ${err}`);
  }
  const buffer = Buffer.from(await resp.arrayBuffer());
  fs.writeFileSync(filePath, buffer);
}

async function main() {
  console.log(`\n=== Generating Luiz Bressane Aula 02 B2 Audio ===`);
  console.log(`Total entries: ${PHRASES.length}\n`);

  let generated = 0, skipped = 0, failed = 0;

  for (let i = 0; i < PHRASES.length; i++) {
    const { text, file, voice } = PHRASES[i];
    const filePath = path.join(DIR, file);
    const voiceName = voice === ARTHUR ? 'Arthur' : 'Ellen';

    if (fs.existsSync(filePath) && fs.statSync(filePath).size > 0) {
      console.log(`[SKIP] ${file} (exists)`);
      skipped++;
      continue;
    }

    try {
      console.log(`[${i + 1}/${PHRASES.length}] Generating ${file} (${voiceName})...`);
      await generate(text, voice, filePath);
      generated++;
      console.log(`  ✓ OK (${fs.statSync(filePath).size} bytes)`);
    } catch (err) {
      console.error(`  ✗ FAILED: ${err.message}`);
      failed++;
    }

    // 500ms delay between requests
    if (i < PHRASES.length - 1) {
      await new Promise(r => setTimeout(r, 500));
    }
  }

  console.log(`\n=== Summary ===`);
  console.log(`Generated: ${generated}`);
  console.log(`Skipped: ${skipped}`);
  console.log(`Failed: ${failed}`);
  console.log(`Total: ${PHRASES.length}`);
}

main().catch(err => { console.error('Fatal:', err); process.exit(1); });
