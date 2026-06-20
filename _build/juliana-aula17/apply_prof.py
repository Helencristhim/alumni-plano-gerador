#!/usr/bin/env python3
import io
B = "/home/dan/dev/work/better/wt-jul-a17/_build/juliana-aula17/"
PROF = "/home/dan/dev/work/better/wt-jul-a17/public/professor/juliana-marques.html"

def rd(p):
    with io.open(p, encoding="utf-8") as f: return f.read()
def wr(p, s):
    with io.open(p, "w", encoding="utf-8") as f: f.write(s)

slides = rd(B+"slides.html")
accordion = rd(B+"accordion.html")
h = rd(PROF)
assert 'data-lesson="17"' not in h, "aula 17 already present!"

anchor_slides = '</div><!-- /slides-container -->'
assert h.count(anchor_slides) == 1
h = h.replace(anchor_slides, slides + "\n" + anchor_slides, 1)

anchor_acc = '</div><!-- /lesson-card Aula 16 -->'
assert h.count(anchor_acc) == 1
h = h.replace(anchor_acc, anchor_acc + "\n" + accordion, 1)

old_ranges = ',16:{start:451,end:480}};var currentLesson=1;'
new_ranges = ',16:{start:451,end:480},17:{start:481,end:510}};var currentLesson=1;'
assert h.count(old_ranges) == 1
h = h.replace(old_ranges, new_ranges, 1)

assert h.count('var currentSlide=1;var totalSlides=480;') == 1
h = h.replace('var currentSlide=1;var totalSlides=480;', 'var currentSlide=1;var totalSlides=510;', 1)

anchor_js = "function prevQc16(){var cards=document.querySelectorAll('#qcContainer16 .qc-card');if(qcCurrent16<=0)return;cards[qcCurrent16].style.display='none';qcCurrent16--;cards[qcCurrent16].style.display='block';document.getElementById('qcScore16').textContent=(qcCurrent16+1)+' / '+cards.length;document.getElementById('prevQcBtn16').style.display=qcCurrent16>0?'inline-flex':'none';document.getElementById('nextQcBtn16').style.display='inline-flex'}"
assert h.count(anchor_js) == 1, "lesson16 JS anchor not found"
js17 = (
    "\nfunction revealGrammar17(){var el=document.getElementById('grammarTable17');if(el)el.classList.add('show')}"
    "\nvar dialogueLine17=1;function nextDialogueLine17(){dialogueLine17++;var box=document.getElementById('dialogue17');if(!box)return;var line=box.querySelector('.dialogue-line[data-line=\"'+dialogueLine17+'\"]');if(line){line.classList.add('visible');if(dialogueLine17>=6){var btn=document.getElementById('nextLineBtn17');if(btn){btn.textContent='Di\\u00e1logo Completo';btn.disabled=true;btn.style.opacity='0.5'}}}}"
    "\nvar qcCurrent17=0;function initQc17(){var cards=document.querySelectorAll('#qcContainer17 .qc-card');if(cards.length>0)cards[0].style.display='block'}initQc17();function nextQc17(){var cards=document.querySelectorAll('#qcContainer17 .qc-card');if(qcCurrent17>=cards.length-1)return;cards[qcCurrent17].style.display='none';qcCurrent17++;cards[qcCurrent17].style.display='block';document.getElementById('qcScore17').textContent=(qcCurrent17+1)+' / '+cards.length;document.getElementById('prevQcBtn17').style.display=qcCurrent17>0?'inline-flex':'none';if(qcCurrent17>=cards.length-1)document.getElementById('nextQcBtn17').style.display='none'}function prevQc17(){var cards=document.querySelectorAll('#qcContainer17 .qc-card');if(qcCurrent17<=0)return;cards[qcCurrent17].style.display='none';qcCurrent17--;cards[qcCurrent17].style.display='block';document.getElementById('qcScore17').textContent=(qcCurrent17+1)+' / '+cards.length;document.getElementById('prevQcBtn17').style.display=qcCurrent17>0?'inline-flex':'none';document.getElementById('nextQcBtn17').style.display='inline-flex'}"
)
h = h.replace(anchor_js, anchor_js + js17, 1)

anchor_menu = ('<div><div style="font-weight:600;font-size:.95rem">En la Farmacia: Salud y S&iacute;ntomas</div><div style="font-size:.8rem;color:var(--text-dim)">Hablar de salud: me duele/me duelen, pedir medicina, vocabulario de la farmacia &mdash; 30 slides</div></div>\n    </div>\n  </div>')
assert h.count(anchor_menu) == 1, "menu card (l16) anchor not found"
menu17 = ('<div><div style="font-weight:600;font-size:.95rem">En la Farmacia: Salud y S&iacute;ntomas</div><div style="font-size:.8rem;color:var(--text-dim)">Hablar de salud: me duele/me duelen, pedir medicina, vocabulario de la farmacia &mdash; 30 slides</div></div>\n    </div>\n'
    '    <div style="display:flex;align-items:center;gap:1rem;padding:1.2rem;background:rgba(255,255,255,.5);backdrop-filter:blur(8px);border:1px solid rgba(200,200,190,.5);border-radius:10px;cursor:pointer;transition:all .3s" onclick="enterSlideMode(481);" onmouseover="this.style.borderColor=\'var(--accent)\'" onmouseout="this.style.borderColor=\'rgba(200,200,190,.5)\'">\n'
    '      <div style="width:48px;height:48px;background:var(--accent);border-radius:8px;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:1.1rem">17</div>\n'
    '      <div><div style="font-weight:600;font-size:.95rem">Hacer Planes e Invitaciones</div><div style="font-size:.8rem;color:var(--text-dim)">Invitar (&iquest;te apetece...?), quedar, aceptar y rechazar con cortes&iacute;a &mdash; 30 slides</div></div>\n'
    '    </div>\n  </div>')
h = h.replace(anchor_menu, menu17, 1)

anchor_stamp = '<div class="stamp" id="stamp16" data-label="Salud" style="background-image:url(\'https://images.unsplash.com/photo-1576091160550-2173dba999ef?w=200&q=80\')"></div>'
assert h.count(anchor_stamp) == 1
stamp17 = anchor_stamp + '\n        <div class="stamp" id="stamp17" data-label="Planes" style="background-image:url(\'https://images.unsplash.com/photo-1496024840928-4c417adf211d?w=200&q=80\')"></div>'
h = h.replace(anchor_stamp, stamp17, 1)

assert h.count('var totalLessons=16;') == 1
h = h.replace('var totalLessons=16;', 'var totalLessons=17;', 1)

wr(PROF, h)
print("PROF applied OK; data-lesson=17 count:", h.count('data-lesson="17"'))
print("ex-lesson-17:", h.count('id="ex-lesson-17"'), "stamp17:", h.count('id="stamp17"'), "menu enterSlideMode(481):", h.count('enterSlideMode(481)'))
