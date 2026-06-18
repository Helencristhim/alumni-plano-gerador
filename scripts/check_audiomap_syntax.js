#!/usr/bin/env node
/*
 * check_audiomap_syntax.js — TRAVA DE DEPLOY (sintaxe de áudio).
 *
 * Varre os materiais publicados (public/aluno + public/professor) e FALHA
 * (exit 1) se QUALQUER bloco <script> de áudio tiver erro de sintaxe JS.
 *
 * Motivo: um erro de sintaxe no objeto `audioMap` (ex: vírgula faltando entre
 * entradas) faz `var audioMap` virar undefined no navegador. Aí TODO clique em
 * `speakText()` lança TypeError e NENHUM áudio toca — nem o fallback de TTS.
 * O check_lesson_integrity.py pega MP3 faltando, mas NÃO pega audioMap mal
 * formado (o arquivo .mp3 existe; o que quebra é o JS). Este gate fecha essa
 * brecha. Incidente 18/06/2026: Pelizaro + 6 alunos com áudio mudo em produção.
 *
 * Usa o próprio parser do Node (vm.Script só COMPILA, não executa) — mesma
 * gramática do navegador, então zero falso-positivo com sintaxe moderna
 * (optional chaining `?.`, nullish `??`, etc.).
 *
 * Uso:
 *   node scripts/check_audiomap_syntax.js              # varre tudo (gate de build)
 *   node scripts/check_audiomap_syntax.js a.html b.html  # varre só os dados
 */
'use strict';
const fs = require('fs');
const path = require('path');
const vm = require('vm');

const ROOT = path.resolve(__dirname, '..');
const DIRS = ['public/aluno', 'public/professor'];

// Mesmos arquivos ignorados pelo check_lesson_integrity.py (não servidos a aluno).
function isIgnored(file) {
  const b = path.basename(file).toLowerCase();
  return b.includes('backup') || b.includes('teste') || b.includes('.bak');
}

function listFiles() {
  const args = process.argv.slice(2);
  if (args.length) return args;
  const out = [];
  for (const d of DIRS) {
    const abs = path.join(ROOT, d);
    if (!fs.existsSync(abs)) continue;
    for (const f of fs.readdirSync(abs)) {
      if (f.endsWith('.html')) out.push(path.join(d, f));
    }
  }
  return out.sort();
}

// Extrai blocos <script> SEM atributos (os de áudio não têm src nem type).
function inlineScripts(html) {
  const re = /<script>([\s\S]*?)<\/script>/g;
  const blocks = [];
  let m;
  while ((m = re.exec(html)) !== null) blocks.push({ code: m[1], index: m.index });
  return blocks;
}

function lineOf(html, index) {
  return html.slice(0, index).split('\n').length;
}

const failures = [];
let scanned = 0;
let blocksChecked = 0;

for (const rel of listFiles()) {
  if (isIgnored(rel)) continue;
  const abs = path.isAbsolute(rel) ? rel : path.join(ROOT, rel);
  let html;
  try { html = fs.readFileSync(abs, 'utf8'); }
  catch (e) { failures.push({ file: rel, msg: `não foi possível ler: ${e.message}` }); continue; }
  scanned++;
  for (const blk of inlineScripts(html)) {
    // Só os blocos relevantes a áudio (audioMap / speakText).
    if (!blk.code.includes('audioMap') && !blk.code.includes('speakText')) continue;
    blocksChecked++;
    try {
      new vm.Script(blk.code); // compila (parse) — não executa
    } catch (e) {
      failures.push({ file: rel, msg: `${e.message} (bloco <script> na linha ~${lineOf(html, blk.index)} do arquivo)` });
      break; // um erro por arquivo basta
    }
  }
}

if (failures.length) {
  console.error(`\n✗ check_audiomap_syntax: ${failures.length} material(is) com bloco de áudio QUEBRADO:\n`);
  for (const f of failures) console.error(`  ${f.file}\n      → ${f.msg}`);
  console.error(`\nUm audioMap com erro de sintaxe deixa TODO o áudio mudo. Corrija antes do deploy.`);
  process.exit(1);
}

console.log(`✓ Sintaxe de áudio OK — ${scanned} materiais, ${blocksChecked} blocos de audioMap/speakText, zero erro de parse.`);
