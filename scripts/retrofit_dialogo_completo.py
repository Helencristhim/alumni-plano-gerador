#!/usr/bin/env python3
"""Troca o limite CRAVADO de `nextDialogueLine()` pelo total real de falas do slide.

O DEFEITO. A funcao vinda do modelo desligava o botao "Next Line" num numero fixo:

    if (dialogueLine >= 10) { ... 'Dialogue Complete'; disabled = true }

O 10 e o total de falas DO MODELO (helen-mendes-aula1). Numa aula com 13 falas o botao
morre na 10 anunciando "Dialogue Complete", e as falas 11-13 nunca ganham `.visible` —
ficam em `opacity:0` para sempre. O slide de Comprehension seguinte cobra justamente o
fim do dialogo, entao a aula pergunta sobre falas que a tela nunca mostrou.
Reportado pelo Dan em patricia-yamaguti-shimada aula 2, slide 19.

ESCOPO. Somente os arquivos passados na lista — os medidos como PERDENDO fala
(limite < total). Arquivos onde o limite cravado ainda cobre todas as falas nao entram:
nao ha dano hoje, e legado nao se mexe sem dano medido (REGRA 30).

SEGURANCA. Casa o corpo INTEIRO da funcao antiga (texto exato, sem regex guloso) e
recusa o arquivo se nao casar exatamente uma vez. Nao toca em mais nada.

    python3 scripts/retrofit_dialogo_completo.py lista.txt
    python3 scripts/retrofit_dialogo_completo.py lista.txt --dry-run
"""
import re
import sys

NOVA = '''// ===== DIALOGUE LINE-BY-LINE =====
// O LIMITE NUNCA E UM NUMERO CRAVADO. Sai do total real de falas da caixa DESTE slide.
// Por que: o modelo tem 10 falas, entao o antigo limite fixo de 10 falas funcionava
// AQUI e desligava o botao na fala 10 em toda aula com mais de 10 falas. As ultimas
// nunca apareciam, e sao justamente as que o slide de Comprehension seguinte cobra
// (incidente patricia-yamaguti-shimada aula 2, slide 19: 13 falas, 3 perdidas, e as 3
// perguntas eram sobre elas). Contar o DOM torna o defeito impossivel de nascer.
function nextDialogueLine(btn) {
  btn = btn || document.getElementById('nextLineBtn');
  var scope = (btn && btn.closest('.slide')) || document;
  var box = scope.querySelector('.dialogue-box') || scope;
  var lines = box.querySelectorAll('.dialogue-line');
  var next = null, shown = 0;
  for (var i = 0; i < lines.length; i++) {
    if (lines[i].classList.contains('visible')) shown++;
    else if (!next) next = lines[i];
  }
  if (next) { next.classList.add('visible'); shown++; }
  if (btn && shown >= lines.length) {
    btn.textContent = 'Dialogue Complete';
    btn.disabled = true;
    btn.style.opacity = '0.5';
  }
}'''

ANTIGA = re.compile(
    r'// ===== DIALOGUE LINE-BY-LINE =====\n'
    r'var dialogueLine = 0;\n'
    r'function nextDialogueLine\(\) \{\n'
    r'  dialogueLine\+\+;\n'
    r'  var line = document\.querySelector\('
    r'\'\.dialogue-line\[data-line="\' \+ dialogueLine \+ \'"\]\'\);\n'
    r'  if \(line\) \{\n'
    r'    line\.classList\.add\(\'visible\'\);\n'
    r'    if \(dialogueLine >= \d+\) \{\n'
    r'      document\.getElementById\(\'nextLineBtn\'\)\.textContent = \'Dialogue Complete\';\n'
    r'      document\.getElementById\(\'nextLineBtn\'\)\.disabled = true;\n'
    r'      document\.getElementById\(\'nextLineBtn\'\)\.style\.opacity = \'0\.5\';\n'
    r'    \}\n'
    r'  \}\n'
    r'\}'
)


def main(argv):
    dry = '--dry-run' in argv
    lista = [a for a in argv[1:] if not a.startswith('--')][0]
    paths = [l.strip() for l in open(lista) if l.strip()]
    ok, recusados = [], []
    for f in paths:
        h = open(f, encoding='utf-8').read()
        if len(ANTIGA.findall(h)) != 1:
            recusados.append(f)
            continue
        if not dry:
            open(f, 'w', encoding='utf-8').write(ANTIGA.sub(lambda m: NOVA, h))
        ok.append(f)
    print('%s: %d arquivo(s)' % ('casariam' if dry else 'corrigidos', len(ok)))
    if recusados:
        print('RECUSADOS (padrao nao casou 1x) — %d:' % len(recusados))
        for f in recusados:
            print('   ' + f)
    return 1 if recusados else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
