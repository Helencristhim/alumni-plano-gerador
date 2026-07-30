#!/usr/bin/env python3
"""
Verifica, NO NAVEGADOR, se o tracking de progresso (REGRA 28) realmente funciona
em cada material IN CLASS: o professor marca os 5 checks do "What I Learned" e o
`lesson-progress.js` grava `inclass_done` da AULA CERTA no Supabase.

Por que no navegador. Um grep so ve se o <script> esta no HTML. O defeito que
importa e de COMPORTAMENTO: o wrap de `toggleCheck` acontece antes da funcao
existir, o `.check-grid` nao tem como dizer de que aula e, o clique nao marca.
Nada disso aparece no texto do arquivo. Este harness clica de verdade.

NUNCA escreve no Supabase de producao. Toda requisicao a *.supabase.co e
ABORTADA e o client e um dublê que so registra a chamada. Rodar isto contra o
banco real acenderia aula de aluno real.

Uso:
    python3 scripts/check_lesson_tracking.py                    # roster inteiro
    python3 scripts/check_lesson_tracking.py public/professor/x-aula3.html ...
    python3 scripts/check_lesson_tracking.py --json out.json
"""

import argparse
import json
import os
import re
import subprocess
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PUBLIC = ROOT / "public"
PORT = 8899

# Dublê do supabase-js. Serve no lugar do bundle do CDN, antes de qualquer
# script da pagina rodar, e registra o que teria ido pra rede.
SUPABASE_STUB = """
window.__UPSERTS = [];
window.__SELECTS = [];
window.supabase = {
  createClient: function () {
    function table(name) {
      return {
        upsert: function (row, opts) {
          window.__UPSERTS.push({ table: name, row: row, opts: opts });
          return Promise.resolve({ data: [row], error: null });
        },
        insert: function (row) {
          window.__UPSERTS.push({ table: name, row: row });
          return Promise.resolve({ data: [row], error: null });
        },
        select: function () {
          window.__SELECTS.push(name);
          var q = {
            eq: function () { return q; },
            order: function () { return q; },
            limit: function () { return q; },
            then: function (cb) { return Promise.resolve(cb({ data: [], error: null })); },
            catch: function () { return q; }
          };
          return q;
        }
      };
    }
    return {
      from: table,
      storage: {
        from: function () {
          return {
            upload: function () { return Promise.resolve({ error: null }); },
            getPublicUrl: function () { return { data: { publicUrl: '' } }; }
          };
        }
      }
    };
  }
};
"""


def start_server():
    proc = subprocess.Popen(
        [sys.executable, "-m", "http.server", str(PORT), "--bind", "127.0.0.1"],
        cwd=str(PUBLIC),
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    for _ in range(60):
        try:
            import urllib.request

            urllib.request.urlopen(f"http://127.0.0.1:{PORT}/", timeout=1).read(1)
            return proc
        except Exception:
            time.sleep(0.2)
    proc.kill()
    raise RuntimeError("http.server nao subiu")


def expected_lesson(path: Path):
    """Numero da aula que o material DEVE gravar. None = hub multi-aula."""
    m = re.search(r"-aula(\d+)\.html$", path.name)
    return int(m.group(1)) if m else None


# Clica os checks do wrap-up e devolve o que o material fez.
# Dispara .click() nativo via JS: os slides ficam fora do fluxo visivel
# (slide-mode), e o click do Playwright exigiria visibilidade.
PROBE = """
() => {
  const out = {
    grids: 0, legacy: 0, items: 0, clicked: 0, checked: 0,
    toggleCheck: typeof window.toggleCheck === 'function',
    toggleChecklist: typeof window.toggleChecklist === 'function',
    wrapped: false, upserts: [], errors: []
  };
  try {
    // O container do checklist nao tem nome unico no roster (.check-grid,
    // .check-list, ou um <div> sem classe). Agrupa pelo container EFETIVO de cada
    // item, igual ao lesson-progress.js. Item DECORATIVO (sem onclick — lista de
    // objetivos, nao checklist) nao conta: nao e o wrap-up.
    const groups = new Map();
    for (const it of document.querySelectorAll('.check-item[onclick]')) {
      const box = it.closest('.check-grid, .check-list') || it.parentElement;
      if (!box) continue;
      if (!groups.has(box)) groups.set(box, []);
      groups.get(box).push(it);
    }
    const grids = Array.from(groups.keys()).filter(g => groups.get(g).length > 1);
    out.grids = grids.length;
    for (const grid of grids) {
      const items = groups.get(grid);
      out.items += items.length;
      for (const it of items) {
        if (!it.classList.contains('checked')) { it.click(); out.clicked++; }
      }
      out.checked += items.filter(it => it.classList.contains('checked')).length;
    }
    // <ul class="checklist"> do template legado
    if (!grids.length) {
      const lists = Array.from(document.querySelectorAll('.checklist'))
        .filter(l => l.querySelector('input[type=checkbox]'));
      out.legacy = lists.length;
      for (const list of lists) {
        const boxes = Array.from(list.querySelectorAll('input[type=checkbox]'));
        out.items += boxes.length;
        for (const b of boxes) {
          if (!b.checked) { b.checked = true; b.dispatchEvent(new Event('change', {bubbles:true})); out.clicked++; }
        }
        out.checked += list.querySelectorAll('input[type=checkbox]:checked').length;
      }
    }
  } catch (e) { out.errors.push(String(e)); }
  out.upserts = (window.__UPSERTS || []).filter(u => u.table === 'lesson_progress');
  return out;
}
"""


def check_one(browser, rel_url: str, path: Path, timeout_ms=25000):
    res = {"file": str(path.relative_to(ROOT)), "ok": False, "reason": None}
    expected = expected_lesson(path)
    res["expected_lesson"] = expected
    ctx = browser.new_context()
    try:
        ctx.add_init_script(SUPABASE_STUB)
        # nada sai para a rede: nem supabase (escrita real), nem CDN/fontes (lentidao)
        # ATENCAO: o filtro NAO pode casar por "supabase" na URL — /lib/supabase-config.js
        # e local e PRECISA rodar (e ele que cria o `sb` que o lesson-progress procura).
        # Só o bundle do CDN vira script vazio; o dublê ja foi instalado no init script.
        def _route(route):
            url = route.request.url
            if "jsdelivr" in url or "cdn." in url:
                return route.fulfill(status=200, content_type="application/javascript", body="")
            if any(h in url for h in ("supabase.co", "googleapis", "gstatic", "unsplash")):
                return route.abort()
            return route.continue_()

        ctx.route("**/*", _route)
        page = ctx.new_page()
        console = []
        page.on("console", lambda m: console.append(m.text))
        page.on("pageerror", lambda e: console.append("PAGEERROR: " + str(e)))
        page.goto(rel_url, wait_until="load", timeout=timeout_ms)
        page.wait_for_timeout(700)  # DOMContentLoaded + initProgress(100ms) + wraps
        probe = page.evaluate(PROBE)
        res.update(probe)
        res["console_warn"] = [c for c in console if "lesson-progress" in c or "PAGEERROR" in c][:8]

        if probe["items"] == 0:
            res["reason"] = "SEM CHECKLIST: nenhum .check-item nem .checklist no material"
        elif not probe["toggleCheck"] and not probe["toggleChecklist"]:
            res["reason"] = "SEM HANDLER: toggleCheck/toggleChecklist nao existem"
        elif probe["checked"] < probe["items"]:
            res["reason"] = f"CLIQUE NAO MARCA: {probe['checked']}/{probe['items']} ficaram .checked"
        elif not probe["upserts"]:
            res["reason"] = "NAO GRAVA: 5/5 marcados e nenhum upsert em lesson_progress"
        else:
            got = [u["row"].get("lesson_number") for u in probe["upserts"]]
            res["saved_lessons"] = got
            if expected is not None and expected not in got:
                res["reason"] = f"AULA ERRADA: marcou a aula {expected} e gravou {got}"
            elif not any(u["row"].get("inclass_done") for u in probe["upserts"]):
                res["reason"] = "inclass_done nao veio true"
            else:
                res["ok"] = True
    except Exception as e:
        res["reason"] = f"ERRO: {type(e).__name__}: {str(e)[:160]}"
    finally:
        try:
            ctx.close()
        except Exception:
            pass
    return res


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="*")
    ap.add_argument("--json", help="grava o relatorio completo")
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--limit", type=int)
    args = ap.parse_args()

    if args.files:
        targets = [Path(f).resolve() for f in args.files]
    else:
        targets = sorted((PUBLIC / "professor").glob("*-aula*.html"))
    if args.limit:
        targets = targets[: args.limit]

    print(f"tracking: {len(targets)} materiais, {args.workers} workers", flush=True)
    server = start_server()
    results = []
    lock = threading.Lock()
    try:
        from playwright.sync_api import sync_playwright

        local = threading.local()

        def worker(path):
            if not hasattr(local, "browser"):
                local.pw = sync_playwright().start()
                local.browser = local.pw.chromium.launch()
            url = f"http://127.0.0.1:{PORT}/professor/{path.name}"
            r = check_one(local.browser, url, path)
            with lock:
                results.append(r)
                n = len(results)
                if not r["ok"]:
                    print(f"  FAIL {r['file']}: {r['reason']}", flush=True)
                if n % 50 == 0:
                    print(f"  ... {n}/{len(targets)}", flush=True)
            return r

        with ThreadPoolExecutor(max_workers=args.workers) as ex:
            list(ex.map(worker, targets))
    finally:
        server.kill()

    bad = [r for r in results if not r["ok"]]
    print(f"\n{'='*60}\nOK: {len(results)-len(bad)}/{len(results)}   FALHAS: {len(bad)}")
    by_reason = {}
    for r in bad:
        key = (r["reason"] or "?").split(":")[0]
        by_reason.setdefault(key, []).append(r["file"])
    for k, v in sorted(by_reason.items(), key=lambda x: -len(x[1])):
        print(f"  {k}: {len(v)}")
        for f in v[:6]:
            print(f"      {f}")
        if len(v) > 6:
            print(f"      ... +{len(v)-6}")

    if args.json:
        Path(args.json).write_text(json.dumps(results, indent=1, ensure_ascii=False))
        print(f"\nrelatorio: {args.json}")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
