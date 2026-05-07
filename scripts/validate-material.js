#!/usr/bin/env node
/**
 * ALUMNI — VALIDAÇÃO FINAL OBRIGATÓRIA
 * Roda os 5 checks antes de qualquer deploy.
 * Usage: node scripts/validate-material.js public/professor/{id}.html public/aluno/{id}.html
 */

const fs = require('fs');
const path = require('path');

const files = process.argv.slice(2);
if (files.length === 0) {
  console.error('Usage: node validate-material.js <file1.html> [file2.html] ...');
  process.exit(1);
}

let totalFails = 0;

files.forEach(file => {
  if (!fs.existsSync(file)) { console.error('File not found: ' + file); process.exit(1); }
  const html = fs.readFileSync(file, 'utf8');
  const label = path.basename(file);

  console.log('\n' + '═'.repeat(60));
  console.log('VALIDANDO: ' + label);
  console.log('═'.repeat(60));

  // CHECK 1 — Português e acentuação
  console.log('\n✦ CHECK 1 — Português e Acentuação');
  const ptErrors = [];
  // Only check words that are ALWAYS wrong without accent (exclude English words like "Portuguese")
  const badWords = [
    ['traducao', 'tradução'], ['comunicacao', 'comunicação'], ['producao', 'produção'],
    ['apresentacao', 'apresentação'], ['informacao', 'informação'],
    ['exercicio', 'exercício'], ['financas', 'finanças'],
    ['tambem', 'também'], ['numero', 'número'], ['pagina', 'página']
  ];
  // Note: "portugues", "pratica", "voce", "nao", "pronuncia" excluded because they match
  // English words (Portuguese, practical, etc.) or appear in audioMap paths
  badWords.forEach(([bad, correct]) => {
    const regex = new RegExp(bad, 'gi');
    const matches = html.match(regex);
    if (matches) {
      // Filter out English contexts and HTML entities
      matches.forEach(m => {
        if (m.toLowerCase() !== correct.replace(/[áàâãéèêíìóòôõúùç]/g, c => {
          return {á:'a',à:'a',â:'a',ã:'a',é:'e',è:'e',ê:'e',í:'i',ì:'i',ó:'o',ò:'o',ô:'o',õ:'o',ú:'u',ù:'u',ç:'c'}[c] || c;
        })) return;
        ptErrors.push(m + ' → deveria ser ' + correct);
      });
    }
  });
  console.log(ptErrors.length === 0 ? '  PASS — acentuação OK' : '  FAIL — ' + ptErrors.length + ' problemas');
  ptErrors.slice(0, 5).forEach(e => console.log('    ' + e));
  if (ptErrors.length > 0) totalFails++;

  // CHECK 2 — Inglês (American English)
  console.log('\n✦ CHECK 2 — Inglês / American English');
  const britishWords = ['colour', 'organise', 'favourite', 'centre', 'realise', 'recognise', 'behaviour', 'programme'];
  const enErrors = [];
  britishWords.forEach(w => {
    const regex = new RegExp('\\b' + w + '\\b', 'gi');
    if (regex.test(html)) enErrors.push('British English: ' + w);
  });
  console.log(enErrors.length === 0 ? '  PASS — American English OK' : '  FAIL — ' + enErrors.length + ' problemas');
  enErrors.forEach(e => console.log('    ' + e));
  if (enErrors.length > 0) totalFails++;

  // CHECK 3 — Nível (basic check - contagem de vocabulário)
  console.log('\n✦ CHECK 3 — Nível x Conteúdo');
  const vocabCards = (html.match(/vocab-card-word/g) || []).length;
  const matchRows = (html.match(/match-row/g) || []).length;
  const fillBlanks = (html.match(/checkBlank/g) || []).length;
  const quizOptions = (html.match(/selectQuiz/g) || []).length;
  console.log('  Vocab cards: ' + vocabCards);
  console.log('  Matching rows: ' + matchRows);
  console.log('  Fill-in checks: ' + fillBlanks);
  console.log('  Quiz options: ' + quizOptions);
  const hasContent = vocabCards > 0 || matchRows > 0;
  console.log(hasContent ? '  PASS — conteúdo presente' : '  FAIL — sem exercícios');
  if (!hasContent) totalFails++;

  // CHECK 4 — Áudios ElevenLabs
  console.log('\n✦ CHECK 4 — Áudios ElevenLabs');
  const mapMatch = html.match(/var audioMap = ({[\s\S]*?});/);
  if (!mapMatch) {
    console.log('  FAIL — audioMap não encontrado');
    totalFails++;
  } else {
    const map = JSON.parse(mapMatch[1]);
    const entries = Object.keys(map);
    let mapMissing = 0;
    entries.forEach(k => {
      if (!fs.existsSync(path.join('public', map[k]))) mapMissing++;
    });

    // Check speakText/data-phrase without audioMap
    const speakTexts = [...html.matchAll(/speakText\('([^']+)'/g)].map(m => m[1]);
    const dataPhrases = [...html.matchAll(/data-phrase="([^"]+)"/g)].map(m => m[1]);
    let unmapped = 0;
    [...speakTexts, ...dataPhrases].forEach(t => { if (!map[t]) unmapped++; });

    console.log('  AudioMap entries: ' + entries.length);
    console.log('  Entries sem MP3: ' + mapMissing);
    console.log('  Frases sem audioMap: ' + unmapped);

    if (mapMissing === 0 && unmapped === 0) {
      console.log('  PASS — todos os áudios cobertos');
    } else {
      console.log('  FAIL — ' + (mapMissing + unmapped) + ' áudios faltando');
      totalFails++;
    }
  }

  // CHECK 5 — Funcionalidade dos exercícios
  console.log('\n✦ CHECK 5 — Funcionalidade');
  const dataExCount = (html.match(/data-exercise=/g) || []).length;
  if (dataExCount > 0) {
    console.log('  FAIL — ' + dataExCount + ' data-exercise encontrados (usar HTML manual)');
    totalFails++;
  }

  const funcs = ['checkBlank', 'selectQuiz', 'checkMatch', 'verifyAllMatches', 'startRecording', 'speakPhrase'];
  let funcMissing = 0;
  funcs.forEach(f => {
    if (!html.includes(f)) { console.log('  AVISO: ' + f + ' não encontrado'); funcMissing++; }
  });

  if (dataExCount === 0 && funcMissing === 0) {
    console.log('  PASS — HTML manual, funções presentes');
  } else if (dataExCount === 0) {
    console.log('  PASS (com avisos) — HTML manual OK, ' + funcMissing + ' funções ausentes');
  }
});

console.log('\n' + '═'.repeat(60));
if (totalFails === 0) {
  console.log('RESULTADO FINAL: ✓ TODOS OS CHECKS PASSARAM');
  console.log('Material APROVADO para deploy.');
} else {
  console.log('RESULTADO FINAL: ✗ ' + totalFails + ' CHECK(S) FALHARAM');
  console.log('Material REJEITADO. Corrigir antes do deploy.');
  process.exit(1);
}
console.log('═'.repeat(60));
