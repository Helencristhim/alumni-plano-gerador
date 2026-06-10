const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const JOSH = 'TxGEqnHWrfWFTfGW9XjX';
const DIR = path.join(__dirname, '..', 'public', 'audio', 'rafael-pelizaro');

// Voice rules:
// - Rafael is MALE -> his lines/exercises = ARTHUR
// - David Chen is MALE Sales Rep -> his lines = JOSH (avoid collision with Rafael)
// - Single words = ARTHUR (student gender)
// - General phrases = ALTERNATE Arthur/Ellen
// - Listening 1 = ARTHUR (Rafael presenting)
// - Listening 2 = ELLEN (procurement director, female)

const PHRASES = [
  // ===== Vocab words (Arthur - student male) =====
  { text: "Negotiate", file: "l4_negotiate.mp3", voice: ARTHUR },
  { text: "Proposal", file: "l4_proposal.mp3", voice: ARTHUR },
  { text: "Terms", file: "l4_terms.mp3", voice: ARTHUR },
  { text: "Discount", file: "l4_discount.mp3", voice: ARTHUR },
  { text: "Contract", file: "l4_contract.mp3", voice: ARTHUR },
  { text: "Clause", file: "l4_clause.mp3", voice: ARTHUR },
  { text: "Counteroffer", file: "l4_counteroffer.mp3", voice: ARTHUR },
  { text: "SLA", file: "l4_sla.mp3", voice: ARTHUR },

  // ===== Vocab example sentences (alternate Arthur/Ellen) =====
  { text: "We need to negotiate better terms with the cloud provider.", file: "l4_we_need_to_negotiate_better.mp3", voice: ARTHUR },
  { text: "The vendor sent a proposal for the new infrastructure project.", file: "l4_the_vendor_sent_a_proposal.mp3", voice: ELLEN },
  { text: "The terms of the agreement include a 99.9 percent uptime guarantee.", file: "l4_the_terms_of_the_agreement.mp3", voice: ARTHUR },
  { text: "They offered a 15 percent discount for a two-year commitment.", file: "l4_they_offered_a_15_percent.mp3", voice: ELLEN },
  { text: "We signed a three-year contract with the data center provider.", file: "l4_we_signed_a_three_year.mp3", voice: ARTHUR },
  { text: "There is a penalty clause if they miss the delivery deadline.", file: "l4_there_is_a_penalty_clause.mp3", voice: ELLEN },
  { text: "Our team prepared a counteroffer with adjusted pricing.", file: "l4_our_team_prepared_a_counteroffer.mp3", voice: ARTHUR },
  { text: "The SLA defines response times for critical support tickets.", file: "l4_the_sla_defines_response.mp3", voice: ELLEN },

  // ===== Grammar context sentences (alternate) =====
  { text: "Can you send us the updated proposal by Friday?", file: "l4_can_you_send_us_the_updated.mp3", voice: ARTHUR },
  { text: "Could you offer a better discount for a longer commitment?", file: "l4_could_you_offer_a_better.mp3", voice: ELLEN },
  { text: "We can offer a 10 percent discount if you sign today.", file: "l4_we_can_offer_a_10_percent.mp3", voice: ARTHUR },
  { text: "We could consider extending the SLA if you increase the volume.", file: "l4_we_could_consider_extending.mp3", voice: ELLEN },

  // ===== Fill-in sentences (alternate) =====
  { text: "Can you include a penalty clause in the contract?", file: "l4_fill_can_you_include.mp3", voice: ARTHUR },
  { text: "Could you reduce the implementation timeline?", file: "l4_fill_could_you_reduce.mp3", voice: ELLEN },
  { text: "We can offer free onboarding if you sign a two-year contract.", file: "l4_fill_we_can_offer_free.mp3", voice: ARTHUR },
  { text: "If you increase the volume, we could lower the unit price.", file: "l4_fill_if_you_increase.mp3", voice: ELLEN },
  { text: "Could you share the detailed SLA before we finalize?", file: "l4_fill_could_you_share.mp3", voice: ARTHUR },

  // ===== Dialogue (Rafael=Arthur, David Chen=Josh) =====
  { text: "Good morning, David. Thank you for meeting with us. I have reviewed your proposal for the cloud infrastructure project.", file: "l4_dialogue_rafael_1.mp3", voice: ARTHUR },
  { text: "Good morning, Rafael. I am glad to hear that. What did you think of the terms?", file: "l4_dialogue_david_2.mp3", voice: JOSH },
  { text: "The overall scope looks good, but I have some questions about the pricing. Could you offer a discount for a two-year commitment instead of one year?", file: "l4_dialogue_rafael_3.mp3", voice: ARTHUR },
  { text: "We could consider a 10 percent discount for a two-year contract. Would that work for your budget?", file: "l4_dialogue_david_4.mp3", voice: JOSH },
  { text: "That is a good start. Can you also include a penalty clause if the uptime drops below 99.9 percent?", file: "l4_dialogue_rafael_5.mp3", voice: ARTHUR },
  { text: "We can add that to the SLA. Our standard penalty is a 5 percent credit per incident. Could you share your expected monthly volume so we can finalize the pricing?", file: "l4_dialogue_david_6.mp3", voice: JOSH },
  { text: "Of course. We expect around 500 terabytes per month. If we increase volume next year, could you lower the unit price?", file: "l4_dialogue_rafael_7.mp3", voice: ARTHUR },
  { text: "Absolutely. We can include a volume-based pricing clause in the contract. I will send the updated proposal by Friday.", file: "l4_dialogue_david_8.mp3", voice: JOSH },

  // ===== Listening 1 (Arthur - Rafael presenting negotiation results) =====
  { text: "Good morning, everyone. I am presenting the results of our vendor negotiation for the new cloud infrastructure. We received three proposals from different vendors. After reviewing the terms, we chose CloudScale Solutions. Their original proposal was 450 thousand dollars per year for 500 terabytes. We negotiated a 15 percent discount by committing to a two-year contract, bringing the annual cost to 382 thousand dollars. The SLA includes 99.9 percent uptime with a penalty clause of 5 percent credit per incident. We also negotiated a volume-based pricing clause. If we increase to 800 terabytes, the unit price drops by 12 percent. The contract includes a 90-day exit clause if the service quality declines. Overall, we saved 136 thousand dollars over two years compared to the original proposal.", file: "l4_listening1_vendor_negotiation.mp3", voice: ARTHUR },

  // ===== Listening 2 (Ellen - procurement director questions) =====
  { text: "Rafael, thank you for the vendor update. I have a few questions. First, you mentioned a 15 percent discount. Can you confirm that is locked in for the full two years? Second, the penalty clause covers uptime, but could you also negotiate penalties for response time? If a critical ticket takes more than 4 hours, we need compensation. And finally, the volume-based pricing sounds promising, but what happens if our volume decreases? Can you check if there is a minimum commitment clause?", file: "l4_listening2_procurement_questions.mp3", voice: ELLEN },

  // ===== Survival card L4 (Arthur - student protagonist) =====
  { text: "Could you offer a better discount for a longer commitment?", file: "l4_survival_could_you_offer.mp3", voice: ARTHUR },
  { text: "Can you include a penalty clause in the SLA?", file: "l4_survival_can_you_include.mp3", voice: ARTHUR },
  { text: "We can offer a two-year commitment if you lower the price.", file: "l4_survival_we_can_offer.mp3", voice: ARTHUR },
  { text: "If you increase the volume, could you reduce the unit cost?", file: "l4_survival_if_you_increase.mp3", voice: ARTHUR },
  { text: "I will send our counteroffer by the end of the week.", file: "l4_survival_i_will_send.mp3", voice: ARTHUR },

  // ===== Speech practice L4 (Arthur) =====
  { text: "Could you offer a 15 percent discount if we commit to a two-year contract?", file: "l4_speech_could_you_offer.mp3", voice: ARTHUR },
  { text: "We can include a penalty clause for uptime below 99.9 percent.", file: "l4_speech_we_can_include.mp3", voice: ARTHUR },
  { text: "If we increase the volume next year, can you lower the unit price?", file: "l4_speech_if_we_increase.mp3", voice: ARTHUR }
];

if (!fs.existsSync(DIR)) fs.mkdirSync(DIR, { recursive: true });

async function generate(phrase) {
  const filePath = path.join(DIR, phrase.file);
  if (fs.existsSync(filePath)) {
    console.log(`SKIP (exists): ${phrase.file}`);
    return;
  }
  console.log(`Generating: ${phrase.file} (voice: ${phrase.voice === ARTHUR ? 'Arthur' : phrase.voice === ELLEN ? 'Ellen' : 'Josh'})`);
  const resp = await fetch(`https://api.elevenlabs.io/v1/text-to-speech/${phrase.voice}`, {
    method: 'POST',
    headers: { 'xi-api-key': API_KEY, 'Content-Type': 'application/json' },
    body: JSON.stringify({
      text: phrase.text,
      model_id: 'eleven_multilingual_v2',
      voice_settings: { stability: 0.5, similarity_boost: 0.75 }
    })
  });
  if (!resp.ok) { console.error(`FAIL ${phrase.file}: ${resp.status} ${resp.statusText}`); return; }
  const buffer = Buffer.from(await resp.arrayBuffer());
  fs.writeFileSync(filePath, buffer);
  console.log(`OK: ${phrase.file} (${buffer.length} bytes)`);
}

(async () => {
  console.log(`\n=== Generating ${PHRASES.length} audio files for Rafael Pelizaro Aula 4 ===\n`);
  for (const p of PHRASES) {
    await generate(p);
    await new Promise(r => setTimeout(r, 300));
  }
  console.log('\n=== Done ===\n');
})();
