#!/usr/bin/env python3
import io
B = "/home/dan/dev/work/better/wt-juliana-g-a14/_build/juliana-aula14/"
PROF = "/home/dan/dev/work/better/wt-juliana-g-a14/public/professor/juliana-marques.html"

def rd(p):
    with io.open(p, encoding="utf-8") as f: return f.read()
def wr(p, s):
    with io.open(p, "w", encoding="utf-8") as f: f.write(s)

slides = rd(B+"slides.html")
accordion = rd(B+"accordion.html")
h = rd(PROF)
assert 'data-lesson="14"' not in h, "aula 14 already present!"

anchor_slides = '</div><!-- /slides-container -->'
assert h.count(anchor_slides) == 1
h = h.replace(anchor_slides, slides + "\n" + anchor_slides, 1)

anchor_acc = '</div><!-- /lesson-card Aula 13 -->'
assert h.count(anchor_acc) == 1
h = h.replace(anchor_acc, anchor_acc + "\n" + accordion, 1)

old_ranges = ',13:{start:361,end:390}};var currentLesson=1;'
new_ranges = ',13:{start:361,end:390},14:{start:391,end:420}};var currentLesson=1;'
assert h.count(old_ranges) == 1
h = h.replace(old_ranges, new_ranges, 1)

assert h.count('var currentSlide=1;var totalSlides=390;') == 1
h = h.replace('var currentSlide=1;var totalSlides=390;', 'var currentSlide=1;var totalSlides=420;', 1)

anchor_js = "function prevQc13(){var cards=document.querySelectorAll('#qcContainer13 .qc-card');if(qcCurrent13<=0)return;cards[qcCurrent13].style.display='none';qcCurrent13--;cards[qcCurrent13].style.display='block';document.getElementById('qcScore13').textContent=(qcCurrent13+1)+' / '+cards.length;document.getElementById('prevQcBtn13').style.display=qcCurrent13>0?'inline-flex':'none';document.getElementById('nextQcBtn13').style.display='inline-flex'}"
assert h.count(anchor_js) == 1, "lesson13 JS anchor not found"
js14 = (
    "\nfunction revealGrammar14(){var el=document.getElementById('grammarTable14');if(el)el.classList.add('show')}"
    "\nvar dialogueLine14=1;function nextDialogueLine14(){dialogueLine14++;var box=document.getElementById('dialogue14');if(!box)return;var line=box.querySelector('.dialogue-line[data-line=\"'+dialogueLine14+'\"]');if(line){line.classList.add('visible');if(dialogueLine14>=6){var btn=document.getElementById('nextLineBtn14');if(btn){btn.textContent='Di\\u00e1logo Completo';btn.disabled=true;btn.style.opacity='0.5'}}}}"
    "\nvar qcCurrent14=0;function initQc14(){var cards=document.querySelectorAll('#qcContainer14 .qc-card');if(cards.length>0)cards[0].style.display='block'}initQc14();function nextQc14(){var cards=document.querySelectorAll('#qcContainer14 .qc-card');if(qcCurrent14>=cards.length-1)return;cards[qcCurrent14].style.display='none';qcCurrent14++;cards[qcCurrent14].style.display='block';document.getElementById('qcScore14').textContent=(qcCurrent14+1)+' / '+cards.length;document.getElementById('prevQcBtn14').style.display=qcCurrent14>0?'inline-flex':'none';if(qcCurrent14>=cards.length-1)document.getElementById('nextQcBtn14').style.display='none'}function prevQc14(){var cards=document.querySelectorAll('#qcContainer14 .qc-card');if(qcCurrent14<=0)return;cards[qcCurrent14].style.display='none';qcCurrent14--;cards[qcCurrent14].style.display='block';document.getElementById('qcScore14').textContent=(qcCurrent14+1)+' / '+cards.length;document.getElementById('prevQcBtn14').style.display=qcCurrent14>0?'inline-flex':'none';document.getElementById('nextQcBtn14').style.display='inline-flex'}"
)
h = h.replace(anchor_js, anchor_js + js14, 1)

anchor_menu = ('<div><div style="font-weight:600;font-size:.95rem">En el Transporte: Bus, Metro y Taxi</div><div style="font-size:.8rem;color:var(--text-dim)">Ir en + transporte, tener que + infinitivo, vocabulario del transporte &mdash; 30 slides</div></div>\n    </div>\n  </div>')
assert h.count(anchor_menu) == 1, "menu card (l13) anchor not found"
menu14 = ('<div><div style="font-weight:600;font-size:.95rem">En el Transporte: Bus, Metro y Taxi</div><div style="font-size:.8rem;color:var(--text-dim)">Ir en + transporte, tener que + infinitivo, vocabulario del transporte &mdash; 30 slides</div></div>\n    </div>\n'
    '    <div style="display:flex;align-items:center;gap:1rem;padding:1.2rem;background:rgba(255,255,255,.5);backdrop-filter:blur(8px);border:1px solid rgba(200,200,190,.5);border-radius:10px;cursor:pointer;transition:all .3s" onclick="enterSlideMode(391);" onmouseover="this.style.borderColor=\'var(--accent)\'" onmouseout="this.style.borderColor=\'rgba(200,200,190,.5)\'">\n'
    '      <div style="width:48px;height:48px;background:var(--accent);border-radius:8px;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:1.1rem">14</div>\n'
    '      <div><div style="font-weight:600;font-size:.95rem">En el Restaurante: Pedir la Comida y la Cuenta</div><div style="font-size:.8rem;color:var(--text-dim)">Pedir con cortes&iacute;a (quer&iacute;a, me gustar&iacute;a, para m&iacute;), vocabulario del restaurante &mdash; 30 slides</div></div>\n'
    '    </div>\n  </div>')
h = h.replace(anchor_menu, menu14, 1)

anchor_stamp = '<div class="stamp" id="stamp13" data-label="Transporte" style="background-image:url(\'https://images.unsplash.com/photo-1556122071-e404eaedb77f?w=200&q=80\')"></div>'
assert h.count(anchor_stamp) == 1
stamp14 = anchor_stamp + '\n        <div class="stamp" id="stamp14" data-label="Restaurante" style="background-image:url(\'https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=200&q=80\')"></div>'
h = h.replace(anchor_stamp, stamp14, 1)

assert h.count('var totalLessons=13;') == 1
h = h.replace('var totalLessons=13;', 'var totalLessons=14;', 1)

wr(PROF, h)
print("PROF applied OK; data-lesson=14 count:", h.count('data-lesson="14"'))
print("ex-lesson-14:", h.count('id="ex-lesson-14"'), "stamp14:", h.count('id="stamp14"'), "menu enterSlideMode(391):", h.count('enterSlideMode(391)'))
