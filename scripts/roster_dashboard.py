#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera um painel HTML do roster: aulas criadas, a partir de qual aula é modelo,
nível CEFR (working tree + Supabase, snapshot) + aulas FEITAS pelo aluno (Supabase ao vivo).

Versão CI: lê o WORKING TREE (o checkout do GitHub Action já é o main atual) via glob
em public/professor/*.html e public/aluno/*.html, sem depender de `git show origin/main:`
nem `git ls-tree` (necessários só no clone local defasado).

Uso: rode da raiz do repo -> python3 scripts/roster_dashboard.py
Saída: public/roster-status.html (caminho relativo no repo)."""
import os
import re
import json
import glob
import subprocess
import urllib.request

# Raiz do repo = pai da pasta scripts/ (independe do cwd)
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SB_URL = 'https://xxdggcopydghbmgqqebq.supabase.co'
SB_KEY = 'sb_publishable_RjekGapp8WtVbDx0J8etDg_hVq7na29'
TARGET = 20

JUNK = ('helen-mendes', 'maisa', 'zilaudio', 'elaine-test', 'elaine-v-a', 'elaine-v-b',
        'daniela-feitozaV2', 'percival-jrV2', 'eduarda-gabriel-new', 'luiz-bressane-backup',
        'helen-mendes-teste', 'vanessa-maluf')
# slugs depreciados (duplicata — o oficial é o -v2): esconder
DEPRECATED = ('daniela-feitoza', 'percival-jr')  # os SEM -v2
SPANISH = ('juliana-marques', 'daniel-bastos')


def read(rel_path):
    """Lê um arquivo do working tree (caminho relativo à raiz do repo). '' se faltar."""
    p = os.path.join(REPO_ROOT, rel_path)
    try:
        with open(p, 'r', encoding='utf-8') as f:
            return f.read()
    except (FileNotFoundError, IsADirectoryError):
        return ''


def is_junk(slug):
    if slug in SPANISH:
        return False
    for j in JUNK:
        if slug == j or slug.startswith(j):
            return True
    if 'listening' in slug or 'palestra' in slug or 'speech-training' in slug or slug.endswith('-teste'):
        return True
    return False


def list_relpaths(subdir):
    """Lista os .html de public/<subdir> como caminhos relativos à raiz do repo."""
    base = os.path.join(REPO_ROOT, 'public', subdir)
    out = []
    for p in glob.glob(os.path.join(base, '*.html')):
        out.append(os.path.relpath(p, REPO_ROOT).replace(os.sep, '/'))
    return out


def main():
    prof_files = list_relpaths('professor')

    # slugs com hub professor (sem '-aula')
    slugs = sorted(set(
        m.group(1) for f in prof_files
        if (m := re.match(r'public/professor/([a-z0-9-]+)\.html$', f)) and '-aula' not in f
    ))
    # standalones por slug (prof)
    standalones = {}
    for f in prof_files:
        m = re.match(r'public/professor/([a-z0-9-]+)-aula(\d+)\.html$', f)
        if m:
            standalones.setdefault(m.group(1), set()).add(int(m.group(2)))

    # níveis do Supabase
    niveis = {}
    try:
        req = urllib.request.Request(f"{SB_URL}/rest/v1/perfis?select=id,data",
                                     headers={'apikey': SB_KEY, 'Authorization': 'Bearer ' + SB_KEY})
        for r in json.load(urllib.request.urlopen(req, timeout=30)):
            d = (r.get('data') or {}).get('perfil', {}) or {}
            nv = (d.get('dadosExtraidos', {}) or {}).get('nivel', {}) or {}
            val = nv.get('valor') or ''
            # forma curta: primeiro token tipo A2 / B1+ / C1
            mm = re.match(r'\s*([ABC][0-2]\+?)', val or '')
            niveis[r['id']] = mm.group(1) if mm else (val[:6] if val else '?')
    except Exception as e:
        print('aviso: falha Supabase perfis:', e)

    rows = []
    for slug in slugs:
        if is_junk(slug) or slug in DEPRECATED:
            continue
        hub = read(f"public/aluno/{slug}.html") or read(f"public/professor/{slug}.html")
        st = sorted(standalones.get(slug, []))
        # CRIADAS = maior N de standalone (jeito do roster_status; ignora accordion
        # fantasma legado no hub, ex.: gabriela-pires ex-lesson 21-25). Sem standalone
        # (ex.: espanhol inline) cai no maior ex-lesson/stamp do hub.
        if st:
            criadas = st[-1]
        else:
            nums = [int(x) for x in re.findall(r'id="(?:ex-lesson|stamp)-?(\d+)"', hub)]
            criadas = max(nums) if nums else 0
        # modelo: menor aula cujo standalone tem id="phaseBar"
        model_from = None
        for n in st:
            if 'id="phaseBar"' in read(f"public/professor/{slug}-aula{n}.html"):
                model_from = n
                break
        rows.append({'slug': slug, 'nivel': niveis.get(slug, '?'),
                     'criadas': criadas, 'model_from': model_from,
                     'standalones': len(st), 'spanish': slug in SPANISH})

    rows.sort(key=lambda r: (r['criadas'], r['slug']))
    gen = subprocess.run(["git", "-C", REPO_ROOT, "rev-parse", "--short", "HEAD"],
                         capture_output=True, text=True).stdout.strip() or '?'
    html = TEMPLATE.replace('__ROWS__', json.dumps(rows, ensure_ascii=False)) \
                   .replace('__SBURL__', SB_URL).replace('__SBKEY__', SB_KEY) \
                   .replace('__TARGET__', str(TARGET)).replace('__GEN__', gen)
    out = os.path.join(REPO_ROOT, 'public', 'roster-status.html')
    with open(out, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"OK: {len(rows)} alunos -> {out}")
    print("'Feitas' busca o Supabase ao vivo a cada load/refresh.")


TEMPLATE = r"""<!DOCTYPE html><html lang=pt-BR><head><meta charset=UTF-8>
<meta name=viewport content="width=device-width,initial-scale=1">
<title>Roster — Status ao vivo</title>
<style>
body{font:14px/1.5 -apple-system,Inter,sans-serif;background:#0f1117;color:#e6e6e6;margin:0;padding:24px}
h1{font-size:1.4rem;margin:0 0 4px} .sub{color:#8b8b9b;font-size:.82rem;margin-bottom:16px}
table{border-collapse:collapse;width:100%;background:#171a23;border-radius:10px;overflow:hidden}
th,td{padding:9px 12px;text-align:left;border-bottom:1px solid #242838}
th{background:#1e2230;cursor:pointer;user-select:none;font-size:.78rem;text-transform:uppercase;letter-spacing:.5px;color:#9aa}
tr:hover td{background:#1c2030}
.bar{height:7px;background:#242838;border-radius:4px;overflow:hidden;min-width:90px;display:inline-block;vertical-align:middle}
.bar>i{display:block;height:100%;background:linear-gradient(90deg,#3b82f6,#22c55e)}
.feitas>i{background:linear-gradient(90deg,#f59e0b,#22c55e)}
.lvl{font-weight:700;padding:2px 7px;border-radius:5px;background:#2a2f40;font-size:.78rem}
.done20{color:#22c55e;font-weight:700}.warn{color:#f59e0b}
.tag{font-size:.68rem;background:#3a2a1a;color:#f59e0b;padding:1px 5px;border-radius:4px;margin-left:5px}
.es{background:#1a2a3a;color:#60a5fa}
button{background:#3b82f6;color:#fff;border:0;padding:7px 14px;border-radius:7px;cursor:pointer;font-weight:600}
small{color:#6b7280}
</style></head><body>
<h1>Roster — Status ao vivo</h1>
<div class=sub>Criadas/Modelo/Nível = snapshot do git (<code>__GEN__</code>) · <b>Feitas</b> = Supabase ao vivo · alvo <b>__TARGET__</b> aulas
&nbsp;<button onclick=load()>↻ Atualizar feitas</button> <span id=st></span></div>
<table id=t><thead><tr>
<th onclick=sortBy('slug')>Aluno</th>
<th onclick=sortBy('nivel')>Nível</th>
<th onclick=sortBy('criadas')>Criadas</th>
<th onclick=sortBy('model_from')>Modelo a partir de</th>
<th onclick=sortBy('feitas')>Feitas pelo aluno (ao vivo)</th>
<th onclick=sortBy('faltam')>Faltam p/ 20</th>
</tr></thead><tbody id=tb></tbody></table>
<script>
var ROWS=__ROWS__, TARGET=__TARGET__, SBURL="__SBURL__", SBKEY="__SBKEY__", sortKey='criadas', asc=true;
function pct(n,d){return d?Math.round(n/d*100):0}
function render(){
 var tb=document.getElementById('tb');tb.innerHTML='';
 ROWS.slice().sort(function(a,b){var x=a[sortKey],y=b[sortKey];x=x==null?-1:x;y=y==null?-1:y;return (x<y?-1:x>y?1:0)*(asc?1:-1)})
 .forEach(function(r){
  var feitas=r.feitas||0, faltam=Math.max(0,TARGET-r.criadas);
  var modtxt = r.model_from==null ? '<small>—</small>' : (r.model_from==1?'<span class=done20>tudo</span>':'aula '+r.model_from+'+');
  var tr=document.createElement('tr');
  tr.innerHTML='<td>'+r.slug+(r.spanish?' <span class="tag es">ES</span>':'')+'</td>'
   +'<td><span class=lvl>'+(r.nivel||'?')+'</span></td>'
   +'<td>'+(r.criadas>=20?'<span class=done20>'+r.criadas+'</span>':r.criadas)+' <span class=bar><i style="width:'+pct(r.criadas,TARGET)+'%"></i></span></td>'
   +'<td>'+modtxt+' <small>('+r.standalones+' standalones)</small></td>'
   +'<td>'+feitas+' / '+r.criadas+' <span class="bar feitas"><i style="width:'+pct(feitas,r.criadas||1)+'%"></i></span></td>'
   +'<td>'+(faltam==0?'<span class=done20>✓ 20</span>':'<span class=warn>'+faltam+'</span>')+'</td>';
  tb.appendChild(tr);
 });
}
function sortBy(k){asc=(sortKey==k)?!asc:true;sortKey=k;render()}
function load(){
 document.getElementById('st').textContent='carregando feitas…';
 fetch(SBURL+'/rest/v1/lesson_progress?select=student_slug,lesson_number,inclass_done&inclass_done=eq.true',
   {headers:{apikey:SBKEY,Authorization:'Bearer '+SBKEY}})
 .then(function(r){return r.json()}).then(function(d){
  var cnt={};d.forEach(function(x){cnt[x.student_slug]=(cnt[x.student_slug]||0)+1});
  ROWS.forEach(function(r){r.feitas=cnt[r.slug]||0});
  document.getElementById('st').textContent='✓ '+new Date().toLocaleTimeString();
  render();
 }).catch(function(e){document.getElementById('st').textContent='erro Supabase: '+e});
}
render();load();setInterval(load,60000);
</script></body></html>"""

if __name__ == '__main__':
    main()
