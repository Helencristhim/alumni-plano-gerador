"""Reskin aluno/daniela-feitoza-v2.html onto the MODEL aluno shell (helen-mendes), preserving
all content blocks verbatim. Output: public/aluno/daniela-feitoza-v2.html (model shell)."""
import re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from extract_blocks import extract_aluno

ROOT = os.getcwd()
MODEL = os.path.join(ROOT, 'public/aluno/helen-mendes.html')
LEGACY = os.path.join(ROOT, 'public/aluno/daniela-feitoza-v2.html')

ACCENT, LIGHT = '#0d7377', '#14919b'
SLUG = 'daniela-feitoza-v2'
NAME = 'Daniela Feitoza'
TITLE = 'Daniela Feitoza | Professional English -- Alumni'
PASSPORT = 'Professional English Program'
SUBTITLE = 'Conversational English for International Professional Events &mdash; 43 Aulas'
STUDENT_INFO = '''      <span>S&atilde;o Paulo, SP</span>
      <span>N&iacute;vel A2+ (Pre-Intermediate)</span>
      <span>IT Manager &mdash; SPF Group</span>
      <span>43 aulas de 60 min</span>'''
TOTAL_AULAS = 43
TOTAL_LESSONS = 14

def hexrgb(h):
    h = h.lstrip('#'); return tuple(int(h[i:i+2],16) for i in (0,2,4))

def replace_inner(s, open_marker, close_marker, new_inner):
    a = s.index(open_marker); a_end = s.index('>', a) + 1
    b = s.index(close_marker, a_end)
    return s[:a_end] + new_inner + s[b:]

def replace_balanced_div_inner(s, open_marker, new_inner):
    a = s.index(open_marker); a_end = s.index('>', a) + 1
    depth, i = 1, a_end
    while depth > 0:
        no = s.find('<div', i); nc = s.find('</div>', i)
        if no != -1 and no < nc: depth += 1; i = no + 4
        else: depth -= 1; i = nc + 6
    return s[:a_end] + new_inner + s[i-6:]

def main():
    blocks = extract_aluno(LEGACY)
    s = open(MODEL, encoding='utf-8').read()

    # --- accent swap (model -> daniela) ---
    r,g,b = hexrgb(ACCENT)
    s = s.replace('#BE123C', ACCENT).replace('#be123c', ACCENT)
    s = s.replace('#F43F5E', LIGHT).replace('#f43f5e', LIGHT)
    s = s.replace('rgba(190,18,60', f'rgba({r},{g},{b}')

    # --- slug / name / localStorage ---
    s = s.replace("window.STUDENT_SLUG='helen-mendes'", f"window.STUDENT_SLUG='{SLUG}'")
    s = re.sub(r'window\.TOTAL_AULAS=\d+', f'window.TOTAL_AULAS={TOTAL_AULAS}', s)
    s = s.replace("localStorage.removeItem('helen-mendes-aluno')", f"localStorage.removeItem('{SLUG}-aluno')")
    s = s.replace("localStorage.removeItem('alumni-progress-helen-mendes')", f"localStorage.removeItem('alumni-progress-{SLUG}')")
    s = s.replace("localStorage.setItem('helen-mendes-aluno'", f"localStorage.setItem('{SLUG}-aluno'")
    s = s.replace("localStorage.getItem('helen-mendes-aluno'", f"localStorage.getItem('{SLUG}-aluno'")
    s = s.replace("'alumni-progress-helen-mendes'", f"'alumni-progress-{SLUG}'")
    s = s.replace("'{SLUG}-aluno'", f"'{SLUG}-aluno'")
    # any remaining helen-mendes (e.g. localStorage keys, comments) -> slug
    s = s.replace('helen-mendes', SLUG)

    # --- title / h1 / labels ---
    s = re.sub(r'<title>[^<]*</title>', f'<title>{TITLE}</title>', s, count=1)
    s = re.sub(r'<h1>[^<]*</h1>', f'<h1>{NAME}</h1>', s, count=1)
    s = re.sub(r'<div class="passport-badge">[^<]*</div>', f'<div class="passport-badge">{PASSPORT}</div>', s, count=1)
    s = re.sub(r'<p class="subtitle">[^<]*</p>', f'<p class="subtitle">{SUBTITLE}</p>', s, count=1)
    s = s.replace(NAME + ' Mendes', NAME)  # safety: undo any 'Daniela Feitoza Mendes' if formed (none expected)

    # --- header student-info ---
    s = replace_balanced_div_inner(s, '<div class="student-info">', '\n' + STUDENT_INFO + '\n    ')

    # --- stamps-row ---
    s = replace_balanced_div_inner(s, '<div class="stamps-row">', '\n' + blocks['stamps_row'] + '\n')

    # --- tab-exercises ---
    s = replace_inner(s, '<div class="tab-content active" id="tab-exercises">',
                      '</div><!-- /tab-exercises -->', '\n' + blocks['tab_exercises'].strip('\n') + '\n')
    # --- tab-complementary ---
    s = replace_inner(s, '<div class="tab-content" id="tab-complementary">',
                      '</div><!-- /tab-complementary -->', '\n' + blocks['tab_complementary'].strip('\n') + '\n')

    # --- audioMap ---
    i = s.index('var audioMap = {'); ib = s.index('{', i) + 1
    j = s.index('\n};', ib)
    s = s[:ib] + '\n' + blocks['audiomap_entries'].strip('\n') + '\n' + s[j+1:]

    # --- totalLessons ---
    s = re.sub(r'var totalLessons=\d+', f'var totalLessons={TOTAL_LESSONS}', s)

    open(LEGACY, 'w', encoding='utf-8').write(s)
    print('wrote', LEGACY, len(s), 'bytes')

if __name__ == '__main__':
    main()
