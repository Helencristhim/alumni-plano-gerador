/**
 * @deprecated Esta API NÃO é chamada por nenhum frontend.
 * O fluxo atual usa: index.html → perfil-360.js → perfil.html → gerar-temas.js
 * Mantida apenas para referência histórica. NÃO deletar sem confirmar com gestão.
 * Data: 2026-05-25
 */
const Anthropic = require('@anthropic-ai/sdk');
const { robustJSONParse, logJSONError } = require('../lib/sanitize-json');

const client = new Anthropic({ apiKey: process.env.ANTHROPIC_API_KEY });

module.exports = async (req, res) => {
  if (req.method !== 'POST') return res.status(405).json({ error: 'Method not allowed' });

  try {
    const { nome, idade, localizacao, profissao, frequencia, nivel, historico, objetivo, numAulas, observacoes, transcricao, modalidade } = req.body;

    const prompt = `Você é um coordenador pedagógico de uma escola de inglês premium. Com base nas informações abaixo, gere um plano pedagógico completo e personalizado.

DADOS DO ALUNO:
- Nome: ${nome}
- Idade: ${idade} anos
- Localização: ${localizacao}
- Profissão: ${profissao}
- Frequência: ${frequencia}
- Nível atual: ${nivel}
- Histórico com o idioma: ${historico}
- Objetivo/Tipo de programa: ${objetivo}
- Número de aulas do bloco: ${numAulas}
- Observações extras: ${observacoes || 'Nenhuma'}

MODALIDADE DA AULA: ${modalidade || 'Online'}. Adaptar atividades: Online=tela compartilhada, chat, breakout rooms; Presencial=flashcards físicos, movimento, objetos reais; Híbrido=indicar qual recurso para cada tipo de aula.

INGLÊS AMERICANO (Regra 143): TODO material em American English por padrão (spelling, vocabulário, expressões, pronúncia). Exceção apenas se perfil indicar British English — sinalizar com [British English].

ADEQUAÇÃO POR NÍVEL (${nivel}):
- A0: Tradução PT-BR em tudo. 4-5 palavras novas/aula (10 circulando). Frases 2-4 palavras. Grammar Tip bilingue. CCQs em português. Practice: matching. Production muito guiada (5 min).
- A1: Tradução PT-BR em tudo. 5-7 palavras novas/aula (10-12 circulando). Frases 4-6 palavras. Grammar Tip bilingue. CCQs em português. Practice: matching. Production guiada (5-10 min).
- A2: ZERO português. 6-8 palavras novas/aula (10-12 circulando). Frases 5-8 palavras. Grammar Tip em inglês. CCQs em inglês simples. Practice: matching, fill-in-blanks, quiz. Production role-play sem script (10-15 min).
- B1: ZERO português. 7-9 palavras novas/aula (10-12 circulando). Textos mais longos. CCQs com justificativa em inglês. Practice variada. Production com imprevistos (15-20 min).
- B2: ZERO português. 10-12 palavras novas/aula (10-13 circulando). Collocations, phrasal verbs. Textos autênticos. Production com debates e apresentações (20 min).
- C1: ZERO português. 10-12 palavras novas/aula (10-13 circulando). Material 100% autêntico. Análise crítica. Production 20+ min.
- C1+: ZERO português. 10-12 palavras novas/aula. Refinamento profissional. Production 37 min. Precisão extrema.
- C2: ZERO português. Polimento: sotaque, estilo, humor, escrita acadêmica.

ADEQUAÇÃO POR IDADE (${idade} anos):
- Crianças (5-12): Jogos, desenhos, vocabulário visual, atividades lúdicas.
- Adolescentes (13-17): Redes sociais, escola, jogos, tecnologia. Mídias: séries teen, YouTubers, músicas pop.
- Adultos jovens (18-30): Cultura pop, carreira, networking. Mídias: séries modernas, podcasts cultura, TikTok English.
- Adultos (31-50): Temas profissionais, viagens de negócios. Mídias: filmes clássicos/modernos, podcasts negócios.
- Adultos 50+: Temas acessíveis, viagens, cultura. Mídias: filmes clássicos, documentários, podcasts calmos. Evitar cultura pop recente.

${transcricao ? `TRANSCRIÇÃO DA CONSULTORIA:\n${transcricao}\n` : ''}

Gere um JSON com EXATAMENTE esta estrutura (sem markdown, sem backticks, só o JSON puro):

{
  "aluno": {
    "nome": "...",
    "localizacao": "...",
    "profissao": "...",
    "frequencia": "...",
    "nivel": "...",
    "historico": "..."
  },
  "objetivoPedagogico": "Parágrafo detalhado descrevendo a meta pedagógica do programa, personalizado para este aluno. 2-3 parágrafos.",
  "diagnostico": {
    "forcas": ["lista de 5-6 pontos fortes identificados na consultoria e dados"],
    "melhorias": ["lista de 5-6 pontos de melhoria identificados"]
  },
  "metodologia": [
    {"titulo": "Nome da estratégia", "descricao": "Explicação da abordagem metodológica"},
    ... (4-5 estratégias personalizadas)
  ],
  "aulas": [
    {
      "numero": 1,
      "fase": "foundation|expansion|fluency",
      "tema": "Título do tema da aula",
      "focoLinguistico": "Descrição detalhada do foco linguístico",
      "atividadeEmSala": "Descrição detalhada da atividade em sala de aula",
      "deverDeCasa": "Descrição do dever de casa"
    },
    ... (${numAulas} aulas total)
  ],
  "continuidade": "Parágrafo descrevendo os próximos blocos de aulas e plano de longo prazo. 2-3 parágrafos.",
  "exercicios": [
    {
      "aulaNumero": 1,
      "tema": "Tema da aula",
      "vocabulario": [
        {"en": "English word", "pt": "Tradução", "exemplo": "Example sentence"}
      ],
      "frasesPronuncia": [
        {"frase": "English phrase to practice", "traducao": "Tradução em português"}
      ],
      "completarFrases": [
        {"frase": "Sentence with ___ blank", "resposta": "answer", "dica": "Hint"}
      ],
      "quiz": [
        {"pergunta": "Pergunta em português sobre situação", "opcoes": ["A", "B", "C"], "correta": 1}
      ],
      "dialogo": {
        "contexto": "Descrição da situação",
        "linhas": [
          {"speaker": "Other person role", "speakerLabel": "XX", "fala": "English dialogue line", "tipo": "npc"},
          {"speaker": "Você", "speakerLabel": "AL", "fala": "", "resposta": "expected answer", "placeholder": "Hint...", "tipo": "aluno"}
        ]
      },
      "midias": [
        {"tipo": "filme|serie|podcast", "titulo": "Title", "descricao": "Description", "dica": "Tip"}
      ]
    }
  ]
}

REGRAS:
- Todas as ${numAulas} aulas devem ter exercícios correspondentes no array "exercicios"
- Cada aula deve ter: vocabulário conforme nível CEFR (A0=4-5, A1=5-7, A2=6-8, B1=7-9, B2+=10-12 palavras novas), 3-4 frases de pronúncia, 3-4 frases para completar, 2 perguntas de quiz, 1 diálogo com 4-6 linhas, 2-3 mídias
- O vocabulário e exercícios DEVEM ser relevantes ao tema específico da aula
- Frases em inglês devem ser gramaticalmente perfeitas
- Traduções devem ser precisas e com acentuação correta em português
- A fase das aulas deve seguir: primeiras ~30% = "foundation", meio ~40% = "expansion", últimas ~30% = "fluency"
- O conteúdo deve ser progressivo — cada aula constrói sobre a anterior
- Adapte a complexidade ao nível do aluno (${nivel})
- TODOS os textos em português devem ter acentuação correta (é, ã, ç, etc.)`;

    const message = await client.messages.create({
      model: 'claude-sonnet-4-6',
      max_tokens: 16000,
      messages: [{ role: 'user', content: prompt }]
    });

    const text = message.content[0].text;
    const parseResult = robustJSONParse(text);
    if (!parseResult.success) {
      logJSONError('gerar-plano', parseResult.error, 1, text);
      throw new Error(`Falha ao interpretar resposta da IA como JSON: ${parseResult.error}`);
    }
    const plano = parseResult.data;

    // Generate a unique ID for this plan
    const id = nome.toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, '').replace(/[^a-z0-9]+/g, '-').replace(/-+/g, '-').replace(/^-|-$/g, '') + '-' + Date.now().toString(36);

    // Store in Vercel KV or return for client-side storage
    const result = { id, plano, criadoEm: new Date().toISOString() };

    res.status(200).json(result);
  } catch (error) {
    console.error('Error:', error);
    res.status(500).json({ error: error.message || 'Internal server error' });
  }
};
