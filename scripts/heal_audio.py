#!/usr/bin/env python3
"""
heal_audio.py — gera os áudios faltantes de uma aula a partir do PRÓPRIO HTML.

Para cada arquivo HTML dado, lê o audioMap embutido (mapa texto->arquivo .mp3),
descobre quais .mp3 estão referenciados mas NÃO existem em public/audio/, e gera
cada um via ElevenLabs usando o texto do próprio mapa (conteúdo garantido correto
— nada de adivinhar por nome).

Voz: ELLEN por padrão (aluna/narração); ARTHUR quando o nome do arquivo indica
falante masculino (david, victor, _dlg_mark, _male). Listenings de mock-player
(data-src sem entrada no audioMap) NÃO são gerados aqui — são reportados para
roteirização manual.

Uso:
  ELEVENLABS_API_KEY=... python3 scripts/heal_audio.py public/professor/x.html [...]
  (--dry para só listar o que faria)
"""
import os
import re
import sys
import json
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PUBLIC = os.path.join(ROOT, "public")
KEY = os.environ.get("ELEVENLABS_API_KEY", "")
ARTHUR = "sfJopaWaOtauCD3HKX6Q"
ELLEN = "BIvP0GN1cAtSRTxNHnWS"
MALE = re.compile(r"david|victor|_dlg_mark|_male|arthur|_man_", re.I)

# audioMap: "texto com aspas escapadas": "/audio/.../arquivo.mp3"
ENTRY = re.compile(r'"((?:[^"\\]|\\.)*)"\s*:\s*"(/audio/[^"]+\.mp3)"')


def parse_map(html):
    out = {}
    for m in ENTRY.finditer(html):
        text = m.group(1).replace('\\"', '"').replace("\\'", "'").replace("\\\\", "\\")
        out[m.group(2)] = text
    return out


def gen(text, voice, out_path):
    data = json.dumps({
        "text": text,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {"stability": 0.5, "similarity_boost": 0.75},
    }).encode()
    req = urllib.request.Request(
        f"https://api.elevenlabs.io/v1/text-to-speech/{voice}",
        data=data,
        headers={"xi-api-key": KEY, "Content-Type": "application/json", "Accept": "audio/mpeg"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=120) as r:
        buf = r.read()
    with open(out_path, "wb") as f:
        f.write(buf)
    return len(buf)


def main():
    dry = "--dry" in sys.argv
    files = [a for a in sys.argv[1:] if a.endswith(".html")]
    if not files:
        print("uso: heal_audio.py <html> [...] [--dry]")
        sys.exit(2)
    if not KEY and not dry:
        print("ERRO: ELEVENLABS_API_KEY ausente")
        sys.exit(2)

    total_gen = total_skip = total_orphan = 0
    for f in files:
        html = open(os.path.join(ROOT, f) if not os.path.isabs(f) else f, encoding="utf-8").read()
        amap = parse_map(html)
        # todas refs .mp3 do HTML
        all_refs = set(re.findall(r"/audio/[A-Za-z0-9_./-]+\.mp3", html))
        missing = sorted(r for r in all_refs if not os.path.exists(os.path.join(PUBLIC, r.lstrip("/"))))
        if not missing:
            print(f"✓ {os.path.basename(f)}: nada faltando")
            continue
        print(f"\n=== {os.path.basename(f)}: {len(missing)} faltando ===")
        for ref in missing:
            out_path = os.path.join(PUBLIC, ref.lstrip("/"))
            text = amap.get(ref)
            if not text or re.fullmatch(r"\s*\[[^\]]*\]\s*", text):
                total_orphan += 1
                motivo = "placeholder de exercício (ordenação) — gerar à parte" if text else "sem texto no audioMap, provável listening mock-player"
                print(f"  ⚠ ÓRFÃO ({motivo}): {os.path.basename(ref)}")
                continue
            voice = ARTHUR if MALE.search(os.path.basename(ref)) else ELLEN
            vname = "ARTHUR" if voice == ARTHUR else "ELLEN"
            if dry:
                print(f"  [dry] {os.path.basename(ref)} <- [{vname}] \"{text[:60]}\"")
                continue
            os.makedirs(os.path.dirname(out_path), exist_ok=True)
            try:
                n = gen(text, voice, out_path)
                total_gen += 1
                print(f"  ✓ {os.path.basename(ref)} ({n//1024}KB) [{vname}] \"{text[:50]}\"")
            except Exception as e:
                print(f"  ✗ FALHOU {os.path.basename(ref)}: {e}")
    print(f"\nresumo: gerados={total_gen} órfãos(sem texto)={total_orphan}")


if __name__ == "__main__":
    main()
