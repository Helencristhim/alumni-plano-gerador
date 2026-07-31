/**
 * POST /api/save-framework — salva a edição de um framework feita no catálogo
 * ABRINDO UM PULL REQUEST. Nunca escreve direto no main.
 *
 * POR QUE PR, E NÃO GRAVAÇÃO DIRETA
 * ---------------------------------
 * public/data/frameworks.json é lido pelo builder e por dois gates. Gravar direto no
 * main faria uma edição de navegador entrar em produção sem passar por nenhum deles.
 * Como PR, a mesma edição roda o GATE 12 (contrato × aulas), o GATE 11 (isolamento) e
 * o banco de exercícios — e só entra se estiver verde. A interface fica rápida; a
 * segurança fica no lugar onde ela já mora.
 *
 * O QUE ESTE ENDPOINT NÃO DEIXA FAZER (de propósito)
 * --------------------------------------------------
 * 1. Mudar `status`. Promover um método a "producao" libera ALUNO REAL a recebê-lo
 *    (GATE 11). Isso é decisão pedagógica, não clique de tela: continua sendo feito
 *    no código, com revisão. Framework novo nasce sempre como "mock".
 * 2. Editar um contrato NO LUGAR. Toda mudança de contrato SOBE a versão e empurra a
 *    anterior pro histórico — é o que impede uma edição de hoje reprovar aula de
 *    ontem (as aulas carimbam a versão em que nasceram). Ver _build/model/FRAMEWORKS.md §7.
 *
 * Configuração (Vercel → Settings → Environment Variables):
 *   GITHUB_TOKEN    fine-grained, no repo do projeto, com Contents:RW + Pull requests:RW
 *   CATALOGO_SENHA  senha combinada; o site é público, então sem isso qualquer um abre PR
 * Sem as duas, o endpoint responde 503 e o catálogo cai sozinho no modo "baixar JSON".
 */

const { aplicarEdicao } = require('../public/lib/framework-edit.js');

const REPO = process.env.GITHUB_REPO || 'Helencristhim/alumni-plano-gerador';
const ARQUIVO = 'public/data/frameworks.json';
const BANCO = 'public/data/exercicios.json';
const API = 'https://api.github.com';

function gh(path, token, opts = {}) {
  return fetch(API + path, {
    ...opts,
    headers: {
      Authorization: `Bearer ${token}`,
      Accept: 'application/vnd.github+json',
      'Content-Type': 'application/json',
      'User-Agent': 'alumni-catalogo',
      ...(opts.headers || {})
    }
  }).then(async (r) => {
    const body = await r.text();
    let json = null;
    try { json = JSON.parse(body); } catch (e) { /* resposta sem JSON */ }
    if (!r.ok) {
      const err = new Error(`GitHub ${r.status} em ${path}: ${(json && json.message) || body.slice(0, 200)}`);
      err.status = r.status;
      throw err;
    }
    return json;
  });
}

const b64decode = (s) => Buffer.from(s, 'base64').toString('utf8');
const b64encode = (s) => Buffer.from(s, 'utf8').toString('base64');

module.exports = async (req, res) => {
  if (req.method !== 'POST') return res.status(405).json({ error: 'Method not allowed' });

  const token = process.env.GITHUB_TOKEN;
  const senha = process.env.CATALOGO_SENHA;
  if (!token || !senha) {
    return res.status(503).json({
      error: 'Edição por PR não está configurada neste deploy (falta GITHUB_TOKEN e/ou ' +
             'CATALOGO_SENHA). Use o botão "Baixar JSON" — o arquivo baixado é exatamente ' +
             'o que entraria no PR.'
    });
  }
  if ((req.headers['x-catalogo-senha'] || '') !== senha) {
    return res.status(401).json({ error: 'Senha do catálogo incorreta.' });
  }

  try {
    const { categoria, id, label, resumo, contrato, autor } = req.body || {};
    if (!categoria || !id || !label) {
      return res.status(400).json({ error: 'categoria, id e label são obrigatórios' });
    }
    if (!/^[a-z0-9][a-z0-9-]{1,40}$/.test(id)) {
      return res.status(400).json({ error: 'id deve ser minúsculo, sem espaço (ex: "task-based")' });
    }

    // ── estado atual do repo ────────────────────────────────────────────────
    const arq = await gh(`/repos/${REPO}/contents/${encodeURIComponent(ARQUIVO)}?ref=main`, token);
    const dados = JSON.parse(b64decode(arq.content));
    const banco = JSON.parse(b64decode(
      (await gh(`/repos/${REPO}/contents/${encodeURIComponent(BANCO)}?ref=main`, token)).content));
        let mutado;
    try {
      // A MUTAÇÃO MORA EM public/lib/framework-edit.js, carregado também pelo navegador.
      // Um lugar só: o arquivo que o botão "baixar JSON" gera é byte-a-byte o que entra
      // no PR. Duas cópias divergiriam no primeiro ajuste, e as duas "funcionariam".
      mutado = aplicarEdicao(dados, banco, { categoria, id, label, resumo, contrato, autor });
    } catch (e) {
      return res.status(400).json({ error: String(e.message || e) });
    }
    const { resumoMudanca: msgContrato, novo } = mutado;

    // ── branch + commit + PR ────────────────────────────────────────────────
    const base = await gh(`/repos/${REPO}/git/ref/heads/main`, token);
    const branch = `chore/catalogo-${id}-${Date.now()}`;
    await gh(`/repos/${REPO}/git/refs`, token, {
      method: 'POST',
      body: JSON.stringify({ ref: `refs/heads/${branch}`, sha: base.object.sha })
    });

    const titulo = novo
      ? `feat(frameworks): novo método "${label}" (mock) — criado no catálogo`
      : `chore(frameworks): "${label}" editado no catálogo — ${msgContrato}`;

    await gh(`/repos/${REPO}/contents/${encodeURIComponent(ARQUIVO)}`, token, {
      method: 'PUT',
      body: JSON.stringify({
        message: titulo,
        content: b64encode(JSON.stringify(dados, null, 2) + '\n'),
        sha: arq.sha,       // se alguém editou no meio do caminho, o GitHub recusa (409)
        branch
      })
    });

    const corpo = [
      `Editado pelo **catálogo** (\`/catalogo.html\`)${autor ? ` por ${autor}` : ''}.`,
      '',
      `- método: **${label}** (\`${id}\`) na categoria **${categoria}**`,
      `- ${msgContrato}`,
      contrato && contrato.obrigatorios
        ? `- exercícios obrigatórios: ${contrato.obrigatorios.map((e) => '`' + e + '`').join(', ') || '_nenhum_'}`
        : null,
      contrato && contrato.proibidos && contrato.proibidos.length
        ? `- proibidos: ${contrato.proibidos.map((e) => '`' + e + '`').join(', ')}` : null,
      novo ? '\n> Nasce com status `mock`: **não toca aluno real** até ser promovido no código (GATE 11).' : null,
      '',
      'Aula já publicada não é afetada: cada aula carimba a versão de contrato em que nasceu ' +
      'e o GATE 12 a julga por essa versão (`_build/model/FRAMEWORKS.md` §7).'
    ].filter(Boolean).join('\n');

    const pr = await gh(`/repos/${REPO}/pulls`, token, {
      method: 'POST',
      body: JSON.stringify({ title: titulo, head: branch, base: 'main', body: corpo })
    });

    return res.status(200).json({ ok: true, pr: pr.html_url, numero: pr.number, contrato: msgContrato });
  } catch (e) {
    const conflito = e.status === 409;
    return res.status(conflito ? 409 : 500).json({
      error: conflito
        ? 'Alguém alterou o frameworks.json enquanto você editava. Recarregue o catálogo e refaça a edição.'
        : String(e.message || e)
    });
  }
};
