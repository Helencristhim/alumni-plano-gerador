const fs = require('fs');
const path = require('path');
const https = require('https');
const API_KEY = process.env.ELEVENLABS_API_KEY;
if (!API_KEY) { console.error('ERROR: Set ELEVENLABS_API_KEY'); process.exit(1); }
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const BASE_DIR = '/Users/helenmendes/alumni-plano-gerador/public';

const audioMap = {
  "Witness": "/audio/luiz-bressane/aula7_witness.mp3",
  "Testify": "/audio/luiz-bressane/aula7_testify.mp3",
  "Account": "/audio/luiz-bressane/aula7_account.mp3",
  "Sequence": "/audio/luiz-bressane/aula7_sequence.mp3",
  "Recollect": "/audio/luiz-bressane/aula7_recollect.mp3",
  "Corroborate": "/audio/luiz-bressane/aula7_corroborate.mp3",
  "Discrepancy": "/audio/luiz-bressane/aula7_discrepancy.mp3",
  "Sworn": "/audio/luiz-bressane/aula7_sworn.mp3",
  "Reliable": "/audio/luiz-bressane/aula7_reliable.mp3",
  "Chronological": "/audio/luiz-bressane/aula7_chronological.mp3",
  "Recount": "/audio/luiz-bressane/aula7_recount.mp3",
  "Deposition": "/audio/luiz-bressane/aula7_deposition.mp3",
  "The witness identified the suspect from a lineup of six individuals.": "/audio/luiz-bressane/aula7_ex_witness.mp3",
  "The forensic expert was called to testify about the DNA results.": "/audio/luiz-bressane/aula7_ex_testify.mp3",
  "The victim gave a detailed account of the robbery to the police.": "/audio/luiz-bressane/aula7_ex_account.mp3",
  "The detective reconstructed the sequence of events before the crime.": "/audio/luiz-bressane/aula7_ex_sequence.mp3",
  "The witness could not recollect the exact time of the incident.": "/audio/luiz-bressane/aula7_ex_recollect.mp3",
  "Security footage corroborated the witness's account of the attack.": "/audio/luiz-bressane/aula7_ex_corroborate.mp3",
  "The defense found a discrepancy between the two witness statements.": "/audio/luiz-bressane/aula7_ex_discrepancy.mp3",
  "The officer submitted a sworn statement describing the arrest.": "/audio/luiz-bressane/aula7_ex_sworn.mp3",
  "The court must determine whether the eyewitness testimony is reliable.": "/audio/luiz-bressane/aula7_ex_reliable.mp3",
  "The prosecutor presented the evidence in chronological order.": "/audio/luiz-bressane/aula7_ex_chronological.mp3",
  "The victim was asked to recount exactly what happened that night.": "/audio/luiz-bressane/aula7_ex_recount.mp3",
  "The attorney took the witness's deposition three weeks before the trial.": "/audio/luiz-bressane/aula7_ex_deposition.mp3",
  "The witness was walking home when he heard a loud noise coming from the building.": "/audio/luiz-bressane/aula7_nt1_walking.mp3",
  "She had already left the office when the police arrived at the scene.": "/audio/luiz-bressane/aula7_nt2_left.mp3",
  "The defendant entered the building while the security guard was checking the cameras.": "/audio/luiz-bressane/aula7_nt3_entered.mp3",
  "By the time the ambulance arrived, the victim had lost consciousness.": "/audio/luiz-bressane/aula7_nt4_lost.mp3",
  "The suspect was running down the alley when the officer spotted him.": "/audio/luiz-bressane/aula7_nt5_running.mp3",
  "The witness testified that the defendant had threatened the victim before the incident.": "/audio/luiz-bressane/aula7_nt6_threatened.mp3",
  "While the jury was deliberating, the judge reviewed the sworn statements.": "/audio/luiz-bressane/aula7_fill1_deliberating.mp3",
  "The detective had already interviewed three witnesses before he found the key evidence.": "/audio/luiz-bressane/aula7_fill2_interviewed.mp3",
  "The suspect was leaving the building when the alarm went off.": "/audio/luiz-bressane/aula7_fill3_leaving.mp3",
  "The witness recounted that she had seen the defendant near the crime scene at eight pm.": "/audio/luiz-bressane/aula7_fill4_recounted.mp3",
  "The forensic team was collecting evidence when the rain started to fall.": "/audio/luiz-bressane/aula7_fill5_collecting.mp3",
  "By the time the trial began, the prosecution had gathered over fifty pieces of evidence.": "/audio/luiz-bressane/aula7_fill6_gathered.mp3",
  "Good morning, Mr. Bressane. Before we begin, please state your name and role for the record.": "/audio/luiz-bressane/aula7_dl_morrison_greeting.mp3",
  "Good morning, Your Honor. I am Luiz Bressane, public defender assigned to the case of State versus Andrade.": "/audio/luiz-bressane/aula7_dl_luiz_intro.mp3",
  "Can you recount the sequence of events on the night in question, based on your client's testimony?": "/audio/luiz-bressane/aula7_dl_morrison_recount.mp3",
  "According to my client, he was walking home from work at approximately nine pm. While he was crossing Avenida Paulista, he noticed a commotion near the bank.": "/audio/luiz-bressane/aula7_dl_luiz_events.mp3",
  "And what happened next? Did your client approach the scene?": "/audio/luiz-bressane/aula7_dl_morrison_next.mp3",
  "No, Your Honor. My client stated that he had already called the police before the suspect fled the scene. He was standing across the street when the officers arrived.": "/audio/luiz-bressane/aula7_dl_luiz_called.mp3",
  "The prosecution claims there is a discrepancy between your client's account and the security footage. How do you respond?": "/audio/luiz-bressane/aula7_dl_morrison_discrepancy.mp3",
  "The footage corroborates my client's account. He was standing on the opposite sidewalk the entire time. The discrepancy the prosecution refers to is a matter of camera angle, not of fact.": "/audio/luiz-bressane/aula7_dl_luiz_corroborate.mp3",
  "On the night of March fifteenth, my client, Mr. Carlos Andrade, was returning home from his job at a logistics company in the Pinheiros district of São Paulo. He had finished his shift at eight thirty pm and was walking along Rua Augusta toward the metro station. While he was crossing Avenida Paulista at approximately nine pm, he heard shouting coming from the direction of a bank branch. Several people were running away from the entrance. My client stopped on the opposite sidewalk and was watching the scene when he noticed a man carrying a dark bag running down a side street. He had already taken out his phone and called the emergency number before the first patrol car arrived. When the officers reached the scene, they found my client standing exactly where the security camera later confirmed his position. The sworn statement he gave to the responding officer that night is entirely consistent with the footage. The prosecution has pointed to a discrepancy regarding the timing, but this is explained by the fact that the bank's security system was running four minutes behind. My client's account is reliable and chronological, and every detail has been corroborated by independent evidence.": "/audio/luiz-bressane/aula7_listening1_luiz_witness_statement.mp3",
  "The case of State versus Andrade began when police received a call about a disturbance near a bank on Avenida Paulista on the night of March fifteenth. When officers arrived at the scene, they found several witnesses who had been watching the events unfold from across the street. The lead detective, Inspector Oliveira, took sworn depositions from three individuals that night. While she was interviewing the witnesses, her team was collecting physical evidence from the bank entrance. The forensic team had already secured the perimeter by the time the detective finished the initial interviews. Over the following weeks, the investigation team worked to corroborate each witness's account against the security footage and forensic evidence. They discovered that two of the three accounts matched perfectly in chronological sequence, while the third witness could not recollect certain details. The defense attorney, Mr. Bressane, argued that his client had been cooperating fully since the beginning and that no reliable evidence placed his client inside the bank.": "/audio/luiz-bressane/aula7_listening2_narrator_case_summary.mp3",
  "The witness was walking home when he heard a loud noise.": "/audio/luiz-bressane/aula7_survival1.mp3",
  "My client had already called the police before the suspect fled.": "/audio/luiz-bressane/aula7_survival2.mp3",
  "While the officers were securing the area, the detective was interviewing witnesses.": "/audio/luiz-bressane/aula7_survival3.mp3",
  "The forensic team had collected all the evidence by the time the trial began.": "/audio/luiz-bressane/aula7_survival4.mp3",
  "I can corroborate my client's account with the security footage.": "/audio/luiz-bressane/aula7_survival5.mp3",
  "[order-l7]": "/audio/luiz-bressane/order_l7_ordering.mp3"
};

// Luiz = male student, so student voice = Arthur
// Judge Morrison = female character = Ellen
// Dialogue lines by character
const ellenPhrases = new Set([
  "Good morning, Mr. Bressane. Before we begin, please state your name and role for the record.",
  "Can you recount the sequence of events on the night in question, based on your client's testimony?",
  "And what happened next? Did your client approach the scene?",
  "The prosecution claims there is a discrepancy between your client's account and the security footage. How do you respond?",
  // Narrator listening 2 uses Ellen
  "The case of State versus Andrade began when police received a call about a disturbance near a bank on Avenida Paulista on the night of March fifteenth. When officers arrived at the scene, they found several witnesses who had been watching the events unfold from across the street. The lead detective, Inspector Oliveira, took sworn depositions from three individuals that night. While she was interviewing the witnesses, her team was collecting physical evidence from the bank entrance. The forensic team had already secured the perimeter by the time the detective finished the initial interviews. Over the following weeks, the investigation team worked to corroborate each witness's account against the security footage and forensic evidence. They discovered that two of the three accounts matched perfectly in chronological sequence, while the third witness could not recollect certain details. The defense attorney, Mr. Bressane, argued that his client had been cooperating fully since the beginning and that no reliable evidence placed his client inside the bank.",
  // Alternating examples - Ellen gets even ones
  "She had already left the office when the police arrived at the scene.",
  "By the time the ambulance arrived, the victim had lost consciousness.",
  "The witness recounted that she had seen the defendant near the crime scene at eight pm.",
  "The forensic team was collecting evidence when the rain started to fall.",
  // Alternating vocab examples
  "The forensic expert was called to testify about the DNA results.",
  "The detective reconstructed the sequence of events before the crime.",
  "Security footage corroborated the witness's account of the attack.",
  "The court must determine whether the eyewitness testimony is reliable.",
  "The victim was asked to recount exactly what happened that night.",
]);

const arthurPhrases = new Set([
  // Luiz's dialogue lines
  "Good morning, Your Honor. I am Luiz Bressane, public defender assigned to the case of State versus Andrade.",
  "According to my client, he was walking home from work at approximately nine pm. While he was crossing Avenida Paulista, he noticed a commotion near the bank.",
  "No, Your Honor. My client stated that he had already called the police before the suspect fled the scene. He was standing across the street when the officers arrived.",
  "The footage corroborates my client's account. He was standing on the opposite sidewalk the entire time. The discrepancy the prosecution refers to is a matter of camera angle, not of fact.",
  // Luiz listening 1
  "On the night of March fifteenth, my client, Mr. Carlos Andrade, was returning home from his job at a logistics company in the Pinheiros district of São Paulo. He had finished his shift at eight thirty pm and was walking along Rua Augusta toward the metro station. While he was crossing Avenida Paulista at approximately nine pm, he heard shouting coming from the direction of a bank branch. Several people were running away from the entrance. My client stopped on the opposite sidewalk and was watching the scene when he noticed a man carrying a dark bag running down a side street. He had already taken out his phone and called the emergency number before the first patrol car arrived. When the officers reached the scene, they found my client standing exactly where the security camera later confirmed his position. The sworn statement he gave to the responding officer that night is entirely consistent with the footage. The prosecution has pointed to a discrepancy regarding the timing, but this is explained by the fact that the bank's security system was running four minutes behind. My client's account is reliable and chronological, and every detail has been corroborated by independent evidence.",
  // Survival phrases (student = Arthur)
  "The witness was walking home when he heard a loud noise.",
  "My client had already called the police before the suspect fled.",
  "While the officers were securing the area, the detective was interviewing witnesses.",
  "The forensic team had collected all the evidence by the time the trial began.",
  "I can corroborate my client's account with the security footage.",
  // Alternating examples - Arthur gets odd ones
  "The witness was walking home when he heard a loud noise coming from the building.",
  "The defendant entered the building while the security guard was checking the cameras.",
  "The suspect was running down the alley when the officer spotted him.",
  "The witness testified that the defendant had threatened the victim before the incident.",
  "While the jury was deliberating, the judge reviewed the sworn statements.",
  "The detective had already interviewed three witnesses before he found the key evidence.",
  "The suspect was leaving the building when the alarm went off.",
  "By the time the trial began, the prosecution had gathered over fifty pieces of evidence.",
  // Alternating vocab examples
  "The witness identified the suspect from a lineup of six individuals.",
  "The victim gave a detailed account of the robbery to the police.",
  "The witness could not recollect the exact time of the incident.",
  "The defense found a discrepancy between the two witness statements.",
  "The officer submitted a sworn statement describing the arrest.",
  "The prosecutor presented the evidence in chronological order.",
  "The attorney took the witness's deposition three weeks before the trial.",
  // Ordering
  "[order-l7]",
]);

let alt = false;
function getVoice(t) {
  // Single words (1-2 words) = student voice = Arthur (Luiz is male)
  if (t.trim().split(/\s+/).length <= 2) return { id: ARTHUR, name: 'Arthur' };
  if (ellenPhrases.has(t)) return { id: ELLEN, name: 'Ellen' };
  if (arthurPhrases.has(t)) return { id: ARTHUR, name: 'Arthur' };
  // Alternate for anything else
  alt = !alt;
  return alt ? { id: ARTHUR, name: 'Arthur' } : { id: ELLEN, name: 'Ellen' };
}

function generate(text, filePath, voice) {
  return new Promise((resolve, reject) => {
    const fullPath = path.join(BASE_DIR, filePath);
    if (fs.existsSync(fullPath)) { console.log(`SKIP (exists): ${filePath}`); return resolve(); }
    const dir = path.dirname(fullPath);
    if (!fs.existsSync(dir)) fs.mkdirSync(dir, { recursive: true });
    const body = JSON.stringify({ text, model_id: 'eleven_monolingual_v1', voice_settings: { stability: 0.5, similarity_boost: 0.75 } });
    const opts = { hostname: 'api.elevenlabs.io', path: `/v1/text-to-speech/${voice.id}`, method: 'POST', headers: { 'xi-api-key': API_KEY, 'Content-Type': 'application/json', Accept: 'audio/mpeg' } };
    const req = https.request(opts, res => {
      if (res.statusCode === 429) { console.log(`RATE LIMITED, waiting 30s...`); setTimeout(() => generate(text, filePath, voice).then(resolve).catch(reject), 30000); return; }
      if (res.statusCode !== 200) { let d = ''; res.on('data', c => d += c); res.on('end', () => { console.error(`ERROR ${res.statusCode}: ${d}`); reject(new Error(d)); }); return; }
      const ws = fs.createWriteStream(fullPath);
      res.pipe(ws);
      ws.on('finish', () => { console.log(`OK [${voice.name}]: ${text.substring(0, 60)}... -> ${filePath}`); resolve(); });
    });
    req.on('error', reject);
    req.write(body);
    req.end();
  });
}

async function main() {
  const entries = Object.entries(audioMap);
  console.log(`\nGenerating ${entries.length} audio files for Luiz Bressane Aula 7...\n`);
  let generated = 0, skipped = 0;
  for (const [text, filePath] of entries) {
    const fullPath = path.join(BASE_DIR, filePath);
    if (fs.existsSync(fullPath)) { skipped++; continue; }
    const voice = getVoice(text);
    try {
      await generate(text, filePath, voice);
      generated++;
      // Delay to avoid rate limiting
      await new Promise(r => setTimeout(r, 500));
    } catch (e) { console.error(`FAILED: ${text.substring(0, 50)}: ${e.message}`); }
  }
  console.log(`\nDone! Generated: ${generated}, Skipped: ${skipped}, Total: ${entries.length}`);
}

main();
