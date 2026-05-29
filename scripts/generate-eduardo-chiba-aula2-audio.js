const fs = require('fs');
const path = require('path');
const https = require('https');

const ELEVENLABS_API_KEY = process.env.ELEVENLABS_API_KEY;
if (!ELEVENLABS_API_KEY) { console.error('ERROR: ELEVENLABS_API_KEY not set'); process.exit(1); }

const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const OUTPUT_DIR = path.join(__dirname, '..', 'public', 'audio', 'eduardo-chiba');

// All Aula 2 phrases from Eduardo Chiba's professor audioMap
const audioMap = {
  // Vocab words (single words / 2-word terms)
  "Value Proposition": "aula2_value_proposition.mp3",
  "Target Market": "aula2_target_market.mp3",
  "Competitive Advantage": "aula2_competitive_advantage.mp3",
  "Commission": "aula2_commission.mp3",
  "Integration": "aula2_integration.mp3",
  "Marketplace": "aula2_marketplace.mp3",
  "Disruption": "aula2_disruption.mp3",
  "Retention": "aula2_retention.mp3",

  // Vocab example sentences
  "Our value proposition is simple: we connect agencies to millions of renters.": "aula2_ex_value_proposition.mp3",
  "Our target market includes real estate agencies and independent brokers.": "aula2_ex_target_market.mp3",
  "Our competitive advantage is our technology platform.": "aula2_ex_competitive_advantage.mp3",
  "We earn a commission on every successful rental transaction.": "aula2_ex_commission.mp3",
  "The integration between our platform and the agency's system is seamless.": "aula2_ex_integration.mp3",
  "Quinto Andar is the largest digital marketplace for rentals in Brazil.": "aula2_ex_marketplace.mp3",
  "Digital platforms have caused major disruption in the real estate industry.": "aula2_ex_disruption.mp3",
  "Our partner retention rate is over ninety percent.": "aula2_ex_retention.mp3",

  // Fill-in-the-blank sentences
  "Our value proposition is simple: we connect agencies to renners.": "aula2_fill_proposition.mp3",
  "The target market for our B2B unit includes agencies and brokers.": "aula2_fill_market.mp3",
  "Our platform is faster than traditional listing services.": "aula2_fill_faster.mp3",
  "We earn a commission on every successful rental transaction.": "aula2_fill_commission.mp3",
  "Our partner retention rate is over ninety percent.": "aula2_fill_retention.mp3",

  // Pronunciation sentences
  "Our value proposition is connecting real estate agencies to millions of renters.": "aula2_pron1.mp3",
  "Quinto Andar is more efficient than traditional listing services.": "aula2_pron2.mp3",
  "Our competitive advantage comes from seamless technology integration.": "aula2_pron3.mp3",

  // Order exercise monologue
  "[order-l2]": "aula2_order_pitch.mp3",

  // Dialogue — Rachel lines (female → Ellen)
  "Eduardo, thank you for meeting me. Could you start by describing Quinto Andar's value proposition?": "aula2_dialogue_rachel_line1.mp3",
  "Interesting. What makes your platform different? What is your competitive advantage?": "aula2_dialogue_rachel_line3.mp3",
  "That is impressive. And how does your commission structure work?": "aula2_dialogue_rachel_line5.mp3",
  "What about partner retention? How do you keep agencies on your platform?": "aula2_dialogue_rachel_line7.mp3",

  // Dialogue — Eduardo lines (male → Arthur)
  "Of course. Our value proposition is simple: we connect real estate agencies to millions of renters through a digital marketplace.": "aula2_dialogue_eduardo_line2.mp3",
  "Our integration is faster than traditional services. Agencies can list properties in twenty-four hours, compared to two to four weeks with traditional methods.": "aula2_dialogue_eduardo_line4.mp3",
  "We earn a transparent commission on every successful transaction. It is more competitive than traditional agency fees.": "aula2_dialogue_eduardo_line6.mp3",
  "Our retention rate is over ninety percent. That is higher than the industry average. The target market values our seamless integration.": "aula2_dialogue_eduardo_line8.mp3",

  // Listening monologues (long-form, generated as single MP3)
  "aula2_listening1_pitch": "aula2_listening1_pitch.mp3",
  "aula2_listening2_market": "aula2_listening2_market.mp3",

  // Quick fire answers
  "Our value proposition is connecting real estate agencies to millions of renters through a digital marketplace.": "aula2_qf1.mp3",
  "Our target market includes real estate agencies, independent brokers, and property owners.": "aula2_qf2.mp3",
  "Our platform is faster and more efficient than traditional listing services.": "aula2_qf3.mp3",
  "We earn a transparent, percentage-based commission on every successful rental transaction.": "aula2_qf4.mp3",
  "Our competitive advantage is our seamless technology integration and nationwide marketplace.": "aula2_qf5.mp3",
  "Our retention rate is over ninety percent, which is higher than the industry average.": "aula2_qf6.mp3",

  // Oral models
  "Our value proposition is connecting agencies to millions of renters through our digital marketplace.": "aula2_oral1.mp3",
  "Our platform is faster and more efficient than traditional agencies. We list properties in 24 hours.": "aula2_oral2.mp3",
  "We earn a transparent commission on every successful transaction. It is more competitive than traditional fees.": "aula2_oral3.mp3",
  "Our competitive advantage is our seamless technology integration and nationwide reach.": "aula2_oral4.mp3",
  "Our target market includes real estate agencies, brokers, and property owners across Brazil.": "aula2_oral5.mp3",
  "Our retention rate is over ninety percent — higher than the industry average.": "aula2_oral6.mp3",

  // Survival IN CLASS
  "Let me introduce myself. I am Eduardo Chiba.": "aula2_survival_ic_1.mp3",
  "Our value proposition is...": "aula2_survival_ic_2.mp3",
  "We are more efficient than...": "aula2_survival_ic_3.mp3",
  "Our competitive advantage is...": "aula2_survival_ic_4.mp3",
  "Our retention rate is over ninety percent.": "aula2_survival_ic_5.mp3",

  // Pre-class survival phrases
  "Our value proposition is connecting agencies to renters.": "aula2_preclass_survival_1.mp3",
  "We are more efficient than traditional services.": "aula2_preclass_survival_2.mp3",
  "Our target market includes agencies and brokers.": "aula2_preclass_survival_3.mp3",
  "The commission structure is transparent.": "aula2_preclass_survival_4.mp3",
  "Our retention rate is higher than the industry average.": "aula2_preclass_survival_5.mp3"
};

// === SPECIAL LONG-FORM TEXTS ===
// These keys in audioMap are NOT the actual text to speak — they map to long monologues

const SPECIAL_TEXTS = {
  "[order-l2]": "Good morning. I am Eduardo Chiba from Quinto Andar. Our value proposition is connecting agencies to millions of renters. We are more efficient than traditional listing services. Our commission model is transparent and competitive. Our partner retention rate is over ninety percent.",
  "aula2_listening1_pitch": "Good morning. Let me tell you about Quinto Andar's business model. Our value proposition is simple: we connect real estate agencies to millions of potential renters through a seamless digital marketplace. Our target market includes agencies, brokers, and property owners who want more digital visibility. What makes us different? Our competitive advantage is our technology. The integration between our platform and agency systems is faster than traditional methods. We earn a transparent commission on every successful transaction. And our partner retention rate? Over ninety percent. That is higher than the industry average. Digital disruption has transformed real estate, and Quinto Andar is leading that transformation in Brazil.",
  "aula2_listening2_market": "Let me explain the market dynamics. Digital platforms have caused significant disruption in the real estate industry worldwide. In Brazil, the traditional model relied on local agencies with limited reach. Quinto Andar changed that by creating a nationwide digital marketplace. Our integration technology is more efficient than manual processes. Agencies can list properties in twenty-four hours, compared to two to four weeks with traditional services. The commission structure is more transparent, and the competitive advantage is clear: faster listings, wider reach, and better retention. Our target market continues to grow as more agencies recognize that digital transformation is not optional — it is essential."
};

// === VOICE ASSIGNMENT ===

// Rachel dialogue lines (female → always Ellen)
const rachelLines = [
  "Eduardo, thank you for meeting me. Could you start by describing Quinto Andar's value proposition?",
  "Interesting. What makes your platform different? What is your competitive advantage?",
  "That is impressive. And how does your commission structure work?",
  "What about partner retention? How do you keep agencies on your platform?"
];

// Eduardo dialogue lines (male → always Arthur)
const eduardoDialogueLines = [
  "Of course. Our value proposition is simple: we connect real estate agencies to millions of renters through a digital marketplace.",
  "Our integration is faster than traditional services. Agencies can list properties in twenty-four hours, compared to two to four weeks with traditional methods.",
  "We earn a transparent commission on every successful transaction. It is more competitive than traditional agency fees.",
  "Our retention rate is over ninety percent. That is higher than the industry average. The target market values our seamless integration."
];

// Listening monologues → Arthur (Eduardo is male)
const listeningKeys = ["aula2_listening1_pitch", "aula2_listening2_market", "[order-l2]"];

function countWords(text) {
  return text.trim().split(/\s+/).length;
}

let phraseAlternator = 0;

function getVoice(text) {
  // Rachel dialogue lines → Ellen
  if (rachelLines.includes(text)) return { id: ELLEN, name: 'Ellen' };
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

  console.log('Eduardo Chiba — Aula 2 — Audio Generation');
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
        if (words > 2 && !rachelLines.includes(key) && !eduardoDialogueLines.includes(key) && !listeningKeys.includes(key)) {
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
