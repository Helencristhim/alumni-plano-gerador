#!/bin/bash
# Generate ElevenLabs audio for Rubens Tofolo — Aula 4: Life Experiences
# Usage: ELEVENLABS_API_KEY=sk-xxx ./scripts/generate-audio-rubens-aula4.sh

if [ -n "$1" ]; then
  export ELEVENLABS_API_KEY="$1"
fi

if [ -z "$ELEVENLABS_API_KEY" ]; then
  echo "ERROR: No API key provided."
  echo "Usage: $0 YOUR_ELEVENLABS_API_KEY"
  echo "   Or: ELEVENLABS_API_KEY=sk-xxx $0"
  exit 1
fi

echo "Using ElevenLabs API key: ${ELEVENLABS_API_KEY:0:8}..."
echo ""

cd "$(dirname "$0")/.." || exit 1

API_KEY="$ELEVENLABS_API_KEY"
ARTHUR="sfJopaWaOtauCD3HKX6Q"
ELLEN="BIvP0GN1cAtSRTxNHnWS"
OUT_DIR="public/audio/rubens-tofolo"
MODEL="eleven_multilingual_v2"

mkdir -p "$OUT_DIR"

TOTAL=0
GENERATED=0
SKIPPED=0
ERRORS=0

generate() {
  local text="$1"
  local filename="$2"
  local voice="$3"
  local filepath="$OUT_DIR/$filename"
  TOTAL=$((TOTAL + 1))

  if [ -f "$filepath" ] && [ $(wc -c < "$filepath") -gt 500 ]; then
    echo "SKIP: $filename (exists)"
    SKIPPED=$((SKIPPED + 1))
    return
  fi

  echo "GEN: $filename"
  echo "     Text: $text"
  echo "     Voice: $([ "$voice" = "$ARTHUR" ] && echo 'Arthur' || echo 'Ellen')"

  curl -s -X POST "https://api.elevenlabs.io/v1/text-to-speech/$voice" \
    -H "xi-api-key: $API_KEY" \
    -H "Content-Type: application/json" \
    -d "{\"text\":\"$text\",\"model_id\":\"$MODEL\",\"voice_settings\":{\"stability\":0.5,\"similarity_boost\":0.75,\"style\":0.0,\"use_speaker_boost\":true}}" \
    --output "$filepath"

  if [ -f "$filepath" ] && [ $(wc -c < "$filepath") -lt 200 ]; then
    echo "  WARNING: File too small, may be error response:"
    cat "$filepath"
    echo ""
    ERRORS=$((ERRORS + 1))
    rm -f "$filepath"
  else
    GENERATED=$((GENERATED + 1))
  fi

  sleep 0.3
}

echo "============================================"
echo "=== Aula 4: Life Experiences             ==="
echo "============================================"
echo ""

# === VOCABULARY (single words = Arthur) ===
generate "Journey" "journey.mp3" "$ARTHUR"
generate "Explore" "explore.mp3" "$ARTHUR"
generate "Milestone" "milestone.mp3" "$ARTHUR"
generate "Challenge" "challenge.mp3" "$ARTHUR"
generate "Accomplish" "accomplish.mp3" "$ARTHUR"
generate "Broaden" "broaden.mp3" "$ARTHUR"
generate "Overcome" "overcome.mp3" "$ARTHUR"
generate "Remarkable" "remarkable.mp3" "$ARTHUR"

# === VOCAB EXAMPLE SENTENCES (alternate Arthur/Ellen) ===
generate "My journey to becoming a doctor started in medical school." "my_journey_to_becoming_a_doctor.mp3" "$ARTHUR"
generate "I want to explore new treatment methods for diabetes." "i_want_to_explore_new_treatment_methods.mp3" "$ELLEN"
generate "Getting my doctorate was a major milestone in my career." "getting_my_doctorate_was_a_major_milestone.mp3" "$ARTHUR"
generate "Learning seven languages was a real challenge." "learning_seven_languages_was_a_real_challenge.mp3" "$ELLEN"
generate "I have accomplished many things in twenty-five years of medicine." "i_have_accomplished_many_things.mp3" "$ARTHUR"
generate "Traveling has broadened my perspective on medicine." "traveling_has_broadened_my_perspective.mp3" "$ELLEN"
generate "I have overcome many obstacles in my career." "i_have_overcome_many_obstacles.mp3" "$ARTHUR"
generate "His career has been truly remarkable." "his_career_has_been_truly_remarkable.mp3" "$ELLEN"

# === GRAMMAR / FILL-IN / SURVIVAL SENTENCES ===
generate "I have visited ninety-five countries." "i_have_visited_ninety_five_countries.mp3" "$ARTHUR"
generate "Have you ever attended a medical conference abroad?" "have_you_ever_attended_a_medical_conference.mp3" "$ELLEN"
generate "I have already published several papers on metabolic syndrome." "i_have_already_published_several_papers.mp3" "$ARTHUR"
generate "I have never missed a conference deadline." "i_have_never_missed_a_conference_deadline.mp3" "$ELLEN"
generate "I have visited Japan, China, and South Korea." "i_have_visited_japan_china_south_korea.mp3" "$ARTHUR"
generate "I have been practicing medicine for over twenty-five years." "i_have_been_practicing_for_over_twenty_five_years.mp3" "$ELLEN"
generate "Have you ever presented at an international conference?" "have_you_ever_presented_at_intl_conference.mp3" "$ARTHUR"
generate "I have already finished my latest research paper." "i_have_already_finished_my_latest_paper.mp3" "$ELLEN"
generate "I haven't visited Africa yet." "i_havent_visited_africa_yet.mp3" "$ARTHUR"
generate "She has never traveled outside of Europe." "she_has_never_traveled_outside_europe.mp3" "$ELLEN"
generate "Have you ever lived in another country?" "have_you_ever_lived_in_another_country.mp3" "$ARTHUR"
generate "I have just returned from a conference in Tokyo." "i_have_just_returned_from_tokyo.mp3" "$ELLEN"
generate "We have already discussed this case." "we_have_already_discussed_this_case.mp3" "$ARTHUR"

# === DIALOGUE 4 (Sarah=Ellen, Rubens=Arthur) ===
generate "Rubens, have you ever been to Asia?" "dialogue4_line1_sarah.mp3" "$ELLEN"
generate "Yes, I have! I have visited Japan, China, and South Korea. Medical conferences there are remarkable." "dialogue4_line2_rubens.mp3" "$ARTHUR"
generate "That is impressive! Have you already explored the conference schedule for tomorrow?" "dialogue4_line3_sarah.mp3" "$ELLEN"
generate "Not yet. I have been so busy with the networking sessions." "dialogue4_line4_rubens.mp3" "$ARTHUR"
generate "I see! What is the biggest milestone in your career so far?" "dialogue4_line5_sarah.mp3" "$ELLEN"
generate "Getting my doctorate in France was a major milestone. I have accomplished a lot since then." "dialogue4_line6_rubens.mp3" "$ARTHUR"
generate "Have you ever had to overcome a major challenge?" "dialogue4_line7_sarah.mp3" "$ELLEN"
generate "Yes, learning to communicate in seven languages was a real challenge. But it has broadened my perspective enormously." "dialogue4_line8_rubens.mp3" "$ARTHUR"

# === LISTENING AUDIOS (full MP3s) ===
generate "I have visited ninety-five countries in my lifetime. I have explored different cultures, overcome language barriers, and accomplished things that most people only dream of. My journey started in medical school in Belem, Brazil. Since then, I have attended conferences on every continent except Antarctica. Getting my doctorate in France was a major milestone. Learning seven languages was a real challenge, but it has broadened my perspective enormously. I have never missed a major medical conference. My career has been truly remarkable, and I have accomplished more than I ever imagined." "listening_life_experiences.mp3" "$ARTHUR"

generate "Have you ever been to a conference in Asia? Yes, I have. I have visited Japan, China, and South Korea. The medical conferences there are remarkable. Have you already explored the schedule for tomorrow? Not yet. I have been so busy with the networking sessions. What is the biggest milestone in your career so far? Getting my doctorate in France was a major milestone. I have accomplished a lot since then. Have you ever had to overcome a major challenge? Yes. Learning to communicate in seven languages was a real challenge. But it has broadened my perspective enormously." "listening_dialogue_present_perfect.mp3" "$ELLEN"

echo ""
echo "============================================"
echo "=== SUMMARY                              ==="
echo "============================================"
echo "Total: $TOTAL"
echo "Generated: $GENERATED"
echo "Skipped: $SKIPPED"
echo "Errors: $ERRORS"
echo ""

if [ "$ERRORS" -gt 0 ]; then
  echo "WARNING: Some audio files failed to generate."
  exit 1
fi

echo "All audio files generated successfully!"
