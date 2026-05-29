const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const MODEL = 'eleven_multilingual_v2';
const DIR = path.join(__dirname, '..', 'public', 'audio', 'luiz-bressane');

if (!API_KEY) {
  console.error('ERROR: Set ELEVENLABS_API_KEY environment variable');
  process.exit(1);
}

if (!fs.existsSync(DIR)) fs.mkdirSync(DIR, { recursive: true });

// Voice assignment rules:
// - Single words (1-2 words) = Arthur
// - Phrases alternate Arthur/Ellen
// - Dialogue: Professor Crawford (male) = Arthur, Luiz = Ellen
// - Listening passages alternate
// - [order-l3] = Arthur
let phraseVoiceToggle = 0; // 0=Arthur, 1=Ellen for alternation

const PHRASES = [
  // === VOCAB WORDS (single words = Arthur) ===
  { text: "Plaintiff", voice: ARTHUR, file: "aula3_plaintiff.mp3" },
  { text: "Defendant", voice: ARTHUR, file: "aula3_defendant.mp3" },
  { text: "Judiciary", voice: ARTHUR, file: "aula3_judiciary.mp3" },
  { text: "Tort", voice: ARTHUR, file: "aula3_tort.mp3" },
  { text: "Liable", voice: ARTHUR, file: "aula3_liable.mp3" },
  { text: "Statutory", voice: ARTHUR, file: "aula3_statutory.mp3" },
  { text: "Amend", voice: ARTHUR, file: "aula3_amend.mp3" },
  { text: "Extradite", voice: ARTHUR, file: "aula3_extradite.mp3" },
  { text: "Arbitration", voice: ARTHUR, file: "aula3_arbitration.mp3" },
  { text: "Codify", voice: ARTHUR, file: "aula3_codify.mp3" },
  { text: "Common law", voice: ARTHUR, file: "aula3_common_law.mp3" },
  { text: "Habeas corpus", voice: ARTHUR, file: "aula3_habeas_corpus.mp3" },
  { text: "Sovereignty", voice: ARTHUR, file: "aula3_sovereignty.mp3" },

  // === VOCAB EXAMPLE SENTENCES (alternate Arthur/Ellen) ===
  { text: "The plaintiff filed a lawsuit against the manufacturer for damages.", voice: ARTHUR, file: "aula3_the_plaintiff_filed_a_lawsuit.mp3" },
  { text: "The defendant denied all charges and entered a plea of not guilty.", voice: ELLEN, file: "aula3_the_defendant_denied_all_charges.mp3" },
  { text: "An independent judiciary is essential for a functioning democracy.", voice: ARTHUR, file: "aula3_an_independent_judiciary_is_essential.mp3" },
  { text: "A tort is a civil wrong that causes harm to another person.", voice: ELLEN, file: "aula3_a_tort_is_a_civil_wrong.mp3" },
  { text: "The company was found liable for the environmental damage.", voice: ARTHUR, file: "aula3_the_company_was_found_liable.mp3" },
  { text: "The statutory age for voting is eighteen in most countries.", voice: ELLEN, file: "aula3_the_statutory_age_for_voting.mp3" },
  { text: "Congress voted to amend the constitution to protect civil rights.", voice: ARTHUR, file: "aula3_congress_voted_to_amend.mp3" },
  { text: "The government agreed to extradite the suspect to face trial abroad.", voice: ELLEN, file: "aula3_the_government_agreed_to_extradite.mp3" },
  { text: "The two companies resolved their dispute through arbitration.", voice: ARTHUR, file: "aula3_the_two_companies_resolved.mp3" },
  { text: "Napoleon was the first to codify French law into a unified system.", voice: ELLEN, file: "aula3_napoleon_was_the_first_to_codify.mp3" },
  { text: "Common law relies on judicial precedent rather than written statutes.", voice: ARTHUR, file: "aula3_common_law_relies_on_judicial.mp3" },
  { text: "The lawyer filed a habeas corpus petition to challenge the detention.", voice: ELLEN, file: "aula3_the_lawyer_filed_a_habeas_corpus.mp3" },
  { text: "National sovereignty means a state has the right to govern itself.", voice: ARTHUR, file: "aula3_national_sovereignty_means_a_state.mp3" },

  // === GRAMMAR IN CONTEXT - Relative clauses (alternate) ===
  { text: "In common law systems, which rely on judicial precedent, courts play a central role in shaping the law.", voice: ELLEN, file: "aula3_in_common_law_systems_which_rely.mp3" },
  { text: "In civil law countries, where statutes are codified into comprehensive codes, the judiciary interprets the written law.", voice: ARTHUR, file: "aula3_in_civil_law_countries_where_statutes.mp3" },
  { text: "Judges who serve on constitutional courts have the power to review legislation.", voice: ELLEN, file: "aula3_judges_who_serve_on_constitutional.mp3" },
  { text: "Arbitration, which is a popular alternative to litigation, helps resolve disputes efficiently.", voice: ARTHUR, file: "aula3_arbitration_which_is_a_popular.mp3" },

  // === DIALOGUE: Professor Crawford (male) = Arthur, Luiz = Ellen ===
  { text: "Good afternoon, everyone. Welcome to the comparative law panel at the Washington symposium.", voice: ARTHUR, file: "aula3_dl_crawford_welcome.mp3" },
  { text: "Thank you, Professor Crawford. It is an honor to be part of this discussion.", voice: ELLEN, file: "aula3_dl_luiz_honor.mp3" },
  { text: "In the United States, which follows a common law tradition, judges rely heavily on precedent.", voice: ARTHUR, file: "aula3_dl_crawford_common_law.mp3" },
  { text: "That is interesting. In Brazil, where the legal system is based on codified statutes, the role of the judiciary is different.", voice: ELLEN, file: "aula3_dl_luiz_brazil_codified.mp3" },
  { text: "Can you explain how tort law works in Brazil?", voice: ARTHUR, file: "aula3_dl_crawford_tort_law.mp3" },
  { text: "Of course. In Brazilian civil law, a plaintiff who suffers harm can file a claim, and the defendant may be found liable under statutory provisions.", voice: ELLEN, file: "aula3_dl_luiz_tort_brazil.mp3" },
  { text: "Here in the US, common law torts have evolved through judicial decisions rather than codified rules.", voice: ARTHUR, file: "aula3_dl_crawford_us_torts.mp3" },
  { text: "One area where our systems converge is arbitration, which has become increasingly popular in both countries.", voice: ELLEN, file: "aula3_dl_luiz_arbitration.mp3" },
  { text: "Absolutely. And what about habeas corpus? How does it function in the Brazilian system?", voice: ARTHUR, file: "aula3_dl_crawford_habeas.mp3" },
  { text: "Habeas corpus, which is guaranteed by our constitution, protects individuals from unlawful detention. It is a fundamental safeguard of sovereignty and individual rights.", voice: ELLEN, file: "aula3_dl_luiz_habeas_brazil.mp3" },

  // === LISTENING 1 (long passage - Arthur) ===
  { text: "Comparative law is a field that examines different legal systems around the world. In this talk, I will compare common law and civil law traditions. Common law, which originated in England, relies on judicial precedent. Judges who hear cases create binding decisions that future courts must follow. Civil law, which is found in most of continental Europe and Latin America, is based on codified statutes. The judiciary in civil law countries interprets the written code rather than creating new law. One key difference involves tort law. In common law systems, tort liability has evolved through case law. In civil law systems, liability is defined by statutory provisions. Both systems use arbitration, which is a method of resolving disputes outside of court. Countries that value sovereignty often resist extraditing suspects to foreign jurisdictions. However, habeas corpus, which protects individuals from unlawful detention, exists in both traditions.", voice: ARTHUR, file: "aula3_listening1_comparative_law.mp3" },

  // === LISTENING 2 (long passage - Ellen) ===
  { text: "Today we will discuss how legal systems around the world have been amended and reformed over time. Professor Maria Torres from Madrid studies civil law reform in Spain. She has found that codifying new statutes is a complex process that requires balancing sovereignty with international obligations. Dr. James Okafor from Lagos examines how common law has been adapted in African countries. In Nigeria, which inherited its legal system from Britain, judges who sit on the Supreme Court often face tension between customary law and statutory law. Finally, attorney Yuki Tanaka from Tokyo has researched arbitration as an alternative to litigation in Japan. She found that plaintiffs who choose arbitration resolve disputes faster than those who go through the courts. The defendant in an arbitration case is more likely to accept a settlement, which reduces the burden on the judiciary.", voice: ELLEN, file: "aula3_listening2_global_reform.mp3" },

  // === IN CLASS grammar examples (alternate) ===
  { text: "In common law systems, which originated in England, courts rely on judicial precedent.", voice: ARTHUR, file: "aula3_ic_rel_clause_common_law.mp3" },
  { text: "A plaintiff who suffers harm can file a tort claim against the defendant.", voice: ELLEN, file: "aula3_ic_rel_clause_plaintiff.mp3" },
  { text: "Arbitration, which is growing in popularity, offers an alternative to traditional litigation.", voice: ARTHUR, file: "aula3_ic_rel_clause_arbitration.mp3" },
  { text: "Countries that codify their laws into comprehensive codes follow the civil law tradition.", voice: ELLEN, file: "aula3_ic_rel_clause_codify.mp3" },

  // === SURVIVAL IC (alternate) ===
  { text: "The judiciary, which interprets the law, plays a crucial role in both systems.", voice: ARTHUR, file: "aula3_survival_ic_judiciary.mp3" },
  { text: "A tort is a wrongful act for which the responsible party may be held liable.", voice: ELLEN, file: "aula3_survival_ic_tort_liable.mp3" },
  { text: "The government refused to extradite the suspect, citing national sovereignty.", voice: ARTHUR, file: "aula3_survival_ic_extradite_sovereignty.mp3" },
  { text: "Habeas corpus protects individuals who are unlawfully detained by the state.", voice: ELLEN, file: "aula3_survival_ic_habeas_corpus.mp3" },
  { text: "Both countries have amended their constitutions to include statutory protections for civil rights.", voice: ARTHUR, file: "aula3_survival_ic_amended_statutory.mp3" },

  // === ORDER (Arthur) ===
  { text: "The comparative law panel began with a discussion of common law and civil law traditions. Professor Crawford explained that in common law systems, which originated in England, courts rely on judicial precedent. Luiz Bressane then described how Brazilian law is based on codified statutes. They discussed tort law, arbitration, and habeas corpus. Both speakers agreed that understanding different legal systems is essential for international cooperation.", voice: ARTHUR, file: "aula3_order_l3_legal_systems.mp3" },
];

async function generateAudio(text, voiceId, outputPath) {
  const resp = await fetch(`https://api.elevenlabs.io/v1/text-to-speech/${voiceId}`, {
    method: 'POST',
    headers: {
      'Accept': 'audio/mpeg',
      'Content-Type': 'application/json',
      'xi-api-key': API_KEY,
    },
    body: JSON.stringify({
      text: text,
      model_id: MODEL,
      voice_settings: { stability: 0.5, similarity_boost: 0.75 },
    }),
  });

  if (!resp.ok) {
    const errText = await resp.text();
    throw new Error(`ElevenLabs API error ${resp.status}: ${errText}`);
  }

  const buffer = Buffer.from(await resp.arrayBuffer());
  fs.writeFileSync(outputPath, buffer);
  return buffer.length;
}

async function main() {
  console.log(`Generating ${PHRASES.length} audio files for Luiz Bressane Aula 03 (B2)...`);
  console.log(`Output: ${DIR}\n`);

  let generated = 0;
  let skipped = 0;
  let failed = 0;

  for (let i = 0; i < PHRASES.length; i++) {
    const p = PHRASES[i];
    const outputPath = path.join(DIR, p.file);

    if (fs.existsSync(outputPath)) {
      const stat = fs.statSync(outputPath);
      if (stat.size > 1000) {
        console.log(`[${i + 1}/${PHRASES.length}] SKIP (exists): ${p.file}`);
        skipped++;
        continue;
      }
    }

    const voiceName = p.voice === ARTHUR ? 'Arthur' : 'Ellen';
    console.log(`[${i + 1}/${PHRASES.length}] Generating (${voiceName}): ${p.file}`);

    try {
      const size = await generateAudio(p.text, p.voice, outputPath);
      console.log(`  -> OK (${(size / 1024).toFixed(1)} KB)`);
      generated++;
    } catch (err) {
      console.error(`  -> FAILED: ${err.message}`);
      failed++;
    }

    // 500ms delay between requests
    if (i < PHRASES.length - 1) {
      await new Promise(r => setTimeout(r, 500));
    }
  }

  console.log(`\n=== SUMMARY ===`);
  console.log(`Generated: ${generated}`);
  console.log(`Skipped: ${skipped}`);
  console.log(`Failed: ${failed}`);
  console.log(`Total entries: ${PHRASES.length}`);
}

main().catch(err => {
  console.error('Fatal error:', err);
  process.exit(1);
});
