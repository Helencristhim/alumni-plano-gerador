#!/bin/bash
# Generate ElevenLabs MP3 audios for Mark Kazuyoshi Seki Omagari — Aula 3
# Voice assignment: Arthur=Mark/vocab words, Ellen=Jess, Alternate for general sentences

set -e

APIKEY="$ELEVENLABS_API_KEY"
if [ -z "$APIKEY" ]; then
  echo "ERROR: set ELEVENLABS_API_KEY"
  exit 1
fi

DIR="/Users/helenmendes/alumni-plano-gerador/public/audio/mark-kazuyoshi-seki-omagari"
ARTHUR="sfJopaWaOtauCD3HKX6Q"
ELLEN="BIvP0GN1cAtSRTxNHnWS"

generate() {
  local VOICE_ID="$1"
  local TEXT="$2"
  local FILENAME="$3"
  local FILEPATH="$DIR/$FILENAME"

  if [ -f "$FILEPATH" ] && [ "$(wc -c < "$FILEPATH")" -gt 1000 ]; then
    echo "SKIP (exists): $FILENAME"
    return 0
  fi

  echo "Generating: $FILENAME ($([ "$VOICE_ID" = "$ARTHUR" ] && echo 'Arthur' || echo 'Ellen'))"
  curl -s "https://api.elevenlabs.io/v1/text-to-speech/$VOICE_ID" \
    -H "xi-api-key: $APIKEY" \
    -H "Content-Type: application/json" \
    -d "{\"text\":\"$TEXT\",\"model_id\":\"eleven_multilingual_v2\",\"voice_settings\":{\"stability\":0.5,\"similarity_boost\":0.75}}" \
    --output "$FILEPATH"

  local SIZE=$(wc -c < "$FILEPATH")
  if [ "$SIZE" -lt 1000 ]; then
    echo "WARNING: $FILENAME is only $SIZE bytes!"
    cat "$FILEPATH"
    echo ""
  else
    echo "OK: $FILENAME ($SIZE bytes)"
  fi
}

echo "===== BATCH 1: Vocab Words (Arthur) ====="
generate "$ARTHUR" "Family" "family.mp3"
generate "$ARTHUR" "Brother" "brother.mp3"
generate "$ARTHUR" "Sister" "sister.mp3"
generate "$ARTHUR" "Parent" "parent.mp3"
generate "$ARTHUR" "Cousin" "cousin.mp3"
sleep 2

echo ""
echo "===== BATCH 2: Vocab Words (Arthur) ====="
generate "$ARTHUR" "Pet" "pet.mp3"
generate "$ARTHUR" "Bedroom" "bedroom.mp3"
generate "$ARTHUR" "Living room" "living_room.mp3"
generate "$ARTHUR" "my" "my.mp3"
generate "$ARTHUR" "his" "his.mp3"
sleep 2

echo ""
echo "===== BATCH 3: Vocab Words + Context (Arthur/Ellen alternating) ====="
generate "$ARTHUR" "our" "our.mp3"
generate "$ARTHUR" "their" "their.mp3"
generate "$ARTHUR" "My family has four people: my mom, my dad, my brother, and me." "my_family_has_four_people_my_mom_my_dad_my_brother_and_me.mp3"
generate "$ELLEN" "His name is Lucas and he is ten years old." "his_name_is_lucas_and_he_is_ten_years_old.mp3"
generate "$ARTHUR" "Our house has three bedrooms and a living room." "our_house_has_three_bedrooms_and_a_living_room.mp3"
sleep 2

echo ""
echo "===== BATCH 4: Context Sentences (alternating) ====="
generate "$ELLEN" "His brother is ten years old." "his_brother_is_ten_years_old.mp3"
generate "$ARTHUR" "She has a garden." "she_has_a_garden.mp3"
generate "$ELLEN" "We watch TV in the living room." "we_watch_tv_in_the_living_room.mp3"
generate "$ARTHUR" "Our house has three bedrooms." "our_house_has_three_bedrooms.mp3"
generate "$ELLEN" "I have one brother and his name is Lucas." "i_have_one_brother_and_his_name_is_lucas.mp3"
sleep 2

echo ""
echo "===== BATCH 5: Practice Sentences (Arthur=Mark) ====="
generate "$ARTHUR" "My family has four people." "my_family_has_four_people.mp3"
generate "$ARTHUR" "My pet dog is called Thor." "my_pet_dog_is_called_thor.mp3"
generate "$ARTHUR" "I have one brother." "i_have_one_brother.mp3"
generate "$ARTHUR" "His name is Lucas." "his_name_is_lucas.mp3"
generate "$ARTHUR" "My mom has a garden." "my_mom_has_a_garden.mp3"
sleep 2

echo ""
echo "===== BATCH 6: Practice Sentences (alternating) ====="
generate "$ARTHUR" "My cousin lives in Campinas." "my_cousin_lives_in_campinas.mp3"
generate "$ARTHUR" "We have a pet dog." "we_have_a_pet_dog.mp3"
generate "$ARTHUR" "My bedroom is blue." "my_bedroom_is_blue.mp3"
generate "$ARTHUR" "His name is Thor." "his_name_is_thor.mp3"
generate "$ELLEN" "How many people are in your family?" "how_many_people_are_in_your_family.mp3"
sleep 2

echo ""
echo "===== BATCH 7: Dialogue - Jess lines (Ellen) ====="
generate "$ELLEN" "Hi Mark! Tell me about your family." "hi_mark_tell_me_about_your_family.mp3"
generate "$ELLEN" "Who are they?" "who_are_they.mp3"
generate "$ELLEN" "How old is your brother?" "how_old_is_your_brother.mp3"
generate "$ELLEN" "Do you have a pet?" "do_you_have_a_pet.mp3"
generate "$ELLEN" "That is cool! Do you share a bedroom?" "that_is_cool_do_you_share_a_bedroom.mp3"
sleep 2

echo ""
echo "===== BATCH 8: Dialogue - Mark lines (Arthur) ====="
generate "$ARTHUR" "I have a small family. There are four people." "i_have_a_small_family_there_are_four_people.mp3"
generate "$ARTHUR" "My mom, my dad, my brother Lucas, and me." "my_mom_my_dad_my_brother_lucas_and_me.mp3"
generate "$ARTHUR" "He is ten years old. He likes Minecraft too." "he_is_ten_years_old_he_likes_minecraft_too.mp3"
generate "$ARTHUR" "Yes! We have a dog. His name is Thor." "yes_we_have_a_dog_his_name_is_thor.mp3"
generate "$ARTHUR" "No, our house has three bedrooms. My bedroom is blue." "no_our_house_has_three_bedrooms_my_bedroom_is_blue.mp3"
sleep 2

echo ""
echo "===== BATCH 9: Remaining + Speech Card ====="
generate "$ARTHUR" "My bedroom has blue walls." "my_bedroom_has_blue_walls.mp3"
sleep 2

echo ""
echo "===== BATCH 10: Listening 1 (Arthur - home) ====="
generate "$ARTHUR" "Let me tell you about my home. Our house is in Morumbi, São Paulo. It has three bedrooms, a living room, a kitchen, and a garden. My bedroom has blue walls and a big window. My brother's bedroom is next to mine. The living room is our favorite room. We watch movies there on weekends. My mom's garden has beautiful flowers. Our dog Thor loves to play in the garden." "aula3_listening1_home.mp3"
sleep 2

echo ""
echo "===== BATCH 11: Listening 2 (Arthur - family) ====="
generate "$ARTHUR" "My dad's name is Marcos. He works in an office in São Paulo. He has a car and he drives me to school every morning. My mom's name is Keiko. Her garden is her favorite hobby. She has beautiful flowers — red, yellow, and white. My brother Lucas is ten years old. His favorite game is Minecraft. He plays every day after school. And Thor is our dog. He is three years old. His favorite thing is running in the garden." "aula3_listening2_family.mp3"
sleep 2

echo ""
echo "===== VERIFICATION ====="
AULA3_FILES=(
  family.mp3 brother.mp3 sister.mp3 parent.mp3 cousin.mp3
  pet.mp3 bedroom.mp3 living_room.mp3 my.mp3 his.mp3
  our.mp3 their.mp3
  my_family_has_four_people_my_mom_my_dad_my_brother_and_me.mp3
  his_name_is_lucas_and_he_is_ten_years_old.mp3
  our_house_has_three_bedrooms_and_a_living_room.mp3
  his_brother_is_ten_years_old.mp3
  she_has_a_garden.mp3
  we_watch_tv_in_the_living_room.mp3
  our_house_has_three_bedrooms.mp3
  i_have_one_brother_and_his_name_is_lucas.mp3
  my_family_has_four_people.mp3
  my_pet_dog_is_called_thor.mp3
  i_have_one_brother.mp3
  his_name_is_lucas.mp3
  my_mom_has_a_garden.mp3
  my_cousin_lives_in_campinas.mp3
  we_have_a_pet_dog.mp3
  my_bedroom_is_blue.mp3
  his_name_is_thor.mp3
  how_many_people_are_in_your_family.mp3
  hi_mark_tell_me_about_your_family.mp3
  who_are_they.mp3
  how_old_is_your_brother.mp3
  do_you_have_a_pet.mp3
  that_is_cool_do_you_share_a_bedroom.mp3
  i_have_a_small_family_there_are_four_people.mp3
  my_mom_my_dad_my_brother_lucas_and_me.mp3
  he_is_ten_years_old_he_likes_minecraft_too.mp3
  yes_we_have_a_dog_his_name_is_thor.mp3
  no_our_house_has_three_bedrooms_my_bedroom_is_blue.mp3
  my_bedroom_has_blue_walls.mp3
  aula3_listening1_home.mp3
  aula3_listening2_family.mp3
)

PASS=0
FAIL=0
for f in "${AULA3_FILES[@]}"; do
  FPATH="$DIR/$f"
  if [ -f "$FPATH" ]; then
    SIZE=$(wc -c < "$FPATH")
    if [ "$SIZE" -gt 1000 ]; then
      PASS=$((PASS+1))
    else
      echo "FAIL (too small $SIZE bytes): $f"
      FAIL=$((FAIL+1))
    fi
  else
    echo "FAIL (missing): $f"
    FAIL=$((FAIL+1))
  fi
done

echo ""
echo "===== RESULT: $PASS passed, $FAIL failed out of ${#AULA3_FILES[@]} files ====="
