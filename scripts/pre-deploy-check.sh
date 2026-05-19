#!/bin/bash
# Pre-deploy governance check for Alumni Plano Gerador
# Run before every deploy to catch common issues

ERRORS=0
WARNINGS=0

echo "========================================"
echo "  GOVERNANCA PRE-DEPLOY"
echo "========================================"
echo ""

# 1. Check for untracked HTML files in professor/ and aluno/
UNTRACKED=$(git status public/professor/ public/aluno/ --short 2>/dev/null | grep "^??" | grep -v backup | grep "\.html$")
if [ -n "$UNTRACKED" ]; then
    echo "ERRO: Arquivos HTML nao commitados (vao dar 404 na Vercel):"
    echo "$UNTRACKED" | sed 's/^/  /'
    ERRORS=$((ERRORS + 1))
    echo ""
fi

# 2. Check for deleted files still referenced
DELETED=$(git status public/professor/ public/aluno/ --short 2>/dev/null | grep "^ D" | grep "\.html$")
if [ -n "$DELETED" ]; then
    echo "ERRO: Arquivos HTML deletados (vao dar 404):"
    echo "$DELETED" | sed 's/^/  /'
    ERRORS=$((ERRORS + 1))
    echo ""
fi

# 3. Check professor files have correct 4-tab structure (not old 5-tab)
for f in public/professor/*.html; do
    [ ! -f "$f" ] && continue
    BASENAME=$(basename "$f")
    # Skip backups, tests, legacy files
    case "$BASENAME" in
        *backup*|*test*|elaine-v-*|maisa.html) continue ;;
    esac
    # Check for old model tabs
    if grep -q "Plano de Aula" "$f" 2>/dev/null; then
        if grep -q "Material do Professor" "$f" 2>/dev/null; then
            echo "AVISO: $BASENAME usa modelo antigo (5 abas com Plano de Aula + Material do Professor)"
            WARNINGS=$((WARNINGS + 1))
        fi
    fi
done

# 4. Check that multi-lesson files have lessonRanges or equivalent
for f in public/professor/*.html; do
    [ ! -f "$f" ] && continue
    BASENAME=$(basename "$f")
    case "$BASENAME" in
        *backup*|*test*|elaine-v-*|maisa.html) continue ;;
    esac
    # Count actual slides (data-slide attributes, not CSS classes)
    SLIDE_COUNT=$(grep -c 'data-slide="' "$f" 2>/dev/null | head -1 || echo 0)
    SLIDE_COUNT=$((SLIDE_COUNT + 0))
    # Count how many distinct lessons (data-lesson values)
    LESSON_COUNT=$(grep -oE 'data-lesson="[0-9]+"' "$f" 2>/dev/null | sort -u | wc -l | tr -d ' ')
    LESSON_COUNT=$((LESSON_COUNT + 0))
    if [ "$SLIDE_COUNT" -gt 30 ] && [ "$LESSON_COUNT" -gt 1 ]; then
        # Multi-lesson file, check for bounds
        HAS_RANGES=$(grep -c 'lessonRanges\|lessonSlideMap\|lessonSlideRanges\|lessonStartSlide\|lessonSlides' "$f" 2>/dev/null | head -1 || echo 0)
        HAS_RANGES=$((HAS_RANGES + 0))
        if [ "$HAS_RANGES" -eq 0 ]; then
            echo "ERRO: $BASENAME tem $SLIDE_COUNT slides em $LESSON_COUNT aulas mas NENHUM sistema de separacao"
            ERRORS=$((ERRORS + 1))
        fi
    fi
done

# 5. Check all internal links point to existing files
for f in public/professor/*.html; do
    [ ! -f "$f" ] && continue
    BASENAME=$(basename "$f")
    case "$BASENAME" in
        *backup*|*test*|elaine-v-*|maisa.html) continue ;;
    esac
    # Find href links to other professor/aluno files
    LINKS=$(grep -oE 'href="/(professor|aluno)/[^"]*\.html"' "$f" 2>/dev/null | sed 's/href="//;s/"$//')
    for link in $LINKS; do
        TARGET="public${link}"
        if [ ! -f "$TARGET" ]; then
            # Check if it's tracked in git
            if ! git ls-files --error-unmatch "$TARGET" >/dev/null 2>&1; then
                echo "ERRO: $BASENAME linka para $link que NAO EXISTE"
                ERRORS=$((ERRORS + 1))
            fi
        fi
    done
done

echo ""
echo "========================================"
if [ "$ERRORS" -gt 0 ]; then
    echo "  BLOQUEADO: $ERRORS erro(s), $WARNINGS aviso(s)"
    echo "  Corrija os erros antes de fazer deploy."
    echo "========================================"
    exit 1
else
    echo "  OK: 0 erros, $WARNINGS aviso(s)"
    echo "========================================"
    exit 0
fi
