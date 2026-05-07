const Anthropic = require('@anthropic-ai/sdk');
const fs = require('fs');
const path = require('path');
const { createClient } = require('@supabase/supabase-js');
const { robustJSONParse, logJSONError } = require('../lib/sanitize-json');
const { validateAgainstSchema, reportValidation } = require('../lib/profile-schema');

const supabase = process.env.SUPABASE_URL && process.env.SUPABASE_SERVICE_KEY
  ? createClient(process.env.SUPABASE_URL, process.env.SUPABASE_SERVICE_KEY)
  : null;

const client = new Anthropic({ apiKey: process.env.ANTHROPIC_API_KEY });

module.exports = async (req, res) => {
  if (req.method !== 'POST') return res.status(405).json({ error: 'Method not allowed' });

  try {
    const {
      // Bloco 1 — Perfil Pessoal
      nome, idade, profissao, cidade, modalidadeTrabalho, email, whatsapp,
      // Bloco 2 — Programa Desejado
      foco, numAulas, duracao, frequencia, modalidadeAula, plataforma, horarios,
      // Bloco 3 — Urgência
      existeEvento, tipoEvento, dataEvento, localEvento,
      // Bloco 4 — Motivação Emocional
      stake, vitoria,
      // Bloco 5 — Histórico com Inglês
      historicoIngles, nivel, tempoForaAula,
      // Bloco 6 — Personalidade e Estilo
      estiloAprendizagem, estruturaPreferida, lidaComErros, energiaPreferida,
      // Bloco 7 — Interesses Pessoais
      seriesFilmes, musicasPodcasts, hobbies,
      // Bloco 8 — Consultoria
      temAudio, audioUrl,
      resumoZoom,
      transcricao,
      observacoesProfessor
    } = req.body;

    // Gerar slug
    const slug = nome.toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, '').replace(/[^a-z0-9]+/g, '-').replace(/-+/g, '-').replace(/^-|-$/g, '');

    const audioBlock = temAudio ? `
ÁUDIO DA CONSULTORIA: Disponível para reescuta (armazenado). URL: ${audioUrl || 'IndexedDB local'}
Considere que há informação prosódica complementar disponível.
` : `
ÁUDIO DA CONSULTORIA: Não disponível. Análise baseada APENAS em transcrição + observações do professor.
Marque inferências de personalidade com confiança REDUZIDA (máx 70% sem áudio).
`;

    const prompt = `Você é um editor pedagógico sênior com 40 anos de experiência na tradição Cambridge Assessment English (Jeremy Harmer, Scott Thornbury, Penny Ur). Sua especialidade é analisar consultorias de alunos de inglês e gerar perfis 360° que transformam dados brutos em jornadas de aprendizado personalizadas.

Analise os dados abaixo e gere um Perfil 360 estruturado deste aluno.

══════════════════════════════════════
DADOS COMPLETOS DO ALUNO (8 blocos informados pelo gestor)
══════════════════════════════════════

BLOCO 1 — PERFIL PESSOAL:
- Nome: ${nome}
- Idade: ${idade || 'Não informada'}
- Profissão (gestor preencheu): ${profissao || 'Não informada'} — COMPLEMENTAR com detalhes da transcrição: empresa, cargo exato, área de atuação, contexto de uso do inglês no trabalho
- Cidade: ${cidade || 'Não informada'}
- Modalidade trabalho: ${modalidadeTrabalho || 'Não informada'}
- Email: ${email}
- WhatsApp: ${whatsapp || 'Não informado'}

BLOCO 2 — PROGRAMA DESEJADO:
- Foco principal: ${foco === '100% Personalizado' ? 'EXTRAIR DA TRANSCRIÇÃO — analise a consultoria e identifique o foco ideal baseado no que foi discutido e acordado. Detalhe: proporções entre habilidades, contextos profissionais específicos, skills prioritários.' : (foco || 'Não informado')}
- N° de aulas: ${numAulas}
- Duração: ${duracao}
- Frequência: ${frequencia}
- Modalidade da aula: ${modalidadeAula || 'Não informada'}${plataforma ? ` (${plataforma})` : ''}
- Horários disponíveis: ${horarios || 'Não informados'}

BLOCO 3 — URGÊNCIA:
${existeEvento ? `- Evento marcado: SIM
- Tipo: ${tipoEvento}
- Data: ${dataEvento}
- Local: ${localEvento}` : '- Nenhum evento marcado'}

BLOCO 4 — MOTIVAÇÃO EMOCIONAL:
- Stake (o que dá errado se não estiver pronto): ${stake || 'Não declarado'}
- Vitória (como vai se sentir quando conseguir): ${vitoria || 'Não declarada'}

BLOCO 5 — HISTÓRICO COM INGLÊS:
- Histórico declarado: ${historicoIngles || 'Não informado'}
- Nível declarado pelo gestor: ${nivel || 'Não informado'}
- Tempo disponível fora das aulas: ${tempoForaAula || 'Não informado'}

BLOCO 6 — PERSONALIDADE E ESTILO (declarado pelo gestor):
- Estilo de aprendizagem: ${estiloAprendizagem || 'Não informado'}
- Preferência de estrutura: ${estruturaPreferida || 'Não informada'}
- Como lida com erros: ${lidaComErros || 'Não informado'}
- Energia preferida: ${energiaPreferida || 'Não informada'}

BLOCO 7 — INTERESSES PESSOAIS:
- Séries/filmes: ${seriesFilmes || 'Não informado'}
- Músicas/podcasts: ${musicasPodcasts || 'Não informado'}
- Hobbies: ${hobbies || 'Não informado'}

══════════════════════════════════════
INVESTIGAÇÃO DA IA (conforme /docs/INVESTIGACAO-CONSULTORIA.md)
══════════════════════════════════════

Sua tarefa como editor pedagógico sênior:

A) VALIDAR dados declarados pelo gestor (Blocos 1-7):
- Compare cada dado declarado com o que a transcrição revela
- Se confirma: selo 🟢
- Se ajusta: selo 🟡 com justificativa
- Se contradiz: selo 🔴 com evidência da contradição

B) CAPTAR o que só a transcrição revela:
- 3-5 frases textuais ipsis litteris do aluno
- Vocabulário em inglês que o aluno usa naturalmente (revela nível real)
- Frases em inglês que o aluno errou (revela gaps específicos)
- Padrões de fala em PT (palavras de muleta, regionalismos, tom)
- Tópicos mencionados com energia vs com obrigação

C) INFERIR baseado nas observações do professor:
- Tolerância a erro real (como reagiu quando travou?)
- Estilo de aprendizagem real (quando se animou?)
- Energia preferida (ritmo natural da conversa)
- Postura emocional sobre inglês (confiança vs ansiedade)

D) GERAR análise pedagógica completa:
- Resumo executivo, mapa de personalidade, forças/melhorias, necessidades pedagógicas, indicação de professor, justificativa, promessa transformadora

CAMPOS DE dadosExtraidos — VALIDAÇÃO DOS DADOS DECLARADOS:
Para cada campo, COMPARE o que o gestor declarou (Blocos 1-7) com o que a transcrição revela. Se houver discrepância, sinalize com selo adequado.

- idade: Compare com o declarado (${idade || 'não informada'}). Se a transcrição confirma, 🟢. Se ajusta, 🟡.
- profissao: O gestor declarou "${profissao || 'não informada'}". COMPLEMENTE com detalhes da transcrição: empresa, cargo exato, área de atuação, contexto de uso do inglês no trabalho. O valor final deve ser a versão mais completa possível. Ex: gestor escreveu "Head TI - Centauro" → IA complementa "Head de TI na Centauro — lidera equipe de desenvolvimento, participa de reuniões com fornecedores internacionais, apresentações em inglês para board".
- cidade: Compare com o declarado (${cidade || 'não informada'}). Se confirma, 🟢. Se a transcrição revela mais detalhes, complemente.
- nivel: Compare com o declarado (${nivel || 'não informado'}). Infira nível REAL baseado na qualidade da fala em inglês. Se difere do declarado, 🟡 com justificativa.
- foco: ${foco === '100% Personalizado' ? 'O gestor selecionou "100% Personalizado" — EXTRAIA o foco ideal INTEIRAMENTE da transcrição. Analise o que foi discutido e acordado: proporções entre habilidades (fala/escuta/leitura/escrita), contextos profissionais, skills prioritários. Seja o mais detalhado possível.' : 'Compare com o declarado (' + (foco || 'não informado') + '). Se confirma, 🟢.'}
- historico: Compare com o declarado (${historicoIngles || 'não informado'}). Enriqueça com detalhes da transcrição.
- eventoAlvo: Compare com Bloco 3. Se confirma, 🟢. Se tem mais detalhes, 🟡.
- hobbies: Compare com Bloco 7 (${seriesFilmes || ''}, ${musicasPodcasts || ''}, ${hobbies || ''}). Enriqueça.

══════════════════════════════════════
FONTES DE ANÁLISE (pesos obrigatórios)
══════════════════════════════════════

FONTE 1 — TRANSCRIÇÃO DA CONSULTORIA (peso 50%):
${transcricao}

${audioBlock}

FONTE 2 — RESUMO DO ZOOM AI COMPANION (peso 15%):
${resumoZoom ? resumoZoom : 'Não fornecido. Usar apenas transcrição e observações.'}
${resumoZoom ? 'INSTRUÇÃO: Este resumo foi gerado automaticamente pelo Zoom AI. Contém tópicos principais, decisões tomadas e próximos passos acordados. Use como fonte complementar para validar e enriquecer o que foi extraído da transcrição. Dê atenção especial a: decisões sobre o programa, expectativas do aluno, compromissos assumidos pela escola.' : ''}

FONTE 3 — OBSERVAÇÕES PÓS-CONSULTORIA DO PROFESSOR (peso 20%):
${typeof observacoesProfessor === 'object' ?
  `- Tom de voz geral: ${observacoesProfessor.tomVoz || 'Não observado'}
- Energia durante consultoria: ${observacoesProfessor.energiaConsultoria || 'Não observada'}
- Momentos de animação: ${observacoesProfessor.momentosAnimacao || 'Não observados'}
- Momentos de hesitação: ${observacoesProfessor.momentosHesitacao || 'Não observados'}
- Observações livres: ${observacoesProfessor.observacoesLivres || 'Nenhuma'}` :
  (observacoesProfessor || 'Nenhuma observação registrada. Inferências de personalidade terão confiança reduzida.')}

══════════════════════════════════════
RULEBOOK DE ADEQUAÇÃO POR NÍVEL
══════════════════════════════════════

A1 (Iniciante): SEMPRE tradução PT-BR. 4-5 palavras/aula. Frases 2-4 palavras. Drilling intenso. CCQs em português. Practice: matching imagem+palavra. Production muito guiada (máx 5 min). Mídias: desenhos, vídeos curtos legendados PT.

A2 (Pré-Intermediário): Tradução PT-BR obrigatória. 5-7 palavras/aula. Frases simples 5-8 palavras. "Blocos de linguagem". CCQs em inglês simples. Practice: matching, fill-in-blanks, quiz. Respostas COMPLETAS. Production: role-play sem script (10-15 min). Mídias: filmes simples, podcasts learners.

B1 (Intermediário): Tradução só termos técnicos/idiomáticos. 6-8 palavras. Textos 8-12 linhas. Expressões idiomáticas. CCQs com justificativa. Practice: reading, ordering, sorting, true/false. Production: role-play com imprevistos (15-20 min). Mídias: legendas EN, TED Talks.

B2 (Intermediário Superior): Sem tradução (exceto técnicos). Collocations, phrasal verbs. Textos autênticos. CCQs complexas. Practice: paráfrase, registro. Production: debates, apresentações (20 min). Mídias: sem legenda, podcasts nativos.

C1 (Avançado): Zero tradução. Material 100% autêntico. Análise crítica. Production: debates complexos, escrita argumentativa (20+ min). Mídias: NPR, The Economist, stand-up.

C1+ (Avançado Plus): Refinamento profissional. Domínio de registros (formal, jurídico, jornalístico, literário). Retórica persuasiva avançada. Capacidade de produzir conteúdo publicável. Mediação cultural. Production: 37 min. Mídias: igual C1 com foco em precisão extrema.

C2 (Proficiente): Polimento — sotaque, estilo, humor, escrita acadêmica. Tradução literária, análise de discurso.

══════════════════════════════════════
RULEBOOK DE ADEQUAÇÃO POR IDADE
══════════════════════════════════════

Crianças (5-12): Jogos, desenhos, vocabulário visual. Mídias: desenhos educativos.
Adolescentes (13-17): Redes sociais, escola, tecnologia. Mídias: séries teen, YouTubers.
Adultos jovens (18-30): Cultura pop, carreira, networking. Mídias: séries modernas, TikTok English.
Adultos (31-50): Temas profissionais, viagens de negócios. Mídias: filmes clássicos/modernos, podcasts negócios.
Adultos 50+: Temas acessíveis, viagens, cultura. Mídias: filmes clássicos, documentários, podcasts calmos.

══════════════════════════════════════
INSTRUÇÕES DE ANÁLISE
══════════════════════════════════════

1. SISTEMA DE SELOS (obrigatório em TODA inferência):
   🟢 Fato declarado — aluno disse explicitamente
   🟡 Inferência forte — 3+ sinais convergentes
   🟠 Inferência moderada — 1-2 sinais
   🔴 Hipótese — chute educado, precisa validação humana

2. REGRA ABSOLUTA: NUNCA apresente hipótese (🔴) como fato (🟢). Sem evidência = sem inferência.

3. CADA INFERÊNCIA deve ter:
   - Valor/classificação
   - % de confiança (0-100)
   - Selo (🟢🟡🟠🔴)
   - 1-3 evidências citadas COM trecho da transcrição entre aspas ou referência à observação do professor

4. FRASES TEXTUAIS: Capture 3-5 frases ipsis litteris do aluno que:
   - Resumem o objetivo dele
   - Revelam a dor real
   - Mostram a vitória esperada
   - Revelam personalidade
   Para cada frase, indique onde será usada (promessa do programa, cabeçalho do material, definição da jornada, citação motivacional).

5. PROMESSA TRANSFORMADORA: A partir do stake + vitória + frases capturadas, gere a promessa do programa usando as PALAVRAS DO ALUNO (não academiquês).

6. SINAIS DE PERSONALIDADE DO TEXTO: Analise iniciativa de fala, articulação de opiniões, mudanças de opinião, linguagem direta vs circunlóquios, repetição de temas (3+ menções = prioridade alta), superlativos, humor verbal, estrutura sintática.

7. MODALIDADE (${modalidadeAula || 'Não informada'}): Adapte as necessidades pedagógicas. Online: exercícios adaptados para tela compartilhada, chat, breakout rooms. Presencial: objetos físicos, movimento, flashcards na mão.

8. ACENTUAÇÃO: Todo texto em português DEVE ter acentuação perfeita (é, ã, ç, ê, ó, ú, à).

══════════════════════════════════════
FORMATO DE SAÍDA (JSON puro, sem markdown)
══════════════════════════════════════

Retorne APENAS JSON puro com esta estrutura exata:

{
  "dadosExtraidos": {
    "idade": { "valor": "47", "selo": "🟢", "evidencia": "Aluno mencionou 'tenho 47 anos'", "encontrado": true },
    "profissao": { "valor": "Agricultor e Advogado", "selo": "🟢", "evidencia": "...", "encontrado": true },
    "cidade": { "valor": "Sorriso, MT", "selo": "🟡", "evidencia": "...", "encontrado": true },
    "nivel": { "valor": "A2 (Pré-Intermediário)", "selo": "🟡", "evidencia": "Baseado na qualidade da fala e vocabulário ativo", "encontrado": true },
    "foco": { "valor": "Travel English", "selo": "🟢", "evidencia": "...", "encontrado": true },
    "historico": { "valor": "Descrição do histórico com o idioma", "selo": "🟢", "evidencia": "...", "encontrado": true },
    "eventoAlvo": { "valor": { "tipo": "Viagem", "data": "2026-06-01", "local": "Miami", "stake": "O que dá errado", "vitoria": "Como vai se sentir" }, "selo": "🟡", "evidencia": "...", "encontrado": true },
    "hobbies": { "valor": ["lista de hobbies"], "selo": "🟠", "evidencia": "...", "encontrado": false }
  },

  "resumoExecutivo": "Parágrafo de 4-6 linhas descrevendo o aluno como pessoa real, em linguagem humana e empática. Incluir profissão, contexto, motivação, personalidade observada, e a dor/ansiedade principal.",

  "frasesTextuais": [
    {
      "frase": "Frase exata dita pelo aluno na transcrição",
      "uso": "promessa_programa | cabecalho_material | definicao_jornada | citacao_motivacional",
      "contexto": "Por que essa frase é significativa"
    }
  ],

  "promessaTransformadora": "A promessa do programa usando as palavras do aluno. Ex: 'De travado na imigração a viajante independente em 5 aulas.'",

  "personagemJornada": {
    "de": "Estado atual do aluno (com palavras dele)",
    "para": "Estado desejado (com palavras dele)",
    "emQuantasAulas": ${numAulas}
  },

  "mapaPersonalidade": {
    "introversaoExtroversao": {
      "valor": 1-10,
      "inferencia": "Descrição curta (ex: Extrovertido moderado)",
      "confianca": 0-100,
      "selo": "🟢|🟡|🟠|🔴",
      "evidencias": ["Evidência 1 com citação", "Evidência 2", "Evidência 3"]
    },
    "seriedadeLudicidade": { "valor": 1-10, "inferencia": "...", "confianca": 0-100, "selo": "...", "evidencias": [] },
    "reflexivoImpulsivo": { "valor": 1-10, "inferencia": "...", "confianca": 0-100, "selo": "...", "evidencias": [] },
    "confianteInseguro": { "valor": 1-10, "inferencia": "...", "confianca": 0-100, "selo": "...", "evidencias": [] },
    "toleranciaErro": {
      "valor": "alta|media|baixa",
      "inferencia": "...",
      "confianca": 0-100,
      "selo": "...",
      "evidencias": []
    },
    "estiloAprendizagem": {
      "valor": "visual|auditivo|cinestesico|leitura_escrita",
      "inferencia": "...",
      "confianca": 0-100,
      "selo": "...",
      "evidencias": []
    },
    "energiaPreferida": {
      "valor": "calma_estruturada|dinamica_variada|mista",
      "inferencia": "...",
      "confianca": 0-100,
      "selo": "...",
      "evidencias": []
    }
  },

  "forcas": [
    { "item": "Descrição da força", "selo": "🟢|🟡|🟠", "evidencia": "Citação ou referência" }
  ],

  "melhorias": [
    { "item": "Descrição do ponto de melhoria", "selo": "🟢|🟡|🟠", "evidencia": "Citação ou referência" }
  ],

  "necessidadesPedagogicas": {
    "adaptacaoNivel": "Resumo do que o rulebook define para o nível extraído em dadosExtraidos.nivel",
    "adaptacaoIdade": "Resumo do que o rulebook define para a idade extraída em dadosExtraidos.idade",
    "estiloAprendizagem": "Como adaptar o material ao estilo inferido",
    "toleranciaTraducao": "alta|media|baixa — baseada no nível",
    "ritmoIdeal": "Descrição do ritmo ideal de aula para este aluno",
    "tiposExercicio": ["Lista dos tipos de exercício mais adequados"],
    "midiasApropriadas": ["Lista de 5-8 sugestões de filmes/séries/podcasts adequados à idade e nível"],
    "adaptacaoModalidade": "Como adaptar para ${modalidadeAula || 'Não informada'}: exercícios, dinâmicas, recursos"
  },

  "indicacaoProfessor": {
    "perfilIdeal": "Descrição DETALHADA do professor ideal para este aluno em dois aspectos: (1) PERFIL ACADÊMICO: formação, certificações (CELTA/DELTA/TESOL), experiência com o nível e foco do aluno, especialidade (business/travel/academic/legal), sotaque preferível (UK/US/neutro); (2) PERFIL DE PERSONALIDADE: energia (calmo vs dinâmico), estilo de feedback (direto vs gentil), tolerância ao silêncio, senso de humor, capacidade de adaptar ritmo. Baseie-se no mapa de personalidade e nas frases textuais do aluno.",
    "justificativa": ["Razão 1 baseada no perfil do aluno", "Razão 2 baseada no estilo de aprendizagem", "Razão 3 baseada na personalidade"]
  },

  "justificativaPrograma": "Parágrafo de 4-8 linhas explicando por que este programa específico (${numAulas} aulas com o foco extraído) faz sentido para esta pessoa específica, considerando nível, idade, objetivo, evento-alvo, personalidade e contexto de vida.",

  "perguntasValidacao": [
    "Pergunta sugerida para validar hipótese 🔴 antes da primeira aula"
  ],

  "conflitosIdentificados": [
    "Descrição de qualquer contradição entre inferências que o gestor deve revisar"
  ],

  "stakeAutomatico": {
    "texto": "O que dá errado se o aluno não estiver pronto — extraído da transcrição e observações",
    "evidencia": "Trecho da transcrição ou observação que sustenta esta inferência",
    "selo": "🟢|🟡|🟠|🔴"
  },

  "vitoriaAutomatica": {
    "texto": "Como o aluno vai se sentir quando conseguir — extraído da transcrição e observações",
    "evidencia": "Trecho da transcrição ou observação que sustenta esta inferência",
    "selo": "🟢|🟡|🟠|🔴"
  }
}

REGRAS FINAIS CRÍTICAS:
- Retorne APENAS JSON puro. Sem backticks, sem markdown, sem texto antes ou depois do JSON.
- O JSON DEVE ser válido. Verifique: todas as strings usam aspas duplas, aspas dentro de strings são escapadas com \\", quebras de linha dentro de strings usam \\n, todas as vírgulas entre propriedades estão presentes, todos os colchetes e chaves estão fechados.
- TODOS os textos em português com acentuação perfeita.
- Pelo menos 3 frases textuais capturadas.
- Todos os 7 eixos do mapa de personalidade preenchidos com pelo menos 1 evidência citada.
- Se não houver evidência suficiente para um eixo, use selo 🔴 e confiança < 50%.
- A promessa transformadora deve usar palavras do aluno, não academiquês.
- TODOS os 8 campos de dadosExtraidos devem estar presentes. Se não encontrado, use encontrado: false, selo "🔴", valor: null.
- ATENÇÃO COM ASPAS: quando citar falas do aluno dentro de strings JSON, use aspas simples (') em vez de aspas duplas para evitar quebrar o JSON. Exemplo correto: "evidencia": "Aluno disse 'eu travo quando o cara fala rápido'"
- Seja CONCISO nas evidências — máximo 1-2 frases por evidência. Não copie parágrafos inteiros da transcrição.

REGRAS COMPLEMENTARES 119-137 (aplicar ao gerar o perfil):
- REGRA 119: mínimo 10 palavras circulando por aula no programa recomendado.
- REGRA 120: composição varia por nível (A0: 6-8 novas + cognatos, B2: 10-12 novas + revisão).
- REGRA 122: nominalização contextual — usar PRIMEIRO NOME em contextos informais, SOBRENOME em formais. NUNCA nomes genéricos.
- REGRA 123: mescla geral/foco em 4 dimensões (vocabulário, contexto, production, atividades complementares). Proporção: A0/A1=70/30, A2=60/40, B1=50/50, B2=40/60, C1+=30/70.
- REGRA 127: NÃO inventar mídia nas recomendações. Toda mídia deve ser REAL e VERIFICÁVEL.
- REGRA 131: tradução acessível por nível — A0/A1 via tooltip, A2 seletiva, B1/B2/C1/C1+/C2 sem tradução.
- REGRA 135: reconhecer cargas emocionais do nível do aluno e adaptar tom do perfil.
- REGRA 136: adequar por faixa etária (5-12: lúdico 30min, 13-17: peer-like, 31-50: ROI profissional, 50+: validar experiência).
- REGRA 137: reconhecer cenário de consultoria (A: aluno fala EN, B: aluno fala só PT, C: sem consultoria).

REGRAS ABSOLUTAS 138-142:
- REGRA 138: 90 min universal para adultos em Material Professor e Plano de Aula. Exceção: crianças 5-12 = 30 min.
- REGRA 139: Vocabulary + Expressions obrigatórios em TODOS os níveis no Pre-class. A0 começa com situações reais (NÃO alfabeto/cores).
- REGRA 140: NUNCA repetir vocabulário/expressions como novo conteúdo em aulas posteriores. Revisão e callback permitidos.
- REGRA 141: áudios SEMPRE ElevenLabs. Zero tolerância para Web Speech em material publicado.
- REGRA 142: invocar UX/UI ao criar qualquer nova página HTML. Consistência Alumni, WCAG AAA, mobile-first.
- REGRA 143: INGLÊS AMERICANO como padrão absoluto. Spelling, pronúncia, vocabulário e expressões sempre em American English. Exceção APENAS quando perfil indicar necessidade de British English — nesse caso, sinalizar explicitamente com [British English].
- REGRA META: coerência absoluta entre 5 abas — vocabulário idêntico, aplicações diferentes, critério de sucesso alcançável.`;

    const message = await client.messages.create({
      model: 'claude-sonnet-4-6',
      max_tokens: 16000,
      messages: [{ role: 'user', content: prompt }]
    });

    let text = message.content[0].text;
    let perfil;
    let parseResult = robustJSONParse(text);

    // If parse failed, retry up to 2 more times with feedback
    let retries = 0;
    while (!parseResult.success && retries < 2) {
      retries++;
      logJSONError(slug || 'perfil-360', parseResult.error, retries, text);
      console.log(`Retry ${retries}/2: solicitando JSON válido à API...`);

      const retryMessage = await client.messages.create({
        model: 'claude-sonnet-4-6',
        max_tokens: 16000,
        messages: [
          { role: 'user', content: prompt },
          { role: 'assistant', content: text },
          { role: 'user', content: `Sua resposta anterior teve erro de JSON na posição indicada: "${parseResult.error}". Refaça o JSON garantindo que está perfeitamente válido. Use aspas simples dentro de strings para evitar conflito. Verifique todas as vírgulas e chaves de fechamento. Retorne APENAS o JSON corrigido.` }
        ]
      });

      text = retryMessage.content[0].text;
      parseResult = robustJSONParse(text);
    }

    if (!parseResult.success) {
      logJSONError(slug || 'perfil-360', parseResult.error, 'final', text);
      return res.status(500).json({
        error: 'JSON_PARSE_ERROR',
        message: 'Erro técnico ao gerar perfil. Por favor, tente novamente.',
        retries: retries,
        lastError: parseResult.error,
        responseLength: text ? text.length : 0
      });
    }

    console.log(`Parse OK (estratégia: ${parseResult.strategy}, retries: ${retries})`);
    perfil = parseResult.data;

    // Build result object FIRST (schema validation needs dadosFormulario)
    const result = {
      id: slug,
      perfil,
      dadosExtraidos: perfil.dadosExtraidos || null,
      dadosFormulario: {
        // Bloco 1
        nome, idade, profissao, cidade, modalidadeTrabalho, email, whatsapp,
        // Bloco 2
        foco, numAulas, duracao, frequencia, modalidadeAula, plataforma, horarios,
        // Bloco 3
        existeEvento, tipoEvento, dataEvento, localEvento,
        // Bloco 4
        stake, vitoria,
        // Bloco 5
        historicoIngles, nivel, tempoForaAula,
        // Bloco 6
        estiloAprendizagem, estruturaPreferida, lidaComErros, energiaPreferida,
        // Bloco 7
        seriesFilmes, musicasPodcasts, hobbies,
        // Bloco 8
        temAudio, audioUrl
      },
      transcricao,
      observacoesProfessor,
      criadoEm: new Date().toISOString(),
      status: 'rascunho'
    };

    // ── SCHEMA VALIDATION (bloqueante) ──
    let schemaResult = validateAgainstSchema(result);
    console.log(reportValidation(schemaResult, slug));

    // Retry if errors found (up to 2 retries)
    let schemaRetries = 0;
    while (!schemaResult.valid && schemaRetries < 2) {
      schemaRetries++;
      const errorList = schemaResult.errors.map(e => `${e.field}: ${e.message}`).join('; ');
      console.log(`Schema incompleto (retry ${schemaRetries}/2): ${errorList}`);

      const retryMsg = await client.messages.create({
        model: 'claude-sonnet-4-6',
        max_tokens: 16000,
        messages: [
          { role: 'user', content: prompt },
          { role: 'assistant', content: text },
          { role: 'user', content: `O JSON gerado está INCOMPLETO segundo o schema obrigatório. Campos com erro:\n${errorList}\n\nGere o JSON completo novamente com TODOS os campos listados no schema. Retorne APENAS JSON válido.` }
        ]
      });
      text = retryMsg.content[0].text;
      parseResult = robustJSONParse(text);
      if (parseResult.success) {
        perfil = parseResult.data;
        result.perfil = perfil;
        result.dadosExtraidos = perfil.dadosExtraidos || null;
        schemaResult = validateAgainstSchema(result);
        console.log(reportValidation(schemaResult, `${slug} retry ${schemaRetries}`));
      } else {
        break;
      }
    }

    // If still invalid after retries, return 500
    if (!schemaResult.valid) {
      const errorList = schemaResult.errors.map(e => `${e.field}: ${e.message}`).join('; ');
      console.error(`Schema FALHOU após ${schemaRetries} retries: ${errorList}`);
      return res.status(500).json({
        error: 'SCHEMA_INCOMPLETE',
        message: 'O perfil gerado está incompleto. Tente processar a consultoria novamente.',
        errors: schemaResult.errors,
        retries: schemaRetries,
      });
    }

    // Save to Supabase (primary shared storage)
    if (supabase) {
      try {
        const d = result.dadosFormulario || {};
        await supabase.from('perfis').upsert({
          id: slug, data: result, status: result.status || 'rascunho',
          nome: d.nome || nome || slug,
          nivel: result.dadosExtraidos?.nivel?.valor || d.nivel || nivel || '',
          num_aulas: parseInt(numAulas) || 0, foco: d.foco || foco || ''
        });
        console.log(`Perfil salvo no Supabase: ${slug}`);
      } catch(e) { console.error('Supabase save failed:', e.message); }
    }

    res.setHeader('Content-Type', 'application/json; charset=utf-8');
    res.status(200).json(result);
  } catch (error) {
    console.error('Erro ao gerar Perfil 360:', error);
    res.status(500).json({ error: error.message || 'Erro interno do servidor' });
  }
};
