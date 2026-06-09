const fs = require('fs');
const path = require('path');
const https = require('https');

const ELEVENLABS_API_KEY = process.env.ELEVENLABS_API_KEY;
if (!ELEVENLABS_API_KEY) {
  console.error('ERROR: ELEVENLABS_API_KEY not set');
  process.exit(1);
}

// Vozes atualizadas (jun/2026)
const ASH = 'VU16byTywsWv5JpI8rbc';    // Masculina neutra (Roberto)
const RILEY = 'hA4zGnmTwX2NQiTRMt7o';  // Feminina neutra (David - para contraste)

const OUTPUT_DIR = path.join(__dirname, 'public', 'audio', 'roberto-rezende');

// 13 áudios faltando do IN CLASS aula 2
// Diálogo Roberto + David (linhas 47-54) + frases ordering (55-59)
const audios = [
  // Diálogo - Roberto fala
  { text: "Good morning, David. I heard you also transitioned from engineering.", file: "aula2_good_morning_david.mp3", voice: ASH },
  // Diálogo - David fala
  { text: "That is right, Roberto. I studied chemical engineering but moved into sales ten years ago.", file: "aula2_thats_right_roberto.mp3", voice: RILEY },
  // Roberto
  { text: "Really? What made you change?", file: "aula2_really_what_made_you_change.mp3", voice: ASH },
  // David
  { text: "The company needed someone to lead the Asia Pacific client base. It was challenging but I achieved great results.", file: "aula2_the_company_needed_someone_to_lead.mp3", voice: RILEY },
  // Roberto
  { text: "I understand. I transitioned in 2019. Now I manage over fifty clients and negotiate contracts every month.", file: "aula2_i_understand_i_transitioned.mp3", voice: ASH },
  // David
  { text: "That is impressive. How is the revenue looking this year?", file: "aula2_that_is_impressive.mp3", voice: RILEY },
  // Roberto
  { text: "We achieved our target three months early. Now we are expanding into agriculture.", file: "aula2_we_achieved_our_target.mp3", voice: ASH },
  // David
  { text: "Great work. Do you attend many trade fairs?", file: "aula2_great_work_do_you_attend.mp3", voice: RILEY },
  // Ordering/Survival phrases - todas Roberto (Ash)
  { text: "I transitioned from engineering to sales. Now I lead the Brazilian market.", file: "aula2_i_transitioned_now_i_lead.mp3", voice: ASH },
  { text: "We achieved our sales target and expanded into agriculture.", file: "aula2_we_achieved_and_expanded.mp3", voice: ASH },
  { text: "I manage over fifty clients and negotiate contracts every month.", file: "aula2_i_manage_and_negotiate.mp3", voice: ASH },
  { text: "Negotiating in English is challenging, but I attend trade fairs to build our client base.", file: "aula2_negotiating_is_challenging.mp3", voice: ASH },
  { text: "Our revenue increased by fifteen percent. The company is expanding.", file: "aula2_our_revenue_increased_expanding.mp3", voice: ASH },
];

function generateAudio(text, voiceId, outputPath) {
  return new Promise((resolve, reject) => {
    const data = JSON.stringify({
      text: text,
      model_id: 'eleven_multilingual_v2',
      voice_settings: { stability: 0.5, similarity_boost: 0.75 }
    });

    const options = {
      hostname: 'api.elevenlabs.io',
      path: `/v1/text-to-speech/${voiceId}`,
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
        res.on('end', () => reject(new Error(`HTTP ${res.statusCode}: ${body}`)));
        return;
      }
      const chunks = [];
      res.on('data', c => chunks.push(c));
      res.on('end', () => {
        fs.writeFileSync(outputPath, Buffer.concat(chunks));
        resolve();
      });
    });

    req.on('error', reject);
    req.write(data);
    req.end();
  });
}

async function main() {
  if (!fs.existsSync(OUTPUT_DIR)) fs.mkdirSync(OUTPUT_DIR, { recursive: true });

  console.log(`Gerando ${audios.length} áudios para roberto-rezende aula2...\n`);

  for (let i = 0; i < audios.length; i++) {
    const a = audios[i];
    const outPath = path.join(OUTPUT_DIR, a.file);

    // Pular se já existe
    if (fs.existsSync(outPath)) {
      console.log(`[${i+1}/${audios.length}] SKIP (já existe): ${a.file}`);
      continue;
    }

    const voiceName = a.voice === ASH ? 'Ash' : 'Riley';
    console.log(`[${i+1}/${audios.length}] ${voiceName}: "${a.text.substring(0, 60)}..." → ${a.file}`);

    try {
      await generateAudio(a.text, a.voice, outPath);
      console.log(`  ✓ OK`);
    } catch (err) {
      console.error(`  ✗ ERRO: ${err.message}`);
    }

    // Rate limit protection
    if (i < audios.length - 1) await new Promise(r => setTimeout(r, 500));
  }

  console.log('\nDone!');
}

main();
