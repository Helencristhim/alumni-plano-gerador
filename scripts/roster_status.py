#!/usr/bin/env python3
"""
roster_status.py — conta o material REAL de cada aluno direto do git (origin/main),
em vez de depender do CONTROLE-roster-aulas.md (que é manual e desatualiza).

Fonte da verdade = arquivos public/professor/{slug}-aula{N}.html no origin/main.
A contagem de um aluno = maior N de aula (as aulas 1..N-k antigas ficam inline no hub;
as novas são standalone, então o maior número standalone = total de aulas criadas).

Uso:
    cd alumni-plano-gerador && git fetch origin
    python3 ../roster_status.py                 # tabela markdown
    python3 ../roster_status.py --html > out.html

Roda de dentro de qualquer worktree do repo alumni-plano-gerador.
"""
import re
import subprocess
import sys
from collections import defaultdict

TARGET = 20  # política 12/06/2026: todo aluno com material -> 20 aulas

# Alunos da fila da Helen (não mexer sem OK do Dan)
HELEN = {
    "marlene-landucci", "daniela-feitoza", "roberto-pires",
    "carlos-vinicius-vale-bassan", "percival-jr", "roberto-rezende",
    "luiz-bressane", "natalie-viegas", "maria-claudia-curimbaba",
}
# Não são alunos reais / lixo / fora
TRASH = {
    "elaine-test", "elaine-v-a", "elaine-v-b", "daniela-feitozaV2",
    "percival-jrV2", "eduarda-gabriel-new", "luiz-bressane-backup-a2",
    "maisa", "helen-mendes-teste", "zilaudio",
}
MODEL = {"helen-mendes"}            # aluna modelo (shell oficial)
SPANISH = {"daniel-bastos", "juliana-marques"}  # espanhol — caso à parte
SPECIAL_5 = {"patricia-ruffo"}      # programa fecha em 5 aulas
HOLD = {"fabiana-michelly-silva", "vanessa-maluf"}  # Helen mexendo — não gerar (memória)


def git_files():
    out = subprocess.run(
        ["git", "ls-tree", "-r", "origin/main", "--name-only"],
        capture_output=True, text=True, check=True,
    ).stdout
    return out.splitlines()


def count_lessons(files):
    pat = re.compile(r"^public/professor/([a-z0-9-]+)-aula(\d+)\.html$")
    mx = defaultdict(int)
    for f in files:
        m = pat.match(f)
        if m:
            slug, n = m.group(1), int(m.group(2))
            mx[slug] = max(mx[slug], n)
    return mx


def classify(slug):
    if slug in TRASH:
        return "lixo"
    if slug in HOLD:
        return "hold (Helen)"
    if slug in MODEL:
        return "modelo"
    if slug in SPANISH:
        return "espanhol (à parte)"
    if slug in SPECIAL_5:
        return "patricia (fecha em 5)"
    if slug in HELEN:
        return "HELEN"
    return "DAN"


def git_head_short():
    return subprocess.run(
        ["git", "rev-parse", "--short", "origin/main"],
        capture_output=True, text=True, check=True,
    ).stdout.strip()


PAGE_TMPL = """<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>Painel interno — material por aluno</title>
<style>
  body {{ font-family: -apple-system, Segoe UI, Roboto, sans-serif; background:#f4f5f7;
         color:#1a1a2e; margin:0; padding:24px; }}
  .wrap {{ max-width:920px; margin:0 auto; }}
  h1 {{ font-size:22px; margin:0 0 4px; }}
  .sub {{ color:#667; font-size:13px; margin-bottom:20px; }}
  h2 {{ font-size:15px; margin:26px 0 8px; color:#1B4965;
        border-bottom:2px solid #e3e6ea; padding-bottom:4px; }}
  table {{ width:100%; border-collapse:collapse; background:#fff; border-radius:8px;
          overflow:hidden; box-shadow:0 1px 3px rgba(0,0,0,.08); margin-bottom:10px; }}
  th,td {{ text-align:left; padding:8px 12px; font-size:14px; border-bottom:1px solid #eef0f2; }}
  th {{ background:#1B4965; color:#fff; font-weight:600; font-size:12px;
        text-transform:uppercase; letter-spacing:.03em; }}
  td.num {{ text-align:center; font-variant-numeric:tabular-nums; }}
  .bar {{ display:inline-block; height:8px; border-radius:4px; background:#16a34a; vertical-align:middle; }}
  .bartrack {{ display:inline-block; width:90px; height:8px; border-radius:4px;
              background:#e3e6ea; vertical-align:middle; margin-right:6px; }}
  tr:last-child td {{ border-bottom:none; }}
  .next {{ background:#fffbe6; }}
  .legend {{ font-size:12px; color:#667; margin-top:18px; line-height:1.6; }}
  code {{ background:#eef0f2; padding:1px 5px; border-radius:4px; }}
</style></head><body><div class="wrap">
<h1>Painel interno — quantas aulas cada aluno tem</h1>
<div class="sub">Gerado automaticamente de <code>origin/main @ {head}</code> · fonte = arquivos
no git (não tabela manual) · alvo padrão = 20 aulas · <strong>uso interno, não divulgar pros alunos</strong>.</div>
{sections}
<div class="legend">
<strong>Como atualizar:</strong> rode <code>python3 better/roster_status.py --page &lt;caminho&gt;</code>
(de dentro de <code>alumni-plano-gerador/</code>, após <code>git fetch origin</code>) e comite. A contagem
é o maior nº de aula em <code>public/professor/{{slug}}-aula*.html</code>.<br>
<strong>Responsável:</strong> DAN = eu gero · HELEN = fila dela (não mexo) · espanhol = caso à parte
(daniel-bastos, juliana-marques) · hold = Helen mexendo (fabiana, vanessa) · modelo = helen-mendes.
</div></div></body></html>
"""


def render_section(title, rows, mark_next=False):
    body = []
    for i, (owner, n, faltam, alvo, slug) in enumerate(rows):
        pct = int(100 * min(n, alvo) / alvo)
        cls = ' class="next"' if (mark_next and i == 0) else ""
        bar = (f'<span class="bartrack"><span class="bar" style="width:{int(90*pct/100)}px">'
               f'</span></span>{n}/{alvo}')
        body.append(f"<tr{cls}><td>{slug}</td><td class='num'>{bar}</td>"
                    f"<td class='num'>{faltam}</td></tr>")
    return (f"<h2>{title}</h2><table><tr><th>Aluno</th><th>Progresso</th>"
            f"<th>Faltam</th></tr>{''.join(body)}</table>")


def write_page(path, rows, head):
    groups = [
        ("👤 DAN — gerar (menor contagem primeiro = próximo alvo)",
         [r for r in rows if r[0] == "DAN"], True),
        ("🇪🇸 Espanhol — caso à parte",
         [r for r in rows if r[0].startswith("espanhol")], False),
        ("⏸️ Hold — Helen mexendo (não gerar)",
         [r for r in rows if r[0] == "hold (Helen)"], False),
        ("👩‍🏫 Helen — fila dela",
         [r for r in rows if r[0] == "HELEN"], False),
    ]
    secs = [render_section(t, rs, nx) for t, rs, nx in groups if rs]
    html = PAGE_TMPL.format(head=head, sections="\n".join(secs))
    with open(path, "w") as f:
        f.write(html)
    print(f"página escrita em {path} (origin/main @ {head}, {len(rows)} alunos)")


def main():
    files = git_files()
    mx = count_lessons(files)
    rows = []
    for slug, n in mx.items():
        owner = classify(slug)
        if owner == "lixo":
            continue
        alvo = 5 if owner.startswith("patricia") else TARGET
        faltam = max(0, alvo - n)
        rows.append((owner, n, faltam, alvo, slug))
    # ordena: DAN primeiro por menor contagem (alvo da próxima geração), depois o resto
    order = {"DAN": 0, "espanhol (à parte)": 1, "hold (Helen)": 2, "HELEN": 3,
             "patricia (fecha em 5)": 4, "modelo": 5}
    rows.sort(key=lambda r: (order.get(r[0], 9), r[1], r[4]))

    if "--page" in sys.argv:
        idx = sys.argv.index("--page")
        path = sys.argv[idx + 1]
        write_page(path, rows, git_head_short())
        return

    if "--html" in sys.argv:
        print("<table border=1 cellpadding=6><tr><th>Aluno</th><th>Aulas criadas</th>"
              "<th>Alvo</th><th>Faltam</th><th>Responsável</th></tr>")
        for owner, n, faltam, alvo, slug in rows:
            print(f"<tr><td>{slug}</td><td>{n}</td><td>{alvo}</td>"
                  f"<td>{faltam}</td><td>{owner}</td></tr>")
        print("</table>")
        return

    print(f"| Aluno | Criadas | Alvo | Faltam | Responsável |")
    print(f"|---|---|---|---|---|")
    for owner, n, faltam, alvo, slug in rows:
        print(f"| {slug} | {n} | {alvo} | {faltam} | {owner} |")
    dan = [r for r in rows if r[0] == "DAN"]
    tot = sum(r[2] for r in dan)
    print(f"\n_DAN: {len(dan)} alunos, {tot} aulas faltam pro alvo {TARGET}. "
          f"Próximo alvo automático = menor contagem (topo da lista DAN)._")


if __name__ == "__main__":
    main()
