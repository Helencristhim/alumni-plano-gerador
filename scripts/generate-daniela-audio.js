#!/usr/bin/env node
/**
 * Generate ElevenLabs audio files for Daniela Feitoza - Lessons 1-5
 * Usage: ELEVENLABS_API_KEY=... node generate-daniela-audio.js
 */

const fs = require('fs');
const path = require('path');

const API_URL = 'https://api.elevenlabs.io/v1/text-to-speech';
const VOICE_ID = 'pNInz6obpgDQGcFmaJgB'; // Arthur
const API_KEY = process.env.ELEVENLABS_API_KEY;
const OUTPUT_DIR = path.join(__dirname, '..', 'public', 'audio', 'daniela-feitoza');

if (!API_KEY) {
  console.error('Set ELEVENLABS_API_KEY');
  process.exit(1);
}

if (!fs.existsSync(OUTPUT_DIR)) {
  fs.mkdirSync(OUTPUT_DIR, { recursive: true });
}

// All phrases needed for Lessons 1-5
const phrases = [
  // === LESSON 1: Who is Daniela? Diagnostic + Personal Introduction ===
  // Pre-class vocabulary words
  "introduction",
  "I work as an IT Manager.",
  "manager",
  "I am the manager of the SAP team.",
  "corporate",
  "We handle corporate systems for the entire group.",
  "responsible for",
  "I am responsible for system integrations.",
  "team",
  "My team manages all SAP modules.",
  "interests",
  "My interests include technology and travel.",
  // Pre-class example sentences
  "Hi, my name is Daniela and I work at Centauro.",
  "I live in São Paulo, near the Berrini area.",
  "I manage corporate systems with a focus on SAP.",
  "Nice to meet you. I am from Brazil.",
  // Lesson 1 - Material do Professor (different sentences)
  "Let me introduce myself.",
  "I have been working in IT for many years.",
  "My company is the official Nike distributor in Brazil.",
  "I am based in São Paulo.",
  "I work from home most of the week.",
  "We operate Centauro stores across Brazil.",
  // Lesson 1 - Dialogue
  "Hi there! What is your name?",
  "My name is Daniela. Nice to meet you.",
  "Nice to meet you too, Daniela. What do you do?",
  "I work as an IT Manager at a retail company in Brazil.",
  "That sounds interesting! Tell me more about your company.",
  "We are the official Nike distributor in Brazil. We operate Centauro stores.",
  // Lesson 1 - Pronunciation practice
  "Hi, I am Daniela Feitoza. I work as an IT Manager at Centauro.",
  "My company is the official Nike distributor in Brazil.",

  // === LESSON 2: Breaking the Ice — First Contact at International Events ===
  // Pre-class vocabulary
  "conference",
  "Are you attending the conference this week?",
  "networking",
  "Networking is the best part of events like this.",
  "attendee",
  "There are hundreds of attendees at this event.",
  "small talk",
  "Small talk helps you connect with new people.",
  "What brings you here?",
  "What brings you here today?",
  "approach",
  "I want to learn how to approach people at events.",
  // Pre-class sentences
  "Hi! Is this your first time at this conference?",
  "What brings you to this event?",
  "I am here for the SAP technology sessions.",
  "Have you been to any interesting sessions so far?",
  // Lesson 2 - Material do Professor (different sentences)
  "This is a great event, isn't it?",
  "I don't think we've met. I'm Daniela.",
  "Are you enjoying the conference so far?",
  "Which company are you with?",
  "I flew in from São Paulo for this event.",
  "Would you like to grab a coffee during the break?",
  // Lesson 2 - Dialogue
  "Excuse me, is this seat taken?",
  "No, go ahead! Are you here for the tech sessions?",
  "Yes, I am. I work with SAP systems. What about you?",
  "I am in retail technology too. What a coincidence!",
  "That is great! What brings you to this conference?",
  "I am looking for new integration solutions. And you?",
  "Same here. We are always looking for better tools.",
  "We should exchange contacts. Here is my card.",
  // Lesson 2 - Pronunciation
  "Hi, is this your first time at this conference?",
  "What brings you to this event?",

  // === LESSON 3: Talking About Your Job — IT Manager at Centauro/Nike ===
  // Pre-class vocabulary
  "distributor",
  "We are the official distributor of Nike in Brazil.",
  "retail",
  "Centauro is one of the largest retail chains in Brazil.",
  "e-commerce",
  "We also run the entire Nike e-commerce operation.",
  "headquartered",
  "The company is headquartered in São Paulo.",
  "oversee",
  "I oversee all corporate systems.",
  "implementation",
  "I led the SAP implementation last year.",
  // Pre-class sentences
  "I work for the SPF Group, which operates Centauro.",
  "My team is responsible for all SAP modules.",
  "We manage both physical stores and e-commerce.",
  "I have been in this role for several years.",
  // Lesson 3 - Material do Professor
  "Could you tell me about your role?",
  "I lead the corporate systems team.",
  "Our company operates over 200 stores nationwide.",
  "I am responsible for system integrations across the group.",
  "We handle everything from inventory to point of sale.",
  "My day-to-day involves managing SAP and coordinating with stakeholders.",
  // Lesson 3 - Dialogue
  "So, what exactly do you do at Centauro?",
  "I am the IT Manager. I oversee all corporate systems.",
  "That is a big responsibility. How large is your team?",
  "We have about fifteen people working on different SAP modules.",
  "And you manage the Nike operation as well?",
  "Yes, we are the official Nike distributor. We run their stores and e-commerce.",
  // Lesson 3 - Pronunciation
  "I work as an IT Manager at the SPF Group, which operates Centauro and Nike in Brazil.",
  "My team manages all corporate systems, including SAP modules and e-commerce platforms.",

  // === LESSON 4: Articles and the basics of English rhythm ===
  // Pre-class vocabulary
  "article",
  "An article is a small word like a, an, or the.",
  "rhythm",
  "English rhythm is different from Portuguese.",
  "stress",
  "Word stress changes the meaning of some words.",
  "syllable",
  "The word technology has four syllables.",
  "pronunciation",
  "Good pronunciation helps people understand you.",
  "content word",
  "Content words carry the main meaning of a sentence.",
  // Pre-class sentences
  "I work for a company called Centauro.",
  "It is the biggest sports retailer in Brazil.",
  "I manage a team of fifteen people.",
  "The company has an office near Berrini.",
  // Lesson 4 - Material do Professor
  "She works at a large company in São Paulo.",
  "The system was implemented by our team.",
  "I have a meeting with the director tomorrow.",
  "We need an update on the project status.",
  "Technology is changing the retail industry.",
  "I am responsible for the corporate systems.",
  // Lesson 4 - Pronunciation focus words
  "technology",
  "responsible",
  "corporate",
  "distributor",
  "professional",
  "integration",

  // === LESSON 5: Describing Your Company — Centauro, Nike Brazil & SPF Group ===
  // Pre-class vocabulary
  "operates",
  "Centauro operates more than 200 stores in Brazil.",
  "partners with",
  "Our company partners with Nike for distribution.",
  "founded",
  "The SPF Group was founded in São Paulo.",
  "the largest",
  "Centauro is the largest sports retailer in Brazil.",
  "supply chain",
  "We manage the entire supply chain for Nike products.",
  "brick-and-mortar",
  "We have both brick-and-mortar stores and an online platform.",
  // Pre-class sentences
  "The SPF Group is the official Nike distributor in Brazil.",
  "We operate Centauro stores and the Nike e-commerce platform.",
  "Our headquarters are located in São Paulo.",
  "The company is one of the most important in the sports retail segment.",
  // Lesson 5 - Material do Professor
  "Let me tell you about my company.",
  "We distribute Nike products across the entire country.",
  "Centauro is present in all major Brazilian cities.",
  "Our e-commerce platform serves millions of customers.",
  "The group has grown significantly in recent years.",
  "We are always looking for new technology partners.",
  // Lesson 5 - Dialogue
  "I would love to hear about your company. Can you tell me more?",
  "Of course! I work for the SPF Group. We are the official Nike distributor in Brazil.",
  "That is impressive! How many stores do you have?",
  "We operate over 200 Centauro stores, plus the entire Nike e-commerce.",
  "What is your role in all of this?",
  "I manage the corporate systems. Everything from SAP to our online platforms.",
  // Lesson 5 - Pronunciation
  "The SPF Group operates Centauro, the largest sports retailer in Brazil, and is the official Nike distributor.",
  "We manage over 200 brick-and-mortar stores and a complete e-commerce platform.",

  // === SURVIVAL CARD phrases (progressive) ===
  "Excuse me, could you repeat that, please?",
  "Sorry, I did not catch that.",
  "Could you speak more slowly, please?",
  "What does that mean?",
  "How do you say this in English?",
  "Just a moment, please.",
  "Nice to meet you.",
  "Thank you so much.",
  "Could I ask you a question?",
  "Let me think about that for a moment."
];

async function generateAudio(text, filename) {
  const filePath = path.join(OUTPUT_DIR, filename);

  // Skip if already exists
  if (fs.existsSync(filePath)) {
    console.log(`  [skip] ${filename} already exists`);
    return filePath;
  }

  const response = await fetch(`${API_URL}/${VOICE_ID}`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'xi-api-key': API_KEY,
      'Accept': 'audio/mpeg'
    },
    body: JSON.stringify({
      text: text,
      model_id: 'eleven_monolingual_v1',
      voice_settings: {
        stability: 0.5,
        similarity_boost: 0.75
      }
    })
  });

  if (!response.ok) {
    const err = await response.text();
    console.error(`  [ERROR] ${filename}: ${response.status} ${err}`);
    return null;
  }

  const buffer = Buffer.from(await response.arrayBuffer());
  fs.writeFileSync(filePath, buffer);
  console.log(`  [ok] ${filename} (${buffer.length} bytes)`);
  return filePath;
}

function textToFilename(text) {
  return text
    .toLowerCase()
    .replace(/[^a-z0-9\s]/g, '')
    .replace(/\s+/g, '_')
    .substring(0, 60)
    + '.mp3';
}

async function main() {
  console.log(`Generating ${phrases.length} audio files for Daniela Feitoza...`);
  console.log(`Output: ${OUTPUT_DIR}\n`);

  const audioMap = {};
  let success = 0;
  let failed = 0;

  for (let i = 0; i < phrases.length; i++) {
    const text = phrases[i];
    const filename = textToFilename(text);

    console.log(`[${i + 1}/${phrases.length}] "${text.substring(0, 50)}..."`);

    const result = await generateAudio(text, filename);
    if (result) {
      audioMap[text] = `/audio/daniela-feitoza/${filename}`;
      success++;
    } else {
      failed++;
    }

    // Rate limiting: 120ms between requests
    if (i < phrases.length - 1) {
      await new Promise(r => setTimeout(r, 120));
    }
  }

  // Save audioMap
  const mapPath = path.join(OUTPUT_DIR, 'audioMap.json');
  fs.writeFileSync(mapPath, JSON.stringify(audioMap, null, 2));

  console.log(`\nDone! ${success} generated, ${failed} failed.`);
  console.log(`Audio map: ${mapPath}`);
}

main().catch(console.error);
