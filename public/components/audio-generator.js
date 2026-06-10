/* ═══════════════════════════════════════════════════════════════
   ALUMNI BY BETTER — AUDIO GENERATOR
   Utilitario para gerar e gerenciar audios ElevenLabs.
   Inclui fallback via Web Speech API.

   USO COM ELEVENLABS:
   1. Obtenha uma API key em https://elevenlabs.io
   2. Defina a variavel de ambiente ELEVENLABS_API_KEY
      ou passe diretamente para generateAudio()
   3. Cada chamada consome ~150 caracteres de cota

   USO SEM API KEY (fallback automatico):
   - speakWithFallback() usa Web Speech API do navegador
   - Qualidade inferior mas funciona offline
   ═══════════════════════════════════════════════════════════════ */

/* ── Configuration ── */
const ELEVENLABS_CONFIG = {
  apiUrl: 'https://api.elevenlabs.io/v1/text-to-speech',
  voiceId: 'sfJopaWaOtauCD3HKX6Q',       // Arthur — male, neutral American
  modelId: 'eleven_multilingual_v2',
  stability: 0.5,
  similarity_boost: 0.75,
  outputFormat: 'mp3_44100_128'
};

/* Alternate voices for variety */
const VOICE_OPTIONS = {
  arthur:  'sfJopaWaOtauCD3HKX6Q',  // Male, neutral American (default)
  ellen:   'BIvP0GN1cAtSRTxNHnWS',  // Female, calm American conversational
  rachel:  '21m00Tcm4TlvDq8ikWAM',  // Female, calm American
  domi:    'AZnzlk1XvdvUeBnXmlld',  // Female, energetic
  bella:   'EXAVITQu4vr4xnSDxMaL',  // Female, soft
  josh:    'TxGEqnHWrfWFTfGW9XjX',  // Male, deep
  adam:    'sfJopaWaOtauCD3HKX6Q'    // Alias for Arthur
};


/* ═══════════════════════════════════════════════════════════════
   generateAudio(text, options)
   Gera um arquivo de audio via ElevenLabs API.

   @param {string} text — Texto em ingles para sintetizar
   @param {object} options — {
     apiKey: string (obrigatorio),
     voiceId: string (opcional, default Arthur),
     outputFormat: string (opcional),
     stability: number (opcional),
     similarity_boost: number (opcional)
   }
   @returns {Promise<Blob>} — Audio blob (mp3)
   ═══════════════════════════════════════════════════════════════ */
async function generateAudio(text, options = {}) {
  const apiKey = options.apiKey || (typeof process !== 'undefined' && process.env && process.env.ELEVENLABS_API_KEY);

  if (!apiKey) {
    throw new Error(
      'ElevenLabs API key required. Pass {apiKey: "..."} or set ELEVENLABS_API_KEY env var.'
    );
  }

  const voiceId = options.voiceId || ELEVENLABS_CONFIG.voiceId;
  const url = `${ELEVENLABS_CONFIG.apiUrl}/${voiceId}`;

  const body = {
    text: text,
    model_id: options.modelId || ELEVENLABS_CONFIG.modelId,
    voice_settings: {
      stability: options.stability ?? ELEVENLABS_CONFIG.stability,
      similarity_boost: options.similarity_boost ?? ELEVENLABS_CONFIG.similarity_boost
    }
  };

  const response = await fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'xi-api-key': apiKey,
      'Accept': 'audio/mpeg'
    },
    body: JSON.stringify(body)
  });

  if (!response.ok) {
    const errorText = await response.text();
    throw new Error(`ElevenLabs API error (${response.status}): ${errorText}`);
  }

  return await response.blob();
}


/* ═══════════════════════════════════════════════════════════════
   saveAudioBlob(blob, filename)
   Salva um blob de audio como arquivo (Node.js) ou download (browser).
   ═══════════════════════════════════════════════════════════════ */
async function saveAudioBlob(blob, filename) {
  // Node.js environment
  if (typeof process !== 'undefined' && typeof require !== 'undefined') {
    const fs = require('fs');
    const buffer = Buffer.from(await blob.arrayBuffer());
    fs.writeFileSync(filename, buffer);
    return filename;
  }

  // Browser environment — trigger download
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = filename;
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(url);
  return filename;
}


/* ═══════════════════════════════════════════════════════════════
   generateLessonAudios(lessonData, options)
   Gera todos os audios necessarios para uma aula.

   @param {object} lessonData — {
     vocab: [{en, pt, example}],
     phrases: [{text}],
     context: {text},
     grammar: {text}
   }
   @param {object} options — {apiKey, voiceId, outputDir}
   @returns {Promise<object>} — audioMap {text: blobOrPath}
   ═══════════════════════════════════════════════════════════════ */
async function generateLessonAudios(lessonData, options = {}) {
  const audioMap = {};
  const tasks = [];

  // Default voice IDs for different content types
  const VOICE_ARTHUR = VOICE_OPTIONS.arthur;  // Vocabulary/drilling
  const VOICE_ELLEN  = VOICE_OPTIONS.ellen;   // Dialogue/phrase-model

  // Vocabulary words — use Arthur voice (drilling)
  if (lessonData.vocab) {
    lessonData.vocab.forEach((item) => {
      if (item.en) {
        tasks.push({ key: item.en, text: item.en, voiceId: item.voiceId || VOICE_ARTHUR });
      }
      if (item.example) {
        tasks.push({ key: item.example, text: item.example, voiceId: item.voiceId || VOICE_ARTHUR });
      }
    });
  }

  // Phrases — use Ellen voice (dialogue/phrase-model)
  if (lessonData.phrases) {
    lessonData.phrases.forEach((phrase) => {
      const text = typeof phrase === 'string' ? phrase : phrase.text;
      const voiceId = (typeof phrase === 'object' && phrase.voiceId) ? phrase.voiceId : VOICE_ELLEN;
      if (text) {
        tasks.push({ key: text, text: text, voiceId: voiceId });
      }
    });
  }

  // Context — use Ellen voice (conversational)
  if (lessonData.context && lessonData.context.text) {
    tasks.push({ key: 'context', text: lessonData.context.text, voiceId: lessonData.context.voiceId || VOICE_ELLEN });
  }

  // Grammar — use Arthur voice (instructional)
  if (lessonData.grammar && lessonData.grammar.text) {
    tasks.push({ key: 'grammar', text: lessonData.grammar.text, voiceId: lessonData.grammar.voiceId || VOICE_ARTHUR });
  }

  // Generate sequentially to respect rate limits (10 req/s for free tier)
  for (const task of tasks) {
    try {
      const taskOptions = { ...options, voiceId: task.voiceId || options.voiceId };
      const blob = await generateAudio(task.text, taskOptions);

      if (options.outputDir) {
        const safeName = task.key.replace(/[^a-z0-9]/gi, '_').substring(0, 50).toLowerCase();
        const filename = `${options.outputDir}/${safeName}.mp3`;
        await saveAudioBlob(blob, filename);
        audioMap[task.key] = filename;
      } else {
        audioMap[task.key] = blob;
      }

      // Small delay between requests to avoid rate limiting
      await new Promise(resolve => setTimeout(resolve, 120));
    } catch (err) {
      console.warn(`[audio-generator] Falha ao gerar audio para "${task.key}":`, err.message);
      audioMap[task.key] = null;
    }
  }

  return audioMap;
}


/* ═══════════════════════════════════════════════════════════════
   buildAudioMap(audioFiles)
   Constroi o mapa texto->caminho para embedar no HTML.

   @param {object} audioFiles — {text: filePath, ...}
   @returns {object} — Mapa limpo, sem entradas null
   ═══════════════════════════════════════════════════════════════ */
function buildAudioMap(audioFiles) {
  const map = {};
  for (const [key, value] of Object.entries(audioFiles)) {
    if (value) {
      map[key] = value;
    }
  }
  return map;
}


/* ═══════════════════════════════════════════════════════════════
   speakWithFallback(text, audioMap)
   Toca audio pre-gerado ou usa Web Speech API como fallback.
   Funciona no browser sem dependencias externas.

   @param {string} text — Texto a reproduzir
   @param {object} audioMap — {text: "path/to/audio.mp3"}
   ═══════════════════════════════════════════════════════════════ */
function speakWithFallback(text, audioMap) {
  audioMap = audioMap || {};

  // If audioMap is empty or phrase not found, go straight to Web Speech API
  if (!audioMap || Object.keys(audioMap).length === 0) {
    _speakWithWebAPI(text);
    return;
  }

  // Normalize lookup: try exact match, then lowercased
  const file = audioMap[text] || audioMap[text.toLowerCase()];

  if (!file) {
    // Phrase not in audioMap — use Web Speech API directly
    _speakWithWebAPI(text);
    return;
  }

  // Pre-generated audio exists — try to play it
  try {
    if (file instanceof Blob) {
      const url = URL.createObjectURL(file);
      const audio = new Audio(url);
      audio.onended = function() { URL.revokeObjectURL(url); };
      audio.onerror = function(err) {
        console.warn('[audio] Blob audio failed to load, falling back to Web Speech API:', err);
        URL.revokeObjectURL(url);
        _speakWithWebAPI(text);
      };
      audio.play().catch(function(err) {
        console.warn('[audio] Blob playback failed, falling back to Web Speech API:', err);
        URL.revokeObjectURL(url);
        _speakWithWebAPI(text);
      });
    } else {
      // String path or URL
      const audio = new Audio(file);
      audio.onerror = function(err) {
        console.warn('[audio] MP3 file failed to load (' + file + '), falling back to Web Speech API:', err);
        _speakWithWebAPI(text);
      };
      audio.play().catch(function(err) {
        console.warn('[audio] MP3 playback failed (' + file + '), falling back to Web Speech API:', err);
        _speakWithWebAPI(text);
      });
    }
  } catch (err) {
    console.warn('[audio] Audio() constructor threw error, falling back to Web Speech API:', err);
    _speakWithWebAPI(text);
  }
}


/* ── Web Speech API fallback (internal) ── */
function _speakWithWebAPI(text) {
  if (typeof speechSynthesis === 'undefined') {
    console.warn('[audio] Speech synthesis not available in this browser.');
    return;
  }

  // Cancel any ongoing speech
  speechSynthesis.cancel();

  const utterance = new SpeechSynthesisUtterance(text);
  utterance.lang = 'en-US';
  utterance.rate = 0.85;
  utterance.pitch = 1.0;
  utterance.volume = 1.0;

  // Attempt to select a natural-sounding voice
  const voices = speechSynthesis.getVoices();
  const preferredVoices = [
    'Google US English',
    'Samantha',
    'Alex',
    'Microsoft Mark',
    'en-US'
  ];

  for (const pref of preferredVoices) {
    const match = voices.find(v =>
      v.name.includes(pref) || v.lang.startsWith(pref)
    );
    if (match) {
      utterance.voice = match;
      break;
    }
  }

  speechSynthesis.speak(utterance);
}


/* ═══════════════════════════════════════════════════════════════
   createAudioButton(text, audioMap, label)
   Gera HTML de um botao "Ouvir" para embedar em materiais.

   @param {string} text — Texto cujo audio sera tocado
   @param {object} audioMap — Mapa de audios
   @param {string} label — Label do botao (default "Ouvir")
   @returns {string} — HTML string
   ═══════════════════════════════════════════════════════════════ */
function createAudioButton(text, audioMap, label) {
  label = label || 'Ouvir';
  const audioSrc = audioMap[text] || audioMap[text.toLowerCase()];
  const iconSvg = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 0 1 0 7.07"/></svg>';

  if (audioSrc && typeof audioSrc === 'string') {
    return `<button class="audio-btn-student" onclick="(function(){var a=new Audio('${audioSrc.replace(/'/g, "\\'")}');a.play().catch(function(){var u=new SpeechSynthesisUtterance('${text.replace(/'/g, "\\'")}');u.lang='en-US';u.rate=0.85;speechSynthesis.speak(u);});})()">${iconSvg} ${label}</button>`;
  }

  // Fallback to Web Speech API
  return `<button class="audio-btn-student" onclick="(function(){if(typeof speakWithFallback==='function'){speakWithFallback('${text.replace(/'/g, "\\'")}',{});}else{var u=new SpeechSynthesisUtterance('${text.replace(/'/g, "\\'")}');u.lang='en-US';u.rate=0.85;speechSynthesis.speak(u);}})()">${iconSvg} ${label}</button>`;
}


/* ═══════════════════════════════════════════════════════════════
   BATCH GENERATION SCRIPT (Node.js CLI)

   Usage:
     ELEVENLABS_API_KEY=your_key node audio-generator.js lesson.json output/

   lesson.json format:
   {
     "vocab": [{"en": "check-in", "example": "I'd like to check in."}],
     "phrases": ["Could I have the bill?"],
     "context": {"text": "You arrive at a hotel..."},
     "grammar": {"text": "We use 'would like' to..."}
   }
   ═══════════════════════════════════════════════════════════════ */
if (typeof process !== 'undefined' && typeof require !== 'undefined' && require.main === module) {
  (async function() {
    const fs = require('fs');
    const path = require('path');

    const args = process.argv.slice(2);
    if (args.length < 2) {
      console.log('Usage: ELEVENLABS_API_KEY=... node audio-generator.js <lesson.json> <output-dir>');
      process.exit(1);
    }

    const lessonPath = args[0];
    const outputDir = args[1];

    if (!fs.existsSync(outputDir)) {
      fs.mkdirSync(outputDir, { recursive: true });
    }

    const lessonData = JSON.parse(fs.readFileSync(lessonPath, 'utf-8'));
    const apiKey = process.env.ELEVENLABS_API_KEY;

    if (!apiKey) {
      console.error('Set ELEVENLABS_API_KEY environment variable.');
      process.exit(1);
    }

    console.log('Generating audios...');
    const audioMap = await generateLessonAudios(lessonData, {
      apiKey,
      outputDir
    });

    // Write audioMap JSON
    const mapPath = path.join(outputDir, 'audioMap.json');
    const cleanMap = buildAudioMap(audioMap);
    fs.writeFileSync(mapPath, JSON.stringify(cleanMap, null, 2));

    console.log(`Done. ${Object.keys(cleanMap).length} audios generated.`);
    console.log(`Audio map saved to: ${mapPath}`);
  })();
}


/* ═══════════════════════════════════════════════════════════════
   EXPORTS
   ═══════════════════════════════════════════════════════════════ */
if (typeof module !== 'undefined' && module.exports) {
  module.exports = {
    ELEVENLABS_CONFIG,
    VOICE_OPTIONS,
    generateAudio,
    saveAudioBlob,
    generateLessonAudios,
    buildAudioMap,
    speakWithFallback,
    speakText,
    createAudioButton
  };
}

/* ═══════════════════════════════════════════════════════════════
   GLOBAL speakText() — wrapper chamado pelo exercises.js e pelos HTMLs gerados.
   Usa audioMap global (definido no HTML) com fallback para Web Speech API.
   Suporta play/pause toggle quando btnEl e fornecido.
   ═══════════════════════════════════════════════════════════════ */
var _activeDialogueAudio = null;
var _activeDialogueBtn = null;

var _playSvg = '<svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 010 7.07"/></svg>';
var _pauseSvg = '<svg viewBox="0 0 24 24"><rect x="6" y="4" width="4" height="16"/><rect x="14" y="4" width="4" height="16"/></svg>';

function _resetDialogueBtn(btn) {
  if (btn) {
    btn.classList.remove('playing');
    btn.innerHTML = _playSvg;
  }
}

function speakText(text, btnEl) {
  // If same button clicked while playing — pause/stop
  if (_activeDialogueAudio && _activeDialogueBtn === btnEl) {
    _activeDialogueAudio.pause();
    _activeDialogueAudio.currentTime = 0;
    _resetDialogueBtn(_activeDialogueBtn);
    _activeDialogueAudio = null;
    _activeDialogueBtn = null;
    return;
  }

  // Stop any other playing audio
  if (_activeDialogueAudio) {
    _activeDialogueAudio.pause();
    _activeDialogueAudio.currentTime = 0;
    _resetDialogueBtn(_activeDialogueBtn);
    _activeDialogueAudio = null;
    _activeDialogueBtn = null;
  }

  var map = (typeof audioMap !== 'undefined') ? audioMap : {};
  var file = map[text] || map[text.toLowerCase()];

  if (file && typeof file === 'string') {
    var audio = new Audio(file);
    _activeDialogueAudio = audio;
    _activeDialogueBtn = btnEl;

    if (btnEl) {
      btnEl.classList.add('playing');
      btnEl.innerHTML = _pauseSvg;
    }

    audio.onended = function() {
      _resetDialogueBtn(btnEl);
      _activeDialogueAudio = null;
      _activeDialogueBtn = null;
    };
    audio.onerror = function() {
      console.warn('[speakText] MP3 failed, falling back to Web Speech API');
      _resetDialogueBtn(btnEl);
      _activeDialogueAudio = null;
      _activeDialogueBtn = null;
      _speakWithWebAPI(text);
    };
    audio.play().catch(function(err) {
      console.warn('[speakText] Playback failed:', err);
      _resetDialogueBtn(btnEl);
      _activeDialogueAudio = null;
      _activeDialogueBtn = null;
      _speakWithWebAPI(text);
    });
  } else {
    // No MP3 — fallback to Web Speech API (no toggle for TTS)
    if (btnEl) {
      btnEl.style.opacity = '0.6';
      setTimeout(function() { btnEl.style.opacity = '1'; }, 600);
    }
    _speakWithWebAPI(text);
  }
}
