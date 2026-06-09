/**
 * Generate ElevenLabs audio for Roberto Rezende - Aula 7 (Numbers and Forecasts)
 * Voice: Roberto (male student) = Arthur, Amy Wong (female) = Ellen
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
  // VOCAB WORDS (Arthur)
  { text: "Increase", file: "aula7_increase.mp3", voice: ARTHUR },
  { text: "Decrease", file: "aula7_decrease.mp3", voice: ARTHUR },
  { text: "Percentage", file: "aula7_percentage.mp3", voice: ARTHUR },
  { text: "Growth", file: "aula7_growth.mp3", voice: ARTHUR },
  { text: "Trend", file: "aula7_trend.mp3", voice: ARTHUR },
  { text: "Compare", file: "aula7_compare.mp3", voice: ARTHUR },
  { text: "Chart", file: "aula7_chart.mp3", voice: ARTHUR },
  { text: "Significant", file: "aula7_significant.mp3", voice: ARTHUR },
  { text: "Outperform", file: "aula7_outperform.mp3", voice: ARTHUR },
  { text: "Projection", file: "aula7_projection.mp3", voice: ARTHUR },

  // VOCAB EXAMPLES (alternate)
  { text: "Sales increased by fifteen percentage this quarter.", file: "aula7_sales_increased_by_fifteen.mp3", voice: ARTHUR },
  { text: "We saw a decrease in generator orders last month.", file: "aula7_we_saw_a_decrease.mp3", voice: ELLEN },
  { text: "The agricultural segment represents forty percentage of our revenue.", file: "aula7_the_agricultural_segment.mp3", voice: ARTHUR },
  { text: "Growth in the mining sector was stronger than expected.", file: "aula7_growth_in_the_mining.mp3", voice: ELLEN },
  { text: "The trend shows a steady increase in diesel engine sales.", file: "aula7_the_trend_shows.mp3", voice: ARTHUR },
  { text: "Let me compare Q1 and Q2 results side by side.", file: "aula7_let_me_compare.mp3", voice: ELLEN },
  { text: "This chart shows our performance across all segments.", file: "aula7_this_chart_shows.mp3", voice: ARTHUR },
  { text: "The growth in agriculture was more significant than in mining.", file: "aula7_the_growth_in_agriculture.mp3", voice: ELLEN },
  { text: "The Brazil office outperformed all other regional offices.", file: "aula7_the_brazil_office.mp3", voice: ARTHUR },
  { text: "Our projection for Q3 is higher than Q2.", file: "aula7_our_projection_for_q3.mp3", voice: ELLEN },

  // DIALOGUE (Roberto=Arthur, Amy=Ellen)
  { text: "Good morning, Amy. I am presenting the Q2 results for Brazil.", file: "aula7_dialogue_roberto1.mp3", voice: ARTHUR },
  { text: "Good morning, Roberto. I have the charts ready. How did Brazil perform?", file: "aula7_dialogue_amy1.mp3", voice: ELLEN },
  { text: "Overall, Q2 was stronger than Q1. Sales increased by fifteen percent.", file: "aula7_dialogue_roberto2.mp3", voice: ARTHUR },
  { text: "That is a significant increase. Which segment had the best growth?", file: "aula7_dialogue_amy2.mp3", voice: ELLEN },
  { text: "Agriculture was the strongest segment. It outperformed mining by twenty percent.", file: "aula7_dialogue_roberto3.mp3", voice: ARTHUR },
  { text: "Interesting. What about generators? I noticed a decrease on the chart.", file: "aula7_dialogue_amy3.mp3", voice: ELLEN },
  { text: "Yes, generators decreased by eight percent. But our projection for Q3 is more optimistic than Q2.", file: "aula7_dialogue_roberto4.mp3", voice: ARTHUR },
  { text: "Good. So the trend is positive overall. Can you compare the Brazil numbers with the other offices?", file: "aula7_dialogue_amy4.mp3", voice: ELLEN },

  // LISTENING 1 (Arthur — Q2 presentation monologue)
  { text: "Good morning, everyone. I am presenting the Q2 results for Brazil. Overall, this quarter was stronger than Q1. Total sales increased by fifteen percent. The agricultural segment was our best performer, with growth of thirty-two percent compared to last quarter. It outperformed all other segments. Mining also showed a significant increase of eighteen percent. However, the generator segment saw a decrease of eight percent, which was lower than our target. When we compare Brazil with other regional offices, our numbers were higher than average. The trend is positive, and our projection for Q3 is more optimistic. We are forecasting the highest growth in agriculture.", file: "aula7_listening1_q2_presentation.mp3", voice: ARTHUR },

  // LISTENING 2 (Ellen — Amy's data questions)
  { text: "Thank you, Roberto. I have some questions about the data. First, you said agriculture outperformed mining. By what percentage exactly? Second, the generator decrease. Was it worse than last year or better? Third, when you compare Brazil with other offices, which office had the highest overall growth? And finally, your Q3 projection. Is it more conservative or more aggressive than Q2? Mr. Zhang wants the most accurate numbers for the board meeting.", file: "aula7_listening2_amy_data_questions.mp3", voice: ELLEN },

  // QUICKFIRE (Arthur)
  { text: "Q2 was stronger than Q1. Sales increased by fifteen percent.", file: "aula7_quickfire1.mp3", voice: ARTHUR },
  { text: "Agriculture was the best segment. It outperformed mining by twenty percent.", file: "aula7_quickfire2.mp3", voice: ARTHUR },
  { text: "Generators decreased by eight percent, which was lower than our target.", file: "aula7_quickfire3.mp3", voice: ARTHUR },
  { text: "Our Q3 projection is more optimistic than Q2.", file: "aula7_quickfire4.mp3", voice: ARTHUR },
  { text: "Brazil had the highest growth compared to other offices.", file: "aula7_quickfire5.mp3", voice: ARTHUR },
  { text: "The trend shows agriculture is growing faster than mining.", file: "aula7_quickfire6.mp3", voice: ARTHUR },

  // SURVIVAL (Arthur)
  { text: "Q2 was stronger than Q1 across all segments.", file: "aula7_survival1.mp3", voice: ARTHUR },
  { text: "Agriculture had the highest growth this quarter.", file: "aula7_survival2.mp3", voice: ARTHUR },
  { text: "Our projection for Q3 is more optimistic.", file: "aula7_survival3.mp3", voice: ARTHUR },
  { text: "As you can see on the chart, sales increased significantly.", file: "aula7_survival4.mp3", voice: ARTHUR },
  { text: "Brazil outperformed all other regional offices.", file: "aula7_survival5.mp3", voice: ARTHUR },

  // FILL SENTENCES (alternate)
  { text: "Q2 was stronger than Q1. Sales increased by fifteen percent.", file: "aula7_fill_q2_was_stronger.mp3", voice: ARTHUR },
  { text: "Agriculture was the best segment this quarter.", file: "aula7_fill_agriculture_was_best.mp3", voice: ELLEN },
  { text: "The growth was more significant than expected.", file: "aula7_fill_growth_more_significant.mp3", voice: ARTHUR },
  { text: "Brazil had the highest revenue of all offices.", file: "aula7_fill_brazil_highest.mp3", voice: ELLEN },
  { text: "Generators performed worse than mining.", file: "aula7_fill_generators_worse.mp3", voice: ARTHUR },

  // ORDERING (Arthur)
  { text: "Good morning. I am presenting the Q2 results. Q2 was stronger than Q1. Agriculture had the highest growth. Generators decreased by eight percent. Our Q3 projection is more optimistic than Q2.", file: "order_l7_ordering.mp3", voice: ARTHUR },
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
