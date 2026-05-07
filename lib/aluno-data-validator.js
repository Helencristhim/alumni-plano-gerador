/**
 * ALUMNI — Validador de Dados do Aluno por Fase
 * Verifica campos obrigatórios para cada fase do sistema.
 * Bloqueia avanço se faltar algo crítico.
 */

const FASES = {
  criacao: {
    nome: 'Criação de Aluno',
    obrigatorios: [
      { campo: 'nome', label: 'Nome completo', path: 'nome' },
      { campo: 'email', label: 'Email do aluno', path: 'email' },
      { campo: 'numAulas', label: 'Número de aulas', path: 'numAulas' },
      { campo: 'frequencia', label: 'Frequência semanal', path: 'frequencia' },
      { campo: 'modalidade', label: 'Modalidade', path: 'modalidade' },
      { campo: 'transcricao', label: 'Transcrição da consultoria', path: 'transcricao', minLength: 200 },
    ],
    recomendados: [
      { campo: 'whatsapp', label: 'WhatsApp do aluno', path: 'whatsapp' },
      { campo: 'duracao', label: 'Duração da aula', path: 'duracao' },
      { campo: 'observacoesProfessor', label: 'Observações do professor', path: 'observacoesProfessor' },
    ]
  },

  perfil: {
    nome: 'Geração do Perfil 360',
    obrigatorios: [
      { campo: 'resumoExecutivo', label: 'Resumo executivo', path: 'perfil.resumoExecutivo', minLength: 50 },
      { campo: 'mapaPersonalidade', label: 'Mapa de personalidade (7 eixos)', path: 'perfil.mapaPersonalidade', minKeys: 7 },
      { campo: 'forcas', label: 'Forças (mínimo 3)', path: 'perfil.forcas', minLength: 3 },
      { campo: 'melhorias', label: 'Melhorias (mínimo 3)', path: 'perfil.melhorias', minLength: 3 },
      { campo: 'promessaTransformadora', label: 'Promessa transformadora', path: 'perfil.promessaTransformadora' },
      { campo: 'justificativaPrograma', label: 'Justificativa do programa', path: 'perfil.justificativaPrograma', minLength: 50 },
    ],
    recomendados: [
      { campo: 'frasesTextuais', label: 'Frases textuais (mínimo 3)', path: 'perfil.frasesTextuais', minLength: 3 },
      { campo: 'indicacaoProfessor', label: 'Indicação de professor', path: 'perfil.indicacaoProfessor' },
      { campo: 'dadosExtraidos', label: 'Dados extraídos (8 campos)', path: 'perfil.dadosExtraidos', minKeys: 8 },
    ]
  },

  material: {
    nome: 'Geração de Material',
    obrigatorios: [
      { campo: 'perfilAprovado', label: 'Perfil aprovado', path: 'status', expectedValue: 'aprovado' },
    ],
    recomendados: [
      { campo: 'professorDesignado', label: 'Professor designado', path: 'perfil.indicacaoProfessor.nome' },
    ]
  }
};

function getNestedValue(obj, path) {
  return path.split('.').reduce((o, k) => (o && o[k] !== undefined) ? o[k] : null, obj);
}

function validateAlunoData(data, fase) {
  const config = FASES[fase];
  if (!config) {
    return { valid: false, issues: [{ severity: 'error', campo: 'fase', message: `Fase desconhecida: ${fase}` }] };
  }

  const issues = [];

  // Verificar obrigatórios
  config.obrigatorios.forEach(field => {
    const valor = getNestedValue(data, field.path);

    if (field.expectedValue) {
      if (valor !== field.expectedValue) {
        issues.push({
          severity: 'error',
          campo: field.campo,
          message: `${field.label}: esperado "${field.expectedValue}", encontrado "${valor || 'vazio'}".`
        });
      }
      return;
    }

    if (valor === null || valor === undefined || valor === '') {
      issues.push({
        severity: 'error',
        campo: field.campo,
        message: `${field.label} é obrigatório e está vazio.`
      });
      return;
    }

    if (field.minLength) {
      const length = typeof valor === 'string' ? valor.split(/\s+/).length : (Array.isArray(valor) ? valor.length : 0);
      if (length < field.minLength) {
        issues.push({
          severity: 'error',
          campo: field.campo,
          message: `${field.label}: ${length} encontrado, mínimo ${field.minLength}.`
        });
      }
    }

    if (field.minKeys && typeof valor === 'object' && !Array.isArray(valor)) {
      const keys = Object.keys(valor).length;
      if (keys < field.minKeys) {
        issues.push({
          severity: 'error',
          campo: field.campo,
          message: `${field.label}: ${keys} campos encontrados, mínimo ${field.minKeys}.`
        });
      }
    }
  });

  // Verificar recomendados
  config.recomendados.forEach(field => {
    const valor = getNestedValue(data, field.path);
    if (!valor || (typeof valor === 'string' && !valor.trim())) {
      issues.push({
        severity: 'warning',
        campo: field.campo,
        message: `${field.label} não preenchido (recomendado).`
      });
    }

    if (field.minLength && valor) {
      const length = Array.isArray(valor) ? valor.length : (typeof valor === 'object' ? Object.keys(valor).length : 0);
      if (length < field.minLength) {
        issues.push({
          severity: 'warning',
          campo: field.campo,
          message: `${field.label}: ${length} encontrado, recomendado ${field.minLength}.`
        });
      }
    }
  });

  const errors = issues.filter(i => i.severity === 'error');
  const warnings = issues.filter(i => i.severity === 'warning');

  return {
    valid: errors.length === 0,
    fase: config.nome,
    errors,
    warnings,
    issues,
    summary: `Fase "${config.nome}": ${errors.length} erros, ${warnings.length} avisos`
  };
}

if (typeof module !== 'undefined' && module.exports) {
  module.exports = { validateAlunoData, FASES };
}
