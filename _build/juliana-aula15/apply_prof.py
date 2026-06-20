#!/usr/bin/env python3
import io
B = "/home/dan/dev/work/better/wt-jul-a15/_build/juliana-aula15/"
PROF = "/home/dan/dev/work/better/wt-jul-a15/public/professor/juliana-marques.html"

def rd(p):
    with io.open(p, encoding="utf-8") as f: return f.read()
def wr(p, s):
    with io.open(p, "w", encoding="utf-8") as f: f.write(s)

slides = rd(B+"slides.html")
accordion = rd(B+"accordion.html")
h = rd(PROF)
assert 'data-lesson="15"' not in h, "aula 15 already present!"

anchor_slides = '</div><!-- /slides-container -->'
assert h.count(anchor_slides) == 1
h = h.replace(anchor_slides, slides + "\n" + anchor_slides, 1)

anchor_acc = '</div><!-- /lesson-card Aula 14 -->'
assert h.count(anchor_acc) == 1
h = h.replace(anchor_acc, anchor_acc + "\n" + accordion, 1)

old_ranges = ',14:{start:391,end:420}};var currentLesson=1;'
new_ranges = ',14:{start:391,end:420},15:{start:421,end:450}};var currentLesson=1;'
assert h.count(old_ranges) == 1
h = h.replace(old_ranges, new_ranges, 1)

assert h.count('var currentSlide=1;var totalSlides=420;') == 1
h = h.replace('var currentSlide=1;var totalSlides=420;', 'var currentSlide=1;var totalSlides=450;', 1)

anchor_js = "function prevQc14(){var cards=document.querySelectorAll('#qcContainer14 .qc-card');if(qcCurrent14<=0)return;cards[qcCurrent14].style.display='none';qcCurrent14--;cards[qcCurrent14].style.display='block';document.getElementById('qcScore14').textContent=(qcCurrent14+1)+' / '+cards.length;document.getElementById('prevQcBtn14').style.display=qcCurrent14>0?'inline-flex':'none';document.getElementById('nextQcBtn14').style.display='inline-flex'}"
assert h.count(anchor_js) == 1, "lesson14 JS anchor not found"
js15 = (
    "\nfunction revealGrammar15(){var el=document.getElementById('grammarTable15');if(el)el.classList.add('show')}"
    "\nvar dialogueLine15=1;function nextDialogueLine15(){dialogueLine15++;var box=document.getElementById('dialogue15');if(!box)return;var line=box.querySelector('.dialogue-line[data-line=\"'+dialogueLine15+'\"]');if(line){line.classList.add('visible');if(dialogueLine15>=6){var btn=document.getElementById('nextLineBtn15');if(btn){btn.textContent='Di\\u00e1logo Completo';btn.disabled=true;btn.style.opacity='0.5'}}}}"
    "\nvar qcCurrent15=0;function initQc15(){var cards=document.querySelectorAll('#qcContainer15 .qc-card');if(cards.length>0)cards[0].style.display='block'}initQc15();function nextQc15(){var cards=document.querySelectorAll('#qcContainer15 .qc-card');if(qcCurrent15>=cards.length-1)return;cards[qcCurrent15].style.display='none';qcCurrent15++;cards[qcCurrent15].style.display='block';document.getElementById('qcScore15').textContent=(qcCurrent15+1)+' / '+cards.length;document.getElementById('prevQcBtn15').style.display=qcCurrent15>0?'inline-flex':'none';if(qcCurrent15>=cards.length-1)document.getElementById('nextQcBtn15').style.display='none'}function prevQc15(){var cards=document.querySelectorAll('#qcContainer15 .qc-card');if(qcCurrent15<=0)return;cards[qcCurrent15].style.display='none';qcCurrent15--;cards[qcCurrent15].style.display='block';document.getElementById('qcScore15').textContent=(qcCurrent15+1)+' / '+cards.length;document.getElementById('prevQcBtn15').style.display=qcCurrent15>0?'inline-flex':'none';document.getElementById('nextQcBtn15').style.display='inline-flex'}"
)
h = h.replace(anchor_js, anchor_js + js15, 1)

anchor_menu = ('<div><div style="font-weight:600;font-size:.95rem">En el Restaurante: Pedir la Comida y la Cuenta</div><div style="font-size:.8rem;color:var(--text-dim)">Pedir con cortes&iacute;a (quer&iacute;a, me gustar&iacute;a, para m&iacute;), vocabulario del restaurante &mdash; 30 slides</div></div>\n    </div>\n  </div>')
assert h.count(anchor_menu) == 1, "menu card (l14) anchor not found"
menu15 = ('<div><div style="font-weight:600;font-size:.95rem">En el Restaurante: Pedir la Comida y la Cuenta</div><div style="font-size:.8rem;color:var(--text-dim)">Pedir con cortes&iacute;a (quer&iacute;a, me gustar&iacute;a, para m&iacute;), vocabulario del restaurante &mdash; 30 slides</div></div>\n    </div>\n'
    '    <div style="display:flex;align-items:center;gap:1rem;padding:1.2rem;background:rgba(255,255,255,.5);backdrop-filter:blur(8px);border:1px solid rgba(200,200,190,.5);border-radius:10px;cursor:pointer;transition:all .3s" onclick="enterSlideMode(421);" onmouseover="this.style.borderColor=\'var(--accent)\'" onmouseout="this.style.borderColor=\'rgba(200,200,190,.5)\'">\n'
    '      <div style="width:48px;height:48px;background:var(--accent);border-radius:8px;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:1.1rem">15</div>\n'
    '      <div><div style="font-weight:600;font-size:.95rem">De Compras: En la Tienda de Ropa</div><div style="font-size:.8rem;color:var(--text-dim)">Comprar ropa: talla, precio (&iquest;cu&aacute;nto cuesta?), demostrativos este/esta, pagar &mdash; 30 slides</div></div>\n'
    '    </div>\n  </div>')
h = h.replace(anchor_menu, menu15, 1)

anchor_stamp = '<div class="stamp" id="stamp14" data-label="Restaurante" style="background-image:url(\'https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=200&q=80\')"></div>'
assert h.count(anchor_stamp) == 1
stamp15 = anchor_stamp + '\n        <div class="stamp" id="stamp15" data-label="De Compras" style="background-image:url(\'https://images.unsplash.com/photo-1441986300917-64674bd600d8?w=200&q=80\')"></div>'
h = h.replace(anchor_stamp, stamp15, 1)

assert h.count('var totalLessons=14;') == 1
h = h.replace('var totalLessons=14;', 'var totalLessons=15;', 1)

wr(PROF, h)
print("PROF applied OK; data-lesson=15 count:", h.count('data-lesson="15"'))
print("ex-lesson-15:", h.count('id="ex-lesson-15"'), "stamp15:", h.count('id="stamp15"'), "menu enterSlideMode(421):", h.count('enterSlideMode(421)'))
