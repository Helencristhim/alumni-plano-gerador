#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""A SUPERFICIE DE AUDIO de uma aula da anatomia `consultivo`: o que precisa virar MP3.

POR QUE UM MODULO SO
--------------------
Duas coisas precisam da mesma resposta: o BUILDER, que injeta o `AUD_MAP` no HTML, e o
GERADOR, que chama a ElevenLabs. Se cada um descobrir a lista por conta propria, elas
divergem na primeira aula fora do padrao -- e a divergencia se manifesta como audio que
nao toca, que e justamente o defeito que nao aparece em gate nenhum.

    uma fonte, dois consumidores.

O QUE CONTA COMO SUPERFICIE (Anexo P-A §3)
-------------------------------------------
A CATEGORIA nao vem de um flag: vem da funcao que o HTML chama.

    say(texto, rate)              -> frase-modelo   -> Text to Speech
    sayAs(texto, rate, genero)    -> narracao       -> Text to Speech, voz por genero
    playTalk(rate, show, de, ate) -> dialogo        -> Text to Dialogue, UM arquivo

O `playTalk` sem `de`/`ate` e o dialogo inteiro; com eles, e um TRECHO -- e cada trecho e
uma unidade de escuta propria na aula, entao vira o seu proprio arquivo. E o que o anexo
chama de "um arquivo final por dialogo": a unidade e o dialogo que a aluna ouve de uma vez,
nao o objeto `TALKS`.

O `rate` NAO multiplica arquivo. "Normal" e "Slower" sao o MESMO audio com `playbackRate`
diferente -- gerar dois MP3s da mesma fala para mudar a velocidade dobraria o custo, o
tempo de QA e a chance de os dois divergirem na proxima edicao do texto.

NOME DE ARQUIVO = HASH DO TRANSCRIPT
-------------------------------------
O anexo §2 diz que "qualquer alteracao no transcript, modelo, Voice ID ou parametros
invalida a aprovacao correspondente". Se o nome do arquivo derivasse da posicao ("a2_fala3"),
editar o texto manteria o nome e o MP3 velho continuaria no ar, aprovado, dizendo outra
coisa. Derivando do hash do (texto + voz + modelo), texto novo = arquivo novo = aprovacao
nova, por construcao.
"""
import hashlib
import html
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import render  # noqa: E402  o mesmo emissor que o builder usa

MODELO = "eleven_v3"          # Anexo P-A §4: modelo de referencia vigente
EP_FALA = "text-to-speech"
EP_DIALOGO = "text-to-dialogue"


def _texto_de(bruto):
    """O texto como o JS o recebe: desescapado UMA vez.

    O HTML guarda `&quot;`/`&#39;` e o navegador desescapa ANTES de compilar o handler --
    entao a string que chega ao `say()` ja vem limpa. Gerar o MP3 a partir do texto ainda
    escapado produziria audio com "&#39;" falado e uma chave de AUD_MAP que nunca casa em
    runtime. E o mesmo erro que a REGRA 7.1 do imersivo documenta em 324 botoes mortos."""
    return html.unescape(bruto).strip()


def falas(html_txt):
    """As chamadas de fala unica: say(...) e sayAs(...).

    Devolve [(texto, genero_ou_None)] na ordem do documento, sem repetir."""
    fora, vistos = [], set()
    # sayAs primeiro: `say(` casa dentro de `sayAs(` e engoliria o genero.
    for m in re.finditer(r"sayAs\(\s*(&quot;|&#39;|['\"])(.*?)\1\s*,\s*[\d.]+\s*,\s*"
                         r"(&quot;|&#39;|['\"])([fm])\3", html_txt, re.S):
        t = _texto_de(m.group(2))
        if t and (t, m.group(4)) not in vistos:
            vistos.add((t, m.group(4)))
            fora.append((t, m.group(4)))
    for m in re.finditer(r"(?<!\w)say\(\s*(&quot;|&#39;|['\"])(.*?)\1", html_txt, re.S):
        t = _texto_de(m.group(2))
        if t and not any(t == x for x, _ in fora):
            fora.append((t, None))
    return fora


def dialogos(html_txt, turnos):
    """Os trechos de dialogo que o HTML de fato toca.

    Cada `playTalk(rate, show, de, ate)` distinto por (de, ate) e uma unidade de escuta.
    Sem `de`/`ate`, e o dialogo inteiro. O `rate` e ignorado de proposito -- ver o cabecalho.
    """
    if not turnos:
        return []
    faixas, vistas = [], set()
    for m in re.finditer(r"playTalk\(\s*[\d.]+\s*,\s*(?:true|false)\s*"
                         r"(?:,\s*(\d+)\s*,\s*(\d+)\s*)?\)", html_txt):
        a = int(m.group(1)) if m.group(1) is not None else 0
        b = int(m.group(2)) if m.group(2) is not None else len(turnos) - 1
        if (a, b) in vistas or a > b or b >= len(turnos):
            continue
        vistas.add((a, b))
        faixas.append((a, b))
    return sorted(faixas)


def _hash(payload):
    return hashlib.sha256(json.dumps(payload, ensure_ascii=False, sort_keys=True)
                          .encode("utf-8")).hexdigest()


def entradas_da_aula(n, frag_dir, vozes, voz_padrao):
    """As entradas de manifesto de UMA aula. `vozes` = {nome_do_personagem: voice_id}."""
    pasta = os.path.join(frag_dir, f"aula{n}")
    if not os.path.isdir(pasta):
        return []
    # O FRAGMENTO EXPANDIDO, nunca o cru.
    #
    # Desde que a atividade passou a ser DECLARADA, o `sayAs` de um exercicio migrado nao
    # esta mais no HTML do fragmento: esta no `blocos.json`. Varrendo o cru, a superficie
    # de audio fica CEGA para ele -- o MP3 nao e gerado, a chave nao entra no AUD_MAP, e o
    # botao toca silencio. Nada disso da erro.
    #
    # Medido: a primeira migracao de um exercicio com audio mudou o AUD_MAP do material, e
    # so a comparacao de bytes viu.
    decl = {}
    bj = os.path.join(pasta, "blocos.json")
    if os.path.exists(bj):
        decl = json.load(open(bj, encoding="utf-8"))
    # O MESMO vocabulario da aula que o builder usa. Sem ele, a expansao daqui classifica
    # o gap-fill de vocabulario como de gramatica e recusa o banco -- o build inteiro morre
    # num ponto que nao tem nada a ver com audio. Duas expansoes da mesma coisa tem de
    # receber o mesmo contexto, senao discordam.
    vocab_da_aula = set()
    for blocos_da_chave in decl.values():
        vocab_da_aula |= render.vocab_da_regiao(blocos_da_chave)

    corpo = ""
    for arq in ("slides.html", "preclass.html", "postclass.html"):
        p = os.path.join(pasta, arq)
        if os.path.exists(p):
            bruto = open(p, encoding="utf-8").read()
            corpo += re.sub(r"[ \t]*<!--\s*BLOCOS:([^>]+?)\s*-->",
                            lambda m: render.blocos(decl.get(m.group(1).strip(), []),
                                                    vocab_da_aula),
                            bruto)

    tj = os.path.join(pasta, "talk.json")
    turnos = json.load(open(tj, encoding="utf-8")) if os.path.exists(tj) else []

    fora = []
    for texto, genero in falas(corpo):
        voz = voz_padrao[genero] if genero else voz_padrao["neutra"]
        h = _hash({"t": texto, "v": voz, "m": MODELO})
        fora.append({
            "asset_id": f"l{n}-fala-{h[:12]}",
            "lesson_id": n,
            "uso": "narracao" if genero else "frase-modelo",
            "category": "narração ou monólogo" if genero else "frase-modelo/pronúncia",
            "transcript_version": 1,
            "transcript_hash": h,
            "transcript": texto,
            "model_id": MODELO,
            "endpoint": EP_FALA,
            "roles": [{"role": "voz única", "voice_id": voz}],
            "file": f"l{n}_fala_{h[:12]}.mp3",
            "chave": texto,          # como o AUD_MAP e consultado em runtime
        })

    for a, b in dialogos(corpo, turnos):
        trecho = turnos[a:b + 1]
        papeis = [{"role": vozes["nomes"][t["s"]], "voice_id": vozes["ids"][t["s"]]}
                  for t in trecho]
        h = _hash({"t": [(t["s"], t["t"]) for t in trecho], "v": [p["voice_id"] for p in papeis],
                   "m": MODELO})
        fora.append({
            "asset_id": f"l{n}-dialogo-{a}-{b}-{h[:12]}",
            "lesson_id": n,
            "uso": f"diálogo, turnos {a}–{b}",
            "category": "diálogo com múltiplas vozes",
            "transcript_version": 1,
            "transcript_hash": h,
            "inputs": [{"text": t["t"], "voice_id": vozes["ids"][t["s"]], "speaker": t["s"]}
                       for t in trecho],
            "model_id": MODELO,
            "endpoint": EP_DIALOGO,
            "roles": papeis,
            "file": f"l{n}_dialogo_{a}_{b}_{h[:12]}.mp3",
            "chave": f"#talk{n}:{a}:{b}",
        })
    return fora


def manifesto(cfg, frag_dir):
    """O manifesto completo do material, na forma do Anexo P-A §2.

    Os campos que so existem DEPOIS de gerar (duration, checksum, qa_status) nascem vazios e
    sao preenchidos pelo gerador. Nascerem declarados importa: campo ausente e campo que
    ninguem lembra de preencher."""
    vozes_cfg = cfg.get("voices") or {}
    cast = cfg.get("cast") or []
    ids, nomes = [], []
    for p in cast:
        nome = p.get("n", "")
        vid = vozes_cfg.get(nome)
        if not vid:
            raise SystemExit(
                f'config sem voz para o personagem {nome!r}. O Anexo P-A §4 exige Voice ID '
                f'por papel, e §7 proibe dois personagens distintos com a mesma voz -- '
                f'declare "voices": {{"{nome}": "<voice_id>"}} no config.')
        ids.append(vid)
        nomes.append(nome)
    if len(set(ids)) != len(ids):
        raise SystemExit("dois personagens do elenco com o MESMO Voice ID. O Anexo P-A §7 "
                         "so admite isso com decisao explicita registrada.")

    padrao = {"neutra": vozes_cfg.get("_neutra") or (ids[0] if ids else None),
              "f": vozes_cfg.get("_f"), "m": vozes_cfg.get("_m")}
    for k in ("_neutra", "_f", "_m"):
        if not (vozes_cfg.get(k) or (k == "_neutra" and padrao["neutra"])):
            raise SystemExit(f'config sem "{k}" em "voices": e a voz das falas avulsas '
                             f'(say/sayAs), que nao pertencem a personagem do elenco.')

    itens = []
    for n in cfg.get("aulas", []):
        itens.extend(entradas_da_aula(n, frag_dir, {"ids": ids, "nomes": nomes}, padrao))
    return itens
