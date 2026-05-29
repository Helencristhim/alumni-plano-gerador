const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const DIR = path.join(__dirname, '..', 'public', 'audio', 'maria-claudia-curimbaba');

// Voice rules:
// - Single words (1-2 words) = ALWAYS Arthur
// - Phrases (3+ words) = ALTERNATE Arthur/Ellen
// - Maria Claudia lines (female) = Ellen
// - Sarah Mitchell lines = Ellen
// - Male character lines = Arthur

const PHRASES = [
  // ===== Vocab words (1-2 words → ALWAYS Arthur) =====
  { text: "Headquarters", file: "aula2_headquarters.mp3", voice: ARTHUR },
  { text: "Branch", file: "aula2_branch.mp3", voice: ARTHUR },
  { text: "Board", file: "aula2_board.mp3", voice: ARTHUR },
  { text: "Shareholder", file: "aula2_shareholder.mp3", voice: ARTHUR },
  { text: "Merge", file: "aula2_merge.mp3", voice: ARTHUR },
  { text: "Acquire", file: "aula2_acquire.mp3", voice: ARTHUR },
  { text: "Division", file: "aula2_division.mp3", voice: ARTHUR },
  { text: "Assets", file: "aula2_assets.mp3", voice: ARTHUR },

  // ===== Vocab example sentences (alternate Arthur/Ellen) =====
  { text: "Our headquarters is located in downtown Sao Paulo.", file: "aula2_our_headquarters_is_located.mp3", voice: ARTHUR },
  { text: "We have two branches in the United States.", file: "aula2_we_have_two_branches.mp3", voice: ELLEN },
  { text: "The board of directors approved the expansion plan.", file: "aula2_the_board_of_directors_approved.mp3", voice: ARTHUR },
  { text: "Each shareholder receives a quarterly dividend report.", file: "aula2_each_shareholder_receives.mp3", voice: ELLEN },
  { text: "The two companies decided to merge last year.", file: "aula2_the_two_companies_decided_to_merge.mp3", voice: ARTHUR },
  { text: "We plan to acquire a logistics company in Texas.", file: "aula2_we_plan_to_acquire.mp3", voice: ELLEN },
  { text: "The technology division is our fastest-growing unit.", file: "aula2_the_technology_division.mp3", voice: ARTHUR },
  { text: "The company's assets include real estate and patents.", file: "aula2_the_companys_assets_include.mp3", voice: ELLEN },

  // ===== Key expressions (alternate) =====
  { text: "Our headquarters is located in...", file: "aula2_expr_our_headquarters_is_located_in.mp3", voice: ARTHUR },
  { text: "Our headquarters is located in Sao Paulo, and we manage operations across three countries.", file: "aula2_expr_hq_example.mp3", voice: ELLEN },
  { text: "The board is responsible for...", file: "aula2_expr_the_board_is_responsible_for.mp3", voice: ARTHUR },
  { text: "The board is responsible for approving major investments and strategic decisions.", file: "aula2_expr_board_example.mp3", voice: ELLEN },
  { text: "We have branches in...", file: "aula2_expr_we_have_branches_in.mp3", voice: ARTHUR },
  { text: "We have branches in Houston, Pittsburgh, and soon in Miami.", file: "aula2_expr_branches_example.mp3", voice: ELLEN },

  // ===== Grammar context passage (Maria Claudia narrative = Ellen) =====
  { text: "Maria Claudia is presenting her holding company to a potential partner from Houston. She explains that the company's headquarters is located in Sao Paulo. The board of directors meets every quarter to review the company's assets and approve new investments. There are three main divisions under the holding. The technology division is the largest, and there is a new logistics branch in Texas. The company's shareholders voted to acquire a small firm in Pittsburgh last month. There are also plans to merge two of the smaller subsidiaries into one stronger division.", file: "aula2_grammar_context_passage.mp3", voice: ELLEN },

  // ===== Fill-in-the-blank sentences (alternate) =====
  { text: "The holding's headquarters is in Sao Paulo.", file: "aula2_fill_the_holdings_headquarters.mp3", voice: ARTHUR },
  { text: "There are three divisions under the main company.", file: "aula2_fill_there_are_three_divisions.mp3", voice: ELLEN },
  { text: "The board's decision was to acquire a new firm.", file: "aula2_fill_the_boards_decision.mp3", voice: ARTHUR },
  { text: "There is a new branch in Texas.", file: "aula2_fill_there_is_a_new_branch.mp3", voice: ELLEN },
  { text: "The shareholders' meeting is scheduled for June.", file: "aula2_fill_the_shareholders_meeting.mp3", voice: ARTHUR },
  { text: "The company's assets include patents and real estate.", file: "aula2_fill_the_companys_assets.mp3", voice: ELLEN },
  { text: "There are two branches in the United States.", file: "aula2_fill_there_are_two_branches.mp3", voice: ARTHUR },
  { text: "The division's revenue grew by fifteen percent.", file: "aula2_fill_the_divisions_revenue.mp3", voice: ELLEN },

  // ===== Survival card phrases (Maria Claudia = Ellen) =====
  { text: "Our headquarters is located in Sao Paulo.", file: "aula2_surv_our_headquarters.mp3", voice: ELLEN },
  { text: "The holding has three subsidiaries.", file: "aula2_surv_the_holding_has.mp3", voice: ELLEN },
  { text: "The board meets quarterly to review our assets.", file: "aula2_surv_the_board_meets.mp3", voice: ELLEN },
  { text: "We are looking to acquire a new company.", file: "aula2_surv_we_are_looking.mp3", voice: ELLEN },
  { text: "There are branches in Houston and Pittsburgh.", file: "aula2_surv_there_are_branches.mp3", voice: ELLEN },

  // ===== Speech practice cards (Maria Claudia = Ellen) =====
  { text: "Our headquarters is located in downtown Sao Paulo, Brazil.", file: "aula2_speech_our_headquarters.mp3", voice: ELLEN },
  { text: "The board of directors is responsible for approving all major investments.", file: "aula2_speech_the_board_of_directors.mp3", voice: ELLEN },
  { text: "There are three divisions under our holding company.", file: "aula2_speech_there_are_three.mp3", voice: ELLEN },
  { text: "We have branches in Houston, Pittsburgh, and Texas.", file: "aula2_speech_we_have_branches.mp3", voice: ELLEN },
  { text: "The shareholders approved the plan to acquire a new firm.", file: "aula2_speech_the_shareholders_approved.mp3", voice: ELLEN },
];

async function gen(text, voiceId, outPath) {
  const r = await fetch('https://api.elevenlabs.io/v1/text-to-speech/' + voiceId, {
    method: 'POST',
    headers: { 'xi-api-key': API_KEY, 'Content-Type': 'application/json' },
    body: JSON.stringify({
      text,
      model_id: 'eleven_multilingual_v2',
      voice_settings: { stability: 0.5, similarity_boost: 0.75 }
    }),
  });
  if (!r.ok) throw new Error(r.status + ': ' + (await r.text()));
  const buf = Buffer.from(await r.arrayBuffer());
  fs.writeFileSync(outPath, buf);
  return buf.length;
}

async function main() {
  if (!API_KEY) { console.error('Set ELEVENLABS_API_KEY env var'); process.exit(1); }
  if (!fs.existsSync(DIR)) fs.mkdirSync(DIR, { recursive: true });

  const seen = new Set();
  const unique = PHRASES.filter(p => {
    const k = p.file.toLowerCase();
    if (seen.has(k)) return false;
    seen.add(k);
    return true;
  });

  console.log('Generating ' + unique.length + ' AULA 2 audio files for Maria Claudia Curimbaba...');
  let generated = 0;
  let skipped = 0;

  for (const p of unique) {
    const outPath = path.join(DIR, p.file);
    if (fs.existsSync(outPath)) {
      console.log('SKIP: ' + p.file);
      skipped++;
    } else {
      try {
        const bytes = await gen(p.text, p.voice, outPath);
        console.log('OK [' + (p.voice === ELLEN ? 'ellen' : 'arthur') + ']: ' + p.file + ' (' + (bytes / 1024).toFixed(1) + 'KB)');
        generated++;
        await new Promise(r => setTimeout(r, 500));
      } catch (e) {
        console.error('FAIL: ' + p.file + ' — ' + e.message);
      }
    }
  }

  console.log('\nDone! Generated: ' + generated + ', Skipped: ' + skipped + ', Total entries: ' + unique.length);
  console.log('Audio files saved to: ' + DIR);
}

main().catch(e => { console.error(e); process.exit(1); });
