/**
 * CONTROLE DE AULAS — Alumni by Better
 *
 * ┌──────────────────────────────────────────────────────────────────────────────┐
 * │ A TAB "CONTROLE DE AULAS" FOI DESATIVADA EM 14/07/2026, A PEDIDO DA HELEN.    │
 * │ Ela nao e mais exibida em nenhum hub (professor nem aluno).                   │
 * └──────────────────────────────────────────────────────────────────────────────┘
 *
 * Os dados que os professores ja preencheram (datas das aulas, feedback do aluno,
 * feedback do material) CONTINUAM na tabela `controle_aulas` do Supabase — some a
 * tela, nao o conteudo. Para trazer a tab de volta: `git revert` do PR que a removeu
 * (o codigo dela esta inteiro no historico).
 *
 * ESTE ARQUIVO CONTINUA EXISTINDO porque os 153 hubs ja publicados o carregam via
 * <script src="/lib/controle-aulas.js">. Ele agora so carrega a tab irma "Resumos das
 * Aulas" — assim a tab nova chega em todos os hubs sem editar nenhum HTML de aluno
 * (REGRA 30 — o legado e intocavel). Nao remover este arquivo sem antes limpar as
 * tags <script> dos hubs.
 */
(function() {
  'use strict';

  if (!window.__RESUMOS_AULA_LOADED && !document.querySelector('script[src="/lib/resumos-aula.js"]')) {
    var resumosScript = document.createElement('script');
    resumosScript.src = '/lib/resumos-aula.js';
    document.body.appendChild(resumosScript);
  }

})();
