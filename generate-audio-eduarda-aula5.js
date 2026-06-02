const fs=require("fs"),path=require("path"),https=require("https");
const ELEVENLABS_API_KEY=process.env.ELEVENLABS_API_KEY;if(!ELEVENLABS_API_KEY){console.error("ERROR");process.exit(1);}
const ARTHUR="sfJopaWaOtauCD3HKX6Q",ELLEN="BIvP0GN1cAtSRTxNHnWS",OUTPUT_DIR=path.join(__dirname,"public","audio","eduarda-gabriel");
const audioMap={
"The restructuring process has been complex.": "aula5_review1.mp3",
"My counterpart in New York has already reviewed the proposal.": "aula5_review2.mp3",
"If I may, I would like to contribute to this discussion.": "aula5_review3.mp3",
"Have we reached a consensus on the timeline?": "aula5_review4.mp3",
"Revenue declined by eight percent compared to last quarter.": "aula5_review5.mp3",
"The forecast shows improvement, but we have not closed the deal yet.": "aula5_review6.mp3",
"We have conducted due diligence on the target.": "aula5_review7.mp3",
"Eduarda is currently negotiating the terms with creditors.": "aula5_review8.mp3",
"We have conducted due diligence, and revenue declined by eight percent compared to last quarter.": "aula5_pron1.mp3",
"If I may, I would like to walk you through the forecast — we estimate a recovery in Q4.": "aula5_pron2.mp3",
"Have you reached a consensus on the proposal, or should we follow up with the stakeholders?": "aula5_pron3.mp3",
"Good morning, everyone. Let us start with introductions. Eduarda, please go ahead.": "aula5_dial1.mp3",
"Good morning. I am Eduarda Gabriel, an associate on the restructuring team at Houlihan Lokey, based in Sao Paulo.": "aula5_dial2.mp3",
"Eduarda has been leading the financial analysis on this case. Eduarda, could you walk us through the latest numbers?": "aula5_dial3.mp3",
"Of course. Revenue in Q3 declined by eight percent compared to Q2. However, the operating margin has improved from fifteen to twenty percent.": "aula5_dial4.mp3",
"What about the restructuring timeline?": "aula5_dial5.mp3",
"We have conducted due diligence and have submitted a proposal to the creditors. We are currently negotiating the final terms.": "aula5_dial6.mp3",
"Have we reached a consensus internally?": "aula5_dial7.mp3",
"Not yet. If I may, I would like to elaborate on two key points. First, the leverage ratio is still higher than the benchmark.": "aula5_dial8.mp3",
"Good point. What do you estimate for Q4?": "aula5_dial9.mp3",
"The forecast shows revenue growing by approximately five percent. If the creditors accept our proposal, we could close the deal by the end of the quarter.": "aula5_dial10.mp3",
"I am Eduarda Gabriel, an associate at Houlihan Lokey.": "aula5_surv1.mp3",
"Could you walk me through the deal structure?": "aula5_surv2.mp3",
"If I may, I would like to share my perspective.": "aula5_surv3.mp3",
"Revenue declined by eight percent compared to Q2.": "aula5_surv4.mp3",
"We have conducted due diligence and submitted the proposal.": "aula5_surv5.mp3",
"[order-l5]": "aula5_order_l5.mp3",
"I am an associate on the restructuring team at Houlihan Lokey in Sao Paulo.": "aula5_oral1.mp3",
"Revenue in Q3 declined by eight percent compared to Q2, but the margin improved.": "aula5_oral2.mp3",
"We have conducted due diligence and submitted the proposal to the creditors.": "aula5_oral3.mp3",
"If I may, I would like to elaborate on the forecast. We estimate a recovery in Q4.": "aula5_oral4.mp3",
"Have we reached a consensus on the next steps, or should I follow up with the team?": "aula5_oral5.mp3",
"The forecast shows revenue growing by approximately five percent. We could close the deal by end of quarter.": "aula5_oral6.mp3",
"Good morning. I am Eduarda Gabriel, an associate at Houlihan Lokey. I am currently working on a restructuring deal.": "aula5_qf1.mp3",
"Revenue in Q3 was approximately one hundred and fifty million. Compared to Q2, it declined by eight percent.": "aula5_qf2.mp3",
"We have conducted due diligence, submitted the proposal, and negotiated the main terms.": "aula5_qf3.mp3",
"Sorry to interrupt, but the forecast shows revenue growing by approximately five percent in Q4.": "aula5_qf4.mp3",
"Not yet. We have negotiated the main terms but have not reached a final consensus.": "aula5_qf5.mp3",
"We are currently negotiating the final terms. We have submitted a proposal and expect to close the deal by end of quarter.": "aula5_qf6.mp3"
};
const jL=["Good morning, everyone. Let us start with introductions. Eduarda, please go ahead.","Eduarda has been leading the financial analysis on this case. Eduarda, could you walk us through the latest numbers?","What about the restructuring timeline?","Have we reached a consensus internally?","Good point. What do you estimate for Q4?"],eL=["Good morning. I am Eduarda Gabriel, an associate on the restructuring team at Houlihan Lokey, based in Sao Paulo.","Of course. Revenue in Q3 declined by eight percent compared to Q2. However, the operating margin has improved from fifteen to twenty percent.","We have conducted due diligence and have submitted a proposal to the creditors. We are currently negotiating the final terms.","Not yet. If I may, I would like to elaborate on two key points. First, the leverage ratio is still higher than the benchmark.","The forecast shows revenue growing by approximately five percent. If the creditors accept our proposal, we could close the deal by the end of the quarter."];
function cw(t){return t.trim().split(/\s+/).length;}let a=0;
function gv(t){if(jL.includes(t))return{id:ARTHUR,name:"Arthur"};if(eL.includes(t))return{id:ELLEN,name:"Ellen"};if(cw(t)<=2)return{id:ARTHUR,name:"Arthur"};const v=a%2===0?{id:ARTHUR,name:"Arthur"}:{id:ELLEN,name:"Ellen"};a++;return v;}
function gen(text,vid,op){return new Promise((res,rej)=>{const d=JSON.stringify({text,model_id:"eleven_monolingual_v1",voice_settings:{stability:.5,similarity_boost:.75}});const o={hostname:"api.elevenlabs.io",path:"/v1/text-to-speech/"+vid+"?output_format=mp3_44100_128",method:"POST",headers:{"Content-Type":"application/json","xi-api-key":ELEVENLABS_API_KEY,"Content-Length":Buffer.byteLength(d)}};const r=https.request(o,rs=>{if(rs.statusCode!==200){let b="";rs.on("data",c=>b+=c);rs.on("end",()=>rej(new Error(rs.statusCode+": "+b)));return;}const ch=[];rs.on("data",c=>ch.push(c));rs.on("end",()=>{fs.writeFileSync(op,Buffer.concat(ch));res();});});r.on("error",rej);r.write(d);r.end();});}
async function main(){const e=Object.entries(audioMap);let g=0,s=0;console.log("Generating "+e.length+" Aula 5 audio files...");for(let i=0;i<e.length;i++){const[t,f]=e[i];const o=path.join(OUTPUT_DIR,f);if(fs.existsSync(o)&&fs.statSync(o).size>1000){s++;if(cw(t)>2&&!jL.includes(t)&&!eL.includes(t))a++;continue;}const v=gv(t);try{await gen(t,v.id,o);g++;console.log("Generated "+(g+s)+"/"+e.length+": "+f+" ("+v.name+")");}catch(err){console.error("FAILED "+f+": "+err.message);}if(i<e.length-1)await new Promise(r=>setTimeout(r,500));}console.log("Done! Generated: "+g+", Skipped: "+s);}
main().catch(console.error);
