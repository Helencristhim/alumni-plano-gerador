const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const VOICE_ID = 'pNInz6obpgDQGcFmaJgB'; // Arthur
const OUTPUT_DIR = path.join(__dirname, '..', 'public', 'audio', 'maisa-de-oliveira-santos');
const MAP_PATH = path.join(OUTPUT_DIR, 'audioMap.json');

const PHRASES = [
  "Are you available on Thursday at 10 AM?",
  "Are you here for the meeting?",
  "Can we reschedule to Thursday?",
  "Can you join the meeting at three?",
  "Can you send me the report?",
  "Could you speak more slowly, please?",
  "David is visiting next month.",
  "Do you like thrillers?",
  "Excuse me, could you repeat that?",
  "For me...",
  "Good morning!",
  "Good morning, David. I am Maísa. I work in finance. Nice to meet you.",
  "How are you?",
  "How big is your team?",
  "How do you say that in English?",
  "How many people will be there?",
  "How was your weekend?",
  "I am 35 years old.",
  "I am Maísa.",
  "I am from São Paulo.",
  "I am going to attend the meeting tomorrow.",
  "I am meeting David on Thursday at 2 PM.",
  "I am sorry, I did not understand.",
  "I attended a board meeting last Tuesday.",
  "I can handle that.",
  "I can not make it at 2 PM.",
  "I can not speak English fluently yet.",
  "I can speak some English.",
  "I can speak some English. I cannot speak fluently yet, but I can learn.",
  "I check my emails first.",
  "I enjoy client meetings when I am prepared.",
  "I enjoy reading market analysis.",
  "I feel more confident about speaking.",
  "I like watching series.",
  "I prefer email to phone calls.",
  "I review market data every morning.",
  "I sent the report yesterday.",
  "I sometimes work from home.",
  "I still need to work on grammar.",
  "I think...",
  "I usually attend meetings on Mondays.",
  "I wake up at seven.",
  "I will send the report right now.",
  "I will send you the agenda by Friday.",
  "I work for a finance company in São Paulo.",
  "I work with a foreign partner.",
  "Last March, I missed a trip to Miami.",
  "My biggest improvement is vocabulary.",
  "My name is Maísa de Oliveira Santos.",
  "My office is on the third floor.",
  "My team manages client portfolios.",
  "One moment, please.",
  "Our firm has an international partner.",
  "Personally, I prefer...",
  "Tell me about last March.",
  "The meeting is on the 10th floor.",
  "There are 12 people in the room.",
  "There is a meeting room on every floor.",
  "What are you watching now?",
  "What are your plans for next week?",
  "What did you do at work yesterday?",
  "What do you do?",
  "What do you like most about your job?",
  "What do you like to do on weekends?",
  "What do you usually do on Monday mornings?",
  "What happened last month at work?",
  "What is your role here?",
  "What time does it start?",
  "When are you free next week?",
  "Where are you from?",
  "Which floor is the meeting on?",
  "Who are you?",
  "across from",
  "after lunch",
  "age",
  "always",
  "at noon",
  "attend meetings",
  "between",
  "binge-watch",
  "block the calendar",
  "blocked",
  "branch office",
  "by 5 PM",
  "by the end of the month",
  "came",
  "city",
  "comfortable",
  "confident",
  "department",
  "episode",
  "financial advisor",
  "floor",
  "go to the office",
  "got",
  "had",
  "handle",
  "headquarters",
  "in March",
  "in the afternoon",
  "in the morning",
  "in two weeks",
  "investment firm",
  "job",
  "last month",
  "last week",
  "last year",
  "made",
  "market",
  "meet clients",
  "meeting room",
  "missed",
  "nervous",
  "never",
  "next Monday",
  "next to",
  "next week",
  "often",
  "on Thursday",
  "plot twist",
  "portfolio manager",
  "postpone",
  "rarely",
  "reception",
  "review reports",
  "risk analyst",
  "said",
  "saw",
  "season",
  "send emails",
  "senior",
  "senior analyst",
  "set up a call",
  "sometimes",
  "streaming",
  "team",
  "told",
  "tomorrow",
  "traveled",
  "unavailable",
  "went",
  "work from home",
  "worked",
  "yesterday"
];

function safeName(text) {
  return text.replace(/[^a-z0-9]/gi, '_').substring(0, 50).toLowerCase();
}

async function generateOne(text, retries = 2) {
  const url = `https://api.elevenlabs.io/v1/text-to-speech/${VOICE_ID}`;
  const body = JSON.stringify({
    text,
    model_id: 'eleven_monolingual_v1',
    voice_settings: { stability: 0.5, similarity_boost: 0.75 }
  });

  for (let attempt = 0; attempt <= retries; attempt++) {
    try {
      const res = await fetch(url, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'xi-api-key': API_KEY,
          'Accept': 'audio/mpeg'
        },
        body
      });

      if (res.status === 429) {
        console.log(`  Rate limited, waiting 30s...`);
        await new Promise(r => setTimeout(r, 30000));
        continue;
      }

      if (!res.ok) {
        const err = await res.text();
        throw new Error(`HTTP ${res.status}: ${err}`);
      }

      const buffer = Buffer.from(await res.arrayBuffer());
      return buffer;
    } catch (e) {
      if (attempt === retries) throw e;
      await new Promise(r => setTimeout(r, 5000));
    }
  }
}

async function main() {
  if (!API_KEY) { console.error('No ELEVENLABS_API_KEY'); process.exit(1); }
  if (!fs.existsSync(OUTPUT_DIR)) fs.mkdirSync(OUTPUT_DIR, { recursive: true });

  // Load existing audioMap
  let audioMap = {};
  if (fs.existsSync(MAP_PATH)) {
    audioMap = JSON.parse(fs.readFileSync(MAP_PATH, 'utf-8'));
  }

  const total = PHRASES.length;
  let generated = 0, skipped = 0, failed = 0;

  for (let i = 0; i < PHRASES.length; i++) {
    const phrase = PHRASES[i];
    const filename = safeName(phrase) + '.mp3';
    const filepath = path.join(OUTPUT_DIR, filename);
    const relPath = `audio/maisa-de-oliveira-santos/${filename}`;

    // Skip if already exists
    if (audioMap[phrase] || fs.existsSync(filepath)) {
      if (!audioMap[phrase]) audioMap[phrase] = relPath;
      skipped++;
      continue;
    }

    try {
      process.stdout.write(`[${i+1}/${total}] Generating: "${phrase.substring(0,40)}..." `);
      const buffer = await generateOne(phrase);
      fs.writeFileSync(filepath, buffer);
      audioMap[phrase] = relPath;
      generated++;
      console.log('OK');
      // Rate limit: 150ms between requests
      await new Promise(r => setTimeout(r, 150));
    } catch (e) {
      console.log(`FAILED: ${e.message}`);
      failed++;
    }
  }

  // Save updated audioMap
  fs.writeFileSync(MAP_PATH, JSON.stringify(audioMap, null, 2));

  console.log(`\nDone! Generated: ${generated}, Skipped: ${skipped}, Failed: ${failed}`);
  console.log(`Total audioMap entries: ${Object.keys(audioMap).length}`);
}

main();
