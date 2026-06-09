/**
 * Generate ElevenLabs audio for Roberto Rezende - Aula 5 (Pipeline Talk)
 *
 * Voice rules:
 * - Roberto (male student): Arthur
 * - Amy Wong (female character): Ellen
 * - Single words: Arthur
 * - Vocab examples: alternate Arthur/Ellen
 * - Dialogue: Roberto=Arthur, Amy=Ellen
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
  { text: "Update", file: "aula5_update.mp3", voice: ARTHUR },
  { text: "Prospect", file: "aula5_prospect.mp3", voice: ARTHUR },
  { text: "Close a deal", file: "aula5_close_a_deal.mp3", voice: ARTHUR },
  { text: "Target", file: "aula5_target.mp3", voice: ARTHUR },
  { text: "Progress", file: "aula5_progress.mp3", voice: ARTHUR },
  { text: "Proposal", file: "aula5_proposal.mp3", voice: ARTHUR },
  { text: "Convert", file: "aula5_convert.mp3", voice: ARTHUR },
  { text: "Quarter", file: "aula5_quarter.mp3", voice: ARTHUR },
  { text: "Milestone", file: "aula5_milestone.mp3", voice: ARTHUR },
  { text: "Estimate", file: "aula5_estimate.mp3", voice: ARTHUR },

  // === VOCAB EXAMPLES (alternate Arthur/Ellen) ===
  { text: "I need to update the team on the pipeline status.", file: "aula5_i_need_to_update_the_team.mp3", voice: ARTHUR },
  { text: "We have five new prospects in the agricultural segment.", file: "aula5_we_have_five_new_prospects.mp3", voice: ELLEN },
  { text: "Roberto is closing a deal with a major mining company.", file: "aula5_roberto_is_closing_a_deal.mp3", voice: ARTHUR },
  { text: "Our target for this quarter is twenty new contracts.", file: "aula5_our_target_for_this_quarter.mp3", voice: ELLEN },
  { text: "We are making good progress on the generator project.", file: "aula5_we_are_making_good_progress.mp3", voice: ARTHUR },
  { text: "The proposal for the logistics company is almost ready.", file: "aula5_the_proposal_for_the_logistics.mp3", voice: ELLEN },
  { text: "We need to convert more prospects into paying clients.", file: "aula5_we_need_to_convert_more.mp3", voice: ARTHUR },
  { text: "This quarter has been our best quarter so far.", file: "aula5_this_quarter_has_been_our_best.mp3", voice: ELLEN },
  { text: "Reaching fifteen clients was a major milestone for the team.", file: "aula5_reaching_fifteen_clients.mp3", voice: ARTHUR },
  { text: "Can you estimate how long the negotiation will take?", file: "aula5_can_you_estimate_how_long.mp3", voice: ELLEN },

  // === DIALOGUE (Roberto=Arthur, Amy=Ellen) ===
  { text: "Good morning, Amy. I am calling to update you on the Brazil pipeline.", file: "aula5_good_morning_amy.mp3", voice: ARTHUR },
  { text: "Good morning, Roberto. How is the quarter progressing?", file: "aula5_good_morning_roberto.mp3", voice: ELLEN },
  { text: "We are currently working on eight active proposals. Three are in the final stage.", file: "aula5_we_are_currently_working.mp3", voice: ARTHUR },
  { text: "That sounds like good progress. Are you targeting any new prospects?", file: "aula5_that_sounds_like_good.mp3", voice: ELLEN },
  { text: "Yes, we are targeting five new companies in the agricultural segment. Two are already converting.", file: "aula5_yes_we_are_targeting.mp3", voice: ARTHUR },
  { text: "Excellent. What about the mining company proposal? Are you closing that this month?", file: "aula5_excellent_what_about.mp3", voice: ELLEN },
  { text: "We are estimating a close by the end of June. The proposal is with their legal team now.", file: "aula5_we_are_estimating_a_close.mp3", voice: ARTHUR },
  { text: "Good. Could you send me the milestone report by Friday? Mr. Zhang is reviewing all regional pipelines.", file: "aula5_good_could_you_send.mp3", voice: ELLEN },

  // === LISTENING 1 (Arthur — Roberto's pipeline update monologue) ===
  { text: "Good morning, everyone. This is Roberto from the Brazil office. I am calling to update you on our pipeline for Q2. We are currently working on eight active proposals. Three of those are in the final stage, and we are estimating closings by the end of this month. Our target for the quarter is twenty new contracts, and so far we have converted twelve prospects. We are also targeting five new companies in the agricultural segment. The mining company proposal is progressing well. The milestone we reached last week was fifteen active clients, which is a new record for the Brazil office. I will send the full pipeline report by Friday.", file: "aula5_listening1_pipeline_update.mp3", voice: ARTHUR },

  // === LISTENING 2 (Ellen — Amy's questions) ===
  { text: "Thank you for the update, Roberto. I have a few questions. First, you mentioned eight active proposals. Are all of those in the diesel engine segment, or are some in generators? Second, the five new agricultural prospects you are targeting, are they large companies or small farms? Third, you said you are estimating three closings this month. What happens if the mining company deal takes longer? And finally, Mr. Zhang wants to know about the conversion rate. You converted twelve out of how many total prospects this quarter? Could you include those numbers in the report you are sending on Friday?", file: "aula5_listening2_amy_questions.mp3", voice: ELLEN },

  // === QUICKFIRE (Arthur — student practice) ===
  { text: "We are currently working on eight active proposals. Three are in the final stage.", file: "aula5_quickfire1.mp3", voice: ARTHUR },
  { text: "We are estimating a close by the end of this month. The proposal is almost ready.", file: "aula5_quickfire2.mp3", voice: ARTHUR },
  { text: "We are targeting five new companies in the agricultural segment this quarter.", file: "aula5_quickfire3.mp3", voice: ARTHUR },
  { text: "We are making good progress. We have converted twelve prospects so far.", file: "aula5_quickfire4.mp3", voice: ARTHUR },
  { text: "The mining company proposal is progressing well. We are closing by end of June.", file: "aula5_quickfire5.mp3", voice: ARTHUR },
  { text: "I am updating the report now. I will send it by Friday.", file: "aula5_quickfire6.mp3", voice: ARTHUR },

  // === SURVIVAL (Arthur — student key phrases) ===
  { text: "We are currently working on eight active proposals.", file: "aula5_survival1.mp3", voice: ARTHUR },
  { text: "Our target for this quarter is twenty new contracts.", file: "aula5_survival2.mp3", voice: ARTHUR },
  { text: "We are estimating a close by the end of this month.", file: "aula5_survival3.mp3", voice: ARTHUR },
  { text: "Could you send me the milestone report by Friday?", file: "aula5_survival4.mp3", voice: ARTHUR },
  { text: "We are making good progress on the pipeline.", file: "aula5_survival5.mp3", voice: ARTHUR },

  // === FILL SENTENCES (alternate Arthur/Ellen) ===
  { text: "We are currently working on eight active proposals. Three are in the final stage.", file: "aula5_fill_we_are_currently_working.mp3", voice: ARTHUR },
  { text: "We are targeting five new companies in the agricultural segment.", file: "aula5_fill_we_are_targeting.mp3", voice: ELLEN },
  { text: "Roberto is closing a deal with the mining company this month.", file: "aula5_fill_roberto_is_closing.mp3", voice: ARTHUR },
  { text: "The team is making good progress on the Q2 pipeline.", file: "aula5_fill_the_team_is_making.mp3", voice: ELLEN },
  { text: "We are estimating a close by the end of June.", file: "aula5_fill_we_are_estimating.mp3", voice: ARTHUR },

  // === ORDERING (Arthur — full pipeline update) ===
  { text: "Good morning. I am calling to update you on the Brazil pipeline. We are currently working on eight active proposals. We are targeting five new prospects in agriculture. We are estimating three closings by end of month. I will send the full pipeline report by Friday.", file: "order_l5_ordering.mp3", voice: ARTHUR },
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
