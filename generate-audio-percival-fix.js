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

// 19 missing audioMap entries + 1 listening exercise
const missingAudios = [
  // === percival-jr (Aula 1) — Percival's lines = Arthur ===
  { text: "I am the Director of Risk and Internal Audit.", path: "public/audio/percival-jr/i_am_the_director_of_risk_and_internal_audit.mp3", voice: ARTHUR },
  { text: "Right now, we are updating the risk matrix.", path: "public/audio/percival-jr/right_now_we_are_updating_the_risk_matrix.mp3", voice: ARTHUR },
  { text: "I am currently focused on compliance.", path: "public/audio/percival-jr/i_am_currently_focused_on_compliance.mp3", voice: ARTHUR },
  { text: "We are developing an action plan for the problem.", path: "public/audio/percival-jr/we_are_developing_an_action_plan_for_the_problem.mp3", voice: ARTHUR },
  { text: "First of all, we identified the issue in the operations department.", path: "public/audio/percival-jr/first_of_all_we_identified_the_issue_in_the_operations.mp3", voice: ELLEN },
  { text: "I am the Director of Risk and Internal Audit at EGEA Saneamento.", path: "public/audio/percival-jr/i_am_the_director_of_risk_and_internal_audit_at_egea.mp3", voice: ARTHUR },
  { text: "I work closely with the operations team.", path: "public/audio/percival-jr/i_work_closely_with_the_operations_team.mp3", voice: ELLEN },

  // === percival-jr-aula2 ===
  { text: "Carry-on", path: "public/audio/percival-jr-aula2/carry_on.mp3", voice: ARTHUR },
  { text: "My carry-on is in the overhead bin.", path: "public/audio/percival-jr-aula2/my_carry_on_is_in_the_overhead_bin.mp3", voice: ELLEN },

  // === percival-jr-aula4 ===
  { text: "My team is reviewing the internal controls and updating the risk matrix.", path: "public/audio/percival-jr-aula4/my_team_is_reviewing_the_internal_controls_updating.mp3", voice: ARTHUR },
  { text: "Right now, I am leading an internal audit.", path: "public/audio/percival-jr-aula4/right_now_i_am_leading_an_internal_audit_short.mp3", voice: ELLEN },
  { text: "My team is reviewing the risk matrix.", path: "public/audio/percival-jr-aula4/my_team_is_reviewing_the_risk_matrix.mp3", voice: ARTHUR },
  { text: "It depends on the stakeholders.", path: "public/audio/percival-jr-aula4/it_depends_on_the_stakeholders_short.mp3", voice: ELLEN },

  // === percival-jr-aula5 ===
  { text: "The project is on track. However, we need more time for compliance.", path: "public/audio/percival-jr-aula5/the_project_is_on_track_however_compliance.mp3", voice: ARTHUR },
  { text: "However, we are facing a delay.", path: "public/audio/percival-jr-aula5/however_we_are_facing_a_delay.mp3", voice: ELLEN },
  { text: "Therefore, compliance is our top priority.", path: "public/audio/percival-jr-aula5/therefore_compliance_is_our_top_priority.mp3", voice: ARTHUR },
  { text: "In addition, I am preparing an update for the board.", path: "public/audio/percival-jr-aula5/in_addition_i_am_preparing_an_update.mp3", voice: ELLEN },
  { text: "First of all, we identified the issue. Then, we developed an action plan. However, we are facing a delay.", path: "public/audio/percival-jr-aula5/first_of_all_then_however.mp3", voice: ARTHUR },
  { text: "We are facing a delay. Therefore, compliance is our top priority.", path: "public/audio/percival-jr-aula5/we_are_facing_a_delay_therefore.mp3", voice: ELLEN },

  // === Listening exercise (Q&A session) ===
  { text: "Thank you for your introduction, Percival. I have a question about your team. How many people are on your team, and what do they do? I manage a team of ten specialists. They are responsible for internal audit, risk assessment, and compliance. We work closely with the operations team.", path: "public/audio/percival-jr/qanda_session_listening.mp3", voice: ARTHUR },
];

function generateAudio(text, voiceId, outputPath) {
  return new Promise((resolve, reject) => {
    const postData = JSON.stringify({
      text: text,
      model_id: 'eleven_monolingual_v1',
      voice_settings: {
        stability: 0.5,
        similarity_boost: 0.75
      }
    });

    const options = {
      hostname: 'api.elevenlabs.io',
      path: `/v1/text-to-speech/${voiceId}?output_format=mp3_44100_128`,
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'xi-api-key': ELEVENLABS_API_KEY,
        'Content-Length': Buffer.byteLength(postData)
      }
    };

    const req = https.request(options, (res) => {
      if (res.statusCode !== 200) {
        let body = '';
        res.on('data', (d) => body += d);
        res.on('end', () => reject(new Error(`API ${res.statusCode}: ${body}`)));
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

function delay(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function main() {
  console.log(`Generating ${missingAudios.length} missing audio files...\n`);

  for (let i = 0; i < missingAudios.length; i++) {
    const item = missingAudios[i];
    const outputPath = path.join(__dirname, item.path);
    const voiceName = item.voice === ARTHUR ? 'Arthur' : 'Ellen';

    // Ensure directory exists
    const dir = path.dirname(outputPath);
    if (!fs.existsSync(dir)) fs.mkdirSync(dir, { recursive: true });

    // Skip if already exists
    if (fs.existsSync(outputPath)) {
      console.log(`[${i+1}/${missingAudios.length}] SKIP (exists): ${path.basename(item.path)}`);
      continue;
    }

    console.log(`[${i+1}/${missingAudios.length}] ${voiceName}: "${item.text.substring(0, 60)}..." -> ${path.basename(item.path)}`);

    try {
      await generateAudio(item.text, item.voice, outputPath);
      console.log(`  ✓ OK`);
    } catch (err) {
      console.error(`  ✗ ERROR: ${err.message}`);
    }

    // Rate limit: wait between requests
    if (i < missingAudios.length - 1) {
      await delay(500);
    }
  }

  console.log('\nDone!');
}

main().catch(console.error);
