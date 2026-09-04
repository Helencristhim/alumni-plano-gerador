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
 * <script src="/lib/controle-aulas.js">. Ele agora so carrega as tabs irmas — assim
 * uma tab nova chega em todos os hubs sem editar nenhum HTML de aluno (REGRA 30 — o
 * legado e intocavel). Nao remover este arquivo sem antes limpar as tags <script>
 * dos hubs.
 *
 * TABS CARREGADAS AQUI:
 *   resumos-aula.js  — lista as aulas ja analisadas (le a tabela `analises`)
 *   family-guide.js  — recado por aula para a familia (le /data/family-guide/{slug}.json)
 *
 * As duas se auto-desligam quando nao ha o que mostrar, entao carregar sempre e
 * seguro: o family-guide, em particular, so injeta a tab se o JSON do aluno existir.
 */
(function() {
  'use strict';

  carrega('/lib/resumos-aula.js', '__RESUMOS_AULA_LOADED');
  carrega('/lib/family-guide.js', '__FAMILY_GUIDE_LOADED');

  function carrega(src, flag) {
    if (window[flag]) return;
    if (document.querySelector('script[src="' + src + '"]')) return;
    var s = document.createElement('script');
    s.src = src;
    document.body.appendChild(s);
  }

})();
