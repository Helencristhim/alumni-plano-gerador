#!/usr/bin/env node
/**
 * ALUMNI — Script de Validação de Coerência Interna
 * Roda antes de publicar qualquer material de aluno.
 * Verifica as 8 regras de coerência absoluta.
 *
 * Uso: node scripts/validate-coherence.js <plano.json>
 * Saída: relatório de validação com PASS/FAIL por regra
 */

const fs = require('fs');

const jsonPath = process.argv[2];
if (!jsonPath) {
  console.error('Uso: node scripts/validate-coherence.js <plano.json>');
  process.exit(1);
}

const data = JSON.parse(fs.readFileSync(jsonPath, 'utf8'));
const plano = data.plano || data;
const aulas = plano.aulas || [];
const exercicios = plano.exercicios || [];

let totalPass = 0;
let totalFail = 0;
let totalWarn = 0;
const results = [];

function pass(regra, msg) {
  totalPass++;
  results.push({ status: 'PASS', regra, msg });
}

function fail(regra, msg) {
  totalFail++;
  results.push({ status: 'FAIL', regra, msg });
}

function warn(regra, msg) {
  totalWarn++;
  results.push({ status: 'WARN', regra, msg });
}

console.log('═══════════════════════════════════════════════════');
console.log('  ALUMNI — VALIDAÇÃO DE COERÊNCIA INTERNA');
console.log('═══════════════════════════════════════════════════\n');

// ── REGRA 1: Vocabulário fechado por aula ──
console.log('REGRA 1 — Vocabulário fechado por aula');
exercicios.forEach((ex, i) => {
  const aulaNum = ex.aulaNumero || i + 1;
  const vocabWords = (ex.vocabulario || []).map(v => v.en.toLowerCase());

  if (vocabWords.length === 0) {
    fail('R1', `Aula ${aulaNum}: Nenhum vocabulário definido no pre-class.`);
    return;
  }

  // Check fill-in-the-blanks use vocab words
  const fillWords = (ex.completarFrases || []).map(f => f.resposta.toLowerCase());
  const fillMissing = fillWords.filter(w => !vocabWords.some(v => v.includes(w) || w.includes(v)));

  if (fillMissing.length > 0) {
    warn('R1', `Aula ${aulaNum}: Fill-in usa palavras não no vocabulário: ${fillMissing.join(', ')}`);
  } else if (fillWords.length > 0) {
    pass('R1', `Aula ${aulaNum}: Fill-in usa ${fillWords.length} palavras do vocabulário. ✓`);
  }

  // Check quiz references vocab context
  const quizCount = (ex.quiz || []).length;
  if (quizCount > 0) {
    pass('R1', `Aula ${aulaNum}: ${quizCount} questões de quiz presentes. ✓`);
  }

  // Count vocab words
  if (vocabWords.length < 4) {
    warn('R1', `Aula ${aulaNum}: Apenas ${vocabWords.length} palavras de vocabulário (recomendado: 5-8 para A2).`);
  } else {
    pass('R1', `Aula ${aulaNum}: ${vocabWords.length} palavras de vocabulário definidas. ✓`);
  }
});

// ── REGRA 2: Estruturas gramaticais coerentes ──
console.log('\nREGRA 2 — Estruturas gramaticais coerentes');
aulas.forEach((aula, i) => {
  const foco = aula.focoLinguistico || '';
  if (foco.length > 10) {
    pass('R2', `Aula ${aula.numero || i+1}: Foco linguístico definido (${foco.substring(0, 60)}...). ✓`);
  } else {
    warn('R2', `Aula ${aula.numero || i+1}: Foco linguístico muito curto ou ausente.`);
  }
});

// ── REGRA 3: Frases-modelo em múltiplos pontos ──
console.log('\nREGRA 3 — Frases-modelo em múltiplos pontos');
exercicios.forEach((ex, i) => {
  const aulaNum = ex.aulaNumero || i + 1;
  const pronunciaFrases = (ex.frasesPronuncia || []).map(f => f.frase.toLowerCase());
  const vocabExemplos = (ex.vocabulario || []).map(v => (v.exemplo || '').toLowerCase());
  const dialogoFalas = ex.dialogo ? (ex.dialogo.linhas || []).map(l => (l.fala || '').toLowerCase()) : [];

  // Check if pronunciation phrases appear in dialogue or vocab examples
  let overlap = 0;
  pronunciaFrases.forEach(frase => {
    const words = frase.split(/\s+/).filter(w => w.length > 3);
    const inVocab = words.some(w => vocabExemplos.some(e => e.includes(w)));
    const inDialogo = words.some(w => dialogoFalas.some(d => d.includes(w)));
    if (inVocab || inDialogo) overlap++;
  });

  if (pronunciaFrases.length === 0) {
    warn('R3', `Aula ${aulaNum}: Nenhuma frase de pronúncia definida.`);
  } else if (overlap >= pronunciaFrases.length * 0.5) {
    pass('R3', `Aula ${aulaNum}: ${overlap}/${pronunciaFrases.length} frases de pronúncia conectadas ao vocabulário/diálogo. ✓`);
  } else {
    warn('R3', `Aula ${aulaNum}: Apenas ${overlap}/${pronunciaFrases.length} frases conectadas. Considere mais sobreposição.`);
  }
});

// ── REGRA 4: Exercícios usam apenas conteúdo já apresentado ──
console.log('\nREGRA 4 — Exercícios usam apenas conteúdo já apresentado');
exercicios.forEach((ex, i) => {
  const aulaNum = ex.aulaNumero || i + 1;
  const vocabWords = (ex.vocabulario || []).map(v => v.en.toLowerCase());
  const vocabPT = (ex.vocabulario || []).map(v => v.pt.toLowerCase());
  const allKnown = [...vocabWords, ...vocabPT];

  // Verify fill-in answers are from vocabulary
  const fills = (ex.completarFrases || []);
  let fillOk = 0;
  fills.forEach(f => {
    const answer = f.resposta.toLowerCase();
    if (allKnown.some(w => w.includes(answer) || answer.includes(w))) {
      fillOk++;
    }
  });

  if (fills.length > 0) {
    if (fillOk === fills.length) {
      pass('R4', `Aula ${aulaNum}: ${fillOk}/${fills.length} respostas de fill-in vindas do vocabulário. ✓`);
    } else {
      warn('R4', `Aula ${aulaNum}: ${fillOk}/${fills.length} respostas de fill-in vindas do vocabulário. ${fills.length - fillOk} podem usar palavras não apresentadas.`);
    }
  }
});

// ── REGRA 5: Imagens conectadas ao vocabulário ──
console.log('\nREGRA 5 — Imagens conectadas ao vocabulário');
warn('R5', 'Validação de imagens requer inspeção visual. Verificar manualmente se a galeria ilustra o vocabulário da aula.');

// ── REGRA 6: Áudios coerentes com o texto ──
console.log('\nREGRA 6 — Áudios coerentes com o texto');
exercicios.forEach((ex, i) => {
  const aulaNum = ex.aulaNumero || i + 1;
  const pronunciaCount = (ex.frasesPronuncia || []).length;
  const vocabCount = (ex.vocabulario || []).length;

  if (pronunciaCount > 0) {
    pass('R6', `Aula ${aulaNum}: ${pronunciaCount} frases de pronúncia + ${vocabCount} exemplos de vocabulário com áudio potencial. ✓`);
  } else {
    warn('R6', `Aula ${aulaNum}: Sem frases de pronúncia definidas para gerar áudio.`);
  }
});

// ── REGRA 7: Guia do professor referencia material exato ──
console.log('\nREGRA 7 — Guia do professor referencia material exato');
aulas.forEach((aula, i) => {
  const atividade = aula.atividadeEmSala || '';
  const dever = aula.deverDeCasa || '';
  const ex = exercicios[i];
  const vocabWords = ex ? (ex.vocabulario || []).map(v => v.en.toLowerCase()) : [];

  // Check if activity description mentions specific vocabulary
  let mentioned = 0;
  vocabWords.forEach(w => {
    if (atividade.toLowerCase().includes(w) || dever.toLowerCase().includes(w)) {
      mentioned++;
    }
  });

  if (vocabWords.length > 0 && mentioned >= 2) {
    pass('R7', `Aula ${aula.numero || i+1}: Atividade menciona ${mentioned}/${vocabWords.length} palavras do vocabulário. ✓`);
  } else if (vocabWords.length > 0) {
    warn('R7', `Aula ${aula.numero || i+1}: Atividade menciona apenas ${mentioned}/${vocabWords.length} palavras. Teacher Guide pode estar genérico.`);
  }
});

// ── REGRA 8: Pre-class prepara, não substitui ──
console.log('\nREGRA 8 — Pre-class prepara, não substitui');
exercicios.forEach((ex, i) => {
  const aulaNum = ex.aulaNumero || i + 1;
  const hasVocab = (ex.vocabulario || []).length > 0;
  const hasFill = (ex.completarFrases || []).length > 0;
  const hasPronuncia = (ex.frasesPronuncia || []).length > 0;
  const hasQuiz = (ex.quiz || []).length > 0;
  const hasDialogo = ex.dialogo && (ex.dialogo.linhas || []).length > 0;

  const types = [hasVocab, hasFill, hasPronuncia, hasQuiz, hasDialogo].filter(Boolean).length;

  if (types >= 4) {
    pass('R8', `Aula ${aulaNum}: Pre-class tem ${types}/5 tipos de exercício (vocabulário, fill-in, pronúncia, quiz, diálogo). ✓`);
  } else if (types >= 2) {
    warn('R8', `Aula ${aulaNum}: Pre-class tem apenas ${types}/5 tipos de exercício. Considere adicionar mais variedade.`);
  } else {
    fail('R8', `Aula ${aulaNum}: Pre-class tem apenas ${types}/5 tipos. Insuficiente para preparar a aula.`);
  }
});

// ── VALIDAÇÕES EXTRAS ──
console.log('\n═══════════════════════════════════════════════════');
console.log('  VALIDAÇÕES EXTRAS');
console.log('═══════════════════════════════════════════════════\n');

// Check acentuação
const jsonStr = JSON.stringify(data);
const badAccents = [];
const checks = [
  [/\bcartao\b/gi, 'cartão'],
  [/\bvoce\b/gi, 'você'],
  [/\bnao\b/gi, 'não'],
  [/\bimigracao\b/gi, 'imigração'],
  [/\balfandega\b/gi, 'alfândega'],
  [/\bportugues\b/gi, 'português'],
  [/\bexercicio\b/gi, 'exercício'],
];
checks.forEach(([regex, correct]) => {
  const matches = jsonStr.match(regex);
  if (matches) {
    badAccents.push(`"${matches[0]}" deveria ser "${correct}" (${matches.length}x)`);
  }
});
if (badAccents.length > 0) {
  fail('ACENTO', `Palavras sem acento encontradas: ${badAccents.join('; ')}`);
} else {
  pass('ACENTO', 'Nenhuma palavra sem acento óbvia encontrada. ✓');
}

// Check number of lessons matches
if (aulas.length !== exercicios.length) {
  fail('SYNC', `Número de aulas (${aulas.length}) ≠ número de blocos de exercícios (${exercicios.length}).`);
} else {
  pass('SYNC', `${aulas.length} aulas = ${exercicios.length} blocos de exercícios. ✓`);
}

// Check mídias
exercicios.forEach((ex, i) => {
  const aulaNum = ex.aulaNumero || i + 1;
  const midias = (ex.midias || []).length;
  if (midias >= 2) {
    pass('MIDIA', `Aula ${aulaNum}: ${midias} mídias complementares. ✓`);
  } else {
    warn('MIDIA', `Aula ${aulaNum}: Apenas ${midias} mídia(s). Recomendado: 2-3.`);
  }
});

// ── RELATÓRIO FINAL ──
console.log('\n═══════════════════════════════════════════════════');
console.log('  RELATÓRIO FINAL');
console.log('═══════════════════════════════════════════════════\n');

results.forEach(r => {
  const icon = r.status === 'PASS' ? '✅' : r.status === 'FAIL' ? '❌' : '⚠️';
  console.log(`${icon} [${r.regra}] ${r.msg}`);
});

console.log(`\n────────────────────────────────────`);
console.log(`  ✅ PASS: ${totalPass}`);
console.log(`  ⚠️  WARN: ${totalWarn}`);
console.log(`  ❌ FAIL: ${totalFail}`);
console.log(`────────────────────────────────────`);

if (totalFail > 0) {
  console.log('\n🚫 MATERIAL NÃO APROVADO PARA PUBLICAÇÃO.');
  console.log('   Corrija os itens FAIL antes de publicar.\n');
  process.exit(1);
} else if (totalWarn > 0) {
  console.log('\n⚠️  MATERIAL APROVADO COM RESSALVAS.');
  console.log('   Revise os itens WARN antes de publicar.\n');
  process.exit(0);
} else {
  console.log('\n✅ MATERIAL APROVADO PARA PUBLICAÇÃO.\n');
  process.exit(0);
}
