#!/usr/bin/env python3
import io, sys
B = "/home/dan/dev/work/better/wt-juliana-a12/_build/juliana-aula12/"
PROF = "/home/dan/dev/work/better/wt-juliana-a12/public/professor/juliana-marques.html"

def rd(p):
    with io.open(p, encoding="utf-8") as f: return f.read()
def wr(p, s):
    with io.open(p, "w", encoding="utf-8") as f: f.write(s)

slides = rd(B+"slides.html")
accordion = rd(B+"accordion.html")
h = rd(PROF)
assert 'data-lesson="12"' not in h, "aula 12 already present!"

# 1) Insert IN CLASS slides before slides-container close
anchor_slides = '</div><!-- /slides-container -->'
assert h.count(anchor_slides) == 1, "slides-container anchor not unique"
h = h.replace(anchor_slides, slides + "\n" + anchor_slides, 1)

# 2) Insert Pre-class accordion after ex-lesson-11 close, inside tab-exercises
anchor_acc = '</div><!-- /lesson-card Aula 11 -->'
assert h.count(anchor_acc) == 1, "ex-lesson-11 anchor not unique"
h = h.replace(anchor_acc, anchor_acc + "\n" + accordion, 1)

# 3) lessonRanges: add 12 (301-330 is 11; 331-360 is 12)
old_ranges = 'var lessonRanges={1:{start:1,end:30},2:{start:31,end:60},3:{start:61,end:90},4:{start:91,end:120},5:{start:121,end:150},6:{start:151,end:180},7:{start:181,end:210},8:{start:211,end:240},9:{start:241,end:270},10:{start:271,end:300},11:{start:301,end:330}};var currentLesson=1;'
new_ranges = 'var lessonRanges={1:{start:1,end:30},2:{start:31,end:60},3:{start:61,end:90},4:{start:91,end:120},5:{start:121,end:150},6:{start:151,end:180},7:{start:181,end:210},8:{start:211,end:240},9:{start:241,end:270},10:{start:271,end:300},11:{start:301,end:330},12:{start:331,end:360}};var currentLesson=1;'
assert h.count(old_ranges) == 1, "lessonRanges anchor not found"
h = h.replace(old_ranges, new_ranges, 1)

# 4) totalSlides 330 -> 360
assert h.count('var currentSlide=1;var totalSlides=330;') == 1
h = h.replace('var currentSlide=1;var totalSlides=330;', 'var currentSlide=1;var totalSlides=360;', 1)

# 5) JS functions for lesson 12 after lesson 11 prevQc11 block
anchor_js = "function prevQc11(){var cards=document.querySelectorAll('#qcContainer11 .qc-card');if(qcCurrent11<=0)return;cards[qcCurrent11].style.display='none';qcCurrent11--;cards[qcCurrent11].style.display='block';document.getElementById('qcScore11').textContent=(qcCurrent11+1)+' / '+cards.length;document.getElementById('prevQcBtn11').style.display=qcCurrent11>0?'inline-flex':'none';document.getElementById('nextQcBtn11').style.display='inline-flex'}"
assert h.count(anchor_js) == 1, "lesson11 JS anchor not found"
js12 = (
    "\nfunction revealGrammar12(){var el=document.getElementById('grammarTable12');if(el)el.classList.add('show')}"
    "\nvar dialogueLine12=1;function nextDialogueLine12(){dialogueLine12++;var box=document.getElementById('dialogue12');if(!box)return;var line=box.querySelector('.dialogue-line[data-line=\"'+dialogueLine12+'\"]');if(line){line.classList.add('visible');if(dialogueLine12>=6){var btn=document.getElementById('nextLineBtn12');if(btn){btn.textContent='Di\\u00e1logo Completo';btn.disabled=true;btn.style.opacity='0.5'}}}}"
    "\nvar qcCurrent12=0;function initQc12(){var cards=document.querySelectorAll('#qcContainer12 .qc-card');if(cards.length>0)cards[0].style.display='block'}initQc12();function nextQc12(){var cards=document.querySelectorAll('#qcContainer12 .qc-card');if(qcCurrent12>=cards.length-1)return;cards[qcCurrent12].style.display='none';qcCurrent12++;cards[qcCurrent12].style.display='block';document.getElementById('qcScore12').textContent=(qcCurrent12+1)+' / '+cards.length;document.getElementById('prevQcBtn12').style.display=qcCurrent12>0?'inline-flex':'none';if(qcCurrent12>=cards.length-1)document.getElementById('nextQcBtn12').style.display='none'}function prevQc12(){var cards=document.querySelectorAll('#qcContainer12 .qc-card');if(qcCurrent12<=0)return;cards[qcCurrent12].style.display='none';qcCurrent12--;cards[qcCurrent12].style.display='block';document.getElementById('qcScore12').textContent=(qcCurrent12+1)+' / '+cards.length;document.getElementById('prevQcBtn12').style.display=qcCurrent12>0?'inline-flex':'none';document.getElementById('nextQcBtn12').style.display='inline-flex'}"
)
h = h.replace(anchor_js, anchor_js + js12, 1)

# 6) IN CLASS menu card after lesson 11 card (insert before menu grid close)
anchor_menu = ('<div><div style="font-weight:600;font-size:.95rem">La Ciudad y los Lugares P&uacute;blicos</div><div style="font-size:.8rem;color:var(--text-dim)">Lugares de la ciudad, HAY + estar + preposiciones de lugar &mdash; 30 slides</div></div>\n    </div>\n  </div>')
assert h.count(anchor_menu) == 1, "menu card (l11) anchor not found"
menu12 = ('<div><div style="font-weight:600;font-size:.95rem">La Ciudad y los Lugares P&uacute;blicos</div><div style="font-size:.8rem;color:var(--text-dim)">Lugares de la ciudad, HAY + estar + preposiciones de lugar &mdash; 30 slides</div></div>\n    </div>\n'
    '    <div style="display:flex;align-items:center;gap:1rem;padding:1.2rem;background:rgba(255,255,255,.5);backdrop-filter:blur(8px);border:1px solid rgba(200,200,190,.5);border-radius:10px;cursor:pointer;transition:all .3s" onclick="enterSlideMode(331);" onmouseover="this.style.borderColor=\'var(--accent)\'" onmouseout="this.style.borderColor=\'rgba(200,200,190,.5)\'">\n'
    '      <div style="width:48px;height:48px;background:var(--accent);border-radius:8px;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:1.1rem">12</div>\n'
    '      <div><div style="font-weight:600;font-size:.95rem">C&oacute;mo Llegar: Pedir y Dar Direcciones</div><div style="font-size:.8rem;color:var(--text-dim)">Pedir/dar direcciones, imperativo informal (gira, sigue, cruza) &mdash; 30 slides</div></div>\n'
    '    </div>\n  </div>')
h = h.replace(anchor_menu, menu12, 1)

# 7) stamp12 after stamp11
anchor_stamp = '<div class="stamp" id="stamp11" data-label="La Ciudad" style="background-image:url(\'https://images.unsplash.com/photo-1502602898657-3e91760cbb34?w=200&q=80\')"></div>'
assert h.count(anchor_stamp) == 1, "stamp11 anchor not found"
stamp12 = anchor_stamp + '\n        <div class="stamp" id="stamp12" data-label="Direcciones" style="background-image:url(\'https://images.unsplash.com/photo-1473163928189-364b2c4e1135?w=200&q=80\')"></div>'
h = h.replace(anchor_stamp, stamp12, 1)

# 8) totalLessons 11 -> 12 (progress JS)
assert h.count('var totalLessons=11;') == 1
h = h.replace('var totalLessons=11;', 'var totalLessons=12;', 1)

wr(PROF, h)
print("PROF applied OK; data-lesson=12 count:", h.count('data-lesson="12"'))
print("ex-lesson-12:", h.count('id="ex-lesson-12"'), "stamp12:", h.count('id="stamp12"'), "menu enterSlideMode(331):", h.count('enterSlideMode(331)'))
