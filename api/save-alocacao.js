const { createClient } = require('@supabase/supabase-js');

const supabase = process.env.SUPABASE_URL && process.env.SUPABASE_SERVICE_KEY
  ? createClient(process.env.SUPABASE_URL, process.env.SUPABASE_SERVICE_KEY)
  : null;

module.exports = async (req, res) => {
  if (req.method !== 'POST') return res.status(405).json({ error: 'Method not allowed' });

  try {
    const { id, professor, horarios, zoomLink, alocacao } = req.body;
    if (!id) return res.status(400).json({ error: 'id is required' });
    if (!supabase) return res.status(500).json({ error: 'Supabase not configured' });

    // Read current row to merge into data JSON
    const { data: current, error: readErr } = await supabase.from('perfis').select('data').eq('id', id).single();
    if (readErr) return res.status(500).json({ error: 'Aluno não encontrado: ' + readErr.message });

    const existingData = current.data || {};
    const updatedData = {
      ...existingData,
      alocacao: alocacao || existingData.alocacao || {},
      professor: professor !== undefined ? professor : (existingData.professor || ''),
      horarios: horarios !== undefined ? horarios : (existingData.horarios || ''),
      // Link do Zoom guardado no JSON `data` (a tabela `perfis` nao tem coluna zoom_link,
      // e `data` sempre existe). O CX preenche pelo card ou pelo modal de alocacao.
      zoomLink: zoomLink !== undefined ? zoomLink : (existingData.zoomLink || '')
    };

    // Update data JSON column (guaranteed to exist) + try top-level columns
    const updatePayload = { data: updatedData };

    const { data: result, error } = await supabase
      .from('perfis')
      .update(updatePayload)
      .eq('id', id)
      .select('id');

    if (error) return res.status(500).json({ error: error.message });
    if (!result || result.length === 0) return res.status(404).json({ error: 'Nenhuma linha atualizada' });

    // Try updating top-level columns too (may not exist, ignore errors)
    try {
      const topLevel = {};
      if (professor !== undefined) topLevel.professor = professor;
      if (horarios !== undefined) topLevel.horarios = horarios;
      if (alocacao !== undefined) topLevel.alocacao = alocacao;
      if (Object.keys(topLevel).length > 0) {
        await supabase.from('perfis').update(topLevel).eq('id', id);
      }
    } catch (_) { /* columns may not exist, that's ok */ }

    res.status(200).json({ ok: true });
  } catch (error) {
    console.error('Erro ao salvar alocação:', error);
    res.status(500).json({ error: error.message });
  }
};
