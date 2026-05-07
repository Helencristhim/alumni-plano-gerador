const fs = require('fs');
const path = require('path');

module.exports = async (req, res) => {
  if (req.method !== 'POST') return res.status(405).json({ error: 'Method not allowed' });

  try {
    const { id, perfil } = req.body;
    if (!id || !perfil) return res.status(400).json({ error: 'id and perfil are required' });

    const perfisDir = path.join(process.cwd(), 'public', 'perfis');
    if (!fs.existsSync(perfisDir)) fs.mkdirSync(perfisDir, { recursive: true });

    // Save profile JSON
    fs.writeFileSync(path.join(perfisDir, `${id}.json`), JSON.stringify(perfil, null, 2));

    // Update index
    const indexPath = path.join(perfisDir, 'index.json');
    let index = [];
    try { index = JSON.parse(fs.readFileSync(indexPath, 'utf8')); } catch(e) {}

    const d = perfil.dadosFormulario || {};
    const existing = index.findIndex(i => i.id === id);
    const entry = {
      id,
      nome: d.nome || perfil.nome || id,
      nivel: perfil.dadosExtraidos?.nivel?.valor || d.nivel || '',
      numAulas: d.numAulas || 0,
      criadoEm: perfil.criadoEm || new Date().toISOString(),
      perfilStatus: perfil.status || 'rascunho',
      foco: d.foco || ''
    };

    if (existing >= 0) {
      index[existing] = entry;
    } else {
      index.push(entry);
    }
    fs.writeFileSync(indexPath, JSON.stringify(index, null, 2));

    res.status(200).json({ ok: true, saved: `perfis/${id}.json` });
  } catch (error) {
    console.error('Erro ao salvar perfil:', error);
    res.status(500).json({ error: error.message || 'Erro ao salvar perfil' });
  }
};
