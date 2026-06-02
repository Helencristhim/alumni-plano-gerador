const fs = require("fs");
const path = require("path");
const https = require("https");
const ELEVENLABS_API_KEY = process.env.ELEVENLABS_API_KEY;
if (!ELEVENLABS_API_KEY) { console.error("ERROR: ELEVENLABS_API_KEY not set"); process.exit(1); }
const ARTHUR = "sfJopaWaOtauCD3HKX6Q";
const ELLEN = "BIvP0GN1cAtSRTxNHnWS";
const OUTPUT_DIR = path.join(__dirname, "public", "audio", "eduarda-gabriel");
const audioMap = {
  "Close a Deal": "aula4_close_a_deal.mp3",
  "File for Bankruptcy": "aula4_file_for_bankruptcy.mp3",
  "Reach an Agreement": "aula4_reach_an_agreement.mp3",
  "Conduct Due Diligence": "aula4_conduct_due_diligence.mp3",
  "Submit a Proposal": "aula4_submit_a_proposal.mp3",
  "Negotiate Terms": "aula4_negotiate_terms.mp3",
  "Raise Capital": "aula4_raise_capital.mp3",
  "Issue a Report": "aula4_issue_a_report.mp3",
  "We closed the deal with the creditors last Friday.": "aula4_ex_close_a_deal.mp3",
  "The company has filed for bankruptcy under Chapter 11.": "aula4_ex_file_for_bankruptcy.mp3",
  "The parties have reached an agreement on the payment terms.": "aula4_ex_reach_an_agreement.mp3",
  "We have conducted due diligence on the target company.": "aula4_ex_conduct_due_diligence.mp3",
  "The advisory team has submitted a proposal to the board.": "aula4_ex_submit_a_proposal.mp3",
  "Eduarda has negotiated the terms with the US counterparts.": "aula4_ex_negotiate_terms.mp3",
  "The company needs to raise capital to fund the restructuring.": "aula4_ex_raise_capital.mp3",
  "We have issued the preliminary report to all stakeholders.": "aula4_ex_issue_a_report.mp3",
  "We have reached an agreement with the creditors.": "aula4_fill1.mp3",
  "The company filed for bankruptcy last month.": "aula4_fill2.mp3",
  "Eduarda has negotiated the terms for three weeks.": "aula4_fill3.mp3",
  "Have you conducted due diligence yet?": "aula4_fill4.mp3",
  "The team has already submitted the proposal.": "aula4_fill5.mp3",
  "They have not raised enough capital yet.": "aula4_fill6.mp3",
  "We have conducted due diligence on the target company.": "aula4_pron1.mp3",
  "The parties have reached an agreement on the restructuring terms.": "aula4_pron2.mp3",
  "Have you submitted the proposal to the board yet?": "aula4_pron3.mp3",
  "Eduarda, what is the status of the Brazilian restructuring case?": "aula4_dial1.mp3",
  "We have made good progress. The company has filed for Chapter 11.": "aula4_dial2.mp3",
  "Have you conducted due diligence yet?": "aula4_dial3.mp3",
  "Yes, we have already conducted due diligence. The report is ready.": "aula4_dial4.mp3",
  "And the creditor negotiations?": "aula4_dial5.mp3",
  "We have negotiated the main terms, but we have not reached a final agreement yet.": "aula4_dial6.mp3",
  "When do you expect to close the deal?": "aula4_dial7.mp3",
  "We have submitted a proposal. If they accept, we could close the deal by the end of the quarter.": "aula4_dial8.mp3",
  "We have closed the deal with the creditors.": "aula4_surv1.mp3",
  "The company has filed for bankruptcy under Chapter 11.": "aula4_surv2.mp3",
  "Have you conducted due diligence yet?": "aula4_surv3.mp3",
  "We have not reached an agreement yet.": "aula4_surv4.mp3",
  "The team has already submitted the proposal.": "aula4_surv5.mp3",
  "[order-l4]": "aula4_order_l4.mp3",
  "We have closed a restructuring deal with Brazilian creditors.": "aula4_oral1.mp3",
  "Yes, the company has filed for Chapter 11 bankruptcy protection.": "aula4_oral2.mp3",
  "We have conducted financial and legal due diligence on the target company.": "aula4_oral3.mp3",
  "Not yet. We have negotiated the main terms but have not reached a final agreement.": "aula4_oral4.mp3",
  "We have submitted a revised proposal with three restructuring scenarios.": "aula4_oral5.mp3",
  "The company needs to raise approximately fifty million dollars. We have already issued a report to potential investors.": "aula4_oral6.mp3"
};
const jamesLines = ["Eduarda, what is the status of the Brazilian restructuring case?","Have you conducted due diligence yet?","And the creditor negotiations?","When do you expect to close the deal?"];
const eduardaLines = ["We have made good progress. The company has filed for Chapter 11.","Yes, we have already conducted due diligence. The report is ready.","We have negotiated the main terms, but we have not reached a final agreement yet.","We have submitted a proposal. If they accept, we could close the deal by the end of the quarter."];
function countWords(t){return t.trim().split(/\s+/).length;}
let alt=0;
function getVoice(text){if(jamesLines.includes(text))return{id:ARTHUR,name:"Arthur"};if(eduardaLines.includes(text))return{id:ELLEN,name:"Ellen"};if(countWords(text)<=2)return{id:ARTHUR,name:"Arthur"};const v=alt%2===0?{id:ARTHUR,name:"Arthur"}:{id:ELLEN,name:"Ellen"};alt++;return v;}
function generateAudio(text,voiceId,outputPath){return new Promise((resolve,reject)=>{const postData=JSON.stringify({text:text,model_id:"eleven_monolingual_v1",voice_settings:{stability:0.5,similarity_boost:0.75}});const options={hostname:"api.elevenlabs.io",path:"/v1/text-to-speech/"+voiceId+"?output_format=mp3_44100_128",method:"POST",headers:{"Content-Type":"application/json","xi-api-key":ELEVENLABS_API_KEY,"Content-Length":Buffer.byteLength(postData)}};const req=https.request(options,(res)=>{if(res.statusCode!==200){let b="";res.on("data",d=>b+=d);res.on("end",()=>reject(new Error("API "+res.statusCode+": "+b)));return;}const chunks=[];res.on("data",c=>chunks.push(c));res.on("end",()=>{fs.writeFileSync(outputPath,Buffer.concat(chunks));resolve();});});req.on("error",reject);req.write(postData);req.end();});}
async function main(){const entries=Object.entries(audioMap);let gen=0,skip=0;console.log("Generating "+entries.length+" Aula 4 audio files...");for(let i=0;i<entries.length;i++){const[text,file]=entries[i];const out=path.join(OUTPUT_DIR,file);if(fs.existsSync(out)&&fs.statSync(out).size>1000){skip++;if(countWords(text)>2&&!jamesLines.includes(text)&&!eduardaLines.includes(text))alt++;continue;}const voice=getVoice(text);try{await generateAudio(text,voice.id,out);gen++;console.log("Generated "+(gen+skip)+"/"+entries.length+": "+file+" ("+voice.name+")");}catch(err){console.error("FAILED "+file+": "+err.message);}if(i<entries.length-1)await new Promise(r=>setTimeout(r,500));}console.log("Done! Generated: "+gen+", Skipped: "+skip);}
main().catch(console.error);
