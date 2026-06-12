#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""check_contrast.py — GATE de contraste COMPUTADO (chromium/chrome headless).

Renderiza a página, varre TODOS os slides (escuros E claros), computa a cor
efetiva de cada texto (subindo ancestrais + alpha blending) e falha se houver
texto ilegível (ratio < 2.5:1). É a prova final de que o contrast-guard +
o CSS do modelo seguram qualquer paleta.

Arquivo sem slides (data-slide) é pulado (exit 0).
USO: python3 _build/model/check_contrast.py arquivo.html [...]
"""
import json
import os
import re
import shutil
import subprocess
import sys

INJECT = """
<script>
window.addEventListener('load', function(){
  function lum(c){
    var m = c.match(/rgba?\\(([\\d.]+),\\s*([\\d.]+),\\s*([\\d.]+)(?:,\\s*([\\d.]+))?\\)/);
    if(!m) return null;
    var a = m[4]===undefined?1:parseFloat(m[4]);
    var ch=[m[1],m[2],m[3]].map(function(v){v=parseFloat(v)/255;
      return v<=0.03928? v/12.92 : Math.pow((v+0.055)/1.055,2.4);});
    return {l:0.2126*ch[0]+0.7152*ch[1]+0.0722*ch[2], a:a};
  }
  function effBg(el, fallback){
    var node=el;
    while(node && node.nodeType===1){
      var cs=getComputedStyle(node);
      var L=lum(cs.backgroundColor);
      if(L && L.a>0.5) return {l:L.l, css:cs.backgroundColor};
      // gradiente/foto: brilho não-computável — pular o elemento (guard cobre em runtime)
      if(cs.backgroundImage && cs.backgroundImage!=='none') return null;
      node=node.parentElement;
    }
    return {l:fallback, css:'assumed'};
  }
  function blend(fg, bgl){ return fg.a>=1? fg.l : fg.l*fg.a + bgl*(1-fg.a); }
  var out=[];
  var slides=document.querySelectorAll('.slide');
  slides.forEach(function(slide, si){
    var isLight = slide.classList.contains('slide-light');
    var fallback = isLight ? 0.93 : 0.05;  // claro assume página clara; resto assume escuro
    slide.querySelectorAll('*').forEach(function(el){
      if(['SCRIPT','STYLE','SVG','PATH','BUTTON'].indexOf(el.tagName)>=0) return;
      var hasText=false;
      el.childNodes.forEach(function(n){ if(n.nodeType===3 && n.textContent.trim()) hasText=true; });
      if(!hasText) return;
      var cs=getComputedStyle(el);
      var fg=lum(cs.color); if(!fg) return;
      var bg=effBg(el, fallback); if(!bg) return;
      var fl=blend(fg,bg.l);
      var ratio=(Math.max(fl,bg.l)+0.05)/(Math.min(fl,bg.l)+0.05);
      if(ratio<2.5){
        out.push({slide:si+1, light:isLight, tag:el.tagName, color:cs.color, bg:bg.css,
                  ratio:Math.round(ratio*100)/100, text:el.textContent.trim().slice(0,60)});
      }
    });
  });
  var pre=document.createElement('pre');
  pre.id='__contrast_audit__';
  pre.textContent=JSON.stringify({slides:slides.length, offenders:out});
  document.body.appendChild(pre);
});
</script>
"""


def find_browser():
    for b in ('chromium', 'chromium-browser', 'google-chrome', 'google-chrome-stable', 'chrome'):
        if shutil.which(b):
            return b
    print('ERRO: nenhum chromium/chrome no PATH')
    sys.exit(2)


def check(path, browser):
    html = open(path, encoding='utf-8').read()
    if 'data-slide=' not in html:
        print(f'{path}: sem slides — pulado')
        return 0
    pub = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(path)), '..'))
    html = re.sub(r'(src|href)="/(lib|styles|assets|audio)/', r'\1="file://' + pub + r'/\2/', html)
    html = html.replace('</body>', INJECT + '</body>', 1) if '</body>' in html else html + INJECT
    # snap chromium só acessa /home e NÃO lê diretórios ocultos (~/.*) — usar dir visível
    tmpdir = os.path.join(os.path.expanduser('~'), 'contrast-check-tmp')
    os.makedirs(tmpdir, exist_ok=True)
    tmp = os.path.join(tmpdir, os.path.basename(path))
    open(tmp, 'w', encoding='utf-8').write(html)
    r = subprocess.run([browser, '--headless', '--disable-gpu', '--no-sandbox',
                        '--virtual-time-budget=8000', '--dump-dom', 'file://' + tmp],
                       capture_output=True, text=True, timeout=120)
    m = re.search(r'<pre id="__contrast_audit__">(.*?)</pre>', r.stdout, re.S)
    os.remove(tmp)
    if not m:
        print(f'{path}: FALHA ao extrair resultado do headless')
        return 2
    data = json.loads(m.group(1))
    offs = data['offenders']
    print(f'{path}: {data["slides"]} slides, {len(offs)} textos ILEGÍVEIS (ratio<2.5)')
    seen = set()
    for o in offs[:25]:
        key = (o['slide'], o['color'], o['text'][:30])
        if key in seen:
            continue
        seen.add(key)
        kind = 'claro' if o['light'] else 'escuro'
        print(f'  slide {o["slide"]:>2} ({kind}) <{o["tag"].lower()}> ratio {o["ratio"]:>4} '
              f'color={o["color"]} bg={o["bg"]} :: {o["text"]!r}')
    if len(offs) > 25:
        print(f'  ... +{len(offs)-25}')
    return 1 if offs else 0


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    browser = find_browser()
    rc = 0
    for p in sys.argv[1:]:
        rc = max(rc, check(p, browser))
    sys.exit(rc)


if __name__ == '__main__':
    main()
