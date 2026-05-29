const fs = require('fs');
const path = require('path');
const https = require('https');

const API_KEY = process.env.ELEVENLABS_API_KEY;
if (!API_KEY) { console.error('ELEVENLABS_API_KEY not set'); process.exit(1); }

const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const MODEL = 'eleven_multilingual_v2';
const OUTPUT_DIR = path.join(__dirname, '..', 'public', 'audio', 'luiz-bressane');

// All aula5_ entries from audioMap — text -> { file, voice }
// Single words = Arthur
// Phrases alternate Arthur/Ellen
// Dialogue: Torres (female) = Ellen, Luiz (male) = Arthur
const entries = [
  // --- Vocabulary (single words = Arthur) ---
  { text: "Acquit", file: "aula5_acquit.mp3", voice: ARTHUR },
  { text: "Exonerate", file: "aula5_exonerate.mp3", voice: ARTHUR },
  { text: "Wrongful", file: "aula5_wrongful.mp3", voice: ARTHUR },
  { text: "Incarcerate", file: "aula5_incarcerate.mp3", voice: ARTHUR },
  { text: "Commute", file: "aula5_commute.mp3", voice: ARTHUR },
  { text: "Recidivism", file: "aula5_recidivism.mp3", voice: ARTHUR },
  { text: "Restitution", file: "aula5_restitution.mp3", voice: ARTHUR },
  { text: "Subpoena", file: "aula5_subpoena.mp3", voice: ARTHUR },
  { text: "Arraignment", file: "aula5_arraignment.mp3", voice: ARTHUR },
  { text: "Perjury", file: "aula5_perjury.mp3", voice: ARTHUR },
  { text: "Contempt", file: "aula5_contempt.mp3", voice: ARTHUR },
  { text: "Adjudicate", file: "aula5_adjudicate.mp3", voice: ARTHUR },
  { text: "Expunge", file: "aula5_expunge.mp3", voice: ARTHUR },

  // --- Vocab example sentences (alternate Arthur/Ellen) ---
  { text: "The jury voted to acquit the defendant after reviewing the new evidence.", file: "aula5_the_jury_voted_to_acquit.mp3", voice: ARTHUR },
  { text: "DNA evidence helped exonerate the man who had been wrongfully imprisoned for eighteen years.", file: "aula5_dna_evidence_helped_exonerate.mp3", voice: ELLEN },
  { text: "The wrongful conviction was overturned after new witnesses came forward.", file: "aula5_the_wrongful_conviction_was_overturned.mp3", voice: ARTHUR },
  { text: "The state incarcerated thousands of nonviolent offenders during the 1990s.", file: "aula5_the_state_incarcerated_thousands.mp3", voice: ELLEN },
  { text: "The governor decided to commute the prisoner's life sentence to twenty years.", file: "aula5_the_governor_decided_to_commute.mp3", voice: ARTHUR },
  { text: "Studies show that recidivism rates drop when inmates receive education in prison.", file: "aula5_studies_show_that_recidivism_rates.mp3", voice: ELLEN },
  { text: "The court ordered the defendant to pay restitution to the victims' families.", file: "aula5_the_court_ordered_restitution.mp3", voice: ARTHUR },
  { text: "The attorney issued a subpoena to compel the witness to testify.", file: "aula5_the_attorney_issued_a_subpoena.mp3", voice: ELLEN },
  { text: "At the arraignment, the accused pleaded not guilty to all charges.", file: "aula5_at_the_arraignment_the_accused.mp3", voice: ARTHUR },
  { text: "The witness was charged with perjury after lying under oath.", file: "aula5_the_witness_was_charged_with_perjury.mp3", voice: ELLEN },
  { text: "The judge held the attorney in contempt for refusing to comply with the court order.", file: "aula5_the_judge_held_the_attorney_in_contempt.mp3", voice: ARTHUR },
  { text: "A panel of three judges was appointed to adjudicate the dispute.", file: "aula5_a_panel_of_three_judges.mp3", voice: ELLEN },
  { text: "After completing his sentence, he applied to have his record expunged.", file: "aula5_after_completing_his_sentence.mp3", voice: ARTHUR },

  // --- Grammar in Context / Third Conditional sentences (alternate) ---
  { text: "If the defense had presented stronger evidence, the jury would have acquitted the defendant.", file: "aula5_gc_if_defense_had_presented.mp3", voice: ELLEN },
  { text: "If the witness had not committed perjury, the wrongful conviction would never have happened.", file: "aula5_gc_if_witness_had_not_committed.mp3", voice: ARTHUR },
  { text: "If the governor had commuted the sentence earlier, the inmate would have been exonerated sooner.", file: "aula5_gc_if_governor_had_commuted.mp3", voice: ELLEN },
  { text: "If the court had ordered restitution, the victims would have received compensation years ago.", file: "aula5_if_court_had_ordered_restitution.mp3", voice: ARTHUR },
  { text: "If the attorney had not issued the subpoena, the key evidence would have remained hidden.", file: "aula5_if_attorney_had_not_issued_subpoena.mp3", voice: ELLEN },
  { text: "If they had invested in rehabilitation programs, recidivism rates would have decreased significantly.", file: "aula5_if_they_had_invested_rehabilitation.mp3", voice: ARTHUR },
  { text: "If the record had been expunged, the former inmate would have had a fresh start.", file: "aula5_if_record_had_been_expunged.mp3", voice: ELLEN },
  { text: "If the arraignment had taken place on time, the trial would not have been delayed.", file: "aula5_if_arraignment_had_taken_place.mp3", voice: ARTHUR },
  { text: "If the judge had held the lawyer in contempt earlier, the proceedings would have been smoother.", file: "aula5_if_judge_had_held_contempt.mp3", voice: ELLEN },

  // --- Dialogue: Torres (female=Ellen), Luiz (male=Arthur) ---
  { text: "Good afternoon, everyone. Welcome to our final roundtable. I am retired Judge Margaret Torres.", file: "aula5_dl_torres_welcome.mp3", voice: ELLEN },
  { text: "Thank you, Judge Torres. I am Luiz Bressane. It has been an extraordinary symposium.", file: "aula5_dl_luiz_intro.mp3", voice: ARTHUR },
  { text: "Today I want us to reflect on the roads not taken. If you had made a different career choice, where would you be today?", file: "aula5_dl_torres_roads_not_taken.mp3", voice: ELLEN },
  { text: "That is a profound question. If I had not become a public defender, I would have pursued academia. But I would not have experienced the cases that shaped who I am.", file: "aula5_dl_luiz_academia.mp3", voice: ARTHUR },
  { text: "I often think about a wrongful conviction case from my early career. If I had adjudicated that case differently, an innocent man would have been incarcerated for decades.", file: "aula5_dl_torres_wrongful.mp3", voice: ELLEN },
  { text: "I had a similar experience. If the witness had not committed perjury, my client would never have been convicted. We fought for years to exonerate him.", file: "aula5_dl_luiz_perjury.mp3", voice: ARTHUR },
  { text: "If you had been the judge in that case, what would you have done differently?", file: "aula5_dl_torres_what_differently.mp3", voice: ELLEN },
  { text: "If I had been the judge, I would have issued a subpoena for additional evidence before allowing the case to go to trial. The arraignment was rushed.", file: "aula5_dl_luiz_subpoena.mp3", voice: ARTHUR },
  { text: "That is exactly why I advocate for having criminal records expunged after exoneration. If we had better systems, restitution would not take so long.", file: "aula5_dl_torres_expunge.mp3", voice: ELLEN },
  { text: "I completely agree. If the justice system had prioritized reducing recidivism through rehabilitation, we would have seen far fewer cases of contempt and repeat offenses.", file: "aula5_dl_luiz_recidivism.mp3", voice: ARTHUR },

  // --- Listening (long passages — Arthur for Luiz narration, Ellen for mixed) ---
  { text: "Throughout my thirty-year career as a public defender in Sao Paulo, I have encountered many cases that challenged my understanding of justice. One case in particular haunts me to this day. In 2008, I defended a young man named Carlos who was wrongfully convicted of armed robbery. If the original investigators had followed proper procedure, they would have discovered the real perpetrator much sooner. Carlos was incarcerated for six years before new DNA evidence helped us exonerate him. If the witness had not committed perjury during the trial, Carlos would never have been convicted. The arraignment was rushed, and the judge refused to issue a subpoena for additional surveillance footage. If the court had adjudicated the case more carefully, an innocent man would not have lost six years of his life. After his release, we fought to have his record expunged and to secure restitution from the state. The case taught me that if we had better systems for reviewing evidence before trial, wrongful convictions would decrease dramatically.", file: "aula5_listening1_luiz_career_reflection.mp3", voice: ARTHUR },
  { text: "In this segment of our roundtable, three legal professionals share their reflections on career-defining moments. First, Judge Margaret Torres from New York. Early in her career, she adjudicated a controversial drug case. If she had not held the prosecution in contempt for withholding evidence, an innocent defendant would have been incarcerated for life. She later advocated for having wrongful conviction records expunged automatically. Next, attorney David Park from Seoul. He specialized in international restitution cases. If his team had not issued a subpoena for offshore banking records, they would never have recovered the stolen assets. He now trains young lawyers on the importance of thorough arraignment procedures. Finally, Professor Ana Lucia Ferreira from Brasilia. Her research on recidivism shows that if countries had invested more in rehabilitation programs during the twentieth century, incarceration rates would have been significantly lower. She argues that if perjury were treated more seriously, fewer wrongful convictions would have occurred.", file: "aula5_listening2_three_reflections.mp3", voice: ELLEN },

  // --- IN CLASS Third Conditional sentences (alternate) ---
  { text: "If the defense had presented stronger evidence, the jury would have acquitted the defendant.", file: "aula5_ic_third_cond_acquitted.mp3", voice: ARTHUR },
  { text: "If the witness had not committed perjury, the wrongful conviction would never have happened.", file: "aula5_ic_third_cond_perjury.mp3", voice: ELLEN },
  { text: "If the governor had commuted the sentence earlier, the inmate would have been exonerated sooner.", file: "aula5_ic_third_cond_commuted.mp3", voice: ARTHUR },
  { text: "If the court had ordered restitution, the victims would have received compensation years ago.", file: "aula5_ic_third_cond_restitution.mp3", voice: ELLEN },

  // --- Survival IC sentences (alternate) ---
  { text: "If the attorney had not issued the subpoena, the key evidence would have remained hidden.", file: "aula5_survival_ic_subpoena.mp3", voice: ARTHUR },
  { text: "If they had invested in rehabilitation, recidivism rates would have decreased significantly.", file: "aula5_survival_ic_recidivism.mp3", voice: ELLEN },
  { text: "If the record had been expunged, the former inmate would have had a fresh start.", file: "aula5_survival_ic_expunged.mp3", voice: ARTHUR },
  { text: "If the arraignment had not been rushed, the wrongful conviction could have been avoided.", file: "aula5_survival_ic_arraignment.mp3", voice: ELLEN },
  { text: "If the judge had held the lawyer in contempt earlier, the trial would have proceeded more fairly.", file: "aula5_survival_ic_contempt.mp3", voice: ARTHUR },

  // --- Order exercise ---
  { text: "[order-l5]", file: "aula5_order_l5_roundtable.mp3", voice: ARTHUR },
];

function sleep(ms) { return new Promise(r => setTimeout(r, ms)); }

function generateAudio(text, voiceId, outputPath) {
  return new Promise((resolve, reject) => {
    const body = JSON.stringify({
      text: text,
      model_id: MODEL,
      voice_settings: { stability: 0.5, similarity_boost: 0.75 }
    });

    const options = {
      hostname: 'api.elevenlabs.io',
      path: `/v1/text-to-speech/${voiceId}`,
      method: 'POST',
      headers: {
        'Accept': 'audio/mpeg',
        'Content-Type': 'application/json',
        'xi-api-key': API_KEY,
        'Content-Length': Buffer.byteLength(body)
      }
    };

    const req = https.request(options, (res) => {
      if (res.statusCode !== 200) {
        let errData = '';
        res.on('data', c => errData += c);
        res.on('end', () => reject(new Error(`HTTP ${res.statusCode}: ${errData}`)));
        return;
      }
      const chunks = [];
      res.on('data', c => chunks.push(c));
      res.on('end', () => {
        const buffer = Buffer.concat(chunks);
        fs.writeFileSync(outputPath, buffer);
        resolve(buffer.length);
      });
    });

    req.on('error', reject);
    req.write(body);
    req.end();
  });
}

async function main() {
  if (!fs.existsSync(OUTPUT_DIR)) fs.mkdirSync(OUTPUT_DIR, { recursive: true });

  let generated = 0, skipped = 0, failed = 0;

  for (const entry of entries) {
    const outputPath = path.join(OUTPUT_DIR, entry.file);

    if (fs.existsSync(outputPath)) {
      const stat = fs.statSync(outputPath);
      if (stat.size > 1000) {
        console.log(`SKIP (exists): ${entry.file}`);
        skipped++;
        continue;
      }
    }

    const voiceName = entry.voice === ARTHUR ? 'Arthur' : 'Ellen';
    const shortText = entry.text.length > 60 ? entry.text.substring(0, 57) + '...' : entry.text;
    console.log(`GEN [${voiceName}]: ${entry.file} — "${shortText}"`);

    try {
      const size = await generateAudio(entry.text, entry.voice, outputPath);
      console.log(`  OK (${(size/1024).toFixed(1)} KB)`);
      generated++;
      await sleep(500);
    } catch (err) {
      console.error(`  FAIL: ${err.message}`);
      failed++;
      await sleep(1000);
    }
  }

  console.log(`\n=== DONE === Generated: ${generated} | Skipped: ${skipped} | Failed: ${failed} | Total: ${entries.length}`);
  if (failed > 0) process.exit(1);
}

main();
