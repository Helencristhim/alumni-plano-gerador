const fs = require('fs');
const path = require('path');
const https = require('https');

const API_KEY = process.env.ELEVENLABS_API_KEY;
if (!API_KEY) { console.error('Missing ELEVENLABS_API_KEY'); process.exit(1); }

const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const OUT_DIR = path.join(__dirname, 'public/audio/elaine-mieko-pinho');

const listenings = [
  {
    file: 'listening9_taxi_ride_full.mp3',
    voice: ELLEN,
    text: "Elaine walks out of JFK Airport with her luggage. She sees a line of yellow taxis and a sign for rideshare pick up. She decides to take a taxi. Could you take me to the Hilton Hotel in Manhattan, please? she asks the driver. Sure! My name is Miguel. It is about 45 minutes with traffic, he says. How much is it to Manhattan? Elaine asks. The fare is about 70 dollars plus tolls, Miguel explains. During the ride, Elaine watches the city through the window. The traffic is heavy, but Miguel knows a good route. Turn right here and then go straight, he says. They arrive at the hotel. Here we are. The Hilton Hotel. The meter shows 72 dollars, says Miguel. Thank you, Miguel! You were very kind. Could I have a receipt, please? Elaine asks. Of course! Here is your receipt. Have a great day! Miguel replies."
  },
  {
    file: 'listening10_rideshare_notification_full.mp3',
    voice: ARTHUR,
    text: "Your driver is arriving in 3 minutes. A white Toyota Camry, license plate TLC-4829. Your driver is Carlos. Estimated time to destination: 35 minutes. Fare estimate: 42 to 55 dollars. Please wait at the designated pick up area. Your driver will confirm your name when he arrives. You can track the car on the map in real time. If you need to cancel, please do so within 2 minutes to avoid a cancellation fee."
  }
];

function generateAudio(text, voiceId, outputPath) {
  return new Promise((resolve, reject) => {
    const data = JSON.stringify({
      text: text,
      model_id: 'eleven_monolingual_v1',
      voice_settings: { stability: 0.5, similarity_boost: 0.75 }
    });

    const options = {
      hostname: 'api.elevenlabs.io',
      path: `/v1/text-to-speech/${voiceId}`,
      method: 'POST',
      headers: {
        'Accept': 'audio/mpeg',
        'Content-Type': 'application/json',
        'xi-api-key': API_KEY,
        'Content-Length': Buffer.byteLength(data)
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
        const buf = Buffer.concat(chunks);
        fs.writeFileSync(outputPath, buf);
        console.log(`OK: ${path.basename(outputPath)} (${(buf.length / 1024).toFixed(1)} KB)`);
        resolve();
      });
    });

    req.on('error', reject);
    req.write(data);
    req.end();
  });
}

(async () => {
  for (const l of listenings) {
    const outPath = path.join(OUT_DIR, l.file);
    if (fs.existsSync(outPath)) {
      console.log(`SKIP: ${l.file} already exists`);
      continue;
    }
    console.log(`Generating: ${l.file}...`);
    await generateAudio(l.text, l.voice, outPath);
  }
  console.log('Done!');
})();
