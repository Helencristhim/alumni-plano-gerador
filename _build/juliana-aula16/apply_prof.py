#!/usr/bin/env python3
import io
B = "/home/dan/dev/work/better/wt-jul-a16/_build/juliana-aula16/"
PROF = "/home/dan/dev/work/better/wt-jul-a16/public/professor/juliana-marques.html"

def rd(p):
    with io.open(p, encoding="utf-8") as f: return f.read()
def wr(p, s):
    with io.open(p, "w", encoding="utf-8") as f: f.write(s)

slides = rd(B+"slides.html")
accordion = rd(B+"accordion.html")
h = rd(PROF)
assert 'data-lesson="16"' not in h, "aula 16 already present!"

anchor_slides = '</div><!-- /slides-container -->'
assert h.count(anchor_slides) == 1
h = h.replace(anchor_slides, slides + "\n" + anchor_slides, 1)

anchor_acc = '</div><!-- /lesson-card Aula 15 -->'
assert h.count(anchor_acc) == 1
h = h.replace(anchor_acc, anchor_acc + "\n" + accordion, 1)

old_ranges = ',15:{start:421,end:450}};var currentLesson=1;'
new_ranges = ',15:{start:421,end:450},16:{start:451,end:480}};var currentLesson=1;'
assert h.count(old_ranges) == 1
h = h.replace(old_ranges, new_ranges, 1)

assert h.count('var currentSlide=1;var totalSlides=450;') == 1
h = h.replace('var currentSlide=1;var totalSlides=450;', 'var currentSlide=1;var totalSlides=480;', 1)

anchor_js = "function prevQc15(){var cards=document.querySelectorAll('#qcContainer15 .qc-card');if(qcCurrent15<=0)return;cards[qcCurrent15].style.display='none';qcCurrent15--;cards[qcCurrent15].style.display='block';document.getElementById('qcScore15').textContent=(qcCurrent15+1)+' / '+cards.length;document.getElementById('prevQcBtn15').style.display=qcCurrent15>0?'inline-flex':'none';document.getElementById('nextQcBtn15').style.display='inline-flex'}"
assert h.count(anchor_js) == 1, "lesson15 JS anchor not found"
js16 = (
    "\nfunction revealGrammar16(){var el=document.getElementById('grammarTable16');if(el)el.classList.add('show')}"
    "\nvar dialogueLine16=1;function nextDialogueLine16(){dialogueLine16++;var box=document.getElementById('dialogue16');if(!box)return;var line=box.querySelector('.dialogue-line[data-line=\"'+dialogueLine16+'\"]');if(line){line.classList.add('visible');if(dialogueLine16>=6){var btn=document.getElementById('nextLineBtn16');if(btn){btn.textContent='Di\\u00e1logo Completo';btn.disabled=true;btn.style.opacity='0.5'}}}}"
    "\nvar qcCurrent16=0;function initQc16(){var cards=document.querySelectorAll('#qcContainer16 .qc-card');if(cards.length>0)cards[0].style.display='block'}initQc16();function nextQc16(){var cards=document.querySelectorAll('#qcContainer16 .qc-card');if(qcCurrent16>=cards.length-1)return;cards[qcCurrent16].style.display='none';qcCurrent16++;cards[qcCurrent16].style.display='block';document.getElementById('qcScore16').textContent=(qcCurrent16+1)+' / '+cards.length;document.getElementById('prevQcBtn16').style.display=qcCurrent16>0?'inline-flex':'none';if(qcCurrent16>=cards.length-1)document.getElementById('nextQcBtn16').style.display='none'}function prevQc16(){var cards=document.querySelectorAll('#qcContainer16 .qc-card');if(qcCurrent16<=0)return;cards[qcCurrent16].style.display='none';qcCurrent16--;cards[qcCurrent16].style.display='block';document.getElementById('qcScore16').textContent=(qcCurrent16+1)+' / '+cards.length;document.getElementById('prevQcBtn16').style.display=qcCurrent16>0?'inline-flex':'none';document.getElementById('nextQcBtn16').style.display='inline-flex'}"
)
h = h.replace(anchor_js, anchor_js + js16, 1)

anchor_menu = ('<div><div style="font-weight:600;font-size:.95rem">De Compras: En la Tienda de Ropa</div><div style="font-size:.8rem;color:var(--text-dim)">Comprar ropa: talla, precio (&iquest;cu&aacute;nto cuesta?), demostrativos este/esta, pagar &mdash; 30 slides</div></div>\n    </div>\n  </div>')
assert h.count(anchor_menu) == 1, "menu card (l15) anchor not found"
menu16 = ('<div><div style="font-weight:600;font-size:.95rem">De Compras: En la Tienda de Ropa</div><div style="font-size:.8rem;color:var(--text-dim)">Comprar ropa: talla, precio (&iquest;cu&aacute;nto cuesta?), demostrativos este/esta, pagar &mdash; 30 slides</div></div>\n    </div>\n'
    '    <div style="display:flex;align-items:center;gap:1rem;padding:1.2rem;background:rgba(255,255,255,.5);backdrop-filter:blur(8px);border:1px solid rgba(200,200,190,.5);border-radius:10px;cursor:pointer;transition:all .3s" onclick="enterSlideMode(451);" onmouseover="this.style.borderColor=\'var(--accent)\'" onmouseout="this.style.borderColor=\'rgba(200,200,190,.5)\'">\n'
    '      <div style="width:48px;height:48px;background:var(--accent);border-radius:8px;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:1.1rem">16</div>\n'
    '      <div><div style="font-weight:600;font-size:.95rem">En la Farmacia: Salud y S&iacute;ntomas</div><div style="font-size:.8rem;color:var(--text-dim)">Hablar de salud: me duele/me duelen, pedir medicina, vocabulario de la farmacia &mdash; 30 slides</div></div>\n'
    '    </div>\n  </div>')
h = h.replace(anchor_menu, menu16, 1)

anchor_stamp = '<div class="stamp" id="stamp15" data-label="De Compras" style="background-image:url(\'https://images.unsplash.com/photo-1441986300917-64674bd600d8?w=200&q=80\')"></div>'
assert h.count(anchor_stamp) == 1
stamp16 = anchor_stamp + '\n        <div class="stamp" id="stamp16" data-label="Salud" style="background-image:url(\'https://images.unsplash.com/photo-1576091160550-2173dba999ef?w=200&q=80\')"></div>'
h = h.replace(anchor_stamp, stamp16, 1)

assert h.count('var totalLessons=15;') == 1
h = h.replace('var totalLessons=15;', 'var totalLessons=16;', 1)

wr(PROF, h)
print("PROF applied OK; data-lesson=16 count:", h.count('data-lesson="16"'))
print("ex-lesson-16:", h.count('id="ex-lesson-16"'), "stamp16:", h.count('id="stamp16"'), "menu enterSlideMode(451):", h.count('enterSlideMode(451)'))
