#!/usr/bin/env python3
import io, sys
B = "/home/dan/dev/work/better/wt-juliana-a11/_build/juliana-aula11/"
PROF = "/home/dan/dev/work/better/wt-juliana-a11/public/professor/juliana-marques.html"

def rd(p):
    with io.open(p, encoding="utf-8") as f: return f.read()
def wr(p, s):
    with io.open(p, "w", encoding="utf-8") as f: f.write(s)

slides = rd(B+"slides.html")
accordion = rd(B+"accordion.html")
h = rd(PROF)
assert 'data-lesson="11"' not in h, "aula 11 already present!"

# 1) Insert IN CLASS slides before slides-container close
anchor_slides = '</div><!-- /slides-container -->'
assert h.count(anchor_slides) == 1, "slides-container anchor not unique"
h = h.replace(anchor_slides, slides + "\n" + anchor_slides, 1)

# 2) Insert Pre-class accordion after ex-lesson-10 close, inside tab-exercises
anchor_acc = '</div><!-- /lesson-card Aula 10 -->'
assert h.count(anchor_acc) == 1, "ex-lesson-10 anchor not unique"
h = h.replace(anchor_acc, anchor_acc + "\n" + accordion, 1)

# 3) lessonRanges: add 10 and 11 (10 was missing in origin/main)
old_ranges = 'var lessonRanges={1:{start:1,end:30},2:{start:31,end:60},3:{start:61,end:90},4:{start:91,end:120},5:{start:121,end:150},6:{start:151,end:180},7:{start:181,end:210},8:{start:211,end:240},9:{start:241,end:270}};var currentLesson=1;'
new_ranges = 'var lessonRanges={1:{start:1,end:30},2:{start:31,end:60},3:{start:61,end:90},4:{start:91,end:120},5:{start:121,end:150},6:{start:151,end:180},7:{start:181,end:210},8:{start:211,end:240},9:{start:241,end:270},10:{start:271,end:300},11:{start:301,end:330}};var currentLesson=1;'
assert h.count(old_ranges) == 1, "lessonRanges anchor not found"
h = h.replace(old_ranges, new_ranges, 1)

# 4) totalSlides
assert h.count('var currentSlide=1;var totalSlides=270;') == 1
h = h.replace('var currentSlide=1;var totalSlides=270;', 'var currentSlide=1;var totalSlides=330;', 1)

# 5) JS functions for lesson 11 after lesson 10 prevQc10 block
anchor_js = "function prevQc10(){var cards=document.querySelectorAll('#qcContainer10 .qc-card');if(qcCurrent10<=0)return;cards[qcCurrent10].style.display='none';qcCurrent10--;cards[qcCurrent10].style.display='block';document.getElementById('qcScore10').textContent=(qcCurrent10+1)+' / '+cards.length;document.getElementById('prevQcBtn10').style.display=qcCurrent10>0?'inline-flex':'none';document.getElementById('nextQcBtn10').style.display='inline-flex'}"
assert h.count(anchor_js) == 1, "lesson10 JS anchor not found"
js11 = (
    "\nfunction revealGrammar11(){var el=document.getElementById('grammarTable11');if(el)el.classList.add('show')}"
    "\nvar dialogueLine11=1;function nextDialogueLine11(){dialogueLine11++;var box=document.getElementById('dialogue11');if(!box)return;var line=box.querySelector('.dialogue-line[data-line=\"'+dialogueLine11+'\"]');if(line){line.classList.add('visible');if(dialogueLine11>=6){var btn=document.getElementById('nextLineBtn11');if(btn){btn.textContent='Di\\u00e1logo Completo';btn.disabled=true;btn.style.opacity='0.5'}}}}"
    "\nvar qcCurrent11=0;function initQc11(){var cards=document.querySelectorAll('#qcContainer11 .qc-card');if(cards.length>0)cards[0].style.display='block'}initQc11();function nextQc11(){var cards=document.querySelectorAll('#qcContainer11 .qc-card');if(qcCurrent11>=cards.length-1)return;cards[qcCurrent11].style.display='none';qcCurrent11++;cards[qcCurrent11].style.display='block';document.getElementById('qcScore11').textContent=(qcCurrent11+1)+' / '+cards.length;document.getElementById('prevQcBtn11').style.display=qcCurrent11>0?'inline-flex':'none';if(qcCurrent11>=cards.length-1)document.getElementById('nextQcBtn11').style.display='none'}function prevQc11(){var cards=document.querySelectorAll('#qcContainer11 .qc-card');if(qcCurrent11<=0)return;cards[qcCurrent11].style.display='none';qcCurrent11--;cards[qcCurrent11].style.display='block';document.getElementById('qcScore11').textContent=(qcCurrent11+1)+' / '+cards.length;document.getElementById('prevQcBtn11').style.display=qcCurrent11>0?'inline-flex':'none';document.getElementById('nextQcBtn11').style.display='inline-flex'}"
)
h = h.replace(anchor_js, anchor_js + js11, 1)

# 6) IN CLASS menu card after lesson 10 card
anchor_menu = '<div><div style="font-weight:600;font-size:.95rem">Personas y Lugares</div><div style="font-size:.8rem;color:var(--text-dim)">Describiendo Personas y Lugares: adjetivos y concordancia &mdash; 30 slides</div></div>\n    </div>\n  </div>'
assert h.count(anchor_menu) == 1, "menu card anchor not found"
menu11 = ('<div><div style="font-weight:600;font-size:.95rem">Personas y Lugares</div><div style="font-size:.8rem;color:var(--text-dim)">Describiendo Personas y Lugares: adjetivos y concordancia &mdash; 30 slides</div></div>\n    </div>\n'
    '    <div style="display:flex;align-items:center;gap:1rem;padding:1.2rem;background:rgba(255,255,255,.5);backdrop-filter:blur(8px);border:1px solid rgba(200,200,190,.5);border-radius:10px;cursor:pointer;transition:all .3s" onclick="enterSlideMode(301);" onmouseover="this.style.borderColor=\'var(--accent)\'" onmouseout="this.style.borderColor=\'rgba(200,200,190,.5)\'">\n'
    '      <div style="width:48px;height:48px;background:var(--accent);border-radius:8px;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:1.1rem">11</div>\n'
    '      <div><div style="font-weight:600;font-size:.95rem">La Ciudad y los Lugares P&uacute;blicos</div><div style="font-size:.8rem;color:var(--text-dim)">Lugares de la ciudad, HAY + estar + preposiciones de lugar &mdash; 30 slides</div></div>\n'
    '    </div>\n  </div>')
h = h.replace(anchor_menu, menu11, 1)

# 7) stamp11 after stamp10
anchor_stamp = '<div class="stamp" id="stamp10" data-label="Descripciones" style="background-image:url(\'https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=200&q=80\')"></div>'
assert h.count(anchor_stamp) == 1, "stamp10 anchor not found"
stamp11 = anchor_stamp + '\n        <div class="stamp" id="stamp11" data-label="La Ciudad" style="background-image:url(\'https://images.unsplash.com/photo-1502602898657-3e91760cbb34?w=200&q=80\')"></div>'
h = h.replace(anchor_stamp, stamp11, 1)

# 8) totalLessons 10 -> 11 (progress JS)
assert h.count('var totalLessons=10;') == 1
h = h.replace('var totalLessons=10;', 'var totalLessons=11;', 1)

wr(PROF, h)
print("PROF applied OK; data-lesson=11 count:", h.count('data-lesson="11"'))
print("ex-lesson-11:", h.count('id="ex-lesson-11"'), "stamp11:", h.count('id="stamp11"'), "menu enterSlideMode(301):", h.count('enterSlideMode(301)'))
