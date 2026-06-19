"""Reskin professor/daniela-feitoza-v2.html onto the MODEL prof shell (helen-mendes),
preserving ALL content: planning, exercises (Pre-class), plan (Plano de Aula),
teacher (Material do Professor), complementary, stamps, audioMap. Adds the legacy
plan/teacher tabs (which have no native model slot) as extra tab buttons + content.
IN CLASS = menu linking the standalones that exist (aula 7-14)."""
import re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from extract_blocks import extract_prof

ROOT = os.getcwd()
MODEL = os.path.join(ROOT, 'public/professor/helen-mendes.html')
LEGACY = os.path.join(ROOT, 'public/professor/daniela-feitoza-v2.html')

ACCENT, LIGHT = '#0d7377', '#14919b'
SLUG = 'daniela-feitoza-v2'
NAME = 'Daniela Feitoza'
TITLE = 'Professor View -- Daniela Feitoza | Professional English'
PASSPORT = 'Professional English Program'
SUBTITLE = 'Conversational English for International Professional Events &mdash; 43 Aulas'
STUDENT_INFO = '''      <span>S&atilde;o Paulo, SP</span>
      <span>N&iacute;vel A2+ (Pre-Intermediate)</span>
      <span>IT Manager &mdash; SPF Group</span>
      <span>43 aulas de 60 min</span>'''
TOTAL_AULAS = 43
TOTAL_LESSONS = 14

# IN CLASS standalone menu (only lessons with a standalone file)
INCLASS = [
    (7,  'Past Simple: Telling Stories That Connect'),
    (8,  'Networking in Action &mdash; Keeping the Conversation Going'),
    (9,  'Pronunciation Lab I &mdash; Sounds That Trip Up Brazilian Speakers'),
    (10, 'Pronunciation Lab II &mdash; Word Stress &amp; Connected Speech'),
    (11, 'Present Perfect vs Past Simple &mdash; Talking About Experience'),
    (12, 'Retail &amp; Fashion Tech Vocabulary &mdash; Presenting a Project'),
    (13, 'Expressing Opinions Professionally'),
    (14, 'Talking About the Future'),
]

def hexrgb(h):
    h=h.lstrip('#'); return tuple(int(h[i:i+2],16) for i in (0,2,4))

def replace_inner(s, om, cm, new):
    a=s.index(om); ae=s.index('>',a)+1; b=s.index(cm,ae); return s[:ae]+new+s[b:]

def replace_balanced_div_inner(s, om, new):
    a=s.index(om); ae=s.index('>',a)+1; depth,i=1,ae
    while depth>0:
        no=s.find('<div',i); nc=s.find('</div>',i)
        if no!=-1 and no<nc: depth+=1; i=no+4
        else: depth-=1; i=nc+6
    return s[:ae]+new+s[i-6:]

def inclass_menu():
    cards=['  <h3 style="font-family:\'Cormorant Garamond\',serif;font-size:1.3rem;margin-bottom:.5rem">IN CLASS -- Selecione a Aula</h3>',
           '  <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:1rem">Aulas 1-6 (material completo de sala): veja as abas <strong>Plano de Aula</strong> e <strong>Material do Professor</strong>. Aulas 7-14 abrem os slides interativos abaixo.</p>',
           '  <div style="display:flex;flex-direction:column;gap:1rem">']
    for n, title in INCLASS:
        cards.append(
            f'    <a href="/professor/{SLUG}-aula{n}.html?autostart=1" style="display:flex;align-items:center;gap:1rem;padding:1.2rem;background:rgba(255,255,255,.5);backdrop-filter:blur(8px);border:1px solid rgba(200,200,190,.5);border-radius:10px;cursor:pointer;transition:all .3s;text-decoration:none;color:inherit" onmouseover="this.style.borderColor=\'var(--accent)\'" onmouseout="this.style.borderColor=\'rgba(200,200,190,.5)\'">\n'
            f'      <div style="width:48px;height:48px;background:var(--accent);border-radius:8px;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:1.1rem">{n:02d}</div>\n'
            f'      <div><div style="font-weight:600;font-size:.95rem">{title}</div><div style="font-size:.8rem;color:var(--text-dim)">Slides interativos -- Aula {n}</div></div>\n'
            f'    </a>')
    cards.append('  </div>')
    cards.append('</div><!-- /tab-inclass -->')
    return '\n'+'\n'.join(cards)+'\n\n'

def main():
    b = extract_prof(LEGACY)
    s = open(MODEL, encoding='utf-8').read()

    r,g,bl = hexrgb(ACCENT)
    s = s.replace('#BE123C', ACCENT).replace('#be123c', ACCENT)
    s = s.replace('#F43F5E', LIGHT).replace('#f43f5e', LIGHT)
    s = s.replace('rgba(190,18,60', f'rgba({r},{g},{bl}')

    s = s.replace("window.STUDENT_SLUG='helen-mendes'", f"window.STUDENT_SLUG='{SLUG}'")
    s = re.sub(r'window\.TOTAL_AULAS=\d+', f'window.TOTAL_AULAS={TOTAL_AULAS}', s)
    s = s.replace('helen-mendes', SLUG)   # localStorage keys, standalone links in inclass (we overwrite inclass anyway), comments

    s = re.sub(r'<title>[^<]*</title>', f'<title>{TITLE}</title>', s, count=1)
    s = re.sub(r'<h1>[^<]*</h1>', f'<h1>{NAME}</h1>', s, count=1)
    s = re.sub(r'<div class="passport-badge">[^<]*</div>', f'<div class="passport-badge">{PASSPORT}</div>', s, count=1)
    s = re.sub(r'<p class="subtitle">[^<]*</p>', f'<p class="subtitle">{SUBTITLE}</p>', s, count=1)

    s = replace_balanced_div_inner(s, '<div class="student-info">', '\n'+STUDENT_INFO+'\n    ')
    s = replace_balanced_div_inner(s, '<div class="stamps-row">', '\n'+b['stamps_row']+'\n')

    # --- tab buttons: insert Plano de Aula + Material do Professor between Pre-class and IN CLASS ---
    s = s.replace(
        '<button class="tab-btn" onclick="switchTab(\'inclass\')">IN CLASS</button>',
        '<button class="tab-btn" onclick="switchTab(\'plan\')">Plano de Aula</button>\n'
        '    <button class="tab-btn" onclick="switchTab(\'teacher\')">Material do Professor</button>\n'
        '    <button class="tab-btn" onclick="switchTab(\'inclass\')">IN CLASS</button>')

    # --- tab contents ---
    s = replace_inner(s, '<div class="tab-content active" id="tab-planning">', '</div><!-- /tab-planning -->', '\n'+b['tab-planning'].strip('\n')+'\n')
    s = replace_inner(s, '<div class="tab-content" id="tab-exercises">', '</div><!-- /tab-exercises -->', '\n'+b['tab-exercises'].strip('\n')+'\n')
    # IN CLASS menu (replace model's helen links)
    s = replace_inner(s, '<div class="tab-content" id="tab-inclass">', '<!-- ========== TAB 4: COMPLEMENTARES ========== -->', inclass_menu())
    s = replace_inner(s, '<div class="tab-content" id="tab-complementary">', '</div><!-- /tab-complementary -->', '\n'+b['tab-complementary'].strip('\n')+'\n')

    # --- inject plan + teacher tab-content divs AFTER tab-inclass close ---
    inclass_close = '</div>\n\n<!-- ========== TAB 4: COMPLEMENTARES ========== -->'
    # the inclass div closes right before the complementary comment
    marker = s.index('<!-- ========== TAB 4: COMPLEMENTARES ========== -->')
    plan_teacher = (
        '<div class="tab-content" id="tab-plan">\n' + b['tab-plan'].strip('\n') + '\n</div><!-- /tab-plan -->\n\n'
        '<div class="tab-content" id="tab-teacher">\n' + b['tab-teacher'].strip('\n') + '\n</div><!-- /tab-teacher -->\n\n')
    s = s[:marker] + plan_teacher + s[marker:]

    # --- empty out the inline slides-wrapper (daniela uses linked standalones, no inline slides) ---
    s = replace_inner(s, '<div class="slides-container" id="slidesContainer">', '</div><!-- /slides-container -->', '\n')

    # --- audioMap ---
    i=s.index('var audioMap = {'); ib=s.index('{',i)+1; j=s.index('\n};',ib)
    s = s[:ib] + '\n' + b['audiomap_entries'].strip('\n') + '\n' + s[j+1:]

    s = re.sub(r'var totalLessons=\d+', f'var totalLessons={TOTAL_LESSONS}', s)

    open(LEGACY,'w',encoding='utf-8').write(s)
    print('wrote', LEGACY, len(s), 'bytes')

if __name__ == '__main__':
    main()
