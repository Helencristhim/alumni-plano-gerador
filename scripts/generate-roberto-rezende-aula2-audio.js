/**
 * Generate ElevenLabs audio for Roberto Rezende - Aula 2
 *
 * Voice rules:
 * - Single words (1-2 words): ALWAYS Arthur
 * - Sentences (3+ words): ALTERNATE Arthur/Ellen
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

// Combined audioMap from roberto-rezende-aula2.html AND roberto-rezende.html
// Using ALL unique filename entries
const audioEntries = [
  // === Single words (1-2 words) — ALWAYS Arthur ===
  { text: "Transition", file: "aula2_transition.mp3", voice: ARTHUR },
  { text: "Lead", file: "aula2_lead.mp3", voice: ARTHUR },
  { text: "Client base", file: "aula2_client_base.mp3", voice: ARTHUR },
  { text: "Revenue", file: "aula2_revenue.mp3", voice: ARTHUR },
  { text: "Negotiate", file: "aula2_negotiate.mp3", voice: ARTHUR },
  { text: "Attend", file: "aula2_attend.mp3", voice: ARTHUR },
  { text: "Manage", file: "aula2_manage.mp3", voice: ARTHUR },
  { text: "Achieve", file: "aula2_achieve.mp3", voice: ARTHUR },
  { text: "Expand", file: "aula2_expand.mp3", voice: ARTHUR },
  { text: "Challenging", file: "aula2_challenging.mp3", voice: ARTHUR },

  // === Sentences from aula2 HTML (IN CLASS file) — alternate Arthur/Ellen ===
  { text: "My transition from engineering to sales was a big step.", file: "aula2_transition_big_step.mp3", voice: ARTHUR },
  { text: "I lead the sales team for the Brazilian market.", file: "aula2_lead_sales_team.mp3", voice: ELLEN },
  { text: "We are building a strong client base in South America.", file: "aula2_building_client_base.mp3", voice: ARTHUR },
  { text: "Our revenue increased by fifteen percent last quarter.", file: "aula2_revenue_increased.mp3", voice: ELLEN },
  { text: "I negotiate contracts with new clients every month.", file: "aula2_negotiate_contracts.mp3", voice: ARTHUR },
  { text: "I attend trade fairs across Brazil and internationally.", file: "aula2_attend_trade_fairs.mp3", voice: ELLEN },
  { text: "I manage relationships with over fifty industrial clients.", file: "aula2_manage_relationships.mp3", voice: ARTHUR },
  { text: "We achieved our sales target three months early.", file: "aula2_achieved_target.mp3", voice: ELLEN },
  { text: "We are expanding into the agricultural segment in the South.", file: "aula2_expanding_agricultural.mp3", voice: ARTHUR },
  { text: "Working with a Chinese company is challenging but rewarding.", file: "aula2_challenging_rewarding.mp3", voice: ELLEN },

  // === Expression starters (aula2 HTML only) ===
  { text: "I studied engineering and then transitioned to...", file: "aula2_expr_studied_transitioned.mp3", voice: ARTHUR },
  { text: "I lead the sales team and manage over...", file: "aula2_expr_lead_manage.mp3", voice: ELLEN },
  { text: "The most challenging part of my job is...", file: "aula2_expr_challenging_part.mp3", voice: ARTHUR },
  { text: "We achieved our target and now we are expanding into...", file: "aula2_expr_achieved_expanding.mp3", voice: ELLEN },
  { text: "I negotiate contracts with clients across...", file: "aula2_expr_negotiate_across.mp3", voice: ARTHUR },

  // === Survival card (aula2 HTML only) ===
  { text: "I studied engineering and then transitioned to sales.", file: "aula2_surv_studied_transitioned.mp3", voice: ELLEN },
  { text: "I lead the sales team and manage over fifty clients.", file: "aula2_surv_lead_manage.mp3", voice: ARTHUR },
  { text: "We achieved our revenue target three months early.", file: "aula2_surv_achieved_revenue.mp3", voice: ELLEN },
  { text: "The most challenging part is negotiating in English.", file: "aula2_surv_challenging_negotiating.mp3", voice: ARTHUR },
  { text: "We are expanding into the agricultural segment.", file: "aula2_surv_expanding_segment.mp3", voice: ELLEN },

  // === Sentences from professor file (Pre-class) with DIFFERENT filenames ===
  { text: "My transition from engineering to sales was a big step.", file: "aula2_my_transition_from_engineering_to_sales.mp3", voice: ARTHUR },
  { text: "I lead the sales team for the Brazilian market.", file: "aula2_i_lead_the_sales_team.mp3", voice: ELLEN },
  { text: "We are building a strong client base in South America.", file: "aula2_we_are_building_a_strong_client_base.mp3", voice: ARTHUR },
  { text: "Our revenue increased by fifteen percent last quarter.", file: "aula2_our_revenue_increased.mp3", voice: ELLEN },
  { text: "I negotiate contracts with new clients every month.", file: "aula2_i_negotiate_contracts.mp3", voice: ARTHUR },
  { text: "I attend trade fairs across Brazil and internationally.", file: "aula2_i_attend_trade_fairs.mp3", voice: ELLEN },
  { text: "I manage relationships with over fifty industrial clients.", file: "aula2_i_manage_relationships.mp3", voice: ARTHUR },
  { text: "We achieved our sales target three months early.", file: "aula2_we_achieved_our_sales_target.mp3", voice: ELLEN },
  { text: "We are expanding into the agricultural segment in the South.", file: "aula2_we_are_expanding.mp3", voice: ARTHUR },
  { text: "Working with a Chinese company is challenging but rewarding.", file: "aula2_working_with_a_chinese_company.mp3", voice: ELLEN },

  // === Context/Grammar sentences from professor file ===
  { text: "Roberto studied mechanical engineering in Brazil.", file: "aula2_roberto_studied_mechanical.mp3", voice: ARTHUR },
  { text: "He leads the sales team for the Brazilian market.", file: "aula2_he_leads_the_sales_team.mp3", voice: ELLEN },
  { text: "Last year, the team expanded into agriculture.", file: "aula2_last_year_the_team_expanded.mp3", voice: ARTHUR },
  { text: "Roberto negotiates contracts with new clients every month.", file: "aula2_roberto_negotiates_contracts.mp3", voice: ELLEN },
  { text: "In 2019, he transitioned from engineering to sales.", file: "aula2_in_2019_he_transitioned.mp3", voice: ARTHUR },

  // === Pre-class sentences from professor file ===
  { text: "I studied engineering and then transitioned to sales.", file: "aula2_i_studied_engineering_and_then.mp3", voice: ELLEN },
  { text: "I lead the sales team and manage over fifty clients.", file: "aula2_i_lead_and_manage.mp3", voice: ARTHUR },
  { text: "We achieved our revenue target three months early.", file: "aula2_we_achieved_revenue_target.mp3", voice: ELLEN },
  { text: "Negotiating in English is challenging but rewarding.", file: "aula2_negotiating_in_english.mp3", voice: ARTHUR },
  { text: "We are expanding into the agricultural segment.", file: "aula2_we_are_expanding_agri.mp3", voice: ELLEN },

  // === Ordering / career story sentences ===
  { text: "I studied mechanical engineering and completed my PhD.", file: "aula2_i_studied_mechanical.mp3", voice: ARTHUR },
  { text: "I worked in research and development for five years.", file: "aula2_i_worked_in_research.mp3", voice: ELLEN },
  { text: "I transitioned from engineering to sales in 2019.", file: "aula2_i_transitioned_in_2019.mp3", voice: ARTHUR },
  { text: "I built a strong client base of over fifty clients.", file: "aula2_i_built_a_strong_client_base.mp3", voice: ELLEN },
  { text: "The company needed someone to lead sales in Brazil.", file: "aula2_the_company_needed_someone.mp3", voice: ARTHUR },
  { text: "Last year, we expanded into the agricultural segment.", file: "aula2_last_year_we_expanded.mp3", voice: ELLEN },

  // === Order audio ===
  { text: "I studied mechanical engineering and completed my PhD. I worked in research and development for five years. I transitioned from engineering to sales in 2019. I built a strong client base of over fifty clients. The company needed someone to lead sales in Brazil. Last year, we expanded into the agricultural segment.", file: "aula2_order_career_story.mp3", voice: ARTHUR },
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
      voice_settings: {
        stability: 0.5,
        similarity_boost: 0.75,
        style: 0.0,
        use_speaker_boost: true
      }
    });

    const options = {
      hostname: 'api.elevenlabs.io',
      port: 443,
      path: `/v1/text-to-speech/${voiceId}`,
      method: 'POST',
      headers: {
        'Accept': 'audio/mpeg',
        'Content-Type': 'application/json',
        'xi-api-key': ELEVENLABS_API_KEY
      }
    };

    const req = https.request(options, (res) => {
      if (res.statusCode !== 200) {
        let body = '';
        res.on('data', chunk => body += chunk);
        res.on('end', () => reject(new Error(`HTTP ${res.statusCode}: ${body}`)));
        return;
      }
      const chunks = [];
      res.on('data', chunk => chunks.push(chunk));
      res.on('end', () => resolve(Buffer.concat(chunks)));
    });

    req.on('error', reject);
    req.write(payload);
    req.end();
  });
}

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function main() {
  // Ensure output dir exists
  if (!fs.existsSync(OUTPUT_DIR)) {
    fs.mkdirSync(OUTPUT_DIR, { recursive: true });
  }

  // Filter to only missing files
  const missing = uniqueEntries.filter(e => {
    const filepath = path.join(OUTPUT_DIR, e.file);
    return !fs.existsSync(filepath);
  });

  console.log(`Total unique entries: ${uniqueEntries.length}`);
  console.log(`Already exist: ${uniqueEntries.length - missing.length}`);
  console.log(`Missing (to generate): ${missing.length}`);

  if (missing.length === 0) {
    console.log('All audio files already exist!');
    return;
  }

  let generated = 0;
  let errors = 0;

  for (const entry of missing) {
    const filepath = path.join(OUTPUT_DIR, entry.file);
    const voiceName = entry.voice === ARTHUR ? 'Arthur' : 'Ellen';

    console.log(`[${generated + errors + 1}/${missing.length}] Generating: ${entry.file} (${voiceName}) — "${entry.text.substring(0, 50)}..."`);

    try {
      const audioBuffer = await generateAudio(entry.text, entry.voice);
      fs.writeFileSync(filepath, audioBuffer);
      generated++;
      console.log(`  OK (${(audioBuffer.length / 1024).toFixed(1)} KB)`);

      // Rate limit: ~2 requests per second
      await sleep(600);
    } catch (err) {
      errors++;
      console.error(`  FAILED: ${err.message}`);
      // Wait longer on error (might be rate limited)
      await sleep(2000);
    }
  }

  console.log(`\nDone! Generated: ${generated}, Errors: ${errors}`);
}

main().catch(console.error);
