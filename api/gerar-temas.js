const Anthropic = require('@anthropic-ai/sdk');
const client = new Anthropic({ apiKey: process.env.ANTHROPIC_API_KEY });

module.exports = async (req, res) => {
  if (req.method !== 'POST') return res.status(405).json({ error: 'Method not allowed' });

  try {
    const { nome, foco, nivel, numAulas, profissao, cidade, vitoria, historico, idade, forcas, fraquezas, resumo, hobbies,
            modalidade,
            // Novos parâmetros para geração em blocos (Regra 121)
            bloco, aulaInicio, aulaFim, temasAnteriores } = req.body;

    if (!foco || !numAulas) {
      return res.status(400).json({ error: 'Foco e número de aulas são obrigatórios.' });
    }

    // Determinar range de aulas a gerar
    const inicio = aulaInicio || 1;
    const fim = aulaFim || parseInt(numAulas);
    const totalBloco = fim - inicio + 1;
    const blocoNum = bloco || 1;
    const totalBlocos = Math.ceil(parseInt(numAulas) / 5) || 1;

    // Read CEFR document for level-specific rules
    const fs = require('fs');
    const path = require('path');
    let cefrContent = '';
    try {
      cefrContent = fs.readFileSync(path.join(__dirname, '..', 'docs', 'CEFR-ALUMNI.md'), 'utf8');
    } catch(e) { cefrContent = ''; }

    // Extract only the relevant level section
    const nivelKey = (nivel || '').toUpperCase().replace(/[^A-C0-2+]/g, '').substring(0, 3);
    let levelSection = '';
    if (cefrContent) {
      const levelHeaders = {
        'A0': '### A0 — BEGINNER ABSOLUTO',
        'A1': '### A1 — INICIANTE',
        'A2': '### A2 — PRÉ-INTERMEDIÁRIO',
        'B1': '### B1 — INTERMEDIÁRIO',
        'B2': '## B2',
        'C1': '## C1',
        'C1+': '### C1+ — AVANÇADO PLUS',
        'C2': '## C2'
      };
      const header = levelHeaders[nivelKey];
      if (header) {
        const startIdx = cefrContent.indexOf(header);
        if (startIdx !== -1) {
          const nextHeader = cefrContent.indexOf('\n### ', startIdx + header.length);
          const nextSection = cefrContent.indexOf('\n---', startIdx + header.length);
          const endIdx = Math.min(
            nextHeader !== -1 ? nextHeader : cefrContent.length,
            nextSection !== -1 ? nextSection : cefrContent.length
          );
          levelSection = cefrContent.substring(startIdx, endIdx).trim();
        }
      }
    }

    // Extract mixing rules
    let mixingRules = '';
    const mixIdx = cefrContent.indexOf('### 9.5.2');
    if (mixIdx !== -1) {
      const mixEnd = cefrContent.indexOf('### 9.5.3', mixIdx);
      mixingRules = cefrContent.substring(mixIdx, mixEnd !== -1 ? mixEnd : mixIdx + 2000).trim();
    }

    // Contexto de blocos anteriores para continuidade pedagógica
    let contextoAnteriores = '';
    if (temasAnteriores && temasAnteriores.length > 0) {
      contextoAnteriores = `
CONTEXTO DE AULAS JÁ GERADAS (blocos anteriores — use para CONTINUIDADE):
Os seguintes temas já foram planejados. Você DEVE:
- Continuar a progressão pedagógica (não repetir temas já cobertos)
- NUNCA repetir vocabulário como novo conteúdo (Regra 140) — pode referenciar para revisão
- Manter coerência temática e progressão de complexidade
- Construir sobre o que já foi ensinado

Temas já planejados:
${temasAnteriores.map(t => '- Aula ' + t.aula + ': ' + t.tema + ' | Foco: ' + (t.focoLinguistico || '').substring(0, 100)).join('\n')}
`;
    }

    // Contexto de bloco
    let contextoBlocos = '';
    if (totalBlocos > 1) {
      contextoBlocos = `
GERAÇÃO EM BLOCOS (Regra 121):
Você está gerando o BLOCO ${blocoNum} de ${totalBlocos} do programa completo de ${numAulas} aulas.
Este bloco contém as aulas ${inicio} a ${fim} (${totalBloco} aulas).
${blocoNum === 1 ? 'Este é o PRIMEIRO bloco — inclui aula diagnóstica + introdução.' : ''}
${blocoNum === totalBlocos ? 'Este é o ÚLTIMO bloco — a aula ' + fim + ' DEVE ser revisão geral + simulação completa + celebração.' : ''}
${blocoNum > 1 && blocoNum < totalBlocos ? 'Este é um bloco intermediário — mantenha progressão e não inclua aula diagnóstica nem final.' : ''}
`;
    }

    const prompt = `Você é um designer instrucional sênior especializado em ensino de inglês personalizado, com formação em Cambridge CELTA/DELTA e experiência com o modelo PPP (Presentation-Practice-Production).

${levelSection ? 'REGRAS CEFR PARA O NÍVEL DO ALUNO:\n' + levelSection + '\n\n' : ''}
${mixingRules ? 'REGRA DE MESCLA INGLÊS GERAL + FOCO:\n' + mixingRules + '\n\n' : ''}
${contextoBlocos}
${contextoAnteriores}
DADOS DO ALUNO:
- Nome: ${nome || 'Aluno'}
- Profissão: ${profissao || 'Não informada'}
- Cidade: ${cidade || 'Não informada'}
- Idade: ${idade || 'Não informada'}
- Nível: ${nivel || 'Não informado'}
- Foco do programa: ${foco}
- Total de aulas do programa completo: ${numAulas}
- Aulas a gerar neste bloco: ${inicio} a ${fim} (${totalBloco} aulas)
- Duração de cada aula: 60-90 minutos
- Modalidade: ${modalidade || 'Online'}
- Histórico com inglês: ${historico || 'Não informado'}
- Vitórias desejadas: ${vitoria || 'Não informadas'}
${forcas ? '- Forças identificadas: ' + forcas : ''}
${fraquezas ? '- Pontos de melhoria: ' + fraquezas : ''}
${resumo ? '- Resumo do perfil: ' + resumo : ''}
${hobbies ? '- Hobbies e interesses pessoais: ' + hobbies : ''}

Gere um CURRÍCULO de ${totalBloco} aulas (aulas ${inicio} a ${fim}) 100% personalizado para este aluno.

REGRAS DE PLANEJAMENTO (TODAS obrigatórias):

PROGRESSÃO E ESTRUTURA:
- Progressão do mais básico ao mais complexo dentro do foco
- Seguir a progressão gramatical do CEFR: Foundation → Building → Expansion (ver seção CEFR acima)
${blocoNum === 1 ? '- Aula 1 SEMPRE é diagnóstica + introdução pessoal' : '- Continuar progressão dos blocos anteriores'}
${blocoNum === totalBlocos ? '- Última aula (aula ' + fim + ') SEMPRE é revisão geral + simulação completa + celebração' : ''}
- Se este bloco contiver a aula do meio do programa (~aula ${Math.round(parseInt(numAulas) / 2)}), incluir revisão + avaliação de progresso

MESCLA GERAL + FOCO (Regra 84, 123):
- Proporção por nível CEFR: A0/A1=70% geral + 30% foco, A2=60/40, B1=50/50, B2=40/60, C1+=30/70
- Mescla aplicada em 4 dimensões: vocabulário, contexto, production, atividades complementares
- Mesmo nas aulas 70% gerais, o foco aparece no contexto (nome, profissão, cidade do aluno)

PERSONALIZAÇÃO CONTEXTUAL (Regra 85, 122):
- NOMINALIZAÇÃO: usar nome REAL do aluno em temas e atividades — NUNCA nomes genéricos
- Usar profissão, cidade, empresa, evento-alvo do aluno como cenário dos exercícios
- Primeiro nome em contextos informais, sobrenome em formais (reservas, documentos)

HOBBIES E INTERESSES (Regra 76):
- USAR hobbies/interesses do aluno como CONTEXTO para aulas de inglês geral
- Ex: gosta de viagens → aula sobre viagens. Gosta de séries → vocabulário de séries. Economia → debate
- Não são aulas "sobre" o hobby — são aulas de inglês COM o hobby como tema

QUANTIDADE PEDAGÓGICA (Regra 119, 120, 139):
- Mínimo 10 palavras circulando por aula (novas + revisão)
- Vocabulary + Expressions obrigatórios em TODAS as aulas
- NUNCA repetir vocabulário como novo em aula posterior (Regra 140) — revisão e callback sim

MODALIDADE DA AULA (${modalidade || 'Online'}):
${(modalidade || 'Online') === 'Online' ? '- Atividades adaptadas para videoconferência (Zoom/Meet): tela compartilhada, chat, breakout rooms\n- Exercícios visuais na tela, role-play via vídeo, listening com áudio compartilhado\n- Homework digital: gravação de áudio, formulários, documentos compartilhados' : ''}
${(modalidade || '') === 'Presencial' ? '- Atividades presenciais: flashcards físicos, movimento pela sala, objetos reais\n- Role-play face a face, dinâmicas em dupla/grupo, board games\n- Homework: caderno, gravação de áudio, leitura impressa' : ''}
${(modalidade || '') === 'Híbrido' ? '- Combinar recursos online E presenciais conforme a aula\n- Indicar em cada atividade se é para aula online ou presencial\n- Homework sempre digital (acessível de qualquer lugar)' : ''}

INGLÊS AMERICANO (Regra 143):
- TODO material em American English por padrão (spelling, vocabulário, expressões, pronúncia)
- Datas: March 15th (não "the 15th of March")
- Spelling: color, organize, center (não colour, organise, centre)
- Exceção: se perfil do aluno indicar British English, sinalizar com [British English]

FORMATAÇÃO DO CURRÍCULO:
- ZERO emojis em qualquer campo (tema, foco, atividade, homework). Usar apenas texto puro
- Acentuação PT-BR perfeita em todos os textos em português
- Capitalização correta em todo início de frase

CONTEÚDO POR AULA (Regra 77, 138):
- Cada aula deve ter conteúdo para 90 MINUTOS (9 fases PPP)
- Atividades em aula: práticas e situacionais (role-play, debate, análise, drilling, listening)
- Homework: reforça o trabalhado em aula (escrita, áudio, leitura) — ESPECÍFICO e MENSURÁVEL

CARGAS EMOCIONAIS (Regra 135):
- Respeitar carga emocional do nível: A0=vergonha de começar, A2=platô, B2=quase fluente
- Incluir aulas de "desbloqueio" para alunos com ansiedade identificada no perfil

HISTÓRICO:
- Se o aluno já domina algo (histórico), NÃO repetir — avançar
- Respeitar experiências negativas anteriores (ex: professor amigo demais, turma com nível errado)

NÍVEL DE DETALHE EXIGIDO — cada campo deve ser EXTENSO e ESPECÍFICO:

- "tema": Nome descritivo conectado ao contexto real do aluno (não genérico). Ex: "Breaking the Ice — First Contact at International Events" ou "Talking About Your Job — IT Manager at Centauro/Nike"
- "focoLinguistico": Estruturas gramaticais ESPECÍFICAS + vocabulário LISTADO. Ex: "Present simple for job descriptions; corporate vocabulary (deal with, liaise with, oversee, ensure compliance); 'I'm responsible for…' / 'I work with…' / 'My team manages…'"
- "atividadeEmAula": Descrição DETALHADA de 3-5 linhas com cenário concreto, o que o professor faz, o que o aluno faz, e qual é o produto final. Ex: "Role-play: ${nome} arrives at a tech conference. Teacher plays an American attendee. Practice: approaching someone, introducing yourself, asking what brings them to the event. Drill 5 natural openers. Focus on body language + tone. Debrief: what felt blocked? What flowed? Record 60-second self-introduction for baseline."
- "homework": Tarefas ESPECÍFICAS e MENSURÁVEIS com duração estimada. Ex: "Record a 2-minute audio introducing yourself as if at a professional event. Use: name, company, role, city. Send recording. Also: listen to podcast episode about small talk and note 5 phrases."

CADA aula deve parecer planejada por um professor CELTA com 10 anos de experiência — nunca genérica.

FORMATO — retorne APENAS um JSON array, sem texto antes ou depois:
[
  {
    "aula": ${inicio},
    "tema": "Tema descritivo e específico",
    "focoLinguistico": "Estruturas + vocabulário listado + padrões de fala",
    "atividadeEmAula": "Descrição detalhada de 3-5 linhas com cenário, dinâmica e produto final",
    "homework": "Tarefas específicas e mensuráveis com duração estimada"
  }
]

Retorne EXATAMENTE ${totalBloco} objetos no array, numerados de ${inicio} a ${fim}. APENAS o JSON, nada mais.`;

    // Retry automático — max 2 tentativas para blocos grandes (>10 aulas), 3 para pequenos
    const maxRetries = totalBloco > 10 ? 2 : 3;
    let lastError = null;
    for (let tentativa = 1; tentativa <= maxRetries; tentativa++) {
      try {
        const response = await client.messages.create({
          model: 'claude-sonnet-4-6',
          max_tokens: 16000,
          messages: [{ role: 'user', content: prompt }]
        });

        const text = response.content[0].text.trim();

        // Parse JSON — try direct parse, then extract from markdown
        let curriculo;
        try {
          curriculo = JSON.parse(text);
        } catch (e) {
          const jsonMatch = text.match(/\[[\s\S]*\]/);
          if (jsonMatch) {
            curriculo = JSON.parse(jsonMatch[0]);
          } else {
            throw new Error('Resposta da IA não é JSON válido');
          }
        }

        // Generate plain-text temas for the textarea
        const temas = curriculo.map(a =>
          'Aula ' + a.aula + ': ' + a.tema + ' — ' + a.focoLinguistico
        ).join('\n');

        return res.status(200).json({
          temas,
          curriculo,
          bloco: {
            numero: blocoNum,
            aulaInicio: inicio,
            aulaFim: fim,
            totalBlocos: totalBlocos,
            geradoEm: new Date().toISOString()
          }
        });

      } catch (retryErr) {
        lastError = retryErr;
        console.error(`Tentativa ${tentativa}/3 falhou:`, retryErr.message);
        if (tentativa < 3) {
          await new Promise(r => setTimeout(r, 2000));
        }
      }
    }

    // Todas as tentativas falharam
    throw lastError;

  } catch (err) {
    console.error('Erro ao gerar temas:', err);
    return res.status(500).json({ error: 'Erro ao gerar temas: ' + err.message });
  }
};
