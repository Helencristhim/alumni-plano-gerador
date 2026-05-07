#!/usr/bin/env node
/**
 * ALUMNI — Validador de Acentuação PT-BR
 * Busca palavras PT-BR sem acento em texto visível puro (HTML content, NOT code).
 * Exit code 1 se encontrar problemas.
 */

const fs = require('fs');
const path = require('path');

const ACCENT_MAP = {
  'criacao': 'criação', 'revisao': 'revisão', 'aprovacao': 'aprovação',
  'publicacao': 'publicação', 'informacao': 'informação', 'atencao': 'atenção',
  'observacao': 'observação', 'indicacao': 'indicação', 'validacao': 'validação',
  'geracao': 'geração', 'secao': 'seção', 'producao': 'produção',
  'comunicacao': 'comunicação', 'imigracao': 'imigração', 'apresentacao': 'apresentação',
  'situacao': 'situação', 'motivacao': 'motivação', 'avaliacao': 'avaliação',
  'compreensao': 'compreensão', 'conclusao': 'conclusão', 'decisao': 'decisão',
  'necessario': 'necessário', 'profissao': 'profissão', 'automatico': 'automático',
  'automatica': 'automática', 'pedagogicas': 'pedagógicas', 'pedagogica': 'pedagógica',
  'academico': 'acadêmico', 'intermediario': 'intermediário', 'avancado': 'avançado',
  'publico': 'público', 'concluidos': 'concluídos', 'extraidos': 'extraídos',
  'historico': 'histórico', 'ultimo': 'último', 'proximo': 'próximo',
  'proxima': 'próxima', 'formulario': 'formulário', 'vitoria': 'vitória',
};

// Only check PURE HTML text content — extract text between > and <
function extractVisibleText(htmlLine) {
  // Get text between HTML tags
  const texts = [];
  const tagContent = htmlLine.replace(/<[^>]*>/g, '|||').split('|||');
  tagContent.forEach(t => {
    const trimmed = t.trim();
    if (trimmed && trimmed.length > 2 && !/^[{}\[\]();,=]/.test(trimmed)) {
      texts.push(trimmed);
    }
  });
  return texts.join(' ');
}

const projectRoot = path.join(__dirname, '..');
const filesToCheck = [];

function addFiles(dir, exts) {
  if (!fs.existsSync(dir)) return;
  fs.readdirSync(dir, { withFileTypes: true }).forEach(item => {
    const fp = path.join(dir, item.name);
    if (item.isDirectory() && !item.name.startsWith('.') && item.name !== 'node_modules') addFiles(fp, exts);
    else if (item.isFile() && exts.some(e => item.name.endsWith(e))) filesToCheck.push(fp);
  });
}

addFiles(path.join(projectRoot, 'public'), ['.html']);

console.log('═══════════════════════════════════════════════════');
console.log('  ALUMNI — VALIDAÇÃO DE ACENTUAÇÃO PT-BR');
console.log('  (Verifica APENAS texto visível em HTML)');
console.log('═══════════════════════════════════════════════════\n');
console.log(`Verificando ${filesToCheck.length} arquivos HTML...\n`);

let totalIssues = 0;

filesToCheck.forEach(filePath => {
  const content = fs.readFileSync(filePath, 'utf8');
  const lines = content.split('\n');
  const relPath = path.relative(projectRoot, filePath);
  
  // Skip <script> and <style> blocks entirely
  let inScript = false;
  let inStyle = false;

  lines.forEach((line, lineNum) => {
    if (/<script/i.test(line)) inScript = true;
    if (/<\/script/i.test(line)) { inScript = false; return; }
    if (/<style/i.test(line)) inStyle = true;
    if (/<\/style/i.test(line)) { inStyle = false; return; }
    if (inScript || inStyle) return;

    // Extract only visible text (between tags)
    const visibleText = extractVisibleText(line);
    if (!visibleText) return;

    Object.entries(ACCENT_MAP).forEach(([bad, good]) => {
      const regex = new RegExp(`\\b${bad}\\b`, 'gi');
      if (regex.test(visibleText)) {
        totalIssues++;
        console.log(`❌ ${relPath}:${lineNum + 1} — "${bad}" → "${good}"`);
        console.log(`   Texto visível: ${visibleText.substring(0, 80)}`);
      }
    });
  });
});

console.log('\n────────────────────────────────────');
if (totalIssues === 0) {
  console.log('✅ Nenhum problema de acentuação em texto visível.');
  process.exit(0);
} else {
  console.log(`❌ ${totalIssues} problema(s) de acentuação em texto visível.`);
  process.exit(1);
}
