const { createClient } = require('@supabase/supabase-js');
const fs = require('fs');
const path = require('path');

const SUPABASE_URL = process.env.SUPABASE_URL || 'https://xxdggcopydghbmgqqebq.supabase.co';
const SUPABASE_SERVICE_KEY = process.env.SUPABASE_SERVICE_KEY;
if (!SUPABASE_SERVICE_KEY) { console.error('Set SUPABASE_SERVICE_KEY env var'); process.exit(1); }

const supabase = createClient(SUPABASE_URL, SUPABASE_SERVICE_KEY);

async function migrate() {
  const perfisDir = path.join(__dirname, '..', 'public', 'perfis');
  const registryPath = path.join(__dirname, '..', 'public', 'planos', 'registry.json');

  // 1. Load registry.json entries
  let registry = [];
  try { registry = JSON.parse(fs.readFileSync(registryPath, 'utf8')); } catch(e) {}

  // 2. Load all JSON profile files
  const files = fs.readdirSync(perfisDir).filter(f => f.endsWith('.json') && f !== 'index.json');

  const rows = [];

  // Add profiles from JSON files (full data)
  for (const file of files) {
    const id = file.replace('.json', '');
    const data = JSON.parse(fs.readFileSync(path.join(perfisDir, file), 'utf8'));
    const d = data.dadosFormulario || {};
    rows.push({
      id,
      data,
      status: data.status || 'rascunho',
      nome: d.nome || data.nome || id,
      nivel: data.dadosExtraidos?.nivel?.valor || d.nivel || '',
      num_aulas: parseInt(d.numAulas) || 0,
      foco: d.foco || ''
    });
    console.log(`  JSON: ${id} (${d.nome || id})`);
  }

  // Add registry entries that don't have JSON files
  for (const reg of registry) {
    if (!rows.find(r => r.id === reg.id)) {
      rows.push({
        id: reg.id,
        data: { dadosFormulario: { nome: reg.nome, nivel: reg.nivel, numAulas: reg.numAulas, foco: reg.foco } },
        status: reg.perfilStatus || 'sem_perfil',
        nome: reg.nome || reg.id,
        nivel: reg.nivel || '',
        num_aulas: parseInt(reg.numAulas) || 0,
        foco: reg.foco || ''
      });
      console.log(`  Registry: ${reg.id} (${reg.nome})`);
    }
  }

  console.log(`\nMigrando ${rows.length} perfis para Supabase...`);

  const { data, error } = await supabase.from('perfis').upsert(rows);

  if (error) {
    console.error('ERRO:', error);
  } else {
    console.log('Migração concluída com sucesso!');

    // Verify
    const { data: check } = await supabase.from('perfis').select('id, nome, status').order('created_at', { ascending: false });
    console.log('\nPerfis no Supabase:');
    check.forEach(r => console.log(`  - ${r.id}: ${r.nome} [${r.status}]`));
  }
}

migrate().catch(console.error);
