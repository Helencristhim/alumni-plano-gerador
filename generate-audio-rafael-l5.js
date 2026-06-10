#!/usr/bin/env node
/**
 * Audio generation script for Rafael Pelizaro — Lesson 5
 * The Sprint Review — Technical Updates for Non-Tech People
 *
 * Uses ElevenLabs API to generate MP3 files
 * Arthur (male) = sfJopaWaOtauCD3HKX6Q
 * Ellen (female) = BIvP0GN1cAtSRTxNHnWS
 */

const fs = require('fs');
const path = require('path');
const https = require('https');

const API_KEY = process.env.ELEVENLABS_API_KEY;
if (!API_KEY) { console.error('Set ELEVENLABS_API_KEY env var'); process.exit(1); }

const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const OUTPUT_DIR = path.join(__dirname, 'public', 'audio', 'rafael-pelizaro');

// Ensure output directory exists
if (!fs.existsSync(OUTPUT_DIR)) fs.mkdirSync(OUTPUT_DIR, { recursive: true });

const entries = [
  // Vocab words (Arthur - student male, 1-2 words)
  { text: "Sprint", file: "l5_sprint.mp3", voice: ARTHUR },
  { text: "Bug", file: "l5_bug.mp3", voice: ARTHUR },
  { text: "Feature", file: "l5_feature.mp3", voice: ARTHUR },
  { text: "Backlog", file: "l5_backlog.mp3", voice: ARTHUR },
  { text: "Scope", file: "l5_scope.mp3", voice: ARTHUR },
  { text: "Downtime", file: "l5_downtime.mp3", voice: ARTHUR },
  { text: "Rollout", file: "l5_rollout.mp3", voice: ARTHUR },
  { text: "Workaround", file: "l5_workaround.mp3", voice: ARTHUR },

  // Vocab example sentences (alternate Arthur/Ellen)
  { text: "We completed all the tasks in the last sprint.", file: "l5_we_completed_all_the_tasks.mp3", voice: ARTHUR },
  { text: "The QA team found a critical bug in the payment module.", file: "l5_the_qa_team_found_a_critical.mp3", voice: ELLEN },
  { text: "We added a new search feature to the dashboard.", file: "l5_we_added_a_new_search.mp3", voice: ARTHUR },
  { text: "There are fifteen items in the backlog for next sprint.", file: "l5_there_are_fifteen_items.mp3", voice: ELLEN },
  { text: "The scope of the project increased after the client meeting.", file: "l5_the_scope_of_the_project.mp3", voice: ARTHUR },
  { text: "We had two hours of downtime last Friday.", file: "l5_we_had_two_hours_of_downtime.mp3", voice: ELLEN },
  { text: "The rollout of the new system starts next Monday.", file: "l5_the_rollout_of_the_new.mp3", voice: ARTHUR },
  { text: "We implemented a workaround until the permanent fix is ready.", file: "l5_we_implemented_a_workaround.mp3", voice: ELLEN },

  // Grammar context sentences (alternate)
  { text: "We fixed three critical bugs last sprint.", file: "l5_we_fixed_three_critical.mp3", voice: ARTHUR },
  { text: "The team deployed the update on Friday.", file: "l5_the_team_deployed_the_update.mp3", voice: ELLEN },
  { text: "I presented the results to the board yesterday.", file: "l5_i_presented_the_results.mp3", voice: ARTHUR },
  { text: "The client approved the new feature last week.", file: "l5_the_client_approved.mp3", voice: ELLEN },

  // Fill-in sentences (alternate)
  { text: "We fixed the login bug before the deadline.", file: "l5_fill_we_fixed_the_login.mp3", voice: ARTHUR },
  { text: "The team deployed the update last Friday.", file: "l5_fill_the_team_deployed.mp3", voice: ELLEN },
  { text: "I presented the sprint results to Margaret yesterday.", file: "l5_fill_i_presented_the_sprint.mp3", voice: ARTHUR },
  { text: "We reduced downtime by 40 percent last quarter.", file: "l5_fill_we_reduced_downtime.mp3", voice: ELLEN },
  { text: "The QA team found and reported five bugs last sprint.", file: "l5_fill_the_qa_team_found.mp3", voice: ARTHUR },

  // Dialogue (Rafael=Arthur, Margaret Torres=Ellen)
  { text: "Good afternoon, Margaret. Thank you for joining the sprint review. I prepared a summary of what we accomplished in the last two weeks.", file: "l5_dialogue_rafael_1.mp3", voice: ARTHUR },
  { text: "Good afternoon, Rafael. I appreciate the update. What were the main deliverables this sprint?", file: "l5_dialogue_margaret_2.mp3", voice: ELLEN },
  { text: "We completed three major items. First, we fixed a critical bug in the payment system. It caused errors for about 5 percent of transactions.", file: "l5_dialogue_rafael_3.mp3", voice: ARTHUR },
  { text: "What does that mean in simple terms? How did it affect our customers?", file: "l5_dialogue_margaret_4.mp3", voice: ELLEN },
  { text: "In simple terms, some customers saw error messages when they tried to pay. We identified the problem and deployed a fix on Tuesday. Since then, zero errors.", file: "l5_dialogue_rafael_5.mp3", voice: ARTHUR },
  { text: "That is great news. What about the new features?", file: "l5_dialogue_margaret_6.mp3", voice: ELLEN },
  { text: "We added a new search feature to the dashboard. Think of it like a search bar that helps users find their data in seconds instead of clicking through multiple pages.", file: "l5_dialogue_rafael_7.mp3", voice: ARTHUR },
  { text: "Excellent. And what is in the backlog for the next sprint?", file: "l5_dialogue_margaret_8.mp3", voice: ELLEN },

  // Listening 1 (Arthur - full sprint review)
  { text: "Good afternoon, everyone. I am presenting the results of Sprint 14. We had three main goals this sprint. First, we fixed a critical bug in the payment system. The bug caused transaction errors for about 5 percent of our users. We identified the root cause on Monday, developed a fix by Wednesday, and deployed it on Thursday. Since the deployment, we recorded zero transaction errors. Second, we added a new search feature to the customer dashboard. Before this feature, users clicked through four or five pages to find their data. Now they type a keyword and see results in two seconds. Early feedback from the beta group showed a 60 percent reduction in support tickets about finding information. Third, we started the rollout of the new notification system. We completed the backend work and began testing with a small group of users. The full rollout starts next Monday. For the next sprint, we have fifteen items in the backlog. The top priority is fixing the remaining bugs from the QA report and expanding the search feature to mobile.", file: "l5_listening1_sprint_review.mp3", voice: ARTHUR },

  // Listening 2 (Ellen - Margaret questions)
  { text: "Rafael, thank you for the sprint update. I have a few questions for you. First, you mentioned the payment bug affected 5 percent of transactions. How many customers were impacted? Can you give me a number? Second, the new search feature sounds promising. You said support tickets decreased by 60 percent. Is that based on the full user base or just the beta group? And finally, you mentioned fifteen items in the backlog. That sounds like a lot. Is there any risk that the scope is too large for one sprint? Do we need to prioritize?", file: "l5_listening2_margaret_questions.mp3", voice: ELLEN },

  // Survival card (Arthur)
  { text: "We fixed three critical bugs last sprint.", file: "l5_survival_we_fixed_three.mp3", voice: ARTHUR },
  { text: "In simple terms, the system was running too slowly.", file: "l5_survival_in_simple_terms.mp3", voice: ARTHUR },
  { text: "We deployed the update on Friday and it is working perfectly.", file: "l5_survival_we_deployed.mp3", voice: ARTHUR },
  { text: "The rollout starts next Monday with a small group of users.", file: "l5_survival_the_rollout_starts.mp3", voice: ARTHUR },
  { text: "We implemented a temporary workaround while we develop the permanent fix.", file: "l5_survival_we_implemented.mp3", voice: ARTHUR },

  // Speech practice (Arthur)
  { text: "We fixed a critical bug in the payment system and deployed the update on Thursday.", file: "l5_speech_we_fixed_a_critical.mp3", voice: ARTHUR },
  { text: "In simple terms, some customers saw error messages when they tried to pay.", file: "l5_speech_in_simple_terms.mp3", voice: ARTHUR },
  { text: "We added a new search feature that reduced support tickets by 60 percent.", file: "l5_speech_we_added_a_new.mp3", voice: ARTHUR },
];

function generateAudio(entry) {
  return new Promise((resolve, reject) => {
    const outputPath = path.join(OUTPUT_DIR, entry.file);

    // Skip if file already exists
    if (fs.existsSync(outputPath)) {
      console.log(`SKIP (exists): ${entry.file}`);
      return resolve();
    }

    const data = JSON.stringify({
      text: entry.text,
      model_id: "eleven_monolingual_v1",
      voice_settings: { stability: 0.5, similarity_boost: 0.75 }
    });

    const options = {
      hostname: 'api.elevenlabs.io',
      path: `/v1/text-to-speech/${entry.voice}`,
      method: 'POST',
      headers: {
        'Accept': 'audio/mpeg',
        'xi-api-key': API_KEY,
        'Content-Type': 'application/json',
        'Content-Length': Buffer.byteLength(data)
      }
    };

    const req = https.request(options, (res) => {
      if (res.statusCode !== 200) {
        let body = '';
        res.on('data', chunk => body += chunk);
        res.on('end', () => {
          console.error(`ERROR ${res.statusCode} for ${entry.file}: ${body}`);
          reject(new Error(`HTTP ${res.statusCode}`));
        });
        return;
      }
      const chunks = [];
      res.on('data', chunk => chunks.push(chunk));
      res.on('end', () => {
        fs.writeFileSync(outputPath, Buffer.concat(chunks));
        console.log(`OK: ${entry.file} (${entry.voice === ARTHUR ? 'Arthur' : 'Ellen'})`);
        resolve();
      });
    });

    req.on('error', reject);
    req.write(data);
    req.end();
  });
}

async function main() {
  console.log(`\nGenerating ${entries.length} audio files for Rafael Pelizaro L5...\n`);

  for (let i = 0; i < entries.length; i++) {
    await generateAudio(entries[i]);
    // Rate limit: wait 500ms between requests
    if (i < entries.length - 1) await new Promise(r => setTimeout(r, 500));
  }

  console.log(`\nDone! ${entries.length} files processed.`);
}

main().catch(console.error);
