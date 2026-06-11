const fs = require('fs');
const path = require('path');
const https = require('https');
const ELEVENLABS_API_KEY = process.env.ELEVENLABS_API_KEY;
if (!ELEVENLABS_API_KEY) { console.error('ERROR: ELEVENLABS_API_KEY not set'); process.exit(1); }
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const RACHEL = '21m00Tcm4TlvDq8ikWAM';
const OUTPUT_DIR = path.join(__dirname, 'public', 'audio', 'anna-flavia-miranda-da-silva');

const audioMap = {
  "Desk": "aula3_desk.mp3", "Computer": "aula3_computer.mp3", "Printer": "aula3_printer.mp3",
  "Chair": "aula3_chair.mp3", "Shelf": "aula3_shelf.mp3", "Whiteboard": "aula3_whiteboard.mp3",
  "Folder": "aula3_folder.mp3", "Calculator": "aula3_calculator.mp3",
  "There is a computer on my desk.": "aula3_there_is_computer.mp3",
  "There are two printers in the office.": "aula3_there_are_printers.mp3",
  "There is a whiteboard on the wall.": "aula3_there_is_whiteboard.mp3",
  "There are many folders on the shelf.": "aula3_there_are_folders.mp3",
  "Is there a calculator on your desk?": "aula3_is_there_calculator.mp3",
  "Are there any chairs in the meeting room?": "aula3_are_there_chairs.mp3",
  "There is not a printer near my desk.": "aula3_there_is_not.mp3",
  "There are not any windows in the meeting room.": "aula3_there_are_not.mp3",
  "Hi Anna Flavia! I love your new office. Can you show me around?": "aula3_dial_marina_1.mp3",
  "Of course, Marina! This is my desk. There is a computer and a calculator on it.": "aula3_dial_anna_1.mp3",
  "Nice! Is there a printer near your desk?": "aula3_dial_marina_2.mp3",
  "No, there is not. The printer is in the hallway. But there is a shelf with all my folders.": "aula3_dial_anna_2.mp3",
  "Are there any meeting rooms on this floor?": "aula3_dial_marina_3.mp3",
  "Yes, there are two meeting rooms. There is a whiteboard in each one.": "aula3_dial_anna_3.mp3",
  "That is great! Is there a coffee machine too?": "aula3_dial_marina_4.mp3",
  "Yes! There is a coffee machine in the kitchen area. Let me show you!": "aula3_dial_anna_4.mp3",
  "This is my workspace at the Sao Paulo office. There is a large desk with a computer and a calculator. There are many folders on the shelf next to my desk. There is a whiteboard on the wall for meetings. There are two printers on this floor, but there is not one near my desk. There is a coffee machine in the kitchen. I like my new office!": "aula3_listening.mp3",
  "There is a computer on my desk.": "aula3_surv_computer.mp3",
  "There are two meeting rooms.": "aula3_surv_meeting_rooms.mp3",
  "Is there a printer near here?": "aula3_surv_printer.mp3",
  "There is not a window in this room.": "aula3_surv_not_window.mp3",
  "Where is the coffee machine?": "aula3_surv_coffee.mp3",
  "There is a computer and a calculator on my desk.": "aula3_speech_1.mp3",
  "There are many folders on the shelf.": "aula3_speech_2.mp3",
  "Is there a whiteboard in the meeting room?": "aula3_speech_3.mp3",
  "There are two meeting rooms on this floor.": "aula3_oral_meeting_rooms.mp3",
  "There is not a window in the meeting room.": "aula3_oral_no_window.mp3",
  "Are there any chairs available?": "aula3_oral_chairs.mp3",
  "This is my desk. There is a computer. There are folders on the shelf. There is a whiteboard on the wall. There are two meeting rooms.": "aula3_order.mp3"
};

const marinaLines = ["Hi Anna Flavia! I love your new office. Can you show me around?","Nice! Is there a printer near your desk?","Are there any meeting rooms on this floor?","That is great! Is there a coffee machine too?"];
const annaLines = ["Of course, Marina! This is my desk. There is a computer and a calculator on it.","No, there is not. The printer is in the hallway. But there is a shelf with all my folders.","Yes, there are two meeting rooms. There is a whiteboard in each one.","Yes! There is a coffee machine in the kitchen area. Let me show you!"];

function countWords(t){return t.trim().split(/\s+/).length}
let alt=0;
function getVoice(text){
  if(marinaLines.includes(text)) return {id:RACHEL,name:'Rachel'};
  if(annaLines.includes(text)) return {id:ELLEN,name:'Ellen'};
  if(countWords(text)<=2) return {id:ELLEN,name:'Ellen'};
  const v=alt%2===0?{id:ELLEN,name:'Ellen'}:{id:ARTHUR,name:'Arthur'};alt++;return v;
}

function generateAudio(text,voiceId,outputPath){
  return new Promise((resolve,reject)=>{
    const postData=JSON.stringify({text,model_id:'eleven_multilingual_v2',voice_settings:{stability:0.5,similarity_boost:0.75}});
    const options={hostname:'api.elevenlabs.io',path:'/v1/text-to-speech/'+voiceId+'?output_format=mp3_44100_128',method:'POST',headers:{'Content-Type':'application/json','xi-api-key':ELEVENLABS_API_KEY,'Content-Length':Buffer.byteLength(postData)}};
    const req=https.request(options,(res)=>{if(res.statusCode!==200){let b='';res.on('data',d=>b+=d);res.on('end',()=>reject(new Error('API '+res.statusCode+': '+b)));return}const chunks=[];res.on('data',c=>chunks.push(c));res.on('end',()=>{fs.writeFileSync(outputPath,Buffer.concat(chunks));resolve()})});
    req.on('error',reject);req.write(postData);req.end();
  });
}

async function main(){
  const entries=Object.entries(audioMap);let gen=0,skip=0;
  console.log('Generating '+entries.length+' Aula 3 audio files...');
  for(let i=0;i<entries.length;i++){
    const[text,file]=entries[i];const out=path.join(OUTPUT_DIR,file);
    if(fs.existsSync(out)&&fs.statSync(out).size>1000){skip++;if(countWords(text)>2&&!marinaLines.includes(text)&&!annaLines.includes(text))alt++;continue}
    const voice=getVoice(text);
    try{await generateAudio(text,voice.id,out);gen++;console.log(`Generated ${gen+skip}/${entries.length}: ${file} (${voice.name})`)}
    catch(err){console.error(`FAILED ${file}: ${err.message}`)}
    if(i<entries.length-1) await new Promise(r=>setTimeout(r,500));
  }
  console.log(`Done! Generated: ${gen}, Skipped: ${skip}`);
}
main().catch(console.error);
