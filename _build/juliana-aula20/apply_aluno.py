#!/usr/bin/env python3
import io
B = "/home/dan/dev/work/better/wt-jul-a20/_build/juliana-aula20/"
ALU = "/home/dan/dev/work/better/wt-jul-a20/public/aluno/juliana-marques.html"

def rd(p):
    with io.open(p, encoding="utf-8") as f: return f.read()
def wr(p, s):
    with io.open(p, "w", encoding="utf-8") as f: f.write(s)

accordion = rd(B+"accordion.html")
h = rd(ALU)
assert 'id="ex-lesson-20"' not in h, "aula 20 already present in aluno!"

anchor_acc = '</div><!-- /lesson-card Aula 19 -->'
assert h.count(anchor_acc) == 1
h = h.replace(anchor_acc, anchor_acc + "\n" + accordion, 1)

anchor_stamp = '<div class="stamp" id="stamp19" data-label="El Futuro" style="background-image:url(\'https://images.unsplash.com/photo-1483354483454-4cd359948304?w=200&q=80\')"></div>'
assert h.count(anchor_stamp) == 1
h = h.replace(anchor_stamp, anchor_stamp + '\n        <div class="stamp" id="stamp20" data-label="&iexcl;Curso Completo!" style="background-image:url(\'https://images.unsplash.com/photo-1530021232320-687d8e3dba54?w=200&q=80\')"></div>', 1)

assert h.count('var totalLessons=19;') == 1
h = h.replace('var totalLessons=19;', 'var totalLessons=20;', 1)

wr(ALU, h)
print("ALUNO applied OK; ex-lesson-20:", h.count('id="ex-lesson-20"'), "stamp20:", h.count('id="stamp20"'))
