#!/usr/bin/env node
// O cache de material do painel nao pode deixar uma aba decidir pela outra.
//
// public/dashboard.html guarda na sessao (sessionStorage) o que a varredura confirmou
// para cada card, e a varredura PULA quem ja esta no cache. O mesmo aluno resolve para
// arquivos diferentes em cada aba (arquivoDoAluno: `{id}` em Alunos Imersivo,
// `{id}-ciclo1` em Alunos Consultivo), e a sessao e a mesma nas duas.
//
// Ate 16/09/2026 a chave era so o id. Medido no Chromium em producao:
//   - imersivo -> consultivo: a Rita Rodrigues (so tem o extra intensivo no imersivo)
//     ficava {p:0} e na aba consultivo o card saia "Criar Material" desabilitado, com o
//     rita-rodrigues-ciclo1.html no ar;
//   - consultivo -> imersivo: Rita e Vanessa Aparecida ficavam {p:1} e o imersivo
//     desenhava "Acessar Material Professor" para /professor/{id}.html, que da 404.
//
// Este teste extrai do HTML as funcoes do cache e da resolucao de arquivo, roda os dois
// sentidos numa sessao so e reprova se o registro de uma aba aparecer na outra. Tambem
// reprova se o render ou a varredura voltarem a ler o Map direto pelo id.
//
// Uso: node scripts/check_dashboard_cache_aba.mjs [caminho/do/dashboard.html]
import fs from 'node:fs';
import vm from 'node:vm';

const arquivo = process.argv[2] || 'public/dashboard.html';
const html = fs.readFileSync(arquivo, 'utf8');
const falhas = [];

function extraiFuncao(nome) {
    const i = html.indexOf('function ' + nome + '(');
    if (i < 0) return null;
    let j = html.indexOf('{', i), prof = 0;
    for (; j < html.length; j++) {
        if (html[j] === '{') prof++;
        else if (html[j] === '}' && --prof === 0) return html.slice(i, j + 1);
    }
    return null;
}

const pecas = ['arquivoDoAluno', 'rememberMaterial', 'chaveMaterial', 'materialConfirmado']
    .map(n => [n, extraiFuncao(n)]);
const mapInit = html.match(/const confirmedMaterials = new Map\([\s\S]*?\}\(\)\);/);
if (!mapInit) falhas.push('nao achei `const confirmedMaterials = new Map(...)`');
for (const [n, src] of pecas.slice(0, 2)) if (!src) falhas.push('nao achei function ' + n);

// Quem le o cache tem de passar pela aba. Leitura direta pelo id e o defeito.
if (/confirmedMaterials\.(get|has)\(\s*(a\.id|id)\s*\)/.test(html)) {
    falhas.push('render/varredura le confirmedMaterials direto pelo id do aluno (sem a aba)');
}

if (mapInit && pecas[0][1] && pecas[1][1]) {
    const store = {};
    const ctx = {
        sessionStorage: {
            getItem: k => (k in store ? store[k] : null),
            setItem: (k, v) => { store[k] = String(v); },
        },
        JSON, Array, Map,
    };
    vm.createContext(ctx);
    const src = pecas.filter(([, s]) => s).map(([, s]) => s).join('\n');
    // O leitor e o que o render/varredura usam; sem materialConfirmado, e o Map pelo id.
    const leitor = html.includes('function materialConfirmado(')
        ? 'materialConfirmado' : '(function(id){ return confirmedMaterials.get(id); })';
    const cenario = (inicio) => `
        var anatVista, ANAT = {'rita-rodrigues': {professor: 'rita-rodrigues-ciclo1', aluno: 'rita-rodrigues-ciclo1'}};
        ${mapInit[0].replace('const ', 'var ')}
        ${src}
        var ler = ${leitor};
        var outra = ${JSON.stringify(inicio)} === 'imersivo' ? 'consultivo' : 'imersivo';
        anatVista = ${JSON.stringify(inicio)};
        rememberMaterial('rita-rodrigues', {p: ${inicio === 'imersivo' ? 0 : 1}, a: 0, l: '', x: {'0p': 1}});
        var mesmaAba = ler('rita-rodrigues');
        anatVista = outra;
        ({mesmaAba: mesmaAba, outraAba: ler('rita-rodrigues')});
    `;
    for (const inicio of ['imersivo', 'consultivo']) {
        for (const k of Object.keys(store)) delete store[k];
        let r;
        try { r = vm.runInContext(cenario(inicio), ctx); }
        catch (e) { falhas.push(inicio + ': erro ao rodar o cenario: ' + e.message); continue; }
        if (!r.mesmaAba) falhas.push(inicio + ': o registro nao volta nem na propria aba');
        if (r.outraAba) falhas.push(inicio + ' -> outra aba: o registro de ' + inicio + ' vazou ('
            + JSON.stringify(r.outraAba) + '); a varredura pularia o card e o botao sairia errado');
    }
}

if (falhas.length) {
    console.error('FAIL check_dashboard_cache_aba (' + arquivo + ')');
    for (const f of falhas) console.error('  - ' + f);
    process.exit(1);
}
console.log('OK check_dashboard_cache_aba: cache de material separado por aba nos dois sentidos');
