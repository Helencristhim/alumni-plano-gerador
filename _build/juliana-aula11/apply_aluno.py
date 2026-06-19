#!/usr/bin/env python3
import io
B = "/home/dan/dev/work/better/wt-juliana-a11/_build/juliana-aula11/"
ALU = "/home/dan/dev/work/better/wt-juliana-a11/public/aluno/juliana-marques.html"

def rd(p):
    with io.open(p, encoding="utf-8") as f: return f.read()
def wr(p, s):
    with io.open(p, "w", encoding="utf-8") as f: f.write(s)

accordion = rd(B+"accordion.html")
h = rd(ALU)
assert 'id="ex-lesson-11"' not in h, "aula 11 already present in aluno!"

# accordion after ex-lesson-10 close
anchor_acc = '</div><!-- /lesson-card Aula 10 -->'
assert h.count(anchor_acc) == 1
h = h.replace(anchor_acc, anchor_acc + "\n" + accordion, 1)

# stamp11
anchor_stamp = '<div class="stamp" id="stamp10" data-label="Descripciones" style="background-image:url(\'https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=200&q=80\')"></div>'
assert h.count(anchor_stamp) == 1
h = h.replace(anchor_stamp, anchor_stamp + '\n        <div class="stamp" id="stamp11" data-label="La Ciudad" style="background-image:url(\'https://images.unsplash.com/photo-1502602898657-3e91760cbb34?w=200&q=80\')"></div>', 1)

# totalLessons
assert h.count('var totalLessons=10;') == 1
h = h.replace('var totalLessons=10;', 'var totalLessons=11;', 1)

wr(ALU, h)
print("ALUNO applied OK; ex-lesson-11:", h.count('id="ex-lesson-11"'), "stamp11:", h.count('id="stamp11"'))
