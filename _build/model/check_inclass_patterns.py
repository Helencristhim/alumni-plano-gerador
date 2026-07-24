#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""check_inclass_patterns.py — gate anti-regressao dos 2 bugs sistemicos de IN CLASS.

Bug 1 (reveal quebrado): slides de Comprehension/Listening com
  <div class="comp-question" onclick="...toggle('revealed')"> + resposta em
  <p class="fill-answer" style="display:none"> MAS sem a regra CSS
  .comp-question.revealed .fill-answer{display:block} -> clicar nao revela nada.
  O padrao CORRETO do modelo e .comp-q/.q-answer. Aulas novas devem usar .comp-q,
  ou (se usarem .comp-question) ter a regra CSS de reveal.

Bug 2 (Common Mistake chapado): slide com <div class="mistake-item" style="...">
  cru (background inline) em vez das classes do modelo .mistake-wrong/.mistake-right.

USO: python3 _build/model/check_inclass_patterns.py public/professor/{slug}-aula{N}.html [...]
Sai != 0 (bloqueia) se algum arquivo tiver qualquer um dos padroes quebrados.
"""
import re
import sys


def check(path):
    s = open(path, encoding='utf-8').read()
    problems = []

    # Bug 1: comp-question sem a regra CSS de reveal
    if 'class="comp-question"' in s and '.comp-question.revealed' not in s:
        n = s.count('class="comp-question"')
        problems.append(
            f'{n}x <div class="comp-question"> SEM a regra CSS '
            f'.comp-question.revealed (reveal nao funciona). Use .comp-q/.q-answer '
            f'do modelo, ou adicione a regra .comp-question.revealed .fill-answer'
            f'{{display:block!important}}.')

    # Bug 2: mistake-item com background inline em vez de .mistake-wrong/.mistake-right
    bad_items = re.findall(r'<div class="mistake-item"\s+style="[^"]*(?:danger-bg|success-bg|background)[^"]*"', s)
    if bad_items:
        problems.append(
            f'{len(bad_items)}x <div class="mistake-item" style="...background..."> cru '
            f'(visual chapado). Use as classes do modelo: '
            f'<div class="mistake-item mistake-wrong"> / mistake-right.')

    # Bug 3 (badge do menu nao-quadrado): o numero da aula no menu IN CLASS e um
    # <div style="width:48px;height:48px;...border-radius:8px"> dentro de um flex row.
    # SEM flex-shrink:0 o flex ESPREME a largura do quadrado quando a descricao e
    # longa (2-3 linhas) -> o "quadradinho" vira RETANGULO VERTICAL. O menu_card do
    # builder ja emite flex-shrink:0; so cards feitos fora do builder (ad-hoc/legado)
    # nascem sem. (Incidente maria-claudia: 20 badges sem flex-shrink.)
    # Assinatura INLINE exata do badge do menu (dimensao -> background accent, direto,
    # sem flex-shrink no meio). Casar so isto evita pegar CSS solto no <style> (svg de
    # icone, .nav-btn circular) — o [^"] ganancioso atravessava as regras do <style>.
    bad_badges = re.findall(r'width:48px;height:48px;background:var\(--accent\);border-radius:8px', s)
    if bad_badges:
        problems.append(
            f'{len(bad_badges)}x badge 48x48 do menu IN CLASS SEM flex-shrink:0 '
            f'(descricao longa espreme o quadrado num retangulo vertical). Use '
            f'width:48px;height:48px;flex-shrink:0;... como o menu_card do builder.')

    # Bug A (template leitura): .ic-reading sem rolagem -> texto+alternativas estouram a tela
    if 'class="ic-reading"' in s and not re.search(r'\.ic-reading\s*\{[^}]*max-height', s):
        problems.append(
            '.ic-reading presente mas SEM max-height/overflow no CSS (texto longo + '
            'alternativas estouram os 100vh e ficam cortados). Adicione '
            '.ic-reading{max-height:42vh;overflow-y:auto}.')

    # Bug D (overlap): slide de leitura centraliza vertical -> conteudo alto transborda
    # pra cima e o titulo invade a barra de capitulos. Exige top-align nos slides de leitura.
    if 'class="ic-reading"' in s and 'ic-reading:not(.ic-collapsed)){align-items:flex-start' not in s:
        problems.append(
            '.ic-reading presente mas SEM a regra de top-align (slide alto transborda '
            'pra cima e o titulo colide com a barra de capitulos). Adicione '
            '.slide:has(.ic-reading:not(.ic-collapsed)){align-items:flex-start}.')

    # Bug B (parte 2): ic-tfrow sem data-answer -> True/False mostra os 2 veredictos
    rows = re.findall(r'<div class="ic-tfrow"([^>]*)>', s)
    missing = [r for r in rows if 'data-answer' not in r]
    if missing:
        problems.append(
            f'{len(missing)}x <div class="ic-tfrow"> SEM data-answer (True/False acende '
            f'TRUE e FALSE juntos). Marque data-answer="true|false" em cada linha.')

    # ============================================================
    # SANIDADE ESTRUTURAL dos componentes IN CLASS canonizados no shell
    # (B2/leitura: gap-fill+bank, Language Focus, Notice, Consolidate, Meaning
    # Guide, Check Your Work, Give the Advice). Cada gate dispara SO se o
    # componente estiver presente — aula que nao usa o bloco passa direto (no-op).
    # Pega bloco emitido pela metade (sem o filho obrigatorio) -> renderiza vazio
    # ou nao funciona. NAO reprova nenhuma aula existente (modelo 1-3 + Pricila).
    # ============================================================

    # Gap-fill em texto: cada .ic-gaptext PRECISA de pelo menos 1 .ic-blank,
    # senao e so um paragrafo sem lacuna (exercicio vazio).
    for m in re.finditer(r'<div class="ic-gaptext">(.*?)</div>\s*(?:<div class="ic-bank|</div>)', s, flags=re.S):
        if 'ic-blank' not in m.group(1):
            problems.append(
                '<div class="ic-gaptext"> SEM nenhuma <span class="ic-blank"> dentro '
                '(texto de gap-fill sem lacuna = exercicio vazio). Coloque as lacunas '
                'com <span class="ic-blank"><span class="ic-n">N</span>...</span>.')
            break

    # Word/Phrase bank: .ic-bank sem nenhum chip .ic-b = banco vazio.
    if 'class="ic-bank"' in s and 'class="ic-b"' not in s:
        problems.append(
            '<div class="ic-bank"> presente mas SEM nenhum <span class="ic-b"> '
            '(banco de palavras/frases vazio). Cada item do banco e um <span class="ic-b">.')

    # Language Focus (registro/intensidade): .ic-lf-list sem nenhuma linha .ic-lf.
    if 'class="ic-lf-list"' in s and 'class="ic-lf"' not in s:
        problems.append(
            '<div class="ic-lf-list"> presente mas SEM nenhuma linha <div class="ic-lf"> '
            '(Language Focus vazio).')

    # Meaning Guide (modais por forca): .ic-modals sem nenhum cartao .ic-modal-c.
    if 'class="ic-modals"' in s and 'class="ic-modal-c"' not in s:
        problems.append(
            '<div class="ic-modals"> presente mas SEM nenhum <div class="ic-modal-c"> '
            '(Meaning Guide sem cartoes de modal).')

    # Consolidate (matching): .ic-match sem as colunas .ic-match-col.
    if 'class="ic-match"' in s and 'class="ic-match-col"' not in s:
        problems.append(
            '<div class="ic-match"> presente mas SEM <div class="ic-match-col"> '
            '(Consolidate/matching sem as colunas de palavras e definicoes).')

    # Give the Advice (cenarios): .ic-scenario sem o rotulo .ic-who.
    if 'class="ic-scenario"' in s and 'class="ic-who"' not in s:
        problems.append(
            '<div class="ic-scenario"> presente mas SEM <div class="ic-who"> '
            '(cenario sem rotulo de quem/qual situacao).')

    # Check Your Work (auto-correcao): .ic-answer PRECISA do head clicavel que
    # chama icToggleAnswer, senao a resposta nunca revela (mesma classe do bug 1).
    if 'class="ic-answer"' in s and 'icToggleAnswer' not in s:
        problems.append(
            '<div class="ic-answer"> presente mas SEM onclick="icToggleAnswer(this)" no '
            '<div class="ic-ans-head"> (Check Your Work nao revela ao clicar).')

    return problems


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    total = 0
    for f in sys.argv[1:]:
        probs = check(f)
        if probs:
            total += len(probs)
            print(f'! {f}')
            for p in probs:
                print(f'    - {p}')
    if total:
        print(f'\nFALHOU: {total} problema(s) de padrao IN CLASS. Corrija antes do PR.')
        sys.exit(1)
    print(f'OK: {len(sys.argv) - 1} arquivo(s) sem padrao IN CLASS quebrado.')


if __name__ == '__main__':
    main()
