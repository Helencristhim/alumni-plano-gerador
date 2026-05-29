const fs = require('fs');
const path = require('path');
const https = require('https');

const ELEVENLABS_API_KEY = process.env.ELEVENLABS_API_KEY;
if (!ELEVENLABS_API_KEY) { console.error('ERROR: ELEVENLABS_API_KEY not set'); process.exit(1); }

const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const OUTPUT_DIR = path.join(__dirname, '..', 'public', 'audio', 'eduardo-chiba');

// All Aula 3 phrases from Eduardo Chiba's professor audioMap
const audioMap = {
  // Vocab words (1-2 word terms) → always Arthur
  "Proposal": "aula3_proposal.mp3",
  "Negotiate": "aula3_negotiate.mp3",
  "Terms": "aula3_terms.mp3",
  "Mutual": "aula3_mutual.mp3",
  "Commitment": "aula3_commitment.mp3",
  "Collaboration": "aula3_collaboration.mp3",
  "Prospect": "aula3_prospect.mp3",
  "Follow-up": "aula3_follow_up.mp3",

  // Vocab example sentences
  "We sent a proposal to the agency last week.": "aula3_ex_proposal.mp3",
  "We need to negotiate the commission rate before signing.": "aula3_ex_negotiate.mp3",
  "The terms of the partnership include a two-year commitment.": "aula3_ex_terms.mp3",
  "This partnership is based on mutual benefit.": "aula3_ex_mutual.mp3",
  "We value long-term commitment from our partners.": "aula3_ex_commitment.mp3",
  "The collaboration between our teams has been very productive.": "aula3_ex_collaboration.mp3",
  "We have several new prospects in the northeast region.": "aula3_ex_prospect.mp3",
  "I will send a follow-up email after our meeting today.": "aula3_ex_follow_up.mp3",

  // Fill-in-the-blank sentences
  "Could you send me the partnership proposal by Friday?": "aula3_fill1.mp3",
  "We would be happy to negotiate the terms of the agreement.": "aula3_fill2.mp3",
  "I will send a follow-up email after our meeting.": "aula3_fill3.mp3",
  "This partnership is based on mutual benefit.": "aula3_fill4.mp3",
  "We have three new prospects in the northeast region.": "aula3_fill5.mp3",
  "Would you mind reviewing our partnership terms?": "aula3_fill6.mp3",

  // Pronunciation sentences
  "Could we schedule a call to discuss the partnership terms?": "aula3_pron1.mp3",
  "We would be happy to negotiate flexible commission rates.": "aula3_pron2.mp3",
  "Would you mind reviewing our proposal before the next meeting?": "aula3_pron3.mp3",

  // Order exercise monologue
  "[order-l3]": "aula3_order_partnership.mp3",

  // Dialogue — Ana lines (female → Ellen)
  "Good morning, Eduardo. Thank you for coming. Could you tell me more about your proposal?": "aula3_dialogue_ana_line1.mp3",
  "Interesting. What kind of commission structure would you offer?": "aula3_dialogue_ana_line3.mp3",
  "Not at all. And what about the commitment period? How long would the contract be?": "aula3_dialogue_ana_line5.mp3",
  "That sounds reasonable. Could you send me a formal proposal by Friday?": "aula3_dialogue_ana_line7.mp3",

  // Dialogue — Eduardo lines (male → Arthur)
  "Of course. I would like to present our partnership terms. We believe this could be a great collaboration.": "aula3_dialogue_eduardo_line2.mp3",
  "We could offer flexible rates based on your volume. Would you mind if I walk you through the numbers?": "aula3_dialogue_eduardo_line4.mp3",
  "We would propose a twelve-month commitment, but we could negotiate the terms if needed.": "aula3_dialogue_eduardo_line6.mp3",
  "Absolutely. I will send a follow-up email today with the full proposal. Thank you for considering this prospect.": "aula3_dialogue_eduardo_line8.mp3",

  // Listening monologues (long-form, generated as single MP3)
  "aula3_listening1_call": "aula3_listening1_call.mp3",
  "aula3_listening2_negotiation": "aula3_listening2_negotiation.mp3",

  // Quick fire answers
  "I would like to present our partnership proposal. Could we schedule a call to discuss the terms?": "aula3_qf1.mp3",
  "Could we discuss the commission structure? We could offer flexible rates based on your volume.": "aula3_qf2.mp3",
  "Would you mind reviewing our proposal before our call next week?": "aula3_qf3.mp3",
  "We would propose a twelve-month commitment. We could negotiate better terms for a longer period.": "aula3_qf4.mp3",
  "Thank you for meeting with me. I will send a follow-up email with our full proposal. Could we schedule a call next week?": "aula3_qf5.mp3",
  "We believe in mutual benefit and long-term collaboration. We negotiate transparent terms with every prospect.": "aula3_qf6.mp3",

  // Oral models
  "Could we schedule a meeting to discuss our partnership proposal?": "aula3_oral1.mp3",
  "We would be happy to negotiate flexible terms for your agency.": "aula3_oral2.mp3",
  "Would you mind reviewing the partnership terms before our next call?": "aula3_oral3.mp3",
  "After every meeting, I send a follow-up email with a clear proposal and next steps.": "aula3_oral4.mp3",
  "We are committed to building long-term collaborations based on mutual benefit.": "aula3_oral5.mp3",
  "We negotiate transparent terms with every prospect. We could offer flexible commission rates.": "aula3_oral6.mp3",

  // Survival IN CLASS
  "Let me introduce myself. I am Eduardo Chiba.": "aula3_survival_ic_1.mp3",
  "Our value proposition is...": "aula3_survival_ic_2.mp3",
  "Could we schedule a call to discuss...?": "aula3_survival_ic_3.mp3",
  "We would be happy to negotiate the terms.": "aula3_survival_ic_4.mp3",
  "Would you mind reviewing our proposal?": "aula3_survival_ic_5.mp3",

  // Pre-class survival phrases
  "Could we schedule a call to discuss the terms?": "aula3_preclass_survival_1.mp3",
  "I would like to present our partnership proposal.": "aula3_preclass_survival_2.mp3",
  "We believe in mutual benefit and long-term collaboration.": "aula3_preclass_survival_3.mp3",
  "Would you mind if I send a follow-up email?": "aula3_preclass_survival_4.mp3",
  "We are committed to building strong partnerships.": "aula3_preclass_survival_5.mp3"
};

// === SPECIAL LONG-FORM TEXTS ===
const SPECIAL_TEXTS = {
  "[order-l3]": "Good morning. Thank you for meeting with me today. I would like to present our partnership proposal. Could we discuss the terms and commission structure? We believe this collaboration would bring mutual benefits. Would you mind if I send a follow-up email next week?",
  "aula3_listening1_call": "Good morning. I would like to discuss our partnership proposal. We believe this collaboration could bring mutual benefits for both companies. Could we schedule a call to go through the terms in detail? We could offer flexible commission rates based on your agency's volume. The commitment period would be twelve months initially, but we would be happy to negotiate if needed. Our goal is to build a long-term relationship based on mutual benefit. I look forward to your response and will send a follow-up email with all the details.",
  "aula3_listening2_negotiation": "Let me explain how we negotiate partnerships at Quinto Andar. When we identify a promising prospect, we send a formal proposal with clear terms. The key is finding mutual benefit. We would usually start with a standard commission rate, but we could adjust it based on volume. If a prospect wants a shorter commitment period, we would negotiate alternative terms. The most important thing is collaboration — we want our partners to feel that this is a true partnership, not just a business transaction. After every initial meeting, we always send a follow-up within twenty-four hours. That follow-up includes a summary of what was discussed and proposed next steps."
};

// === VOICE ASSIGNMENT ===

// Ana dialogue lines (female → always Ellen)
const anaLines = [
  "Good morning, Eduardo. Thank you for coming. Could you tell me more about your proposal?",
  "Interesting. What kind of commission structure would you offer?",
  "Not at all. And what about the commitment period? How long would the contract be?",
  "That sounds reasonable. Could you send me a formal proposal by Friday?"
];

// Eduardo dialogue lines (male → always Arthur)
const eduardoDialogueLines = [
  "Of course. I would like to present our partnership terms. We believe this could be a great collaboration.",
  "We could offer flexible rates based on your volume. Would you mind if I walk you through the numbers?",
  "We would propose a twelve-month commitment, but we could negotiate the terms if needed.",
  "Absolutely. I will send a follow-up email today with the full proposal. Thank you for considering this prospect."
];

// Listening monologues → Arthur (Eduardo is male)
const listeningKeys = ["aula3_listening1_call", "aula3_listening2_negotiation", "[order-l3]"];

function countWords(text) {
  return text.trim().split(/\s+/).length;
}

let phraseAlternator = 0;

function getVoice(text) {
  // Ana dialogue lines → Ellen
  if (anaLines.includes(text)) return { id: ELLEN, name: 'Ellen' };
  // Eduardo dialogue lines → Arthur
  if (eduardoDialogueLines.includes(text)) return { id: ARTHUR, name: 'Arthur' };
  // Listening monologues → Arthur (Eduardo is male)
  if (listeningKeys.includes(text)) return { id: ARTHUR, name: 'Arthur' };
  // Single words (1-2 words) → always Arthur
  var words = countWords(text);
  if (words <= 2) return { id: ARTHUR, name: 'Arthur' };
  // Other phrases (3+ words) → alternate Arthur/Ellen
  var voice = phraseAlternator % 2 === 0 ? { id: ARTHUR, name: 'Arthur' } : { id: ELLEN, name: 'Ellen' };
  phraseAlternator++;
  return voice;
}

function generateAudio(text, voiceId, outputPath) {
  return new Promise((resolve, reject) => {
    const postData = JSON.stringify({
      text,
      model_id: 'eleven_monolingual_v1',
      voice_settings: { stability: 0.5, similarity_boost: 0.75 }
    });
    const options = {
      hostname: 'api.elevenlabs.io',
      path: '/v1/text-to-speech/' + voiceId + '?output_format=mp3_44100_128',
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'xi-api-key': ELEVENLABS_API_KEY,
        'Content-Length': Buffer.byteLength(postData)
      }
    };
    const req = https.request(options, (res) => {
      if (res.statusCode === 429) {
        let body = '';
        res.on('data', (d) => body += d);
        res.on('end', () => reject(new Error('RATE_LIMITED')));
        return;
      }
      if (res.statusCode !== 200) {
        let body = '';
        res.on('data', (d) => body += d);
        res.on('end', () => reject(new Error('API ' + res.statusCode + ': ' + body)));
        return;
      }
      const chunks = [];
      res.on('data', (chunk) => chunks.push(chunk));
      res.on('end', () => {
        fs.writeFileSync(outputPath, Buffer.concat(chunks));
        resolve();
      });
    });
    req.on('error', reject);
    req.write(postData);
    req.end();
  });
}

function delay(ms) { return new Promise(resolve => setTimeout(resolve, ms)); }

async function main() {
  if (!fs.existsSync(OUTPUT_DIR)) fs.mkdirSync(OUTPUT_DIR, { recursive: true });

  const entries = Object.entries(audioMap);
  const total = entries.length;
  let generated = 0, skipped = 0, failed = 0;

  console.log('Eduardo Chiba — Aula 3 — Audio Generation');
  console.log('Total phrases: ' + total);
  console.log('Output: ' + OUTPUT_DIR + '\n');

  for (let i = 0; i < entries.length; i++) {
    const [key, filename] = entries[i];
    const outputPath = path.join(OUTPUT_DIR, filename);

    // Skip existing files (> 1KB to avoid corrupt files)
    if (fs.existsSync(outputPath)) {
      const stats = fs.statSync(outputPath);
      if (stats.size > 1000) {
        skipped++;
        // Keep alternator in sync for skipped 3+ word phrases
        const words = countWords(key);
        if (words > 2 && !anaLines.includes(key) && !eduardoDialogueLines.includes(key) && !listeningKeys.includes(key)) {
          phraseAlternator++;
        }
        continue;
      }
    }

    // Determine TTS text: use SPECIAL_TEXTS for monologues, otherwise the key itself
    const ttsText = SPECIAL_TEXTS[key] || key;
    const voice = getVoice(key);

    // Retry with 30s backoff on 429
    let success = false;
    for (let attempt = 0; attempt < 3; attempt++) {
      try {
        await generateAudio(ttsText, voice.id, outputPath);
        generated++;
        console.log('[' + (generated + skipped) + '/' + total + '] ' + filename + ' (' + voice.name + ')');
        success = true;
        break;
      } catch (err) {
        if (err.message === 'RATE_LIMITED') {
          console.log('  Rate limited, waiting 30s... (attempt ' + (attempt + 1) + '/3)');
          await delay(30000);
        } else {
          console.error('FAILED ' + filename + ': ' + err.message);
          break;
        }
      }
    }

    if (!success) {
      failed++;
    }

    // Rate limiting: 150ms between requests
    if (i < entries.length - 1) await delay(150);
  }

  console.log('\nDone!');
  console.log('Generated: ' + generated);
  console.log('Skipped: ' + skipped);
  console.log('Failed: ' + failed);
  console.log('Total: ' + total);
}

main().catch(console.error);
