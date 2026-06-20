#!/usr/bin/env python3
import io
B = "/home/dan/dev/work/better/wt-juliana-g-a13/_build/juliana-aula13/"
ALU = "/home/dan/dev/work/better/wt-juliana-g-a13/public/aluno/juliana-marques.html"

def rd(p):
    with io.open(p, encoding="utf-8") as f: return f.read()
def wr(p, s):
    with io.open(p, "w", encoding="utf-8") as f: f.write(s)

accordion = rd(B+"accordion.html")
h = rd(ALU)
assert 'id="ex-lesson-13"' not in h, "aula 13 already present in aluno!"

# accordion after ex-lesson-12 close
anchor_acc = '</div><!-- /lesson-card Aula 12 -->'
assert h.count(anchor_acc) == 1
h = h.replace(anchor_acc, anchor_acc + "\n" + accordion, 1)

# stamp13
anchor_stamp = '<div class="stamp" id="stamp12" data-label="Direcciones" style="background-image:url(\'https://images.unsplash.com/photo-1473163928189-364b2c4e1135?w=200&q=80\')"></div>'
assert h.count(anchor_stamp) == 1
h = h.replace(anchor_stamp, anchor_stamp + '\n        <div class="stamp" id="stamp13" data-label="Transporte" style="background-image:url(\'https://images.unsplash.com/photo-1556122071-e404eaedb77f?w=200&q=80\')"></div>', 1)

# totalLessons
assert h.count('var totalLessons=12;') == 1
h = h.replace('var totalLessons=12;', 'var totalLessons=13;', 1)

wr(ALU, h)
print("ALUNO applied OK; ex-lesson-13:", h.count('id="ex-lesson-13"'), "stamp13:", h.count('id="stamp13"'))
