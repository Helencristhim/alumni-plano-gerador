#!/usr/bin/env python3
import io
B = "/home/dan/dev/work/better/wt-jul-a18/_build/juliana-aula18/"
ALU = "/home/dan/dev/work/better/wt-jul-a18/public/aluno/juliana-marques.html"

def rd(p):
    with io.open(p, encoding="utf-8") as f: return f.read()
def wr(p, s):
    with io.open(p, "w", encoding="utf-8") as f: f.write(s)

accordion = rd(B+"accordion.html")
h = rd(ALU)
assert 'id="ex-lesson-18"' not in h, "aula 18 already present in aluno!"

anchor_acc = '</div><!-- /lesson-card Aula 17 -->'
assert h.count(anchor_acc) == 1
h = h.replace(anchor_acc, anchor_acc + "\n" + accordion, 1)

anchor_stamp = '<div class="stamp" id="stamp17" data-label="Planes" style="background-image:url(\'https://images.unsplash.com/photo-1496024840928-4c417adf211d?w=200&q=80\')"></div>'
assert h.count(anchor_stamp) == 1
h = h.replace(anchor_stamp, anchor_stamp + '\n        <div class="stamp" id="stamp18" data-label="El Pasado" style="background-image:url(\'https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=200&q=80\')"></div>', 1)

assert h.count('var totalLessons=17;') == 1
h = h.replace('var totalLessons=17;', 'var totalLessons=18;', 1)

wr(ALU, h)
print("ALUNO applied OK; ex-lesson-18:", h.count('id="ex-lesson-18"'), "stamp18:", h.count('id="stamp18"'))
