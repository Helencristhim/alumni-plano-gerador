#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""publish_family_guide.py — publica o family guide de um aluno.

    python3 scripts/publish_family_guide.py <slug> [<slug> ...]
    python3 scripts/publish_family_guide.py --all
    python3 scripts/publish_family_guide.py --check        (nao escreve; so confere)

O QUE FAZ
---------
Copia `_build/{slug}/family-guide.json` para `public/data/family-guide/{slug}.json`,
que e o caminho que a tab de runtime (`public/lib/family-guide.js`) busca no navegador.

POR QUE DUAS COPIAS, E NAO UMA
------------------------------
E a mesma separacao que o resto do sistema ja faz, e pelo mesmo motivo:

    FONTE (autoral, revisavel)          PUBLICADO (servido)
    _build/{slug}-aula{N}/preclass.html  ->  public/aluno/{slug}.html
    _build/{slug}/family-guide.json      ->  public/data/family-guide/{slug}.json

`_build/` e onde mora o conteudo escrito a mao — PERFIL-360.md, SYLLABUS.md e agora o
family guide — e e o diretorio que a revisao de PR de fato le. `public/` e artefato de
entrega. Editar direto no publicado e o comeco da divergencia: alguem corrige o texto no
lugar servido, a proxima geracao sobrescreve, e a correcao some sem deixar rastro.

**Edite SEMPRE o `_build/`, e rode este script.** O `--check` existe para o gate humano:
se ele reprovar, alguem editou o publicado a mao.

POR QUE UM SCRIPT E NAO UM `cp`
-------------------------------
Porque ele valida antes de copiar. JSON malformado nao quebra o build nem aparece em
review — ele quebra a tab do aluno em silencio, no navegador da mae, e ninguem fica
sabendo. Aqui o arquivo tem de parsear, ter `slug` batendo com o nome do diretorio e ter
pelo menos uma aula, senao nao e publicado.
"""
import json
import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
BUILD = os.path.join(ROOT, '_build')
PUB = os.path.join(ROOT, 'public', 'data', 'family-guide')

OBRIGATORIOS = ('slug', 'aulas')


def fonte(slug):
    return os.path.join(BUILD, slug, 'family-guide.json')


def publicado(slug):
    return os.path.join(PUB, f'{slug}.json')


def valida(slug, path):
    """Devolve (dados, erro). O erro e a mensagem pronta para a saida."""
    try:
        with open(path, encoding='utf-8') as fh:
            dados = json.load(fh)
    except json.JSONDecodeError as e:
        return None, f'JSON invalido ({e.msg}, linha {e.lineno})'
    except OSError as e:
        return None, f'ilegivel ({e.strerror})'

    faltando = [k for k in OBRIGATORIOS if k not in dados]
    if faltando:
        return None, f'faltam as chaves {faltando}'
    if dados['slug'] != slug:
        return None, f'o campo slug diz "{dados["slug"]}" mas o diretorio e "{slug}"'
    if not isinstance(dados['aulas'], list) or not dados['aulas']:
        return None, 'a lista "aulas" esta vazia'
    sem_n = [a for a in dados['aulas'] if 'n' not in a or 'titulo' not in a]
    if sem_n:
        return None, f'{len(sem_n)} aula(s) sem "n" ou "titulo"'
    return dados, None


def slugs_com_guia():
    if not os.path.isdir(BUILD):
        return []
    return sorted(d for d in os.listdir(BUILD) if os.path.isfile(fonte(d)))


def main():
    args = [a for a in sys.argv[1:]]
    checar = '--check' in args
    args = [a for a in args if a != '--check']

    if '--all' in args or not args:
        alvos = slugs_com_guia()
        if not alvos:
            print('Nenhum _build/{slug}/family-guide.json encontrado — nada a fazer.')
            return 0
    else:
        alvos = args

    os.makedirs(PUB, exist_ok=True)
    erros, escritos, iguais = [], [], []

    for slug in alvos:
        src = fonte(slug)
        if not os.path.isfile(src):
            erros.append(f'{slug}: sem {os.path.relpath(src, ROOT)}')
            continue

        dados, erro = valida(slug, src)
        if erro:
            erros.append(f'{slug}: {erro}')
            continue

        # Serializa a partir do objeto lido, nao copia bytes: assim o publicado sai
        # sempre no mesmo formato e um diff no publicado significa mudanca de CONTEUDO.
        texto = json.dumps(dados, ensure_ascii=False, indent=2) + '\n'
        dst = publicado(slug)
        atual = None
        if os.path.isfile(dst):
            with open(dst, encoding='utf-8') as fh:
                atual = fh.read()

        if atual == texto:
            iguais.append(f'{slug} ({len(dados["aulas"])} aula(s))')
            continue

        if checar:
            estado = 'ainda nao publicado' if atual is None else 'DIVERGENTE do _build'
            erros.append(f'{slug}: {estado}')
            continue

        with open(dst, 'w', encoding='utf-8') as fh:
            fh.write(texto)
        escritos.append(f'{slug} ({len(dados["aulas"])} aula(s))')

    for s in escritos:
        print(f'  + publicado  {s}')
    for s in iguais:
        print(f'  = ja igual   {s}')
    for e in erros:
        print(f'  ! {e}')

    if erros:
        print(f'\nfamily-guide: {len(erros)} problema(s).' +
              ('' if checar else ' Corrija o _build/ e rode de novo.'))
        return 1

    print(f'\nfamily-guide OK — {len(escritos)} publicado(s), {len(iguais)} ja igual(is).')
    return 0


if __name__ == '__main__':
    sys.exit(main())
