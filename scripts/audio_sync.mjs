#!/usr/bin/env node
// audio_sync.mjs — os MP3 das aulas moram no Vercel Blob, nao no git.
//
// POR QUE: com ~130 mil MP3 (5 GiB) versionados, todo deploy da Vercel clonava o repo inteiro
// e o clone pendurava ate o limite de 45 min (15 de 56 builds de producao entre 03 e 06/10/2026
// morreram assim, 60% do tempo de build cobrado). O CI ja tinha tirado public/audio do
// checkout pelo mesmo motivo (29/07/2026). Agora o site serve /audio/* por um rewrite do
// vercel.json para o Blob, e o git guarda so o INDICE de cada aluno:
//
//   public/audio/{slug}/_blob.json  ->  { "arquivo.mp3": { "bytes": N, "sha1": "..." } }
//
// O indice e a fonte da verdade de "este audio existe" para os gates (scripts/audio_registro.py).
//
// USO
//   node scripts/audio_sync.mjs subir [slug ...]     sobe os MP3 do disco que o indice nao tem
//                                                    (ou que mudaram) e atualiza o indice.
//                                                    Sem slug: todas as pastas de public/audio.
//   node scripts/audio_sync.mjs baixar slug [...]    traz do Blob para o disco os MP3 do indice
//                                                    que faltam. Os geradores chamam isto ANTES
//                                                    de gerar: eles pulam o que existe no disco,
//                                                    e sem o MP3 local regenerariam tudo na
//                                                    ElevenLabs (custo + voz diferente).
//   node scripts/audio_sync.mjs conferir [slug ...]  exit 1 se ha MP3 no disco fora do indice.
//
// Chave de escrita (so para `subir`): BLOB_READ_WRITE_TOKEN ou ~/.config/alumni/blob.token
// (mesmo esquema da chave da ElevenLabs; nunca commitada). `baixar` e `conferir` nao precisam.
import { execFileSync } from 'node:child_process';
import { createHash } from 'node:crypto';
import { existsSync, mkdirSync, readdirSync, readFileSync, statSync, writeFileSync } from 'node:fs';
import { homedir } from 'node:os';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

export const BLOB_BASE = 'https://gbuok0mwkuvmaraz.public.blob.vercel-storage.com';
const ROOT = join(dirname(fileURLToPath(import.meta.url)), '..');
const AUDIO = join(ROOT, 'public', 'audio');
const INDICE = '_blob.json';
// Cache curto de proposito: o gen_audio regera com o MESMO nome quando o texto muda
// (ledger _src.json). Com cache longo, o aluno ouviria o audio velho por dias.
const CACHE_SEG = 300;
// Limite do Blob no Pro: 75 operacoes avancadas/s. Ficamos abaixo.
const POR_SEG = 50;

const sha1 = (buf) => createHash('sha1').update(buf).digest('hex');
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

function lerIndice(slug) {
  const p = join(AUDIO, slug, INDICE);
  if (!existsSync(p)) return {};
  return JSON.parse(readFileSync(p, 'utf8'));
}

function gravarIndice(slug, idx) {
  const ordenado = Object.fromEntries(Object.keys(idx).sort().map((k) => [k, idx[k]]));
  writeFileSync(join(AUDIO, slug, INDICE), `${JSON.stringify(ordenado, null, 1)}\n`);
}

function mp3DoDisco(slug) {
  const d = join(AUDIO, slug);
  if (!existsSync(d)) return [];
  return readdirSync(d).filter((n) => n.toLowerCase().endsWith('.mp3') && statSync(join(d, n)).isFile());
}

function slugsPedidos(args) {
  if (args.length) return args;
  return existsSync(AUDIO) ? readdirSync(AUDIO).filter((n) => statSync(join(AUDIO, n)).isDirectory()) : [];
}

function chaveOuNada() {
  if (process.env.BLOB_READ_WRITE_TOKEN) return process.env.BLOB_READ_WRITE_TOKEN.trim();
  const f = join(homedir(), '.config', 'alumni', 'blob.token');
  return existsSync(f) ? readFileSync(f, 'utf8').trim() : null;
}

// MP3 que o git ainda versiona. Enquanto houver (antes da virada), MP3 sem Blob nao e
// problema: ele segue no commit como sempre e a virada sobe o que faltar.
function mp3NoGit() {
  try {
    const out = execFileSync('git', ['ls-files', 'public/audio'], {
      cwd: ROOT, encoding: 'utf8', maxBuffer: 256 * 1024 * 1024, stdio: ['ignore', 'pipe', 'ignore'],
    });
    return new Set(out.split('\n').filter((l) => l.toLowerCase().endsWith('.mp3')));
  } catch {
    return new Set();
  }
}

const NOTA_TRANSICAO = '(Blob: sem chave nesta maquina — os MP3 ainda vao para o git como antes. '
  + 'Nada a fazer: nao procure nem crie chave ou armazenamento do Blob; a chave chega na virada.)';

let proxima = 0;
async function vez() {
  const agora = Date.now();
  const minha = Math.max(agora, proxima);
  proxima = minha + 1000 / POR_SEG;
  if (minha > agora) await sleep(minha - agora);
}

async function emParalelo(itens, n, fn) {
  let i = 0;
  await Promise.all(Array.from({ length: n }, async () => { while (i < itens.length) await fn(itens[i++]); }));
}

async function subir(slugs) {
  const token = chaveOuNada();
  if (!token) {
    if (mp3NoGit().size) { console.log(NOTA_TRANSICAO); return; }
    console.error('ERRO: sem chave do Blob. Crie ~/.config/alumni/blob.token (chmod 600) ou exporte BLOB_READ_WRITE_TOKEN.');
    process.exit(2);
  }
  const { put } = await import('@vercel/blob');
  let subidos = 0, falhas = 0;
  for (const slug of slugsPedidos(slugs)) {
    const idx = lerIndice(slug);
    const fila = [];
    for (const nome of mp3DoDisco(slug)) {
      const buf = readFileSync(join(AUDIO, slug, nome));
      const h = sha1(buf);
      if (idx[nome]?.sha1 !== h) fila.push({ nome, buf, h });
    }
    if (!fila.length) continue;
    await emParalelo(fila, 16, async ({ nome, buf, h }) => {
      for (let t = 1; ; t++) {
        await vez();
        try {
          await put(`audio/${slug}/${nome}`, buf, {
            access: 'public', addRandomSuffix: false, allowOverwrite: true,
            contentType: 'audio/mpeg', cacheControlMaxAge: CACHE_SEG, token,
          });
          idx[nome] = { bytes: buf.length, sha1: h };
          subidos++;
          return;
        } catch (e) {
          if (t >= 5) { falhas++; console.error(`  FALHOU ${slug}/${nome}: ${e?.message ?? e}`); return; }
          await sleep(1000 * 2 ** t);
        }
      }
    });
    gravarIndice(slug, idx);
    console.log(`  ${slug}: ${fila.length} enviado(s)`);
  }
  console.log(`audio_sync subir: ${subidos} enviado(s), ${falhas} falha(s)`);
  if (falhas) process.exit(1);
}

async function baixar(slugs) {
  if (!slugs.length) { console.error('uso: audio_sync.mjs baixar <slug> [...]'); process.exit(2); }
  let baixados = 0, falhas = 0;
  for (const slug of slugs) {
    const idx = lerIndice(slug);
    const faltam = Object.keys(idx).filter((n) => !existsSync(join(AUDIO, slug, n)));
    if (!faltam.length) continue;
    mkdirSync(join(AUDIO, slug), { recursive: true });
    await emParalelo(faltam, 16, async (nome) => {
      const url = `${BLOB_BASE}/audio/${slug}/${encodeURIComponent(nome)}`;
      for (let t = 1; ; t++) {
        try {
          const r = await fetch(url);
          if (!r.ok) throw new Error(`HTTP ${r.status}`);
          const buf = Buffer.from(await r.arrayBuffer());
          if (sha1(buf) !== idx[nome].sha1) throw new Error('sha1 diferente do indice');
          writeFileSync(join(AUDIO, slug, nome), buf);
          baixados++;
          return;
        } catch (e) {
          if (t >= 4) { falhas++; console.error(`  FALHOU ${slug}/${nome}: ${e?.message ?? e}`); return; }
          await sleep(500 * 2 ** t);
        }
      }
    });
    console.log(`  ${slug}: ${faltam.length} trazido(s) do Blob`);
  }
  console.log(`audio_sync baixar: ${baixados} trazido(s), ${falhas} falha(s)`);
  if (falhas) process.exit(1);
}

function conferir(slugs) {
  // Antes da virada o MP3 ainda vai para o git (inclusive o recem-gerado, antes do git add):
  // nao ha o que conferir contra o Blob.
  if (mp3NoGit().size) { console.log('(Blob: os MP3 ainda vao para o git como antes — nada a conferir ate a virada.)'); return; }
  const fora = [];
  for (const slug of slugsPedidos(slugs)) {
    const idx = lerIndice(slug);
    for (const nome of mp3DoDisco(slug)) {
      const e = idx[nome];
      if (!e || e.sha1 !== sha1(readFileSync(join(AUDIO, slug, nome)))) fora.push(`${slug}/${nome}`);
    }
  }
  if (fora.length) {
    console.error(`⛔ ${fora.length} MP3 no disco que o Blob nao tem (ou mudaram):`);
    for (const f of fora.slice(0, 15)) console.error(`   ${f}`);
    if (fora.length > 15) console.error(`   (+${fora.length - 15})`);
    console.error('Rode: node scripts/audio_sync.mjs subir');
    process.exit(1);
  }
  console.log('✓ audio_sync: todo MP3 do disco esta no Blob');
}

const [cmd, ...resto] = process.argv.slice(2);
if (cmd === 'subir') await subir(resto);
else if (cmd === 'baixar') await baixar(resto);
else if (cmd === 'conferir') conferir(resto);
else { console.error('uso: audio_sync.mjs subir|baixar|conferir [slug ...]'); process.exit(2); }
