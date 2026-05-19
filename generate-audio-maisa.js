const https = require('https');
const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
if (!API_KEY) {
  console.error('ERROR: ELEVENLABS_API_KEY environment variable is not set.');
  process.exit(1);
}

const VOICE_ID = 'sfJopaWaOtauCD3HKX6Q';
const MODEL_ID = 'eleven_monolingual_v1';
const OUTPUT_DIR = path.join(__dirname, 'public', 'audio', 'maisa-de-oliveira-santos');
const DELAY_MS = 150;

function safeFilename(text) {
  let name = text
    .toLowerCase()
    .replace(/['']/g, '')
    .replace(/[^a-z0-9]+/g, '_')
    .replace(/^_+|_+$/g, '');
  if (name.length > 50) name = name.substring(0, 50).replace(/_+$/, '');
  return name + '.mp3';
}

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

function generateAudio(text, filePath) {
  return new Promise((resolve, reject) => {
    const postData = JSON.stringify({
      text: text,
      model_id: MODEL_ID,
      voice_settings: {
        stability: 0.5,
        similarity_boost: 0.75
      }
    });

    const options = {
      hostname: 'api.elevenlabs.io',
      port: 443,
      path: `/v1/text-to-speech/${VOICE_ID}?output_format=mp3_44100_128`,
      method: 'POST',
      headers: {
        'Accept': 'audio/mpeg',
        'Content-Type': 'application/json',
        'xi-api-key': API_KEY
      }
    };

    const req = https.request(options, (res) => {
      if (res.statusCode !== 200) {
        let body = '';
        res.on('data', chunk => body += chunk);
        res.on('end', () => reject(new Error(`HTTP ${res.statusCode}: ${body}`)));
        return;
      }

      const fileStream = fs.createWriteStream(filePath);
      res.pipe(fileStream);
      fileStream.on('finish', () => {
        fileStream.close();
        resolve();
      });
      fileStream.on('error', reject);
    });

    req.on('error', reject);
    req.write(postData);
    req.end();
  });
}

const ALL_PHRASES = [
  // LESSON 1 - Vocabulary
  "name", "work", "live", "company", "meeting", "client", "partner", "office", "finance",
  // LESSON 1 - Pre-class examples
  "My name is Maísa.", "I work in finance.", "I live in São Paulo.", "My company has international partners.",
  "I have a meeting today.", "The client called this morning.", "My partner is from New York.",
  "I go to the office three times a week.",
  // LESSON 1 - Material examples
  "Her name is Maísa de Oliveira Santos.", "She works in the financial sector.",
  "Maísa lives in São Paulo, Brazil.", "The company has offices in two cities.",
  "We have a meeting every Monday.", "Our client is very important.",
  "The foreign partner visits every month.", "The office is in the business district.",
  // LESSON 1 - Expressions
  "My name is Maísa.", "I'm from São Paulo.", "I work in finance.", "I'm a senior professional.", "Nice to meet you.",
  // LESSON 1 - Survival card
  "Hello, my name is Maísa.", "I work in finance in São Paulo.", "Nice to meet you.", "I'm from Brazil.",
  // LESSON 2 - Vocabulary
  "analyst", "portfolio", "investment", "manage", "firm", "sector", "deal with", "financial", "based in",
  // LESSON 2 - Pre-class examples
  "I am a senior analyst.", "My portfolio includes several assets.", "Investment is my area of expertise.",
  "I manage a team of five people.", "Our firm is well-known in the market.",
  "The financial sector is very dynamic.", "I deal with clients every day.", "I am based in São Paulo.",
  // LESSON 2 - Material examples
  "She is a senior professional in finance.", "The portfolio performed well last quarter.",
  "This investment requires careful analysis.", "Maísa manages important client accounts.",
  "The firm has international partners.", "Working in the financial sector is demanding.",
  "She deals with complex transactions.", "The team is based in the Faria Lima district.",
  // LESSON 2 - Expressions
  "I work in finance.", "I'm a senior professional at my firm.", "My company has a foreign partner.",
  "I deal with clients daily.", "I'm based in São Paulo.",
  // LESSON 3 - Vocabulary
  "busy", "weekend", "commute", "weather", "plans", "quite", "same here", "elevator", "small talk",
  // LESSON 3 - Pre-class examples
  "I am very busy today.", "Do you have plans for the weekend?", "My commute takes about forty minutes.",
  "The weather is hot today.", "I have no plans for Saturday.", "It's quite humid in São Paulo.",
  "Same here, I have a lot of meetings.", "I take the elevator every morning.",
  // LESSON 3 - Material examples
  "It's been a busy week at the office.", "Any plans for the weekend?",
  "How is your commute to the office?", "The weather has been really hot lately.",
  "I'm planning to rest this weekend.", "It's quite cold today, isn't it?",
  "Same here, lots of work.", "We met in the elevator this morning.",
  // LESSON 3 - Key dialogue
  "Good morning, David. How's it going?", "Pretty good, thanks. Busy week?",
  "Very busy. Lots of meetings.", "I know the feeling. Any plans for the weekend?",
  "Not really. Maybe some rest. You?", "Same here. Have a good day!", "You too. See you later.",
  // LESSON 4 - Vocabulary
  "schedule", "start", "finish", "usually", "morning", "afternoon", "hybrid", "rush hour", "log off",
  // LESSON 4 - Pre-class examples
  "My schedule is very full today.", "I start work at eight thirty.",
  "I usually finish around seven.", "In the morning, I check my emails.",
  "In the afternoon, I have meetings.", "I work in a hybrid model.",
  "Rush hour in São Paulo is terrible.", "I log off at seven p.m.",
  // LESSON 4 - Material examples
  "Maísa's schedule includes client lunches.", "She starts her day early.",
  "Most people finish work around six.", "The morning is for focused tasks.",
  "Afternoon meetings run until five.", "Hybrid work means office and home.",
  "Rush hour starts at five thirty.", "She logs off and sometimes goes back online.",
  // LESSON 5 - Vocabulary
  "currency", "exchange rate", "interest rate", "stock market", "revenue", "profit", "loss", "inflation", "index",
  // LESSON 5 - Pre-class examples
  "The dollar is a strong currency.", "The exchange rate is five to one.",
  "The interest rate went up last month.", "The stock market closed higher today.",
  "Our revenue increased by ten percent.", "The company made a good profit.",
  "We had a small loss in March.", "Inflation is a concern for investors.",
  // LESSON 5 - Material examples
  "Brazil's currency is the real.", "The exchange rate changes every day.",
  "Interest rates affect the whole economy.", "The stock market is very volatile.",
  "Total revenue was two point three million.", "Profit margins improved this quarter.",
  "The loss was smaller than expected.", "Inflation reached four point five percent.",
  // LESSON 5 - Financial figures
  "One point two million dollars.", "Three point five percent.",
  "The market closed at fifty-two thousand points.", "Revenue of two point three million.",
  "Down two percent from last quarter.",
  // LESSON 6 - Vocabulary
  "available", "deadline", "update", "confirm", "feedback", "review", "schedule", "report", "question",
  // LESSON 6 - Pre-class examples
  "Are you available on Thursday?", "The deadline is next Friday.",
  "I have an update for you.", "Can you confirm the meeting?",
  "I need your feedback on this.", "Please review the document.",
  "Can we schedule a call?", "The report is ready.",
  // LESSON 6 - Material examples
  "Is David available for a call tomorrow?", "We need to meet the deadline.",
  "Here is the latest update on the project.", "I'll confirm the time by email.",
  "Your feedback was very helpful.", "I reviewed the proposal yesterday.",
  "Let's schedule the meeting for Monday.", "The quarterly report looks good.",
  // LESSON 6 - Questions
  "Do you have a minute?", "Can I ask you something?",
  "What does that mean exactly?", "How does that work?",
  "Is that right?", "Where do you work?", "When is the deadline?", "Who is responsible for this?",
  // LESSON 7 - Vocabulary
  "reschedule", "attend", "forward", "urgent", "availability", "join", "send", "request", "apologize",
  // LESSON 7 - Pre-class examples
  "Can we reschedule the meeting?", "I can't attend the conference.",
  "Could you forward this email?", "This is an urgent matter.",
  "What is your availability this week?", "I'll join the call at three.",
  "Could you send me the file?", "I'd like to request a meeting.",
  // LESSON 7 - Material examples
  "We need to reschedule for next week.", "Maísa will attend the presentation.",
  "Please forward the document to David.", "There is an urgent deadline today.",
  "My availability is limited this week.", "Can you join the meeting at four?",
  "I'll send the report by end of day.", "She made a request for more information.",
  // LESSON 7 - Polite requests
  "Could you please send that?", "Would you mind checking this?",
  "Is it possible to reschedule?", "I'll be available after three p.m.",
  "I can't make it on Thursday. Would Wednesday work?",
  // LESSON 8 - Vocabulary
  "attended", "closed", "reviewed", "spoke", "met", "sent", "received", "presented", "decided",
  // LESSON 8 - Pre-class examples
  "I attended a meeting yesterday.", "We closed the deal last week.",
  "I reviewed the portfolio on Monday.", "I spoke with David on Friday.",
  "We met the new client.", "I sent the report this morning.",
  "She received the proposal.", "He presented the results.",
  // LESSON 8 - Material examples
  "Maísa attended three meetings last Tuesday.", "The team closed an important deal.",
  "She reviewed the financial data carefully.", "They spoke about the investment strategy.",
  "I met the client for lunch yesterday.", "David sent an email late last night.",
  "We received positive feedback.", "She presented the quarterly numbers.",
  // LESSON 8 - Past narrative
  "First, I checked my emails.", "Then, I had a meeting with the team.",
  "After that, I spoke with two clients.", "On Thursday, I reviewed the portfolio.",
  "By Friday, everything was ready.",
  // LESSON 9 - Vocabulary
  "presentation", "conference call", "quarterly", "annual", "trip", "propose", "prepare", "deadline", "schedule",
  // LESSON 9 - Pre-class examples
  "I'm going to present the results next week.", "We're having a conference call on Thursday.",
  "The quarterly report is due on Monday.", "The annual review is in December.",
  "I'm planning a business trip.", "I propose we meet next Tuesday.",
  "I need to prepare for the presentation.", "The deadline is approaching.",
  // LESSON 9 - Material examples
  "Maísa is going to prepare for the meeting.", "We're meeting the client on Friday morning.",
  "I'll check and get back to you.", "The quarterly numbers look promising.",
  "The annual budget needs revision.", "She's going on a business trip next month.",
  "I'd like to propose a new timeline.", "Are you free on Wednesday afternoon?",
  // LESSON 9 - Future phrases
  "I'm going to work on the report.", "We're meeting David at ten.",
  "I'll let you know by tomorrow.", "Are you going to attend the conference?",
  "I'm preparing the presentation for Monday.",
  // LESSON 10 - Review/linking phrases
  "First of all, let me introduce myself.", "Then, I'd like to talk about my work.",
  "After that, I'll discuss what happened last week.", "Also, I have some plans for next month.",
  "To be honest, I'm still learning.", "I think my English is improving.",
  "Actually, I feel more confident now.", "Sorry, what I mean is...", "Let me rephrase that."
];

async function main() {
  // Ensure output directory exists
  fs.mkdirSync(OUTPUT_DIR, { recursive: true });

  // Deduplicate phrases while preserving order
  const uniquePhrases = [...new Set(ALL_PHRASES)];

  console.log(`Total phrases: ${ALL_PHRASES.length}`);
  console.log(`Unique phrases: ${uniquePhrases.length}`);
  console.log(`Output directory: ${OUTPUT_DIR}\n`);

  const audioMap = {};
  let success = 0;
  let failed = 0;

  for (let i = 0; i < uniquePhrases.length; i++) {
    const text = uniquePhrases[i];
    const filename = safeFilename(text);
    const filePath = path.join(OUTPUT_DIR, filename);
    const relativePath = `audio/maisa-de-oliveira-santos/${filename}`;

    // Skip if file already exists
    if (fs.existsSync(filePath)) {
      console.log(`[${i + 1}/${uniquePhrases.length}] SKIP (exists): ${filename}`);
      audioMap[text] = relativePath;
      success++;
      if (i < uniquePhrases.length - 1) await sleep(DELAY_MS);
      continue;
    }

    try {
      console.log(`[${i + 1}/${uniquePhrases.length}] Generating: "${text}" -> ${filename}`);
      await generateAudio(text, filePath);
      audioMap[text] = relativePath;
      success++;
    } catch (err) {
      console.error(`  FAILED: ${err.message}`);
      failed++;
    }

    if (i < uniquePhrases.length - 1) await sleep(DELAY_MS);
  }

  // Save audioMap.json
  const mapPath = path.join(OUTPUT_DIR, 'audioMap.json');
  fs.writeFileSync(mapPath, JSON.stringify(audioMap, null, 2), 'utf-8');

  console.log(`\n--- DONE ---`);
  console.log(`Success: ${success}`);
  console.log(`Failed: ${failed}`);
  console.log(`Audio map saved to: ${mapPath}`);
}

main().catch(err => {
  console.error('Fatal error:', err);
  process.exit(1);
});
