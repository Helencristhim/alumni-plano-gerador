#!/usr/bin/env python3
import io
B = "/home/dan/dev/work/better/wt-jul-a16/_build/juliana-aula16/"
ALU = "/home/dan/dev/work/better/wt-jul-a16/public/aluno/juliana-marques.html"

def rd(p):
    with io.open(p, encoding="utf-8") as f: return f.read()
def wr(p, s):
    with io.open(p, "w", encoding="utf-8") as f: f.write(s)

accordion = rd(B+"accordion.html")
h = rd(ALU)
assert 'id="ex-lesson-16"' not in h, "aula 16 already present in aluno!"

anchor_acc = '</div><!-- /lesson-card Aula 15 -->'
assert h.count(anchor_acc) == 1
h = h.replace(anchor_acc, anchor_acc + "\n" + accordion, 1)

anchor_stamp = '<div class="stamp" id="stamp15" data-label="De Compras" style="background-image:url(\'https://images.unsplash.com/photo-1441986300917-64674bd600d8?w=200&q=80\')"></div>'
assert h.count(anchor_stamp) == 1
h = h.replace(anchor_stamp, anchor_stamp + '\n        <div class="stamp" id="stamp16" data-label="Salud" style="background-image:url(\'https://images.unsplash.com/photo-1576091160550-2173dba999ef?w=200&q=80\')"></div>', 1)

assert h.count('var totalLessons=15;') == 1
h = h.replace('var totalLessons=15;', 'var totalLessons=16;', 1)

wr(ALU, h)
print("ALUNO applied OK; ex-lesson-16:", h.count('id="ex-lesson-16"'), "stamp16:", h.count('id="stamp16"'))
