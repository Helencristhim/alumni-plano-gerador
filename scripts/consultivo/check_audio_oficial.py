#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GATE 40 — o audio e ARQUIVO APROVADO, nunca sintese do navegador (AUT-004).

    "Na producao final, todo audio criado automaticamente para o material oficial e gerado
     pela API da ElevenLabs no pipeline seguro, antes da publicacao. O HTML final apenas
     reproduz arquivos aprovados. Web Speech API, speechSynthesis e SpeechSynthesisUtterance
     sao proibidos no build oficial."
                                              — Anexo P-A, Regra canonica

O DEFEITO QUE ELE EXISTE PARA IMPEDIR
--------------------------------------
Ate 25/08/2026 o molde publicado usava `speechSynthesis` em 17 pontos e NAO tinha uma unica
chamada a `new Audio`. Todo o audio da anatomia era sintese do navegador -- exatamente o que
o anexo proibe. E escolhia a voz por NOME COMERCIAL do sistema operacional (`Microsoft
Aria`, `Samantha`, `Google US English`), contra o §4: "os nomes comerciais de voz nao
substituem Voice IDs".

QUATRO PERGUNTAS, PORQUE SAO QUATRO FORMAS DE FALHAR
-----------------------------------------------------
 1. **A tecnologia proibida voltou?** Em CODIGO -- comentario que explica a proibicao nao e
    a proibicao ("a mencao nao e a expressao", P2 §15). Sem essa distincao o gate reprovaria
    a propria documentacao da troca, e a licao aprendida seria "apague o comentario".
 2. **Alguem escolhe voz por nome comercial?** A tabela do sistema saiu na derivacao; se
    voltar, o audio deixa de ser reproduzivel entre maquinas mesmo sem usar Web Speech.
 3. **Todo botao de audio acha o arquivo dele?** Chamada que nao resolve no `AUD_MAP` e um
    botao que nao faz nada -- e nao da erro em lugar nenhum. E o mesmo modo de falha dos
    324 botoes mortos do imersivo, so que silencioso desde o nascimento.
 4. **Todo arquivo prometido existe?** Mapa apontando para MP3 inexistente e a mesma coisa
    vista do outro lado. O `<audio>` dispara `error`, o player escreve o aviso, e ninguem
    fica sabendo.

O que ele NAO faz: julgar se o MP3 diz o texto certo. Isso e QA auditiva (o `qa_status` do
manifesto), e uma maquina que afirmasse isso estaria mentindo.

ESCOPO: o carimbo `alumni-anatomia=consultivo`. O artefato-prototipo nao e carimbado e
continua livre para usar sintese -- o §1 admite esse modo para prototipo, e e por isso que
a troca mora na DERIVACAO e nao no artefato.

USO:
    python3 scripts/consultivo/check_audio_oficial.py [arquivo.html ...]
    python3 scripts/consultivo/check_audio_oficial.py --selftest
"""
import glob
import html as _html
import json
import os
import re
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ANATOMIA = "consultivo"
VERDE, VERMELHO, ZERA = "\033[32m", "\033[31m", "\033[0m"

PROIBIDO = ["speechSynthesis", "SpeechSynthesisUtterance", "webkitSpeechRecognition"]
# nomes comerciais de voz do sistema (Anexo P-A §4)
NOMES_COMERCIAIS = ["Microsoft Aria", "Microsoft Jenny", "Microsoft Zira", "Microsoft Guy",
                    "Microsoft David", "Google US English", "Samantha", "Alex", "Daniel"]


def carimbo(c):
    m = re.search(r'<meta\s+name="alumni-anatomia"\s+content="([^"]+)"', c[:4000])
    return m.group(1) if m else None


def so_codigo(c):
    """O JS sem comentario. Comentario CITA a tecnologia proibida de proposito -- e onde a
    troca esta explicada."""
    return re.sub(r"/\*.*?\*/|//[^\n]*", " ", c, flags=re.S)


def mapa_de(c):
    m = re.search(r"var AUD_MAP=(\{.*?\});", c, re.S)
    if not m:
        return None
    try:
        return json.loads(m.group(1))
    except ValueError:
        return {}


def chamadas(c):
    """(rotulo, chave) de cada acionador de audio do documento.

    Le o HTML, nao o JS: o que interessa e o que um clique vai procurar. Por isso a busca e
    dentro de `onclick=`, e nao no arquivo inteiro -- a fonte do proprio `say()` contem a
    string `say(` e viraria um falso positivo (aconteceu comigo na primeira medicao)."""
    fora = []
    for m in re.finditer(r'on(?:click|change)="([^"]*)"', c):
        h = _html.unescape(m.group(1))
        for mm in re.finditer(r"(?<!\w)say\(\s*(['\"])(.*?)\1", h):
            fora.append(("say", mm.group(2).strip()))
        for mm in re.finditer(r"sayAs\(\s*(['\"])(.*?)\1", h):
            fora.append(("sayAs", mm.group(2).strip()))
    return fora


def confere(caminho):
    c = open(caminho, encoding="utf-8").read()
    if carimbo(c) != ANATOMIA:
        return False, []
    erros = []
    codigo = so_codigo(c)

    # 1 · a tecnologia proibida
    for t in PROIBIDO:
        n = len(re.findall(re.escape(t), codigo))
        if n:
            erros.append(f"AUDIO PROIBIDO (AUT-004): {t} aparece {n}x no CODIGO. O Anexo P-A "
                         f"proibe Web Speech no build oficial — o HTML final so reproduz "
                         f"arquivos aprovados.")

    # 2 · voz por nome comercial
    achados = [n for n in NOMES_COMERCIAIS if n in codigo]
    if achados:
        erros.append(f"VOZ POR NOME COMERCIAL (Anexo P-A §4): {achados}. Nome comercial de "
                     f"voz nao substitui Voice ID — a voz se decide na geracao, no pipeline.")

    mapa = mapa_de(c)
    ch = chamadas(c)
    if ch and mapa is None:
        erros.append(f"SEM var AUD_MAP e com {len(ch)} acionador(es) de audio: nenhum botao "
                     f"tem onde achar o arquivo dele.")
        return True, erros

    # 3 · todo acionador resolve
    if mapa is not None:
        sem = sorted({t for _, t in ch if t and t not in mapa})
        if sem:
            erros.append(f"{len(sem)} acionador(es) de audio SEM entrada no AUD_MAP — o "
                         f"clique nao faz nada e nao da erro. Ex.: \"{sem[0][:60]}\"")

        # 4 · todo arquivo prometido existe
        faltando = []
        for chave, e in mapa.items():
            src = e.get("src") if isinstance(e, dict) else e
            if not src:
                faltando.append(chave)
                continue
            if not os.path.exists(os.path.join(RAIZ, "public", src.lstrip("/"))):
                faltando.append(src)
        if faltando:
            erros.append(f"{len(faltando)} arquivo(s) do AUD_MAP nao existem no disco. "
                         f"Ex.: {faltando[0]}")
    return True, erros


def alvos_padrao():
    fora = []
    for p in sorted(glob.glob(os.path.join(RAIZ, "public", "professor", "*.html")) +
                    glob.glob(os.path.join(RAIZ, "public", "aluno", "*.html"))):
        try:
            with open(p, encoding="utf-8") as f:
                if carimbo(f.read(4000)) == ANATOMIA:
                    fora.append(p)
        except OSError:
            pass
    return fora


def _confere_texto(t):
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8") as f:
        f.write(t)
        p = f.name
    try:
        return confere(p)
    finally:
        os.unlink(p)


def _selftest():
    base = os.path.join(RAIZ, "public", "professor", "stephanie-vicente.html")
    if not os.path.exists(base):
        print("SELFTEST INCONCLUSIVO — o molde nao esta no lugar.")
        return 1
    limpo = open(base, encoding="utf-8").read()
    _, erros = _confere_texto(limpo)
    if erros:
        print("SELFTEST INCONCLUSIVO — o molde JA esta reprovando:")
        for e in erros:
            print("   ", e)
        return 1

    casos = [
        ("Web Speech de volta no codigo",
         lambda s: s.replace("function audParar()", "function audParar(){speechSynthesis.cancel();}\nfunction _x()", 1),
         "AUDIO PROIBIDO"),
        ("voz por nome comercial",
         lambda s: s.replace("var AUD_EL=null;", "var AUD_EL=null;var pref=['Microsoft Aria'];", 1),
         "NOME COMERCIAL"),
        ("acionador sem entrada no mapa",
         lambda s: s.replace("</body>",
                             '<button onclick="say(\'frase que ninguem gerou\',0.95)">P</button></body>', 1),
         "SEM entrada no AUD_MAP"),
        ("mapa apontando para MP3 inexistente",
         lambda s: re.sub(r'("src":\s*"/audio/[^"]*?)\.mp3"', r'\1-NAO-EXISTE.mp3"', s, count=1),
         "nao existem no disco"),
        ("a proibicao CITADA em comentario — nao pode reprovar",
         lambda s: s.replace("</body>", "<script>/* speechSynthesis e proibido aqui */</script></body>", 1),
         None),
    ]
    falhou = False
    for nome, muta, esperado in casos:
        _, errs = _confere_texto(muta(limpo))
        if esperado is None:
            bom = not errs
            motivo = "ignorado, como deve" if bom else f"REPROVOU indevidamente: {errs[0][:44]}"
        else:
            bom = any(esperado in e for e in errs)
            motivo = (errs[0][:60] if errs else "nao acusou nada")
        print(f"  {'OK  ' if bom else 'FALHA'}  {nome:52} {motivo}")
        if not bom:
            falhou = True
    print()
    if falhou:
        print("SELFTEST FALHOU — a regra parou de morder, ou passou a morder demais.")
        return 1
    print(f"SELFTEST OK — {len(casos)} casos: 4 defeitos pegos, 1 mencao legitima poupada.")
    return 0


def main():
    if "--selftest" in sys.argv:
        return _selftest()
    alvos = [a for a in sys.argv[1:] if a.endswith(".html")] or alvos_padrao()
    print(f"=== GATE 40 — audio oficial (Anexo P-A), anatomia {ANATOMIA} ===")
    total = vistos = 0
    for a in alvos:
        if not os.path.exists(a):
            continue
        aplicou, erros = confere(a)
        if not aplicou:
            continue
        vistos += 1
        rel = os.path.relpath(a, RAIZ)
        if erros:
            total += len(erros)
            print(f"{VERMELHO}FAIL{ZERA}  {rel}")
            for e in erros:
                print(f"        {e}")
        else:
            mapa = mapa_de(open(a, encoding="utf-8").read()) or {}
            print(f"{VERDE}ok{ZERA}    {rel}  ({len(mapa)} ativo(s) de audio)")
    print()
    if total:
        print(f"{VERMELHO}GATE 40 — {total} problema(s) em {vistos} arquivo(s).{ZERA}")
        return 1
    print(f"GATE 40 OK — {vistos} arquivo(s) reproduzem so arquivo aprovado.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
