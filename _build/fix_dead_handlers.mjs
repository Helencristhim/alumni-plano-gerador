/**
 * CONSERTO — os 324 botões mortos (JS inline que não compila no navegador)
 *
 * A CAUSA (uma só, dois sintomas)
 * -------------------------------
 * O gerador põe o inglês do aluno DENTRO de uma string JavaScript, DENTRO de um
 * atributo HTML. Aí o texto precisa sobreviver a DOIS níveis de escape ao mesmo
 * tempo — e em inglês isso falha o tempo todo, de quatro jeitos:
 *
 *   1  &#39;   speakText('Rachel&#39;s task.')      browser desescapa -> aspa fecha errado
 *   2  '       ...?'No, I don't work here.':...    apóstrofo cru fecha a string
 *   3  \\'     ...?'At nine o\\'clock':...         barra escapa a barra, aspa fecha
 *   4  \"      ...?\"I can't see your screen.\":.. barra NÃO escapa em atributo HTML:
 *                                                  o browser fecha o ATRIBUTO no ", e o
 *                                                  resto da resposta VAZA para dentro da
 *                                                  tag como lixo de atributo
 *
 * O CONSERTO (não é remendo: mata a classe)
 * -----------------------------------------
 * O texto sai de dentro da string JS e vira ATRIBUTO. Em atributo, apóstrofo e
 * aspa são caracteres comuns — não há string para fechar, não há o que quebrar.
 *
 *   ANTES  onclick="speakText('Rachel&#39;s task.',this)"
 *   DEPOIS data-speak="Rachel's task." onclick="speakText(this.dataset.speak,this)"
 *
 *   ANTES  onclick="this.textContent=this.textContent==='Show'?'RESP':'Show'"
 *   DEPOIS data-t="Show" data-a="RESP"
 *          onclick="this.textContent=this.textContent===this.dataset.t?this.dataset.a:this.dataset.t"
 *
 * Zero CSS novo, zero função nova, zero dependência. A semântica é idêntica.
 *
 * O CASO 4 SÓ É RECUPERÁVEL PORQUE O ARQUIVO ESTÁ INTACTO
 * ------------------------------------------------------
 * Quem se estilhaça é o PARSE do navegador, não a fonte. O texto vazado continua
 * lá, em ordem, no arquivo. Por isso o regex roda sobre a FONTE CRUA — e recupera
 * a resposta inteira, inclusive a que o browser jogou fora.
 *
 * SÓ TOCA NO QUE ESTÁ QUEBRADO
 * ----------------------------
 * Cada handler é compilado no V8 (new Function = o motor do Chrome) ANTES de ser
 * mexido. Se compila, não se toca — são 5.085 handlers que funcionam, em material
 * de aluno ATIVO (REGRA 12/21). Reescrever o que funciona é risco sem prêmio.
 *
 *   node _build/fix_dead_handlers.mjs --dry-run
 *   node _build/fix_dead_handlers.mjs
 */
import { readFileSync, writeFileSync, readdirSync } from 'node:fs';
import { join } from 'node:path';

const DRY = process.argv.includes('--dry-run');

function htmls(dir) {
  const out = [];
  for (const e of readdirSync(dir, { withFileTypes: true })) {
    const p = join(dir, e.name);
    if (e.isDirectory()) out.push(...htmls(p));
    else if (e.name.endsWith('.html')) out.push(p);
  }
  return out;
}

const desescaparHtml = (s) => s
  .replace(/&#(\d+);/g, (_, d) => String.fromCodePoint(+d))
  .replace(/&#x([0-9a-f]+);/gi, (_, h) => String.fromCodePoint(parseInt(h, 16)))
  .replace(/&quot;/g, '"').replace(/&apos;/g, "'")
  .replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&nbsp;/g, ' ')
  .replace(/&mdash;/g, '—').replace(/&ndash;/g, '–')
  .replace(/&amp;/g, '&');

/** Compila como o Chrome compila um handler inline. */
const compila = (js) => { try { new Function('event', js); return true; } catch { return false; } };

/**
 * O handler JÁ FUNCIONA no navegador?
 *
 * ATENÇÃO — a pegadinha que me pegou: NÃO se testa o código que o regex reconstruiu.
 * Isso é o que o autor QUIS escrever; o navegador recebe outra coisa. Barra invertida
 * não escapa nada em atributo HTML: o atributo termina na PRIMEIRA aspa dupla, ponto.
 *
 *   onclick="...?'"That is overpriced."':'Show Answer'"
 *                 ^ para o navegador, o atributo ACABA aqui
 *
 * Reconstruído, aquilo é um ternário JS perfeitamente válido — e a guarda ingênua dizia
 * "compila, não mexe", pulando justamente os quebrados. Então cortamos igual ao browser:
 * do onclick=" até a primeira ", e só então compilamos.
 */
function jaFunciona(todo) {
  const m = todo.match(/^on\w+="([^"]*)"?/i);
  return m ? compila(desescaparHtml(m[1])) : false;
}

/** Tira as aspas da string JS e desfaz os escapes JS. Devolve o TEXTO que o autor quis. */
function textoPretendido(bruto) {
  let s = bruto.trim();
  // a string pode vir como '...', "...", \"...\", \'...\'
  for (const q of ['\\"', "\\'", '"', "'"]) {
    if (s.startsWith(q) && s.endsWith(q) && s.length > 2 * q.length - 1) { s = s.slice(q.length, -q.length); break; }
  }
  // escapes de string JS -> caractere literal (ordem importa: \\' antes de \\)
  s = s.replace(/\\\\'/g, "'").replace(/\\'/g, "'").replace(/\\"/g, '"').replace(/\\\\/g, '\\');
  return desescaparHtml(s).trim();
}

/** Escapa um texto para viver como VALOR de atributo entre aspas duplas. */
const paraAtributo = (t) => t
  .replace(/&/g, '&amp;').replace(/"/g, '&quot;')
  .replace(/</g, '&lt;').replace(/>/g, '&gt;');

// LIMITE DE SANIDADE: um handler inline tem dezenas de caracteres, nunca milhares.
// Se o regex casar algo gigante, ele atravessou o atributo e está comendo o documento.
// (Foi exatamente o que aconteceu na 1a versão: `[\s\S]*` guloso "consertou" 2.182
// arquivos onde só há 324 quebrados. O dry-run pegou. Por isso a trava fica aqui.)
const MAX = 600;

// ---- padrão A: speakText('TEXTO', this), com ou sem `event.stopPropagation();` na frente
// [^"]* = o valor do atributo NÃO pode conter aspa dupla — é ela que o termina no HTML.
// Guloso até a última ' antes de `,this)`, mas preso DENTRO do atributo.
const SPEAK = /onclick="(event\.stopPropagation\(\);\s*)?speakText\(\s*'([^"]*)'\s*(?:,\s*this\s*)?\)\s*;?\s*"/gi;

// ---- padrão B: this.textContent = this.textContent === 'TRIGGER' ? 'RESP' : 'TRIGGER'
// A resposta é LAZY e pode conter " (caso 4: o \" que o browser usa para fechar o
// atributo cedo, vazando o resto para dentro da tag). Mas NUNCA pode conter `>`:
// o handler mora dentro de uma tag, e `>` é o fim dela. Sem esse limite o regex
// pula para o handler SEGUINTE e a substituição apaga o HTML do meio.
const TOGGLE = /onclick="this\.textContent\s*=\s*this\.textContent\s*===\s*(['"])([^'"]*)\1\s*\?\s*([^>]*?)\s*:\s*\\?(['"])\2\\?\4\s*;?\s*"/gi;

let arquivosTocados = 0, speakFix = 0, toggleFix = 0;
const textosPerdidos = [];

for (const arquivo of htmls('public')) {
  const antes = readFileSync(arquivo, 'utf8');
  if (!/onclick="(speakText\(|this\.textContent)/i.test(antes)) continue;

  let depois = antes;

  /** Um match legítimo cobre UM handler. Se contém outro `onclick=` dentro, o regex
   *  atravessou a fronteira da tag e a substituição apagaria o HTML do meio. Recusa. */
  const vazou = (todo, arquivo) => {
    if (todo.length > MAX) { textosPerdidos.push(`${arquivo}: match de ${todo.length} chars — regex vazou`); return true; }
    if (todo.slice(1).match(/\bon(click|change|input)\s*=/i)) { textosPerdidos.push(`${arquivo}: match engoliu outro handler`); return true; }
    return false;
  };

  depois = depois.replace(SPEAK, (todo, _pref, bruto) => {
    if (vazou(todo, arquivo)) return todo;
    if (jaFunciona(todo)) return todo; // já funciona no navegador: NÃO TOCA
    const texto = textoPretendido(`'${bruto}'`);
    if (!texto) { textosPerdidos.push(`${arquivo}: speakText vazio`); return todo; }
    speakFix++;
    const prefixo = _pref ? 'event.stopPropagation();' : '';
    return `data-speak="${paraAtributo(texto)}" onclick="${prefixo}speakText(this.dataset.speak,this)"`;
  });

  depois = depois.replace(TOGGLE, (todo, _q, gatilho, resposta) => {
    if (vazou(todo, arquivo)) return todo;
    if (jaFunciona(todo)) return todo; // já funciona no navegador: NÃO TOCA
    const t = textoPretendido(`'${gatilho}'`);
    const a = textoPretendido(resposta);
    if (!a) { textosPerdidos.push(`${arquivo}: resposta vazia`); return todo; }
    toggleFix++;
    return `data-t="${paraAtributo(t)}" data-a="${paraAtributo(a)}" ` +
           `onclick="this.textContent=this.textContent===this.dataset.t?this.dataset.a:this.dataset.t"`;
  });

  if (depois !== antes) {
    arquivosTocados++;
    if (!DRY) writeFileSync(arquivo, depois, 'utf8');
  }
}

console.log(`arquivos tocados        : ${arquivosTocados}`);
console.log(`speakText consertados   : ${speakFix}   (o áudio da aula)`);
console.log(`show-answer consertados : ${toggleFix}   (o gabarito)`);
console.log(`TOTAL                   : ${speakFix + toggleFix}`);
if (textosPerdidos.length) {
  console.log(`\n!! ${textosPerdidos.length} não convertidos (texto não recuperável):`);
  textosPerdidos.slice(0, 10).forEach((t) => console.log('   ' + t));
}
if (DRY) console.log('\n(dry-run — nada foi gravado)');
