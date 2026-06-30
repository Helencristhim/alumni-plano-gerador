#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""reaccent_tips.py — re-acentua os tips do professor (data-teacher) que foram
autorados em ASCII. SÓ mexe DENTRO de data-teacher="..." (não toca a tela do aluno
nem o inglês). SÓ troca palavras INEQUÍVOCAS (a forma sem acento não é outra palavra
PT válida). Palavras ambíguas (e/é, esta/está, da/dá, de/dê, so/só, la/lá, pratica,
pronuncia como verbo) NÃO são tocadas — ficam para revisão humana/subagente.

Uso: python3 _build/model/reaccent_tips.py public/professor/{slug}-aula{N}.html [...] [--apply]
Sem --apply = dry-run (conta trocas). Preserva caixa (Não/NÃO/não).
"""
import re
import sys

# inequívocas: forma sem acento NÃO é outra palavra PT válida neste contexto
DICT = {
    'nao': 'não', 'voce': 'você', 'voces': 'vocês', 'audio': 'áudio', 'audios': 'áudios',
    'video': 'vídeo', 'videos': 'vídeos', 'traducao': 'tradução', 'traducoes': 'traduções',
    'ingles': 'inglês', 'portugues': 'português', 'frances': 'francês', 'espanhol': 'espanhol',
    'atencao': 'atenção', 'entao': 'então', 'apos': 'após', 'tres': 'três',
    'proxima': 'próxima', 'proximo': 'próximo', 'proximas': 'próximas', 'proximos': 'próximos',
    'ultimo': 'último', 'ultima': 'última', 'ultimos': 'últimos', 'ultimas': 'últimas',
    'minimo': 'mínimo', 'maximo': 'máximo', 'padrao': 'padrão', 'padroes': 'padrões',
    'expressao': 'expressão', 'expressoes': 'expressões', 'revisao': 'revisão',
    'comparacao': 'comparação', 'comparacoes': 'comparações', 'informacao': 'informação',
    'informacoes': 'informações', 'producao': 'produção', 'transicao': 'transição',
    'transicoes': 'transições', 'discussao': 'discussão', 'opiniao': 'opinião',
    'opinioes': 'opiniões', 'sugestao': 'sugestão', 'sugestoes': 'sugestões',
    'correcao': 'correção', 'correcoes': 'correções', 'introducao': 'introdução',
    'conclusao': 'conclusão', 'seculo': 'século', 'numero': 'número', 'numeros': 'números',
    'licao': 'lição', 'licoes': 'lições', 'peca': 'peça', 'pecam': 'peçam',
    'faca': 'faça', 'facam': 'façam', 'comecar': 'começar', 'comece': 'comece',
    'ja': 'já', 'alem': 'além', 'tambem': 'também', 'porem': 'porém',
    'pais': 'país', 'voce': 'você', 'varias': 'várias', 'varios': 'vários',
    'basico': 'básico', 'basica': 'básica', 'publico': 'público', 'publica': 'pública',
    'especifico': 'específico', 'especifica': 'específica', 'dificil': 'difícil',
    'facil': 'fácil', 'possivel': 'possível', 'nivel': 'nível', 'util': 'útil',
    'disponivel': 'disponível', 'rapido': 'rápido', 'rapida': 'rápida',
    'proprio': 'próprio', 'propria': 'própria', 'historia': 'história',
    'memoria': 'memória', 'obrigatorio': 'obrigatório', 'necessario': 'necessário',
    'vocabulario': 'vocabulário', 'cenario': 'cenário', 'exercicio': 'exercício',
    'exercicios': 'exercícios', 'comentario': 'comentário', 'dialogo': 'diálogo',
    'dialogos': 'diálogos', 'gramatica': 'gramática', 'fonetica': 'fonética',
    'silaba': 'sílaba', 'silabas': 'sílabas', 'enfase': 'ênfase', 'tonica': 'tônica',
    'tecnica': 'técnica', 'tecnicas': 'técnicas', 'logica': 'lógica',
    'automatico': 'automático', 'automatica': 'automática', 'pagina': 'página',
    'paginas': 'páginas', 'titulo': 'título', 'titulos': 'títulos', 'codigo': 'código',
    'multiplo': 'múltiplo', 'multipla': 'múltipla', 'duvida': 'dúvida', 'duvidas': 'dúvidas',
    'pronunciacao': 'pronunciação', 'questao': 'questão', 'questoes': 'questões',
    'razao': 'razão', 'razoes': 'razões', 'situacao': 'situação', 'situacoes': 'situações',
    'acao': 'ação', 'acoes': 'ações', 'reuniao': 'reunião', 'reunioes': 'reuniões',
    'decisao': 'decisão', 'decisoes': 'decisões', 'questionario': 'questionário',
    'relatorio': 'relatório', 'usuario': 'usuário', 'usuarios': 'usuários',
    'area': 'área', 'areas': 'áreas', 'ideia': 'ideia', 'energia': 'energia',
    'estrategia': 'estratégia', 'estrategias': 'estratégias', 'sera': 'será',
    'voce': 'você', 'apos': 'após', 'atraves': 'através', 'series': 'séries',
}

# AMBÍGUAS — NÃO tocar (deixar p/ revisão): e/é, esta/está, este(=this), de/dê, da/dá,
# do/dó, so/só(EN), la/lá(EN), para(válida), pode(válida), pratica(verbo), pronuncia(verbo),
# continua(verbo), termina(verbo), foco(válida), toque(válida), reforce(válida), crie(válida),
# diga(válida), aula(válida), frase(válida), pergunta(válida), ideia(já certa).


def _apply_case(orig, repl):
    if orig.isupper():
        return repl.upper()
    if orig[0].isupper():
        return repl[0].upper() + repl[1:]
    return repl


def reaccent(s):
    """Re-acentua só o conteúdo de cada data-teacher."""
    count = [0]

    def repl(wm):
        w = wm.group(0)
        lo = w.lower()
        if lo in DICT:
            count[0] += 1
            return _apply_case(w, DICT[lo])
        return w

    def fix_pt(seg):
        # só PT: re-acentua palavras inequívocas
        return re.sub(r"[A-Za-z]+", repl, seg)

    def fix_tip(m):
        inner = m.group(1)
        # protege falas em INGLÊS entre aspas simples '...': só re-acentua FORA delas.
        # (também protege &#39; HTML entity de aspa simples)
        parts = re.split(r"('[^']*'|&#39;[^&]*&#39;)", inner)
        new = ''.join(seg if (seg.startswith("'") or seg.startswith('&#39;')) else fix_pt(seg)
                      for seg in parts)
        return 'data-teacher="' + new + '"'

    out = re.sub(r'data-teacher="([^"]*)"', fix_tip, s)
    return out, count[0]


def main():
    args = [a for a in sys.argv[1:] if a != '--apply']
    apply = '--apply' in sys.argv
    grand = 0
    for f in args:
        s = open(f, encoding='utf-8').read()
        out, n = reaccent(s)
        grand += n
        tag = 'APLICADO' if apply else 'dry-run'
        print(f'{f}: {n} troca(s) [{tag}]')
        if apply and out != s:
            open(f, 'w', encoding='utf-8').write(out)
    print(f'TOTAL trocas: {grand}')


if __name__ == '__main__':
    main()
