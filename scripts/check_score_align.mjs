#!/usr/bin/env node
/**
 * GATE 30 — o score nao marca errado quem falou certo.
 *
 * O reconhecedor do navegador ouve certo mas ESCREVE diferente do exercicio, e a
 * comparacao e palavra a palavra:
 *     alvo "ten hours"   -> Chrome escreve "10 hours"
 *     alvo "greenlight"  -> Chrome escreve "green light"
 * Medido em 19/08/2026 (rafael-pelizaro, pre-class 11): as duas marcadas como
 * faltantes com a pronuncia correta. `window.__alumniAlignSpoken` alinha a
 * transcricao ao alvo antes de pontuar.
 *
 * Este gate NAO reimplementa nada: carrega o activity-sync.js de verdade e o
 * analyzeWords de um material de verdade, e mede o score real.
 *
 * Prova as duas metades:
 *   1. os dois casos do defeito passam a pontuar certo;
 *   2. NADA MAIS muda — erro real segue erro, e onde a regra nao se aplica a
 *      transcricao sai intacta (invariante de identidade).
 */
import fs from 'node:fs';
import vm from 'node:vm';

const LIB = 'public/lib/activity-sync.js';
const MATERIAL = 'public/aluno/rafael-pelizaro.html';

function carregaLib() {
  const src = fs.readFileSync(LIB, 'utf8');
  const sandbox = {
    window: {}, document: { addEventListener() {}, querySelectorAll: () => [], querySelector: () => null,
      createElement: () => ({ style: {}, classList: { add() {} }, appendChild() {} }), head: { appendChild() {} }, body: {} },
    navigator: { mediaDevices: {} }, location: { pathname: '/aluno/x.html' },
    localStorage: { getItem: () => null, setItem() {}, removeItem() {} },
    setTimeout() {}, setInterval() {}, clearTimeout() {},
    console: { ...console, warn() {}, error() {} },
    URL: { createObjectURL: () => '', revokeObjectURL() {} },
  };
  sandbox.window = sandbox; sandbox.globalThis = sandbox;
  vm.createContext(sandbox);
  vm.runInContext(src, sandbox, { filename: LIB });
  return sandbox;
}

function carregaAnalyzeWords() {
  const html = fs.readFileSync(MATERIAL, 'utf8');
  const nomes = ['analyzeWords', 'wordsMatch', 'levenshtein'];
  let js = '';
  for (const nome of nomes) {
    const i = html.indexOf('function ' + nome + '(');
    if (i === -1) throw new Error(`funcao ${nome} nao encontrada em ${MATERIAL}`);
    let d = 0, fim = -1;
    for (let k = html.indexOf('{', i); k < html.length; k++) {
      if (html[k] === '{') d++;
      else if (html[k] === '}') { d--; if (d === 0) { fim = k + 1; break; } }
    }
    js += html.slice(i, fim) + '\n';
  }
  const box = { console };
  vm.createContext(box);
  vm.runInContext(js + ';this.analyzeWords=analyzeWords;', box);
  return box.analyzeWords;
}

const lib = carregaLib();
const align = lib.window.__alumniAlignSpoken;
const analyzeWords = carregaAnalyzeWords();
if (typeof align !== 'function') { console.error('FALHOU: window.__alumniAlignSpoken nao existe'); process.exit(1); }

// mesma normalizacao do runtime (activity-sync.js)
const norm = (s) => s.toLowerCase().replace(/[^a-z0-9' ]/g, '');
function faltantes(alvo, falado, { comAlign }) {
  const t = norm(alvo);
  let s = norm(falado);
  if (comAlign) s = align(t, s);
  return analyzeWords(t, s).expected.filter(w => w.status !== 'correct').map(w => w.word);
}

let falhas = 0;
const ok = (c, msg) => { console.log(`  ${c ? 'ok  ' : 'FALHA'}  ${msg}`); if (!c) falhas++; };
const eq = (a, b) => JSON.stringify(a) === JSON.stringify(b);

console.log('\n1) OS DOIS CASOS DO DEFEITO — antes marcavam errado, agora nao');
{
  const alvo = 'This initiative will save the team ten hours a week.';
  const dito = 'this initiative will save the team 10 hours a week';
  ok(eq(faltantes(alvo, dito, { comAlign: false }), ['ten']), 'antes: "ten" caia com o Chrome escrevendo "10"');
  ok(eq(faltantes(alvo, dito, { comAlign: true }), []), 'agora: nenhuma palavra faltante');
}
{
  const alvo = 'With your buy-in, we can greenlight the pilot this quarter.';
  const dito = 'with your buy-in we can green light the pilot this quarter';
  ok(eq(faltantes(alvo, dito, { comAlign: false }), ['greenlight']), 'antes: "greenlight" caia com o Chrome escrevendo "green light"');
  ok(eq(faltantes(alvo, dito, { comAlign: true }), []), 'agora: nenhuma palavra faltante');
}

console.log('\n2) ERRO DE VERDADE CONTINUA ERRO — a regra nao afrouxa nada');
{
  const alvo = 'This initiative will save the team ten hours a week.';
  ok(eq(faltantes(alvo, 'this initiative will save the team 10 minutes a week', { comAlign: true }), ['hours']),
     'trocar "hours" por "minutes" segue faltante');
  ok(faltantes(alvo, 'this initiative will save the team a week', { comAlign: true }).includes('ten'),
     'omitir o numero segue faltante');
}
{
  const alvo = 'With your buy-in, we can greenlight the pilot this quarter.';
  ok(faltantes(alvo, 'with your buy-in we can green the pilot this quarter', { comAlign: true }).includes('greenlight'),
     'falar so "green" NAO vale por "greenlight"');
  const g = 'with your buy-in we can greenlights the pilot this quarter';
  ok(eq(faltantes(alvo, g, { comAlign: false }), faltantes(alvo, g, { comAlign: true })),
     '"greenlights" -> veredito IDENTICO ao de antes (quem julga e o wordsMatch, nao nos)');
}
{
  const alvo = 'I have two reports to send.';
  ok(faltantes(alvo, 'i have to reports to send', { comAlign: true }).includes('two'),
     'homofono ("to" por "two") segue errado — nao inventamos tolerancia');
}
{
  const alvo = 'The green light is on.';
  ok(eq(faltantes(alvo, 'the green light is on', { comAlign: true }), []),
     'alvo com "green light" SEPARADO nao e desmanchado');
}

console.log('\n3) PROVA EM MASSA — em tudo que nao e os dois padroes, o veredito nao muda');
{
  // varre varios alunos, nao so um: a garantia de "nao muda nada" vale para o repo todo
  const dir = 'public/aluno';
  const hubs = fs.readdirSync(dir).filter(f => f.endsWith('.html') && !/-aula\d+\.html$/.test(f)).sort();
  const amostra = hubs.filter((_, i) => i % Math.max(1, Math.floor(hubs.length / 12)) === 0).slice(0, 12);
  const frases = [...new Set(amostra.flatMap(f =>
    [...fs.readFileSync(dir + '/' + f, 'utf8').matchAll(/data-phrase="([^"]+)"/g)].map(m => m[1])))];
  ok(frases.length >= 200, `${frases.length} frases reais de ${amostra.length} alunos`);

  // mutacoes que imitam o que um reconhecedor devolve de errado, SEM tocar
  // nos dois padroes (nenhum digito, nenhuma juncao de palavras do alvo)
  const mutacoes = [
    ['identica',        w => w],
    ['ultima letra',    w => (w.length > 4 ? w.slice(0, -1) : w)],
    ['palavra trocada', (w, i) => (i === 1 ? 'banana' : w)],
    ['palavra a mais',  null],
    ['palavra a menos', null],
    ['ordem trocada',   null],
  ];
  let comparados = 0, divergentes = 0;
  for (const f of frases) {
    const t = norm(f);
    const ws = t.split(/ +/);
    if (ws.length < 3) continue;
    const variantes = [
      ws.map((w, i) => mutacoes[0][1](w, i)).join(' '),
      ws.map((w, i) => mutacoes[1][1](w, i)).join(' '),
      ws.map((w, i) => mutacoes[2][1](w, i)).join(' '),
      ws.concat(['banana']).join(' '),
      ws.slice(1).join(' '),
      [ws[1], ws[0]].concat(ws.slice(2)).join(' '),
    ];
    for (const v of variantes) {
      comparados++;
      const antes = faltantes(f, v, { comAlign: false });
      const depois = faltantes(f, v, { comAlign: true });
      if (!eq(antes, depois)) {
        // so pode divergir se a frase realmente tem numero por extenso ou palavra composta
        divergentes++;
        console.log(`  DIVERGIU  ${JSON.stringify(t)}\n            falado: ${JSON.stringify(v)}\n            antes=${JSON.stringify(antes)} depois=${JSON.stringify(depois)}`);
      }
    }
  }
  ok(divergentes === 0, `${comparados} comparacoes antes-vs-depois, ${divergentes} divergencias`);
}

console.log(falhas === 0 ? '\nGATE 30 OK — os dois casos consertados, nada mais mudou.\n'
                         : `\nGATE 30 FALHOU — ${falhas} verificacao(oes).\n`);
process.exit(falhas === 0 ? 0 : 1);
