#!/bin/bash
API_KEY="$ELEVENLABS_API_KEY"
ARTHUR="sfJopaWaOtauCD3HKX6Q"
ELLEN="BIvP0GN1cAtSRTxNHnWS"
OUT_DIR="public/audio/dienane-brandao-de-mesquita"
MODEL="eleven_multilingual_v2"

generate() {
  local text="$1"; local filename="$2"; local voice="$3"
  local filepath="$OUT_DIR/$filename"
  if [ -f "$filepath" ]; then echo "SKIP: $filename"; return; fi
  echo "GEN: $filename"
  curl -s -X POST "https://api.elevenlabs.io/v1/text-to-speech/$voice" \
    -H "xi-api-key: $API_KEY" -H "Content-Type: application/json" \
    -d "{\"text\":\"$text\",\"model_id\":\"$MODEL\",\"voice_settings\":{\"stability\":0.5,\"similarity_boost\":0.75,\"style\":0.0,\"use_speaker_boost\":true}}" \
    --output "$filepath"
  sleep 0.3
}

echo "=== AULA 2 AUDIO ==="
# Single words (Ellen)
generate "Wake up" "wake_up.mp3" "$ELLEN"
generate "Morning" "morning.mp3" "$ELLEN"
generate "Breakfast" "breakfast.mp3" "$ELLEN"
generate "Drive" "drive.mp3" "$ELLEN"
generate "Meeting" "meeting.mp3" "$ELLEN"
generate "Lunch" "lunch.mp3" "$ELLEN"
generate "Evening" "evening.mp3" "$ELLEN"
generate "Routine" "routine.mp3" "$ELLEN"

# Vocab examples (Ellen)
generate "I wake up at 5 AM." "i_wake_up_at_5_am.mp3" "$ELLEN"
generate "Every morning, I go to the gym." "every_morning_i_go_to_the_gym.mp3" "$ELLEN"
generate "I have breakfast at 6:30." "i_have_breakfast_at_6_30.mp3" "$ELLEN"
generate "I drive to work every day." "i_drive_to_work_every_day.mp3" "$ELLEN"
generate "I have a meeting at 9 AM." "i_have_a_meeting_at_9_am.mp3" "$ELLEN"
generate "I have lunch at noon." "i_have_lunch_at_noon.mp3" "$ELLEN"
generate "In the evening, I watch TV." "in_the_evening_i_watch_tv.mp3" "$ELLEN"
generate "My routine is very busy." "my_routine_is_very_busy.mp3" "$ELLEN"

# Extended phrases (Ellen)
generate "I wake up at 5 AM every day." "i_wake_up_at_5_am_every_day.mp3" "$ELLEN"
generate "I go to the gym at 6." "i_go_to_the_gym_at_6.mp3" "$ELLEN"
generate "I have breakfast at 6:30. Then I drive to work." "i_have_breakfast_at_6_30_then_i_drive_to_work.mp3" "$ELLEN"
generate "My first meeting is at 9 AM." "my_first_meeting_is_at_9_am.mp3" "$ELLEN"
generate "I have lunch at noon. Then I have more meetings." "i_have_lunch_at_noon_then_i_have_more_meetings.mp3" "$ELLEN"
generate "I finish work at 6 PM." "i_finish_work_at_6_pm.mp3" "$ELLEN"
generate "In the evening, I cook dinner and rest." "in_the_evening_i_cook_dinner_and_rest.mp3" "$ELLEN"
generate "Every day, I exercise in the morning." "every_day_i_exercise_in_the_morning.mp3" "$ELLEN"

# Dialogue - Marco (Arthur)
generate "Good morning, Dienane! You look energetic today." "good_morning_dienane_you_look_energetic_today.mp3" "$ARTHUR"
generate "That is early! What do you do in the morning?" "that_is_early_what_do_you_do_in_the_morning.mp3" "$ARTHUR"
generate "And what time do you start work?" "and_what_time_do_you_start_work.mp3" "$ARTHUR"
generate "When do you have lunch?" "when_do_you_have_lunch.mp3" "$ARTHUR"

# Dialogue - Dienane (Ellen)
generate "Thank you! I wake up at 5 AM every day." "thank_you_i_wake_up_at_5_am_every_day.mp3" "$ELLEN"
generate "I go to the gym at 6. Then I have breakfast." "i_go_to_the_gym_at_6_then_i_have_breakfast.mp3" "$ELLEN"
generate "I drive to work at 7:30. My first meeting is at 9." "i_drive_to_work_at_7_30_my_first_meeting_is_at_9.mp3" "$ELLEN"
generate "I have lunch at noon. And in the evening, I cook dinner." "i_have_lunch_at_noon_and_in_the_evening_i_cook_din.mp3" "$ELLEN"

# Grammar examples (alternating)
generate "She wakes up at 5 AM." "she_wakes_up_at_5_am.mp3" "$ARTHUR"
generate "He drives to work." "he_drives_to_work.mp3" "$ARTHUR"
generate "She has lunch at noon." "she_has_lunch_at_noon.mp3" "$ELLEN"

# Listening passages
generate "My name is Pedro. I am a manager. Every morning, I wake up at 6 AM. I have breakfast with my family. Then I drive to work. I start at 8. I have many meetings in the morning. I have lunch at 1 PM. In the evening, I go home and cook dinner. I sleep at 11 PM." "listening2_1_pedro_routine.mp3" "$ARTHUR"
generate "Hi, I am Ana from HR. My routine is very different! I wake up at 7 AM. I do not have breakfast, just coffee! I take the bus to work. I start at 9. I have lunch at noon with my colleagues. In the evening, I exercise at the gym. Then I have dinner and watch TV. I sleep at 10 PM." "listening2_2_ana_routine.mp3" "$ELLEN"

echo "=== DONE ==="
ls -1 "$OUT_DIR"/*.mp3 | wc -l
