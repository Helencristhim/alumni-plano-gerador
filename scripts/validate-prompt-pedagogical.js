#!/usr/bin/env node
/**
 * ALUMNI — Validação de Integridade Pedagógica do Prompt da API
 * Verifica que o prompt da API perfil-360 contém INTEGRALMENTE
 * o conhecimento pedagógico do rulebook.
 *
 * Sai com exit code 1 se conteúdo pedagógico estiver incompleto.
 */

const fs = require('fs');
const path = require('path');

const apiFile = path.join(__dirname, '..', 'api', 'perfil-360.js');
const content = fs.readFileSync(apiFile, 'utf8');

console.log('═══════════════════════════════════════════════════');
console.log('  ALUMNI — VALIDAÇÃO DE INTEGRIDADE PEDAGÓGICA');
console.log('═══════════════════════════════════════════════════\n');

let totalPass = 0;
let totalFail = 0;

function check(name, condition) {
  if (condition) {
    totalPass++;
    console.log(`  ✅ ${name}`);
  } else {
    totalFail++;
    console.log(`  ❌ ${name}`);
  }
}

// 1. Verificar 8 níveis (A1 a C2)
console.log('1. RULEBOOK POR NÍVEL (8 níveis):');
const levels = ['A1', 'A2', 'B1 (', 'B2 (', 'C1 (Avançado)', 'C1+', 'C2'];
levels.forEach(level => {
  check(`Nível ${level}`, content.includes(level));
});

// Verificar que cada nível tem pelo menos 5 dimensões
console.log('\n   Dimensões por nível:');
const dimensions = ['tradução', 'palavras', 'CCQ', 'Practice', 'Production', 'Mídias'];
const a2Section = content.substring(
  content.indexOf('A2 (Pré-Intermediário)'),
  content.indexOf('B1 (Intermediário)')
);
let dimCount = 0;
dimensions.forEach(dim => {
  if (a2Section.toLowerCase().includes(dim.toLowerCase())) dimCount++;
});
check(`A2 tem ${dimCount}/6 dimensões (mínimo 5)`, dimCount >= 5);

// 2. Verificar 5 faixas etárias
console.log('\n2. RULEBOOK POR IDADE (5 faixas):');
const ages = ['5-12', '13-17', '18-30', '31-50', '50+'];
ages.forEach(age => {
  check(`Faixa ${age}`, content.includes(age));
});

// 3. Verificar análise pedagógica (componentes do Perfil 360)
console.log('\n3. ANÁLISE PEDAGÓGICA DO PERFIL 360:');
check('Resumo executivo no output', content.includes('resumoExecutivo'));
check('Mapa de personalidade no output', content.includes('mapaPersonalidade'));
check('Frases textuais no output', content.includes('frasesTextuais'));
check('Necessidades pedagógicas no output', content.includes('necessidadesPedagogicas'));
check('Promessa transformadora no output', content.includes('promessaTransformadora'));
check('Justificativa do programa no output', content.includes('justificativaPrograma'));

// 4. Verificar extração de dados
console.log('\n4. DADOS EXTRAÍDOS DA CONSULTORIA:');
check('Extração de idade', content.includes('idade'));
check('Extração de profissão', content.includes('profissao'));
check('Extração de nível', content.includes('nivel'));
check('Extração de foco', content.includes('foco'));
check('Extração de histórico', content.includes('historico'));
check('Extração de evento-alvo', content.includes('eventoAlvo'));
check('Extração de hobbies', content.includes('hobbies'));

// 5. Verificar sistema de selos
console.log('\n5. SISTEMA DE SELOS:');
check('Selo 🟢', content.includes('🟢'));
check('Selo 🟡', content.includes('🟡'));
check('Selo 🟠', content.includes('🟠'));
check('Selo 🔴', content.includes('🔴'));

// 6. Verificar max_tokens
console.log('\n6. CONFIGURAÇÃO TÉCNICA:');
const maxTokensMatch = content.match(/max_tokens:\s*(\d+)/);
if (maxTokensMatch) {
  const tokens = parseInt(maxTokensMatch[1]);
  check(`max_tokens: ${tokens} (mínimo 16000)`, tokens >= 16000);
} else {
  check('max_tokens encontrado', false);
}

// 7. Verificar modelo
check('Modelo: claude-sonnet-4-6', content.includes('claude-sonnet-4-6'));

// 8. Verificar persona
console.log('\n7. PERSONA:');
check('Harmer/Thornbury/Cambridge mencionado',
  content.includes('Harmer') || content.includes('Thornbury') || content.includes('Cambridge'));

// 8. Verificar CEFR-ALUMNI.md (8 níveis completos)
console.log('\n8. CEFR-ALUMNI.md (8 NÍVEIS):');
const cefrFile = path.join(__dirname, '..', 'docs', 'CEFR-ALUMNI.md');
let cefrContent = '';
try { cefrContent = fs.readFileSync(cefrFile, 'utf8'); } catch(e) { cefrContent = ''; }

const cefrLevels = ['A0', 'A1', 'A2', 'B1', 'B2', 'C1', 'C1+', 'C2'];
cefrLevels.forEach(level => {
  check(`Nível ${level} presente`, cefrContent.includes(`### ${level}`) || cefrContent.includes(`## ${level}`));
});

const cefrSections = ['AUTONOMIA', 'QUANTIDADES POR AULA', 'DISTRIBUIÇÃO PPP', 'ESTRUTURAS GRAMATICAIS', 'VOCABULÁRIO CORE', 'EXPRESSIONS', 'CARGAS EMOCIONAIS'];
cefrSections.forEach(section => {
  const count = (cefrContent.match(new RegExp(section, 'gi')) || []).length;
  check(`Seção "${section}" (${count} ocorrências, mínimo 4)`, count >= 4);
});

check('REGRA A0 PREMIUM presente', cefrContent.includes('REGRA A0 PREMIUM'));
check('REGRA DE EXCEÇÃO ÚNICA (crianças) presente', cefrContent.includes('REGRA DE EXCEÇÃO ÚNICA'));
check('RESUMO DAS QUANTIDADES POR NÍVEL presente', cefrContent.includes('RESUMO DAS QUANTIDADES'));

// 9. Verificar REGRAS-119-A-137.md
console.log('\n9. REGRAS 119-137:');
const regrasFile = path.join(__dirname, '..', 'docs', 'REGRAS-119-A-137.md');
let regrasContent = '';
try { regrasContent = fs.readFileSync(regrasFile, 'utf8'); } catch(e) { regrasContent = ''; }

check('Arquivo REGRAS-119-A-137.md existe', regrasContent.length > 500);

const regras = [119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137];
regras.forEach(r => {
  check(`Regra ${r} presente`, regrasContent.includes(`REGRA ${r}`));
});

// 10. Verificar regras no prompt da API perfil-360
console.log('\n10. REGRAS 119-137 NO PROMPT PERFIL-360:');
const apiRegras = [119,120,122,123,127,131,135,136,137];
apiRegras.forEach(r => {
  check(`Regra ${r} no prompt perfil-360`, content.includes(`REGRA ${r}`));
});

// 11. Verificar REGRAS 138-142
console.log('\n11. REGRAS 138-142:');
const regras2File = path.join(__dirname, '..', 'docs', 'REGRAS-138-A-143.md');
let regras2Content = '';
try { regras2Content = fs.readFileSync(regras2File, 'utf8'); } catch(e) { regras2Content = ''; }

check('Arquivo REGRAS-138-A-143.md existe', regras2Content.length > 200);
[138,139,140,141,142,143].forEach(r => {
  check(`Regra ${r} no documento`, regras2Content.includes(`REGRA ${r}`));
});
check('REGRA META (coerência 5 abas) presente', regras2Content.includes('REGRA META'));

// 12. Verificar regras 138-143 no prompt perfil-360
console.log('\n12. REGRAS 138-143 NO PROMPT PERFIL-360:');
[138,139,140,141,142,143].forEach(r => {
  check(`Regra ${r} no prompt perfil-360`, content.includes(`REGRA ${r}`));
});
check('REGRA META no prompt perfil-360', content.includes('REGRA META'));

// 13. Verificar integridade dos documentos
console.log('\n13. INTEGRIDADE DOS DOCUMENTOS:');
const rulebookFile = path.join(__dirname, '..', 'docs', 'RULEBOOK-PEDAGOGICO.md');
let rulebookExists = false;
try { rulebookExists = fs.statSync(rulebookFile).size > 1000; } catch(e) {}
check('RULEBOOK-PEDAGOGICO.md existe e tem conteúdo', rulebookExists);
check('CEFR-ALUMNI.md tem 8 níveis', cefrContent.includes('A0') && cefrContent.includes('C2'));
check('REGRAS-119-A-137.md tem 19 regras', regrasContent.includes('REGRA 119') && regrasContent.includes('REGRA 137'));
check('REGRAS-138-A-143.md tem 6 regras (138-143)', regras2Content.includes('REGRA 138') && regras2Content.includes('REGRA 143'));

// Resultado
console.log('\n────────────────────────────────────');
console.log(`  ✅ PASS: ${totalPass}`);
console.log(`  ❌ FAIL: ${totalFail}`);
console.log('────────────────────────────────────');

if (totalFail > 0) {
  console.log('\n🚫 INTEGRIDADE PEDAGÓGICA COMPROMETIDA.');
  console.log('   Restaure o conteúdo pedagógico antes de fazer deploy.\n');
  process.exit(1);
} else {
  console.log('\n✅ INTEGRIDADE PEDAGÓGICA VERIFICADA.\n');
  process.exit(0);
}
