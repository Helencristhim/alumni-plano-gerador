const fs = require('fs');
const path = require('path');
const https = require('https');

const ELEVENLABS_API_KEY = process.env.ELEVENLABS_API_KEY;
if (!ELEVENLABS_API_KEY) { console.error('ERROR: ELEVENLABS_API_KEY not set'); process.exit(1); }

const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const OUTPUT_DIR = path.join(__dirname, '..', 'public', 'audio', 'eduardo-chiba');

// All Aula 4 phrases from Eduardo Chiba's professor audioMap
const audioMap = {
  // Vocab words (1-2 word terms) → always Arthur
  "KPI": "aula4_kpi.mp3",
  "Growth": "aula4_growth.mp3",
  "Conversion": "aula4_conversion.mp3",
  "Churn": "aula4_churn.mp3",
  "Benchmark": "aula4_benchmark.mp3",
  "Quarter": "aula4_quarter.mp3",
  "Forecast": "aula4_forecast.mp3",
  "ROI": "aula4_roi.mp3",

  // Vocab example sentences
  "Our most important KPI is the number of new partner agencies per quarter.": "aula4_ex_kpi.mp3",
  "We have seen consistent growth in our B2B unit this year.": "aula4_ex_growth.mp3",
  "Our conversion rate from prospect to partner is thirty-five percent.": "aula4_ex_conversion.mp3",
  "We have reduced our churn rate to less than ten percent.": "aula4_ex_churn.mp3",
  "The industry benchmark for retention is around seventy percent.": "aula4_ex_benchmark.mp3",
  "We have onboarded fifty new agencies this quarter.": "aula4_ex_quarter.mp3",
  "Our revenue forecast for next year is very optimistic.": "aula4_ex_forecast.mp3",
  "The ROI for our partners has been excellent — most see results within three months.": "aula4_ex_roi.mp3",

  // Fill-in-the-blank sentences
  "We have grown our partner network by forty percent this year.": "aula4_fill1.mp3",
  "The conversion rate has improved significantly this quarter.": "aula4_fill2.mp3",
  "Our revenue forecast for next year is very optimistic.": "aula4_fill3.mp3",
  "We have reduced our churn rate to less than ten percent.": "aula4_fill4.mp3",
  "The industry benchmark for partner retention is seventy percent.": "aula4_fill5.mp3",
  "The ROI for our partners has been excellent.": "aula4_fill6.mp3",

  // Pronunciation sentences
  "We have grown our partner network by forty percent this year.": "aula4_pron1.mp3",
  "The conversion rate has improved significantly compared to last quarter.": "aula4_pron2.mp3",
  "Our ROI forecast for the next quarter is very optimistic.": "aula4_pron3.mp3",

  // Order exercise monologue
  "[order-l4]": "aula4_order_quarterly.mp3",

  // Dialogue — Lisa lines (female → Ellen)
  "Eduardo, thank you for the update. How has the B2B unit performed this quarter?": "aula4_dialogue_lisa_line1.mp3",
  "That is impressive growth. What about revenue? Have you hit the forecast?": "aula4_dialogue_lisa_line3.mp3",
  "And churn? That was a concern last year. Has it improved?": "aula4_dialogue_lisa_line5.mp3",
  "Great. What about conversion? How many prospects have become partners?": "aula4_dialogue_lisa_line7.mp3",

  // Dialogue — Eduardo lines (male → Arthur)
  "We have had an excellent quarter. Our partner network has grown by forty percent since January.": "aula4_dialogue_eduardo_line2.mp3",
  "Yes, revenue has increased by twenty-five percent compared to the same quarter last year. We have exceeded the benchmark.": "aula4_dialogue_eduardo_line4.mp3",
  "Absolutely. We have reduced churn to eight point five percent, well below the ten percent industry benchmark.": "aula4_dialogue_eduardo_line6.mp3",
  "Our conversion rate has improved to thirty-five percent. The ROI for our partners has been consistently positive.": "aula4_dialogue_eduardo_line8.mp3",

  // Listening monologues (long-form, generated as single MP3)
  "aula4_listening1_quarterly": "aula4_listening1_quarterly.mp3",
  "aula4_listening2_forecast": "aula4_listening2_forecast.mp3",

  // Quick fire answers
  "Revenue has increased by twenty-five percent compared to the same quarter last year.": "aula4_qf1.mp3",
  "We have grown our partner network by forty percent this year. Our conversion rate has improved to thirty-five percent.": "aula4_qf2.mp3",
  "Our churn rate has dropped to eight point five percent, well below the industry benchmark of ten percent.": "aula4_qf3.mp3",
  "Our forecast for next quarter is very optimistic. We expect to continue the growth trend and onboard fifty more agencies.": "aula4_qf4.mp3",
  "The ROI for our partners has been consistently positive. Most see measurable results within the first quarter.": "aula4_qf5.mp3",
  "We have grown by forty percent, reduced churn below benchmark, and increased revenue by twenty-five percent.": "aula4_qf6.mp3",

  // Oral models
  "Revenue has increased by twenty-five percent compared to the same quarter last year.": "aula4_oral1.mp3",
  "We have grown our partner network by forty percent since January.": "aula4_oral2.mp3",
  "We have reduced our churn rate to eight point five percent, well below the industry benchmark.": "aula4_oral3.mp3",
  "Our conversion rate has improved to thirty-five percent — up five percentage points from last quarter.": "aula4_oral4.mp3",
  "Our forecast for next year is very optimistic. We expect thirty percent revenue growth.": "aula4_oral5.mp3",
  "The ROI for our partners has been consistently positive for three consecutive quarters.": "aula4_oral6.mp3",

  // Survival IN CLASS
  "Let me introduce myself. I am Eduardo Chiba.": "aula4_survival_ic_1.mp3",
  "Our value proposition is...": "aula4_survival_ic_2.mp3",
  "Could we schedule a call to discuss...?": "aula4_survival_ic_3.mp3",
  "We have grown by... percent.": "aula4_survival_ic_4.mp3",
  "Our forecast for next quarter is...": "aula4_survival_ic_5.mp3",

  // Pre-class survival phrases
  "We have grown our partner network by forty percent.": "aula4_preclass_survival_1.mp3",
  "Revenue has increased by twenty-five percent compared to last year.": "aula4_preclass_survival_2.mp3",
  "Our churn rate is well below the industry benchmark.": "aula4_preclass_survival_3.mp3",
  "The forecast for next quarter is very promising.": "aula4_preclass_survival_4.mp3",
  "The ROI for our partners has been consistently positive.": "aula4_preclass_survival_5.mp3"
};

// === SPECIAL LONG-FORM TEXTS ===
const SPECIAL_TEXTS = {
  "[order-l4]": "Good morning. I would like to present our quarterly results. Our KPIs show strong growth across all metrics. We have increased revenue by twenty-five percent compared to last year. Our churn rate is well below the industry benchmark. The forecast for next quarter is very promising.",
  "aula4_listening1_quarterly": "Good morning, everyone. I would like to present our quarterly results for the B2B unit. We have had an outstanding quarter. Our partner network has grown by forty percent since January, which means we have added over two hundred new agencies to the platform. Revenue has increased by twenty-five percent compared to the same quarter last year, and we have exceeded our benchmark for the third consecutive time. On the retention side, we have reduced our churn rate to eight point five percent, well below the industry benchmark of ten percent. Our conversion rate has improved to thirty-five percent, up five percentage points from the previous quarter. The ROI for our partner agencies has been consistently positive. Looking ahead, our forecast for next quarter is very optimistic.",
  "aula4_listening2_forecast": "Let me share our forecast and strategic priorities for the coming year. Based on the KPIs we have achieved this quarter, we are projecting thirty percent revenue growth for next year. We have introduced a new KPI, the partner satisfaction score, which currently stands at eight point seven out of ten. Our conversion rate has been trending upward for three consecutive quarters, and we expect this momentum to continue. The ROI for our partners has been consistently positive, which is driving organic growth through referrals. We have set ambitious benchmarks: five hundred new partners, churn below eight percent, and revenue exceeding ten million reais. The data tells a clear story, our B2B unit has become a growth engine for Quinto Andar."
};

// === VOICE ASSIGNMENT ===

// Lisa dialogue lines (female → always Ellen)
const lisaLines = [
  "Eduardo, thank you for the update. How has the B2B unit performed this quarter?",
  "That is impressive growth. What about revenue? Have you hit the forecast?",
  "And churn? That was a concern last year. Has it improved?",
  "Great. What about conversion? How many prospects have become partners?"
];

// Eduardo dialogue lines (male → always Arthur)
const eduardoDialogueLines = [
  "We have had an excellent quarter. Our partner network has grown by forty percent since January.",
  "Yes, revenue has increased by twenty-five percent compared to the same quarter last year. We have exceeded the benchmark.",
  "Absolutely. We have reduced churn to eight point five percent, well below the ten percent industry benchmark.",
  "Our conversion rate has improved to thirty-five percent. The ROI for our partners has been consistently positive."
];

// Listening monologues → Arthur (Eduardo is male)
const listeningKeys = ["aula4_listening1_quarterly", "aula4_listening2_forecast", "[order-l4]"];

function countWords(text) {
  return text.trim().split(/\s+/).length;
}

let phraseAlternator = 0;

function getVoice(text) {
  // Lisa dialogue lines → Ellen
  if (lisaLines.includes(text)) return { id: ELLEN, name: 'Ellen' };
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

  console.log('Eduardo Chiba — Aula 4 — Audio Generation');
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
        if (words > 2 && !lisaLines.includes(key) && !eduardoDialogueLines.includes(key) && !listeningKeys.includes(key)) {
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
