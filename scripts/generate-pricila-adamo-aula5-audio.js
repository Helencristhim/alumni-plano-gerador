const fs = require('fs');
const path = require('path');
const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const DIR = path.join(__dirname, '..', 'public', 'audio', 'pricila-adamo');

const PHRASES = [
  { text: "Wellness", voice: ARTHUR, file: "aula5_wellness.mp3" },
  { text: "Balance", voice: ARTHUR, file: "aula5_balance.mp3" },
  { text: "Mindful", voice: ARTHUR, file: "aula5_mindful.mp3" },
  { text: "Symptom", voice: ARTHUR, file: "aula5_symptom.mp3" },
  { text: "Prescription", voice: ARTHUR, file: "aula5_prescription.mp3" },
  { text: "Relief", voice: ARTHUR, file: "aula5_relief.mp3" },
  { text: "Prevent", voice: ARTHUR, file: "aula5_prevent.mp3" },
  { text: "Recommend", voice: ARTHUR, file: "aula5_recommend.mp3" },
  { text: "Recovery", voice: ARTHUR, file: "aula5_recovery.mp3" },
  { text: "Habit", voice: ARTHUR, file: "aula5_habit.mp3" },
  { text: "Wellness is not just about your body, it is about your mind too.", voice: ARTHUR, file: "aula5_wellness_sentence.mp3" },
  { text: "You should find a good balance between work and rest.", voice: ELLEN, file: "aula5_balance_sentence.mp3" },
  { text: "Being mindful helps you reduce stress and enjoy the moment.", voice: ARTHUR, file: "aula5_mindful_sentence.mp3" },
  { text: "If you have any symptoms, you should see a doctor.", voice: ELLEN, file: "aula5_symptom_sentence.mp3" },
  { text: "The doctor gave me a prescription for the medicine.", voice: ARTHUR, file: "aula5_prescription_sentence.mp3" },
  { text: "I felt relief when the headache finally went away.", voice: ELLEN, file: "aula5_relief_sentence.mp3" },
  { text: "Exercise and good food can help prevent many diseases.", voice: ARTHUR, file: "aula5_prevent_sentence.mp3" },
  { text: "I would recommend walking thirty minutes every day.", voice: ELLEN, file: "aula5_recommend_sentence.mp3" },
  { text: "Recovery after surgery takes time and patience.", voice: ARTHUR, file: "aula5_recovery_sentence.mp3" },
  { text: "Drinking water is a simple but important habit.", voice: ELLEN, file: "aula5_habit_sentence.mp3" },
  { text: "You should...", voice: ARTHUR, file: "aula5_expr_you_should.mp3" },
  { text: "You could try...", voice: ELLEN, file: "aula5_expr_you_could.mp3" },
  { text: "It might help to...", voice: ARTHUR, file: "aula5_expr_it_might.mp3" },
  { text: "I would recommend...", voice: ELLEN, file: "aula5_expr_recommend.mp3" },
  { text: "The best thing you could do is...", voice: ARTHUR, file: "aula5_expr_best_thing.mp3" },
  // Dialogue: Dr. Carter = Arthur, Pricila = Ellen
  { text: "Good morning, Pricila! How are you feeling today? Any symptoms I should know about?", voice: ARTHUR, file: "aula5_dialogue_carter_1.mp3" },
  { text: "I have been feeling tired lately. I think I need to find a better balance in my life.", voice: ELLEN, file: "aula5_dialogue_pricila_1.mp3" },
  { text: "That is very common during big life changes. You should make sure you are getting enough sleep. I would also recommend daily walks.", voice: ARTHUR, file: "aula5_dialogue_carter_2.mp3" },
  { text: "I have heard that being mindful could help with stress. What do you think?", voice: ELLEN, file: "aula5_dialogue_pricila_2.mp3" },
  { text: "Absolutely! Mindfulness is a great habit. It might help you feel more relaxed and prevent burnout.", voice: ARTHUR, file: "aula5_dialogue_carter_3.mp3" },
  { text: "That is a relief to hear. As a dentist, I know about wellness, but I have not been following my own advice.", voice: ELLEN, file: "aula5_dialogue_pricila_3.mp3" },
  { text: "The best thing you could do is start small. No prescription needed — just good habits and patience. Recovery from stress takes time.", voice: ARTHUR, file: "aula5_dialogue_carter_4.mp3" },
  { text: "Thank you, Doctor. I am going to embrace this new chapter of my life with better habits.", voice: ELLEN, file: "aula5_dialogue_pricila_4.mp3" },
  // Listening 1: Pricila's wellness routine (Ellen)
  { text: "Since I started thinking about retirement, I have been paying more attention to my wellness. As a dentist, I spent decades standing all day, and now I have some back pain. My doctor recommended walking thirty minutes every day, and I should say, it has made a huge difference. I also started being more mindful. I try to enjoy the present moment instead of worrying about the future. One habit I want to develop is drinking more water. It sounds simple, but I always forget. I think the best thing I could do is find a good balance between activity and rest. Prevention is better than recovery, as we say in medicine. I might even try yoga. My friend said it could help with flexibility. The most important thing is that I feel relief knowing I am taking care of myself.", voice: ELLEN, file: "aula5_listening_1_wellness_routine.mp3" },
  // Listening 2: Dr. Carter's advice (Arthur)
  { text: "I have been a doctor for over twenty years, and the most common symptom I see in patients over fifty is stress. My recommendation is always the same: you should focus on prevention, not just treatment. Good habits are the best medicine. You should walk every day, even if it is just fifteen minutes. You could try meditation or mindfulness. It might feel strange at first, but many patients tell me it changed their lives. Balance is the key word. You should not work too much or rest too much. Find the right balance. And if you have any symptoms that worry you, do not wait. See a doctor. Sometimes a simple prescription can bring relief. But most of the time, recovery starts with small changes in your daily habits.", voice: ARTHUR, file: "aula5_listening_2_doctor_advice.mp3" },
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
  console.log('Generating ' + PHRASES.length + ' audio files for Pricila Adamo — Aula 5...');
  let generated = 0, skipped = 0;
  for (const p of PHRASES) {
    const outPath = path.join(DIR, p.file);
    if (fs.existsSync(outPath)) { console.log('SKIP: ' + p.file); skipped++; }
    else {
      try {
        const bytes = await gen(p.text, p.voice, outPath);
        console.log('OK [' + (p.voice === ELLEN ? 'ellen' : 'arthur') + ']: ' + p.file + ' (' + (bytes/1024).toFixed(1) + 'KB)');
        generated++;
        await new Promise(r => setTimeout(r, 500));
      } catch(e) { console.error('FAIL: ' + p.file + ' — ' + e.message); }
    }
  }
  console.log('\nDone! Generated: ' + generated + ', Skipped: ' + skipped + ', Total: ' + PHRASES.length);
}

main().catch(e => { console.error(e); process.exit(1); });
