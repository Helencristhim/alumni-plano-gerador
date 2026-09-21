#!/bin/bash
# BUILD DA VERCEL — cadeia unica de gates + limpeza de disco.
#
# POR QUE ISTO EXISTE (21/09/2026)
# --------------------------------
# A cadeia morava inteira dentro do "buildCommand" do vercel.json. A Vercel limita
# esse campo a 256 caracteres e a cadeia ja estava em 235: o passo novo de liberar
# disco estourou o limite e a Vercel recusou o deploy antes de qualquer build
# ("`buildCommand` should NOT be longer than 256 characters"). A cadeia passou a
# morar aqui, e o vercel.json so chama este arquivo.
#
# A SEMANTICA E EXATAMENTE A DE ANTES, passo por passo:
#   - check_deploy_source.py  -> BLOQUEANTE. Se reprovar, o deploy NAO sai (REGRA 19,
#     e a trava que existe por causa da producao que voltou para maio em 03/08/2026).
#   - os demais gates          -> avisam, nunca derrubam deploy ("|| true", como antes).
#   - libera_disco_build.py    -> ULTIMO, de proposito: check_lesson_integrity.py
#     consulta `git ls-files`, e este passo apaga o .git efemero do container.
set -u

python3 scripts/check_deploy_source.py || exit 1

node scripts/build-lesson-counts.js    || true
python3 scripts/build_anatomias.py     || true
python3 scripts/check_lesson_integrity.py || true
node scripts/check_audiomap_syntax.js  || true

python3 scripts/libera_disco_build.py  || true

exit 0
