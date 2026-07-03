#!/usr/bin/env python3
"""
audit_hubs_struct.py — auditoria estrutural de TODOS os hubs (aluno+professor),
cobrindo as 4 classes de defeito de layout encontradas:

  1. ORPHAN      — accordion Pre-class/In-class órfão (ex-lesson em depth < base):
                   vaza pra outras abas. Fix: _build/model/check_hub_orphans.py
  2. SLIDES_COMP — slides inline (data-slide) aninhados DENTRO do #tab-complementary
                   (deviam vir depois, fora das abas). Quebra slide-mode + vaza.
  3. DIV_IMBAL   — <div> != </div> no corpo (fora script/style): bloco malformado.
  4. MENU_MIX    — menu IN CLASS com formato MISTO (.inclass-lesson-card hero +
                   linha flex do modelo): cards de tamanhos diferentes.

Uso (de dentro de alumni-plano-gerador/, após git fetch):
    python3 ../audit_hubs_struct.py            # lê do origin/main
    python3 ../audit_hubs_struct.py --local    # lê do working tree
"""
import os
import re
import subprocess
import sys

O = re.compile(r'<div\b', re.I)
C = re.compile(r'</div>', re.I)


def read(path, local):
    if local:
        try:
            return open(path, encoding='utf-8').read()
        except FileNotFoundError:
            return ''
    return subprocess.run(["git", "show", f"origin/main:{path}"],
                          capture_output=True, text=True).stdout


COMP_HDR = re.compile(r'Materiais Complementares\s*(?:&mdash;|—|&#8212;|-)\s*Aula\s*(\d+)', re.I)


def analyze(txt):
    depth = 0
    sty = scr = False
    ex = []
    comp_open = False
    comp_d = None
    slides_in_comp = False
    tab_base = None          # profundidade logo após abrir a 1ª tab-content
    comp_hdrs = []           # (n_aula, depth) de cada cabeçalho "Materiais Complementares — Aula N"
    for l in txt.split('\n'):
        ls = l.lower()
        if '<style' in ls:
            sty = True
        if '<script' in ls:
            scr = True
        if not (sty or scr):
            depth += len(O.findall(l)) - len(C.findall(l))
        if '</style>' in ls:
            sty = False
        if '</script>' in ls:
            scr = False
        if tab_base is None and 'class="tab-content' in ls:
            tab_base = depth
        hm = COMP_HDR.search(l)
        if hm:
            comp_hdrs.append((int(hm.group(1)), depth))
        m = re.search(r'id="ex-lesson-(\d+)"', l)
        if m:
            ex.append((int(m.group(1)), depth))
        if 'id="tab-complementary"' in l and not comp_open:
            comp_open = True
            comp_d = depth
        elif comp_open and comp_d is not None and depth < comp_d:
            comp_open = False
        if re.search(r'data-slide="\d+"', l) and comp_open:
            slides_in_comp = True
    base = ex[0][1] if ex else None
    orphans = [n for n, d in ex if base is not None and d < base]
    imbalance = depth  # balanço só do corpo (script/style já pulados acima)
    # ESCAPE — conteúdo que vazou pra FORA das abas (depth < base da tab-content):
    # net pode fechar em 0 (fechamento errado se compensa) e o DIV_IMBAL não vê,
    # mas o bloco renderiza no topo do body, sempre visível. Pega Complementares
    # e ex-lessons cujo cabeçalho cai abaixo da profundidade-base das abas.
    escaped = []
    if tab_base is not None:
        escaped += [f"comp{n}" for n, d in comp_hdrs if d < tab_base]
        escaped += [f"ex{n}" for n, d in ex if d < tab_base]
    # menu misto: só na região do tab-inclass
    mix = False
    mi = txt.find('id="tab-inclass"')
    mc = txt.find('id="tab-complementary"', mi) if mi >= 0 else -1
    if mi >= 0 and mc >= 0:
        region = txt[mi:mc]
        hero = region.count('class="inclass-lesson-card"')
        flex = len(re.findall(r'display:flex;align-items:center;gap:1rem;padding:1\.2rem', region))
        mix = hero > 0 and flex > 0
    return orphans, slides_in_comp, imbalance, mix, escaped


def flags_for(txt):
    """Lista de flags de defeito estrutural/shell de um hub (vazio = limpo)."""
    orph, sic, imb, mix, escaped = analyze(txt)
    flags = []
    if orph:
        flags.append(f"ORPHAN{orph}")
    if escaped:
        flags.append(f"ESCAPE{escaped}")
    if sic:
        flags.append("SLIDES_COMP")
    if imb != 0:
        flags.append(f"DIV_IMBAL({imb:+d})")
    if mix:
        flags.append("MENU_MIX")
    # OLD_SHELL — hub fora do shell do modelo (geração pré-modelo): carrega
    # os componentes legados /components/exercises.js ou activity-tracker.js,
    # que nenhum hub do modelo usa. Fica visualmente diferente de todos.
    if '/components/exercises.js' in txt or '/components/activity-tracker.js' in txt:
        flags.append("OLD_SHELL")
    return flags


# Slugs lixo: hubs que NÃO devem bloquear o CI (não são alunos reais / depreciados).
# ATENÇÃO: o filtro é por slug EXATO (basename sem .html), NUNCA por substring —
# senão um lixo curto mascara um aluno real (ex.: 'maisa' escondia
# 'maisa-de-oliveira-santos', que passou a ser o slug canônico).
JUNK_SLUGS = ('daniela-feitozaV2', 'percival-jrV2', 'zilaudio',
              'elaine-test', 'eduarda-gabriel-new', 'helen-mendes-teste')


def is_hub_path(p):
    return bool(re.search(r'public/(aluno|professor)/[a-z0-9-]+\.html$', p) and '-aula' not in p)


def slug_of(p):
    return os.path.basename(p)[:-5] if p.endswith('.html') else os.path.basename(p)


def check_mode(paths):
    """GATE de CI: recebe arquivos (tocados num PR), checa só os que são HUB,
    sai 1 se algum tiver defeito. Lê do working tree."""
    hubs = [p for p in paths if is_hub_path(p)
            and slug_of(p) not in JUNK_SLUGS]
    if not hubs:
        print("audit_hubs_struct --check: nenhum hub real nos arquivos dados — OK")
        return 0
    bad = []
    for p in hubs:
        try:
            txt = open(p, encoding='utf-8').read()
        except FileNotFoundError:
            continue
        fl = flags_for(txt)
        status = '✅ LIMPO' if not fl else '⚠️  ' + ' · '.join(fl)
        print(f"  {p:<50} {status}")
        if fl:
            bad.append(p)
    if bad:
        print(f"\n❌ {len(bad)} hub(s) com defeito estrutural/shell — PR BLOQUEADO.")
        return 1
    print(f"\n✅ {len(hubs)} hub(s) tocado(s) — todos limpos.")
    return 0


def main():
    if '--check' in sys.argv:
        paths = [a for a in sys.argv[1:] if a != '--check']
        sys.exit(check_mode(paths))
    local = '--local' in sys.argv
    files = subprocess.run(["git", "ls-tree", "-r", "origin/main", "--name-only"],
                           capture_output=True, text=True).stdout.split('\n')
    hubs = [f for f in files if is_hub_path(f)]
    findings = []
    for h in hubs:
        txt = read(h, local)
        if not txt:
            continue
        flags = flags_for(txt)
        if flags:
            findings.append((h.replace('public/', ''), flags))
    src = 'working tree' if local else 'origin/main'
    print(f"=== Auditoria estrutural — {len(hubs)} hubs ({src}) ===")
    if not findings:
        print("✅ TUDO LIMPO — nenhum defeito estrutural.")
        return
    print(f"⚠️  {len(findings)} hub(s) com defeito:\n")
    for tag, flags in sorted(findings):
        print(f"   {tag:<45} {' · '.join(flags)}")


if __name__ == '__main__':
    main()
