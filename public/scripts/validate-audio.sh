#!/bin/bash
# ═══════════════════════════════════════════════════════════════
# ALUMNI BY BETTER — Audio Validation Script
# Validates audio assets for a given student profile.
#
# Usage: ./validate-audio.sh <perfilId>
# Example: ./validate-audio.sh maisa
# ═══════════════════════════════════════════════════════════════

set -euo pipefail

if [ $# -lt 1 ]; then
  echo "Usage: $0 <perfilId>"
  echo "Example: $0 maisa"
  exit 1
fi

PERFIL_ID="$1"
BASE_DIR="$(cd "$(dirname "$0")/.." && pwd)"
PASS=true

echo "═══════════════════════════════════════════"
echo " Audio Validation: ${PERFIL_ID}"
echo "═══════════════════════════════════════════"
echo ""

# 1. Count audioMap entries in the professor HTML
PROF_FILE="${BASE_DIR}/${PERFIL_ID}-professor.html"
if [ -f "$PROF_FILE" ]; then
  AUDIOMAP_ENTRIES=$(grep -o '"[^"]*\.mp3"' "$PROF_FILE" 2>/dev/null | wc -l | tr -d ' ')
  echo "[1] audioMap entries in professor HTML: ${AUDIOMAP_ENTRIES}"
else
  AUDIOMAP_ENTRIES=0
  echo "[1] Professor HTML not found: ${PROF_FILE}"
  PASS=false
fi

# 2. Count MP3 files in /public/audio/{perfilId}/
AUDIO_DIR="${BASE_DIR}/audio/${PERFIL_ID}"
if [ -d "$AUDIO_DIR" ]; then
  MP3_COUNT=$(find "$AUDIO_DIR" -name "*.mp3" -type f 2>/dev/null | wc -l | tr -d ' ')
  echo "[2] MP3 files in ${AUDIO_DIR}: ${MP3_COUNT}"
else
  MP3_COUNT=0
  echo "[2] Audio directory not found: ${AUDIO_DIR}"
fi

# 3. Count speakText() calls in both HTMLs
ALUNO_FILE="${BASE_DIR}/${PERFIL_ID}-aluno.html"
SPEAK_PROF=0
SPEAK_ALUNO=0

if [ -f "$PROF_FILE" ]; then
  SPEAK_PROF=$(grep -o 'speakText(' "$PROF_FILE" 2>/dev/null | wc -l | tr -d ' ')
fi
if [ -f "$ALUNO_FILE" ]; then
  SPEAK_ALUNO=$(grep -o 'speakText(' "$ALUNO_FILE" 2>/dev/null | wc -l | tr -d ' ')
fi
SPEAK_TOTAL=$((SPEAK_PROF + SPEAK_ALUNO))
echo "[3] speakText() calls — professor: ${SPEAK_PROF}, aluno: ${SPEAK_ALUNO}, total: ${SPEAK_TOTAL}"

# 4. Report
echo ""
echo "───────────────────────────────────────────"

if [ "$AUDIOMAP_ENTRIES" -gt 0 ] && [ "$MP3_COUNT" -gt 0 ] && [ "$SPEAK_TOTAL" -gt 0 ]; then
  if [ "$MP3_COUNT" -ge "$AUDIOMAP_ENTRIES" ]; then
    echo "RESULT: PASS"
    echo "All ${MP3_COUNT} MP3 files present for ${AUDIOMAP_ENTRIES} audioMap entries."
  else
    echo "RESULT: FAIL"
    echo "MP3 files (${MP3_COUNT}) < audioMap entries (${AUDIOMAP_ENTRIES}). Missing audio files."
    PASS=false
  fi
else
  echo "RESULT: FAIL"
  if [ "$AUDIOMAP_ENTRIES" -eq 0 ]; then echo "  - No audioMap entries found in professor HTML."; fi
  if [ "$MP3_COUNT" -eq 0 ]; then echo "  - No MP3 files found in audio directory."; fi
  if [ "$SPEAK_TOTAL" -eq 0 ]; then echo "  - No speakText() calls found in either HTML."; fi
  PASS=false
fi

echo "───────────────────────────────────────────"

if [ "$PASS" = true ]; then
  exit 0
else
  exit 1
fi
