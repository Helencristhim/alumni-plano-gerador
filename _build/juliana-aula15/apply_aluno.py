#!/usr/bin/env python3
import io
B = "/home/dan/dev/work/better/wt-jul-a15/_build/juliana-aula15/"
ALU = "/home/dan/dev/work/better/wt-jul-a15/public/aluno/juliana-marques.html"

def rd(p):
    with io.open(p, encoding="utf-8") as f: return f.read()
def wr(p, s):
    with io.open(p, "w", encoding="utf-8") as f: f.write(s)

accordion = rd(B+"accordion.html")
h = rd(ALU)
assert 'id="ex-lesson-15"' not in h, "aula 15 already present in aluno!"

anchor_acc = '</div><!-- /lesson-card Aula 14 -->'
assert h.count(anchor_acc) == 1
h = h.replace(anchor_acc, anchor_acc + "\n" + accordion, 1)

anchor_stamp = '<div class="stamp" id="stamp14" data-label="Restaurante" style="background-image:url(\'https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=200&q=80\')"></div>'
assert h.count(anchor_stamp) == 1
h = h.replace(anchor_stamp, anchor_stamp + '\n        <div class="stamp" id="stamp15" data-label="De Compras" style="background-image:url(\'https://images.unsplash.com/photo-1441986300917-64674bd600d8?w=200&q=80\')"></div>', 1)

assert h.count('var totalLessons=14;') == 1
h = h.replace('var totalLessons=14;', 'var totalLessons=15;', 1)

wr(ALU, h)
print("ALUNO applied OK; ex-lesson-15:", h.count('id="ex-lesson-15"'), "stamp15:", h.count('id="stamp15"'))
