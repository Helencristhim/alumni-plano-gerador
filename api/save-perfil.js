const { createClient } = require('@supabase/supabase-js');

const supabase = process.env.SUPABASE_URL && process.env.SUPABASE_SERVICE_KEY
  ? createClient(process.env.SUPABASE_URL, process.env.SUPABASE_SERVICE_KEY)
  : null;

module.exports = async (req, res) => {
  if (req.method !== 'POST') return res.status(405).json({ error: 'Method not allowed' });

  try {
    const { id, perfil } = req.body;
    if (!id || !perfil) return res.status(400).json({ error: 'id and perfil are required' });

    if (!supabase) return res.status(500).json({ error: 'Supabase not configured' });

    const d = perfil.dadosFormulario || {};
    const { error } = await supabase.from('perfis').upsert({
      id,
      data: perfil,
      status: perfil.status || 'rascunho',
      nome: d.nome || perfil.nome || id,
      nivel: perfil.dadosExtraidos?.nivel?.valor || d.nivel || '',
      num_aulas: parseInt(d.numAulas) || 0,
      foco: d.foco || ''
    });

    if (error) return res.status(500).json({ error: error.message });
    res.status(200).json({ ok: true });
  } catch (error) {
    console.error('Erro ao salvar perfil:', error);
    res.status(500).json({ error: error.message || 'Erro ao salvar perfil' });
  }
};
