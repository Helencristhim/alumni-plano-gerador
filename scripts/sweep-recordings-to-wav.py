#!/usr/bin/env python3
"""
Rede de seguranca: varre o bucket Supabase 'recordings' e converte para WAV qualquer
gravacao que ainda esteja em Opus (audio/mp4 ou audio/webm). Idempotente — pula o que ja
e WAV. Converte no MESMO path (as URLs continuam validas) com content-type audio/wav.

Motivo: o Chrome grava em Opus, que o Safari nao decodifica. A correcao principal forca
webm + transcoda no upload (public/lib/activity-sync.js). Este script e so um seguro extra
para o caso raro de alguma gravacao escapar como Opus.

Requer: ffmpeg no PATH. Em ambiente Linux: `apt-get install -y ffmpeg`. Em macOS: `brew install ffmpeg`.
Uso: python3 scripts/sweep-recordings-to-wav.py
"""
import json, subprocess, urllib.request, urllib.parse, os, tempfile, shutil, sys

# Chave publishable (anon) — ja e publica em public/lib/supabase-config.js
AK = "sb_publishable_RjekGapp8WtVbDx0J8etDg_hVq7na29"
SB = "https://xxdggcopydghbmgqqebq.supabase.co"
BUCKET = "recordings"
H = {"apikey": AK, "Authorization": "Bearer " + AK}


def req(method, url, data=None, headers=None, raw=False):
    r = urllib.request.Request(url, data=data, method=method)
    for k, v in (headers or {}).items():
        r.add_header(k, v)
    with urllib.request.urlopen(r) as resp:
        return resp.read() if raw else json.loads(resp.read())


def listdir(prefix):
    out, off = [], 0
    while True:
        items = req("POST", f"{SB}/storage/v1/object/list/{BUCKET}",
                    data=json.dumps({"prefix": prefix, "limit": 100, "offset": off}).encode(),
                    headers={**H, "Content-Type": "application/json"})
        if not items:
            break
        out += items
        if len(items) < 100:
            break
        off += 100
    return out


def main():
    if not shutil.which("ffmpeg"):
        print("ERRO: ffmpeg nao encontrado no PATH. Instale (apt-get install -y ffmpeg / brew install ffmpeg).")
        sys.exit(1)

    folders = [x["name"] for x in listdir("") if x.get("id") is None]
    print(f"Pastas: {len(folders)}")
    conv = skip = fail = 0
    failed = []
    for folder in folders:
        for it in listdir(folder + "/"):
            if it.get("id") is None:
                continue
            mime = ((it.get("metadata") or {}).get("mimetype") or "").lower()
            path = f"{folder}/{it['name']}"
            if "wav" in mime:
                skip += 1
                continue
            ep = urllib.parse.quote(path)
            try:
                data = req("GET", f"{SB}/storage/v1/object/public/{BUCKET}/{ep}", headers=H, raw=True)
            except Exception:
                fail += 1; failed.append(path + " (download)"); continue
            with tempfile.NamedTemporaryFile(suffix=".in", delete=False) as f:
                f.write(data); inp = f.name
            outp = inp + ".wav"
            # 16kHz mono: voz nitida + arquivo pequeno (evita HTTP 400 em gravacoes longas)
            rc = subprocess.run(["ffmpeg", "-y", "-i", inp, "-ar", "16000", "-ac", "1", outp],
                                capture_output=True).returncode
            if rc != 0 or not os.path.exists(outp) or os.path.getsize(outp) < 100:
                fail += 1; failed.append(path + " (ffmpeg)")
                os.unlink(inp)
                if os.path.exists(outp):
                    os.unlink(outp)
                continue
            wav = open(outp, "rb").read()
            try:
                req("PUT", f"{SB}/storage/v1/object/{BUCKET}/{ep}", data=wav,
                    headers={**H, "Content-Type": "audio/wav", "x-upsert": "true", "Cache-Control": "max-age=60"}, raw=True)
                conv += 1; print(f"  CONVERTIDO {path}")
            except Exception as e:
                fail += 1; failed.append(f"{path} (upload {e})")
            os.unlink(inp); os.unlink(outp)

    print(f"\nResultado: convertidos={conv} ja-wav={skip} falhas={fail}")
    for x in failed:
        print("  FALHA:", x)


if __name__ == "__main__":
    main()
