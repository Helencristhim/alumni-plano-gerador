#!/usr/bin/env python3
import io
B = "/home/dan/dev/work/better/wt-jul-a20/_build/juliana-aula20/"
PROF = "/home/dan/dev/work/better/wt-jul-a20/public/professor/juliana-marques.html"

def rd(p):
    with io.open(p, encoding="utf-8") as f: return f.read()
def wr(p, s):
    with io.open(p, "w", encoding="utf-8") as f: f.write(s)

slides = rd(B+"slides.html")
accordion = rd(B+"accordion.html")
h = rd(PROF)
assert 'data-lesson="20"' not in h, "aula 20 already present!"

anchor_slides = '</div><!-- /slides-container -->'
assert h.count(anchor_slides) == 1
h = h.replace(anchor_slides, slides + "\n" + anchor_slides, 1)

anchor_acc = '</div><!-- /lesson-card Aula 19 -->'
assert h.count(anchor_acc) == 1
h = h.replace(anchor_acc, anchor_acc + "\n" + accordion, 1)

old_ranges = ',19:{start:541,end:570}};var currentLesson=1;'
new_ranges = ',19:{start:541,end:570},20:{start:571,end:600}};var currentLesson=1;'
assert h.count(old_ranges) == 1
h = h.replace(old_ranges, new_ranges, 1)

assert h.count('var currentSlide=1;var totalSlides=570;') == 1
h = h.replace('var currentSlide=1;var totalSlides=570;', 'var currentSlide=1;var totalSlides=600;', 1)

anchor_js = "function prevQc19(){var cards=document.querySelectorAll('#qcContainer19 .qc-card');if(qcCurrent19<=0)return;cards[qcCurrent19].style.display='none';qcCurrent19--;cards[qcCurrent19].style.display='block';document.getElementById('qcScore19').textContent=(qcCurrent19+1)+' / '+cards.length;document.getElementById('prevQcBtn19').style.display=qcCurrent19>0?'inline-flex':'none';document.getElementById('nextQcBtn19').style.display='inline-flex'}"
assert h.count(anchor_js) == 1, "lesson19 JS anchor not found"
js20 = (
    "\nfunction revealGrammar20(){var el=document.getElementById('grammarTable20');if(el)el.classList.add('show')}"
    "\nvar dialogueLine20=1;function nextDialogueLine20(){dialogueLine20++;var box=document.getElementById('dialogue20');if(!box)return;var line=box.querySelector('.dialogue-line[data-line=\"'+dialogueLine20+'\"]');if(line){line.classList.add('visible');if(dialogueLine20>=6){var btn=document.getElementById('nextLineBtn20');if(btn){btn.textContent='Di\\u00e1logo Completo';btn.disabled=true;btn.style.opacity='0.5'}}}}"
    "\nvar qcCurrent20=0;function initQc20(){var cards=document.querySelectorAll('#qcContainer20 .qc-card');if(cards.length>0)cards[0].style.display='block'}initQc20();function nextQc20(){var cards=document.querySelectorAll('#qcContainer20 .qc-card');if(qcCurrent20>=cards.length-1)return;cards[qcCurrent20].style.display='none';qcCurrent20++;cards[qcCurrent20].style.display='block';document.getElementById('qcScore20').textContent=(qcCurrent20+1)+' / '+cards.length;document.getElementById('prevQcBtn20').style.display=qcCurrent20>0?'inline-flex':'none';if(qcCurrent20>=cards.length-1)document.getElementById('nextQcBtn20').style.display='none'}function prevQc20(){var cards=document.querySelectorAll('#qcContainer20 .qc-card');if(qcCurrent20<=0)return;cards[qcCurrent20].style.display='none';qcCurrent20--;cards[qcCurrent20].style.display='block';document.getElementById('qcScore20').textContent=(qcCurrent20+1)+' / '+cards.length;document.getElementById('prevQcBtn20').style.display=qcCurrent20>0?'inline-flex':'none';document.getElementById('nextQcBtn20').style.display='inline-flex'}"
)
h = h.replace(anchor_js, anchor_js + js20, 1)

anchor_menu = ('<div><div style="font-weight:600;font-size:.95rem">Mis Planes de Futuro</div><div style="font-size:.8rem;color:var(--text-dim)">Hablar del futuro: voy a + infinitivo, metas y objetivos (pienso, quiero, espero) &mdash; 30 slides</div></div>\n    </div>\n  </div>')
assert h.count(anchor_menu) == 1, "menu card (l19) anchor not found"
menu20 = ('<div><div style="font-weight:600;font-size:.95rem">Mis Planes de Futuro</div><div style="font-size:.8rem;color:var(--text-dim)">Hablar del futuro: voy a + infinitivo, metas y objetivos (pienso, quiero, espero) &mdash; 30 slides</div></div>\n    </div>\n'
    '    <div style="display:flex;align-items:center;gap:1rem;padding:1.2rem;background:rgba(255,255,255,.5);backdrop-filter:blur(8px);border:1px solid rgba(200,200,190,.5);border-radius:10px;cursor:pointer;transition:all .3s" onclick="enterSlideMode(571);" onmouseover="this.style.borderColor=\'var(--accent)\'" onmouseout="this.style.borderColor=\'rgba(200,200,190,.5)\'">\n'
    '      <div style="width:48px;height:48px;background:var(--accent);border-radius:8px;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:1.1rem">20</div>\n'
    '      <div><div style="font-weight:600;font-size:.95rem">Revisi&oacute;n y Cierre &mdash; Checkpoint Final</div><div style="font-size:.8rem;color:var(--text-dim)">Repaso de todo el curso: pasado vs futuro, la ciudad, el restaurante y las compras en una historia &mdash; 30 slides</div></div>\n'
    '    </div>\n  </div>')
h = h.replace(anchor_menu, menu20, 1)

anchor_stamp = '<div class="stamp" id="stamp19" data-label="El Futuro" style="background-image:url(\'https://images.unsplash.com/photo-1483354483454-4cd359948304?w=200&q=80\')"></div>'
assert h.count(anchor_stamp) == 1
stamp20 = anchor_stamp + '\n        <div class="stamp" id="stamp20" data-label="&iexcl;Curso Completo!" style="background-image:url(\'https://images.unsplash.com/photo-1530021232320-687d8e3dba54?w=200&q=80\')"></div>'
h = h.replace(anchor_stamp, stamp20, 1)

assert h.count('var totalLessons=19;') == 1
h = h.replace('var totalLessons=19;', 'var totalLessons=20;', 1)

wr(PROF, h)
print("PROF applied OK; data-lesson=20 count:", h.count('data-lesson="20"'))
print("ex-lesson-20:", h.count('id="ex-lesson-20"'), "stamp20:", h.count('id="stamp20"'), "menu enterSlideMode(571):", h.count('enterSlideMode(571)'))
