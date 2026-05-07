/**
 * ALUMNI — Validador de Perfil 360
 * Valida completude e integridade do perfil gerado pela API.
 * Usado no backend (antes de retornar) e no frontend (antes de renderizar).
 */

function validateProfile(data) {
  const issues = [];
  const perfil = data.perfil || data;
  const form = data.dadosFormulario || {};

  // ── NOME ──
  const nome = form.nome || data.nome || '';
  if (!nome || !nome.trim()) {
    issues.push({ severity: 'error', field: 'nome', message: 'Nome do aluno ausente nos dados do formulário.' });
  }

  // ── RESUMO EXECUTIVO ──
  const resumo = perfil.resumoExecutivo || '';
  if (!resumo) {
    issues.push({ severity: 'error', field: 'resumoExecutivo', message: 'Resumo executivo ausente.' });
  } else if (resumo.length < 100) {
    issues.push({ severity: 'warning', field: 'resumoExecutivo', message: `Resumo executivo muito curto (${resumo.length} caracteres, mínimo recomendado: 100).` });
  }

  // ── FRASES TEXTUAIS ──
  const frases = perfil.frasesTextuais || [];
  if (frases.length < 3) {
    issues.push({ severity: 'warning', field: 'frasesTextuais', message: `Apenas ${frases.length} frases textuais capturadas (mínimo: 3).` });
  }

  // ── PROMESSA TRANSFORMADORA ──
  if (!perfil.promessaTransformadora) {
    issues.push({ severity: 'error', field: 'promessaTransformadora', message: 'Promessa transformadora ausente.' });
  }

  // ── PERSONAGEM-JORNADA ──
  if (!perfil.personagemJornada) {
    issues.push({ severity: 'warning', field: 'personagemJornada', message: 'Personagem-jornada não definido.' });
  }

  // ── MAPA DE PERSONALIDADE (7 eixos obrigatórios) ──
  const mp = perfil.mapaPersonalidade || {};
  const requiredAxes = [
    'introversaoExtroversao',
    'seriedadeLudicidade',
    'reflexivoImpulsivo',
    'confianteInseguro',
    'toleranciaErro',
    'estiloAprendizagem',
    'energiaPreferida'
  ];
  const presentAxes = requiredAxes.filter(a => mp[a]);
  const missingAxes = requiredAxes.filter(a => !mp[a]);

  if (missingAxes.length > 0) {
    issues.push({
      severity: 'error',
      field: 'mapaPersonalidade',
      message: `Mapa de personalidade incompleto. Faltam ${missingAxes.length} eixos: ${missingAxes.join(', ')}.`
    });
  }

  // Verificar que cada eixo tem valor e pelo menos 1 evidência
  presentAxes.forEach(ax => {
    const eixo = mp[ax];
    if (!eixo.valor && eixo.valor !== 0) {
      issues.push({ severity: 'warning', field: `mapaPersonalidade.${ax}`, message: `Eixo ${ax}: valor não definido.` });
    }
    if (!eixo.evidencias || eixo.evidencias.length === 0) {
      issues.push({ severity: 'warning', field: `mapaPersonalidade.${ax}`, message: `Eixo ${ax}: sem evidências citadas.` });
    }
  });

  // ── FORÇAS ──
  const forcas = perfil.forcas || [];
  if (forcas.length < 3) {
    issues.push({ severity: 'warning', field: 'forcas', message: `Apenas ${forcas.length} forças identificadas (mínimo: 3).` });
  }

  // ── MELHORIAS ──
  const melhorias = perfil.melhorias || [];
  if (melhorias.length < 3) {
    issues.push({ severity: 'warning', field: 'melhorias', message: `Apenas ${melhorias.length} melhorias identificadas (mínimo: 3).` });
  }

  // ── NECESSIDADES PEDAGÓGICAS ──
  if (!perfil.necessidadesPedagogicas) {
    issues.push({ severity: 'error', field: 'necessidadesPedagogicas', message: 'Necessidades pedagógicas ausentes.' });
  }

  // ── INDICAÇÃO DE PROFESSOR ──
  const prof = perfil.indicacaoProfessor || {};
  if (!prof.perfilIdeal && !prof.descricao) {
    issues.push({ severity: 'warning', field: 'indicacaoProfessor', message: 'Indicação de professor não preenchida.' });
  }

  // ── JUSTIFICATIVA DO PROGRAMA ──
  const just = perfil.justificativaPrograma || '';
  if (!just) {
    issues.push({ severity: 'error', field: 'justificativaPrograma', message: 'Justificativa do programa ausente.' });
  } else if (just.length < 50) {
    issues.push({ severity: 'warning', field: 'justificativaPrograma', message: `Justificativa muito curta (${just.length} caracteres).` });
  }

  // ── DADOS EXTRAÍDOS ──
  const de = perfil.dadosExtraidos || {};
  const camposExtraidos = ['idade', 'profissao', 'cidade', 'nivel', 'foco', 'historico', 'eventoAlvo', 'hobbies'];
  const naoEncontrados = camposExtraidos.filter(c => {
    const campo = de[c];
    if (!campo) return true;
    return campo.encontrado === false;
  });

  if (naoEncontrados.length > 3) {
    issues.push({
      severity: 'warning',
      field: 'dadosExtraidos',
      message: `${naoEncontrados.length} campos não encontrados na consultoria: ${naoEncontrados.join(', ')}.`
    });
  }

  // ── STAKE E VITÓRIA ──
  if (!perfil.stakeAutomatico || !perfil.stakeAutomatico.texto) {
    issues.push({ severity: 'warning', field: 'stakeAutomatico', message: 'Stake automático não extraído.' });
  }
  if (!perfil.vitoriaAutomatica || !perfil.vitoriaAutomatica.texto) {
    issues.push({ severity: 'warning', field: 'vitoriaAutomatica', message: 'Vitória automática não extraída.' });
  }

  // ── RESULTADO ──
  const errors = issues.filter(i => i.severity === 'error');
  const warnings = issues.filter(i => i.severity === 'warning');

  return {
    valid: errors.length === 0,
    errors,
    warnings,
    issues,
    summary: `${errors.length} erros, ${warnings.length} avisos`
  };
}

if (typeof module !== 'undefined' && module.exports) {
  module.exports = { validateProfile };
}
