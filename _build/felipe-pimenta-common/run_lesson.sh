#!/usr/bin/env bash
# Pipeline de UMA aula do Felipe: gera -> builda -> audio -> hub -> TODOS os gates.
# Uso (da raiz do repo):  bash _build/felipe-pimenta-common/run_lesson.sh N
# Sai != 0 se qualquer gate bloqueante falhar. NAO commita: o commit e manual.
set -uo pipefail
N="$1"
SLUG=felipe-pimenta
export PATH="$HOME/.nvm/versions/node/v24.18.0/bin:$PATH"
PROF="public/professor/${SLUG}-aula${N}.html"
ALU="public/aluno/${SLUG}-aula${N}.html"
HUBP="public/professor/${SLUG}.html"
HUBA="public/aluno/${SLUG}.html"
F="$PROF $ALU $HUBP $HUBA"
fail=0
step() { echo ""; echo "───── $* ─────"; }

step "1. gerar conteudo"
python3 "_build/${SLUG}-aula${N}/gen.py" || exit 1

step "2. builder (modelo helen-mendes)"
python3 _build/model/build_from_model.py "_build/${SLUG}-aula${N}/config.json" >/dev/null || exit 1
echo "ok: $PROF + $ALU"

step "3. audio ElevenLabs"
ELEVENLABS_API_KEY="$(cat /home/dan/dev/work/better/.elevenlabs_key)" \
  python3 _build/model/gen_audio.py "_build/${SLUG}-aula${N}/config.json" 2>&1 | tail -1 || exit 1

step "4. GATE qualidade de audio (mp3 podre)"
python3 _build/model/check_audio_quality.py "_build/${SLUG}-aula${N}/config.json" 2>&1 | tail -1

step "5. insert_hub (aditivo)"
python3 _build/model/insert_hub.py "_build/${SLUG}-aula${N}/config.json" >/dev/null || exit 1
echo "ok: hub prof + aluno"

step "GATES BLOQUEANTES"
node scripts/check_inline_js.mjs --base origin/main $F 2>&1 | grep -E "handlers mortos|OK —|MORTO" || fail=1
python3 _build/model/validate_lesson.py "$PROF" "$ALU" 2>&1 | tail -1 | grep -q "TODOS PASSARAM" \
  && echo "validate_lesson    : PASS" || { echo "validate_lesson    : FAIL"; python3 _build/model/validate_lesson.py "$PROF" "$ALU" 2>&1 | grep '✗'; fail=1; }
python3 _build/model/check_vocab_progression.py "$HUBP" 2>&1 | grep -qE "^✅ PASS" \
  && echo "vocab_progression  : PASS (REGRA 22)" || { echo "vocab_progression  : FAIL"; fail=1; }
python3 _build/model/check_preclass_coherence.py "$HUBP" 2>&1 | grep -qE "^OK" \
  && echo "preclass_coherence : PASS (REGRA 29)" || { echo "preclass_coherence : FAIL"; fail=1; }
python3 _build/model/audit_hubs_struct.py --check "$HUBP" "$HUBA" 2>&1 | grep -q "todos limpos" \
  && echo "hubs_struct        : LIMPO" || { echo "hubs_struct        : DEFEITO"; fail=1; }
python3 _build/model/check_inclass_patterns.py "$PROF" 2>&1 | grep -q "^OK" \
  && echo "inclass_patterns   : PASS" || { echo "inclass_patterns   : FAIL"; fail=1; }
python3 _build/model/check_contrast.py $F >/dev/null 2>&1 \
  && echo "contrast           : PASS" || { echo "contrast           : FAIL"; fail=1; }
python3 scripts/check_lesson_integrity.py $F 2>&1 | tail -1

echo ""
if [ "$fail" -eq 0 ]; then echo "✅ AULA $N — TODOS OS GATES VERDES"; else echo "❌ AULA $N — GATE VERMELHO"; fi
exit $fail
