/**
 * Generate ElevenLabs audio for Roberto Rezende - Aula 6 (Following Up)
 *
 * Voice rules:
 * - Roberto (male student): Arthur
 * - Karen Walsh (female character): Ellen
 * - Single words: Arthur
 * - Vocab examples: alternate Arthur/Ellen
 * - Dialogue: Roberto=Arthur, Karen=Ellen
 * - Survival/Quickfire: Arthur
 * - Fill sentences: alternate Arthur/Ellen
 */

const fs = require('fs');
const path = require('path');
const https = require('https');

const ELEVENLABS_API_KEY = process.env.ELEVENLABS_API_KEY;
if (!ELEVENLABS_API_KEY) {
  console.error('ERROR: ELEVENLABS_API_KEY not set');
  process.exit(1);
}

const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';

const OUTPUT_DIR = path.join(__dirname, '..', 'public', 'audio', 'roberto-rezende');

const audioEntries = [
  // === VOCAB WORDS (Arthur — male student) ===
  { text: "Confirm", file: "aula6_confirm.mp3", voice: ARTHUR },
  { text: "Reminder", file: "aula6_reminder.mp3", voice: ARTHUR },
  { text: "Inquiry", file: "aula6_inquiry.mp3", voice: ARTHUR },
  { text: "Availability", file: "aula6_availability.mp3", voice: ARTHUR },
  { text: "Reschedule", file: "aula6_reschedule.mp3", voice: ARTHUR },
  { text: "Agenda", file: "aula6_agenda.mp3", voice: ARTHUR },
  { text: "Feedback", file: "aula6_feedback.mp3", voice: ARTHUR },
  { text: "Attachment", file: "aula6_attachment.mp3", voice: ARTHUR },
  { text: "Regarding", file: "aula6_regarding.mp3", voice: ARTHUR },
  { text: "Forward", file: "aula6_forward.mp3", voice: ARTHUR },

  // === VOCAB EXAMPLES (alternate Arthur/Ellen) ===
  { text: "I will confirm the meeting time by end of day.", file: "aula6_i_will_confirm_the_meeting.mp3", voice: ARTHUR },
  { text: "Could you send me a reminder before the call?", file: "aula6_could_you_send_me_a_reminder.mp3", voice: ELLEN },
  { text: "We received an inquiry from the mining company.", file: "aula6_we_received_an_inquiry.mp3", voice: ARTHUR },
  { text: "Please check your availability for next Tuesday.", file: "aula6_please_check_your_availability.mp3", voice: ELLEN },
  { text: "I am going to reschedule the call to Thursday.", file: "aula6_i_am_going_to_reschedule.mp3", voice: ARTHUR },
  { text: "I will send the agenda before the meeting.", file: "aula6_i_will_send_the_agenda.mp3", voice: ELLEN },
  { text: "We are waiting for feedback from the client.", file: "aula6_we_are_waiting_for_feedback.mp3", voice: ARTHUR },
  { text: "Please find the proposal in the attachment.", file: "aula6_please_find_the_proposal.mp3", voice: ELLEN },
  { text: "I am writing regarding our last conversation.", file: "aula6_i_am_writing_regarding.mp3", voice: ARTHUR },
  { text: "I will forward the email to the engineering team.", file: "aula6_i_will_forward_the_email.mp3", voice: ELLEN },

  // === DIALOGUE (Roberto=Arthur, Karen=Ellen) ===
  { text: "Good morning, Karen. I am calling to follow up on the proposal we sent last week.", file: "aula6_dialogue_roberto1.mp3", voice: ARTHUR },
  { text: "Good morning, Roberto. Yes, I received the attachment. I am going to review it with my team this week.", file: "aula6_dialogue_karen1.mp3", voice: ELLEN },
  { text: "That is great. I will send you an updated agenda for our next meeting. When is your availability?", file: "aula6_dialogue_roberto2.mp3", voice: ARTHUR },
  { text: "I am going to check with my manager. Could you send me a reminder on Wednesday?", file: "aula6_dialogue_karen2.mp3", voice: ELLEN },
  { text: "Of course. I will also forward the technical specifications from our engineering team.", file: "aula6_dialogue_roberto3.mp3", voice: ARTHUR },
  { text: "Perfect. Regarding the pricing, we are going to need a revised estimate before we confirm.", file: "aula6_dialogue_karen3.mp3", voice: ELLEN },
  { text: "I will prepare a revised proposal and send it as an attachment by Friday.", file: "aula6_dialogue_roberto4.mp3", voice: ARTHUR },
  { text: "Sounds good. I will give you feedback as soon as we review everything. We are going to schedule a final call next week.", file: "aula6_dialogue_karen4.mp3", voice: ELLEN },

  // === LISTENING 1 (Arthur — Roberto's follow-up update monologue) ===
  { text: "Good morning, everyone. I am calling to follow up on the proposals we sent to three clients last week. First, the mining company. Karen Walsh confirmed she received the attachment and is going to review it with her team. I will send her an updated agenda and the technical specifications by Wednesday. She is going to need a revised estimate before they confirm. Second, the agricultural client. They sent an inquiry about our generator line. I am going to reschedule the demo to next Thursday because of their availability. I will forward their questions to the engineering team today. Third, the logistics company. I am still waiting for feedback on our proposal. I will send a reminder email this afternoon. We are going to follow up by phone on Friday if there is no response.", file: "aula6_listening1_followup_update.mp3", voice: ARTHUR },

  // === LISTENING 2 (Ellen — Amy's follow-up questions) ===
  { text: "Thank you, Roberto. A few questions. First, regarding the mining company, when is Karen going to give you feedback on the revised estimate? Second, the agricultural client asked about generators. Are you going to include the new models in the demo? Third, you mentioned the logistics company has not responded. Will you reschedule or cancel if they do not reply by Friday? And finally, are you going to confirm all three meetings for next week? Please send me the agenda with updated timelines.", file: "aula6_listening2_amy_followup.mp3", voice: ELLEN },

  // === QUICKFIRE (Arthur) ===
  { text: "I am calling to follow up on the proposal we sent last week.", file: "aula6_quickfire1.mp3", voice: ARTHUR },
  { text: "I will send you the revised estimate as an attachment by Friday.", file: "aula6_quickfire2.mp3", voice: ARTHUR },
  { text: "I am going to reschedule the call to Thursday. Is that available for you?", file: "aula6_quickfire3.mp3", voice: ARTHUR },
  { text: "We are going to need your feedback before we can confirm the order.", file: "aula6_quickfire4.mp3", voice: ARTHUR },
  { text: "I will forward the technical specifications to your team today.", file: "aula6_quickfire5.mp3", voice: ARTHUR },
  { text: "Regarding your inquiry, I am going to prepare a detailed response.", file: "aula6_quickfire6.mp3", voice: ARTHUR },

  // === SURVIVAL (Arthur) ===
  { text: "I am calling to follow up on our proposal.", file: "aula6_survival1.mp3", voice: ARTHUR },
  { text: "I will send you the revised estimate by Friday.", file: "aula6_survival2.mp3", voice: ARTHUR },
  { text: "I am going to reschedule the meeting to next week.", file: "aula6_survival3.mp3", voice: ARTHUR },
  { text: "Please find the attachment regarding our discussion.", file: "aula6_survival4.mp3", voice: ARTHUR },
  { text: "I will confirm the agenda and send a reminder.", file: "aula6_survival5.mp3", voice: ARTHUR },

  // === FILL SENTENCES (alternate) ===
  { text: "I will send you the revised estimate by Friday.", file: "aula6_fill_i_will_send.mp3", voice: ARTHUR },
  { text: "We are going to reschedule the meeting to next week.", file: "aula6_fill_we_are_going_to.mp3", voice: ELLEN },
  { text: "I will confirm the agenda and send a reminder.", file: "aula6_fill_i_will_confirm.mp3", voice: ARTHUR },
  { text: "She is going to review the proposal with her team.", file: "aula6_fill_she_is_going_to.mp3", voice: ELLEN },
  { text: "I will forward the email to the engineering team.", file: "aula6_fill_i_will_forward.mp3", voice: ARTHUR },

  // === ORDERING (Arthur — full follow-up email read aloud) ===
  { text: "Dear Karen, I am writing regarding our last conversation. I will send you the updated specifications as an attachment. Please check your availability for a call next week. I am going to prepare a revised estimate for your team. I will confirm the agenda and send a reminder. Best regards.", file: "order_l6_ordering.mp3", voice: ARTHUR },
];

// Deduplicate by filename
const seen = new Set();
const uniqueEntries = [];
for (const entry of audioEntries) {
  if (!seen.has(entry.file)) {
    seen.add(entry.file);
    uniqueEntries.push(entry);
  }
}

function generateAudio(text, voiceId) {
  return new Promise((resolve, reject) => {
    const payload = JSON.stringify({
      text: text,
      model_id: "eleven_monolingual_v1",
      voice_settings: { stability: 0.5, similarity_boost: 0.75, style: 0.0, use_speaker_boost: true }
    });
    const options = {
      hostname: 'api.elevenlabs.io', port: 443,
      path: `/v1/text-to-speech/${voiceId}`,
      method: 'POST',
      headers: { 'Accept': 'audio/mpeg', 'Content-Type': 'application/json', 'xi-api-key': ELEVENLABS_API_KEY }
    };
    const req = https.request(options, (res) => {
      if (res.statusCode !== 200) { let body = ''; res.on('data', chunk => body += chunk); res.on('end', () => reject(new Error(`HTTP ${res.statusCode}: ${body}`))); return; }
      const chunks = []; res.on('data', chunk => chunks.push(chunk)); res.on('end', () => resolve(Buffer.concat(chunks)));
    });
    req.on('error', reject); req.write(payload); req.end();
  });
}

function sleep(ms) { return new Promise(resolve => setTimeout(resolve, ms)); }

async function main() {
  if (!fs.existsSync(OUTPUT_DIR)) fs.mkdirSync(OUTPUT_DIR, { recursive: true });
  const missing = uniqueEntries.filter(e => !fs.existsSync(path.join(OUTPUT_DIR, e.file)));
  console.log(`Total unique entries: ${uniqueEntries.length}`);
  console.log(`Already exist: ${uniqueEntries.length - missing.length}`);
  console.log(`Missing (to generate): ${missing.length}`);
  if (missing.length === 0) { console.log('All audio files already exist!'); return; }
  let generated = 0, errors = 0;
  for (const entry of missing) {
    const filepath = path.join(OUTPUT_DIR, entry.file);
    const voiceName = entry.voice === ARTHUR ? 'Arthur' : 'Ellen';
    console.log(`[${generated + errors + 1}/${missing.length}] Generating: ${entry.file} (${voiceName}) — "${entry.text.substring(0, 50)}..."`);
    try {
      const audioBuffer = await generateAudio(entry.text, entry.voice);
      fs.writeFileSync(filepath, audioBuffer);
      generated++;
      console.log(`  OK (${(audioBuffer.length / 1024).toFixed(1)} KB)`);
      await sleep(600);
    } catch (err) {
      errors++;
      console.error(`  FAILED: ${err.message}`);
      await sleep(2000);
    }
  }
  console.log(`\nDone! Generated: ${generated}, Errors: ${errors}`);
}

main().catch(console.error);
