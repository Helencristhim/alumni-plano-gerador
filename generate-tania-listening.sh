#!/bin/bash
set -e

API_KEY="$ELEVENLABS_API_KEY"
VOICE_ID="BIvP0GN1cAtSRTxNHnWS"  # Ellen (female - Tania is protagonist)
BASE_DIR="/Users/helenmendes/alumni-plano-gerador/public/audio"

generate_audio() {
    local text="$1"
    local output_dir="$2"
    local aula_name="$3"

    echo "Generating audio for $aula_name..."

    # Create directory if needed
    mkdir -p "$output_dir"

    # Generate with ElevenLabs
    curl -s -X POST "https://api.elevenlabs.io/v1/text-to-speech/${VOICE_ID}" \
        -H "xi-api-key: ${API_KEY}" \
        -H "Content-Type: application/json" \
        -d "{
            \"text\": $(echo "$text" | python3 -c 'import json,sys; print(json.dumps(sys.stdin.read()))'),
            \"model_id\": \"eleven_turbo_v2_5\",
            \"voice_settings\": {
                \"stability\": 0.5,
                \"similarity_boost\": 0.75
            }
        }" \
        --output "${output_dir}/listening_1.mp3"

    # Copy as listening_2.mp3
    cp "${output_dir}/listening_1.mp3" "${output_dir}/listening_2.mp3"

    echo "Done: $aula_name ($(du -h "${output_dir}/listening_1.mp3" | cut -f1))"
}

# AULA 2 - Airport Check-in
TEXT_AULA2="Agent: Good morning! Welcome to International Airlines. Could I see your passport, please?
Tania: Good morning! Here is my passport. I am flying to Paris.
Agent: Thank you, Mrs. Rosa. Could I see your booking confirmation?
Tania: Yes, here it is. Could I have a window seat, please?
Agent: Of course! I have seat 14A for you. Are you checking any luggage today?
Tania: Yes, I have one suitcase. How much luggage can I take?
Agent: You can check one bag up to 23 kilos. Could I see your luggage?
Tania: Here it is. Could you tell me where my gate is?
Agent: Your gate is B7. Departure is at 3:30 PM. Here is your boarding pass.
Tania: Thank you very much! Could you tell me where Terminal B is?"

generate_audio "$TEXT_AULA2" "${BASE_DIR}/tania-rosa-aula2" "aula2"

# AULA 3 - Hotel Check-in
TEXT_AULA3="Receptionist: Good evening! Welcome to the Grand Palace Hotel. How can I help you?
Tania: Good evening! I have a reservation under the name Tania Rosa.
Receptionist: Let me check. Yes, Mrs. Rosa! A double room for three nights. Is that correct?
Tania: Yes, that is correct. I would like a room with a view, if possible.
Receptionist: Of course! Room 405 on the fourth floor has a lovely city view. Would you like breakfast included?
Tania: Yes, I would. What time is breakfast served?
Receptionist: Breakfast is from 7 to 10 AM in the restaurant on the first floor.
Tania: That sounds perfect. What time is checkout?
Receptionist: Checkout is at 11 AM. Here is your room key. The elevator is on your right.
Tania: Thank you very much! Could you also recommend a good restaurant nearby?"

generate_audio "$TEXT_AULA3" "${BASE_DIR}/tania-rosa-aula3" "aula3"

# AULA 4 - Directions
TEXT_AULA4="Tania: Excuse me, could you help me? I am looking for the Art Museum.
Local: Of course! The Art Museum is not far from here.
Tania: How do I get there?
Local: Go straight on this street for two blocks.
Tania: Two blocks. And then?
Local: Then turn left at the corner. You will see a big bridge.
Tania: Turn left at the corner, near the bridge. Got it.
Local: The museum is across from the bridge, next to a cafe.
Tania: Across from the bridge, next to a cafe. Is it far to walk?
Local: No, about ten minutes. You can also take the subway. The station is on the next block."

generate_audio "$TEXT_AULA4" "${BASE_DIR}/tania-rosa-aula4" "aula4"

# AULA 6 - Shopping
TEXT_AULA6="Tania: Good afternoon! I am looking for souvenirs for my family.
Shopkeeper: Welcome! We have scarves, bags, and handmade jewelry. What are you looking for?
Tania: I love that blue scarf. How much is it?
Shopkeeper: That one is thirty-five euros.
Tania: And the red one? Is it cheaper?
Shopkeeper: The red one is twenty-eight euros. It is smaller, but very popular.
Tania: I would like both. Is there a discount if I buy two?
Shopkeeper: Yes! If you buy two, the total is fifty-five euros instead of sixty-three.
Tania: That is a good deal! Could I pay with a credit card?
Shopkeeper: Of course! Here is your receipt. Would you like a bag?"

generate_audio "$TEXT_AULA6" "${BASE_DIR}/tania-rosa-aula6" "aula6"

# AULA 7 - Cultural Conversation
TEXT_AULA7="Marco: You are Brazilian, right? I love Brazil! Have you ever been to Italy?
Tania: Yes, I have! I have been to Rome and Florence. The monuments are incredible.
Marco: What did you like most about Italy?
Tania: I loved the traditions and the food. Every region has different customs.
Marco: That is true! Have you visited any festivals in your travels?
Tania: Yes, I have been to a music festival in Spain. It was an amazing experience.
Marco: Spain is wonderful! I have never been to South America. What is Brazil like?
Tania: Brazil has incredible diversity, different cultures, languages, and traditions in every region.
Marco: That sounds fascinating! What landmarks should I visit?
Tania: You should visit Rio de Janeiro, the Amazon, and Salvador. Brazil has a very rich heritage."

generate_audio "$TEXT_AULA7" "${BASE_DIR}/tania-rosa-aula7" "aula7"

echo ""
echo "=== VERIFICATION ==="
for aula in aula2 aula3 aula4 aula6 aula7; do
    for f in listening_1.mp3 listening_2.mp3; do
        filepath="${BASE_DIR}/tania-rosa-${aula}/${f}"
        if [ -f "$filepath" ]; then
            size=$(stat -f%z "$filepath" 2>/dev/null || stat -c%s "$filepath" 2>/dev/null)
            if [ "$size" -gt 50000 ]; then
                echo "OK: tania-rosa-${aula}/${f} — ${size} bytes"
            else
                echo "WARNING (small): tania-rosa-${aula}/${f} — ${size} bytes"
            fi
        else
            echo "MISSING: tania-rosa-${aula}/${f}"
        fi
    done
done
