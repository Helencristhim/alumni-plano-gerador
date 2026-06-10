const fs = require('fs');
const path = require('path');
const https = require('https');

const ELEVENLABS_API_KEY = process.env.ELEVENLABS_API_KEY;
if (!ELEVENLABS_API_KEY) {
  console.error('ERROR: ELEVENLABS_API_KEY not set');
  process.exit(1);
}

// Vozes atualizadas (jun/2026) — Roberto = male → ASH for protagonist
const ASH = 'VU16byTywsWv5JpI8rbc';    // Masculina neutra
const RILEY = 'hA4zGnmTwX2NQiTRMt7o';  // Feminina neutra

const OUTPUT_DIR = path.join(__dirname, '..', 'public', 'audio', 'roberto-rezende');
if (!fs.existsSync(OUTPUT_DIR)) fs.mkdirSync(OUTPUT_DIR, { recursive: true });

const audios = [
  // Vocab words (1-2 words = ASH)
  { text: "Recap", file: "aula10_recap.mp3", voice: ASH },
  { text: "Go over", file: "aula10_go_over.mp3", voice: ASH },
  { text: "Bring up", file: "aula10_bring_up.mp3", voice: ASH },
  { text: "Action items", file: "aula10_action_items.mp3", voice: ASH },
  { text: "Takeaway", file: "aula10_takeaway.mp3", voice: ASH },
  { text: "Sum up", file: "aula10_sum_up.mp3", voice: ASH },
  { text: "On the same page", file: "aula10_on_the_same_page.mp3", voice: ASH },
  { text: "Move on to", file: "aula10_move_on_to.mp3", voice: ASH },
  { text: "Input", file: "aula10_input.mp3", voice: ASH },
  { text: "Address", file: "aula10_address.mp3", voice: ASH },

  // Vocab sentences (alternating ASH/RILEY)
  { text: "Let me recap the results from Q1 before we move on.", file: "aula10_let_me_recap_the_results.mp3", voice: ASH },
  { text: "I would like to go over the pipeline update with you.", file: "aula10_i_would_like_to_go_over.mp3", voice: RILEY },
  { text: "Can I bring up the agricultural segment?", file: "aula10_can_i_bring_up_the_agricultural.mp3", voice: ASH },
  { text: "The action items for next quarter are clear.", file: "aula10_the_action_items_for_next.mp3", voice: RILEY },
  { text: "The key takeaway is that we are ahead of target.", file: "aula10_the_key_takeaway_is_that.mp3", voice: ASH },
  { text: "Let me sum up what we discussed today.", file: "aula10_let_me_sum_up_what_we.mp3", voice: RILEY },
  { text: "Are we all on the same page about the timeline?", file: "aula10_are_we_all_on_the_same.mp3", voice: ASH },
  { text: "Let us move on to the next topic.", file: "aula10_let_us_move_on_to_the_next.mp3", voice: RILEY },
  { text: "I would like your input on the new strategy.", file: "aula10_i_would_like_your_input.mp3", voice: ASH },
  { text: "We need to address this issue before Friday.", file: "aula10_we_need_to_address_this.mp3", voice: RILEY },

  // Dialogue: Roberto=ASH, Wei Lin=RILEY, Amy=RILEY
  { text: "Good morning, everyone. Let us get started. I would like to go over the Q2 pipeline results.", file: "aula10_dialogue_roberto1.mp3", voice: ASH },
  { text: "Thank you, Roberto. Before we move on, I would like to recap the targets we set in January.", file: "aula10_dialogue_weilin1.mp3", voice: RILEY },
  { text: "Good point. Our target was twenty new contracts. We are currently at eighteen.", file: "aula10_dialogue_roberto2.mp3", voice: ASH },
  { text: "That is excellent progress. I would like to bring up the agricultural segment. Are we on the same page about expanding there?", file: "aula10_dialogue_amy1.mp3", voice: RILEY },
  { text: "Yes. We are targeting five new prospects in agriculture. Two are converting this month.", file: "aula10_dialogue_roberto3.mp3", voice: ASH },
  { text: "Great. What are the action items for next quarter?", file: "aula10_dialogue_weilin2.mp3", voice: RILEY },
  { text: "I will send a summary email after this meeting. The key takeaway is that we are ahead of target.", file: "aula10_dialogue_roberto4.mp3", voice: ASH },
  { text: "Perfect. Let me sum up: eighteen contracts closed, two converting, and five new prospects. Well done, Roberto.", file: "aula10_dialogue_amy2.mp3", voice: RILEY },

  // Listening 1: Roberto's Q2 presentation (ASH)
  { text: "Good morning, team. I am going to present the Q2 results for the Brazilian market. We set a target of twenty new contracts in January. Currently, we have eighteen signed contracts. That is ninety percent of our target. The agricultural segment is performing well. We are working with five new prospects. Two are converting this month. Our revenue increased by fifteen percent compared to Q1. The biggest challenge this quarter was negotiating with the mining company. However, we are making good progress. I estimate we will close that deal by end of July. The team is also preparing for the Agrishow trade fair next month. I will send a detailed report by Friday. Are there any questions?", file: "aula10_listening1_q2_presentation.mp3", voice: ASH },

  // Listening 2: Amy's feedback (RILEY)
  { text: "Roberto, I have some input on how you ran this meeting. First, you addressed all the agenda items clearly. Your recap of the Q2 results was concise and professional. You used linking words effectively: however for contrast, currently for present actions. One suggestion: when you bring up new topics, give a brief context first. For example, instead of just saying we are targeting five prospects, explain why agriculture is a priority. Overall, your meeting skills are much stronger than in January. The team is on the same page thanks to your clear communication. Well done.", file: "aula10_listening2_amy_feedback.mp3", voice: RILEY },

  // Quick fire answers (alternating)
  { text: "Let me recap the results from last month.", file: "aula10_quickfire1.mp3", voice: ASH },
  { text: "Could we address that later? Let us move on to the pipeline update.", file: "aula10_quickfire2.mp3", voice: RILEY },
  { text: "I would like your input on the new pricing strategy.", file: "aula10_quickfire3.mp3", voice: ASH },
  { text: "Let me sum up the key takeaways from today.", file: "aula10_quickfire4.mp3", voice: RILEY },
  { text: "Wei Lin, the action item for you is to review the contract by Friday.", file: "aula10_quickfire5.mp3", voice: ASH },
  { text: "Are we all on the same page about the timeline?", file: "aula10_quickfire6.mp3", voice: RILEY },

  // Survival card (alternating)
  { text: "Let me recap the key points from last quarter.", file: "aula10_survival1.mp3", voice: ASH },
  { text: "I would like to go over the pipeline update.", file: "aula10_survival2.mp3", voice: RILEY },
  { text: "Are we all on the same page?", file: "aula10_survival3.mp3", voice: ASH },
  { text: "The main takeaway is that we are ahead of target.", file: "aula10_survival4.mp3", voice: RILEY },
  { text: "Let me sum up the action items for next quarter.", file: "aula10_survival5.mp3", voice: ASH },

  // Ordering audio (full meeting sequence)
  { text: "Good morning. Let me recap the Q2 results. We have eighteen signed contracts this quarter. We are currently working on five new agricultural prospects. I will send the summary email by end of day. Let me sum up the action items for next quarter.", file: "order_l10_ordering.mp3", voice: ASH }
];

function generateAudio(item) {
  return new Promise((resolve, reject) => {
    const filePath = path.join(OUTPUT_DIR, item.file);
    if (fs.existsSync(filePath)) {
      console.log(`SKIP (exists): ${item.file}`);
      return resolve();
    }

    const postData = JSON.stringify({
      text: item.text,
      model_id: "eleven_multilingual_v2",
      voice_settings: { stability: 0.5, similarity_boost: 0.75 }
    });

    const options = {
      hostname: 'api.elevenlabs.io',
      path: `/v1/text-to-speech/${item.voice}`,
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'xi-api-key': ELEVENLABS_API_KEY,
        'Accept': 'audio/mpeg'
      }
    };

    const req = https.request(options, (res) => {
      if (res.statusCode !== 200) {
        let body = '';
        res.on('data', c => body += c);
        res.on('end', () => {
          console.error(`ERROR ${res.statusCode} for ${item.file}: ${body}`);
          reject(new Error(`HTTP ${res.statusCode}`));
        });
        return;
      }
      const chunks = [];
      res.on('data', c => chunks.push(c));
      res.on('end', () => {
        fs.writeFileSync(filePath, Buffer.concat(chunks));
        console.log(`OK: ${item.file} (${item.voice === ASH ? 'ASH' : 'RILEY'})`);
        resolve();
      });
    });

    req.on('error', reject);
    req.write(postData);
    req.end();
  });
}

async function main() {
  console.log(`Generating ${audios.length} audio files for Roberto Rezende Aula 10...`);
  console.log(`Output: ${OUTPUT_DIR}\n`);

  for (let i = 0; i < audios.length; i++) {
    await generateAudio(audios[i]);
    // Rate limit: wait 500ms between requests
    if (i < audios.length - 1) await new Promise(r => setTimeout(r, 500));
  }

  console.log(`\nDone! ${audios.length} files processed.`);
}

main().catch(e => { console.error(e); process.exit(1); });
