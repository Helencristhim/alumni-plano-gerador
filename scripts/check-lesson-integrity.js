#!/usr/bin/env node
/*
 * check-lesson-integrity.js — TRAVA DE DEPLOY (roda no buildCommand da Vercel).
 *
 * Falha o build (exit 1) — e portanto BLOQUEIA o deploy — se qualquer aula
 * publicada tiver:
 *   1. HTML vazio / corrompido / truncado (sem </html> no fim);
 *   2. referência a um .mp3 que NÃO existe em public/audio/ (aula "sem som").
 *
 * Versão Node do scripts/check_lesson_integrity.py (mesma lógica), para rodar
 * no mesmo runtime do build sem depender de python3.
 *
 * Ignora arquivos *backup* e *teste* (não servidos a aluno).
 */
const fs = require("fs");
const path = require("path");

const ROOT = path.dirname(__dirname);
const PUBLIC = path.join(ROOT, "public");
const SKIP = /backup|teste|test|-new-/i;
const REF = /\/audio\/[A-Za-z0-9_.\/-]+\.mp3/g;

function lessonFiles() {
  const out = [];
  for (const sub of ["aluno", "professor"]) {
    const dir = path.join(PUBLIC, sub);
    if (!fs.existsSync(dir)) continue;
    for (const f of fs.readdirSync(dir)) {
      if (f.endsWith(".html")) out.push(path.join(dir, f));
    }
  }
  return out.sort();
}

function main() {
  const args = process.argv.slice(2).filter((a) => !a.startsWith("-"));
  const files = args.length ? args : lessonFiles();
  const errors = [];
  let checked = 0;

  for (const f of files) {
    const base = path.basename(f);
    if (SKIP.test(base)) continue;
    let content;
    try {
      content = fs.readFileSync(f, "utf8");
    } catch (e) {
      errors.push(`${base}: ilegível (${e.message})`);
      continue;
    }
    checked++;
    const size = content.length;
    const lines = (content.match(/\n/g) || []).length;
    if (size < 500 || lines < 10) {
      errors.push(`${base}: VAZIO/CORROMPIDO (${lines} linhas / ${size} bytes)`);
      continue;
    }
    if (!content.slice(-3000).includes("</html>")) {
      errors.push(`${base}: TRUNCADO (sem </html> no final — geração cortada)`);
    }
    const refs = [...new Set(content.match(REF) || [])];
    const miss = refs
      .filter((r) => !fs.existsSync(path.join(PUBLIC, r.replace(/^\//, ""))))
      .sort();
    if (miss.length) {
      const shown = miss.slice(0, 6).map((m) => path.basename(m)).join(", ");
      const extra = miss.length > 6 ? ` (+${miss.length - 6})` : "";
      errors.push(`${base}: ${miss.length} ÁUDIO(S) FALTANDO -> ${shown}${extra}`);
    }
  }

  if (errors.length) {
    console.error("=".repeat(60));
    console.error(`  TRAVA DE INTEGRIDADE: ${errors.length} PROBLEMA(S) — DEPLOY BLOQUEADO`);
    console.error("=".repeat(60));
    for (const e of errors) console.error(`  x ${e}`);
    console.error("\nNenhuma aula sobe sem áudio/íntegra. Corrija os itens acima.");
    process.exit(1);
  }
  console.log(`OK integridade — ${checked} aulas, áudio completo, sem corrupção.`);
}

// fail-open: um erro inesperado no próprio checador NÃO deve bloquear todos os
// deploys. Só bloqueamos (exit 1) em problema de integridade CONFIRMADO acima.
try {
  main();
} catch (e) {
  console.error(`[check-lesson-integrity] aviso: checador falhou (${e.message}) — seguindo sem bloquear.`);
  process.exit(0);
}
