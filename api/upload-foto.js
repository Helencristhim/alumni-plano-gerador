const { createClient } = require('@supabase/supabase-js');

const supabase = process.env.SUPABASE_URL && process.env.SUPABASE_SERVICE_KEY
  ? createClient(process.env.SUPABASE_URL, process.env.SUPABASE_SERVICE_KEY)
  : null;

module.exports = async (req, res) => {
  if (req.method !== 'POST') return res.status(405).json({ error: 'Method not allowed' });

  try {
    if (!supabase) return res.status(500).json({ error: 'Supabase not configured' });

    const { slug, fileName, fileBase64 } = req.body;
    if (!slug || !fileBase64) return res.status(400).json({ error: 'slug and fileBase64 are required' });

    // Validate extension
    var ext = (fileName || 'photo.jpg').split('.').pop().toLowerCase();
    if (!['jpg', 'jpeg', 'png', 'webp'].includes(ext)) {
      return res.status(400).json({ error: 'Only jpg, jpeg, png, webp allowed' });
    }

    // Convert base64 to buffer
    var base64Data = fileBase64.replace(/^data:image\/\w+;base64,/, '');
    var buffer = Buffer.from(base64Data, 'base64');

    // Validate size (5MB max)
    if (buffer.length > 5 * 1024 * 1024) {
      return res.status(400).json({ error: 'File too large (max 5MB)' });
    }

    var path = slug + '.' + ext;
    var mimeType = ext === 'png' ? 'image/png' : ext === 'webp' ? 'image/webp' : 'image/jpeg';

    // Remove old file if exists (ignore errors)
    await supabase.storage.from('fotos-alunos').remove([path]);

    // Upload new file
    var { data, error } = await supabase.storage.from('fotos-alunos').upload(path, buffer, {
      contentType: mimeType,
      cacheControl: '3600',
      upsert: true
    });

    if (error) return res.status(500).json({ error: 'Upload failed: ' + error.message });

    // Get public URL
    var { data: urlData } = supabase.storage.from('fotos-alunos').getPublicUrl(path);
    var publicUrl = urlData.publicUrl;

    // Also update the perfil record with fotoUrl
    var { error: updateError } = await supabase
      .from('perfis')
      .update({ data: supabase.rpc ? undefined : undefined })
      .eq('id', slug);

    // Update fotoUrl in the perfil data JSON
    var { data: perfilData } = await supabase
      .from('perfis')
      .select('data')
      .eq('id', slug)
      .single();

    if (perfilData && perfilData.data) {
      var updatedData = { ...perfilData.data, fotoUrl: publicUrl };
      if (updatedData.dadosFormulario) {
        updatedData.dadosFormulario.fotoUrl = publicUrl;
      }
      await supabase.from('perfis').update({ data: updatedData }).eq('id', slug);
    }

    res.status(200).json({ ok: true, url: publicUrl });
  } catch (error) {
    console.error('Erro ao fazer upload da foto:', error);
    res.status(500).json({ error: error.message || 'Internal server error' });
  }
};
