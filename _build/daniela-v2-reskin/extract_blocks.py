"""Extract daniela-feitoza-v2 content blocks from the LEGACY hub for splicing into the model shell."""
import re

def _balanced_div_inner(src, open_marker):
    """Return inner HTML of the div that begins with open_marker, balancing nested <div>."""
    a = src.index(open_marker)
    a_end = src.index('>', a) + 1
    depth = 1
    i = a_end
    while depth > 0:
        no = src.find('<div', i)
        nc = src.find('</div>', i)
        if nc == -1:
            raise ValueError('unbalanced')
        if no != -1 and no < nc:
            depth += 1
            i = no + 4
        else:
            depth -= 1
            i = nc + 6
    return src[a_end:i-6]  # exclude the final </div>

def _trim_one_trailing_div(s):
    m = re.search(r'\s*</div>\s*$', s)
    if m:
        return s[:m.start()] + '\n'
    return s

def extract_aluno(path):
    src = open(path, encoding='utf-8').read()
    blocks = {}
    blocks['student_info'] = _balanced_div_inner(src, '<div class="student-info">').strip('\n')
    blocks['stamps_row'] = _balanced_div_inner(src, '<div class="stamps-row">').strip('\n')
    a = src.index('<div class="tab-content active" id="tab-exercises">')
    a_end = src.index('>', a) + 1
    b = src.index('<!-- ==================== TAB 2: ATIVIDADES COMPLEMENTARES ====================')
    blocks['tab_exercises'] = _trim_one_trailing_div(src[a_end:b])
    c = src.index('<div class="tab-content" id="tab-complementary">')
    c_end = src.index('>', c) + 1
    d = src.index('<button class="reset-btn"', c_end)
    blocks['tab_complementary'] = _trim_one_trailing_div(src[c_end:d])
    i = src.index('const audioMap = {')
    ib = src.index('{', i) + 1
    j = src.index('\n    };', i)
    blocks['audiomap_entries'] = src[ib:j].rstrip()
    return blocks

if __name__ == '__main__':
    b = extract_aluno('public/aluno/daniela-feitoza-v2.html')
    for k,v in b.items():
        print(f"{k}: len={len(v)} ex-lesson={v.count('id=\"ex-lesson-')} media-wrap={v.count('media-card-wrapper')} stamps={v.count('id=\"stamp')} audioentries={v.count(chr(34)+': '+chr(34))} vocab-pc={v.count('vocab-card-pc')} match-row={v.count('class=\"match-row\"')} quiz-item={v.count('class=\"quiz-item\"')}")


def extract_prof(path):
    src = open(path, encoding='utf-8').read()
    b = {}
    b['student_info'] = _balanced_div_inner(src, '<div class="student-info">').strip('\n')
    b['stamps_row'] = _balanced_div_inner(src, '<div class="stamps-row">').strip('\n')
    for tab in ['tab-planning', 'tab-exercises', 'tab-plan', 'tab-teacher', 'tab-complementary']:
        b[tab] = _balanced_div_inner(src, f'id="{tab}"')
    i = src.index('const audioMap = {'); ib = src.index('{', i) + 1
    j = src.index('\n    };', i)
    b['audiomap_entries'] = src[ib:j].rstrip()
    return b
