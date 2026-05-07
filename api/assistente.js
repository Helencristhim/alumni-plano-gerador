const Anthropic = require('@anthropic-ai/sdk');
const { robustJSONParse, logJSONError } = require('../lib/sanitize-json');

const client = new Anthropic({ apiKey: process.env.ANTHROPIC_API_KEY });

module.exports = async (req, res) => {
  if (req.method !== 'POST') return res.status(405).json({ error: 'Method not allowed' });

  try {
    const { plano, instrucao } = req.body;

    const prompt = `Você é um assistente pedagógico. O professor quer alterar o plano de estudos abaixo.

PLANO ATUAL (JSON):
${JSON.stringify(plano, null, 2)}

INSTRUÇÃO DO PROFESSOR:
"${instrucao}"

Aplique a alteração solicitada pelo professor e retorne o plano COMPLETO atualizado em JSON, com a MESMA estrutura exata. Retorne APENAS o JSON puro, sem markdown, sem backticks, sem explicações.

REGRAS:
- Mantenha toda a estrutura intacta
- Só altere o que foi solicitado
- Se o professor pedir para trocar um tema de aula, atualize também os exercícios correspondentes
- Se adicionar ou remover aulas, ajuste o array de exercícios também
- Mantenha acentuação correta em português
- Mantenha inglês gramaticalmente correto`;

    const message = await client.messages.create({
      model: 'claude-sonnet-4-6',
      max_tokens: 16000,
      messages: [{ role: 'user', content: prompt }]
    });

    const text = message.content[0].text;
    const parseResult = robustJSONParse(text);
    if (!parseResult.success) {
      logJSONError('assistente', parseResult.error, 1, text);
      throw new Error(`Falha ao interpretar resposta da IA como JSON: ${parseResult.error}`);
    }
    const planoAtualizado = parseResult.data;

    res.status(200).json({ plano: planoAtualizado });
  } catch (error) {
    console.error('Error:', error);
    res.status(500).json({ error: error.message || 'Internal server error' });
  }
};
