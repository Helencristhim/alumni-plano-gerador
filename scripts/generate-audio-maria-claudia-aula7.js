const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const DIR = path.join(__dirname, '..', 'public', 'audio', 'maria-claudia-curimbaba');

const PHRASES = [
  // ===== Vocab (Ellen) =====
  { text: "Negotiate", file: "aula7_negotiate.mp3", voice: ELLEN },
  { text: "Proposal", file: "aula7_proposal.mp3", voice: ELLEN },
  { text: "Counteroffer", file: "aula7_counteroffer.mp3", voice: ELLEN },
  { text: "Discount", file: "aula7_discount.mp3", voice: ELLEN },
  { text: "Terms", file: "aula7_terms.mp3", voice: ELLEN },
  { text: "Clause", file: "aula7_clause.mp3", voice: ELLEN },
  { text: "Leverage", file: "aula7_leverage.mp3", voice: ELLEN },
  { text: "Concession", file: "aula7_concession.mp3", voice: ELLEN },

  // ===== Vocab examples (alternate) =====
  { text: "We need to negotiate the price before signing the contract.", file: "aula7_we_need_to_negotiate.mp3", voice: ARTHUR },
  { text: "The vendor submitted a proposal for the new logistics contract.", file: "aula7_the_vendor_submitted.mp3", voice: ELLEN },
  { text: "We will make a counteroffer if the price is too high.", file: "aula7_we_will_make_a_counteroffer.mp3", voice: ARTHUR },
  { text: "If you order in bulk, we will offer a ten percent discount.", file: "aula7_if_you_order_in_bulk.mp3", voice: ELLEN },
  { text: "The payment terms are net 30 days.", file: "aula7_the_payment_terms.mp3", voice: ARTHUR },
  { text: "There is a penalty clause for late delivery.", file: "aula7_there_is_a_penalty_clause.mp3", voice: ELLEN },
  { text: "Our volume gives us leverage to negotiate better prices.", file: "aula7_our_volume_gives_us.mp3", voice: ARTHUR },
  { text: "We made a concession on the delivery timeline.", file: "aula7_we_made_a_concession.mp3", voice: ELLEN },

  // ===== Expressions (alternate) =====
  { text: "If you agree to..., we will...", file: "aula7_expr_if_you_agree.mp3", voice: ARTHUR },
  { text: "If you agree to a two-year contract, we will offer a fifteen percent discount.", file: "aula7_expr_if_you_agree_example.mp3", voice: ELLEN },
  { text: "We are willing to...", file: "aula7_expr_we_are_willing.mp3", voice: ARTHUR },
  { text: "We are willing to extend the payment terms to 60 days.", file: "aula7_expr_willing_example.mp3", voice: ELLEN },
  { text: "On the condition that...", file: "aula7_expr_on_the_condition.mp3", voice: ARTHUR },
  { text: "We will accept the price on the condition that delivery is guaranteed by March.", file: "aula7_expr_condition_example.mp3", voice: ELLEN },

  // ===== Grammar context passage (Ellen) =====
  { text: "Maria Claudia is negotiating a new logistics contract with a vendor in Texas. She reviews the proposal carefully. If the price is too high, she will make a counteroffer. The vendor offers a five percent discount, but Maria Claudia wants ten percent. If you agree to a two-year contract, we will increase the discount to ten percent, the vendor says. Maria Claudia considers the terms. There is a penalty clause for late delivery, which gives her leverage. We are willing to sign for two years on the condition that delivery is guaranteed within five business days, she replies. If both sides make concessions, they will reach an agreement.", file: "aula7_grammar_context_passage.mp3", voice: ELLEN },

  // ===== Fill-in (alternate) =====
  { text: "We need to negotiate the price before signing.", file: "aula7_fill_negotiate_price.mp3", voice: ARTHUR },
  { text: "The vendor submitted a proposal for the new contract.", file: "aula7_fill_vendor_proposal.mp3", voice: ELLEN },
  { text: "We will make a counteroffer if the price is too high.", file: "aula7_fill_counteroffer.mp3", voice: ARTHUR },
  { text: "If you order in bulk, we will offer a ten percent discount.", file: "aula7_fill_discount.mp3", voice: ELLEN },
  { text: "The payment terms are net 30 days.", file: "aula7_fill_payment_terms.mp3", voice: ARTHUR },
  { text: "There is a penalty clause for late delivery.", file: "aula7_fill_penalty_clause.mp3", voice: ELLEN },
  { text: "Our volume gives us leverage to negotiate better prices.", file: "aula7_fill_leverage.mp3", voice: ARTHUR },
  { text: "We made a concession on the delivery timeline.", file: "aula7_fill_concession.mp3", voice: ELLEN },

  // ===== Ordering =====
  { text: "Thank you for your proposal. Let me review the terms. The price seems high. We would like to negotiate. If you offer a ten percent discount, we will sign today. We are willing to extend the contract to two years. On the condition that delivery is guaranteed, we have a deal. Let me prepare the final contract with the agreed terms.", file: "aula7_order_negotiation_sequence.mp3", voice: ELLEN },

  // ===== Survival (Ellen) =====
  { text: "If the price is right, we will sign the contract.", file: "aula7_surv_price_right.mp3", voice: ELLEN },
  { text: "We are willing to negotiate the terms.", file: "aula7_surv_willing_negotiate.mp3", voice: ELLEN },
  { text: "On the condition that delivery is on time, we agree.", file: "aula7_surv_condition_delivery.mp3", voice: ELLEN },
  { text: "We would like to make a counteroffer.", file: "aula7_surv_counteroffer.mp3", voice: ELLEN },
  { text: "If both sides make concessions, we will reach a deal.", file: "aula7_surv_concessions_deal.mp3", voice: ELLEN },

  // ===== Speech (Ellen) =====
  { text: "If the price is too high, we will make a counteroffer.", file: "aula7_speech_counteroffer.mp3", voice: ELLEN },
  { text: "We are willing to extend the payment terms to 60 days.", file: "aula7_speech_willing_extend.mp3", voice: ELLEN },
  { text: "If you agree to a two-year contract, we will offer a discount.", file: "aula7_speech_two_year.mp3", voice: ELLEN },
  { text: "There is a penalty clause for late delivery in the contract.", file: "aula7_speech_penalty_clause.mp3", voice: ELLEN },
  { text: "On the condition that delivery is guaranteed, we will sign.", file: "aula7_speech_condition_sign.mp3", voice: ELLEN },

  // ===== Listening 1 (MC negotiating = Ellen) =====
  { text: "Thank you for the proposal. I have reviewed the terms carefully. The base price of two hundred thousand dollars is higher than we expected. If you can reduce it by ten percent, we will commit to a two-year contract. We also need to discuss the delivery timeline. There is currently no penalty clause for late delivery, and that is a concern for us. If deliveries are late, our production line will stop. We are willing to make a concession on the payment terms. Instead of net 15, we will accept net 30. But on the condition that delivery is guaranteed within five business days. If we can agree on these terms, I am ready to sign today.", file: "aula7_ic_listening1_mc_negotiates.mp3", voice: ELLEN },

  // ===== Listening 2 (David = Arthur) =====
  { text: "Maria Claudia, let me share how we handled a similar negotiation in Pittsburgh last month. The vendor's initial proposal was three hundred thousand dollars. We knew we had leverage because we are their largest client. If we threatened to switch vendors, they would lose significant revenue. So we made a counteroffer at two hundred and fifty thousand. They came back with two hundred and seventy-five. We were willing to accept that price on the condition that they included free shipping. In the end, both sides made concessions. We paid a slightly higher price, but they added a penalty clause for late delivery and extended the warranty. If you use your leverage wisely, you will always get better terms.", file: "aula7_ic_listening2_david_strategy.mp3", voice: ARTHUR },

  // ===== Dialogue =====
  { text: "Thank you for meeting with us today. I have reviewed your proposal.", file: "aula7_ic_dlg_mc_1.mp3", voice: ELLEN },
  { text: "Thank you, Maria Claudia. We believe the terms are very competitive.", file: "aula7_ic_dlg_vendor_1.mp3", voice: ARTHUR },
  { text: "The quality is excellent, but the price is higher than expected. If you offer a ten percent discount, we will sign for two years.", file: "aula7_ic_dlg_mc_2.mp3", voice: ELLEN },
  { text: "Ten percent is significant. We are willing to offer seven percent. If you increase the order volume, we will consider a higher discount.", file: "aula7_ic_dlg_vendor_2.mp3", voice: ARTHUR },
  { text: "We can increase the volume by twenty percent. But on the condition that delivery is guaranteed within five days.", file: "aula7_ic_dlg_mc_3.mp3", voice: ELLEN },
  { text: "Five days is tight, but we can manage it. If we add a penalty clause for late delivery, will that give you confidence?", file: "aula7_ic_dlg_vendor_3.mp3", voice: ARTHUR },
  { text: "Yes, that is exactly what we need. We are also willing to extend the payment terms to net 30.", file: "aula7_ic_dlg_mc_4.mp3", voice: ELLEN },
  { text: "Net 30 works for us. So the final terms are: ten percent discount, two-year contract, five-day delivery with penalty clause.", file: "aula7_ic_dlg_vendor_4.mp3", voice: ARTHUR },
  { text: "Agreed. If both sides honor these terms, this will be a very successful partnership.", file: "aula7_ic_dlg_mc_5.mp3", voice: ELLEN },
  { text: "Absolutely. Let me prepare the final contract. We have a deal, Maria Claudia.", file: "aula7_ic_dlg_vendor_5.mp3", voice: ARTHUR },

  // ===== Error correction =====
  { text: "If we will increase the order, they offer a discount.", file: "aula7_ic_error_will_increase.mp3", voice: ARTHUR },
  { text: "If the price is too high, we making a counteroffer.", file: "aula7_ic_error_we_making.mp3", voice: ELLEN },
  { text: "We are willing to signing the contract.", file: "aula7_ic_error_willing_signing.mp3", voice: ARTHUR },
  { text: "On the condition that delivery will be guaranteed.", file: "aula7_ic_error_will_be.mp3", voice: ELLEN },
  { text: "If both sides will make concessions, we reach a deal.", file: "aula7_ic_error_both_will.mp3", voice: ARTHUR },
];

async function gen(text, voiceId, outPath) {
  const r = await fetch('https://api.elevenlabs.io/v1/text-to-speech/' + voiceId, {
    method: 'POST',
    headers: { 'xi-api-key': API_KEY, 'Content-Type': 'application/json' },
    body: JSON.stringify({ text, model_id: 'eleven_multilingual_v2', voice_settings: { stability: 0.5, similarity_boost: 0.75 } }),
  });
  if (!r.ok) throw new Error(r.status + ': ' + (await r.text()));
  const buf = Buffer.from(await r.arrayBuffer());
  fs.writeFileSync(outPath, buf);
  return buf.length;
}

async function main() {
  if (!API_KEY) { console.error('Set ELEVENLABS_API_KEY env var'); process.exit(1); }
  if (!fs.existsSync(DIR)) fs.mkdirSync(DIR, { recursive: true });
  const seen = new Set();
  const unique = PHRASES.filter(p => { const k = p.file.toLowerCase(); if (seen.has(k)) return false; seen.add(k); return true; });
  console.log('Generating ' + unique.length + ' AULA 7 audio files...');
  let generated = 0, skipped = 0;
  for (const p of unique) {
    const outPath = path.join(DIR, p.file);
    if (fs.existsSync(outPath)) { console.log('SKIP: ' + p.file); skipped++; }
    else {
      try {
        const bytes = await gen(p.text, p.voice, outPath);
        console.log('OK [' + (p.voice === ELLEN ? 'ellen' : 'arthur') + ']: ' + p.file + ' (' + (bytes / 1024).toFixed(1) + 'KB)');
        generated++;
        await new Promise(r => setTimeout(r, 500));
      } catch (e) { console.error('FAIL: ' + p.file + ' — ' + e.message); }
    }
  }
  console.log('\nDone! Generated: ' + generated + ' | Skipped: ' + skipped + ' | Total: ' + unique.length);
}
main();
