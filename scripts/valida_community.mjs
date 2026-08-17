// Validacao final do doc (secao 7) medida no NAVEGADOR, servida por HTTP.
// Nao verifica "se o HTML abre": clica, mede estado computado e conta.
import { chromium } from 'playwright';

const BASE = process.env.BASE || 'http://127.0.0.1:8899/community/fernanda/';
const PAGES = [
  'index.html',
  'when-is-the-party.html',
  'same-week-different-days.html',
  'who-looks-after-them.html',
  'who-is-that.html',
  'where-from.html',
];

const browser = await chromium.launch();
let falhas = 0;
const falhar = (m) => { falhas++; console.log('  FALHA  ' + m); };
const ok = (m) => console.log('  ok     ' + m);

// ---------- rotas do hub ----------
{
  const page = await browser.newPage();
  await page.goto(BASE + 'index.html');
  const links = await page.$$eval('a[href$=".html"]', as => as.map(a => a.getAttribute('href')));
  const alvos = [...new Set(links)];
  console.log(`\n== HUB: ${alvos.length} rota(s) no catalogo ==`);
  for (const href of alvos) {
    const r = await page.goto(new URL(href, BASE + 'index.html').href);
    const st = r.status();
    const t = await page.title();
    if (st !== 200) falhar(`rota ${href} -> HTTP ${st}`);
    else ok(`rota ${href} -> 200  "${t}"`);
    await page.goBack();
  }
  // volta ao catalogo a partir de um material
  await page.goto(BASE + 'when-is-the-party.html');
  const back = await page.$$eval('a[href="./"]', as => as.length);
  if (back < 1) falhar('material sem link de volta ao catalogo'); else ok(`link de volta ao catalogo (${back}x)`);
  await page.close();
}

for (const p of PAGES.filter(p => p !== 'index.html')) {
  console.log(`\n== ${p} ==`);
  const page = await browser.newPage({ viewport: { width: 380, height: 800 } });
  const erros = [];
  page.on('pageerror', e => erros.push(e.message));
  const req404 = [];
  page.on('response', r => { if (r.status() >= 400) req404.push(r.url().split('/').pop() + ' ' + r.status()); });
  await page.goto(BASE + p);
  await page.waitForTimeout(700);

  // 1) NENHUMA traducao visivel no carregamento
  const trAbertas = await page.$$eval('.tr', els =>
    els.filter(e => getComputedStyle(e).display !== 'none' && e.offsetParent !== null)
       .map(e => e.textContent.trim().slice(0, 60)));
  if (trAbertas.length) falhar(`${trAbertas.length} traducao(oes) ABERTA(S) no load: ${JSON.stringify(trAbertas)}`);
  else ok('nenhuma traducao aberta no carregamento');

  // 2) toggle ver/ocultar portugues
  const tog = await page.$('.tr-toggle');
  if (!tog) falhar('sem botao "ver em portugues"');
  else {
    await tog.click(); await page.waitForTimeout(200);
    const visivel = await page.$$eval('.tr', els => els.some(e => getComputedStyle(e).display !== 'none'));
    const rot1 = (await tog.textContent()).trim();
    await tog.click(); await page.waitForTimeout(200);
    const aindaVis = await page.$$eval('.tr', els => els.filter(e => getComputedStyle(e).display !== 'none').length);
    const rot2 = (await tog.textContent()).trim();
    if (visivel && aindaVis === 0 && rot1 === 'ocultar português' && rot2 === 'ver em português') ok('toggle PT abre e fecha (rotulo alterna)');
    else falhar(`toggle PT: abriu=${visivel} sobrou=${aindaVis} rotulos="${rot1}"/"${rot2}"`);
  }

  // 3) orientacao em PT que NAO e traducao fica visivel (classe propria, 1.1)
  const ptNotes = await page.$$eval('.pt-note', els =>
    els.map(e => ({ vis: getComputedStyle(e).display !== 'none', txt: e.textContent.trim().slice(0, 50) })));
  if (ptNotes.length) {
    const escondida = ptNotes.filter(x => !x.vis);
    if (escondida.length) falhar(`.pt-note escondida: ${JSON.stringify(escondida)}`);
    else ok(`${ptNotes.length} orientacao(oes) .pt-note visivel(is), fora do regime .tr`);
  }

  // 4) TODO botao de audio tem MP3 no AUDIO_MAP e o arquivo responde 200
  const audio = await page.evaluate(async () => {
    const map = window.AUDIO_MAP || {};
    const pedidos = [...document.querySelectorAll('[data-say]')].map(b => b.getAttribute('data-say'));
    const semMapa = [...new Set(pedidos.filter(t => !map[t]))];
    const arquivos = [...new Set(Object.values(map))];
    const ruins = [];
    for (const f of arquivos) {
      const r = await fetch('audio/' + f, { method: 'HEAD' });
      if (!r.ok) ruins.push(f + ' ' + r.status);
    }
    return { botoes: pedidos.length, entradas: Object.keys(map).length, semMapa, ruins };
  });
  if (audio.semMapa.length) falhar(`${audio.semMapa.length} frase(s) sem MP3 no AUDIO_MAP: ${JSON.stringify(audio.semMapa)}`);
  else ok(`${audio.botoes} botoes de audio, ${audio.entradas} entradas no AUDIO_MAP, 0 sem MP3`);
  if (audio.ruins.length) falhar(`MP3 que nao responde: ${JSON.stringify(audio.ruins)}`);
  else ok(`${audio.entradas} MP3 servidos com 200`);

  // 5) o audio TOCA de fato (a fonte e o MP3, nao o sintetizador)
  const toca = await page.evaluate(() => new Promise(res => {
    const b = document.querySelector('[data-say]');
    if (!b) return res('sem botao');
    const orig = window.Audio;
    let src = null;
    window.Audio = function (s) { src = s; const a = new orig(s); a.play = () => Promise.resolve(); return a; };
    (b.querySelector('button') || b).click();
    setTimeout(() => { window.Audio = orig; res(src || 'NENHUM Audio() criado'); }, 400);
  }));
  if (typeof toca === 'string' && toca.includes('audio/')) ok(`play usa MP3: ${toca.split('/').pop()}`);
  else falhar(`play NAO criou Audio() com MP3: ${toca}`);

  // 6) videos: iframe montado + link alternativo
  const vids = await page.$$eval('.video[data-video]', els => els.map(e => ({
    id: e.getAttribute('data-video'),
    iframe: !!e.querySelector('iframe'),
    link: e.querySelector('a.video-link')?.getAttribute('href') || null,
    instr: (e.closest('.moment')?.querySelector('.en-instr')?.textContent || '').trim(),
  })));
  for (const v of vids) {
    const temFoco = /look for|look at/i.test(v.instr);
    const soNomear = /^watch.*(what do you see\?)$/i.test(v.instr);
    if (!v.iframe) falhar(`video ${v.id} sem iframe`);
    else if (!v.link) falhar(`video ${v.id} sem link alternativo`);
    else if (!temFoco) falhar(`video ${v.id} sem FOCO DE OBSERVACAO na instrucao: "${v.instr}"`);
    else if (soNomear) falhar(`video ${v.id} termina na nomeacao: "${v.instr}"`);
    else ok(`video ${v.id}: iframe + link + foco de observacao`);
  }

  // 7) interativos: cartas, seletores, planejador, escrita, gerador de nome
  const inter = await page.evaluate(() => {
    const r = {};
    const rev = document.querySelector('[data-reveal]');
    if (rev) {
      const card = document.getElementById(rev.getAttribute('data-reveal'));
      rev.click(); const abriu = card.classList.contains('open');
      rev.click(); const fechou = !card.classList.contains('open');
      r.reveal = abriu && fechou ? 'toggle ok' : `abriu=${abriu} fechou=${fechou}`;
    }
    const ta = [...document.querySelectorAll('textarea')];
    r.textareas = ta.map(t => ({ id: t.id, ph: t.placeholder, aria: t.getAttribute('aria-label') }));
    const nb = document.getElementById('dadname');
    if (nb) {
      nb.value = 'Jón';
      nb.dispatchEvent(new Event('input', { bubbles: true }));
      r.nameGen = document.getElementById('nbout').textContent.trim();
      r.nameLabel = document.querySelector('label[for="dadname"]').textContent.trim();
    }
    r.rec = [...document.querySelectorAll('.rec')].length;
    r.pron = [...document.querySelectorAll('.pron')].length;
    r.picks = [...document.querySelectorAll('.pickcard')].length;
    r.dayBtns = [...document.querySelectorAll('[data-day]')].length;
    return r;
  });
  if (inter.reveal) (inter.reveal === 'toggle ok' ? ok('cartas abrem E FECHAM (toggle)') : falhar('carta: ' + inter.reveal));
  for (const t of inter.textareas) ok(`campo de escrita #${t.id}: placeholder="${t.ph}" aria="${t.aria}"`);
  if (inter.nameGen) ok(`gerador de nome: label="${inter.nameLabel}" -> "${inter.nameGen}"`);
  const extras = [];
  if (inter.rec) extras.push(`${inter.rec} gravacao(oes)`);
  if (inter.pron) extras.push(`${inter.pron} pronome(s) clicavel(is)`);
  if (inter.picks) extras.push(`${inter.picks} cartao(oes) de escolha`);
  if (inter.dayBtns) extras.push(`${inter.dayBtns} seletor(es) de dia`);
  if (extras.length) ok('interativos: ' + extras.join(', '));

  // 8) gravacao e OPCIONAL: a atividade vale sem ela
  const gravOpc = await page.$$eval('.rec', els => els.every(e => !e.required && !e.disabled));
  if (inter.rec && !gravOpc) falhar('gravacao parece obrigatoria');
  else if (inter.rec) ok('gravacao opcional (nada bloqueia sem ela)');

  // 9) regime NAO avaliativo: zero score/gabarito/porcentagem na tela
  const aval = await page.evaluate(() => {
    // O footer traz a referencia da unidade ("Essential 1 / 02 Favorite holidays"): e
    // catalogo, nao contador de acertos. Medir o CORPO das atividades, sem footer/header.
    const txt = [...document.querySelectorAll('.moment')].map(m => m.innerText).join('\n');
    const marcas = [];
    if (/\b\d+\s*\/\s*\d+\b/.test(txt)) marcas.push('contador X/Y');
    if (/\b\d+%/.test(txt)) marcas.push('porcentagem');
    if (/correct|incorrect|wrong answer|acertou|errou|gabarito/i.test(txt)) marcas.push('certo/errado');
    if (document.querySelector('progress, [role="progressbar"]')) marcas.push('barra de progresso');
    return marcas;
  });
  if (aval.length) falhar('marca avaliativa na tela: ' + aval.join(', '));
  else ok('regime nao avaliativo: sem score, gabarito, % ou progresso');

  // 10) 380px sem rolagem horizontal
  const overflow = await page.evaluate(() => {
    const de = document.documentElement;
    const culpados = [...document.querySelectorAll('*')]
      .filter(e => e.getBoundingClientRect().right > de.clientWidth + 1)
      .slice(0, 4).map(e => e.tagName.toLowerCase() + '.' + (e.className || '').toString().split(' ')[0]);
    return { scrollW: de.scrollWidth, clientW: de.clientWidth, culpados };
  });
  if (overflow.scrollW > overflow.clientW + 1) falhar(`rolagem horizontal em 380px (${overflow.scrollW} > ${overflow.clientW}): ${JSON.stringify(overflow.culpados)}`);
  else ok('380px sem rolagem horizontal');

  // 11) reading: 2-3 paragrafos curtos, audio por paragrafo, reacao nao avaliativa
  const read = await page.$$eval('article.reading', arts => arts.map(a => ({
    pars: a.querySelectorAll('.r-par').length,
    comAudio: [...a.querySelectorAll('.r-par')].filter(p => p.querySelector('[data-say]')).length,
  })));
  for (const r of read) {
    if (r.pars < 2 || r.pars > 3) falhar(`reading com ${r.pars} paragrafos (esperado 2-3)`);
    else if (r.comAudio !== r.pars) falhar(`reading: ${r.comAudio}/${r.pars} paragrafos com audio`);
    else ok(`reading: ${r.pars} paragrafos, todos com audio`);
  }

  // 12) console limpo e nenhum recurso 404
  if (erros.length) falhar('erro de JS: ' + erros[0]);
  else ok('console sem erro de JS');
  const faltantes = req404.filter(x => !x.includes('favicon'));
  if (faltantes.length) falhar('recurso ausente: ' + faltantes.slice(0, 3).join(', '));
  else ok('nenhum recurso 404');

  await page.close();
}

await browser.close();
console.log(falhas ? `\n${falhas} FALHA(S)` : '\nTUDO PASSOU');
process.exit(falhas ? 1 : 0);
