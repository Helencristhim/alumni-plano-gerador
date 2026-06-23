// One-off: corrige cidade da Juliana Marques (Curitiba -> São Paulo) em todos os materiais.
const fs = require('fs');
const path = require('path');

const ROOT = path.join(__dirname, '..');
const FILES = [
  'public/professor/juliana-marques.html',
  'public/aluno/juliana-marques.html',
  '_build/juliana-aula11/slides.html',
  '_build/juliana-aula12/slides.html',
  '_build/juliana-aula13/slides.html',
];

for (const rel of FILES) {
  const fp = path.join(ROOT, rel);
  if (!fs.existsSync(fp)) { console.log('skip (missing): ' + rel); continue; }
  let html = fs.readFileSync(fp, 'utf8');
  const before = (html.match(/Curitiba/gi) || []).length;
  // 1) renomear os 2 MP3s que carregam a cidade no nome
  html = html.split('vivo_en_curitiba.mp3').join('vivo_en_sao_paulo.mp3');
  html = html.split('aula2_soy_brasilena_de_curitiba.mp3').join('aula2_soy_brasilena_de_sao_paulo.mp3');
  // 2) perfil: trocar UF junto
  html = html.split('Curitiba, PR').join('São Paulo, SP');
  // 3) restante das menções visíveis + chaves de áudio (mesma string literal => áudio continua casando)
  html = html.replace(/Curitiba/g, 'São Paulo');
  const after = (html.match(/Curitiba/gi) || []).length;
  fs.writeFileSync(fp, html, 'utf8');
  console.log(`${rel}: ${before} -> ${after} restantes`);
}
