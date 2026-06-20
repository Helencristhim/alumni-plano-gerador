#!/usr/bin/env python3
import io
B = "/home/dan/dev/work/better/wt-jul-a18/_build/juliana-aula18/"
PROF = "/home/dan/dev/work/better/wt-jul-a18/public/professor/juliana-marques.html"

def rd(p):
    with io.open(p, encoding="utf-8") as f: return f.read()
def wr(p, s):
    with io.open(p, "w", encoding="utf-8") as f: f.write(s)

slides = rd(B+"slides.html")
accordion = rd(B+"accordion.html")
h = rd(PROF)
assert 'data-lesson="18"' not in h, "aula 18 already present!"

anchor_slides = '</div><!-- /slides-container -->'
assert h.count(anchor_slides) == 1
h = h.replace(anchor_slides, slides + "\n" + anchor_slides, 1)

anchor_acc = '</div><!-- /lesson-card Aula 17 -->'
assert h.count(anchor_acc) == 1
h = h.replace(anchor_acc, anchor_acc + "\n" + accordion, 1)

old_ranges = ',17:{start:481,end:510}};var currentLesson=1;'
new_ranges = ',17:{start:481,end:510},18:{start:511,end:540}};var currentLesson=1;'
assert h.count(old_ranges) == 1
h = h.replace(old_ranges, new_ranges, 1)

assert h.count('var currentSlide=1;var totalSlides=510;') == 1
h = h.replace('var currentSlide=1;var totalSlides=510;', 'var currentSlide=1;var totalSlides=540;', 1)

anchor_js = "function prevQc17(){var cards=document.querySelectorAll('#qcContainer17 .qc-card');if(qcCurrent17<=0)return;cards[qcCurrent17].style.display='none';qcCurrent17--;cards[qcCurrent17].style.display='block';document.getElementById('qcScore17').textContent=(qcCurrent17+1)+' / '+cards.length;document.getElementById('prevQcBtn17').style.display=qcCurrent17>0?'inline-flex':'none';document.getElementById('nextQcBtn17').style.display='inline-flex'}"
assert h.count(anchor_js) == 1, "lesson17 JS anchor not found"
js18 = (
    "\nfunction revealGrammar18(){var el=document.getElementById('grammarTable18');if(el)el.classList.add('show')}"
    "\nvar dialogueLine18=1;function nextDialogueLine18(){dialogueLine18++;var box=document.getElementById('dialogue18');if(!box)return;var line=box.querySelector('.dialogue-line[data-line=\"'+dialogueLine18+'\"]');if(line){line.classList.add('visible');if(dialogueLine18>=6){var btn=document.getElementById('nextLineBtn18');if(btn){btn.textContent='Di\\u00e1logo Completo';btn.disabled=true;btn.style.opacity='0.5'}}}}"
    "\nvar qcCurrent18=0;function initQc18(){var cards=document.querySelectorAll('#qcContainer18 .qc-card');if(cards.length>0)cards[0].style.display='block'}initQc18();function nextQc18(){var cards=document.querySelectorAll('#qcContainer18 .qc-card');if(qcCurrent18>=cards.length-1)return;cards[qcCurrent18].style.display='none';qcCurrent18++;cards[qcCurrent18].style.display='block';document.getElementById('qcScore18').textContent=(qcCurrent18+1)+' / '+cards.length;document.getElementById('prevQcBtn18').style.display=qcCurrent18>0?'inline-flex':'none';if(qcCurrent18>=cards.length-1)document.getElementById('nextQcBtn18').style.display='none'}function prevQc18(){var cards=document.querySelectorAll('#qcContainer18 .qc-card');if(qcCurrent18<=0)return;cards[qcCurrent18].style.display='none';qcCurrent18--;cards[qcCurrent18].style.display='block';document.getElementById('qcScore18').textContent=(qcCurrent18+1)+' / '+cards.length;document.getElementById('prevQcBtn18').style.display=qcCurrent18>0?'inline-flex':'none';document.getElementById('nextQcBtn18').style.display='inline-flex'}"
)
h = h.replace(anchor_js, anchor_js + js18, 1)

anchor_menu = ('<div><div style="font-weight:600;font-size:.95rem">Hacer Planes e Invitaciones</div><div style="font-size:.8rem;color:var(--text-dim)">Invitar (&iquest;te apetece...?), quedar, aceptar y rechazar con cortes&iacute;a &mdash; 30 slides</div></div>\n    </div>\n  </div>')
assert h.count(anchor_menu) == 1, "menu card (l17) anchor not found"
menu18 = ('<div><div style="font-weight:600;font-size:.95rem">Hacer Planes e Invitaciones</div><div style="font-size:.8rem;color:var(--text-dim)">Invitar (&iquest;te apetece...?), quedar, aceptar y rechazar con cortes&iacute;a &mdash; 30 slides</div></div>\n    </div>\n'
    '    <div style="display:flex;align-items:center;gap:1rem;padding:1.2rem;background:rgba(255,255,255,.5);backdrop-filter:blur(8px);border:1px solid rgba(200,200,190,.5);border-radius:10px;cursor:pointer;transition:all .3s" onclick="enterSlideMode(511);" onmouseover="this.style.borderColor=\'var(--accent)\'" onmouseout="this.style.borderColor=\'rgba(200,200,190,.5)\'">\n'
    '      <div style="width:48px;height:48px;background:var(--accent);border-radius:8px;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:1.1rem">18</div>\n'
    '      <div><div style="font-weight:600;font-size:.95rem">Mi Fin de Semana: Hablar del Pasado</div><div style="font-size:.8rem;color:var(--text-dim)">El pret&eacute;rito: verbos regulares e irregulares (fui, com&iacute;, visit&eacute;), contar el fin de semana &mdash; 30 slides</div></div>\n'
    '    </div>\n  </div>')
h = h.replace(anchor_menu, menu18, 1)

anchor_stamp = '<div class="stamp" id="stamp17" data-label="Planes" style="background-image:url(\'https://images.unsplash.com/photo-1496024840928-4c417adf211d?w=200&q=80\')"></div>'
assert h.count(anchor_stamp) == 1
stamp18 = anchor_stamp + '\n        <div class="stamp" id="stamp18" data-label="El Pasado" style="background-image:url(\'https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=200&q=80\')"></div>'
h = h.replace(anchor_stamp, stamp18, 1)

assert h.count('var totalLessons=17;') == 1
h = h.replace('var totalLessons=17;', 'var totalLessons=18;', 1)

wr(PROF, h)
print("PROF applied OK; data-lesson=18 count:", h.count('data-lesson="18"'))
print("ex-lesson-18:", h.count('id="ex-lesson-18"'), "stamp18:", h.count('id="stamp18"'), "menu enterSlideMode(511):", h.count('enterSlideMode(511)'))
