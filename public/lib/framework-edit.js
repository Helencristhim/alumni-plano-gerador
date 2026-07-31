/**
 * A EDIÇÃO DE UM FRAMEWORK, EM UM LUGAR SÓ.
 *
 * Este arquivo é carregado pelos DOIS lados: pelo navegador (catálogo, no botão
 * "baixar JSON" e na prévia) e pela função serverless (api/save-framework.js, que
 * abre o PR). É de propósito: se a mutação existisse duas vezes, o arquivo baixado
 * e o arquivo do PR divergiriam no primeiro ajuste — e ninguém perceberia, porque os
 * dois "funcionam".
 *
 * As duas regras que moram aqui (e o motivo delas):
 *
 * 1. `status` não se edita. Promover um método a "producao" é o que libera ALUNO REAL
 *    a recebê-lo (GATE 11). Isso é decisão pedagógica, feita no código com revisão —
 *    não um clique numa tela. Framework novo nasce sempre "mock".
 *
 * 2. Contrato nunca se edita no lugar: SOBE a versão e a anterior vai pro histórico.
 *    Cada aula carimba a versão em que nasceu e o GATE 12 a julga por ela. Sem isso,
 *    tirar um exercício do contrato reprovaria centenas de aulas já publicadas — e a
 *    saída seria desligar o gate. Ver _build/model/FRAMEWORKS.md §7.
 */
(function (raiz) {
  'use strict';

  function contratoIgual(a, b) {
    if (!a || !b) return false;
    var norm = function (c) {
      return JSON.stringify({
        o: (c.obrigatorios || []).slice().sort(),
        p: (c.proibidos || []).slice().sort(),
        m: c.min_slides || null
      });
    };
    return norm(a) === norm(b);
  }

  /**
   * Aplica a edição e devolve { dados, resumoMudanca, novo }.
   * `dados` é MUTADO (o chamador passa uma cópia se quiser preservar o original).
   * Lança Error com mensagem em português quando o pedido é inválido.
   */
  function aplicarEdicao(dados, banco, p) {
    if (!p || !p.categoria || !p.id || !p.label) {
      throw new Error('categoria, id e label são obrigatórios');
    }
    if (!/^[a-z0-9][a-z0-9-]{1,40}$/.test(p.id)) {
      throw new Error('o id deve ser minúsculo e sem espaço (ex.: "task-based")');
    }

    var validos = {};
    (banco.exercicios || []).forEach(function (e) { validos[e.id] = true; });
    ['obrigatorios', 'proibidos'].forEach(function (lista) {
      ((p.contrato && p.contrato[lista]) || []).forEach(function (eid) {
        if (!validos[eid]) {
          throw new Error('o exercício "' + eid + '" não existe no banco. O banco é gerado ' +
                          'do builder — só dá pra exigir o que o builder sabe montar.');
        }
      });
    });
    var obr = (p.contrato && p.contrato.obrigatorios) || [];
    var pro = (p.contrato && p.contrato.proibidos) || [];
    var choque = obr.filter(function (e) { return pro.indexOf(e) !== -1; });
    if (choque.length) {
      throw new Error('"' + choque[0] + '" está como obrigatório E proibido ao mesmo tempo.');
    }

    var cat = (dados.categorias || []).filter(function (c) { return c.id === p.categoria; })[0];
    if (!cat) throw new Error('a categoria "' + p.categoria + '" não existe');

    cat.frameworks = cat.frameworks || [];
    var fw = cat.frameworks.filter(function (f) { return f.id === p.id; })[0];
    var novo = !fw;

    if (novo) {
      fw = { id: p.id, label: p.label, status: 'mock', resumo: p.resumo || '' };
      cat.frameworks.push(fw);
      dados.mocks = dados.mocks || {};
      dados.mocks[p.id] = dados.mocks[p.id] || [];
    } else {
      fw.label = p.label;
      if (p.resumo !== undefined) fw.resumo = p.resumo;
    }

    var resumoMudanca = novo ? 'método criado (status mock)' : 'rótulo/resumo atualizados';
    if (p.contrato) {
      var atual = fw.contrato;
      var autoria = p.origem || ('editado' + (p.autor ? ' por ' + p.autor : ''));
      if (!atual) {
        fw.contrato = { versao: 1, origem: p.origem || ('criado no catálogo' + (p.autor ? ' por ' + p.autor : '')),
                        obrigatorios: obr, proibidos: pro,
                        min_slides: p.contrato.min_slides || null };
        fw.contrato_historico = [];
        resumoMudanca = 'contrato v1 criado';
      } else if (!contratoIgual(atual, p.contrato)) {
        fw.contrato_historico = fw.contrato_historico || [];
        fw.contrato_historico.push(atual);
        fw.contrato = { versao: Number(atual.versao) + 1, origem: autoria,
                        obrigatorios: obr, proibidos: pro,
                        min_slides: p.contrato.min_slides || null };
        resumoMudanca = 'contrato v' + atual.versao + ' → v' + fw.contrato.versao +
                        ' (a v' + atual.versao + ' foi para o histórico)';
      }
    }

    return { dados: dados, resumoMudanca: resumoMudanca, novo: novo };
  }

  var api = { aplicarEdicao: aplicarEdicao, contratoIgual: contratoIgual };
  if (typeof module === 'object' && module.exports) module.exports = api;
  else raiz.FrameworkEdit = api;
})(typeof globalThis !== 'undefined' ? globalThis : this);
