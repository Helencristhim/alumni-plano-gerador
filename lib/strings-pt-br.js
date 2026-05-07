/**
 * ALUMNI — Strings PT-BR Centralizadas
 * Fonte única de verdade para TODAS as labels, mensagens, microcopy,
 * placeholders, alt texts e titles do sistema.
 *
 * Componentes importam deste arquivo. NUNCA hardcoded.
 * Toda string visível ao usuário vive aqui.
 */

const STRINGS = {
  // ── GLOBAL ──
  global: {
    appName: 'Alumni by Better',
    logoAlt: 'Alumni by Better',
    badges: {
      visaoGestor: 'VISÃO GESTOR',
      visaoProfessor: 'VISÃO PROFESSOR',
      visaoAluno: 'VISÃO ALUNO',
    },
    nav: {
      novoAluno: 'Novo Aluno',
      planosGerados: 'Painel de Alunos',
      perfil360: 'Perfil 360',
      pastaAluno: 'Pasta do Aluno',
    },
    status: {
      rascunho: 'Rascunho',
      emRevisao: 'Em Revisão',
      aprovado: 'Aprovado',
      materialPublicado: 'Material Publicado',
      semPerfil: 'Sem Perfil',
    },
    actions: {
      salvar: 'Salvar Alterações',
      copiar: 'Copiar',
      copiado: 'Copiado!',
      fechar: 'Fechar',
      cancelar: 'Cancelar',
      excluir: 'Excluir',
      editar: 'Editar',
      editado: 'Editado',
      verMais: 'Ver mais',
      tentarNovamente: 'Tentar novamente',
    },
    validation: {
      campoObrigatorio: 'Este campo é obrigatório.',
      emailInvalido: 'Email válido é obrigatório.',
      minimopalavras: (n, atual) => `Mínimo de ${n} palavras (atual: ${atual}).`,
    },
    loading: {
      processando: 'Processando...',
      gerando: 'Gerando...',
      salvando: 'Salvando...',
      salvo: 'Salvo',
    },
  },

  // ── FORMULÁRIO (index.html) ──
  formulario: {
    titulo: 'Plataforma de Jornadas',
    subtitulo: 'Crie uma nova jornada de transformação para um aluno',
    bloco1: {
      tag: 'Bloco 1',
      titulo: 'Identificação Básica',
      nome: 'Nome completo',
      nomePlaceholder: 'Ex: Maria Clara Ferreira',
      email: 'Email do aluno',
      emailPlaceholder: 'Ex: maria@email.com',
      whatsapp: 'WhatsApp do aluno',
      whatsappPlaceholder: 'Ex: (41) 99999-0000',
    },
    bloco2: {
      tag: 'Bloco 2',
      titulo: 'Estrutura do Programa',
      numAulas: 'Número de aulas',
      duracao: 'Duração da aula',
      frequencia: 'Frequência semanal',
      modalidade: 'Modalidade',
      plataforma: 'Plataforma',
      duracaoOpcoes: ['30 min', '45 min', '60 min', '90 min'],
      frequenciaOpcoes: ['1x por semana', '2x por semana', '3x por semana'],
      modalidadeOpcoes: ['Online', 'Presencial', 'Híbrido'],
      plataformaOpcoes: ['Zoom', 'Google Meet', 'Microsoft Teams', 'Outra'],
    },
    bloco3: {
      tag: 'Bloco 3 — Peça Central',
      titulo: 'Consultoria',
      audio: {
        label: 'Áudio da consultoria',
        uploadLabel: 'Clique para enviar o áudio da consultoria',
        formatos: 'mp3, wav, m4a, ogg, webm',
        nota: 'Altamente recomendado — o áudio permite análise prosódica e fica disponível no Perfil 360 para reescuta.',
        storage: 'Armazenamento local no navegador (IndexedDB).',
      },
      transcricao: {
        label: 'Transcrição da consultoria',
        placeholder: 'Cole aqui a transcrição completa da consultoria com o aluno. Pode ser gerada por ferramentas como MacWhisper, Otter.ai, Google Recorder, ou YouTube auto-caption. A transcrição é a fonte principal de análise — quanto mais completa, melhor o Perfil 360.',
        minPalavras: 200,
        contagem: (n) => `${n} palavras`,
        minimoLabel: 'Mínimo: 200 palavras',
        btnTranscrever: 'Transcrever com Web Speech API',
        notaTranscricao: 'Qualidade básica — edição manual será necessária após a transcrição.',
      },
      observacoes: {
        label: 'Observações pós-consultoria do professor',
        placeholder: 'Anote aqui o que a transcrição NÃO captura: tom de voz do aluno, energia, hesitação, humor, postura, momentos em que travou, momentos em que se animou, sotaque/regionalismos, mudanças de humor durante a consultoria. Quanto mais detalhe sobre COMO ele falou (não só o que falou), melhor a análise de personalidade.',
        avisoVazio: 'Sem áudio e sem observações, a análise de personalidade fica significativamente limitada.',
      },
    },
    submit: {
      botao: 'Processar Consultoria',
      loading: 'Processando consultoria... Gerando Perfil 360 com análise completa. Isso leva cerca de 2 minutos — não feche esta página.',
    },
    erros: {
      nomeObrigatorio: 'Nome é obrigatório.',
      emailObrigatorio: 'Email válido é obrigatório.',
      frequenciaObrigatoria: 'Selecione a frequência.',
      modalidadeObrigatoria: 'Selecione a modalidade.',
      transcricaoCurta: (atual) => `A transcrição deve ter no mínimo 200 palavras (atual: ${atual}).`,
      timeout: 'A geração do perfil excedeu o tempo limite (5 minutos). Tente novamente com uma transcrição mais curta.',
      rede: 'Erro de conexão com o servidor. Verifique sua internet e tente novamente.',
      jsonParse: 'Houve um erro técnico na geração do perfil. Por favor, clique em "Processar Consultoria" de novo. Se persistir, tente reduzir o tamanho da transcrição.',
      generico: (msg) => `Erro ao processar: ${msg}. Tente novamente.`,
      perfilIncompleto: 'O perfil gerado está incompleto. Tente processar a consultoria novamente.',
    },
  },

  // ── PERFIL 360 (perfil.html) ──
  perfil: {
    titulo: 'Perfil 360',
    subtituloDefault: 'Análise completa do aluno',
    alunoSemNome: 'Aluno sem nome',
    secoes: {
      statusControles: 'Controles de Status',
      dadosExtraidos: {
        titulo: 'Dados Extraídos da Consultoria',
        subtitulo: 'Campos extraídos automaticamente pela IA. Todos são editáveis — corrija conforme necessário.',
        naoEncontrado: 'Não encontrado na consultoria — preencha manualmente.',
        evidenciaPrefix: 'Evidência:',
      },
      resumoExecutivo: {
        tag: 'Seção 1',
        titulo: 'Resumo Executivo',
      },
      frasesTextuais: {
        titulo: 'Frases Textuais Capturadas',
        subtitulo: 'Frases ipsis litteris do aluno que alimentam a jornada.',
      },
      mapaPersonalidade: {
        tag: 'Seção 2',
        titulo: 'Mapa de Personalidade',
        verEvidencias: 'Ver evidências',
        ocultarEvidencias: 'Ocultar evidências',
        discordo: 'Discordo, ajustar',
        aplicar: 'Aplicar',
        eixosWarning: (n, faltantes) => `Atenção: O mapa de personalidade tem apenas ${n} de 7 eixos obrigatórios. Faltam: ${faltantes}.`,
      },
      forcasMelhorias: {
        tag: 'Seção 3',
        titulo: 'Forças e Pontos de Melhoria',
        forcas: 'Forças',
        melhorias: 'Pontos de Melhoria',
      },
      necessidades: {
        tag: 'Seção 4',
        titulo: 'Necessidades Pedagógicas',
      },
      professor: {
        tag: 'Seção 5',
        titulo: 'Indicação de Professor',
        nomeLabel: 'Nome do Professor Recomendado',
        nomePlaceholder: 'Ex: Prof. Ana Silva',
        descricaoPlaceholder: 'Descreva o perfil ideal do professor para este aluno...',
      },
      justificativa: {
        tag: 'Seção 6',
        titulo: 'Justificativa do Programa',
      },
      consultoria: {
        tag: 'Seção 7',
        titulo: 'Consultoria Completa',
        audioTitle: '7A — Áudio',
        audioIndisponivel: 'Áudio não enviado. Análise baseada em transcrição e observações do professor.',
        transcricaoTitle: '7B — Transcrição Completa',
        transcricaoPlaceholder: 'Transcrição da consultoria...',
        observacoesTitle: '7C — Observações do Professor',
        observacoesPlaceholder: 'Observações do professor sobre o aluno...',
        frasesTitle: '7D — Frases Textuais Capturadas',
      },
      geracao: {
        tag: 'Seção 8',
        titulo: 'Geração de Material',
        btnGerar: 'Gerar Prompt para Claude Code',
        btnDesabilitado: 'Aprove o perfil antes de gerar',
        urlLabel: 'URL do Material Publicado (Vercel)',
        urlPlaceholder: 'Cole a URL do material publicado aqui',
        linkPublicoTitle: 'Link Público do Aluno',
        btnCopiarLink: 'Copiar Link',
      },
    },
    labels: {
      idade: 'IDADE',
      profissao: 'PROFISSÃO',
      cidade: 'CIDADE / ESTADO',
      nivelIngles: 'NÍVEL DE INGLÊS',
      focoPrincipal: 'FOCO PRINCIPAL',
      historico: 'HISTÓRICO COM O IDIOMA',
      eventoAlvo: 'EVENTO-ALVO',
      eventoTipo: 'Tipo',
      eventoData: 'Data',
      eventoLocal: 'Local',
      eventoStake: 'Stake',
      eventoVitoria: 'Vitória',
      hobbies: 'HOBBIES E INTERESSES',
      stakeAutomatico: 'STAKE AUTOMÁTICO',
      vitoriaAutomatica: 'VITÓRIA AUTOMÁTICA',
    },
    nivelOpcoes: [
      { valor: 'A0 (Beginner Absoluto)', label: 'A0 — Beginner Absoluto' },
      { valor: 'A1 (Iniciante)', label: 'A1 — Iniciante' },
      { valor: 'A2 (Pré-Intermediário)', label: 'A2 — Pré-Intermediário' },
      { valor: 'B1 (Intermediário)', label: 'B1 — Intermediário' },
      { valor: 'B2 (Intermediário Superior)', label: 'B2 — Intermediário Superior' },
      { valor: 'C1 (Avançado)', label: 'C1 — Avançado' },
      { valor: 'C1+ (Avançado Plus)', label: 'C1+ — Avançado Plus' },
      { valor: 'C2 (Proficiente)', label: 'C2 — Proficiente' },
    ],
    focoOpcoes: [
      'Travel English', 'Business English', 'Conversação',
      'Proficiência', 'Apresentações', 'Acadêmico', 'Outros',
    ],
    validacao: {
      titulo: 'Validação do Perfil',
      fechar: 'Fechar',
      erros: {
        semNomeIdade: 'Dados Extraídos: nem nome nem idade estão preenchidos.',
        semResumo: 'Resumo executivo está vazio.',
        poucasFrases: (n) => `Apenas ${n} frases textuais (mínimo: 3).`,
        eixosFaltando: (faltantes) => `Mapa de personalidade incompleto. Faltam: ${faltantes}.`,
        semForcas: 'Nenhuma força identificada.',
        semMelhorias: 'Nenhuma melhoria identificada.',
        semJustificativa: 'Justificativa do programa está vazia.',
        semProfessorNome: 'Nome do professor recomendado não preenchido.',
        semProfessorJustificativa: 'Justificativa da indicação de professor não preenchida.',
        camposNaoExtraidos: (campos) => `Campos não extraídos da consultoria: ${campos}. Preencha manualmente ou reprocesse.`,
      },
    },
  },

  // ── DASHBOARD (dashboard.html) ──
  dashboard: {
    titulo: 'Painel de Alunos',
    subtitulo: 'Gerencie jornadas de transformação',
    novoAluno: '+ Novo Aluno',
    buscarPlaceholder: 'Buscar por nome do aluno...',
    ordenar: 'Ordenar:',
    ordenarOpcoes: {
      recente: 'Mais recente',
      antigo: 'Mais antigo',
      nomeAZ: 'Nome A-Z',
      nomeZA: 'Nome Z-A',
      status: 'Status',
    },
    filtros: {
      todos: 'Todos',
      rascunho: 'Rascunho',
      emRevisao: 'Em Revisão',
      aprovado: 'Aprovado',
      publicado: 'Publicado',
      semPerfil: 'Sem Perfil',
    },
    stats: {
      total: 'Total de Alunos',
      emCriacao: 'Em Criação',
      emAndamento: 'Em Andamento',
      concluidos: 'Concluídos',
    },
    card: {
      perfil360: 'Perfil 360',
      material: 'Material',
      copiarLink: 'Copiar Link',
      criarPerfil: 'Criar Perfil',
      naoDesignado: 'Não designado',
      aulasConcluidas: (n, total) => `${n} de ${total} aulas concluídas`,
      diasPara: (n, tipo) => `${n} dias para ${tipo}`,
    },
    vazio: {
      titulo: 'Nenhum aluno encontrado',
      mensagem: 'Clique em "+ Novo Aluno" para começar uma nova jornada.',
      btnCriar: 'Criar Primeiro Aluno',
    },
  },

  // ── PASTA DO ALUNO (aluno.html) ──
  alunoPasta: {
    linkPublico: {
      titulo: 'Link Público do Aluno',
      btnCopiar: 'Copiar Link Público do Aluno',
      linkCopiado: 'Link copiado!',
      materialNaoPublicado: 'Material não publicado ainda',
      oQueAlunoVe: 'O que o aluno vê:',
      oQueAlunoNaoVe: 'O aluno NÃO vê: Plano de aula, Material do professor, Perfil 360, Indicação de professor',
      itensVisiveis: [
        'Exercícios pre-class',
        'Atividades complementares',
        'Survival card progressivo',
        'Anotações pessoais',
      ],
    },
    tabs: {
      perfil: 'Perfil do Aluno',
      preclass: 'Pre-class',
      planoAula: 'Plano de Aula',
      materialProfessor: 'Material do Professor',
      atividades: 'Atividades',
      registro: 'Registro de Aulas',
    },
    registro: {
      titulo: 'Registro de Aulas',
      novaAula: '+ Nova Aula',
      dataAula: 'Data da aula',
      statusAula: 'Status',
      statusOpcoes: {
        naoRealizada: 'Não realizada',
        realizada: 'Realizada',
        cancelada: 'Cancelada',
      },
      campos: {
        coberto: 'O que foi coberto',
        cobertoPlaceholder: 'Conteúdos e tópicos trabalhados nesta aula...',
        avancos: 'O que o aluno avançou bem',
        avancosPlaceholder: 'Pontos de evolução e progresso...',
        travou: 'O que travou',
        travouPlaceholder: 'Dificuldades, bloqueios, pontos que precisam reforço...',
        observacoes: 'Observações sobre o aluno',
        observacoesPlaceholder: 'Humor, energia, eventos pessoais que afetaram a aula...',
        ajustes: 'Ajustes para próxima aula',
        ajustesPlaceholder: 'Adaptações e mudanças para a próxima aula...',
        proximoPasso: 'Próximo passo combinado',
        proximoPassoPlaceholder: 'O que ficou combinado para a próxima aula...',
      },
    },
    perfilNaoGerado: 'Perfil 360 ainda não foi gerado para este aluno.',
    materialNaoGerado: 'Material não gerado ainda.',
    verPerfilCompleto: 'Ver Perfil 360 completo',
    excluir: {
      botao: 'Excluir aluno',
      titulo: 'Excluir Aluno',
      confirmacao: 'Tem certeza que deseja excluir este aluno? Todos os dados (perfil, formulário e registro de aulas) serão removidos permanentemente.',
    },
  },

  // ── NECESSIDADES PEDAGÓGICAS ──
  necessidades: {
    adequacaoNivel: 'Adequação por Nível',
    adequacaoIdade: 'Adequação por Idade',
    estiloAprendizagem: 'Estilo de Aprendizagem',
    toleranciaTraducao: 'Tolerância a Tradução',
    ritmoIdeal: 'Ritmo Ideal',
    tiposExercicio: 'Tipos de Exercício Preferíveis',
    midiasApropriadas: 'Mídias Apropriadas',
    adaptacaoModalidade: 'Adaptação à Modalidade',
  },

  // ── SELOS ──
  selos: {
    verde: { label: 'Fato declarado', cor: 'var(--success)' },
    amarelo: { label: 'Inferência forte', cor: 'var(--warning)' },
    laranja: { label: 'Inferência moderada', cor: '#c2410c' },
    vermelho: { label: 'Hipótese', cor: 'var(--error)' },
  },
};

// Para uso em Node.js (scripts de validação)
if (typeof module !== 'undefined' && module.exports) {
  module.exports = STRINGS;
}

// Para uso em browser (inline em HTML)
if (typeof window !== 'undefined') {
  window.ALUMNI_STRINGS = STRINGS;
}
