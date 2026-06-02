const fs = require('fs');
const path = require('path');
const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const DIR = path.join(__dirname, '..', 'public', 'audio', 'luiz-bressane');

const PHRASES = [
  // === Vocabulary (13 words) — Arthur for male student ===
  { text: "Equity", voice: ARTHUR, filename: "aula6_equity" },
  { text: "Impartial", voice: ARTHUR, filename: "aula6_impartial" },
  { text: "Accountability", voice: ARTHUR, filename: "aula6_accountability" },
  { text: "Proportional", voice: ARTHUR, filename: "aula6_proportional" },
  { text: "Retribution", voice: ARTHUR, filename: "aula6_retribution" },
  { text: "Restorative", voice: ARTHUR, filename: "aula6_restorative" },
  { text: "Disproportionate", voice: ARTHUR, filename: "aula6_disproportionate" },
  { text: "Inherent", voice: ARTHUR, filename: "aula6_inherent" },
  { text: "Inalienable", voice: ARTHUR, filename: "aula6_inalienable" },
  { text: "Abolish", voice: ARTHUR, filename: "aula6_abolish" },
  { text: "Uphold", voice: ARTHUR, filename: "aula6_uphold" },
  { text: "Dissent", voice: ARTHUR, filename: "aula6_dissent" },
  { text: "Fundamental", voice: ARTHUR, filename: "aula6_fundamental" },

  // === Example sentences (alternating voices) ===
  { text: "True equity requires treating people according to their circumstances, not identically.", voice: ELLEN, filename: "aula6_equity_sentence" },
  { text: "A judge must remain impartial throughout the entire trial.", voice: ARTHUR, filename: "aula6_impartial_sentence" },
  { text: "Accountability is essential for maintaining public trust in the legal system.", voice: ELLEN, filename: "aula6_accountability_sentence" },
  { text: "The sentence should be proportional to the severity of the crime.", voice: ARTHUR, filename: "aula6_proportional_sentence" },
  { text: "Some argue that retribution is a necessary component of justice.", voice: ELLEN, filename: "aula6_retribution_sentence" },
  { text: "Restorative justice focuses on healing rather than punishment.", voice: ARTHUR, filename: "aula6_restorative_sentence" },
  { text: "The punishment was disproportionate to the offense committed.", voice: ELLEN, filename: "aula6_disproportionate_sentence" },
  { text: "Human dignity is an inherent right that cannot be legislated away.", voice: ARTHUR, filename: "aula6_inherent_sentence" },
  { text: "The constitution protects certain inalienable rights for all citizens.", voice: ELLEN, filename: "aula6_inalienable_sentence" },
  { text: "Many countries have voted to abolish the death penalty.", voice: ARTHUR, filename: "aula6_abolish_sentence" },
  { text: "It is the duty of every court to uphold the rule of law.", voice: ELLEN, filename: "aula6_uphold_sentence" },
  { text: "Justice Oliveira filed a written dissent arguing the majority opinion was unconstitutional.", voice: ARTHUR, filename: "aula6_dissent_sentence" },
  { text: "Access to legal representation is a fundamental right in any democracy.", voice: ELLEN, filename: "aula6_fundamental_sentence" },

  // === Mixed Conditional grammar examples (alternating) ===
  { text: "If the court had abolished the death penalty decades ago, the system would be more humane today.", voice: ARTHUR, filename: "aula6_mixed1_abolished" },
  { text: "If justice were truly impartial, fewer wrongful convictions would have occurred.", voice: ELLEN, filename: "aula6_mixed2_impartial" },
  { text: "If the legislature had upheld the reform, citizens would have greater protections now.", voice: ARTHUR, filename: "aula6_mixed3_upheld" },
  { text: "If restorative justice were the norm, many victims would have found closure years ago.", voice: ELLEN, filename: "aula6_mixed4_restorative" },
  { text: "If accountability were built into the system, fewer abuses would have gone unpunished.", voice: ARTHUR, filename: "aula6_mixed5_accountability" },
  { text: "If the punishment had been proportional, the public would trust the courts more today.", voice: ELLEN, filename: "aula6_mixed6_proportional" },
  { text: "If we had recognized these rights as inalienable from the start, the legal framework would be stronger now.", voice: ARTHUR, filename: "aula6_mixed7_inalienable" },
  { text: "If the dissenting opinion had prevailed, the law would protect more people today.", voice: ELLEN, filename: "aula6_mixed8_dissent" },
  { text: "If equity were the foundation of the system, disproportionate sentencing would never have become so widespread.", voice: ARTHUR, filename: "aula6_mixed9_equity" },

  // === Dialogue: Luiz (Arthur) + Prof. Osei (Ellen) ===
  { text: "Good afternoon, Professor Osei. I have been looking forward to this conversation about the philosophy of justice.", voice: ARTHUR, filename: "aula6_dl_luiz_greeting" },
  { text: "Thank you, Luiz. The question of what justice truly means has occupied philosophers for millennia. Let me begin with a provocation.", voice: ELLEN, filename: "aula6_dl_osei_greeting" },
  { text: "If retribution were the only purpose of punishment, would our legal systems be more just or less just today?", voice: ELLEN, filename: "aula6_dl_osei_provocation" },
  { text: "That is a fascinating question. If we had built our systems entirely around retribution, I believe we would have created more cycles of violence rather than justice.", voice: ARTHUR, filename: "aula6_dl_luiz_retribution" },
  { text: "Exactly. And if restorative justice had been adopted as the fundamental approach decades ago, communities would have healed rather than fractured.", voice: ELLEN, filename: "aula6_dl_osei_restorative" },
  { text: "I see your point. But can we truly abolish punishment entirely? If there were no accountability, people would not feel safe.", voice: ARTHUR, filename: "aula6_dl_luiz_accountability" },
  { text: "You raise an inherent tension in the philosophy of law. If equity and proportionality were always upheld, perhaps punishment would feel less like retribution and more like justice.", voice: ELLEN, filename: "aula6_dl_osei_tension" },
  { text: "As a public defender, I have witnessed disproportionate sentences destroy lives. If the system had prioritized rehabilitation, many of my clients would be contributing members of society today.", voice: ARTHUR, filename: "aula6_dl_luiz_disproportionate" },
  { text: "That brings us to inalienable rights. If we truly believed that dignity were inalienable, we would never have allowed such systemic inequities to persist.", voice: ELLEN, filename: "aula6_dl_osei_inalienable" },
  { text: "I filed a dissent in a landmark case last year arguing exactly that. If the majority had agreed, it would have transformed how we define justice in Brazil.", voice: ARTHUR, filename: "aula6_dl_luiz_dissent" },

  // === Listening 1: Luiz's philosophy reflection (long passage — Arthur) ===
  { text: "Throughout my career as a public defender, I have constantly questioned what justice truly means. Early in my career, I believed that the law was inherently fair. If you followed the rules, equity would prevail. But experience taught me otherwise. I have witnessed disproportionate sentences handed down to people who committed minor offenses while those with resources walked free. If the system had been truly impartial from the beginning, I believe we would have far fewer people in prison today. I began to question whether retribution should be the fundamental purpose of punishment. If restorative justice had been adopted in Brazil decades ago, communities would be stronger and recidivism rates would be lower. I have also seen how the lack of accountability among officials has eroded public trust. If we had built accountability into every level of the justice system, citizens would trust the courts more today. The question of inalienable rights haunts me. If we truly believed that every person had inalienable dignity, we would never have tolerated the conditions in our prisons. I filed a dissent in a landmark case arguing that disproportionate sentencing violated fundamental constitutional principles. If the court had upheld my argument, it would have changed the trajectory of criminal justice in Brazil.", voice: ARTHUR, filename: "aula6_listening1_luiz_justice_philosophy" },

  // === Listening 2: Prof. Osei panel (Ellen) ===
  { text: "In today's symposium, we heard from three scholars on the philosophy of justice. Professor Amara Osei from the University of Ghana argued that if African nations had adopted restorative justice models based on indigenous traditions rather than colonial legal frameworks, the concept of accountability would look very different today. She believes that retribution, as imported through colonial law, undermined inherent community-based approaches to conflict resolution. Dr. Henrik Larsson from Stockholm presented research showing that if Scandinavian countries had not abolished punitive approaches in the 1970s, their current equity-based systems would not exist. He demonstrated that proportional sentencing, combined with restorative practices, has led to some of the lowest recidivism rates in the world. Finally, Judge Maria Esperanza from Buenos Aires shared a powerful dissent she wrote arguing that certain rights are inalienable regardless of what the majority votes. She argued that if the judiciary had consistently upheld fundamental rights over political pressure, fewer disproportionate sentences would have been handed down across Latin America. The panel concluded that justice is not simply about punishment, but about creating systems that are impartial, proportional, and fundamentally committed to human dignity.", voice: ELLEN, filename: "aula6_listening2_osei_global_justice" },

  // === IN CLASS grammar examples ===
  { text: "If the court had abolished the death penalty, the system would be more humane today.", voice: ARTHUR, filename: "aula6_ic_mixed_abolished" },
  { text: "If justice were truly impartial, fewer wrongful convictions would have occurred.", voice: ELLEN, filename: "aula6_ic_mixed_impartial" },
  { text: "If the legislature had upheld the reform, citizens would have greater protections now.", voice: ARTHUR, filename: "aula6_ic_mixed_upheld" },
  { text: "If restorative justice were the norm, many victims would have found closure years ago.", voice: ELLEN, filename: "aula6_ic_mixed_restorative" },

  // === Survival Card phrases ===
  { text: "If the court had prioritized equity, disproportionate sentencing would not be so widespread today.", voice: ARTHUR, filename: "aula6_survival_ic_equity" },
  { text: "If accountability were built into the system from the start, public trust would be stronger now.", voice: ELLEN, filename: "aula6_survival_ic_accountability" },
  { text: "If the dissenting opinion had prevailed, the law would protect more people today.", voice: ARTHUR, filename: "aula6_survival_ic_dissent" },
  { text: "If restorative justice had been adopted earlier, many communities would have healed instead of fractured.", voice: ELLEN, filename: "aula6_survival_ic_restorative" },
  { text: "If we truly believed that rights were inalienable, we would never have tolerated such inequity.", voice: ARTHUR, filename: "aula6_survival_ic_inalienable" },

  // === Ordering exercise audio ===
  { text: "Professor Osei asks whether retribution alone can create a just system. Luiz argues that retribution creates cycles of violence. They discuss restorative justice as an alternative. Luiz raises the concern that abolishing punishment entirely removes accountability. Professor Osei concludes that equity and proportionality must be the foundation of any just system.", voice: ARTHUR, filename: "aula6_order_l6_justice_debate" },
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
  console.log('Generating ' + PHRASES.length + ' audio files for Aula 6...');
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
  console.log('\nDone! Total MP3s in dir: ' + fs.readdirSync(DIR).filter(f => f.endsWith('.mp3')).length);
}
main().catch(e => { console.error(e); process.exit(1); });
