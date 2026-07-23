#!/usr/bin/env bash
# scope-guard.sh — trava de escopo de modelo (PreToolUse Edit|Write).
# Lê o JSON da tool call em stdin, olha .claude/scope.lock e BLOQUEIA (exit 2)
# edições fora do escopo ativo. Sem lock => não bloqueia nada.
#
#   .claude/scope.lock = "kids-teens"  -> proíbe editar material ADULTO
#   .claude/scope.lock = "adulto"      -> proíbe editar KIDS/TEENS
#
# Escopos por caminho:
#   KIDS/TEENS = bento | theo | word-arena | kids | teens (arquivos e assets)
#   MATERIAL   = public/professor|aluno|audio/...  (HTML/áudio de aluno)
# Infra compartilhada (scripts, css, lib, catálogo, docs, .claude, builder) fica
# sempre editável — a trava é só sobre o MATERIAL do outro modelo.
set -euo pipefail

INPUT="$(cat)"
FILE="$(printf '%s' "$INPUT" | jq -r '.tool_input.file_path // ""' 2>/dev/null || echo "")"
[ -n "$FILE" ] || exit 0

ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
LOCK="$ROOT/.claude/scope.lock"
[ -f "$LOCK" ] || exit 0
MODE="$(tr -d '[:space:]' < "$LOCK" 2>/dev/null || echo "")"
[ -n "$MODE" ] || exit 0

# só arquivos deste repo importam
case "$FILE" in
  *alumni-plano-gerador*) : ;;
  *) exit 0 ;;
esac

KT='(bento|theo|word-arena|kids|teens)'
MATERIAL='public/(professor|aluno|audio)/'

is_kt()       { printf '%s' "$FILE" | grep -Eiq "$KT"; }
is_material() { printf '%s' "$FILE" | grep -Eq  "$MATERIAL"; }

block() {
  echo "🚫 SCOPE-LOCK ($MODE) — edição BLOQUEADA: $FILE" >&2
  echo "   $1" >&2
  echo "   Trocar de modo: /kids-teens ou /adulto · destravar: /escopo-livre" >&2
  exit 2
}

if [ "$MODE" = "kids-teens" ]; then
  # proíbe material que NÃO seja kids/teens (= adulto e outros alunos)
  if is_material && ! is_kt; then
    block "Modo kids-teens: proibido tocar em material ADULTO (helen-mendes e alunos adultos)."
  fi
elif [ "$MODE" = "adulto" ]; then
  # proíbe qualquer arquivo kids/teens
  if is_kt; then
    block "Modo adulto: proibido tocar em KIDS/TEENS (bento, theo, word-arena, kids*, teens*)."
  fi
fi
exit 0
