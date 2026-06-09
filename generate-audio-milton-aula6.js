const fs = require('fs');
const path = require('path');
const https = require('https');

const ELEVENLABS_API_KEY = process.env.ELEVENLABS_API_KEY;
if (!ELEVENLABS_API_KEY) { console.error('ERROR: ELEVENLABS_API_KEY not set'); process.exit(1); }

// Voices: Arthur (male, neutral) / Ellen (female, calm) — alternating
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const OUTPUT_DIR = path.join(__dirname, 'public', 'audio', 'milton-sayegh');

// Milton = male → protagonist voice = Arthur
// Alternating for general phrases
const audioEntries = [
  // VOCAB WORDS (Milton = Arthur)
  { text: "Subject Line", file: "subject_line.mp3", voice: ARTHUR },
  { text: "Recipient", file: "recipient.mp3", voice: ARTHUR },
  { text: "Attachment", file: "attachment.mp3", voice: ARTHUR },
  { text: "Deadline", file: "deadline_email.mp3", voice: ARTHUR },
  { text: "CC", file: "cc.mp3", voice: ARTHUR },
  { text: "Follow Up", file: "follow_up.mp3", voice: ARTHUR },
  { text: "Proofread", file: "proofread.mp3", voice: ARTHUR },
  { text: "Regards", file: "regards.mp3", voice: ARTHUR },
  { text: "Forward", file: "forward_email.mp3", voice: ARTHUR },
  { text: "Greeting", file: "greeting_email.mp3", voice: ARTHUR },

  // VOCAB EXAMPLE SENTENCES (alternating)
  { text: "A clear subject line helps the recipient understand the purpose of your email.", file: "a_clear_subject_line_helps_the_recipient.mp3", voice: ARTHUR },
  { text: "Please find the attachment with the updated contract.", file: "please_find_the_attachment_with_the_updated.mp3", voice: ELLEN },
  { text: "The deadline for the proposal is next Friday.", file: "the_deadline_for_the_proposal_is_next_friday.mp3", voice: ARTHUR },
  { text: "I will CC the legal team on this email.", file: "i_will_cc_the_legal_team_on_this_email.mp3", voice: ELLEN },
  { text: "I am writing to follow up on our previous conversation.", file: "i_am_writing_to_follow_up_on_our_previous.mp3", voice: ARTHUR },
  { text: "Please proofread the document before sending it.", file: "please_proofread_the_document_before_sending.mp3", voice: ELLEN },
  { text: "Best regards, Milton Sayegh.", file: "best_regards_milton_sayegh.mp3", voice: ARTHUR },
  { text: "Could you forward this email to the sales team?", file: "could_you_forward_this_email_to_the_sales.mp3", voice: ELLEN },
  { text: "The greeting sets the tone for a professional email.", file: "the_greeting_sets_the_tone_for_a_professional.mp3", voice: ARTHUR },
  { text: "I would like to confirm the details of our agreement.", file: "i_would_like_to_confirm_the_details.mp3", voice: ARTHUR },

  // LINKING WORD SENTENCES (alternating)
  { text: "Furthermore, we need to review the shipping schedule.", file: "furthermore_we_need_to_review_the_shipping.mp3", voice: ARTHUR },
  { text: "However, the client has requested a different delivery date.", file: "however_the_client_has_requested_a_different.mp3", voice: ELLEN },
  { text: "Therefore, I suggest we schedule a call to discuss this matter.", file: "therefore_i_suggest_we_schedule_a_call.mp3", voice: ARTHUR },
  { text: "Regarding your inquiry about pricing, please see the attached document.", file: "regarding_your_inquiry_about_pricing.mp3", voice: ELLEN },
  { text: "In addition, I have included the latest catalog for your review.", file: "in_addition_i_have_included_the_latest.mp3", voice: ARTHUR },

  // EMAIL ARTIFACT PHRASES (Milton = Arthur)
  { text: "Dear Ms. Chen, Thank you for your interest in our products.", file: "dear_ms_chen_thank_you_for_your_interest.mp3", voice: ARTHUR },
  { text: "I am pleased to inform you that we have approved the order.", file: "i_am_pleased_to_inform_you.mp3", voice: ARTHUR },
  { text: "However, we will need to adjust the delivery timeline.", file: "however_we_will_need_to_adjust.mp3", voice: ARTHUR },
  { text: "Furthermore, our quality team will inspect all items before shipment.", file: "furthermore_our_quality_team_will_inspect.mp3", voice: ARTHUR },
  { text: "Therefore, please confirm the shipping address at your earliest convenience.", file: "therefore_please_confirm_the_shipping_address.mp3", voice: ARTHUR },
  { text: "In addition, I have attached our latest price list for your reference.", file: "in_addition_i_have_attached_our_latest.mp3", voice: ARTHUR },
  { text: "I look forward to a successful partnership.", file: "i_look_forward_to_a_successful_partnership.mp3", voice: ARTHUR },
  { text: "Best regards, Milton Sayegh, Export Director, Sayegh Jewelry.", file: "best_regards_milton_sayegh_export_director.mp3", voice: ARTHUR },

  // DIALOGUE (Milton = Arthur protagonist)
  { text: "Dear Mr. Rodriguez, I hope this message finds you well.", file: "dear_mr_rodriguez_i_hope_this_message.mp3", voice: ARTHUR },
  { text: "I am writing to follow up on the contract we discussed at the trade show.", file: "i_am_writing_to_follow_up_on_the_contract.mp3", voice: ARTHUR },
  { text: "As per our conversation, we agreed on exclusive distribution rights for California.", file: "as_per_our_conversation_we_agreed.mp3", voice: ARTHUR },
  { text: "However, I noticed that the draft contract does not include the exclusivity clause.", file: "however_i_noticed_that_the_draft_contract.mp3", voice: ARTHUR },
  { text: "Furthermore, the payment terms need to be revised to net 45 days.", file: "furthermore_the_payment_terms_need.mp3", voice: ARTHUR },
  { text: "Therefore, I kindly request that you update the document and send it back by Friday.", file: "therefore_i_kindly_request_that_you_update.mp3", voice: ARTHUR },
  { text: "Please do not hesitate to reach out if you need any clarification.", file: "please_do_not_hesitate_to_reach_out.mp3", voice: ARTHUR },

  // PRONUNCIATION PHRASES (Milton = Arthur)
  { text: "I look forward to hearing from you.", file: "i_look_forward_to_hearing_from_you.mp3", voice: ARTHUR },
  { text: "I am writing to inform you about a change in our delivery schedule.", file: "i_am_writing_to_inform_you_about_a_change.mp3", voice: ARTHUR },
  { text: "As discussed in our last meeting, the new terms are as follows.", file: "as_discussed_in_our_last_meeting.mp3", voice: ARTHUR },
  { text: "Please do not hesitate to contact me if you have any questions.", file: "please_do_not_hesitate_to_contact_me.mp3", voice: ARTHUR },
  { text: "I am writing regarding the partnership agreement we discussed last week.", file: "i_am_writing_regarding_the_partnership.mp3", voice: ARTHUR },

  // ORDERING EXERCISE
  { text: "Dear Mr. Rodriguez. I hope this message finds you well. I am writing regarding the contract we discussed at the trade show. I look forward to hearing from you. Best regards, Milton Sayegh.", file: "order_l6_ordering.mp3", voice: ARTHUR },
];

if (!fs.existsSync(OUTPUT_DIR)) fs.mkdirSync(OUTPUT_DIR, { recursive: true });

function generateAudio(entry) {
  return new Promise((resolve, reject) => {
    const filePath = path.join(OUTPUT_DIR, entry.file);
    if (fs.existsSync(filePath)) {
      console.log(`SKIP (exists): ${entry.file}`);
      return resolve();
    }

    const data = JSON.stringify({
      text: entry.text,
      model_id: 'eleven_monolingual_v1',
      voice_settings: { stability: 0.5, similarity_boost: 0.75 }
    });

    const options = {
      hostname: 'api.elevenlabs.io',
      path: `/v1/text-to-speech/${entry.voice}`,
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'xi-api-key': ELEVENLABS_API_KEY,
        'Content-Length': Buffer.byteLength(data)
      }
    };

    const req = https.request(options, (res) => {
      if (res.statusCode !== 200) {
        let body = '';
        res.on('data', d => body += d);
        res.on('end', () => {
          console.error(`ERROR ${res.statusCode} for "${entry.text}": ${body}`);
          resolve();
        });
        return;
      }
      const chunks = [];
      res.on('data', chunk => chunks.push(chunk));
      res.on('end', () => {
        fs.writeFileSync(filePath, Buffer.concat(chunks));
        console.log(`OK: ${entry.file} (${entry.voice === ARTHUR ? 'Arthur' : 'Ellen'})`);
        resolve();
      });
    });

    req.on('error', (e) => { console.error(`NETWORK ERROR: ${e.message}`); resolve(); });
    req.write(data);
    req.end();
  });
}

async function main() {
  console.log(`Generating ${audioEntries.length} audio files for Milton Aula 6...`);
  console.log(`Output: ${OUTPUT_DIR}\n`);

  for (let i = 0; i < audioEntries.length; i++) {
    await generateAudio(audioEntries[i]);
    // Rate limiting: 100ms between requests
    await new Promise(r => setTimeout(r, 100));
  }

  console.log('\nDone!');
}

main();
