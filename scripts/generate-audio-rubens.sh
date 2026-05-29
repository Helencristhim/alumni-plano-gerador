#!/bin/bash
# Generate ElevenLabs audio for Rubens Tofolo
# Usage: ./scripts/generate-audio-rubens.sh YOUR_API_KEY
# Or:    ELEVENLABS_API_KEY=sk-xxx ./scripts/generate-audio-rubens.sh
#
# Voices: Arthur (sfJopaWaOtauCD3HKX6Q) = male, Ellen (BIvP0GN1cAtSRTxNHnWS) = female
# Rubens is male => single words + student phrases use Arthur
# Dialogue: sarah lines = Ellen, rubens lines = Arthur
# General sentences: alternate Arthur/Ellen

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
echo "=== Generating audio for Rubens Tofolo   ==="
echo "============================================"
echo ""

# -----------------------------------------------
# SURVIVAL PHRASES (Arthur - male student voice)
# -----------------------------------------------
echo "=== Survival Phrases (Arthur) ==="
generate "Could you repeat that, please?" "could_you_repeat_that_please.mp3" "$ARTHUR"
generate "I specialize in endocrinology and obesity." "i_specialize_in_endocrinology_and_obesity.mp3" "$ARTHUR"
generate "I have been practicing medicine for over twenty-five years." "i_have_been_practicing_medicine_for_over_twenty_five_years.mp3" "$ARTHUR"
generate "Could you speak a little slower, please?" "could_you_speak_a_little_slower_please.mp3" "$ARTHUR"
generate "It is nice to meet you. I am Dr. Tofolo from Brazil." "it_is_nice_to_meet_you_i_am_dr_tofolo_from_brazil.mp3" "$ARTHUR"

# -----------------------------------------------
# SINGLE WORDS - Vocabulary (Arthur - male student)
# -----------------------------------------------
echo ""
echo "=== Single Words / Vocabulary (Arthur) ==="
generate "Specialize" "specialize.mp3" "$ARTHUR"
generate "Background" "background.mp3" "$ARTHUR"
generate "Currently" "currently.mp3" "$ARTHUR"
generate "Fluency" "fluency.mp3" "$ARTHUR"
generate "Conference" "conference.mp3" "$ARTHUR"
generate "Recall" "recall.mp3" "$ARTHUR"
generate "Comprehensive" "comprehensive.mp3" "$ARTHUR"
generate "Reactivate" "reactivate.mp3" "$ARTHUR"

# -----------------------------------------------
# VOCAB EXAMPLE SENTENCES (Alternating Arthur/Ellen)
# -----------------------------------------------
echo ""
echo "=== Vocab Example Sentences (Alternating) ==="
generate "I specialize in endocrinology and obesity management." "i_specialize_in_endocrinology_and_obesity_management.mp3" "$ARTHUR"
generate "His background includes research in the United States and France." "his_background_includes_research_in_the_us_and_france.mp3" "$ELLEN"
generate "I am currently leading a study on metabolic syndrome." "i_am_currently_leading_a_study_on_metabolic_syndrome.mp3" "$ARTHUR"
generate "She achieved fluency in English after living abroad." "she_achieved_fluency_in_english_after_living_abroad.mp3" "$ELLEN"
generate "The conference attracted specialists from forty countries." "the_conference_attracted_specialists_from_forty_countries.mp3" "$ARTHUR"
generate "I can recall presenting research in California in nineteen ninety-five." "i_can_recall_presenting_research_in_california.mp3" "$ELLEN"
generate "We need a comprehensive review of the latest data." "we_need_a_comprehensive_review_of_the_latest_data.mp3" "$ARTHUR"
generate "He wants to reactivate his English for international events." "he_wants_to_reactivate_his_english_for_intl_events.mp3" "$ELLEN"

# -----------------------------------------------
# DIALOGUE LINES - Sarah = Ellen, Rubens = Arthur
# -----------------------------------------------
echo ""
echo "=== Dialogue Lines ==="
generate "Hi there! I am Dr. Sarah Chen from Johns Hopkins. Are you attending the plenary session on metabolic health?" "dialogue_line1_sarah.mp3" "$ELLEN"
generate "Yes, I am! I specialize in endocrinology. I am very interested in the new research." "dialogue_line2_rubens.mp3" "$ARTHUR"
generate "That is great! Where are you based?" "dialogue_line3_sarah.mp3" "$ELLEN"
generate "I have a clinic in Belem, in northern Brazil. I currently focus on diabetes and obesity." "dialogue_line4_rubens.mp3" "$ARTHUR"
generate "Interesting! How long have you been in the field?" "dialogue_line5_sarah.mp3" "$ELLEN"
generate "I have been practicing for over twenty-five years. My background includes research in the United States and France." "dialogue_line6_rubens.mp3" "$ARTHUR"
generate "Impressive! A doctorate from France. In French or English?" "dialogue_line7_sarah.mp3" "$ELLEN"
generate "In French, actually. I speak seven languages, but I want to reactivate my English fluency for conferences like this." "dialogue_line8_rubens.mp3" "$ARTHUR"

# -----------------------------------------------
# STUDENT EXERCISE PHRASES (Arthur - male student)
# -----------------------------------------------
echo ""
echo "=== Student Exercise Phrases (Arthur) ==="
generate "I specialize in endocrinology." "i_specialize_in_endocrinology.mp3" "$ARTHUR"
generate "I have visited ninety-five countries." "i_have_visited_ninety_five_countries.mp3" "$ARTHUR"
generate "I currently focus on diabetes and obesity." "i_currently_focus_on_diabetes_and_obesity.mp3" "$ARTHUR"
generate "My background includes research in the United States." "my_background_includes_research_in_the_us.mp3" "$ARTHUR"
generate "I want to reactivate my English fluency." "i_want_to_reactivate_my_english_fluency.mp3" "$ARTHUR"
generate "I have been practicing for over twenty-five years." "i_have_been_practicing_for_over_twenty_five_years.mp3" "$ARTHUR"
generate "The conference starts tomorrow morning." "the_conference_starts_tomorrow_morning.mp3" "$ARTHUR"
generate "I can recall my time in California very well." "i_can_recall_my_time_in_california_very_well.mp3" "$ARTHUR"
generate "We need a comprehensive plan for the patients." "we_need_a_comprehensive_plan_for_the_patients.mp3" "$ARTHUR"

# -----------------------------------------------
# SELF-INTRODUCTION (Arthur - student voice)
# -----------------------------------------------
echo ""
echo "=== Self-Introduction (Arthur) ==="
generate "Good morning, everyone. My name is Dr. Rubens Tofolo. I am an endocrinologist from Belem, Brazil. I specialize in diabetes and obesity management. I have been practicing for over twenty-five years. My background includes research in the United States and France. I currently focus on metabolic syndrome, and I am here to reactivate my English fluency for international conferences." "full_self_introduction.mp3" "$ARTHUR"
generate "Good morning, everyone. My name is Dr. Rubens Tofolo." "good_morning_my_name_is_dr_rubens_tofolo.mp3" "$ARTHUR"
generate "I am an endocrinologist from Belem, Brazil." "i_am_an_endocrinologist_from_belem_brazil.mp3" "$ARTHUR"
generate "I have a clinic in Belem, in northern Brazil." "i_have_a_clinic_in_belem_in_northern_brazil.mp3" "$ARTHUR"

# -----------------------------------------------
# GENERAL SENTENCES (Alternating Arthur/Ellen)
# -----------------------------------------------
echo ""
echo "=== General Sentences (Alternating) ==="
generate "She achieved fluency after years of practice." "she_achieved_fluency_after_years_of_practice.mp3" "$ELLEN"
generate "He recalled his years living in California." "he_recalled_his_years_living_in_california.mp3" "$ARTHUR"
generate "The review was comprehensive and detailed." "the_review_was_comprehensive_and_detailed.mp3" "$ELLEN"

# -----------------------------------------------
# GRAMMAR EXAMPLES (Alternating Arthur/Ellen)
# -----------------------------------------------
echo ""
echo "=== Grammar Examples (Alternating) ==="
generate "I work every day." "i_work_every_day.mp3" "$ARTHUR"
generate "I have worked here for twenty years." "i_have_worked_here_for_twenty_years.mp3" "$ELLEN"
generate "I work since 2001." "i_work_since_2001_wrong.mp3" "$ARTHUR"
generate "I have worked here since 2001." "i_have_worked_here_since_2001.mp3" "$ELLEN"

# -----------------------------------------------
# ORDERING EXERCISE
# -----------------------------------------------
echo ""
echo "=== Ordering Exercise (Arthur) ==="
generate "Good morning, everyone. My name is Dr. Rubens Tofolo. I am an endocrinologist from Belem, Brazil. I specialize in diabetes and obesity management. I have been practicing for over twenty-five years. My background includes research in the United States and France. I currently focus on metabolic syndrome, and I am here to reactivate my English fluency for international conferences." "order_l1_self_introduction.mp3" "$ARTHUR"

echo ""
echo "============================================"
echo "=== SUMMARY ==="
echo "============================================"
echo "Total entries:  $TOTAL"
echo "Generated:      $GENERATED"
echo "Skipped:        $SKIPPED"
echo "Errors:         $ERRORS"
echo ""
echo "Output dir: $OUT_DIR"
echo ""

if [ $ERRORS -gt 0 ]; then
  echo "WARNING: $ERRORS files had errors. Re-run the script to retry."
  exit 1
fi

echo "Done! All audio files generated successfully."
