#!/usr/bin/env bash
# Pipeline de UMA aula do Felipe de Araujo Dias: gera -> builda -> audio -> hub -> GATES.
# Uso (da raiz do repo):  bash _build/felipe-de-araujo-dias-common/run_lesson.sh N
# Sai != 0 se qualquer gate bloqueante falhar. NAO commita: o commit e manual.
set -uo pipefail
N="$1"
SLUG=felipe-de-araujo-dias
D="_build/${SLUG}-aula${N}"
PROF="public/professor/${SLUG}-aula${N}.html"
ALU="public/aluno/${SLUG}-aula${N}.html"
HUBP="public/professor/${SLUG}.html"
HUBA="public/aluno/${SLUG}.html"
F="$PROF $ALU $HUBP $HUBA"
fail=0
step() { echo ""; echo "----- $* -----"; }

step "1. gerar conteudo (1a passada)"
python3 "$D/gen.py" || exit 1

step "2. builder (modelo helen-mendes)"
python3 _build/model/build_from_model.py "$D/config.json" >/dev/null || exit 1

step "3. contar slides do arquivo BUILDADO e regerar o menu_desc"
COUNT=$(python3 - "$PROF" <<'PY'
import re, sys
c = open(sys.argv[1], encoding='utf-8').read()
i, j = c.find('<div class="slides-container"'), c.find('</div><!-- /slides-container -->')
print(len(re.findall(r'<div class="slide ', c[i:j])))
PY
)
echo "slides buildados: $COUNT"
python3 "$D/gen.py" "$COUNT" || exit 1
python3 _build/model/build_from_model.py "$D/config.json" >/dev/null || exit 1
echo "ok: $PROF + $ALU"

step "4. audio ElevenLabs"
python3 _build/model/gen_audio.py "$D/config.json" 2>&1 | tail -1 || exit 1

step "4b. GATE qualidade de audio (mp3 podre)"
python3 _build/model/check_audio_quality.py "$D/config.json" 2>&1 | tail -1

step "5. insert_hub (aditivo)"
python3 _build/model/insert_hub.py "$D/config.json" >/dev/null || exit 1
echo "ok: hub prof + aluno"

step "6. links dos Complementares abrem de verdade"
python3 _build/${SLUG}-common/checklinks.py --files "$D/complementary.html" 2>&1 | tail -4 \
  || { echo "links             : FAIL"; fail=1; }

step "GATES BLOQUEANTES"
node scripts/check_inline_js.mjs --base origin/main $F 2>&1 | grep -E "handlers mortos|OK —|MORTO" || fail=1
python3 _build/model/validate_lesson.py "$PROF" "$ALU" 2>&1 | tail -1 | grep -q "TODOS PASSARAM" \
  && echo "validate_lesson    : PASS" \
  || { echo "validate_lesson    : FAIL"; python3 _build/model/validate_lesson.py "$PROF" "$ALU" 2>&1 | grep '✗'; fail=1; }
python3 _build/model/check_inclass_patterns.py "$PROF" 2>&1 | grep -q "^OK" \
  && echo "inclass_patterns   : PASS" || { echo "inclass_patterns   : FAIL"; fail=1; }
python3 _build/model/check_vocab_progression.py "$HUBP" 2>&1 | grep -qE "^✅ PASS" \
  && echo "vocab_progression  : PASS (REGRA 22)" || { echo "vocab_progression  : FAIL"; fail=1; }
python3 _build/model/check_grammar_progression.py public/professor/${SLUG}-aula*.html 2>&1 | tail -1
python3 _build/model/check_grammar_progression.py public/professor/${SLUG}-aula*.html >/dev/null 2>&1 \
  && echo "grammar_progression: PASS (REGRA 22)" || { echo "grammar_progression: FAIL"; fail=1; }
python3 _build/model/check_preclass_coherence.py "$HUBP" 2>&1 | grep -qE "^OK" \
  && echo "preclass_coherence : PASS (REGRA 29)" || { echo "preclass_coherence : FAIL"; fail=1; }
python3 _build/model/audit_hubs_struct.py --check "$HUBP" "$HUBA" 2>&1 | grep -q "todos limpos" \
  && echo "hubs_struct        : LIMPO" || { echo "hubs_struct        : DEFEITO"; fail=1; }
python3 _build/model/check_contrast.py $F >/dev/null 2>&1 \
  && echo "contrast           : PASS" || { echo "contrast           : FAIL"; fail=1; }
python3 scripts/check_lesson_integrity.py $F 2>&1 | tail -1
python3 scripts/check_lesson_integrity.py $F >/dev/null 2>&1 \
  && echo "lesson_integrity   : PASS" || { echo "lesson_integrity   : FAIL"; fail=1; }
python3 scripts/check_undefined_handlers.py --base origin/main $F >/dev/null 2>&1 \
  && echo "undefined_handlers : PASS" || { echo "undefined_handlers : FAIL"; fail=1; }
python3 scripts/check_forbidden_patterns.py --base origin/main $F >/dev/null 2>&1 \
  && echo "forbidden_patterns : PASS" || { echo "forbidden_patterns : FAIL"; fail=1; }
python3 scripts/check_vocab_reveal.py $F >/dev/null 2>&1 \
  && echo "vocab_reveal       : PASS" || { echo "vocab_reveal       : FAIL"; fail=1; }
python3 scripts/check_order_audio_len.py $F >/dev/null 2>&1 \
  && echo "order_audio_len    : PASS" || { echo "order_audio_len    : FAIL"; fail=1; }
python3 scripts/check_produce_modes.py $F >/dev/null 2>&1 \
  && echo "produce_modes      : PASS" || { echo "produce_modes      : FAIL"; fail=1; }
python3 scripts/check_framework_isolation.py >/dev/null 2>&1 \
  && echo "framework_isolation: PASS" || { echo "framework_isolation: FAIL"; fail=1; }
python3 _build/model/check_no_regression.py --base origin/main "$HUBP" "$HUBA" >/dev/null 2>&1 \
  && echo "no_regression      : PASS" || { echo "no_regression      : FAIL"; fail=1; }
python3 scripts/check_legacy_baseline.py 2>&1 | tail -2

echo ""
if [ "$fail" -eq 0 ]; then echo "AULA $N -- TODOS OS GATES VERDES"; else echo "AULA $N -- GATE VERMELHO"; fi
exit $fail
