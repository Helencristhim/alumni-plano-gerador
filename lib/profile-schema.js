/**
 * ALUMNI — Profile Schema (Fonte Única de Verdade)
 *
 * Define EXATAMENTE qual estrutura JSON o sistema espera.
 * Usado por: API (validação antes de retornar), Frontend (antes de salvar e renderizar).
 * Adicionar campo = atualizar AQUI e nada mais.
 */

const PROFILE_SCHEMA = {
  // Dados do formulário (preenchidos pelo gestor)
  dadosFormulario: {
    // Bloco 1 — Perfil Pessoal
    nome:              { type: 'string', required: true, label: 'Nome completo' },
    email:             { type: 'string', required: true, label: 'Email do aluno' },
    idade:             { type: 'any',    required: false, label: 'Idade' },
    profissao:         { type: 'string', required: false, label: 'Profissão' },
    cidade:            { type: 'string', required: false, label: 'Cidade' },
    sexo:              { type: 'string', required: false, label: 'Sexo' },
    modalidadeTrabalho:{ type: 'string', required: false, label: 'Modalidade de trabalho' },
    whatsapp:          { type: 'string', required: false, label: 'WhatsApp' },
    // Bloco 2 — Programa
    foco:              { type: 'string', required: false, label: 'Foco principal' },
    numAulas:          { type: 'any',    required: true, label: 'Número de aulas' },
    duracao:           { type: 'string', required: true, label: 'Duração da aula' },
    frequencia:        { type: 'string', required: true, label: 'Frequência semanal' },
    modalidadeAula:    { type: 'string', required: false, label: 'Modalidade da aula' },
    plataforma:        { type: 'string', required: false, label: 'Plataforma' },
    horarios:          { type: 'string', required: false, label: 'Horários' },
    // Bloco 3 — Urgência
    existeEvento:      { type: 'any',    required: false, label: 'Tem evento marcado' },
    tipoEvento:        { type: 'string', required: false, label: 'Tipo do evento' },
    dataEvento:        { type: 'string', required: false, label: 'Data do evento' },
    localEvento:       { type: 'string', required: false, label: 'Local do evento' },
    // Bloco 4 — Motivação
    stake:             { type: 'string', required: false, label: 'Stake' },
    vitoria:           { type: 'string', required: false, label: 'Vitória' },
    // Bloco 5 — Histórico
    historicoIngles:   { type: 'string', required: false, label: 'Histórico com inglês' },
    nivel:             { type: 'string', required: false, label: 'Nível declarado' },
    tempoForaAula:     { type: 'string', required: false, label: 'Tempo fora de aula' },
    // Bloco 6 — Personalidade
    estiloAprendizagem:{ type: 'string', required: false, label: 'Estilo de aprendizagem' },
    estruturaPreferida:{ type: 'string', required: false, label: 'Estrutura preferida' },
    lidaComErros:      { type: 'string', required: false, label: 'Como lida com erros' },
    energiaPreferida:  { type: 'string', required: false, label: 'Energia preferida' },
    // Bloco 7 — Interesses
    seriesFilmes:      { type: 'string', required: false, label: 'Séries e filmes' },
    musicasPodcasts:   { type: 'string', required: false, label: 'Músicas e podcasts' },
    hobbies:           { type: 'string', required: false, label: 'Hobbies' },
    // Bloco 8 — Consultoria
    temAudio:          { type: 'any',    required: false, label: 'Tem áudio' },
  },

  // Perfil gerado pela IA
  perfil: {
    resumoExecutivo: {
      type: 'string', required: true, minLength: 100,
      label: 'Resumo Executivo',
      renderType: 'textarea',
      section: 1,
    },
    frasesTextuais: {
      type: 'array', required: true, minItems: 3,
      label: 'Frases Textuais Capturadas',
      itemShape: { frase: 'string', uso: 'string', contexto: 'string' },
      renderType: 'frase-list',
      section: 1,
    },
    promessaTransformadora: {
      type: 'string', required: true,
      label: 'Promessa Transformadora',
      renderType: 'text-highlight',
      section: 1,
    },
    personagemJornada: {
      type: 'object', required: true,
      label: 'Personagem-Jornada',
      fields: { de: 'string', para: 'string', emQuantasAulas: 'number' },
      renderType: 'journey-card',
      section: 1,
    },
    mapaPersonalidade: {
      type: 'object', required: true, minKeys: 7,
      label: 'Mapa de Personalidade',
      requiredKeys: [
        'introversaoExtroversao', 'seriedadeLudicidade', 'reflexivoImpulsivo',
        'confianteInseguro', 'toleranciaErro', 'estiloAprendizagem', 'energiaPreferida'
      ],
      keyLabels: {
        introversaoExtroversao: 'Introversão ↔ Extroversão',
        seriedadeLudicidade: 'Sério ↔ Brincalhão',
        reflexivoImpulsivo: 'Reflexivo ↔ Impulsivo',
        confianteInseguro: 'Confiante ↔ Inseguro com idioma',
        toleranciaErro: 'Tolerância ao Erro',
        estiloAprendizagem: 'Estilo de Aprendizagem',
        energiaPreferida: 'Energia Preferida em Aula',
      },
      itemShape: { valor: 'any', inferencia: 'string', confianca: 'number', selo: 'string', evidencias: 'array' },
      renderType: 'personality-map',
      section: 2,
    },
    forcas: {
      type: 'array', required: true, minItems: 3,
      label: 'Forças',
      itemShape: { item: 'string', selo: 'string', evidencia: 'string' },
      renderType: 'strength-list',
      section: 3,
    },
    melhorias: {
      type: 'array', required: true, minItems: 3,
      label: 'Pontos de Melhoria',
      itemShape: { item: 'string', selo: 'string', evidencia: 'string' },
      renderType: 'improvement-list',
      section: 3,
    },
    necessidadesPedagogicas: {
      type: 'object', required: true,
      label: 'Necessidades Pedagógicas',
      fields: {
        adaptacaoNivel: 'string', adaptacaoIdade: 'string',
        estiloAprendizagem: 'string', toleranciaTraducao: 'string',
        ritmoIdeal: 'string', tiposExercicio: 'array',
        midiasApropriadas: 'array', adaptacaoModalidade: 'string',
      },
      renderType: 'info-grid',
      section: 4,
    },
    indicacaoProfessor: {
      type: 'object', required: true,
      label: 'Indicação de Professor',
      fields: { perfilIdeal: 'string', justificativa: 'array', nome: 'string' },
      renderType: 'professor-card',
      section: 5,
    },
    justificativaPrograma: {
      type: 'string', required: true, minLength: 50,
      label: 'Justificativa do Programa',
      renderType: 'textarea',
      section: 6,
    },
    stakeAutomatico: {
      type: 'object', required: false,
      label: 'Stake Automático',
      fields: { texto: 'string', evidencia: 'string', selo: 'string' },
      renderType: 'extracted-text',
      section: 6,
    },
    vitoriaAutomatica: {
      type: 'object', required: false,
      label: 'Vitória Automática',
      fields: { texto: 'string', evidencia: 'string', selo: 'string' },
      renderType: 'extracted-text',
      section: 6,
    },
    perguntasValidacao: {
      type: 'array', required: false,
      label: 'Perguntas de Validação',
      renderType: 'string-list',
      section: 8,
    },
    conflitosIdentificados: {
      type: 'array', required: false,
      label: 'Conflitos Identificados',
      renderType: 'string-list',
      section: 8,
    },
    programaDetalhado: {
      type: 'object', required: false,
      label: 'Programa Detalhado (extraído da consultoria)',
      fields: {
        focoPrincipal: 'string',
        distribuicao: 'array',
        cenariosPrioritarios: 'array',
        habilidadesPrioritarias: 'object',
        evitar: 'array',
        momentosEnergia: 'array',
        resumoParaCurriculo: 'string',
      },
      renderType: 'info-grid',
      section: 7,
    },
    dadosExtraidos: {
      type: 'object', required: true,
      label: 'Dados Extraídos da Consultoria',
      renderType: 'extracted-data-grid',
      section: 0,
      fields: {
        idade:      { type: 'extracted', label: 'Idade', inputType: 'number' },
        profissao:  { type: 'extracted', label: 'Profissão', inputType: 'text' },
        cidade:     { type: 'extracted', label: 'Cidade / Estado', inputType: 'text' },
        nivel:      { type: 'extracted', label: 'Nível de Inglês', inputType: 'select-nivel' },
        foco:       { type: 'extracted', label: 'Foco Principal', inputType: 'select-foco' },
        historico:  { type: 'extracted', label: 'Histórico com o Idioma', inputType: 'textarea' },
        eventoAlvo: { type: 'extracted', label: 'Evento-Alvo', inputType: 'evento-compound' },
        hobbies:    { type: 'extracted', label: 'Hobbies e Interesses', inputType: 'textarea' },
      },
    },
  },

  // Metadados do registro
  meta: {
    id:     { type: 'string', required: true, label: 'Slug do aluno' },
    status: { type: 'string', required: true, label: 'Status do perfil', values: ['rascunho', 'em_revisao', 'aprovado', 'material_publicado'] },
    criadoEm: { type: 'string', required: true, label: 'Data de criação' },
  },
};

/**
 * Valida dados contra o schema. Retorna { valid, errors[], warnings[] }.
 */
function validateAgainstSchema(data) {
  const errors = [];
  const warnings = [];

  function addIssue(severity, field, message) {
    (severity === 'error' ? errors : warnings).push({ severity, field, message });
  }

  // Validar dadosFormulario
  const form = data.dadosFormulario || {};
  Object.entries(PROFILE_SCHEMA.dadosFormulario).forEach(([key, spec]) => {
    const val = form[key];
    if (spec.required && (!val || (typeof val === 'string' && !val.trim()))) {
      addIssue('error', `dadosFormulario.${key}`, `${spec.label} é obrigatório.`);
    }
  });

  // Validar perfil
  const perfil = data.perfil || {};
  Object.entries(PROFILE_SCHEMA.perfil).forEach(([key, spec]) => {
    const val = perfil[key];
    const severity = spec.required ? 'error' : 'warning';

    // Verificar presença
    if (val === undefined || val === null) {
      if (spec.required) addIssue('error', `perfil.${key}`, `${spec.label} ausente.`);
      return;
    }

    // Verificar tipo string com minLength
    if (spec.type === 'string') {
      if (typeof val !== 'string' || !val.trim()) {
        addIssue(severity, `perfil.${key}`, `${spec.label} está vazio.`);
      } else if (spec.minLength && val.length < spec.minLength) {
        addIssue('warning', `perfil.${key}`, `${spec.label} muito curto (${val.length} chars, mínimo ${spec.minLength}).`);
      }
    }

    // Verificar tipo array com minItems
    if (spec.type === 'array') {
      if (!Array.isArray(val)) {
        addIssue(severity, `perfil.${key}`, `${spec.label} deveria ser array.`);
      } else if (spec.minItems && val.length < spec.minItems) {
        addIssue(severity, `perfil.${key}`, `${spec.label}: ${val.length} itens (mínimo ${spec.minItems}).`);
      }
    }

    // Verificar tipo object com minKeys
    if (spec.type === 'object') {
      if (typeof val !== 'object' || Array.isArray(val)) {
        addIssue(severity, `perfil.${key}`, `${spec.label} deveria ser objeto.`);
      } else if (spec.minKeys && Object.keys(val).length < spec.minKeys) {
        addIssue(severity, `perfil.${key}`, `${spec.label}: ${Object.keys(val).length} chaves (mínimo ${spec.minKeys}).`);
      }
      // Verificar requiredKeys
      if (spec.requiredKeys) {
        const missing = spec.requiredKeys.filter(k => !val[k]);
        if (missing.length > 0) {
          addIssue(severity, `perfil.${key}`, `${spec.label}: faltam ${missing.length} chaves: ${missing.join(', ')}.`);
        }
      }
    }
  });

  // Validar meta
  if (!data.id) addIssue('error', 'id', 'Slug do aluno ausente.');
  if (!data.status) addIssue('warning', 'status', 'Status do perfil ausente.');

  return {
    valid: errors.length === 0,
    errors,
    warnings,
    issues: [...errors, ...warnings],
    summary: `${errors.length} erros, ${warnings.length} avisos`,
  };
}

/**
 * Gera relatório legível para console/log.
 */
function reportValidation(result, context) {
  const lines = [`\n=== VALIDAÇÃO ${context ? '(' + context + ')' : ''} ===`];
  if (result.valid) {
    lines.push(`✅ Válido (${result.warnings.length} avisos)`);
  } else {
    lines.push(`❌ Inválido: ${result.summary}`);
  }
  result.errors.forEach(e => lines.push(`  ❌ [${e.field}] ${e.message}`));
  result.warnings.forEach(w => lines.push(`  ⚠️ [${w.field}] ${w.message}`));
  return lines.join('\n');
}

if (typeof module !== 'undefined' && module.exports) {
  module.exports = { PROFILE_SCHEMA, validateAgainstSchema, reportValidation };
}
if (typeof window !== 'undefined') {
  window.PROFILE_SCHEMA = PROFILE_SCHEMA;
  window.validateAgainstSchema = validateAgainstSchema;
}
