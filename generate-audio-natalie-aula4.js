const https = require('https');
const fs = require('fs');
const path = require('path');

const ASH = 'VU16byTywsWv5JpI8rbc';
const RILEY = 'hA4zGnmTwX2NQiTRMt7o';
const API_KEY = process.env.ELEVENLABS_API_KEY;
const OUTPUT_DIR = path.join(__dirname, 'public', 'audio', 'natalie-viegas');

const entries = [
  // ===== VOCAB WORDS (Riley - Natalie is female) =====
  { file: 'aula4_proposal.mp3', text: 'Proposal', voice: RILEY },
  { file: 'aula4_scope.mp3', text: 'Scope', voice: RILEY },
  { file: 'aula4_deliverable.mp3', text: 'Deliverable', voice: RILEY },
  { file: 'aula4_allocate.mp3', text: 'Allocate', voice: RILEY },
  { file: 'aula4_streamline.mp3', text: 'Streamline', voice: RILEY },
  { file: 'aula4_roll_out.mp3', text: 'Roll out', voice: RILEY },
  { file: 'aula4_assess.mp3', text: 'Assess', voice: RILEY },
  { file: 'aula4_sprint.mp3', text: 'Sprint', voice: RILEY },
  { file: 'aula4_track.mp3', text: 'Track', voice: RILEY },
  { file: 'aula4_scalable.mp3', text: 'Scalable', voice: RILEY },

  // ===== VOCAB EXAMPLE SENTENCES (alternate Riley/Ash) =====
  { file: 'aula4_i_am_writing_a_proposal.mp3', text: 'I am writing a proposal for the new security module.', voice: RILEY },
  { file: 'aula4_we_need_to_define_the_scope.mp3', text: 'We need to define the scope before starting the next phase.', voice: ASH },
  { file: 'aula4_we_are_tracking_all_deliverables.mp3', text: 'We are tracking all the deliverables in the project dashboard.', voice: RILEY },
  { file: 'aula4_i_have_allocated_the_budget.mp3', text: 'I have allocated the budget for next quarter.', voice: RILEY },
  { file: 'aula4_i_have_streamlined_the_approval.mp3', text: 'I have streamlined the approval process. It is now thirty percent faster.', voice: ASH },
  { file: 'aula4_i_am_currently_rolling_out.mp3', text: 'I am currently rolling out the first module of the system.', voice: RILEY },
  { file: 'aula4_we_are_assessing_the_risks.mp3', text: 'We are assessing the risks for the next sprint.', voice: ASH },
  { file: 'aula4_we_have_completed_three_sprints.mp3', text: 'We have completed three sprints so far.', voice: RILEY },
  { file: 'aula4_the_team_is_tracking_deliverables.mp3', text: 'The team is tracking all the deliverables in our project dashboard.', voice: ASH },
  { file: 'aula4_we_have_designed_scalable.mp3', text: 'We have designed the system to be scalable from the start.', voice: RILEY },

  // ===== FILL-IN-THE-BLANK SENTENCES =====
  { file: 'aula4_fill_i_am_currently_rolling_out.mp3', text: 'I am currently rolling out the new module for the Ministry of Justice.', voice: RILEY },
  { file: 'aula4_fill_we_have_already_completed.mp3', text: 'We have already completed three sprints this quarter.', voice: ASH },
  { file: 'aula4_fill_the_team_is_tracking.mp3', text: 'The team is tracking all deliverables in the project dashboard.', voice: RILEY },
  { file: 'aula4_fill_she_has_allocated.mp3', text: 'She has allocated the budget for the next quarter.', voice: ASH },
  { file: 'aula4_fill_i_have_streamlined.mp3', text: 'I have streamlined the approval process to save time.', voice: RILEY },
  { file: 'aula4_fill_we_are_assessing.mp3', text: 'We are assessing the scope of the new proposal.', voice: ASH },

  // ===== SPEECH CARDS (Riley - student voice) =====
  { file: 'aula4_speech_rolling_out_tracking.mp3', text: 'I am currently rolling out a new module and tracking all the deliverables.', voice: RILEY },
  { file: 'aula4_speech_completed_allocated.mp3', text: 'We have completed three sprints so far and have allocated the budget.', voice: RILEY },
  { file: 'aula4_speech_streamlined_scalable.mp3', text: 'I have streamlined the approval process and the system is scalable.', voice: RILEY },

  // ===== ORDERING =====
  { file: 'order_l4_ordering.mp3', text: 'We received the proposal from the Ministry of Justice. I assessed the scope and allocated the budget. The team has completed three sprints so far. We are currently rolling out the first module. Two more agencies have expressed interest in the system.', voice: RILEY },

  // ===== SURVIVAL CARD (Pre-class) =====
  { file: 'aula4_surv_i_am_currently_working.mp3', text: 'I am currently working on a major project.', voice: RILEY },
  { file: 'aula4_surv_we_have_completed.mp3', text: 'We have completed three sprints so far.', voice: ASH },
  { file: 'aula4_surv_i_have_allocated.mp3', text: 'I have allocated the budget for next quarter.', voice: RILEY },
  { file: 'aula4_surv_the_team_is_tracking.mp3', text: 'The team is tracking all the deliverables.', voice: ASH },
  { file: 'aula4_surv_the_system_is_scalable.mp3', text: 'The system is scalable for other agencies.', voice: RILEY },

  // ===== IN CLASS DIALOGUE (Carlos=Ash, Natalie=Riley) =====
  { file: 'aula4_dlg_good_morning_natalie.mp3', text: 'Good morning, Natalie. Can you give me a quick update on the Ministry of Justice project?', voice: ASH },
  { file: 'aula4_dlg_of_course_carlos.mp3', text: 'Of course, Carlos. We are making great progress. We have completed three sprints so far.', voice: RILEY },
  { file: 'aula4_dlg_that_is_excellent.mp3', text: 'That is excellent. What are you working on right now?', voice: ASH },
  { file: 'aula4_dlg_i_am_currently_rolling_out.mp3', text: 'I am currently rolling out the first module. The team is tracking all the deliverables in our project dashboard.', voice: RILEY },
  { file: 'aula4_dlg_have_you_allocated.mp3', text: 'Have you allocated the budget for next quarter?', voice: ASH },
  { file: 'aula4_dlg_yes_i_have.mp3', text: 'Yes, I have. I have also streamlined the approval process. It is now thirty percent faster.', voice: RILEY },
  { file: 'aula4_dlg_impressive_is_the_system.mp3', text: 'Impressive. Is the system scalable for other agencies?', voice: ASH },
  { file: 'aula4_dlg_absolutely_we_have.mp3', text: 'Absolutely. We have designed it to be scalable from the start. Two other agencies have already expressed interest.', voice: RILEY },

  // ===== IN CLASS ORAL DRILLING =====
  { file: 'aula4_oral_rolling_out_module.mp3', text: 'I am currently rolling out the first module.', voice: RILEY },
  { file: 'aula4_oral_completed_sprints.mp3', text: 'We have completed three sprints so far.', voice: RILEY },
  { file: 'aula4_oral_allocated_budget.mp3', text: 'I have allocated the budget for next quarter.', voice: RILEY },
  { file: 'aula4_oral_tracking_deliverables.mp3', text: 'The team is tracking all the deliverables.', voice: RILEY },
  { file: 'aula4_oral_streamlined_process.mp3', text: 'I have streamlined the approval process.', voice: RILEY },
  { file: 'aula4_oral_scalable_agencies.mp3', text: 'The system is scalable for other agencies.', voice: RILEY },

  // ===== IN CLASS ORAL DRILLING 2 (longer sentences) =====
  { file: 'aula4_oral2_allocated_rolling.mp3', text: 'We have allocated the resources and are now rolling out the system.', voice: RILEY },
  { file: 'aula4_oral2_assessing_scope.mp3', text: 'I am currently assessing the scope of the new proposal.', voice: RILEY },
  { file: 'aula4_oral2_streamlined_faster.mp3', text: 'The team has streamlined the process and it is now much faster.', voice: RILEY },
  { file: 'aula4_oral2_scalable_interest.mp3', text: 'Two agencies have expressed interest because the system is scalable.', voice: RILEY },

  // ===== IN CLASS SURVIVAL CARD =====
  { file: 'aula4_ic_surv_currently_working.mp3', text: 'I am currently working on a major project for the Ministry of Justice.', voice: RILEY },
  { file: 'aula4_ic_surv_completed_sprints.mp3', text: 'We have completed three sprints so far.', voice: RILEY },
  { file: 'aula4_ic_surv_allocated_budget.mp3', text: 'I have allocated the budget for next quarter.', voice: RILEY },
  { file: 'aula4_ic_surv_tracking_deliverables.mp3', text: 'The team is tracking all the deliverables.', voice: RILEY },
  { file: 'aula4_ic_surv_designed_scalable.mp3', text: 'The system has been designed to be scalable.', voice: RILEY },

  // ===== IN CLASS LISTENING PASSAGES =====
  { file: 'aula4_listening_1_standup.mp3', text: 'Good morning, team. Let me give you a quick update on the Ministry of Justice project. We are currently working on the security module. This is sprint four, and we are tracking five deliverables this week. The scope has not changed since the proposal was approved last month. However, I need to allocate more resources to the compliance review. The team is assessing the risks right now, and we have already streamlined the initial approval process. Our next milestone is the client demo scheduled for next Friday. Any questions? Great. Let us keep up the momentum.', voice: RILEY },
  { file: 'aula4_listening_2_briefing.mp3', text: 'Good afternoon, everyone. I am Natalie Viegas, Account Executive at Microsoft Brasil. I am here to present a progress update on the Ministry of Justice digital transformation project. We have completed three sprints so far and are currently rolling out the first module. Our team is tracking fifteen deliverables, and twelve are already complete. I have allocated the budget for the next quarter, and I have streamlined the procurement process, which is now thirty percent faster. The system we have built is scalable. Two additional agencies have already expressed interest in adopting the platform. We are assessing the scope for expanding the project in Q4. Thank you for your time. I am happy to take any questions.', voice: RILEY },

  // ===== IN CLASS ERROR AUDIO =====
  { file: 'aula4_ic_error_i_am_work.mp3', text: 'I am work on a new proposal right now.', voice: RILEY },
  { file: 'aula4_ic_error_we_have_complete.mp3', text: 'We have complete three sprints so far.', voice: RILEY },
  { file: 'aula4_ic_error_she_is_allocate.mp3', text: 'She is allocate the budget this week.', voice: RILEY },
  { file: 'aula4_ic_error_they_has_rolled.mp3', text: 'They has already rolled out the system.', voice: RILEY },
];

function generateAudio(entry) {
  return new Promise((resolve, reject) => {
    const data = JSON.stringify({
      text: entry.text,
      model_id: 'eleven_multilingual_v2',
      voice_settings: { stability: 0.5, similarity_boost: 0.75 }
    });

    const options = {
      hostname: 'api.elevenlabs.io',
      path: `/v1/text-to-speech/${entry.voice}`,
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'xi-api-key': API_KEY,
        'Content-Length': Buffer.byteLength(data)
      }
    };

    const outPath = path.join(OUTPUT_DIR, entry.file);

    if (fs.existsSync(outPath)) {
      console.log(`SKIP (exists): ${entry.file}`);
      return resolve();
    }

    const req = https.request(options, (res) => {
      if (res.statusCode !== 200) {
        let body = '';
        res.on('data', d => body += d);
        res.on('end', () => {
          console.error(`ERROR ${res.statusCode} for ${entry.file}: ${body}`);
          resolve();
        });
        return;
      }
      const ws = fs.createWriteStream(outPath);
      res.pipe(ws);
      ws.on('finish', () => {
        console.log(`OK: ${entry.file}`);
        resolve();
      });
      ws.on('error', reject);
    });

    req.on('error', reject);
    req.write(data);
    req.end();
  });
}

async function main() {
  if (!API_KEY) {
    console.error('ERROR: ELEVENLABS_API_KEY not set. Export it or add to ~/.zshrc');
    process.exit(1);
  }

  if (!fs.existsSync(OUTPUT_DIR)) {
    fs.mkdirSync(OUTPUT_DIR, { recursive: true });
  }

  console.log(`Generating ${entries.length} audio files for Natalie Viegas (Aula 4)...`);
  console.log(`Output: ${OUTPUT_DIR}\n`);

  for (let i = 0; i < entries.length; i++) {
    console.log(`[${i + 1}/${entries.length}] ${entries[i].file}`);
    await generateAudio(entries[i]);
    // Rate limit: 200ms between requests
    await new Promise(r => setTimeout(r, 200));
  }

  console.log('\nDone!');
}

main().catch(console.error);
