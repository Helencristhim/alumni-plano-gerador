/**
 * Valida a senha de acesso do aluno — NO SERVIDOR.
 *
 * Por que servidor e nao um hash no HTML: o repositorio e PUBLICO. Um hash de 4 digitos
 * publicado se quebra por forca bruta offline em milissegundos, o que daria a sensacao de
 * protecao sem a protecao. Aqui as senhas vivem na env var ACESSO_ALUNOS (Vercel), nunca
 * no git, e quem quiser adivinhar tem de fazer 10.000 requisicoes pela rede.
 *
 * O que isto protege, e o que NAO protege — sem ilusao:
 *   PROTEGE  o uso casual: link aberto por engano, colega curioso, alguem testando na
 *            pagina errada. Foi assim que o Pre-class do rafael-pelizaro apareceu todo
 *            respondido em 19/08/2026.
 *   NAO PROTEGE  contra quem sabe usar F12 ou `curl`: o HTML continua sendo servido
 *            estaticamente, entao o conteudo e alcancavel por fora do bloqueio. Fechar
 *            isso exige middleware que segure o proprio HTML — outro trabalho.
 *
 * Gerar/rotacionar senhas: scripts/gerar_senhas_alunos.py
 */
const MAPA = (() => {
  try { return JSON.parse(process.env.ACESSO_ALUNOS || '{}'); }
  catch (e) { console.error('ACESSO_ALUNOS mal formado:', e.message); return {}; }
})();

const espera = (ms) => new Promise((r) => setTimeout(r, ms));

module.exports = async (req, res) => {
  if (req.method !== 'POST') return res.status(405).json({ ok: false });

  const { slug, senha } = req.body || {};
  if (!slug || typeof slug !== 'string') return res.status(400).json({ ok: false });

  // Sem env configurada o acesso fica LIBERADO de proposito: uma variavel que nao subiu
  // nao pode trancar 123 alunos para fora do material deles.
  if (Object.keys(MAPA).length === 0) {
    return res.status(200).json({ ok: true, semSenha: true });
  }

  const esperado = MAPA[slug];
  if (!esperado) return res.status(200).json({ ok: true, semSenha: true });

  // Custo fixo por tentativa: torna a varredura das 10.000 combinacoes lenta o bastante
  // para nao valer a pena, sem depender de estado entre requisicoes.
  await espera(400);

  if (String(senha || '') !== String(esperado)) {
    return res.status(401).json({ ok: false });
  }
  return res.status(200).json({ ok: true });
};
