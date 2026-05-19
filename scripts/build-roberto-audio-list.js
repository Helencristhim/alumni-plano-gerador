#!/usr/bin/env node
/**
 * Build the master audio list for Roberto Pires from content JSON.
 *
 * Output: scripts/roberto-audio-list.json
 *   [{ text, voice: "arthur"|"ellen", filename }]
 *
 * Voice assignment rules (per prompt):
 *   - Arthur (pNInz6obpgDQGcFmaJgB) → vocabulary single words, oral drilling, error correction, pronunciation, survival cards (alternating with Ellen)
 *   - Ellen  (CwhRBWXzGAHq8TQ4Fs17) → dialogue lines (when speaker is the foreign agent/staff/passenger), context sentences, listening comprehension answers, frases-modelo
 *   - In dialogues, voice is dictated by the line.voice field
 *   - In survival card, alternate Arthur/Ellen by line index
 */

const fs = require('fs');
const path = require('path');

const SRC = path.join(__dirname, 'roberto-pires-content.json');
const OUT = path.join(__dirname, 'roberto-audio-list.json');

const data = JSON.parse(fs.readFileSync(SRC, 'utf8'));

function slugify(s) {
  return String(s)
    .toLowerCase()
    .normalize('NFD').replace(/[̀-ͯ]/g, '')
    .replace(/[^a-z0-9\s'-]/g, ' ')
    .replace(/'/g, '')
    .trim()
    .replace(/\s+/g, '-')
    .replace(/-+/g, '-')
    .replace(/^-|-$/g, '')
    .slice(0, 80);
}

const seen = new Set();
const list = [];

function add(text, voice) {
  if (!text) return;
  const t = String(text).trim();
  if (!t) return;
  const key = t;
  if (seen.has(key)) return;
  seen.add(key);
  list.push({ text: t, voice, filename: slugify(t) + '.mp3' });
}

// Onboarding — mix of voices, alternate by index
data.onboarding.frasesEmergencia.forEach((p, i) => add(p.en, i % 2 === 0 ? 'arthur' : 'ellen'));

// Per lesson
data.aulas.forEach((aula) => {
  // Vocabulary single words (Arthur)
  aula.vocabulario.forEach(v => add(v.en, 'arthur'));
  // Vocabulary example sentences (Arthur)
  aula.vocabulario.forEach(v => add(v.ex, 'arthur'));

  // Frases-modelo Pre-class (Ellen — frases-modelo)
  (aula.frasesModeloPreClass || []).forEach(f => add(f, 'ellen'));
  // Frases-modelo Material Professor (Ellen)
  (aula.frasesModeloMaterial || []).forEach(f => add(f, 'ellen'));

  // Pre-class fill-in phrases (alternate)
  const fill1 = aula.preClassExercicios.fillBlankWithHint || [];
  const fill2 = aula.preClassExercicios.fillBlank || [];
  [...fill1, ...fill2].forEach((it, i) => add(it.phrase, i % 2 === 0 ? 'arthur' : 'ellen'));

  // Pre-class multiple choice question stems and CORRECT options (Ellen)
  (aula.preClassExercicios.multipleChoice || []).forEach(q => {
    add(q.q, 'ellen');
    add(q.options[q.correct], 'arthur');
  });

  // Pre-class ordering — final correct phrase as concatenation (Arthur)
  if (aula.preClassExercicios.ordering) {
    add(aula.preClassExercicios.ordering.correct.join(' '), 'arthur');
  }

  // Pre-class pronunciation phrases (Arthur — drilling)
  (aula.preClassExercicios.pronunciation || []).forEach(p => add(p.phrase, 'arthur'));

  // Material Professor — vocabulary context sentences (Ellen — diálogos/exemplos)
  (aula.materialProfessorExercicios.vocabularyContextSentences || []).forEach(v => add(v.sentence, 'ellen'));

  // Dialogue — voice from line
  if (aula.materialProfessorExercicios.dialogue) {
    aula.materialProfessorExercicios.dialogue.lines.forEach(l => add(l.text, l.voice));
  }

  // Listening comprehension answers (Arthur)
  (aula.materialProfessorExercicios.listeningQuestions || []).forEach(q => add(q.a, 'arthur'));

  // Oral drilling expected answers (Arthur — drilling)
  (aula.materialProfessorExercicios.oralDrillingPrompts || []).forEach(p => add(p.en, 'arthur'));

  // Error correction RIGHT versions (Arthur)
  (aula.materialProfessorExercicios.errorCorrection || []).forEach(e => add(e.right, 'arthur'));

  // Role-play expected outputs (Ellen — frase modelo)
  (aula.materialProfessorExercicios.rolePlays || []).forEach(rp => {
    if (rp.esperado && !rp.esperado.startsWith('Open production') && !rp.esperado.startsWith('Production')) {
      add(rp.esperado, 'ellen');
    }
  });

  // Substitution drill — model + each substitution rendered (Arthur)
  if (aula.materialProfessorExercicios.substitutionDrill) {
    const sd = aula.materialProfessorExercicios.substitutionDrill;
    add(sd.modelo, 'arthur');
    sd.substituicoes.forEach(sub => {
      const rendered = sd.modelo.replace('___', sub);
      add(rendered, 'arthur');
    });
  }

  // Survival card — alternate Arthur/Ellen
  if (aula.survivalCard) {
    aula.survivalCard.linhas.forEach((l, i) => add(l.en, i % 2 === 0 ? 'arthur' : 'ellen'));
  }

  // Blocos dominados (Arthur)
  (aula.blocosDominados || []).forEach(b => add(b, 'arthur'));
});

// Add common contraction variants so audioMap has fallbacks
const contractionPairs = [
  ["I'm", "I am"],
  ["don't", "do not"],
  ["didn't", "did not"],
  ["can't", "cannot"],
  ["won't", "will not"],
  ["I'll", "I will"],
  ["it's", "it is"],
  ["that's", "that is"],
  ["you're", "you are"],
  ["I'd", "I would"],
  ["could've", "could have"],
];
const expanded = [];
list.forEach(item => {
  let expandedText = item.text;
  contractionPairs.forEach(([c, full]) => {
    expandedText = expandedText.replace(new RegExp('\\b' + c.replace("'", "'") + '\\b', 'g'), full);
  });
  if (expandedText !== item.text && !seen.has(expandedText)) {
    expanded.push({ text: expandedText, voice: item.voice, filename: slugify(expandedText) + '.mp3' });
    seen.add(expandedText);
  }
});

const final = [...list, ...expanded];

fs.writeFileSync(OUT, JSON.stringify(final, null, 2), 'utf8');

const arthurCount = final.filter(x => x.voice === 'arthur').length;
const ellenCount  = final.filter(x => x.voice === 'ellen').length;
const totalChars  = final.reduce((s, x) => s + x.text.length, 0);

console.log('Wrote', OUT);
console.log('Total phrases:', final.length);
console.log('  Arthur:', arthurCount);
console.log('  Ellen :', ellenCount);
console.log('Total characters (~ElevenLabs cost):', totalChars);
console.log('First 5:');
final.slice(0, 5).forEach(x => console.log('  [' + x.voice + ']', x.text.slice(0, 60), '→', x.filename));
