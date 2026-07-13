/**
 * GATE — BOTÃO MORTO (JavaScript inline que não compila)
 *
 * O BUG QUE ELE PEGA
 * ------------------
 * O gerador concatena o texto em inglês do aluno dentro de um atributo HTML que
 * contém uma string JavaScript. O apóstrofo do inglês é escapado como entidade:
 *
 *     onclick="speakText('Rachel&#39;s task is data quality.',this)"
 *
 * Parece seguro. Não é. O navegador DESESCAPA a entidade ANTES de compilar o
 * handler — `&#39;` vira `'` — e a string fecha no lugar errado:
 *
 *     speakText('Rachel's task is data quality.',this)
 *              ~~~~~~~~^ SyntaxError
 *
 * O botão morre. Silenciosamente: o HTML é válido, a página abre bonita, o
 * console fica limpo. O Chrome só compila handler inline NA HORA DO CLIQUE —
 * então o erro só existe no instante em que o aluno clica e nada acontece.
 *
 * POR QUE NENHUM VALIDADOR VIA ISSO
 * ---------------------------------
 * check_audiomap_syntax.js / check_audiomap_esprima.py parseiam o objeto
 * `audioMap` DENTRO do <script>. Nenhum validador parseia o JS que mora nos
 * ATRIBUTOS. Era o ponto cego — e é exatamente onde o texto do aluno entra.
 *
 * POR QUE NODE E NÃO PYTHON
 * -------------------------
 * `new Function(codigo)` compila no V8 — o MESMO motor do Chrome. Este gate não
 * SIMULA o navegador: ele usa o navegador. E o CI não tem `pip install`; node é
 * nativo do ubuntu-latest. Zero dependência nova.
 *
 * CRITÉRIO: "NÃO PIOROU VS A BASE" (igual ao GATE 6)
 * -------------------------------------------------
 * Existe legado quebrado. Exigir zero travaria todo PR que ENCOSTE num arquivo
 * legado — remédio pior que a doença. Então:
 *   - arquivo NOVO   → zero tolerância (nasce quebrado = PR barrado)
 *   - arquivo TOCADO → não pode ter MAIS botões mortos que na base
 * Quando o conserto do legado mergear, todo mundo vai a zero e o gate vira
 * absoluto de graça.
 *
 *   node scripts/check_inline_js.mjs public/professor/x.html        (arquivos)
 *   node scripts/check_inline_js.mjs --base origin/main <arquivos>  (CI de PR)
 *   node scripts/check_inline_js.mjs --all                          (repo todo)
 */
import { readFileSync, readdirSync } from 'node:fs';
import { execFileSync } from 'node:child_process';
import { join } from 'node:path';

/** Walk recursivo em vez de fs.globSync: globSync é Node 22+ e o CI não fixa versão. */
function htmlsEm(dir) {
  const out = [];
  for (const e of readdirSync(dir, { withFileTypes: true })) {
    const p = join(dir, e.name);
    if (e.isDirectory()) out.push(...htmlsEm(p));
    else if (e.name.endsWith('.html')) out.push(p);
  }
  return out;
}

// todo handler inline que o HTML aceita — não só onclick
const HANDLERS = [
  'onclick', 'onchange', 'oninput', 'onsubmit', 'onkeyup', 'onkeydown',
  'onkeypress', 'onfocus', 'onblur', 'onmouseover', 'onmouseout',
  'onload', 'onerror', 'ondblclick', 'onselect',
];
// aspas duplas OU simples: o navegador aceita as duas formas
const ATTR = new RegExp(`\\b(${HANDLERS.join('|')})\\s*=\\s*("([^"]*)"|'([^']*)')`, 'gi');
// dentro de <script>, "onclick" é string comum, não atributo — não é handler
const SCRIPT = /<script\b[\s\S]*?<\/script>/gi;

/** O navegador desescapa entidades HTML antes de compilar o handler. Fazemos igual. */
function desescapar(s) {
  return s
    .replace(/&#(\d+);/g, (_, d) => String.fromCodePoint(+d))
    .replace(/&#x([0-9a-f]+);/gi, (_, h) => String.fromCodePoint(parseInt(h, 16)))
    .replace(/&quot;/g, '"')
    .replace(/&apos;/g, "'")
    .replace(/&lt;/g, '<')
    .replace(/&gt;/g, '>')
    .replace(/&nbsp;/g, ' ')
    .replace(/&mdash;/g, '—')
    .replace(/&ndash;/g, '–')
    .replace(/&amp;/g, '&'); // por último: &amp;#39; -> &#39;, não -> '
}

/** Conta handlers mortos num HTML. Devolve [{linha, handler, codigo, erro}]. */
function mortos(html) {
  const corpo = html.replace(SCRIPT, (m) => ' '.repeat(m.length)); // preserva offsets
  const achados = [];

  for (const m of corpo.matchAll(ATTR)) {
    const bruto = m[3] !== undefined ? m[3] : m[4];
    const codigo = desescapar(bruto);
    try {
      // exatamente o que o browser faz: compila o atributo como corpo de função
      // (corpo de função, não script: `return false` é legal num handler)
      new Function('event', codigo);
    } catch (e) {
      achados.push({
        linha: html.slice(0, m.index).split('\n').length,
        handler: m[1].toLowerCase(),
        codigo: codigo.slice(0, 90),
        erro: e.message,
      });
    }
  }
  return achados;
}

function naBase(base, caminho) {
  try {
    const html = execFileSync('git', ['show', `${base}:${caminho}`], {
      encoding: 'utf8', maxBuffer: 128 * 1024 * 1024,
    });
    return { existe: true, n: mortos(html).length };
  } catch {
    return { existe: false, n: 0 }; // arquivo novo neste PR
  }
}

// ---------------------------------------------------------------- main
const argv = process.argv.slice(2);
let base = null;
const arquivos = [];
for (let i = 0; i < argv.length; i++) {
  if (argv[i] === '--base') base = argv[++i];
  else if (argv[i] === '--all') arquivos.push(...htmlsEm('public'));
  else if (argv[i].endsWith('.html')) arquivos.push(argv[i]);
}

if (arquivos.length === 0) {
  console.log('nenhum arquivo HTML para checar — nada a fazer.');
  process.exit(0);
}

let regrediu = false;
let totalMortos = 0;
let herdados = 0;

for (const arquivo of arquivos) {
  let html;
  try { html = readFileSync(arquivo, 'utf8'); } catch { continue; } // deletado no PR
  const achados = mortos(html);
  totalMortos += achados.length;
  if (achados.length === 0) continue;

  const b = base ? naBase(base, arquivo) : { existe: false, n: 0 };

  if (achados.length <= b.n) {
    // já estava quebrado assim antes — é legado, não é este PR
    herdados += achados.length;
    console.log(`~ ${arquivo}: ${achados.length} botão(ões) morto(s) — HERDADO da base (não piorou)`);
    continue;
  }

  regrediu = true;
  const novos = achados.length - b.n;
  const origem = b.existe ? `${b.n} na base -> ${achados.length} agora (+${novos})` : `arquivo NOVO com ${achados.length}`;
  console.log(`\n✗ ${arquivo}: ${origem}`);
  for (const a of achados.slice(0, 5)) {
    console.log(`    L${a.linha} ${a.handler}: ${a.codigo}`);
    console.log(`      V8 (motor do Chrome): ${a.erro}`);
  }
  if (achados.length > 5) console.log(`    ... e mais ${achados.length - 5}`);
}

console.log(`\narquivos checados : ${arquivos.length}`);
console.log(`handlers mortos   : ${totalMortos}${herdados ? ` (${herdados} herdados do legado)` : ''}`);

if (regrediu) {
  console.log(`
BLOQUEADO — este PR introduz botão que NÃO FUNCIONA no navegador.

O aluno clica e nada acontece. Não aparece erro no console ao carregar a página:
o Chrome só compila o handler inline no instante do clique.

CAUSA QUASE SEMPRE A MESMA: texto em inglês com apóstrofo dentro do argumento
string de um onclick.

    RUIM   onclick="speakText('Rachel&#39;s task is done.', this)"
                             o browser desescapa &#39; -> ' e a string quebra

    BOM    o texto vira CONTEÚDO/atributo, nunca argumento de string no onclick:
           <button data-speak="Rachel's task is done." onclick="speakText(this.dataset.speak, this)">
           <div class="fill-item" onclick="revealFill(this)">
             <span class="fill-answer">Rachel's task is done.</span>
           </div>

Ali apóstrofo e aspa são caracteres comuns. A classe inteira do bug deixa de existir.`);
  process.exit(1);
}

console.log('OK — todo handler inline compila no V8. Nenhum botão morto novo.');
process.exit(0);
