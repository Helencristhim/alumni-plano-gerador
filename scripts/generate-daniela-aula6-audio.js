#!/usr/bin/env node
/**
 * Generate ElevenLabs audio files for Daniela Feitoza - Aula 6 (SAP World)
 * Voices: Riley (female, neutral) for protagonist phrases, Ash (male) for alternation
 */

const fs = require('fs');
const path = require('path');
const https = require('https');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const OUTPUT_DIR = path.join(__dirname, '..', 'public', 'audio', 'daniela-feitoza');

// Voice IDs (updated Jun/2026)
const RILEY = 'hA4zGnmTwX2NQiTRMt7o';  // Female neutral
const ASH = 'VU16byTywsWv5JpI8rbc';     // Male neutral

if (!API_KEY) {
  console.error('Set ELEVENLABS_API_KEY env var');
  process.exit(1);
}

if (!fs.existsSync(OUTPUT_DIR)) {
  fs.mkdirSync(OUTPUT_DIR, { recursive: true });
}

// Aula 6 phrases with voice assignment
// Daniela = female, so protagonist phrases use Riley
// General/process phrases alternate Riley/Ash
const phrases = [
  // Vocab card sentences (protagonist = Riley, alternating Ash)
  { text: "We implement SAP modules across all departments.", file: "we_implement_sap_modules_across_all_departments.mp3", voice: RILEY },
  { text: "The finance module tracks all transactions automatically.", file: "the_finance_module_tracks_all_transactions_automatically.mp3", voice: ASH },
  { text: "Our workflow includes three approval steps before any purchase.", file: "our_workflow_includes_three_approval_steps.mp3", voice: RILEY },
  { text: "All customer information is stored in our database.", file: "all_customer_information_is_stored_in_our_database.mp3", voice: ASH },
  { text: "We need to integrate SAP with our existing tools.", file: "we_need_to_integrate_sap_with_our_existing_tools.mp3", voice: RILEY },
  { text: "We customize every SAP module to fit our business needs.", file: "we_customize_every_sap_module_to_fit_our_business_needs.mp3", voice: ASH },
  { text: "We plan to deploy the new system next quarter.", file: "we_plan_to_deploy_the_new_system_next_quarter.mp3", voice: RILEY },
  { text: "We are upgrading our SAP version this year.", file: "we_are_upgrading_our_sap_version_this_year.mp3", voice: ASH },

  // Survival card phrases (protagonist = Riley)
  { text: "We use SAP for all our operations.", file: "we_use_sap_for_all_our_operations.mp3", voice: RILEY },
  { text: "This module handles inventory management.", file: "this_module_handles_inventory_management.mp3", voice: RILEY },
  { text: "The system integrates with our database.", file: "the_system_integrates_with_our_database.mp3", voice: RILEY },
  { text: "We are implementing a new workflow.", file: "we_are_implementing_a_new_workflow.mp3", voice: RILEY },
  { text: "Could you walk me through the process?", file: "could_you_walk_me_through_the_process.mp3", voice: RILEY },

  // Ordering exercise - full sequence narration
  { text: "A store employee creates a purchase request in SAP. SAP checks the inventory levels in the database. The manager approves the purchase order in the system. The supplier receives the order and ships the products. The finance module updates the payment records.", file: "order_l6_ordering.mp3", voice: RILEY },
];

function generateAudio(text, voiceId, outputPath) {
  return new Promise((resolve, reject) => {
    const data = JSON.stringify({
      text: text,
      model_id: 'eleven_multilingual_v2',
      voice_settings: {
        stability: 0.5,
        similarity_boost: 0.75,
        style: 0,
        use_speaker_boost: true
      }
    });

    const options = {
      hostname: 'api.elevenlabs.io',
      port: 443,
      path: `/v1/text-to-speech/${voiceId}`,
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'xi-api-key': API_KEY,
        'Accept': 'audio/mpeg',
        'Content-Length': Buffer.byteLength(data)
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
        const buffer = Buffer.concat(chunks);
        fs.writeFileSync(outputPath, buffer);
        resolve(buffer.length);
      });
    });

    req.on('error', reject);
    req.write(data);
    req.end();
  });
}

async function main() {
  console.log(`Generating ${phrases.length} audio files for Daniela Aula 6...\n`);

  let generated = 0;
  let skipped = 0;

  for (const p of phrases) {
    const outputPath = path.join(OUTPUT_DIR, p.file);

    if (fs.existsSync(outputPath)) {
      console.log(`  SKIP (exists): ${p.file}`);
      skipped++;
      continue;
    }

    try {
      const size = await generateAudio(p.text, p.voice, outputPath);
      console.log(`  OK: ${p.file} (${(size / 1024).toFixed(1)} KB)`);
      generated++;
      // Rate limit: wait 500ms between requests
      await new Promise(r => setTimeout(r, 500));
    } catch (err) {
      console.error(`  FAIL: ${p.file} - ${err.message}`);
    }
  }

  console.log(`\nDone! Generated: ${generated}, Skipped: ${skipped}, Total: ${phrases.length}`);
}

main();
