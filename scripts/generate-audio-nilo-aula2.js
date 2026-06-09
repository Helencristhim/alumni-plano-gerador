#!/usr/bin/env node
const fs = require('fs');
const path = require('path');
const https = require('https');
const API_KEY = process.env.ELEVENLABS_API_KEY;
const SLUG = 'nilo-mesquita-patucci';
const DIR = path.join(__dirname, '..', 'public', 'audio', SLUG);
const ASH = 'VU16byTywsWv5JpI8rbc';
const RILEY = 'hA4zGnmTwX2NQiTRMt7o';
if (!fs.existsSync(DIR)) fs.mkdirSync(DIR, { recursive: true });

const entries = [
  ["Department", "aula2_department.mp3", ASH],
  ["Responsibilities", "aula2_responsibilities.mp3", ASH],
  ["Manage", "aula2_manage.mp3", ASH],
  ["Report to", "aula2_report_to.mp3", ASH],
  ["Coordinate", "aula2_coordinate.mp3", ASH],
  ["Headquarters", "aula2_headquarters.mp3", ASH],
  ["Enforce", "aula2_enforce.mp3", ASH],
  ["Investigate", "aula2_investigate.mp3", ASH],
  ["I manage the compliance department at Corinthians.", "aula2_i_manage_the_compliance_department_at_corinthi.mp3", ASH],
  ["My responsibilities include enforcing FIFA regulations.", "aula2_my_responsibilities_include_enforcing_fifa_re.mp3", ASH],
  ["I report to the General Director of the club.", "aula2_i_report_to_the_general_director_of_the_club.mp3", ASH],
  ["We coordinate with the legal department on investigations.", "aula2_we_coordinate_with_the_legal_department_on_in.mp3", ASH],
  ["Our headquarters is located in Sao Paulo.", "aula2_our_headquarters_is_located_in_sao_paulo.mp3", ASH],
  ["We enforce internal regulations and FIFA standards.", "aula2_we_enforce_internal_regulations_and_fifa_stand.mp3", ASH],
  ["The team investigates potential violations of governance rules.", "aula2_the_team_investigates_potential_violations_of.mp3", RILEY],
  ["We have a team of five people in the department.", "aula2_we_have_a_team_of_five_people_in_the_departme.mp3", ASH],
  ["I manage a team of five people.", "aula2_i_manage_a_team_of_five_people.mp3", ASH],
  ["I report to the General Director.", "aula2_i_report_to_the_general_director.mp3", ASH],
  ["We coordinate with external auditors every quarter.", "aula2_we_coordinate_with_external_auditors_every_qu.mp3", ASH],
  ["Our headquarters is in the Parque Sao Jorge area.", "aula2_our_headquarters_is_in_the_parque_sao_jorge_a.mp3", ASH],
  ["My team investigates compliance violations.", "aula2_my_team_investigates_compliance_violations.mp3", ASH],
  ["So, Nilo, what does a typical day look like for you at Corinthians?", "aula2_dia_so_nilo_what_does_a_typical_day.mp3", RILEY],
  ["Well, I manage the compliance department. We have a team of five people who work directly with me.", "aula2_dia_well_i_manage_the_compliance_department.mp3", ASH],
  ["That sounds like a lot of responsibility. Who do you report to?", "aula2_dia_that_sounds_like_a_lot_of_responsibility.mp3", RILEY],
  ["I report to the General Director. I also coordinate with the legal department on investigations.", "aula2_dia_i_report_to_the_general_director.mp3", ASH],
  ["Interesting! And where is your headquarters?", "aula2_dia_interesting_and_where_is_your_headquarter.mp3", RILEY],
  ["Our headquarters is in the Parque Sao Jorge area of Sao Paulo. But I work from our office in Barra Funda.", "aula2_dia_our_headquarters_is_in_the_parque_sao_jor.mp3", ASH],
  ["What is the hardest part of your job?", "aula2_dia_what_is_the_hardest_part_of_your_job.mp3", RILEY],
  ["Investigating potential violations is challenging. We enforce FIFA regulations at the club level, and sometimes that creates tension.", "aula2_dia_investigating_potential_violations_is_cha.mp3", ASH],
  ["I manage the team.", "aula2_i_manage_the_team.mp3", ASH],
  ["She coordinates with FIFA.", "aula2_she_coordinates_with_fifa.mp3", RILEY],
  ["He reports to the director.", "aula2_he_reports_to_the_director.mp3", ASH],
  ["They investigate violations.", "aula2_they_investigate_violations.mp3", ASH],
  ["Does he manage the department?", "aula2_does_he_manage_the_department.mp3", RILEY],
  ["What does the team do?", "aula2_what_does_the_team_do.mp3", ASH],
  ["The compliance department at Sport Club Corinthians Paulista has five full-time employees. Nilo Patucci manages the team and reports directly to the General Director. The department has three main responsibilities: first, they enforce internal regulations and FIFA standards. Second, they investigate potential violations of governance rules. Third, they coordinate with external auditors and the Brazilian Football Confederation. The headquarters is located in Sao Paulo, and the team works from the Barra Funda office.", "aula2_listening1_department.mp3", ASH],
  ["My name is Dr. Amara Osei, and I manage the governance unit at the Ghana Football Association. My team has eight people. We report to the Executive Committee. Our main responsibilities include enforcing FIFA standards in Ghana, investigating match-fixing allegations, and coordinating with law enforcement agencies. Our headquarters is in Accra, and we also have regional offices in Kumasi and Tamale.", "aula2_listening2_amara.mp3", RILEY],
  ["I manage the compliance department.", "aula2_i_manage_the_compliance_department.mp3", ASH],
  ["My main responsibilities include enforcing regulations.", "aula2_my_main_responsibilities_include_enforcing_re.mp3", ASH],
  ["We enforce FIFA regulations at the club.", "aula2_we_enforce_fifa_regulations_at_the_club.mp3", ASH],
  ["I report to the General Director. I manage the compliance department. We have a team of five full-time employees. We enforce FIFA standards and investigate violations. We also coordinate with the Brazilian Football Confederation.", "aula2_order_l2.mp3", ASH],
  ["I manage the compliance department and I report to the General Director.", "aula2_speech_i_manage_the_compliance.mp3", ASH],
  ["My responsibilities include enforcing FIFA standards and investigating violations.", "aula2_speech_my_responsibilities.mp3", ASH],
  ["We coordinate with the legal department and external auditors.", "aula2_speech_we_coordinate.mp3", ASH],
];

function gen(text, filename, voiceId) {
  return new Promise((resolve, reject) => {
    const fp = path.join(DIR, filename);
    if (fs.existsSync(fp) && fs.statSync(fp).size > 1000) { console.log('  SKIP:', filename); return resolve(); }
    const body = JSON.stringify({ text, model_id: 'eleven_turbo_v2_5', voice_settings: { stability: 0.5, similarity_boost: 0.75 } });
    const opts = { hostname: 'api.elevenlabs.io', path: `/v1/text-to-speech/${voiceId}`, method: 'POST', headers: { 'xi-api-key': API_KEY, 'Content-Type': 'application/json', 'Accept': 'audio/mpeg', 'Content-Length': Buffer.byteLength(body) } };
    const req = https.request(opts, res => {
      if (res.statusCode !== 200) { let e=''; res.on('data',d=>e+=d); res.on('end',()=>{ console.error('  ERR',res.statusCode,filename,e.substring(0,100)); reject(new Error('HTTP '+res.statusCode)); }); return; }
      const chunks = []; res.on('data', c => chunks.push(c)); res.on('end', () => { const buf = Buffer.concat(chunks); fs.writeFileSync(fp, buf); console.log('  OK:', filename, buf.length, 'bytes'); resolve(); });
    });
    req.on('error', reject); req.write(body); req.end();
  });
}

async function main() {
  console.log(`Generating ${entries.length} audio files...`);
  let ok=0, err=0;
  for (let i=0; i<entries.length; i++) {
    try { await gen(entries[i][0], entries[i][1], entries[i][2]); ok++; if(i<entries.length-1) await new Promise(r=>setTimeout(r,150)); }
    catch(e) { err++; }
  }
  console.log(`Done: ${ok} OK, ${err} errors`);
}
main().catch(console.error);
