#!/usr/bin/env bash
# Bateria de gates por aula do Diogo. Uso: bash _build/diogo-leal-gates.sh N
set -u
N="$1"
export PATH="$HOME/.nvm/versions/node/v24.18.0/bin:$PATH"
cd /home/dan/dev/work/better/wt-diogo-conv

P="public/professor/diogo-leal-aula$N.html"
A="public/aluno/diogo-leal-aula$N.html"
HP="public/professor/diogo-leal.html"
HA="public/aluno/diogo-leal.html"

echo "=== 1. GATE 7 (inline JS / data-speak) ==="
node scripts/check_inline_js.mjs --base origin/main "$P" "$A" "$HP" "$HA" 2>&1 | tail -3

echo "=== 2. validate_lesson (standalone) ==="
python3 _build/model/validate_lesson.py "$P" "$A" 2>&1 | tail -3

echo "=== 3. validate_lesson (HUB) — criterio: nao piorou vs origin/main ==="
# baseline tem de rodar NO MESMO caminho (o validador so faz os checks de hub/mp3 se achar o repo)
TMP=$(mktemp -d)
cp "$HP" "$TMP/prof.now" ; cp "$HA" "$TMP/aluno.now"
git show origin/main:"$HP" > "$HP" ; git show origin/main:"$HA" > "$HA"
python3 _build/model/validate_lesson.py "$HP" "$HA" 2>&1 | grep -E '✗' | sed -E 's/\(ex:.*//; s/\(pos [0-9]+\).*//; s/[0-9]+ MP3/N MP3/' | sort | uniq -c > "$TMP/base.txt"
cp "$TMP/prof.now" "$HP" ; cp "$TMP/aluno.now" "$HA"
python3 _build/model/validate_lesson.py "$HP" "$HA" 2>&1 | grep -E '✗' | sed -E 's/\(ex:.*//; s/\(pos [0-9]+\).*//; s/[0-9]+ MP3/N MP3/' | sort | uniq -c > "$TMP/now.txt"
echo "  categorias de achado — base: $(wc -l < "$TMP/base.txt") | agora: $(wc -l < "$TMP/now.txt")"
if diff -q "$TMP/base.txt" "$TMP/now.txt" > /dev/null; then
  echo "  ✅ hub: achados IDENTICOS a base (todos legado; nenhum novo)"
else
  echo "  ⚠️  DIFERENCA vs base:"; diff "$TMP/base.txt" "$TMP/now.txt"
fi
rm -rf "$TMP"

echo "=== 4. check_vocab_progression (REGRA 22) ==="
python3 _build/model/check_vocab_progression.py "$HP" 2>&1 | tail -2

echo "=== 5. check_preclass_coherence (REGRA 29) ==="
python3 _build/model/check_preclass_coherence.py "$HP" 2>&1 | tail -2

echo "=== 6. audit_hubs_struct ==="
python3 /home/dan/dev/work/better/audit_hubs_struct.py --check "$HP" "$HA" 2>&1 | tail -3

echo "=== 7. check_no_regression ==="
python3 _build/model/check_no_regression.py --base origin/main "$P" "$A" "$HP" "$HA" 2>&1 | tail -4

echo "=== 8. check_order_audio ==="
python3 _build/model/check_order_audio.py HEAD diogo-leal 2>&1 | tail -2; echo "  exit=$?"

echo "=== 9. check_lesson_integrity (so diogo) ==="
python3 scripts/check_lesson_integrity.py 2>&1 | grep -i diogo | head -3; echo "  (vazio = OK)"

echo "=== 10. check_audio_quality ==="
python3 _build/model/check_audio_quality.py public/audio/diogo-leal 2>&1 | tail -1

echo "=== 11. contraste (aula N vs baseline do modelo) ==="
python3 _build/model/check_contrast.py "$P" 2>&1 | tail -1
