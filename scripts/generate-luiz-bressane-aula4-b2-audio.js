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
// - Dialogue: Dr. Webb (female) = Ellen, Luiz (male) = Arthur
// - Listening passages alternate
// - [order-l4] = Arthur

const PHRASES = [
  // === VOCAB WORDS (single words = Arthur) ===
  { text: "Parole", voice: ARTHUR, file: "aula4_parole.mp3" },
  { text: "Probation", voice: ARTHUR, file: "aula4_probation.mp3" },
  { text: "Felony", voice: ARTHUR, file: "aula4_felony.mp3" },
  { text: "Misdemeanor", voice: ARTHUR, file: "aula4_misdemeanor.mp3" },
  { text: "Sanction", voice: ARTHUR, file: "aula4_sanction.mp3" },
  { text: "Compliance", voice: ARTHUR, file: "aula4_compliance.mp3" },
  { text: "Fraudulent", voice: ARTHUR, file: "aula4_fraudulent.mp3" },
  { text: "Negligence", voice: ARTHUR, file: "aula4_negligence.mp3" },
  { text: "Compensate", voice: ARTHUR, file: "aula4_compensate.mp3" },
  { text: "Deterrent", voice: ARTHUR, file: "aula4_deterrent.mp3" },
  { text: "Rehabilitation", voice: ARTHUR, file: "aula4_rehabilitation.mp3" },
  { text: "Enforcement", voice: ARTHUR, file: "aula4_enforcement.mp3" },
  { text: "Clemency", voice: ARTHUR, file: "aula4_clemency.mp3" },

  // === VOCAB EXAMPLE SENTENCES (alternate Arthur/Ellen) ===
  { text: "The prisoner was granted parole after serving ten years of his sentence.", voice: ARTHUR, file: "aula4_the_prisoner_was_granted_parole.mp3" },
  { text: "The judge ordered two years of probation instead of prison time.", voice: ELLEN, file: "aula4_the_judge_ordered_two_years_of_probation.mp3" },
  { text: "Armed robbery is classified as a felony in most jurisdictions.", voice: ARTHUR, file: "aula4_armed_robbery_is_classified_as_a_felony.mp3" },
  { text: "Shoplifting under fifty dollars is typically charged as a misdemeanor.", voice: ELLEN, file: "aula4_shoplifting_under_fifty_dollars.mp3" },
  { text: "The international community imposed sanctions against the regime.", voice: ARTHUR, file: "aula4_the_international_community_imposed_sanctions.mp3" },
  { text: "All financial institutions must ensure compliance with anti-money laundering laws.", voice: ELLEN, file: "aula4_all_financial_institutions_must_ensure.mp3" },
  { text: "The executive was charged with fraudulent accounting practices.", voice: ARTHUR, file: "aula4_the_executive_was_charged_with_fraudulent.mp3" },
  { text: "Medical negligence can result in significant compensation claims.", voice: ELLEN, file: "aula4_medical_negligence_can_result_in.mp3" },
  { text: "The court ordered the company to compensate the victims for their losses.", voice: ARTHUR, file: "aula4_the_court_ordered_the_company_to_compensate.mp3" },
  { text: "The threat of imprisonment serves as a deterrent against violent crime.", voice: ELLEN, file: "aula4_the_threat_of_imprisonment_serves_as.mp3" },
  { text: "The rehabilitation program helped former inmates reintegrate into society.", voice: ARTHUR, file: "aula4_the_rehabilitation_program_helped.mp3" },
  { text: "Strict enforcement of traffic laws has reduced accidents significantly.", voice: ELLEN, file: "aula4_strict_enforcement_of_traffic_laws.mp3" },
  { text: "The governor granted clemency to the death-row inmate after new evidence emerged.", voice: ARTHUR, file: "aula4_the_governor_granted_clemency.mp3" },

  // === GRAMMAR IN CONTEXT - Second Conditional sentences (alternate) ===
  { text: "If a company failed to ensure compliance, regulators would impose heavy sanctions.", voice: ELLEN, file: "aula4_gc_if_a_company_failed_compliance.mp3" },
  { text: "If the defendant were found guilty of a felony, the judge would consider both deterrence and rehabilitation when determining the sentence.", voice: ARTHUR, file: "aula4_gc_if_defendant_found_guilty.mp3" },
  { text: "If the evidence proved negligence, the court would order the defendant to compensate the victims.", voice: ELLEN, file: "aula4_gc_if_evidence_proved_negligence.mp3" },

  // === GRAMMAR TIP - Fill-in / Application sentences (alternate) ===
  { text: "If a prisoner showed genuine rehabilitation, the parole board would grant early release.", voice: ARTHUR, file: "aula4_if_prisoner_showed_rehabilitation.mp3" },
  { text: "If we reduced sentences for misdemeanors, we would have more resources for enforcement.", voice: ELLEN, file: "aula4_if_we_reduced_sentences_misdemeanors.mp3" },
  { text: "If the governor granted clemency, the inmate would be released from death row.", voice: ARTHUR, file: "aula4_if_governor_granted_clemency.mp3" },
  { text: "If stricter sanctions were imposed, companies would improve their compliance programs.", voice: ELLEN, file: "aula4_if_stricter_sanctions_imposed.mp3" },
  { text: "If fraudulent behavior went unpunished, it would undermine public trust in the system.", voice: ARTHUR, file: "aula4_if_fraudulent_behavior_went_unpunished.mp3" },
  { text: "If probation programs were better funded, fewer offenders would return to crime.", voice: ELLEN, file: "aula4_if_probation_programs_better_funded.mp3" },

  // === DIALOGUE: Dr. Webb (female) = Ellen, Luiz (male) = Arthur ===
  { text: "Good afternoon, everyone. Welcome to the ethics workshop. I am Dr. Karen Webb from Columbia Law School.", voice: ELLEN, file: "aula4_dl_webb_welcome.mp3" },
  { text: "Thank you, Dr. Webb. I am Luiz Bressane, a public defender from Sao Paulo.", voice: ARTHUR, file: "aula4_dl_luiz_intro.mp3" },
  { text: "Today we will explore hypothetical legal dilemmas. Let me start with a scenario. If a client confessed to you privately, but pleading guilty would result in a felony conviction, what would you do?", voice: ELLEN, file: "aula4_dl_webb_scenario1.mp3" },
  { text: "That is a classic ethical dilemma. If I were in that situation, I would advise my client on the consequences of both options, but I would never reveal a confidential confession.", voice: ARTHUR, file: "aula4_dl_luiz_response1.mp3" },
  { text: "Interesting. And if the prosecution offered probation instead of prison, would you recommend accepting the plea?", voice: ELLEN, file: "aula4_dl_webb_probation.mp3" },
  { text: "It would depend on the circumstances. If the evidence were weak, I would recommend going to trial. But if the case were strong, I would explain that probation is far better than a felony conviction.", voice: ARTHUR, file: "aula4_dl_luiz_depends.mp3" },
  { text: "Let us consider another scenario. If you discovered that a witness were providing fraudulent testimony, how would you handle it?", voice: ELLEN, file: "aula4_dl_webb_scenario2.mp3" },
  { text: "If I discovered fraudulent testimony, I would report it to the court immediately. Negligence in addressing fraud would undermine the entire justice system.", voice: ARTHUR, file: "aula4_dl_luiz_fraud.mp3" },
  { text: "Now, here is the big question. If you could change one thing about the criminal justice system, what would it be?", voice: ELLEN, file: "aula4_dl_webb_big_question.mp3" },
  { text: "If I could change one thing, I would invest more in rehabilitation programs. I believe that rehabilitation, not just punishment, is the most effective deterrent against crime.", voice: ARTHUR, file: "aula4_dl_luiz_rehabilitation.mp3" },

  // === LISTENING 1 (long passage - Arthur) ===
  { text: "Imagine you are a defense attorney in New York. Your client has been charged with a felony for corporate fraud. The prosecution claims the company failed to maintain compliance with financial regulations. If you could prove that the negligence was not intentional, the judge would likely reduce the charge to a misdemeanor. The key question is: would the court order the company to compensate the victims, or would the sanctions be limited to a fine? In many jurisdictions, enforcement agencies would require full compensation. The defense argues that parole or probation would be more appropriate than prison, citing the defendant's clean record and contributions to rehabilitation programs in the community. If the governor were to grant clemency, it would set a controversial precedent for future cases involving fraudulent corporate behavior.", voice: ARTHUR, file: "aula4_listening1_ethics_scenario.mp3" },

  // === LISTENING 2 (long passage - Ellen) ===
  { text: "In this segment of the ethics workshop, three attorneys share their perspectives on hypothetical legal reform. Attorney Rosa Mendes from Lisbon argues that if countries invested more in rehabilitation, recidivism rates would drop significantly. She believes that enforcement alone is not enough — society must also offer deterrent programs that address the root causes of crime. Professor James Whitfield from London disagrees. He argues that if sanctions were more severe, compliance would improve naturally. He points to cases where fraudulent executives received only probation, which he considers negligent. Finally, Dr. Amara Osei from Accra presents a middle ground. She suggests that if parole systems were reformed to include mandatory rehabilitation, fewer felons would reoffend. She also argues that clemency should be reserved for cases involving genuine remorse and misdemeanor-level offenses.", voice: ELLEN, file: "aula4_listening2_three_attorneys.mp3" },

  // === IN CLASS grammar examples (alternate) ===
  { text: "If a prisoner showed genuine rehabilitation, the parole board would grant early release.", voice: ARTHUR, file: "aula4_ic_second_cond_rehabilitation.mp3" },
  { text: "If we reduced sentences for misdemeanors, we would have more resources for enforcement.", voice: ELLEN, file: "aula4_ic_second_cond_misdemeanors.mp3" },
  { text: "If the governor granted clemency, the inmate would be released from death row.", voice: ARTHUR, file: "aula4_ic_second_cond_clemency.mp3" },
  { text: "If stricter sanctions were imposed, companies would improve their compliance programs.", voice: ELLEN, file: "aula4_ic_second_cond_sanctions.mp3" },

  // === SURVIVAL CARD IN CLASS (alternate) ===
  { text: "If fraudulent behavior went unpunished, it would undermine public trust in the justice system.", voice: ARTHUR, file: "aula4_survival_ic_fraudulent.mp3" },
  { text: "If probation programs were better funded, fewer offenders would return to crime.", voice: ELLEN, file: "aula4_survival_ic_probation.mp3" },
  { text: "If the court found negligence, the defendant would be ordered to compensate the victims.", voice: ARTHUR, file: "aula4_survival_ic_negligence.mp3" },
  { text: "If rehabilitation were prioritized over punishment, society would benefit in the long run.", voice: ELLEN, file: "aula4_survival_ic_rehabilitation.mp3" },
  { text: "If enforcement agencies had more resources, compliance rates would increase dramatically.", voice: ARTHUR, file: "aula4_survival_ic_enforcement.mp3" },

  // === ORDER exercise ===
  { text: "Good afternoon, everyone. Welcome to the ethics workshop. I am Dr. Karen Webb from Columbia Law School. Today we will explore hypothetical legal dilemmas. If a client confessed to you privately, but pleading guilty would result in a felony conviction, what would you do? That is a classic ethical dilemma. If I were in that situation, I would advise my client on the consequences, but I would never reveal a confidential confession. If I could change one thing about the criminal justice system, I would invest more in rehabilitation programs.", voice: ARTHUR, file: "aula4_order_l4_ethics_workshop.mp3" },
];

async function generateAudio(text, voiceId, outputFile) {
  const filePath = path.join(DIR, outputFile);
  if (fs.existsSync(filePath)) {
    const stat = fs.statSync(filePath);
    if (stat.size > 1000) {
      console.log(`SKIP (exists): ${outputFile}`);
      return true;
    }
  }

  console.log(`GENERATING: ${outputFile} (${voiceId === ARTHUR ? 'Arthur' : 'Ellen'})`);

  try {
    const response = await fetch(`https://api.elevenlabs.io/v1/text-to-speech/${voiceId}`, {
      method: 'POST',
      headers: {
        'Accept': 'audio/mpeg',
        'Content-Type': 'application/json',
        'xi-api-key': API_KEY
      },
      body: JSON.stringify({
        text: text,
        model_id: MODEL,
        voice_settings: {
          stability: 0.5,
          similarity_boost: 0.75,
          style: 0.0,
          use_speaker_boost: true
        }
      })
    });

    if (!response.ok) {
      const errText = await response.text();
      console.error(`ERROR ${response.status} for ${outputFile}: ${errText}`);
      return false;
    }

    const buffer = Buffer.from(await response.arrayBuffer());
    fs.writeFileSync(filePath, buffer);
    console.log(`OK: ${outputFile} (${(buffer.length / 1024).toFixed(1)} KB)`);
    return true;
  } catch (err) {
    console.error(`FETCH ERROR for ${outputFile}: ${err.message}`);
    return false;
  }
}

async function main() {
  console.log(`\n=== Luiz Bressane Aula 04 B2 Audio Generation ===`);
  console.log(`Total phrases: ${PHRASES.length}`);
  console.log(`Output dir: ${DIR}\n`);

  let generated = 0, skipped = 0, failed = 0;

  for (const phrase of PHRASES) {
    const result = await generateAudio(phrase.text, phrase.voice, phrase.file);
    if (result) {
      const filePath = path.join(DIR, phrase.file);
      if (fs.existsSync(filePath) && fs.statSync(filePath).size > 1000) {
        // Check if it was skipped or newly generated
        skipped++; // approximate
      }
      generated++;
    } else {
      failed++;
    }
    // 500ms delay between API calls
    await new Promise(r => setTimeout(r, 500));
  }

  console.log(`\n=== SUMMARY ===`);
  console.log(`Total: ${PHRASES.length}`);
  console.log(`Success: ${generated}`);
  console.log(`Failed: ${failed}`);

  // Verify all files exist
  console.log(`\n=== VERIFICATION ===`);
  let missing = 0;
  for (const phrase of PHRASES) {
    const filePath = path.join(DIR, phrase.file);
    if (!fs.existsSync(filePath) || fs.statSync(filePath).size < 1000) {
      console.log(`MISSING: ${phrase.file}`);
      missing++;
    }
  }
  if (missing === 0) {
    console.log(`All ${PHRASES.length} audio files verified OK!`);
  } else {
    console.log(`${missing} files still missing!`);
  }
}

main().catch(console.error);
