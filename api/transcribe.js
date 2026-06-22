// Speech-to-Text para o word-by-word (escopo inicial: aula do Marcos).
// Recebe o audio gravado (base64) e transcreve via ElevenLabs Scribe.
// Requer ELEVENLABS_API_KEY nas env vars do Vercel.
module.exports = async (req, res) => {
  if (req.method !== 'POST') return res.status(405).json({ error: 'Method not allowed' });
  try {
    var key = process.env.ELEVENLABS_API_KEY;
    if (!key) return res.status(500).json({ error: 'STT nao configurado (ELEVENLABS_API_KEY ausente)' });
    var body = req.body || {};
    var audioBase64 = body.audioBase64;
    var mimeType = body.mimeType || 'audio/webm';
    var lang = body.lang || 'eng';
    if (!audioBase64) return res.status(400).json({ error: 'audioBase64 obrigatorio' });
    var b64 = String(audioBase64).replace(/^data:[^;]+;base64,/, '');
    var buf = Buffer.from(b64, 'base64');
    if (!buf.length) return res.status(400).json({ error: 'audio vazio' });
    if (buf.length > 8 * 1024 * 1024) return res.status(413).json({ error: 'audio grande demais' });

    var ext = mimeType.indexOf('mp4') !== -1 ? 'mp4' : 'webm';
    var form = new FormData();
    form.append('model_id', 'scribe_v1');
    form.append('language_code', lang);
    form.append('file', new Blob([buf], { type: mimeType }), 'rec.' + ext);

    var r = await fetch('https://api.elevenlabs.io/v1/speech-to-text', {
      method: 'POST',
      headers: { 'xi-api-key': key },
      body: form
    });
    var data = await r.json().catch(function () { return {}; });
    if (!r.ok) return res.status(502).json({ error: 'STT falhou', detail: data });
    return res.status(200).json({ text: (data && data.text) || '' });
  } catch (e) {
    return res.status(500).json({ error: String((e && e.message) || e) });
  }
};
