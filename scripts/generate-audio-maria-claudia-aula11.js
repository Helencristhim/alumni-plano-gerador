const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const DIR = path.join(__dirname, '..', 'public', 'audio', 'maria-claudia-curimbaba');

const PHRASES = [
  // ===== Vocab (Ellen) =====
  { text: "Dial in", file: "aula11_dial_in.mp3", voice: ELLEN },
  { text: "Mute", file: "aula11_mute.mp3", voice: ELLEN },
  { text: "Screen share", file: "aula11_screen_share.mp3", voice: ELLEN },
  { text: "Bandwidth", file: "aula11_bandwidth.mp3", voice: ELLEN },
  { text: "Time zone", file: "aula11_time_zone.mp3", voice: ELLEN },
  { text: "Lag", file: "aula11_lag.mp3", voice: ELLEN },
  { text: "Drop off", file: "aula11_drop_off.mp3", voice: ELLEN },
  { text: "Follow-up", file: "aula11_follow_up.mp3", voice: ELLEN },

  // ===== Vocab examples (alternate) =====
  { text: "Could everyone please dial in five minutes early?", file: "aula11_could_everyone_dial_in.mp3", voice: ARTHUR },
  { text: "Would you mind muting your microphone when you are not speaking?", file: "aula11_would_you_mind_muting.mp3", voice: ELLEN },
  { text: "Could you screen share the presentation, please?", file: "aula11_could_you_screen_share.mp3", voice: ARTHUR },
  { text: "We do not have the bandwidth to take on another project right now.", file: "aula11_we_do_not_have_bandwidth.mp3", voice: ELLEN },
  { text: "Houston is one hour behind Sao Paulo's time zone.", file: "aula11_houston_is_one_hour.mp3", voice: ARTHUR },
  { text: "There is a slight lag on the line. Could you repeat that?", file: "aula11_there_is_a_slight_lag.mp3", voice: ELLEN },
  { text: "I apologize, I dropped off the call for a moment.", file: "aula11_i_apologize_dropped_off.mp3", voice: ARTHUR },
  { text: "I will send a follow-up email with the action items.", file: "aula11_i_will_send_follow_up.mp3", voice: ELLEN },

  // ===== Expressions (alternate) =====
  { text: "Could you please...?", file: "aula11_expr_could_you_please.mp3", voice: ARTHUR },
  { text: "Could you please share your screen so we can see the numbers?", file: "aula11_expr_could_you_example.mp3", voice: ELLEN },
  { text: "Would you mind...?", file: "aula11_expr_would_you_mind.mp3", voice: ARTHUR },
  { text: "Would you mind repeating that? There was a lag on the line.", file: "aula11_expr_would_you_example.mp3", voice: ELLEN },
  { text: "I apologize for...", file: "aula11_expr_i_apologize_for.mp3", voice: ARTHUR },
  { text: "I apologize for the technical difficulties. Let me reconnect.", file: "aula11_expr_apologize_example.mp3", voice: ELLEN },

  // ===== Grammar context passage (Ellen) =====
  { text: "Maria Claudia is leading a conference call with her counterparts in Houston and Pittsburgh. The call starts at 10 AM Sao Paulo time, which is 8 AM in Houston. Good morning, everyone. Could you please confirm you can hear me clearly? she begins. David has a lag on his connection. Would you mind repeating the agenda, Maria Claudia? There was a slight delay, he asks. She screen shares the Q3 presentation. Could you all see my screen? A participant drops off and reconnects. I apologize for dropping off. My bandwidth was low, they explain. Maria Claudia handles it smoothly: No problem. Would you mind muting your microphone when you are not speaking? It helps with the audio quality. She closes: I will send a follow-up email with all the action items.", file: "aula11_grammar_context_passage.mp3", voice: ELLEN },

  // ===== Fill-in (alternate) =====
  { text: "Could everyone please dial in five minutes early?", file: "aula11_fill_dial_in.mp3", voice: ARTHUR },
  { text: "Would you mind muting your microphone?", file: "aula11_fill_muting.mp3", voice: ELLEN },
  { text: "Could you screen share the presentation, please?", file: "aula11_fill_screen_share.mp3", voice: ARTHUR },
  { text: "We do not have the bandwidth for another project.", file: "aula11_fill_bandwidth.mp3", voice: ELLEN },
  { text: "Houston is one hour behind our time zone.", file: "aula11_fill_time_zone.mp3", voice: ARTHUR },
  { text: "There is a slight lag on the line.", file: "aula11_fill_lag.mp3", voice: ELLEN },
  { text: "I apologize, I dropped off the call for a moment.", file: "aula11_fill_dropped_off.mp3", voice: ARTHUR },
  { text: "I will send a follow-up email with the action items.", file: "aula11_fill_follow_up.mp3", voice: ELLEN },

  // ===== Ordering =====
  { text: "Good morning, everyone. Can you hear me clearly? Let me share my screen so you can see the agenda. Could you please mute your microphone when not speaking? Would you mind repeating that? There was a lag. I apologize for the technical issue. I am back now. I will send a follow-up email with all action items. Thank you.", file: "aula11_order_call_sequence.mp3", voice: ELLEN },

  // ===== Survival (Ellen) =====
  { text: "Could you please repeat that?", file: "aula11_surv_could_you_repeat.mp3", voice: ELLEN },
  { text: "Would you mind muting your microphone?", file: "aula11_surv_would_you_mute.mp3", voice: ELLEN },
  { text: "I apologize for the technical issue.", file: "aula11_surv_apologize_tech.mp3", voice: ELLEN },
  { text: "Could you screen share the presentation?", file: "aula11_surv_screen_share.mp3", voice: ELLEN },
  { text: "I will send a follow-up email after the call.", file: "aula11_surv_follow_up.mp3", voice: ELLEN },

  // ===== Speech (Ellen) =====
  { text: "Could you please share your screen so we can see the numbers?", file: "aula11_speech_share_screen.mp3", voice: ELLEN },
  { text: "Would you mind repeating that? There was a lag on the line.", file: "aula11_speech_repeating.mp3", voice: ELLEN },
  { text: "I apologize for the technical difficulties.", file: "aula11_speech_apologize.mp3", voice: ELLEN },
  { text: "Houston is one hour behind Sao Paulo's time zone.", file: "aula11_speech_time_zone.mp3", voice: ELLEN },
  { text: "I will send a follow-up email with the action items.", file: "aula11_speech_follow_up.mp3", voice: ELLEN },

  // ===== Listening 1 (MC leads call = Ellen) =====
  { text: "Good morning, everyone. Thank you for dialing in. I know we are working across three time zones today, so I appreciate everyone adjusting their schedules. Could you please confirm you can hear me clearly? I am going to screen share the Q3 presentation now. Could you all see my screen? Perfect. Let me go through the agenda. We have three items today. First, the revenue update. Second, the procurement contract. Third, action items from last month. Would you mind muting your microphones when you are not speaking? It really helps with the audio quality. If you have any questions, please use the raise hand feature or type in the chat. I will send a follow-up email with all the action items and the recording after the call.", file: "aula11_ic_listening1_mc_leads.mp3", voice: ELLEN },

  // ===== Listening 2 (David handles issues = Arthur) =====
  { text: "Sorry, Maria Claudia. I apologize for interrupting. There seems to be a lag on my end. Would you mind repeating the revenue numbers? I dropped off the call for about thirty seconds and missed the beginning. Also, I cannot see your screen share. Could you please stop sharing and share again? Sometimes that fixes the issue. While we wait, I wanted to mention that the Pittsburgh team had similar bandwidth problems last week. We upgraded our internet connection, and it made a big difference. If anyone else is experiencing lag, I would suggest turning off your camera to save bandwidth. Could you please continue with the agenda, Maria Claudia? I can hear you clearly now.", file: "aula11_ic_listening2_david_issues.mp3", voice: ARTHUR },

  // ===== Dialogue =====
  { text: "Good morning, David. Could you please confirm you can hear me?", file: "aula11_ic_dlg_mc_1.mp3", voice: ELLEN },
  { text: "Good morning. Yes, I can hear you, but there is a slight lag. Could you speak a bit slower?", file: "aula11_ic_dlg_david_1.mp3", voice: ARTHUR },
  { text: "Of course. Would you mind muting when you are not speaking? There is some background noise.", file: "aula11_ic_dlg_mc_2.mp3", voice: ELLEN },
  { text: "Done. I apologize for that. Could you screen share the presentation now?", file: "aula11_ic_dlg_david_2.mp3", voice: ARTHUR },
  { text: "Let me share my screen. Can everyone see it? Sarah, are you still on the call?", file: "aula11_ic_dlg_mc_3.mp3", voice: ELLEN },
  { text: "I think Sarah dropped off. Her bandwidth might be low. She will probably dial back in shortly.", file: "aula11_ic_dlg_david_3.mp3", voice: ARTHUR },
  { text: "No problem. Let us continue. Would you mind giving us the Pittsburgh update while we wait?", file: "aula11_ic_dlg_mc_4.mp3", voice: ELLEN },
  { text: "Sure. Revenue is up eight percent. But I apologize, the numbers on my end are a bit delayed because of the lag.", file: "aula11_ic_dlg_david_4.mp3", voice: ARTHUR },
  { text: "That is fine. Could you please send the detailed report as a follow-up after the call?", file: "aula11_ic_dlg_mc_5.mp3", voice: ELLEN },
  { text: "Absolutely. I will send a follow-up email with all the numbers and action items by end of day.", file: "aula11_ic_dlg_david_5.mp3", voice: ARTHUR },

  // ===== Error correction =====
  { text: "Would you mind to repeat that?", file: "aula11_ic_error_mind_to_repeat.mp3", voice: ARTHUR },
  { text: "Could you to send the report?", file: "aula11_ic_error_could_to_send.mp3", voice: ELLEN },
  { text: "I apologize for drop off the call.", file: "aula11_ic_error_drop_off.mp3", voice: ARTHUR },
  { text: "Would you mind to mute your microphone?", file: "aula11_ic_error_mind_to_mute.mp3", voice: ELLEN },
  { text: "Could you please sharing your screen?", file: "aula11_ic_error_please_sharing.mp3", voice: ARTHUR },
];

async function gen(text, voiceId, outPath) {
  const r = await fetch('https://api.elevenlabs.io/v1/text-to-speech/' + voiceId, {
    method: 'POST',
    headers: { 'xi-api-key': API_KEY, 'Content-Type': 'application/json' },
    body: JSON.stringify({ text, model_id: 'eleven_multilingual_v2', voice_settings: { stability: 0.5, similarity_boost: 0.75 } }),
  });
  if (!r.ok) throw new Error(r.status + ': ' + (await r.text()));
  const buf = Buffer.from(await r.arrayBuffer());
  fs.writeFileSync(outPath, buf);
  return buf.length;
}

async function main() {
  if (!API_KEY) { console.error('Set ELEVENLABS_API_KEY env var'); process.exit(1); }
  if (!fs.existsSync(DIR)) fs.mkdirSync(DIR, { recursive: true });
  const seen = new Set();
  const unique = PHRASES.filter(p => { const k = p.file.toLowerCase(); if (seen.has(k)) return false; seen.add(k); return true; });
  console.log('Generating ' + unique.length + ' AULA 11 audio files...');
  let generated = 0, skipped = 0;
  for (const p of unique) {
    const outPath = path.join(DIR, p.file);
    if (fs.existsSync(outPath)) { console.log('SKIP: ' + p.file); skipped++; }
    else {
      try {
        const bytes = await gen(p.text, p.voice, outPath);
        console.log('OK [' + (p.voice === ELLEN ? 'ellen' : 'arthur') + ']: ' + p.file + ' (' + (bytes / 1024).toFixed(1) + 'KB)');
        generated++;
        await new Promise(r => setTimeout(r, 500));
      } catch (e) { console.error('FAIL: ' + p.file + ' — ' + e.message); }
    }
  }
  console.log('\nDone! Generated: ' + generated + ' | Skipped: ' + skipped + ' | Total: ' + unique.length);
}
main();
