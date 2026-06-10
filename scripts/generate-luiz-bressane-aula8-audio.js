const fs = require('fs');
const path = require('path');
const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const DIR = path.join(__dirname, '..', 'public', 'audio', 'luiz-bressane');

const PHRASES = [
  // =========================================================
  // === PRE-CLASS: Example sentences (alternating Arthur/Ellen)
  // =========================================================
  { text: "The ruling set a precedent that changed how courts handle similar cases.", voice: ARTHUR, filename: "aula8_ex_precedent" },
  { text: "The defense attorney's cross-examination revealed several inconsistencies.", voice: ELLEN, filename: "aula8_ex_cross_examination" },
  { text: "The allegations against the official were never proven in court.", voice: ARTHUR, filename: "aula8_ex_allegation" },
  { text: "The suspect was taken into custody pending a bail hearing.", voice: ELLEN, filename: "aula8_ex_custody" },
  { text: "The plaintiff filed a tort claim for damages caused by negligence.", voice: ARTHUR, filename: "aula8_ex_tort" },
  { text: "Each nation's sovereignty must be respected in international agreements.", voice: ELLEN, filename: "aula8_ex_sovereignty" },
  { text: "Mandatory minimum sentences are intended to serve as a deterrent.", voice: ARTHUR, filename: "aula8_ex_deterrent" },
  { text: "The firm was fined for failure to maintain regulatory compliance.", voice: ELLEN, filename: "aula8_ex_compliance" },
  { text: "The witness was charged with perjury after contradicting her sworn statement.", voice: ARTHUR, filename: "aula8_ex_perjury" },
  { text: "The court ordered full restitution to the victims of the fraud.", voice: ELLEN, filename: "aula8_ex_restitution" },
  { text: "Accountability within the judiciary is essential for maintaining public trust.", voice: ARTHUR, filename: "aula8_ex_accountability" },
  { text: "The attorney took the witness's deposition two weeks before the trial.", voice: ELLEN, filename: "aula8_ex_deposition" },

  // =========================================================
  // === PRE-CLASS: Grammar in Context sentences
  // =========================================================
  { text: "Throughout my career, I have handled cases involving precedent-setting rulings, and I have been advocating for greater accountability in the system.", voice: ARTHUR, filename: "aula8_gc1_pres_perf" },
  { text: "A judge who fails to ensure compliance with due process undermines the sovereignty of the legal system.", voice: ELLEN, filename: "aula8_gc2_relative" },
  { text: "If the court imposed harsher penalties for perjury, witnesses would think twice before lying under oath.", voice: ARTHUR, filename: "aula8_gc3_second_cond" },
  { text: "If the prosecution had secured the deposition earlier, the case would not have been dismissed.", voice: ELLEN, filename: "aula8_gc4_third_cond" },
  { text: "If accountability were built into every institution, fewer wrongful convictions would have occurred.", voice: ARTHUR, filename: "aula8_gc5_mixed_cond" },
  { text: "The witness was giving her deposition when the defense attorney interrupted with a cross-examination request.", voice: ELLEN, filename: "aula8_gc6_narrative" },

  // =========================================================
  // === PRE-CLASS: Fill-in-the-blank sentences
  // =========================================================
  { text: "I have been working on precedent-setting cases for over twenty years.", voice: ARTHUR, filename: "aula8_fill1" },
  { text: "The investigation, which uncovered multiple allegations, led to a landmark tort case.", voice: ELLEN, filename: "aula8_fill2" },
  { text: "If the state had provided restitution sooner, the victims would not be suffering today.", voice: ARTHUR, filename: "aula8_fill3" },
  { text: "If compliance were mandatory for all institutions, fewer cases of negligence would occur.", voice: ELLEN, filename: "aula8_fill4" },
  { text: "The detective had already taken the deposition before the suspect was taken into custody.", voice: ARTHUR, filename: "aula8_fill5" },
  { text: "She was reviewing the allegations when the judge called for a recess.", voice: ELLEN, filename: "aula8_fill6" },

  // =========================================================
  // === PRE-CLASS: Ordering exercise phrases
  // =========================================================
  { text: "The ruling set a precedent for how courts handle allegations of perjury.", voice: ARTHUR, filename: "aula8_order_phrase1" },
  { text: "If accountability had been enforced from the start, the system would be more just today.", voice: ELLEN, filename: "aula8_order_phrase2" },

  // =========================================================
  // === PRE-CLASS: Speech/pronunciation practice
  // =========================================================
  { text: "Cross-examination is a fundamental tool that every defense attorney must master.", voice: ARTHUR, filename: "aula8_speech1" },
  { text: "The court ordered restitution because the defendant had caused significant financial harm.", voice: ELLEN, filename: "aula8_speech2" },
  { text: "If sovereignty were not protected by international law, smaller nations would be vulnerable to exploitation.", voice: ARTHUR, filename: "aula8_speech3" },
  { text: "The witness had given a sworn deposition, but during cross-examination, she contradicted her earlier account.", voice: ELLEN, filename: "aula8_speech4" },
  { text: "If the deterrent had been stronger, the crime rate would have decreased.", voice: ARTHUR, filename: "aula8_speech5" },

  // =========================================================
  // === PRE-CLASS: Survival Card phrases
  // =========================================================
  { text: "Throughout my career, I have handled cases that set important precedents for accountability in the justice system.", voice: ELLEN, filename: "aula8_survival1" },
  { text: "If compliance with due process had been ensured, the tort claim would never have been filed.", voice: ARTHUR, filename: "aula8_survival2" },
  { text: "The witness was taken into custody after the court discovered she had committed perjury.", voice: ELLEN, filename: "aula8_survival3" },
  { text: "If restitution were always proportional to the harm caused, the system would be more equitable.", voice: ARTHUR, filename: "aula8_survival4" },
  { text: "The deposition, which corroborated the allegations, proved to be the turning point of the case.", voice: ELLEN, filename: "aula8_survival5" },

  // =========================================================
  // === PRE-CLASS: Ordering exercise summary audio
  // =========================================================
  { text: "Luiz reviews vocabulary from all eight lessons. He discusses precedent, cross-examination, allegations, custody, tort, sovereignty, deterrent, compliance, perjury, restitution, accountability, and deposition. He demonstrates grammar structures including present perfect, relative clauses, second conditional, third conditional, mixed conditional, and narrative tenses.", voice: ARTHUR, filename: "order_l8_ordering" },

  // =========================================================
  // === IN CLASS: Dialogue Part 1 — Luiz (Arthur) + Dr. Obi (Ellen)
  // =========================================================
  { text: "Dr. Obi, I have admired your work on international human rights law for years. It is a privilege to share this panel with you.", voice: ARTHUR, filename: "aula8_dl_luiz_greeting" },
  { text: "Thank you, Luiz. I have been researching comparative legal systems, and the work that public defenders do in Brazil is truly remarkable.", voice: ELLEN, filename: "aula8_dl_obi_response" },
  { text: "If our legal system had adopted restorative practices earlier, many communities would be in a much better position today.", voice: ARTHUR, filename: "aula8_dl_luiz_restorative" },
  { text: "Absolutely. In Nigeria, which has a dual legal system, we have been experimenting with community courts that prioritize reconciliation over punishment.", voice: ELLEN, filename: "aula8_dl_obi_nigeria" },

  // === IN CLASS: Dialogue Part 2 ===
  { text: "I remember a case last year. I was preparing the defense when new evidence emerged. The witness had given a contradictory deposition, which completely changed the direction of the trial.", voice: ARTHUR, filename: "aula8_dl_luiz_case" },
  { text: "That is fascinating. If every jurisdiction were to adopt mandatory deposition review protocols, cases like that would be resolved much more efficiently.", voice: ELLEN, filename: "aula8_dl_obi_deposition" },
  { text: "I agree. The precedent that case set has influenced how our office handles similar situations. We have been training younger defenders to identify inconsistencies early.", voice: ARTHUR, filename: "aula8_dl_luiz_precedent" },
  { text: "That is exactly the kind of systemic change we need. The right to equity, which is inalienable, must be at the center of every legal reform.", voice: ELLEN, filename: "aula8_dl_obi_equity" },

  // =========================================================
  // === IN CLASS: Survival Card (slide 278) — alternating
  // =========================================================
  { text: "I have worked as a public defender since 2010.", voice: ARTHUR, filename: "aula8_survival_ic1" },
  { text: "If the reform had passed, the system would be more equitable today.", voice: ELLEN, filename: "aula8_survival_ic2" },
  { text: "The judge, who has served for over 30 years, announced her retirement.", voice: ARTHUR, filename: "aula8_survival_ic3" },
  { text: "While I was reviewing the case, new evidence emerged.", voice: ELLEN, filename: "aula8_survival_ic4" },
  { text: "If I were to redesign the legal system, I would prioritize equity above all else.", voice: ARTHUR, filename: "aula8_survival_ic5" },

  // =========================================================
  // === IN CLASS: Listening 1 — Luiz's Conference Keynote Speech (Arthur — long passage)
  // =========================================================
  { text: "Distinguished colleagues, thank you for this opportunity to address the Global Legal Reform Summit. Throughout my career as a public defender in Brazil, I have handled hundreds of cases involving precedent-setting rulings, and I have been advocating for greater accountability in the criminal justice system for over twenty years. Today, I want to share three reflections with you. First, the question of precedent. A single ruling can change how courts handle thousands of similar cases. The precedent we set in State versus Almeida in 2019 transformed how Brazilian courts evaluate cross-examination evidence. The defense attorney's cross-examination in that case revealed inconsistencies that had been overlooked for decades. Second, I want to discuss the role of compliance and due process. A judge who fails to ensure compliance with due process undermines the sovereignty of the legal system itself. I have seen cases where the prosecution had secured a deposition, but because proper protocols were not followed, the evidence was inadmissible. If accountability were built into every institution from the beginning, fewer wrongful convictions would have occurred. Third, let me address deterrence and restitution. If the court imposed harsher penalties for perjury, witnesses would think twice before lying under oath. But punishment alone is not enough. The court must also ensure full restitution to victims. If the state had provided restitution sooner in many of the cases I have worked on, the victims would not still be suffering today. I was preparing my closing arguments in a major case last year when new allegations emerged. The witness was giving her deposition when the defense attorney interrupted with a cross-examination request that changed everything. These are the moments that define our profession. Thank you.", voice: ARTHUR, filename: "aula8_listening1_luiz_conference_speech" },

  // =========================================================
  // === IN CLASS: Listening 2 — Panel Discussion (Ellen — long passage)
  // =========================================================
  { text: "Welcome to the afternoon panel discussion on comparative legal reform. Our three panelists bring diverse perspectives from across the globe. Dr. Amara Obi from the University of Lagos opened by noting that in countries which have adopted restorative justice frameworks, recidivism rates have dropped significantly. She has been researching the intersection of traditional African dispute resolution and modern legal systems for over fifteen years. She argued that if sovereignty were not protected by international law, smaller nations would be vulnerable to having their legal traditions overwritten by colonial frameworks. Professor James Crawford from Georgetown University followed with an analysis of precedent in common law systems. He noted that cross-examination, which is a fundamental tool in adversarial systems, is often misused or poorly understood. If compliance with due process had been ensured in several landmark American cases, the tort claims that followed would never have been filed. He emphasized that accountability within the judiciary is essential for maintaining public trust, and that if the deterrent for judicial misconduct had been stronger, public confidence in the courts would be higher today. Finally, Luiz Bressane, a public defender from Brazil, shared his experience with a case that set a precedent for how courts handle allegations of perjury. He described how the witness had given a sworn deposition, but during cross-examination, she contradicted her earlier account. The case resulted in full restitution to the victims and led to new protocols for deposition review. All three panelists agreed that if accountability had been enforced from the start, the global justice system would be more equitable today.", voice: ELLEN, filename: "aula8_listening2_panel_discussion" },
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
  console.log('Generating ' + PHRASES.length + ' audio files for Aula 8...');
  let generated = 0, skipped = 0;
  for (const p of PHRASES) {
    const fname = p.filename + '.mp3';
    const outPath = path.join(DIR, fname);
    if (fs.existsSync(outPath)) { console.log('SKIP: ' + fname); skipped++; }
    else {
      try {
        const bytes = await gen(p.text, p.voice, outPath);
        console.log('OK [' + (p.voice === ELLEN ? 'ellen' : 'arthur') + ']: ' + fname + ' (' + (bytes/1024).toFixed(1) + 'KB)');
        generated++;
        await new Promise(r => setTimeout(r, 500));
      } catch(e) { console.error('FAIL: ' + fname + ' -- ' + e.message); }
    }
  }
  console.log('\nDone! Generated: ' + generated + ', Skipped: ' + skipped + ', Total: ' + PHRASES.length);
  console.log('Total MP3s in dir: ' + fs.readdirSync(DIR).filter(f => f.endsWith('.mp3')).length);
}
main().catch(e => { console.error(e); process.exit(1); });
