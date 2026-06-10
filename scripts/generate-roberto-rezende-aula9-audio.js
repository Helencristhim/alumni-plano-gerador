/**
 * Generate ElevenLabs audio for Roberto Rezende - Aula 9 (Email Essentials)
 * Voice: Roberto (male student) = Arthur, Lisa Chen (female) = Ellen
 */
const fs = require('fs');
const path = require('path');
const https = require('https');

const ELEVENLABS_API_KEY = process.env.ELEVENLABS_API_KEY;
if (!ELEVENLABS_API_KEY) { console.error('ERROR: ELEVENLABS_API_KEY not set'); process.exit(1); }

const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const OUTPUT_DIR = path.join(__dirname, '..', 'public', 'audio', 'roberto-rezende');

const audioEntries = [
  // VOCAB WORDS (Arthur - male student - 10)
  { text: "Regarding", file: "aula9_regarding.mp3", voice: ARTHUR },
  { text: "Attachment", file: "aula9_attachment.mp3", voice: ARTHUR },
  { text: "Acknowledge", file: "aula9_acknowledge.mp3", voice: ARTHUR },
  { text: "Clarify", file: "aula9_clarify.mp3", voice: ARTHUR },
  { text: "Inquire", file: "aula9_inquire.mp3", voice: ARTHUR },
  { text: "Notify", file: "aula9_notify.mp3", voice: ARTHUR },
  { text: "Approve", file: "aula9_approve.mp3", voice: ARTHUR },
  { text: "Outline", file: "aula9_outline.mp3", voice: ARTHUR },
  { text: "Forward", file: "aula9_forward.mp3", voice: ARTHUR },
  { text: "Follow through", file: "aula9_follow_through.mp3", voice: ARTHUR },

  // VOCAB EXAMPLES (alternate Arthur/Ellen - 10)
  { text: "I am writing regarding the proposal we discussed at the trade fair.", file: "aula9_i_am_writing_regarding_the_proposal.mp3", voice: ARTHUR },
  { text: "Please find the contract attached for your review.", file: "aula9_please_find_the_contract_attached.mp3", voice: ELLEN },
  { text: "I would like to acknowledge receipt of your email.", file: "aula9_i_would_like_to_acknowledge_receipt.mp3", voice: ARTHUR },
  { text: "Could you clarify the delivery timeline for the engines?", file: "aula9_could_you_clarify_the_delivery_timeline.mp3", voice: ELLEN },
  { text: "I am writing to inquire about the status of our order.", file: "aula9_i_am_writing_to_inquire_about_the_status.mp3", voice: ARTHUR },
  { text: "I wanted to notify you that the shipment has been delayed.", file: "aula9_i_wanted_to_notify_you_that_the_shipment.mp3", voice: ELLEN },
  { text: "The regional manager has approved the new pricing structure.", file: "aula9_the_regional_manager_has_approved.mp3", voice: ARTHUR },
  { text: "I will outline the key points of our proposal below.", file: "aula9_i_will_outline_the_key_points.mp3", voice: ELLEN },
  { text: "I have forwarded your message to the logistics team.", file: "aula9_i_have_forwarded_your_message.mp3", voice: ARTHUR },
  { text: "We need to follow through on our commitments to this client.", file: "aula9_we_need_to_follow_through.mp3", voice: ELLEN },

  // DIALOGUE (Roberto=Arthur, Lisa=Ellen - 8 lines)
  { text: "Hi Roberto. I reviewed your email draft. The content is good, however, you need to use more formal language.", file: "aula9_dialogue_lisa1.mp3", voice: ELLEN },
  { text: "What do you mean by formal language? I thought my email was clear.", file: "aula9_dialogue_roberto1.mp3", voice: ARTHUR },
  { text: "It is clear, but for clients, we use linking words like however, therefore, and in addition. Furthermore, we avoid contractions.", file: "aula9_dialogue_lisa2.mp3", voice: ELLEN },
  { text: "I see. So instead of writing I want to tell you about the deal, I should write I am writing to notify you regarding the deal.", file: "aula9_dialogue_roberto2.mp3", voice: ARTHUR },
  { text: "Exactly. In addition, always start with the purpose. For example, I am writing regarding our meeting on Friday.", file: "aula9_dialogue_lisa3.mp3", voice: ELLEN },
  { text: "What about ending the email? I usually write Thanks and my name.", file: "aula9_dialogue_roberto3.mp3", voice: ARTHUR },
  { text: "For formal emails, use I look forward to hearing from you or Please do not hesitate to contact me. Therefore, your closing feels more professional.", file: "aula9_dialogue_lisa4.mp3", voice: ELLEN },
  { text: "That makes sense. I will rewrite the email and forward it to you for review.", file: "aula9_dialogue_roberto4.mp3", voice: ARTHUR },

  // LISTENING 1 (Ellen - Lisa's email writing tips monologue)
  { text: "Good morning, team. Today I want to share some tips on writing professional emails. First, always state your purpose clearly in the opening line. Write I am writing regarding or I am writing to inquire about. Second, use linking words to connect your ideas. However shows contrast. Therefore shows result. In addition and furthermore add information. Third, avoid contractions. Write I am instead of I'm, do not instead of don't. Fourth, always acknowledge emails you receive. A simple Thank you for your email regarding the proposal is enough. Fifth, end with a professional closing: I look forward to your reply, or Please do not hesitate to contact me. As per company policy, always include your full signature with title and contact information.", file: "aula9_listening1_email_tips.mp3", voice: ELLEN },

  // LISTENING 2 (Arthur - Roberto's questions)
  { text: "Thank you, Lisa. That was very useful. I have a few questions. First, you mentioned we should use linking words. Can you give us an example of how to use however and therefore in the same email? Second, when should we use regarding versus about? Is regarding always better? Third, you said to acknowledge emails. What if the email does not require a response? Should we still reply? Finally, what is the difference between attachment and enclosed? I hear both in business emails.", file: "aula9_listening2_roberto_questions.mp3", voice: ARTHUR },

  // QUICKFIRE (Arthur - 6)
  { text: "I am writing regarding the proposal we discussed.", file: "aula9_quickfire1.mp3", voice: ARTHUR },
  { text: "Please find the updated contract attached.", file: "aula9_quickfire2.mp3", voice: ARTHUR },
  { text: "I would like to clarify the delivery schedule.", file: "aula9_quickfire3.mp3", voice: ARTHUR },
  { text: "However, we need to review the pricing first.", file: "aula9_quickfire4.mp3", voice: ARTHUR },
  { text: "I look forward to hearing from you.", file: "aula9_quickfire5.mp3", voice: ARTHUR },
  { text: "Therefore, I suggest we schedule a meeting next week.", file: "aula9_quickfire6.mp3", voice: ARTHUR },

  // SURVIVAL (Arthur - 5)
  { text: "I am writing regarding the contract we discussed.", file: "aula9_survival1.mp3", voice: ARTHUR },
  { text: "Please find the document attached for your review.", file: "aula9_survival2.mp3", voice: ARTHUR },
  { text: "I would like to acknowledge receipt of your email.", file: "aula9_survival3.mp3", voice: ARTHUR },
  { text: "However, I would like to clarify a few points.", file: "aula9_survival4.mp3", voice: ARTHUR },
  { text: "I look forward to hearing from you at your earliest convenience.", file: "aula9_survival5.mp3", voice: ARTHUR },

  // ORDERING (Arthur - email sequence)
  { text: "Dear Mr. Silva, I am writing regarding our meeting at the trade fair. However, the delivery timeline is eight to ten weeks. In addition, I have attached the updated catalog. I look forward to hearing from you.", file: "order_l9_ordering.mp3", voice: ARTHUR },

  // FILL-IN-THE-BLANK phrases (for Pre-class)
  { text: "The price is high. However, the quality is excellent.", file: "aula9_the_price_is_high_however.mp3", voice: ELLEN },
  { text: "The client approved the order. Therefore, we can proceed with production.", file: "aula9_the_client_approved_therefore.mp3", voice: ARTHUR },
];

const seen = new Set();
const uniqueEntries = [];
for (const entry of audioEntries) { if (!seen.has(entry.file)) { seen.add(entry.file); uniqueEntries.push(entry); } }

function generateAudio(text, voiceId) {
  return new Promise((resolve, reject) => {
    const payload = JSON.stringify({ text, model_id: "eleven_monolingual_v1", voice_settings: { stability: 0.5, similarity_boost: 0.75, style: 0.0, use_speaker_boost: true } });
    const options = { hostname: 'api.elevenlabs.io', port: 443, path: `/v1/text-to-speech/${voiceId}`, method: 'POST', headers: { 'Accept': 'audio/mpeg', 'Content-Type': 'application/json', 'xi-api-key': ELEVENLABS_API_KEY } };
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
    } catch (err) { errors++; console.error(`  FAILED: ${err.message}`); await sleep(2000); }
  }
  console.log(`\nDone! Generated: ${generated}, Errors: ${errors}`);
}
main().catch(console.error);
