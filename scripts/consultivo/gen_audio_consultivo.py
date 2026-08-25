#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera os MP3s oficiais da anatomia `consultivo` pela API da ElevenLabs (Anexo P-A).

    AUT-004 · Audio oficial por tecnologia proibida · BLOCKER
    "Web Speech API, speechSynthesis e SpeechSynthesisUtterance sao proibidos no build
     oficial." (Anexo P-A, Regra canonica)

O molde publicado usava `speechSynthesis` em 17 pontos e nao tinha uma unica chamada a
`new Audio`. Pior: escolhia a voz por NOME COMERCIAL do sistema operacional (`Microsoft
Aria`, `Samantha`, `Google US English`) -- e o §4 do anexo diz que "os nomes comerciais de
voz nao substituem Voice IDs".

O QUE ESTE SCRIPT FAZ, E O QUE NAO
-----------------------------------
FAZ: le o manifesto (emitido pelo builder a partir de `audio_surface.py`), chama o endpoint
que a CATEGORIA pede, grava o MP3 e devolve ao manifesto o que so existe depois de gerar --
duracao, checksum, e, no caso do dialogo, o instante em que cada turno comeca.

NAO FAZ: decidir o que precisa de audio. Isso e `audio_surface.py`, e e de la que o builder
tira a mesma lista. Duas descobertas independentes divergiriam, e a divergencia aparece como
audio que nao toca -- defeito que nao da erro em lugar nenhum.

DOIS ENDPOINTS, PORQUE SAO DUAS COISAS (§3)
--------------------------------------------
  fala unica  -> /v1/text-to-speech/{voice}
  dialogo     -> /v1/text-to-dialogue/with-timestamps

O `with-timestamps` nao e luxo: e o que permite UM arquivo por dialogo (como o anexo exige)
sem perder o realce de quem esta falando. Ele devolve `voice_segments` com o inicio de cada
turno, e esses instantes vao para o manifesto e de la para o `AUD_MAP`. Sem eles a escolha
seria entre desobedecer o anexo (um MP3 por turno) ou perder o realce.

IDEMPOTENTE PELO HASH DO TRANSCRIPT
------------------------------------
O nome do arquivo deriva do hash de (texto + voz + modelo). Rodar de novo pula o que ja
existe; mudar uma virgula do texto produz nome novo, arquivo novo e aprovacao nova -- que e
literalmente o que o §2 pede ("qualquer alteracao no transcript invalida a aprovacao").

A CREDENCIAL NAO ENTRA NO REPO (§1)
------------------------------------
`ELEVENLABS_API_KEY`, ou `~/.config/alumni/elevenlabs.key` fora do repositorio. Nunca em
codigo, prompt, arquivo distribuido ou log.

USO:
    python3 scripts/consultivo/gen_audio_consultivo.py _build/consultivo/{slug}/config.json
    python3 scripts/consultivo/gen_audio_consultivo.py ... --dry-run
"""
import hashlib
import json
import os
import subprocess
import sys
import time
import urllib.error
import urllib.request

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
sys.path.insert(0, AQUI)
import audio_surface  # noqa: E402

API = "https://api.elevenlabs.io/v1"
VOICE_SETTINGS = {"stability": 0.5, "similarity_boost": 0.75, "style": 0.0,
                  "use_speaker_boost": True}


def key():
    k = os.environ.get("ELEVENLABS_API_KEY")
    if not k:
        p = os.path.expanduser("~/.config/alumni/elevenlabs.key")
        if os.path.exists(p):
            k = open(p, encoding="utf-8").read().strip()
    if not k:
        raise SystemExit(
            "sem credencial: exporte ELEVENLABS_API_KEY ou crie ~/.config/alumni/"
            "elevenlabs.key (chmod 600). O Anexo P-A §1 proibe a credencial no repo.")
    return k


def _post(url, corpo, k, binario):
    req = urllib.request.Request(
        url, data=json.dumps(corpo).encode("utf-8"),
        headers={"xi-api-key": k, "Content-Type": "application/json",
                 "Accept": "audio/mpeg" if binario else "application/json"})
    ultimo = None
    for tentativa in range(4):
        try:
            with urllib.request.urlopen(req, timeout=180) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            corpo_erro = e.read()[:300].decode("utf-8", "replace")
            ultimo = f"HTTP {e.code}: {corpo_erro}"
            # 4xx que nao seja 429 e erro de pedido: repetir so gasta cota.
            if e.code != 429 and 400 <= e.code < 500:
                break
        except Exception as e:                                    # noqa: BLE001
            ultimo = str(e)
        time.sleep(2 * (tentativa + 1))
    raise SystemExit(f"ElevenLabs recusou: {ultimo}")


def duracao(caminho):
    """Segundos do MP3. Sem ffprobe, devolve None -- campo vazio e honesto; numero
    inventado nao e."""
    try:
        r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                            "-of", "csv=p=0", caminho], capture_output=True, text=True,
                           timeout=30)
        return round(float(r.stdout.strip()), 2) if r.returncode == 0 else None
    except (OSError, ValueError):
        return None


def gera(item, k, destino, dry):
    caminho = os.path.join(destino, item["file"])
    if os.path.exists(caminho) and os.path.getsize(caminho) > 0:
        return "pulado", caminho
    if dry:
        return "geraria", caminho

    if item["endpoint"] == audio_surface.EP_DIALOGO:
        dados = _post(f"{API}/text-to-dialogue/with-timestamps",
                      {"inputs": [{"text": i["text"], "voice_id": i["voice_id"]}
                                  for i in item["inputs"]],
                       "model_id": item["model_id"]}, k, binario=False)
        pacote = json.loads(dados)
        import base64
        audio = base64.b64decode(pacote["audio_base64"])
        # os instantes de cada turno, para o realce de quem fala (ver o cabecalho)
        item["turnos"] = [
            {"speaker": item["inputs"][s["dialogue_input_index"]]["speaker"],
             "inicio": round(s["start_time_seconds"], 3),
             "fim": round(s["end_time_seconds"], 3)}
            for s in pacote.get("voice_segments", [])]
    else:
        voz = item["roles"][0]["voice_id"]
        audio = _post(f"{API}/text-to-speech/{voz}",
                      {"text": item["transcript"], "model_id": item["model_id"],
                       "voice_settings": VOICE_SETTINGS}, k, binario=True)

    with open(caminho, "wb") as f:
        f.write(audio)
    return "gerado", caminho


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    dry = "--dry-run" in sys.argv
    if not args:
        raise SystemExit(__doc__.strip().splitlines()[-2].strip())
    cfg_path = os.path.abspath(args[0])
    cfg = json.load(open(cfg_path, encoding="utf-8"))
    frag = os.path.dirname(cfg_path)
    slug = cfg["slug"]
    destino = os.path.join(RAIZ, "public", "audio", slug)
    os.makedirs(destino, exist_ok=True)

    itens = audio_surface.manifesto(cfg, frag)
    print(f"=== audio oficial (Anexo P-A) — {slug}: {len(itens)} ativo(s)")
    k = None if dry else key()

    contagem = {"gerado": 0, "pulado": 0, "geraria": 0}
    for it in itens:
        estado, caminho = gera(it, k, destino, dry)
        contagem[estado] += 1
        if estado == "gerado":
            b = open(caminho, "rb").read()
            it["checksum"] = "sha256:" + hashlib.sha256(b).hexdigest()
            it["duration"] = duracao(caminho)
            it["qa_status"] = "gerado, aguardando aprovação auditiva"
            it["reviewer"] = ""
            it["date"] = time.strftime("%Y-%m-%d")
        elif estado == "pulado":
            b = open(caminho, "rb").read()
            it["checksum"] = "sha256:" + hashlib.sha256(b).hexdigest()
            it["duration"] = duracao(caminho)
            it.setdefault("qa_status", "gerado, aguardando aprovação auditiva")
        print(f"  {estado:8} {it['file']:44} {it['category']}")

    if not dry:
        mp = os.path.join(frag, "audio_manifest.json")
        # O manifesto anterior guarda os TURNOS e o qa_status ja aprovado. Reescrever do
        # zero apagaria a aprovacao auditiva de quem nao mudou -- e o §2 diz que so a
        # ALTERACAO invalida a aprovacao, nao a regeracao do manifesto.
        antigo = {}
        if os.path.exists(mp):
            antigo = {x.get("asset_id"): x for x in json.load(open(mp, encoding="utf-8"))}
        for it in itens:
            velho = antigo.get(it["asset_id"])
            if velho and velho.get("transcript_hash") == it.get("transcript_hash"):
                for campo in ("turnos", "qa_status", "reviewer", "date"):
                    if campo in velho and campo not in it:
                        it[campo] = velho[campo]
        with open(mp, "w", encoding="utf-8") as f:
            json.dump(itens, f, ensure_ascii=False, indent=1)
        print(f"\nmanifesto: {os.path.relpath(mp, RAIZ)}")

    print(f"\ngerados={contagem['gerado']}  pulados={contagem['pulado']}"
          + (f"  geraria={contagem['geraria']}" if dry else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
