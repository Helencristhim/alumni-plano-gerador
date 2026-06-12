const https = require('https');
const fs = require('fs');
const path = require('path');

const ASH = 'VU16byTywsWv5JpI8rbc';
const RILEY = 'hA4zGnmTwX2NQiTRMt7o';
const API_KEY = process.env.ELEVENLABS_API_KEY;
const OUTPUT_DIR = path.join(__dirname, 'public', 'audio', 'natalie-viegas');

const entries = [
  // ===== VOCAB WORDS (Riley - Natalie is female) =====
  { file: 'aula6_draft.mp3', text: 'Draft', voice: RILEY },
  { file: 'aula6_revise.mp3', text: 'Revise', voice: RILEY },
  { file: 'aula6_outline.mp3', text: 'Outline', voice: RILEY },
  { file: 'aula6_executive_summary.mp3', text: 'Executive summary', voice: RILEY },
  { file: 'aula6_findings.mp3', text: 'Findings', voice: RILEY },
  { file: 'aula6_recommendation.mp3', text: 'Recommendation', voice: RILEY },
  { file: 'aula6_benchmark.mp3', text: 'Benchmark', voice: RILEY },
  { file: 'aula6_comply.mp3', text: 'Comply', voice: RILEY },
  { file: 'aula6_implement.mp3', text: 'Implement', voice: RILEY },
  { file: 'aula6_concise.mp3', text: 'Concise', voice: RILEY },

  // ===== FILL-IN-THE-BLANK SENTENCES (alternate Riley/Ash) =====
  { file: 'aula6_fill_report_was_drafted.mp3', text: 'The report was drafted by the finance team.', voice: ASH },
  { file: 'aula6_fill_findings_were_presented.mp3', text: 'The findings were presented to the board of directors.', voice: RILEY },
  { file: 'aula6_fill_recommendations_have_been_made.mp3', text: 'Three recommendations have been made based on the data.', voice: ASH },
  { file: 'aula6_fill_executive_summary_reviewed.mp3', text: 'The executive summary was reviewed by the VP.', voice: RILEY },
  { file: 'aula6_fill_changes_will_be_implemented.mp3', text: 'The changes will be implemented next quarter.', voice: ASH },
  { file: 'aula6_fill_reports_are_submitted.mp3', text: 'All reports are submitted before the end of the quarter.', voice: RILEY },

  // ===== SPEECH CARDS (Riley - student voice) =====
  { file: 'aula6_speech_report_drafted_revised.mp3', text: 'The report was drafted by the team and revised by the manager.', voice: RILEY },
  { file: 'aula6_speech_findings_presented.mp3', text: 'The findings were presented to the board and three recommendations were made.', voice: RILEY },
  { file: 'aula6_speech_executive_summary_reviewed.mp3', text: 'The executive summary has been reviewed and the changes will be implemented next quarter.', voice: RILEY },

  // ===== ORDERING =====
  { file: 'aula6_order_l6_ordering.mp3', text: 'Create an outline. Research and gather findings. Draft the report. Revise and submit the executive summary. Implement recommendations.', voice: RILEY },

  // ===== SURVIVAL CARD (Pre-class) =====
  { file: 'aula6_surv_report_drafted.mp3', text: 'The report was drafted and submitted on time.', voice: RILEY },
  { file: 'aula6_surv_findings_presented.mp3', text: 'The findings were presented to the leadership team.', voice: ASH },
  { file: 'aula6_surv_executive_summary_concise.mp3', text: 'The executive summary should be concise and well-structured.', voice: RILEY },

  // ===== IN CLASS ORAL DRILLING =====
  { file: 'aula6_oral_report_drafted.mp3', text: 'The report was drafted by the team.', voice: RILEY },
  { file: 'aula6_oral_findings_presented.mp3', text: 'The findings were presented to the board.', voice: ASH },
  { file: 'aula6_oral_two_recommendations.mp3', text: 'Two recommendations have been made.', voice: RILEY },
  { file: 'aula6_oral_executive_summary_concise.mp3', text: 'The executive summary should be concise.', voice: ASH },
  { file: 'aula6_oral_changes_implemented.mp3', text: 'The changes were implemented immediately.', voice: RILEY },
  { file: 'aula6_oral_comply_benchmarks.mp3', text: 'All reports must comply with benchmarks.', voice: ASH },

  // ===== IN CLASS DIALOGUE (VP Rodriguez=Ash, Natalie=Riley) =====
  { file: 'aula6_dlg_vp_walk_me_through.mp3', text: 'Natalie, I have read your Q3 report. Can you walk me through the key findings?', voice: ASH },
  { file: 'aula6_dlg_natalie_three_modules.mp3', text: 'Of course. Three modules were delivered on schedule, and the approval process was streamlined by thirty percent.', voice: RILEY },
  { file: 'aula6_dlg_vp_what_recommendations.mp3', text: 'That is great progress. What recommendations were made?', voice: ASH },
  { file: 'aula6_dlg_natalie_two_recommendations.mp3', text: 'Two recommendations were included. First, additional resources should be allocated to compliance. Second, the system should be benchmarked against international standards.', voice: RILEY },
  { file: 'aula6_dlg_vp_revised_by_legal.mp3', text: 'Good. Has the report been revised by legal?', voice: ASH },
  { file: 'aula6_dlg_natalie_revised_approved.mp3', text: 'Yes, it has been revised and approved. The final version was submitted yesterday. It complies with all global standards.', voice: RILEY },
  { file: 'aula6_dlg_vp_when_implemented.mp3', text: 'Excellent. When will the changes be implemented?', voice: ASH },
  { file: 'aula6_dlg_natalie_changes_q4.mp3', text: 'The changes will be implemented in Q4. A follow-up report will be submitted by December fifteenth. The executive summary is concise and ready for distribution.', voice: RILEY },

  // ===== IN CLASS ERROR SENTENCES =====
  { file: 'aula6_ic_error_draft.mp3', text: 'The report was draft by the team last week.', voice: RILEY },
  { file: 'aula6_ic_error_findings_was.mp3', text: 'The findings was presented to the board.', voice: RILEY },
  { file: 'aula6_ic_error_have_implemented.mp3', text: 'The recommendations have implemented already.', voice: RILEY },
  { file: 'aula6_ic_error_will_be_implement.mp3', text: 'The changes will be implement next month.', voice: RILEY },
  { file: 'aula6_ic_error_draft_v2.mp3', text: 'The report was draft by the team.', voice: RILEY },
  { file: 'aula6_ic_error_have_implement.mp3', text: 'The recommendations have implement already.', voice: RILEY },

  // ===== IN CLASS LISTENING PASSAGES =====
  { file: 'aula6_listening_1_quarterly_report.mp3', text: 'Good morning, everyone. I am here to present the Q3 performance report for the customer engagement project. The report was prepared by my team over the past two weeks. Our findings show that ten out of twelve deliverables were completed on schedule. The customer satisfaction score was measured at ninety-two percent, which exceeds our benchmark of eighty-five percent. Two deliverables were delayed due to resource constraints, but they have been rescheduled for early Q4. Based on our findings, three recommendations were made. First, additional training should be provided to the support team. Second, the reporting process should be streamlined. Third, benchmarks should be revised to reflect the new service standards. The executive summary has been distributed to all stakeholders. A follow-up report will be submitted in January.', voice: RILEY },
  { file: 'aula6_listening_2_report_update.mp3', text: 'Hi team, quick update on the annual report. The draft was completed by the deadline, so we are on track. The financial section was reviewed by accounting and most of the data has been verified. However, the revenue projections still need to be revised. They were based on last year\'s benchmarks and those numbers are outdated. I have spoken with the finance director and it was recommended that we update the benchmarks before final submission. The executive summary has been written but it needs to be more concise. The legal section was approved yesterday, so that is done. The full report will be submitted to the board by Friday. Any questions?', voice: ASH },
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
      headers: { 'Content-Type': 'application/json', 'xi-api-key': API_KEY, 'Content-Length': Buffer.byteLength(data) }
    };
    const outPath = path.join(OUTPUT_DIR, entry.file);
    if (fs.existsSync(outPath)) { console.log(`SKIP (exists): ${entry.file}`); return resolve(); }
    const req = https.request(options, (res) => {
      if (res.statusCode !== 200) { let body=''; res.on('data',d=>body+=d); res.on('end',()=>{console.error(`ERROR ${res.statusCode} for ${entry.file}: ${body}`);resolve();}); return; }
      const ws = fs.createWriteStream(outPath); res.pipe(ws);
      ws.on('finish', () => { console.log(`OK: ${entry.file}`); resolve(); });
      ws.on('error', reject);
    });
    req.on('error', reject); req.write(data); req.end();
  });
}

async function main() {
  if (!API_KEY) { console.error('ERROR: ELEVENLABS_API_KEY not set.'); process.exit(1); }
  if (!fs.existsSync(OUTPUT_DIR)) fs.mkdirSync(OUTPUT_DIR, { recursive: true });
  console.log(`Generating ${entries.length} audio files for Natalie Viegas (Aula 6)...\n`);
  for (let i = 0; i < entries.length; i++) {
    console.log(`[${i+1}/${entries.length}] ${entries[i].file}`);
    await generateAudio(entries[i]);
    await new Promise(r => setTimeout(r, 200));
  }
  console.log('\nDone!');
}
main().catch(console.error);
