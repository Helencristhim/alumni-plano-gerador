#!/usr/bin/env node
/**
 * O EDITOR DE FRAMEWORK NO TERMINAL — a mesma coisa que o catálogo faz, sem navegador.
 *
 * Editar public/data/frameworks.json na mão funciona até o dia em que alguém troca um
 * exercício do contrato SEM subir a versão. Aí as aulas já publicadas, que carimbaram
 * a versão em que nasceram, passam a ser julgadas por uma regra que não existia quando
 * nasceram — e o GATE 12 fica vermelho em coisa que ninguém quebrou. A regra da versão
 * não pode depender de memória; então ela mora no código, e este CLI é a porta.
 *
 * A LÓGICA NÃO ESTÁ AQUI. Está em public/lib/framework-edit.js, o mesmo arquivo que o
 * navegador e a função serverless carregam. Três portas, uma regra só.
 *
 * Exemplos:
 *   node scripts/framework-edit.mjs --listar
 *   node scripts/framework-edit.mjs --ver adulto/ppp
 *   node scripts/framework-edit.mjs --exercicios
 *
 *   # tirar o gapfill do contrato do PPP (sobe pra v2 sozinho)
 *   node scripts/framework-edit.mjs --cat adulto --id ppp --tirar gapfill
 *
 *   # método novo (nasce mock, nunca toca aluno real)
 *   node scripts/framework-edit.mjs --cat adulto --id dogme --label "Dogme" \
 *     --resumo "Sem material: a aula sai da conversa." \
 *     --obrigatorios dialogo,slide-tarefa,checklist --min 20
 *
 * Depois de editar, o fluxo é o de sempre: branch, commit, PR, gates, merge.
 */
import { readFileSync, writeFileSync } from 'node:fs';
import { createRequire } from 'node:module';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const require = createRequire(import.meta.url);
const RAIZ = join(dirname(fileURLToPath(import.meta.url)), '..');
const ARQ = join(RAIZ, 'public/data/frameworks.json');
const BANCO = join(RAIZ, 'public/data/exercicios.json');
const { aplicarEdicao } = require(join(RAIZ, 'public/lib/framework-edit.js'));

const args = {};
for (let i = 2; i < process.argv.length; i++) {
  const a = process.argv[i];
  if (!a.startsWith('--')) continue;
  const k = a.slice(2);
  const prox = process.argv[i + 1];
  if (prox && !prox.startsWith('--')) { args[k] = prox; i++; } else { args[k] = true; }
}
const lista = (v) => (typeof v === 'string' ? v.split(',').map((s) => s.trim()).filter(Boolean) : null);

const dados = JSON.parse(readFileSync(ARQ, 'utf8'));
const banco = JSON.parse(readFileSync(BANCO, 'utf8'));

function acha(catId, id) {
  const cat = (dados.categorias || []).find((c) => c.id === catId);
  return cat ? { cat, fw: (cat.frameworks || []).find((f) => f.id === id) } : {};
}

if (args.exercicios) {
  console.log(`banco: ${banco.exercicios.length} exercícios (gerado do builder)\n`);
  for (const [g, rot] of Object.entries(banco.grupos)) {
    const doGrupo = banco.exercicios.filter((e) => e.grupo === g);
    if (!doGrupo.length) continue;
    console.log(`  ${rot}`);
    for (const e of doGrupo) {
      const nv = e.verificavel === false ? '  (o gate não confere este)' : '';
      console.log(`    ${e.id.padEnd(18)} ${e.label}${nv}`);
    }
  }
  process.exit(0);
}

if (args.listar) {
  for (const c of dados.categorias || []) {
    console.log(`\n${c.label} (${c.id})`);
    for (const f of c.frameworks || []) {
      const ct = f.contrato
        ? `contrato v${f.contrato.versao} · ${(f.contrato.obrigatorios || []).length} obrigatórios · ${f.contrato.min_slides || '?'}+ slides`
        : 'sem contrato';
      console.log(`  ${f.id.padEnd(20)} ${String(f.status).padEnd(12)} ${ct}`);
    }
  }
  process.exit(0);
}

if (typeof args.ver === 'string') {
  const [catId, id] = args.ver.split('/');
  const { fw } = acha(catId, id);
  if (!fw) { console.error(`não achei ${args.ver}`); process.exit(1); }
  console.log(JSON.stringify({ id: fw.id, label: fw.label, status: fw.status,
    contrato: fw.contrato, historico: (fw.contrato_historico || []).map((h) => h.versao) }, null, 2));
  process.exit(0);
}

if (!args.cat || !args.id) {
  console.error('uso: --cat <categoria> --id <framework> [--label X] [--resumo Y] [--min N]\n' +
                '     [--obrigatorios a,b,c] [--proibidos x,y] [--por a,b] [--tirar c,d]\n' +
                '     ou --listar | --ver cat/id | --exercicios');
  process.exit(2);
}

const { fw } = acha(args.cat, args.id);
const base = (fw && fw.contrato) || { obrigatorios: [], proibidos: [], min_slides: null };

// --por/--tirar mexem no que JÁ existe (o caso comum: "tira o gapfill daqui").
// --obrigatorios/--proibidos substituem a lista inteira.
let obrigatorios = lista(args.obrigatorios) || base.obrigatorios.slice();
let proibidos = lista(args.proibidos) || base.proibidos.slice();
for (const e of lista(args.por) || []) if (!obrigatorios.includes(e)) obrigatorios.push(e);
for (const e of lista(args.tirar) || []) {
  obrigatorios = obrigatorios.filter((x) => x !== e);
  proibidos = proibidos.filter((x) => x !== e);
}

const payload = {
  categoria: args.cat,
  id: args.id,
  label: args.label || (fw && fw.label) || args.id,
  resumo: args.resumo !== undefined && args.resumo !== true ? args.resumo : (fw ? fw.resumo : ''),
  contrato: { obrigatorios, proibidos,
              min_slides: args.min ? parseInt(args.min, 10) : base.min_slides },
  autor: 'terminal',
  origem: 'editado no terminal (scripts/framework-edit.mjs)'
};

let r;
try {
  r = aplicarEdicao(dados, banco, payload);
} catch (e) {
  console.error('recusado: ' + e.message);
  process.exit(1);
}

if (args['dry-run']) {
  console.log(`(dry-run) ${r.resumoMudanca}`);
  console.log(JSON.stringify(acha(args.cat, args.id).fw.contrato, null, 2));
  process.exit(0);
}

writeFileSync(ARQ, JSON.stringify(r.dados, null, 2) + '\n');
console.log(`${args.cat}/${args.id}: ${r.resumoMudanca}`);
console.log('\npróximo passo: python3 scripts/check_contrato_aula.py  (GATE 12) e abra o PR de sempre.');
