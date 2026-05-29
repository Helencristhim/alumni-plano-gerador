const fs = require('fs');
const path = require('path');
const https = require('https');

const ELEVENLABS_API_KEY = process.env.ELEVENLABS_API_KEY;
if (!ELEVENLABS_API_KEY) { console.error('ERROR: ELEVENLABS_API_KEY not set'); process.exit(1); }

const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const OUTPUT_DIR = path.join(__dirname, '..', 'public', 'audio', 'eduardo-chiba');

// All phrases from Eduardo Chiba's professor audioMap
const audioMap = {
  // Survival / emergency phrases
  "Could you repeat that, please?": "could_you_repeat_that_please.mp3",
  "Let me give you some context on that.": "let_me_give_you_some_context_on_that.mp3",
  "From a business perspective, I would say...": "from_a_business_perspective_i_would_say.mp3",
  "That is an excellent point.": "that_is_an_excellent_point.mp3",
  "In my experience at Quinto Andar...": "in_my_experience_at_quinto_andar.mp3",

  // Vocab words (single words)
  "Partnership": "partnership.mp3",
  "Stakeholder": "stakeholder.mp3",
  "Inventory": "inventory.mp3",
  "Scalable": "scalable.mp3",
  "Pipeline": "pipeline.mp3",
  "Onboarding": "onboarding.mp3",
  "Revenue": "revenue.mp3",
  "Milestone": "milestone.mp3",

  // Vocab example sentences
  "We are building new partnerships with real estate agencies across Brazil.": "we_are_building_new_partnerships_with_real_estate_agencies.mp3",
  "The stakeholders are expecting a progress update by Friday.": "the_stakeholders_are_expecting_a_progress_update.mp3",
  "Our inventory includes over ten thousand properties in Sao Paulo.": "our_inventory_includes_over_ten_thousand_properties.mp3",
  "The platform is highly scalable and can handle millions of users.": "the_platform_is_highly_scalable.mp3",
  "We have a strong pipeline of potential partners for next quarter.": "we_have_a_strong_pipeline_of_potential_partners.mp3",
  "The onboarding process for new brokers takes about two weeks.": "the_onboarding_process_for_new_brokers.mp3",
  "Our revenue has grown significantly since we launched the B2B unit.": "our_revenue_has_grown_significantly.mp3",
  "We reached an important milestone when we signed our hundredth agency.": "we_reached_an_important_milestone.mp3",

  // Context / grammar sentences
  "I am responsible for building partnerships with real estate agencies.": "i_am_responsible_for_building_partnerships.mp3",
  "Eduardo works with brokers to integrate their inventory into the platform.": "eduardo_works_with_brokers_to_integrate.mp3",
  "We are currently scaling our onboarding process for new partners.": "we_are_currently_scaling_our_onboarding_process.mp3",
  "The team has reached several important milestones this year.": "the_team_has_reached_several_important_milestones.mp3",
  "Our pipeline includes over fifty potential stakeholders.": "our_pipeline_includes_over_fifty_potential_stakeholders.mp3",
  "Quinto Andar generates most of its revenue from the B2B channel.": "quinto_andar_generates_most_of_its_revenue.mp3",

  // Self-introduction sentences
  "Let me introduce myself. I am Eduardo Chiba, Head of B2B at Quinto Andar.": "let_me_introduce_myself_i_am_eduardo_chiba.mp3",
  "I am responsible for partnerships with real estate agencies and brokers.": "i_am_responsible_for_partnerships_with_real_estate.mp3",
  "We are currently scaling our inventory integration platform across Brazil.": "we_are_currently_scaling_our_inventory_integration.mp3",

  // Order exercise — monologue (all 5 sentences combined)
  "[order-l1]": "order_l1_self_introduction.mp3",

  // Dialogue — Sarah lines (female → Ellen)
  "Hi! I am Sarah, VP of Partnerships at a PropTech firm in New York. Are you a speaker today?": "dialogue_sarah_line1.mp3",
  "Quinto Andar? I have heard of you! What exactly does your B2B unit do?": "dialogue_sarah_line3.mp3",
  "That sounds really scalable! How big is your partnership pipeline right now?": "dialogue_sarah_line5.mp3",
  "Impressive! Have you reached any major milestones recently?": "dialogue_sarah_line7.mp3",

  // Dialogue — Eduardo lines (male → Arthur)
  "Nice to meet you, Sarah! I am Eduardo Chiba, Head of B2B at Quinto Andar in Brazil.": "dialogue_eduardo_line2.mp3",
  "We work with real estate agencies and brokers. I am responsible for integrating their inventory into our platform.": "dialogue_eduardo_line4.mp3",
  "We are currently onboarding over fifty new agencies this quarter. Our pipeline is growing fast.": "dialogue_eduardo_line6.mp3",
  "Yes, we have just hit a significant revenue milestone. Our stakeholders are very pleased with the results.": "dialogue_eduardo_line8.mp3",

  // Survival IN CLASS
  "Let me introduce myself. I am Eduardo Chiba.": "survival_ic_1.mp3",
  "I am responsible for the B2B unit.": "survival_ic_2.mp3",
  "We are currently working on new partnerships.": "survival_ic_3.mp3",
  "I have been in this industry for five years.": "survival_ic_4.mp3",
  "I would love to discuss this further.": "survival_ic_5.mp3",

  // Quick fire answers
  "I am Eduardo Chiba, Head of B2B at Quinto Andar. I work with real estate agencies and brokers.": "quickfire_answer1.mp3",
  "We are currently scaling our partnership pipeline and onboarding new agencies.": "quickfire_answer2.mp3",
  "Our revenue has grown significantly. We have reached several important milestones this quarter.": "quickfire_answer3.mp3",
  "Our platform is highly scalable. We integrate broker inventory and make it available to millions of users.": "quickfire_answer4.mp3",
  "The onboarding process takes about two weeks. We help you integrate your inventory into our platform.": "quickfire_answer5.mp3",
  "We have just reached an important milestone — we signed our hundredth partner agency.": "quickfire_answer6.mp3",

  // Oral models
  "I am the Head of B2B at Quinto Andar, responsible for partnerships with real estate agencies.": "oral_model1.mp3",
  "We are currently scaling our onboarding process for new partner agencies.": "oral_model2.mp3",
  "Quinto Andar is one of Brazil's largest real estate platforms. We connect agencies, brokers, and customers.": "oral_model3.mp3",
  "We have reached an important milestone — we onboarded our hundredth partner agency this quarter.": "oral_model4.mp3",
  "We have a strong pipeline of potential partners. Over fifty agencies are in different stages of onboarding.": "oral_model5.mp3",
  "Our revenue has grown significantly since we launched the B2B unit. The stakeholders are very pleased.": "oral_model6.mp3",

  // Listening monologues (long-form, generated as single MP3)
  "listening1_full": "listening1_self_introduction.mp3",
  "listening2_full": "listening2_b2b_model.mp3",

  // Pre-class survival phrases
  "Let me introduce myself. I am Eduardo Chiba from Quinto Andar.": "preclass_survival_1.mp3",
  "I am the Head of the B2B Unit in Sao Paulo.": "preclass_survival_2.mp3",
  "I work with real estate agencies and brokers.": "preclass_survival_3.mp3",
  "We are currently scaling our partnership pipeline.": "preclass_survival_4.mp3",
  "I would love to discuss potential collaboration opportunities.": "preclass_survival_5.mp3"
};

// === SPECIAL LONG-FORM TEXTS ===
// These keys in audioMap are NOT the actual text to speak — they map to long monologues

const SPECIAL_TEXTS = {
  "[order-l1]": "Hi, I am Eduardo Chiba from Quinto Andar. I am the Head of the B2B Unit in Sao Paulo. I work with real estate agencies and brokers. We are currently scaling our partnership pipeline. I would love to discuss potential collaboration opportunities.",
  "listening1_full": "Let me introduce myself. I am Eduardo Chiba, Head of B2B at Quinto Andar. I am responsible for building partnerships with real estate agencies and brokers across Brazil. We are currently onboarding over fifty new agencies this quarter. Our inventory includes over ten thousand properties in Sao Paulo. I am very excited about the growth of our platform.",
  "listening2_full": "Quinto Andar is one of Brazil's largest real estate platforms. Our B2B unit works with agencies and brokers to integrate their inventory into our platform. The onboarding process for new partners takes about two weeks. We have a commission-based revenue model. Our pipeline includes over fifty potential stakeholders. We recently reached an important milestone — we signed our five hundredth partner agency nationwide. Our revenue has grown significantly since we launched the B2B unit."
};

// === VOICE ASSIGNMENT ===

// Sarah dialogue lines (female → always Ellen)
const sarahLines = [
  "Hi! I am Sarah, VP of Partnerships at a PropTech firm in New York. Are you a speaker today?",
  "Quinto Andar? I have heard of you! What exactly does your B2B unit do?",
  "That sounds really scalable! How big is your partnership pipeline right now?",
  "Impressive! Have you reached any major milestones recently?"
];

// Eduardo dialogue lines (male → always Arthur)
const eduardoDialogueLines = [
  "Nice to meet you, Sarah! I am Eduardo Chiba, Head of B2B at Quinto Andar in Brazil.",
  "We work with real estate agencies and brokers. I am responsible for integrating their inventory into our platform.",
  "We are currently onboarding over fifty new agencies this quarter. Our pipeline is growing fast.",
  "Yes, we have just hit a significant revenue milestone. Our stakeholders are very pleased with the results."
];

// Listening monologues → Arthur (Eduardo is male)
const listeningKeys = ["listening1_full", "listening2_full", "[order-l1]"];

function countWords(text) {
  return text.trim().split(/\s+/).length;
}

let phraseAlternator = 0;

function getVoice(text) {
  // Sarah dialogue lines → Ellen
  if (sarahLines.includes(text)) return { id: ELLEN, name: 'Ellen' };
  // Phrases starting with "Hi! I am Sarah" → Ellen
  if (text.startsWith('Hi! I am Sarah')) return { id: ELLEN, name: 'Ellen' };
  // Eduardo dialogue lines → Arthur
  if (eduardoDialogueLines.includes(text)) return { id: ARTHUR, name: 'Arthur' };
  // Listening monologues → Arthur (Eduardo is male)
  if (listeningKeys.includes(text)) return { id: ARTHUR, name: 'Arthur' };
  // Single words (1-2 words) → always Arthur
  const words = countWords(text);
  if (words <= 2) return { id: ARTHUR, name: 'Arthur' };
  // Other phrases (3+ words) → alternate Arthur/Ellen
  const voice = phraseAlternator % 2 === 0 ? { id: ARTHUR, name: 'Arthur' } : { id: ELLEN, name: 'Ellen' };
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

  console.log('Eduardo Chiba — Audio Generation');
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
        if (words > 2 && !sarahLines.includes(key) && !eduardoDialogueLines.includes(key) && !listeningKeys.includes(key)) {
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

    if (!success && generated === 0 && skipped === 0) {
      failed++;
    } else if (!success) {
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
