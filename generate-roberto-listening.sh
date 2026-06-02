#!/bin/bash

# ElevenLabs API config
VOICE_ID="sfJopaWaOtauCD3HKX6Q"  # Arthur (male - Roberto is male protagonist)
MODEL="eleven_turbo_v2_5"
OUTPUT_DIR="/Users/helenmendes/alumni-plano-gerador/public/audio/roberto-rezende"

# Listening 1: Voicemail about career transition
# Context: Slide 19 - voicemail from Roberto to a colleague about his career
# Comprehension Qs: What did he study? (mechanical eng + PhD), When transition? (2019), What achieved? (50+ client base)
TEXT1="Hi David, it's Roberto. I wanted to follow up on our conversation from last week about career transitions. As you know, my background is in mechanical engineering. I studied at the Federal University in Rio and completed my PhD in 2014. I spent five years working in research and development, but in 2019, the company needed someone to lead sales in Brazil. It was a big step, but I made the transition from engineering to sales. Since then, I have built a strong client base of over fifty industrial clients. Last year, we expanded into the agricultural segment, and our revenue increased by fifteen percent. It has been challenging, especially negotiating contracts in English, but very rewarding. Let me know if you want to chat more about it. Talk soon."

# Listening 2: Podcast interview about typical day
# Context: Slide 24 - podcast interview about typical day for sales exec who changed careers
# Comprehension Qs: What in morning? (manages emails, negotiates), What before transitioning? (PhD in eng), Most challenging? (negotiating in English)
TEXT2="Welcome to the Career Changers podcast. Today we are speaking with a sales executive who transitioned from engineering. So, tell us about your typical day. Sure. I usually start my morning managing emails and checking in with the Hong Kong office. Then I prioritize client meetings. I negotiate contracts with new clients almost every month. In the afternoon, I attend trade fairs or visit industrial clients across Brazil. The most challenging part is definitely negotiating contracts in English with international clients. Before all this, I completed my PhD in mechanical engineering. I made the switch to sales in 2019, so it was quite a change. But now I manage relationships with over fifty clients, and we achieved our sales target three months early last quarter. That is impressive. What advice would you give to someone considering a career change? Stay organized, be patient, and never stop learning. The transition was the best decision I ever made."

echo "Generating Listening 1: Career Voicemail..."
curl -s -X POST "https://api.elevenlabs.io/v1/text-to-speech/${VOICE_ID}" \
  -H "xi-api-key: ${ELEVENLABS_API_KEY}" \
  -H "Content-Type: application/json" \
  -d "$(python3 -c "
import json
text = '''${TEXT1}'''
print(json.dumps({
    'text': text,
    'model_id': '${MODEL}',
    'voice_settings': {
        'stability': 0.5,
        'similarity_boost': 0.75
    }
}))
")" \
  --output "${OUTPUT_DIR}/aula2_listening1_career_voicemail.mp3"

echo "Generating Listening 2: Typical Day..."
curl -s -X POST "https://api.elevenlabs.io/v1/text-to-speech/${VOICE_ID}" \
  -H "xi-api-key: ${ELEVENLABS_API_KEY}" \
  -H "Content-Type: application/json" \
  -d "$(python3 -c "
import json
text = '''${TEXT2}'''
print(json.dumps({
    'text': text,
    'model_id': '${MODEL}',
    'voice_settings': {
        'stability': 0.5,
        'similarity_boost': 0.75
    }
}))
")" \
  --output "${OUTPUT_DIR}/aula2_listening2_typical_day.mp3"

echo ""
echo "=== Verification ==="
ls -la "${OUTPUT_DIR}/aula2_listening1_career_voicemail.mp3" 2>&1
ls -la "${OUTPUT_DIR}/aula2_listening2_typical_day.mp3" 2>&1

# Check file sizes
SIZE1=$(stat -f%z "${OUTPUT_DIR}/aula2_listening1_career_voicemail.mp3" 2>/dev/null || echo "0")
SIZE2=$(stat -f%z "${OUTPUT_DIR}/aula2_listening2_typical_day.mp3" 2>/dev/null || echo "0")
echo ""
echo "Listening 1 size: ${SIZE1} bytes"
echo "Listening 2 size: ${SIZE2} bytes"

if [ "$SIZE1" -gt 50000 ] && [ "$SIZE2" -gt 50000 ]; then
    echo "SUCCESS: Both files are >50KB"
else
    echo "WARNING: One or both files may be too small (check for API errors)"
    echo "--- Listening 1 content check ---"
    file "${OUTPUT_DIR}/aula2_listening1_career_voicemail.mp3"
    echo "--- Listening 2 content check ---"
    file "${OUTPUT_DIR}/aula2_listening2_typical_day.mp3"
fi
