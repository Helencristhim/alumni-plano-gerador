#!/usr/bin/env python3
import io
B = "/home/dan/dev/work/better/wt-juliana-a12/_build/juliana-aula12/"
ALU = "/home/dan/dev/work/better/wt-juliana-a12/public/aluno/juliana-marques.html"

def rd(p):
    with io.open(p, encoding="utf-8") as f: return f.read()
def wr(p, s):
    with io.open(p, "w", encoding="utf-8") as f: f.write(s)

accordion = rd(B+"accordion.html")
h = rd(ALU)
assert 'id="ex-lesson-12"' not in h, "aula 12 already present in aluno!"

# accordion after ex-lesson-11 close
anchor_acc = '</div><!-- /lesson-card Aula 11 -->'
assert h.count(anchor_acc) == 1
h = h.replace(anchor_acc, anchor_acc + "\n" + accordion, 1)

# stamp12
anchor_stamp = '<div class="stamp" id="stamp11" data-label="La Ciudad" style="background-image:url(\'https://images.unsplash.com/photo-1502602898657-3e91760cbb34?w=200&q=80\')"></div>'
assert h.count(anchor_stamp) == 1
h = h.replace(anchor_stamp, anchor_stamp + '\n        <div class="stamp" id="stamp12" data-label="Direcciones" style="background-image:url(\'https://images.unsplash.com/photo-1473163928189-364b2c4e1135?w=200&q=80\')"></div>', 1)

# totalLessons
assert h.count('var totalLessons=11;') == 1
h = h.replace('var totalLessons=11;', 'var totalLessons=12;', 1)

wr(ALU, h)
print("ALUNO applied OK; ex-lesson-12:", h.count('id="ex-lesson-12"'), "stamp12:", h.count('id="stamp12"'))
