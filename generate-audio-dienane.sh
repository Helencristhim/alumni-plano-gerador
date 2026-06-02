#!/bin/bash
# Generate ElevenLabs audio for Dienane Brandão de Mesquita
# Voices: Arthur (sfJopaWaOtauCD3HKX6Q) = male, Ellen (BIvP0GN1cAtSRTxNHnWS) = female

API_KEY="$ELEVENLABS_API_KEY"
ARTHUR="sfJopaWaOtauCD3HKX6Q"
ELLEN="BIvP0GN1cAtSRTxNHnWS"
OUT_DIR="public/audio/dienane-brandao-de-mesquita"
MODEL="eleven_multilingual_v2"

mkdir -p "$OUT_DIR"

generate() {
  local text="$1"
  local filename="$2"
  local voice="$3"
  local filepath="$OUT_DIR/$filename"

  if [ -f "$filepath" ]; then
    echo "SKIP: $filename (exists)"
    return
  fi

  echo "GEN: $filename ($text)"
  curl -s -X POST "https://api.elevenlabs.io/v1/text-to-speech/$voice" \
    -H "xi-api-key: $API_KEY" \
    -H "Content-Type: application/json" \
    -d "{\"text\":\"$text\",\"model_id\":\"$MODEL\",\"voice_settings\":{\"stability\":0.5,\"similarity_boost\":0.75,\"style\":0.0,\"use_speaker_boost\":true}}" \
    --output "$filepath"

  # Check if file is valid (not an error JSON)
  if [ -f "$filepath" ] && [ $(wc -c < "$filepath") -lt 200 ]; then
    echo "  WARNING: File too small, may be error"
    cat "$filepath"
    echo ""
  fi

  sleep 0.3
}

echo "=== Generating audio for Dienane Brandão de Mesquita ==="
echo "=== Single words (Ellen - female student) ==="
generate "Name" "name.mp3" "$ELLEN"
generate "Age" "age.mp3" "$ELLEN"
generate "City" "city.mp3" "$ELLEN"
generate "Job" "job.mp3" "$ELLEN"
generate "Live" "live.mp3" "$ELLEN"
generate "Company" "company.mp3" "$ELLEN"
generate "Family" "family.mp3" "$ELLEN"
generate "Manager" "manager.mp3" "$ELLEN"

echo "=== Vocab examples (Ellen) ==="
generate "My name is Dienane." "my_name_is_dienane.mp3" "$ELLEN"
generate "I am 50 years old." "i_am_50_years_old.mp3" "$ELLEN"
generate "Altamira is my city." "altamira_is_my_city.mp3" "$ELLEN"
generate "My job is in Human Resources." "my_job_is_in_human_resources.mp3" "$ELLEN"
generate "I live in Altamira, Pará." "i_live_in_altamira_para.mp3" "$ELLEN"
generate "I work at a big company." "i_work_at_a_big_company.mp3" "$ELLEN"
generate "My family is in Belém." "my_family_is_in_belem.mp3" "$ELLEN"
generate "She is the HR manager." "she_is_the_hr_manager.mp3" "$ELLEN"

echo "=== Expressions (Ellen) ==="
generate "My name is Dienane. I am from Altamira." "my_name_is_dienane_i_am_from_altamira.mp3" "$ELLEN"
generate "I work in Human Resources." "i_work_in_human_resources.mp3" "$ELLEN"
generate "Nice to meet you." "nice_to_meet_you.mp3" "$ELLEN"
generate "Could you speak slowly, please?" "could_you_speak_slowly_please.mp3" "$ELLEN"
generate "How do you say that in English?" "how_do_you_say_that_in_english.mp3" "$ELLEN"
generate "I don't understand." "i_dont_understand.mp3" "$ELLEN"

echo "=== Grammar examples (alternating) ==="
generate "I am Dienane. I am from Altamira." "i_am_dienane_i_am_from_altamira.mp3" "$ELLEN"
generate "She is a manager. Her company is big." "she_is_a_manager_her_company_is_big.mp3" "$ARTHUR"
generate "We are colleagues. They are from Belém." "we_are_colleagues_they_are_from_belem.mp3" "$ARTHUR"
generate "My family is in Belém. The city is beautiful." "my_family_is_in_belem_the_city_is_beautiful.mp3" "$ELLEN"

echo "=== Fill-in phrases (Ellen) ==="
generate "I am from Altamira." "i_am_from_altamira.mp3" "$ELLEN"
generate "She is a manager." "she_is_a_manager.mp3" "$ELLEN"
generate "We are colleagues." "we_are_colleagues.mp3" "$ELLEN"

echo "=== Dialogue — Marco lines (Arthur) ==="
generate "Hi! Are you here for the training?" "hi_are_you_here_for_the_training.mp3" "$ARTHUR"
generate "Nice to meet you! I am Marco. Where are you from?" "nice_to_meet_you_i_am_marco_where_are_you_from.mp3" "$ARTHUR"
generate "I am from São Paulo. What is your job?" "i_am_from_sao_paulo_what_is_your_job.mp3" "$ARTHUR"
generate "Interesting! Is your company big?" "interesting_is_your_company_big.mp3" "$ARTHUR"

echo "=== Dialogue — Dienane lines (Ellen) ==="
generate "Yes! My name is Dienane. Nice to meet you." "yes_my_name_is_dienane_nice_to_meet_you.mp3" "$ELLEN"
generate "I am from Altamira, in Pará. And you?" "i_am_from_altamira_in_para_and_you.mp3" "$ELLEN"
generate "I work in Human Resources. I am a manager." "i_work_in_human_resources_i_am_a_manager.mp3" "$ELLEN"
generate "Yes, it is a very big company. My family is in Belém, but I live in Altamira for work." "yes_it_is_a_very_big_company_my_family_is_in_bele.mp3" "$ELLEN"

echo "=== Additional phrases ==="
generate "I am from Altamira, Pará." "i_am_from_altamira_para.mp3" "$ELLEN"
generate "I am Dienane." "i_am_dienane.mp3" "$ELLEN"
generate "My name is Dienane. Nice to meet you." "my_name_is_dienane_nice_to_meet_you.mp3" "$ELLEN"
generate "She is from Belém." "she_is_from_belem.mp3" "$ARTHUR"
generate "We are managers." "we_are_managers.mp3" "$ARTHUR"
generate "You are my teacher." "you_are_my_teacher.mp3" "$ARTHUR"
generate "It is a big company." "it_is_a_big_company.mp3" "$ARTHUR"
generate "They are from Belém." "they_are_from_belem.mp3" "$ARTHUR"
generate "Hi, I am Dienane. I work in HR at a big company." "hi_i_am_dienane_i_work_in_hr_at_a_big_company.mp3" "$ELLEN"
generate "I am a manager. I work in Human Resources." "i_am_a_manager_i_work_in_human_resources.mp3" "$ELLEN"
generate "My company is big." "my_company_is_big.mp3" "$ELLEN"
generate "I work in HR." "i_work_in_hr.mp3" "$ELLEN"

echo "=== Listening passages ==="
generate "Good morning, everyone. My name is Carlos. I am 45 years old. I am from Brasília. I work at a technology company. I am a project manager. My team has 10 people. Nice to meet you all." "listening1_office_intro.mp3" "$ARTHUR"
generate "Hello. My name is Ana. I am the new HR manager. I am from Recife, but I live in Brasília now. I am 38 years old. I have a small family. My husband and two children. I am very happy to be here." "listening2_hr_intro.mp3" "$ELLEN"

echo "=== DONE ==="
echo "Total files:"
ls -1 "$OUT_DIR"/*.mp3 2>/dev/null | wc -l
