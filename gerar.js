#!/usr/bin/env node
/**
 * Script para gerar página estática de plano pedagógico
 * Uso: node gerar.js plano.json
 * O JSON deve seguir a estrutura padrão do sistema
 */

const fs = require('fs');
const path = require('path');

const jsonPath = process.argv[2];
if (!jsonPath) { console.error('Uso: node gerar.js <plano.json>'); process.exit(1); }

const data = JSON.parse(fs.readFileSync(jsonPath, 'utf8'));
const p = data.plano;
const a = p.aluno;
const id = data.id;

// Read template
const template = fs.readFileSync(path.join(__dirname, 'public', 'plano.html'), 'utf8');

// Generate static version with embedded data
const staticHtml = template
  .replace(
    `<div class="loading-overlay" id="loadingOverlay">`,
    `<script>window.__PLANO_DATA__ = ${JSON.stringify(data)};</script>\n<div class="loading-overlay" id="loadingOverlay" style="display:none">`
  )
  .replace(
    `// Get plan ID from URL\n    const pathParts = window.location.pathname.split('/');\n    currentId = pathParts[pathParts.length - 1] || pathParts[pathParts.length - 2];`,
    `currentId = '${id}';`
  )
  .replace(
    `function loadPlano() {\n        const planos = JSON.parse(localStorage.getItem('alumni-planos') || '[]');\n        const found = planos.find(p => p.id === currentId);`,
    `function loadPlano() {\n        const found = window.__PLANO_DATA__;`
  );

// Write to public directory
const outPath = path.join(__dirname, 'public', 'planos', id + '.html');
fs.mkdirSync(path.join(__dirname, 'public', 'planos'), { recursive: true });
fs.writeFileSync(outPath, staticHtml);

// Update index/registry
const registryPath = path.join(__dirname, 'public', 'planos', 'registry.json');
let registry = [];
if (fs.existsSync(registryPath)) registry = JSON.parse(fs.readFileSync(registryPath, 'utf8'));
registry.unshift({ id, nome: a.nome, nivel: a.nivel, numAulas: p.aulas?.length || 0, criadoEm: data.criadoEm });
fs.writeFileSync(registryPath, JSON.stringify(registry, null, 2));

console.log(`\n✅ Plano gerado: public/planos/${id}.html`);
console.log(`📋 Registry atualizado com ${registry.length} plano(s)`);
