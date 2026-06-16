#!/usr/bin/env python3
"""
roster_status.py — conta o material REAL de cada aluno direto do git (origin/main)
e monta um painel com nível, idade, material criado e attendance (ao vivo).

Fonte da verdade:
  - material criado = arquivos public/professor/{slug}-aula{N}.html (maior N) no origin/main.
  - nome / idade / nível = perfil 360 dentro do hub public/professor/{slug}.html (best-effort).
  - attendance ("Aulas utilizadas") = planilha Google via /api/attendance (buscado no browser).

Uso (de dentro de alumni-plano-gerador/, após git fetch origin):
    python3 ../roster_status.py                 # tabela markdown
    python3 ../roster_status.py --page out.html # página HTML (com attendance ao vivo)
"""
import re
import subprocess
import sys
from collections import defaultdict

TARGET = 20  # política 12/06/2026: todo aluno com material -> 20 aulas

# 16/06/2026: Dan assumiu TODO o roster — não existe mais "fila da Helen".
HELEN = set()
HOLD = set()
TRASH = {
    "elaine-test", "elaine-v-a", "elaine-v-b", "daniela-feitozaV2",
    "percival-jrV2", "eduarda-gabriel-new", "luiz-bressane-backup-a2",
    "maisa", "helen-mendes-teste", "zilaudio",
}
MODEL = {"helen-mendes"}
SPANISH = {"daniel-bastos", "juliana-marques"}   # espanhol — caso à parte
SPECIAL_5 = {"patricia-ruffo"}                    # programa fecha em 5 aulas


def sh(args):
    return subprocess.run(args, capture_output=True, text=True).stdout


def git_files():
    return sh(["git", "ls-tree", "-r", "origin/main", "--name-only"]).splitlines()


def git_head_short():
    return sh(["git", "rev-parse", "--short", "origin/main"]).strip()


def count_lessons(files):
    pat = re.compile(r"^public/professor/([a-z0-9-]+)-aula(\d+)\.html$")
    mx = defaultdict(int)
    for f in files:
        m = pat.match(f)
        if m:
            mx[m.group(1)] = max(mx[m.group(1)], int(m.group(2)))
    return mx


def _clean(s):
    s = re.sub(r"&ccedil;", "ç", s); s = re.sub(r"&atilde;", "ã", s)
    s = re.sub(r"&eacute;", "é", s); s = re.sub(r"&iacute;", "í", s)
    s = re.sub(r"&aacute;", "á", s); s = re.sub(r"&ecirc;", "ê", s)
    s = re.sub(r"&[a-z]+;", "", s)
    return s.strip()


def profile_meta(slug):
    """Best-effort: extrai (nome, idade, nível) do hub. '' quando não acha."""
    html = sh(["git", "show", f"origin/main:public/professor/{slug}.html"])
    if not html:
        return "", "", ""
    name = ""
    m = re.search(r"Professor View\s*[—\-|]+\s*([^|<]+?)\s*\|", html)
    if m:
        name = _clean(m.group(1))
    if not name:
        m = re.search(r"Nome\s*</label>\s*<span[^>]*>([^<]+)", html, re.I)
        if m:
            name = _clean(m.group(1))
    idade = ""
    for pat in [r"Idade\s*</label>\s*<span[^>]*>\s*(\d{1,3})",
                r"IDADE\s*</div>\s*<div[^>]*>\s*(\d{1,3})",
                r"Idade[^0-9<]{0,12}(\d{1,3})\s*anos"]:
        m = re.search(pat, html, re.I)
        if m:
            idade = m.group(1); break
    nivel = ""
    for pat in [r"N[íi]vel\s*</label>\s*<span[^>]*>([^<]+)",
                r"N[ÍI]VEL\s*</div>\s*<div[^>]*>([^<]+)",
                r"N[íi]vel\s*[:<][^A-C]{0,12}\b(A1|A2|B1|B2|C1)\b[^<]{0,28}"]:
        m = re.search(pat, html, re.I)
        if m:
            nivel = _clean(m.group(1)); break
    if not nivel:  # último recurso: 1º token CEFR do documento
        m = re.search(r"\b(A1|A2|B1|B2|C1)\b", html)
        if m:
            nivel = m.group(1) + " (?)"
    return name, idade, nivel


def normname(s):
    s = s.lower()
    s = (s.replace("á", "a").replace("ã", "a").replace("â", "a")
          .replace("é", "e").replace("ê", "e").replace("í", "i")
          .replace("ó", "o").replace("õ", "o").replace("ô", "o")
          .replace("ú", "u").replace("ç", "c"))
    return re.sub(r"\s+", " ", s).strip()


def classify(slug):
    if slug in TRASH:  return "lixo"
    if slug in HOLD:   return "hold (Helen)"
    if slug in MODEL:  return "modelo"
    if slug in SPANISH: return "espanhol (à parte)"
    if slug in SPECIAL_5: return "patricia (fecha em 5)"
    if slug in HELEN:  return "HELEN"
    return "DAN"


def build_rows(with_meta=False):
    mx = count_lessons(git_files())
    rows = []
    for slug, n in mx.items():
        owner = classify(slug)
        if owner == "lixo":
            continue
        alvo = 5 if owner.startswith("patricia") else TARGET
        name = idade = nivel = ""
        if with_meta:
            name, idade, nivel = profile_meta(slug)
        rows.append({"slug": slug, "n": n, "alvo": alvo,
                     "faltam": max(0, alvo - n), "owner": owner,
                     "name": name or slug, "idade": idade, "nivel": nivel})
    order = {"DAN": 0, "espanhol (à parte)": 1, "hold (Helen)": 2, "HELEN": 3,
             "patricia (fecha em 5)": 4, "modelo": 5}
    rows.sort(key=lambda r: (order.get(r["owner"], 9), r["n"], r["slug"]))
    return rows


PAGE_TMPL = """<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>Painel interno — material por aluno</title>
<style>
  body {{ font-family:-apple-system,Segoe UI,Roboto,sans-serif; background:#f4f5f7; color:#1a1a2e; margin:0; padding:24px; }}
  .wrap {{ max-width:1040px; margin:0 auto; }}
  h1 {{ font-size:22px; margin:0 0 4px; }}
  .sub {{ color:#667; font-size:13px; margin-bottom:18px; }}
  h2 {{ font-size:15px; margin:24px 0 8px; color:#1B4965; border-bottom:2px solid #e3e6ea; padding-bottom:4px; }}
  table {{ width:100%; border-collapse:collapse; background:#fff; border-radius:8px; overflow:hidden; box-shadow:0 1px 3px rgba(0,0,0,.08); margin-bottom:10px; }}
  th,td {{ text-align:left; padding:8px 12px; font-size:14px; border-bottom:1px solid #eef0f2; }}
  th {{ background:#1B4965; color:#fff; font-weight:600; font-size:11px; text-transform:uppercase; letter-spacing:.03em; }}
  td.num {{ text-align:center; font-variant-numeric:tabular-nums; }}
  .bartrack {{ display:inline-block; width:80px; height:8px; border-radius:4px; background:#e3e6ea; vertical-align:middle; margin-right:6px; }}
  .bar {{ display:inline-block; height:8px; border-radius:4px; background:#16a34a; vertical-align:middle; }}
  .lvl {{ display:inline-block; padding:1px 7px; border-radius:10px; background:#e7eef5; color:#1B4965; font-size:12px; font-weight:600; }}
  tr:last-child td {{ border-bottom:none; }}
  .next {{ background:#fffbe6; }}
  .att {{ color:#0e6251; font-weight:600; }}
  .legend {{ font-size:12px; color:#667; margin-top:16px; line-height:1.6; }}
  code {{ background:#eef0f2; padding:1px 5px; border-radius:4px; }}
</style></head><body><div class="wrap">
<h1>Painel interno — material &amp; frequência por aluno</h1>
<div class="sub"><strong>Criadas</strong> = aulas com material pronto (git <code>origin/main @ {head}</code>) ·
<strong>Alvo</strong> = meta de aulas · nível/idade = perfil do hub ·
<strong>Aulas feitas</strong> = planilha "Aulas utilizadas" ao vivo via <code>/api/attendance</code> ·
<strong>uso interno, não divulgar pros alunos</strong>.</div>
{sections}
<div class="legend">
<strong>Atualizar criadas/nível/idade:</strong> <code>python3 scripts/roster_status.py --page public/painel-roster-interno.html</code> e comitar.
As "Aulas feitas" atualizam sozinhas (leem a planilha a cada carregamento).<br>
Onde nível/idade aparece em branco, o hub do aluno não expõe o campo num formato que o parser reconhece.
</div>
<script>
fetch('/api/attendance').then(function(r){{return r.json();}}).then(function(d){{
  if(!d || !d.ok || !d.byName) return;
  document.querySelectorAll('td[data-name]').forEach(function(td){{
    var k = td.getAttribute('data-name');
    var v = d.byName[k];
    td.textContent = (v===undefined||v==='') ? '—' : v;
  }});
}}).catch(function(){{}});
</script>
</div></body></html>
"""


def render_section(title, rows, mark_next=False):
    body = []
    for r in rows:
        pct = int(100 * min(r["n"], r["alvo"]) / r["alvo"])
        bar = (f'<span class="bartrack"><span class="bar" style="width:{int(80*pct/100)}px">'
               f'</span></span>{r["n"]}')
        lvl = f'<span class="lvl">{r["nivel"]}</span>' if r["nivel"] else "—"
        body.append(
            f"<tr><td>{r['name']}</td><td>{lvl}</td>"
            f"<td class='num'>{r['idade'] or '—'}</td>"
            f"<td class='num'>{bar}</td><td class='num'>{r['alvo']}</td>"
            f"<td class='num att' data-name='{normname(r['name'])}'>…</td></tr>")
    return (f"<h2>{title}</h2><table><tr><th>Aluno</th><th>Nível</th><th>Idade</th>"
            f"<th>Criadas</th><th>Alvo</th><th>Aulas feitas</th></tr>"
            f"{''.join(body)}</table>")


def write_page(path, rows, head):
    groups = [
        ("Alunos", [r for r in rows if r["owner"] == "DAN"], False),
        ("Espanhol", [r for r in rows if r["owner"].startswith("espanhol")], False),
        ("Programa de 5 aulas", [r for r in rows if r["owner"].startswith("patricia")], False),
    ]
    secs = [render_section(t, rs, nx) for t, rs, nx in groups if rs]
    with open(path, "w") as f:
        f.write(PAGE_TMPL.format(head=head, sections="\n".join(secs)))
    print(f"página escrita em {path} ({len(rows)} alunos, origin/main @ {head})")


def main():
    if "--page" in sys.argv:
        path = sys.argv[sys.argv.index("--page") + 1]
        write_page(path, build_rows(with_meta=True), git_head_short())
        return
    rows = build_rows(with_meta="--meta" in sys.argv)
    cols = "| Aluno | Criadas | Alvo | Faltam | Responsável |"
    print(cols + "\n|---|---|---|---|---|")
    for r in rows:
        print(f"| {r['slug']} | {r['n']} | {r['alvo']} | {r['faltam']} | {r['owner']} |")
    dan = [r for r in rows if r["owner"] == "DAN"]
    print(f"\n_DAN: {len(dan)} alunos, {sum(r['faltam'] for r in dan)} aulas faltam pro alvo {TARGET}._")


if __name__ == "__main__":
    main()
