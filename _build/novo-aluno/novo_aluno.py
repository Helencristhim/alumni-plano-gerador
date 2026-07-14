#!/usr/bin/env python3
"""
Gera o Perfil 360 de um aluno novo sem passar pelo formulario do site.

Faz o mesmo que a pagina "Novo Aluno" (public/index.html): monta o payload dos
8 blocos e faz POST em /api/perfil-360, que chama o Claude, valida o schema e
faz upsert na tabela `perfis` do Supabase.

Quem tem as chaves (ANTHROPIC_API_KEY, SUPABASE_SERVICE_KEY) e a funcao na
Vercel, nao esta maquina. Aqui so precisa de ELEVENLABS_API_KEY, e apenas se
voce mandar audio em vez de transcricao.

Uso:
    python3 _build/novo-aluno/novo_aluno.py --template > alunos/maria.json
    python3 _build/novo-aluno/novo_aluno.py alunos/maria.json --dry-run
    python3 _build/novo-aluno/novo_aluno.py alunos/maria.json
    python3 _build/novo-aluno/novo_aluno.py alunos/*.json        # lote
"""

import argparse
import json
import os
import re
import sys
import time
import unicodedata
from pathlib import Path

import requests

REPO = Path(__file__).resolve().parents[2]
OUT_DIR = REPO / "_build" / "_perfis-novos"
API = "https://alumni-plano-gerador.vercel.app/api/perfil-360"
SUPABASE_REST = "https://xxdggcopydghbmgqqebq.supabase.co/rest/v1/perfis"
SUPABASE_ANON = "sb_publishable_RjekGapp8WtVbDx0J8etDg_hVq7na29"  # publishable, mesma do site

MIN_PALAVRAS = 200  # mesmo limiar do contador do formulario

# Campos obrigatorios no formulario (marcados com * em public/index.html)
OBRIGATORIOS = [
    "nome", "idade", "sexo", "email",
    "foco", "numAulas", "duracao", "frequencia", "modalidadeAula",
    "nivel",
]

# Valores aceitos pelos <select> do formulario. Errar aqui envenena o prompt em
# silencio: a API aceita qualquer string, o Claude improvisa e o perfil sai torto.
ENUMS = {
    "sexo": ["Feminino", "Masculino"],
    "foco": ["100% Personalizado", "Travel English", "Business English",
             "Corporate + Legal", "Conversação", "Proficiência",
             "Apresentações", "Acadêmico", "Outros"],
    "duracao": ["30 min", "45 min", "60 min", "90 min"],
    "frequencia": ["1x por semana", "2x por semana", "3x por semana"],
    "modalidadeAula": ["Online", "Presencial", "Híbrido"],
    "plataforma": ["Zoom", "Google Meet", "Microsoft Teams", "Outra"],
    "nivel": ["A0", "A1", "A2", "B1", "B2", "C1", "C1+", "C2"],
    "modalidadeTrabalho": ["Presencial", "Remoto", "Híbrido"],
    "tempoForaAula": ["Nenhum", "30 min", "1 hora", "2+ horas"],
    "estiloAprendizagem": ["Visual", "Auditivo", "Lendo/escrevendo", "Praticando", "Não sei"],
    "estruturaPreferida": ["Bem estruturadas com roteiro", "Mistas", "Mais livres e espontâneas"],
    "lidaComErros": ["Fico frustrado", "Levo na boa e rio", "Depende do dia",
                     "Prefiro não arriscar para não errar"],
    "energiaPreferida": ["Calma e organizada", "Dinâmica e variada", "Depende do tema"],
    "tomVoz": ["Calmo", "Animado", "Monótono", "Variado", "Hesitante"],
    "energiaConsultoria": ["Constante", "Oscilou", "Cresceu ao longo", "Diminuiu ao longo"],
}

TEMPLATE = {
    "_comentario": "Campos obrigatorios: nome, idade, sexo, email, foco, numAulas, duracao, frequencia, modalidadeAula, nivel + (transcricao_arquivo OU audio_arquivo). O resto e opcional — o que voce deixar vazio, o Claude extrai da transcricao.",
    "nome": "Maria Clara Ferreira",
    "idade": 34,
    "sexo": "Feminino",
    "email": "maria@email.com",
    "foco": "100% Personalizado",
    "numAulas": 20,
    "duracao": "60 min",
    "frequencia": "1x por semana",
    "modalidadeAula": "Online",
    "nivel": "A2",
    "transcricao_arquivo": "alunos/maria-transcricao.txt",
    "audio_arquivo": "",
    "profissao": "",
    "cidade": "",
    "whatsapp": "",
    "plataforma": "Zoom",
    "horarios": "",
    "observacoesProfessor": {
        "tomVoz": "",
        "energiaConsultoria": "",
        "momentosAnimacao": "",
        "momentosHesitacao": "",
        "observacoesLivres": "",
    },
}


def slugify(nome: str) -> str:
    """Mesma regra do servidor (api/perfil-360.js) — o slug tem que bater."""
    s = unicodedata.normalize("NFD", nome.lower())
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return re.sub(r"^-|-$", "", s)


def limpar_legenda(texto: str) -> str:
    """Zoom exporta .vtt e .srt com cues e timestamps. Plaud exporta texto puro."""
    linhas = []
    for linha in texto.splitlines():
        l = linha.strip()
        if not l or l == "WEBVTT" or l.isdigit():
            continue
        if "-->" in l:
            continue
        if l.startswith(("NOTE ", "Kind:", "Language:")):
            continue
        if linhas and linhas[-1] == l:  # legenda repete a mesma fala em cues seguidos
            continue
        linhas.append(l)
    return "\n".join(linhas)


def ler_transcricao(caminho: Path) -> str:
    texto = caminho.read_text(encoding="utf-8", errors="replace")
    if caminho.suffix.lower() in (".vtt", ".srt") or texto.lstrip().startswith("WEBVTT"):
        texto = limpar_legenda(texto)
    return texto.strip()


def transcrever_audio(caminho: Path) -> str:
    """ElevenLabs Scribe. Usa a ELEVENLABS_API_KEY do .env.local."""
    key = os.environ.get("ELEVENLABS_API_KEY")
    if not key:
        sys.exit("ELEVENLABS_API_KEY ausente. Carregue o .env.local:\n"
                 "  set -a; . ./.env.local; set +a")

    mb = caminho.stat().st_size / 1e6
    print(f"  transcrevendo {caminho.name} ({mb:.0f} MB) via ElevenLabs Scribe...")
    t0 = time.time()
    with caminho.open("rb") as fh:
        r = requests.post(
            "https://api.elevenlabs.io/v1/speech-to-text",
            headers={"xi-api-key": key},
            data={"model_id": "scribe_v1", "language_code": "por", "diarize": "true"},
            files={"file": (caminho.name, fh)},
            timeout=1800,
        )
    if not r.ok:
        sys.exit(f"  STT falhou [{r.status_code}]: {r.text[:400]}")

    data = r.json()
    texto = _texto_com_falantes(data) or data.get("text", "")
    print(f"  transcricao pronta em {time.time()-t0:.0f}s ({len(texto.split())} palavras)")
    return texto.strip()


def _texto_com_falantes(data: dict) -> str:
    """Reconstroi o texto com rotulo de falante quando o diarize devolve speaker_id.

    Numa consultoria isso importa: sem separar quem fala, o Claude atribui ao
    aluno frases que sao do consultor.
    """
    palavras = data.get("words") or []
    if not any(p.get("speaker_id") for p in palavras):
        return ""
    blocos, atual, falante = [], [], None
    for p in palavras:
        if p.get("type") == "spacing":
            continue
        sid = p.get("speaker_id")
        if sid != falante and atual:
            blocos.append(f"{falante}: {''.join(atual).strip()}")
            atual = []
        falante = sid
        atual.append(p.get("text", ""))
    if atual:
        blocos.append(f"{falante}: {''.join(atual).strip()}")
    return "\n".join(blocos)


def validar(cfg: dict, arquivo: Path) -> list:
    erros = []
    for campo in OBRIGATORIOS:
        if not str(cfg.get(campo, "")).strip():
            erros.append(f"campo obrigatorio ausente: {campo}")
    for campo, validos in ENUMS.items():
        valor = str(cfg.get(campo, "")).strip()
        if valor and valor not in validos:
            erros.append(f"{campo}={valor!r} invalido. Aceitos: {validos}")
    obs = cfg.get("observacoesProfessor") or {}
    for campo in ("tomVoz", "energiaConsultoria"):
        valor = str(obs.get(campo, "")).strip()
        if valor and valor not in ENUMS[campo]:
            erros.append(f"observacoesProfessor.{campo}={valor!r} invalido. Aceitos: {ENUMS[campo]}")
    if not (cfg.get("transcricao_arquivo") or cfg.get("audio_arquivo")):
        erros.append("informe transcricao_arquivo ou audio_arquivo")
    return erros


def montar_payload(cfg: dict, transcricao: str, tem_audio: bool) -> dict:
    slug = slugify(cfg["nome"])
    obs = cfg.get("observacoesProfessor") or {}
    return {
        "nome": cfg["nome"], "idade": int(cfg["idade"]), "sexo": cfg["sexo"],
        "profissao": cfg.get("profissao", ""), "cidade": cfg.get("cidade", ""),
        "modalidadeTrabalho": cfg.get("modalidadeTrabalho", ""),
        "email": cfg["email"], "whatsapp": cfg.get("whatsapp", ""),

        "foco": cfg["foco"], "numAulas": int(cfg["numAulas"]),
        "duracao": cfg["duracao"], "frequencia": cfg["frequencia"],
        "modalidadeAula": cfg["modalidadeAula"], "plataforma": cfg.get("plataforma", ""),
        "horarios": cfg.get("horarios", ""),

        "existeEvento": bool(cfg.get("existeEvento", False)),
        "tipoEvento": cfg.get("tipoEvento", ""), "dataEvento": cfg.get("dataEvento", ""),
        "localEvento": cfg.get("localEvento", ""),

        "stake": cfg.get("stake", ""), "vitoria": cfg.get("vitoria", ""),

        "historicoIngles": cfg.get("historicoIngles", ""), "nivel": cfg["nivel"],
        "tempoForaAula": cfg.get("tempoForaAula", ""),

        "estiloAprendizagem": cfg.get("estiloAprendizagem", ""),
        "estruturaPreferida": cfg.get("estruturaPreferida", ""),
        "lidaComErros": cfg.get("lidaComErros", ""),
        "energiaPreferida": cfg.get("energiaPreferida", ""),

        "seriesFilmes": cfg.get("seriesFilmes", ""),
        "musicasPodcasts": cfg.get("musicasPodcasts", ""),
        "hobbies": cfg.get("hobbies", ""),

        "temAudio": tem_audio,
        "audioUrl": f"local://{slug}" if tem_audio else None,
        "resumoZoom": cfg.get("resumoZoom", ""),
        "transcricao": transcricao,
        "observacoesProfessor": {
            "tomVoz": obs.get("tomVoz", ""),
            "energiaConsultoria": obs.get("energiaConsultoria", ""),
            "momentosAnimacao": obs.get("momentosAnimacao", ""),
            "momentosHesitacao": obs.get("momentosHesitacao", ""),
            "observacoesLivres": obs.get("observacoesLivres", ""),
        },
        "slug": slug,
    }


def gerar(payload: dict, tentativas: int = 2) -> dict:
    """POST no /api/perfil-360. A propria API ja faz retry de schema; aqui o
    retry cobre o que ela desiste (JSON_PARSE_ERROR / SCHEMA_INCOMPLETE), que e
    exatamente o que a UI manda o usuario fazer: processar de novo."""
    for tentativa in range(1, tentativas + 1):
        t0 = time.time()
        print(f"  gerando perfil (tentativa {tentativa}/{tentativas}) — leva 1-3 min...")
        try:
            r = requests.post(API, json=payload, timeout=840)
        except requests.exceptions.Timeout:
            print("  timeout na API")
            continue

        if r.ok:
            print(f"  perfil gerado em {time.time()-t0:.0f}s")
            return r.json()

        try:
            erro = r.json()
        except ValueError:
            erro = {"error": r.text[:200]}
        print(f"  falhou [{r.status_code}]: {erro.get('error')} — {erro.get('message', '')}")
        if erro.get("error") not in ("JSON_PARSE_ERROR", "SCHEMA_INCOMPLETE"):
            break  # erro nao-transitorio: nao adianta insistir
    return {}


def confirmar_no_supabase(slug: str) -> dict:
    """A resposta da API dizer 200 nao prova que o upsert passou. Confere na fonte."""
    r = requests.get(
        SUPABASE_REST,
        params={"id": f"eq.{slug}", "select": "id,nome,nivel,status,num_aulas,foco"},
        headers={"apikey": SUPABASE_ANON},
        timeout=30,
    )
    linhas = r.json() if r.ok else []
    return linhas[0] if linhas else {}


def processar(arquivo: Path, dry_run: bool) -> bool:
    print(f"\n=== {arquivo.name}")
    cfg = json.loads(arquivo.read_text(encoding="utf-8"))

    erros = validar(cfg, arquivo)
    if erros:
        for e in erros:
            print(f"  ERRO: {e}")
        return False

    slug = slugify(cfg["nome"])
    base = arquivo.parent

    if cfg.get("transcricao_arquivo"):
        caminho = (base / cfg["transcricao_arquivo"]).resolve()
        if not caminho.exists():
            print(f"  ERRO: transcricao nao encontrada: {caminho}")
            return False
        transcricao = ler_transcricao(caminho)
        tem_audio = bool(cfg.get("audio_arquivo"))
    else:
        caminho = (base / cfg["audio_arquivo"]).resolve()
        if not caminho.exists():
            print(f"  ERRO: audio nao encontrado: {caminho}")
            return False
        transcricao = transcrever_audio(caminho)
        tem_audio = True
        # guarda a transcricao ao lado do audio: se o perfil precisar ser refeito,
        # nao paga STT de novo
        destino = caminho.with_suffix(".txt")
        destino.write_text(transcricao, encoding="utf-8")
        print(f"  transcricao salva: {destino}")

    palavras = len(transcricao.split())
    if palavras < MIN_PALAVRAS:
        print(f"  AVISO: transcricao com {palavras} palavras (< {MIN_PALAVRAS}). "
              "O perfil sai raso — o Claude nao tem de onde extrair.")
    print(f"  slug: {slug} | {palavras} palavras | nivel informado: {cfg['nivel']}")

    payload = montar_payload(cfg, transcricao, tem_audio)

    if dry_run:
        print("  [dry-run] payload valido, nada enviado.")
        return True

    resultado = gerar(payload)
    if not resultado or not resultado.get("perfil"):
        print("  FALHOU: perfil nao gerado.")
        return False

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    saida = OUT_DIR / f"{slug}.json"
    saida.write_text(json.dumps(resultado, ensure_ascii=False, indent=2), encoding="utf-8")

    linha = confirmar_no_supabase(slug)
    if not linha:
        print(f"  AVISO: perfil gerado e salvo em {saida.relative_to(REPO)}, "
              "mas NAO apareceu no Supabase. Confira o dashboard.")
        return False

    extraido = (resultado.get("dadosExtraidos") or {}).get("nivel", {}).get("valor", "?")
    print(f"  OK — no Supabase: {linha['nome']} | nivel {linha['nivel']} "
          f"(extraido: {extraido}) | {linha['num_aulas']} aulas | status {linha['status']}")
    print(f"  copia local: {saida.relative_to(REPO)}")
    print(f"  revisar: https://alumni-plano-gerador.vercel.app/perfil.html?id={slug}")
    return True


def main():
    ap = argparse.ArgumentParser(description="Gera Perfil 360 de aluno(s) novo(s) sem o formulario.")
    ap.add_argument("arquivos", nargs="*", type=Path, help="JSON(s) de aluno")
    ap.add_argument("--template", action="store_true", help="imprime um JSON modelo e sai")
    ap.add_argument("--dry-run", action="store_true", help="valida e mostra o que faria, sem chamar a API")
    args = ap.parse_args()

    if args.template:
        print(json.dumps(TEMPLATE, ensure_ascii=False, indent=2))
        return

    if not args.arquivos:
        ap.error("passe ao menos um JSON de aluno (ou --template)")

    ok = sum(processar(a, args.dry_run) for a in args.arquivos)
    total = len(args.arquivos)
    print(f"\n{ok}/{total} processado(s) com sucesso.")
    sys.exit(0 if ok == total else 1)


if __name__ == "__main__":
    main()
