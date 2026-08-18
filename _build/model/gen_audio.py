#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""gen_audio.py — gera os MP3s ElevenLabs de uma aula buildada pelo build_from_model.py.
Lê o audio_manifest.json ao lado do config.json. Pula existentes. Vozes em voices.json
(REGRA 35: arthur/ellen — Ash/Kristen NÃO existem na conta). Modelo: eleven_multilingual_v2
(frases) e eleven_turbo_v2_5 + language_code='en' em texto de até 2 palavras — ver _model_for().

USO: ELEVENLABS_API_KEY=... python3 _build/model/gen_audio.py _build/{slug}-aula{N}/config.json
"""
import hashlib
import json
import os
import sys
import time
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
VOICES = json.load(open(os.path.join(HERE, 'voices.json'), encoding='utf-8'))

cfg_path = os.path.abspath(sys.argv[1])
cfg = json.load(open(cfg_path, encoding='utf-8'))
manifest = json.load(open(os.path.join(os.path.dirname(cfg_path), 'audio_manifest.json'), encoding='utf-8'))
OUT = os.path.join(ROOT, 'public', 'audio', cfg['slug'])
KEY = os.environ.get('ELEVENLABS_API_KEY')
if not KEY:
    # Fallback PERMANENTE: a key fica fora do repo público (nunca commitada), em
    # ~/.config/alumni/elevenlabs.key. Assim o áudio roda sem precisar passar a key
    # toda vez (env continua tendo prioridade). Ver memória elevenlabs-key-local.
    _keyfile = os.path.expanduser('~/.config/alumni/elevenlabs.key')
    if os.path.exists(_keyfile):
        with open(_keyfile, encoding='utf-8') as _kf:
            KEY = _kf.read().strip()
assert KEY, ('ELEVENLABS_API_KEY não setada e ~/.config/alumni/elevenlabs.key não existe. '
             'Crie o arquivo com a key (chmod 600) ou exporte a variável.')
os.makedirs(OUT, exist_ok=True)

# Vozes: voices.json (arthur/ellen, inglês) + override por config (cfg['voices']).
# REGRA: material NÃO-inglês (lang != 'en') NUNCA pode usar voz de inglês — exige
# MODELO KIDS: vozes de CRIANÇA por padrão, substituindo arthur/ellen SÓ pro kids
# (o adulto mantém arthur/ellen intocados). Leo = "Cute Energetic Young Kid" (personagem
# masculino/Bento); Candy = "Young & Sweet" (personagem feminino/Maya) — o PAR do diálogo
# é criança+criança. Override explícito no cfg['voices'] ainda vence. Ver memória
# kids-voices-crianca. Para separar NARRAÇÃO do diálogo no futuro, usar Ana (children story
# narrator, fBJDfBxPazPKo9oZ1P8t) num data-voice próprio.
if cfg.get('model') == 'kids':
    VOICES = {**VOICES, 'arthur': '1tDEBGOo8EqEPApM49eJ', 'ellen': 'Nggzl2QAXh3OijoXD116'}
# override com vozes do idioma-alvo (ex: espanhol = vozes de Espanha). Trava de código.
VOICES = {**VOICES, **cfg.get('voices', {})}
LANG = cfg.get('lang', 'en')
assert LANG == 'en' or cfg.get('voices'), (
    f"aula lang='{LANG}' SEM 'voices' no config — material não-inglês exige vozes do "
    f"idioma-alvo (proibido usar arthur/ellen, que são vozes de inglês).")

FORCE = '--force' in sys.argv or os.environ.get('GEN_AUDIO_FORCE') == '1'

# --only=a.mp3,b.mp3 — regera SÓ esses arquivos (conserto pontual de um áudio que saiu
# errado, sem torrar API nem mexer nos outros MP3 da aula, que estão bons). Implica --force
# nos escolhidos: é justamente o arquivo existente que se quer trocar.
ONLY = set()
for _a in sys.argv[2:]:
    if _a.startswith('--only='):
        ONLY |= {x.strip() for x in _a[len('--only='):].split(',') if x.strip()}
if ONLY:
    FORCE = True
    _known = {p['file'] for p in manifest}
    assert ONLY <= _known, '--only com arquivo fora do manifest: %s' % sorted(ONLY - _known)
    manifest = [p for p in manifest if p['file'] in ONLY]

# GUARD DE TRUNCAMENTO (nasce certo, não depende só do GATE 5b).
# A ElevenLabs às vezes devolve um clipe curto/parcial (foi o que truncou o Stage 2 da
# Anna). gen_audio gravava cego + pulava existentes => o arquivo ruim fossilizava e só o
# gate downstream pegava. Aqui medimos o retorno vs. o TEXTO (text-aware, MESMO corte do
# scripts/check_order_audio_len.py) e RE-TENTAMOS na hora. Piso 400 B/char: áudio saudável
# tem ~600-1150 B/char; truncado <200. Texto de 1-2 palavras fica muito acima de 400, então
# NUNCA re-tenta à toa. Se todas as tentativas vierem curtas, NÃO grava e conta como erro
# (sys.exit(1) => alto, dá pra re-rodar) em vez de gravar podre silenciosamente.
MIN_BYTES_PER_CHAR = 400
MAX_TRIES = 3


# PALAVRA SOLTA PRECISA DO IDIOMA TRAVADO (incidente Graziele, aula 7).
# O eleven_multilingual_v2 DEDUZ o idioma do texto. Numa frase ele acerta pelo contexto;
# num vocab card de UMA palavra não há contexto, e cognato latino sai com pronúncia de
# outra língua: "Arrive" saiu "arriva" (o ASR da própria ElevenLabs transcreveu 'Arriva'
# e 'אריווה'). Regerar no mesmo modelo REPETE o defeito — é determinístico, não sorteio —
# e o multilingual_v2 IGNORA language_code (o áudio volta byte a byte igual).
# Quem respeita language_code é o turbo/flash v2.5. Então: texto de até 2 palavras em
# material de inglês vai no eleven_turbo_v2_5 com language_code='en' (mesma voz, idioma
# travado); 3+ palavras seguem no multilingual_v2, onde o contexto já resolve.
SHORT_WORDS = 2


def _model_for(text):
    """(model_id, language_code) — trava o idioma onde falta contexto p/ o modelo deduzir."""
    if LANG == 'en' and len(text.split()) <= SHORT_WORDS:
        return 'eleven_turbo_v2_5', 'en'
    return 'eleven_multilingual_v2', None


def tts(text, voice):
    model, lang = _model_for(text)
    payload = {'text': text, 'model_id': model,
               'voice_settings': {'stability': 0.5, 'similarity_boost': 0.75,
                                  'style': 0.0, 'use_speaker_boost': True}}
    if lang:
        payload['language_code'] = lang
    body = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request('https://api.elevenlabs.io/v1/text-to-speech/' + VOICES[voice],
                                 data=body, headers={'xi-api-key': KEY, 'Content-Type': 'application/json',
                                                     'Accept': 'audio/mpeg'})
    with urllib.request.urlopen(req, timeout=90) as r:
        return r.read()


# ===== LEDGER DE PROCEDENCIA (o MP3 sabe de que TEXTO nasceu) =====
# O nome do arquivo de audio e POSICIONAL (a7_order_sequence.mp3), nao derivado do texto.
# Reescrever o exercicio NAO muda o nome -> o "pula existentes" acima mantinha para sempre
# o audio do RASCUNHO ANTERIOR, e nada downstream conseguia perceber: o MP3 e valido, tem
# o tamanho certo pro texto, e o manifesto (que e o DESEJADO) bate com a tela. Só ouvindo.
# Aconteceu na Fabiana, aulas 6 a 10: o audio do "Put the story in order" narra uma historia
# com outros personagens e outros eventos (PR deste conserto).
# O ledger grava, ao lado dos MP3s, o sha1 de (voz|texto) que PRODUZIU cada arquivo:
#   - hash bate      -> pula (nada mudou)
#   - hash diverge   -> REGENERA (o texto foi reescrito depois de gerar o audio)
#   - sem entrada    -> pula (legado: nao sabemos de que texto nasceu; REGRA 30)
# O gate scripts/check_audio_src.py exige o hash nos arquivos DO PR.
LEDGER = os.path.join(OUT, '_src.json')


def _src_hash(text, voice):
    return hashlib.sha1((voice + '|' + text).encode('utf-8')).hexdigest()


try:
    with open(LEDGER, encoding='utf-8') as _lf:
        ledger = json.load(_lf)
except (IOError, ValueError):
    ledger = {}


def _save_ledger():
    with open(LEDGER, 'w', encoding='utf-8') as _lf:
        json.dump(ledger, _lf, indent=1, sort_keys=True, ensure_ascii=False)
        _lf.write('\n')


gen = skip = err = stale = 0
for p in manifest:
    fp = os.path.join(OUT, p['file'])
    want = _src_hash(p['text'], p['voice'])
    if os.path.exists(fp) and not FORCE:
        have = ledger.get(p['file'])
        if have is None:
            skip += 1          # legado sem procedencia: nao se toca
            continue
        if have == want:
            skip += 1
            continue
        stale += 1
        print('  ~ %s DESSINCRONIZADO (texto mudou depois de gerar) — regenerando'
              % p['file'])
    floor = len(p['text']) * MIN_BYTES_PER_CHAR  # tamanho mínimo compatível com o texto
    data = None
    try:
        for attempt in range(1, MAX_TRIES + 1):
            data = tts(p['text'], p['voice'])
            if len(data) >= floor:
                break  # tamanho bate com o texto — ok
            print('  ~ %s CURTO (%d b p/ %d chars, min %d) — re-tentando %d/%d'
                  % (p['file'], len(data), len(p['text']), floor, attempt, MAX_TRIES))
            data = None
            time.sleep(1.2)
    except Exception as e:
        err += 1
        print('  ! ERR %s -> %s' % (p['file'], str(e)[:140]))
        continue
    if data is None:
        err += 1
        print('  ! TRUNCADO %s — %d tentativas vieram curtas p/ o texto; NAO gravado (re-rode)'
              % (p['file'], MAX_TRIES))
        continue
    open(fp, 'wb').write(data)
    ledger[p['file']] = want
    _save_ledger()
    gen += 1
    print('  + %s (%s, %d b)' % (p['file'], p['voice'], len(data)))
    time.sleep(0.3)
_save_ledger()
print('Done: %d gen (%d por texto reescrito), %d skip, %d err (total %d)'
      % (gen, stale, skip, err, len(manifest)))
sys.exit(1 if err else 0)
