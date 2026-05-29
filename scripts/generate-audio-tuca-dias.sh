#!/bin/bash
# Generate all ElevenLabs audio files for Tuca Dias
# Usage: ./scripts/generate-audio-tuca-dias.sh YOUR_API_KEY
# Or:    ELEVENLABS_API_KEY=sk-xxx ./scripts/generate-audio-tuca-dias.sh

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
node scripts/generate-audio-tuca-dias.js
