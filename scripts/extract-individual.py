#!/usr/bin/env python3
"""
Extract individual aula files from a monolithic professor HTML.
Creates slug-new-aulaN.html files with 4 tabs + slides for that lesson only.

Usage: python3 scripts/extract-individual.py eduarda-gabriel
"""
import sys
import re
import os

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 scripts/extract-individual.py <slug>")
        sys.exit(1)

    slug = sys.argv[1]
    new_slug = slug + '-new'
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    main_file = os.path.join(base_dir, 'public', 'professor', f'{slug}.html')

    if not os.path.exists(main_file):
        print(f"ERROR: {main_file} not found")
        sys.exit(1)

    with open(main_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    total_lines = len(lines)
    print(f"Read {total_lines} lines from {slug}.html")
    content = ''.join(lines)

    # ========== IDENTIFY SECTIONS ==========

    # Find audioMap
    audiomap_start = None
    audiomap_end = None
    for i, line in enumerate(lines):
        if 'var audioMap = {' in line:
            audiomap_start = i
        if audiomap_start and line.strip() == '};':
            audiomap_end = i
            break

    print(f"audioMap: lines {audiomap_start+1}-{audiomap_end+1}")

    # Find CSS (between </script> after audioMap and </style>)
    css_start = audiomap_end + 1
    css_end = None
    for i in range(css_start, len(lines)):
        if '</style>' in lines[i]:
            css_end = i
            break

    # Find Supabase config lines
    supabase_lines = []
    for i, line in enumerate(lines):
        if 'supabase' in line.lower() or 'STUDENT_SLUG' in line or 'TOTAL_AULAS' in line:
            if i > css_end:
                supabase_lines.append(i)
                if 'TOTAL_AULAS' in line:
                    break

    # Find </head> and <body>
    head_end = None
    body_start = None
    for i, line in enumerate(lines):
        if '</head>' in line:
            head_end = i
        if '<body>' in line:
            body_start = i
            break

    # Find logo-bar
    logobar_start = None
    logobar_end = None
    for i, line in enumerate(lines):
        if 'class="logo-bar"' in line or 'logo-bar' in line and '<div' in line:
            logobar_start = i
        if logobar_start and not logobar_end and '</div>' in line and i > logobar_start:
            logobar_end = i
            break

    # Find header hero
    header_start = None
    header_end = None
    for i, line in enumerate(lines):
        if '<!-- HEADER HERO -->' in line or 'class="header"' in line:
            if header_start is None:
                header_start = i
        if header_start and 'class="container"' in line:
            header_end = i - 1
            break

    # Find speed control
    speed_start = None
    speed_end = None
    for i, line in enumerate(lines):
        if 'class="speed-control"' in line:
            speed_start = i
        if speed_start and not speed_end and '</div>' in line and i > speed_start + 3:
            speed_end = i
            break

    # Find tabs wrapper
    tabs_start = None
    tabs_end = None
    for i, line in enumerate(lines):
        if 'class="tabs-wrapper"' in line:
            tabs_start = i
        if tabs_start and not tabs_end and '</div>' in line and '</div>' in lines[i]:
            if i > tabs_start + 2:
                tabs_end = i
                break

    # Find planning tab
    planning_start = None
    planning_end = None
    for i, line in enumerate(lines):
        if 'id="tab-planning"' in line:
            planning_start = i
        if planning_start and '/tab-planning' in line:
            planning_end = i
            break

    # Find pre-class exercises per lesson
    lesson_exercises = {}
    ex_starts = []
    for i, line in enumerate(lines):
        m = re.search(r'id="ex-lesson-(\d+)"', line)
        if m:
            lesson_num = int(m.group(1))
            ex_starts.append((lesson_num, i))

    # Find the exercise tab boundaries
    tab_exercises_start = None
    tab_exercises_end = None
    for i, line in enumerate(lines):
        if 'id="tab-exercises"' in line:
            tab_exercises_start = i
        if tab_exercises_start and '/tab-exercises' in line:
            tab_exercises_end = i
            break

    # Map exercise boundaries
    for idx, (lesson_num, start_line) in enumerate(ex_starts):
        if idx + 1 < len(ex_starts):
            end_line = ex_starts[idx + 1][1] - 1
        else:
            end_line = tab_exercises_end - 1
        lesson_exercises[lesson_num] = (start_line, end_line)
        print(f"  Pre-class lesson {lesson_num}: lines {start_line+1}-{end_line+1}")

    # Find complementary sections per lesson
    lesson_complementary = {}
    comp_start = None
    for i, line in enumerate(lines):
        if 'id="tab-complementary"' in line:
            comp_start = i
        if comp_start and '/tab-complementary' in line:
            comp_end = i
            break

    # Parse complementary by lesson headers
    comp_sections = []
    current_comp_start = None
    for i in range(comp_start, comp_end + 1):
        if 'Materiais Complementares' in lines[i] or ('Aula' in lines[i] and 'media-grid' not in lines[i] and '<h' in lines[i]):
            if current_comp_start is not None:
                comp_sections.append((current_comp_start, i - 1))
            current_comp_start = i
    if current_comp_start is not None:
        comp_sections.append((current_comp_start, comp_end - 1))

    for idx, (s, e) in enumerate(comp_sections):
        lesson_complementary[idx + 1] = (s, e)
        print(f"  Complementary lesson {idx+1}: lines {s+1}-{e+1}")

    # Find slides per lesson
    lesson_slides = {}
    slide_data = []
    for i, line in enumerate(lines):
        m = re.search(r'data-slide="(\d+)".*data-lesson="(\d+)"', line)
        if m:
            slide_num = int(m.group(1))
            lesson_num = int(m.group(2))
            slide_data.append((slide_num, lesson_num, i))

    # Group slides by lesson and find their line ranges
    from collections import defaultdict
    slides_by_lesson = defaultdict(list)
    for slide_num, lesson_num, line_idx in slide_data:
        slides_by_lesson[lesson_num].append((slide_num, line_idx))

    # Find the end of the slides container
    slides_container_end = None
    for i, line in enumerate(lines):
        if '/slides-container' in line:
            slides_container_end = i
            break

    for lesson_num in sorted(slides_by_lesson.keys()):
        slides = slides_by_lesson[lesson_num]
        first_slide_line = slides[0][1]
        # End is either next lesson's first slide - 1, or slides_container_end
        if lesson_num + 1 in slides_by_lesson:
            last_slide_line = slides_by_lesson[lesson_num + 1][0][1] - 2
        else:
            last_slide_line = slides_container_end - 2

        # Find the actual end by looking for the closing </div> of the last slide
        # Each slide is a <div class="slide ..."> ... </div> block
        last_slide_num = slides[-1][0]
        last_slide_start = slides[-1][1]
        # Find the next slide start or container end
        if lesson_num + 1 in slides_by_lesson:
            next_lesson_start = slides_by_lesson[lesson_num + 1][0][1]
        else:
            next_lesson_start = slides_container_end

        lesson_slides[lesson_num] = {
            'first_slide': slides[0][0],
            'last_slide': slides[-1][0],
            'count': len(slides),
            'start_line': first_slide_line,
            'end_line': next_lesson_start - 1
        }
        print(f"  Slides lesson {lesson_num}: slides {slides[0][0]}-{slides[-1][0]} ({len(slides)} slides), lines {first_slide_line+1}-{next_lesson_start}")

    # Find phase bar and labels
    phase_bar_start = None
    phase_labels_end = None
    for i, line in enumerate(lines):
        if 'class="phase-bar"' in line:
            phase_bar_start = i
        if phase_bar_start and 'phase-labels' in line:
            for j in range(i, len(lines)):
                if '</div>' in lines[j] and 'phase-labels' not in lines[j]:
                    phase_labels_end = j
                    break
            break

    # Find slides-container opening
    slides_container_start = None
    for i, line in enumerate(lines):
        if 'id="slidesContainer"' in line:
            slides_container_start = i
            break

    # Find teacher T, nav bar, confetti
    teacher_t_line = None
    nav_bar_start = None
    nav_bar_end = None
    confetti_line = None
    for i, line in enumerate(lines):
        if 'class="teacher-t"' in line:
            teacher_t_line = i
        if 'class="nav-bar"' in line:
            nav_bar_start = i
        if nav_bar_start and not nav_bar_end and '</div>' in line and i > nav_bar_start + 2:
            nav_bar_end = i
        if 'class="confetti-container"' in line:
            confetti_line = i

    # Find JS section
    js_start = None
    js_end = None
    for i in range(confetti_line, len(lines)):
        if '<script>' in lines[i] and 'src=' not in lines[i]:
            js_start = i
        if js_start and '</script>' in lines[i]:
            js_end = i
            break

    print(f"JS: lines {js_start+1}-{js_end+1}")

    # Find lesson-progress.js line
    progress_line = None
    for i, line in enumerate(lines):
        if 'lesson-progress.js' in line:
            progress_line = i
            break

    # ========== EXTRACT AUDIOMAP PHRASES PER LESSON ==========
    audiomap_content = ''.join(lines[audiomap_start:audiomap_end + 1])
    audiomap_entries = {}
    for m in re.finditer(r'"([^"]+)":\s*"([^"]+)"', audiomap_content):
        audiomap_entries[m.group(1)] = m.group(2)

    print(f"Total audioMap entries: {len(audiomap_entries)}")

    # ========== CREATE INDIVIDUAL FILES ==========
    num_lessons = len(lesson_exercises)

    # Get total aulas from the main file
    total_aulas_match = re.search(r'TOTAL_AULAS=(\d+)', content)
    total_aulas = total_aulas_match.group(1) if total_aulas_match else '50'

    # Get accent color
    accent_match = re.search(r'--accent:\s*([^;]+);', content)
    accent_color = accent_match.group(1).strip() if accent_match else '#7C5CBF'

    for lesson_num in range(1, num_lessons + 1):
        print(f"\n{'='*60}")
        print(f"Creating {new_slug}-aula{lesson_num}.html")
        print(f"{'='*60}")

        if lesson_num not in lesson_exercises:
            print(f"  WARNING: No exercises found for lesson {lesson_num}, skipping")
            continue
        if lesson_num not in lesson_slides:
            print(f"  WARNING: No slides found for lesson {lesson_num}, skipping")
            continue

        # Get slide info for this lesson
        sinfo = lesson_slides[lesson_num]
        num_slides = sinfo['count']
        first_slide = sinfo['first_slide']
        last_slide = sinfo['last_slide']
        offset = first_slide - 1  # To renumber slides starting from 1

        # Collect all text from pre-class and slides of this lesson to find used phrases
        # Include the welcome/onboarding card text too (common to all lessons)
        first_lesson_start = lesson_exercises[1][0] if 1 in lesson_exercises else lesson_exercises[lesson_num][0]
        welcome_text = ''.join(lines[tab_exercises_start:first_lesson_start]) if tab_exercises_start else ''
        preclass_text = ''.join(lines[lesson_exercises[lesson_num][0]:lesson_exercises[lesson_num][1] + 1])
        slides_text = ''.join(lines[sinfo['start_line']:sinfo['end_line'] + 1])
        lesson_text = welcome_text + preclass_text + slides_text

        # Find all phrases referenced in speakText calls and data-phrase attributes
        used_phrases = set()
        # Pattern: speakText('phrase') or speakText('phrase',this) or speakText('phrase', this)
        for m in re.finditer(r"speakText\('([^']+)'", lesson_text):
            used_phrases.add(m.group(1).replace("\\'", "'"))
        for m in re.finditer(r'speakText\("([^"]+)"', lesson_text):
            used_phrases.add(m.group(1))
        for m in re.finditer(r'data-phrase="([^"]+)"', lesson_text):
            used_phrases.add(m.group(1))
        # Also check for order items
        for m in re.finditer(r'\[order-l\d+\]', lesson_text):
            used_phrases.add(m.group(0))

        # Filter audioMap for this lesson
        filtered_audio = {}
        for phrase, path in audiomap_entries.items():
            if phrase in used_phrases:
                filtered_audio[phrase] = path

        print(f"  Used phrases: {len(used_phrases)}, audioMap entries: {len(filtered_audio)}")

        # Build slidePhases for this lesson (renumbered)
        slide_phases = {}
        for slide_num, l_num, line_idx in slide_data:
            if l_num == lesson_num:
                new_num = slide_num - offset
                phase_match = re.search(r'data-phase="(\d+)"', lines[line_idx])
                if phase_match:
                    slide_phases[new_num] = int(phase_match.group(1))

        # Get lesson title and theme from IN CLASS cards in the main
        lesson_title = f"Aula {lesson_num}"
        lesson_subtitle = ""
        for i, line in enumerate(lines):
            if f'onclick="enterSlideMode({first_slide})"' in line or (first_slide == 1 and 'onclick="enterSlideMode(1)"' in line):
                # Look for title in nearby lines
                for j in range(i, min(i+5, len(lines))):
                    title_m = re.search(r'font-weight:600.*?>([^<]+)<', lines[j])
                    if title_m:
                        lesson_title = title_m.group(1)
                    sub_m = re.search(r'text-dim.*?>([^<]+)<', lines[j])
                    if sub_m:
                        lesson_subtitle = sub_m.group(1)
                break

        # For lesson 1, the enterSlideMode might not pass a number
        if lesson_num == 1:
            for i, line in enumerate(lines):
                if 'enterSlideMode(1)' in line or ('enterSlideMode()' in line and 'tab-inclass' in ''.join(lines[max(0,i-10):i])):
                    for j in range(i, min(i+5, len(lines))):
                        title_m = re.search(r'font-weight:600.*?>([^<]+)<', lines[j])
                        if title_m:
                            lesson_title = title_m.group(1)
                        sub_m = re.search(r'text-dim.*?>([^<]+)<', lines[j])
                        if sub_m:
                            lesson_subtitle = sub_m.group(1)
                    break

        print(f"  Title: {lesson_title}")
        print(f"  Subtitle: {lesson_subtitle}")

        # ========== BUILD THE FILE ==========
        out = []

        # --- HEAD ---
        out.append('<!DOCTYPE html>\n')
        out.append('<html lang="pt-BR">\n')
        out.append('<head>\n')
        out.append('<meta charset="UTF-8">\n')
        out.append('<meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
        out.append('<meta name="robots" content="noindex, nofollow">\n')
        out.append(f'<title>Professor View — Eduarda Gabriel | Aula {lesson_num} | Business English | Alumni by Better</title>\n')
        out.append('<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500&display=swap" rel="stylesheet">\n')

        # AudioMap
        out.append('<script>\n')
        out.append('var audioMap = {\n')
        audio_items = list(filtered_audio.items())
        for idx, (phrase, path) in enumerate(audio_items):
            escaped_phrase = phrase.replace('"', '\\"')
            comma = ',' if idx < len(audio_items) - 1 else ''
            out.append(f'  "{escaped_phrase}": "{path}"{comma}\n')
        out.append('};\n')
        out.append('</script>\n')

        # CSS (from after audioMap script close to </style>)
        # Find the <style> tag after the audioMap
        style_start = None
        for i in range(audiomap_end + 1, len(lines)):
            if '<style>' in lines[i]:
                style_start = i
                break

        if style_start and css_end:
            for i in range(style_start, css_end + 1):
                out.append(lines[i])

        # Supabase
        out.append('<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2/dist/umd/supabase.min.js"></script>\n')
        out.append('<script src="/lib/supabase-config.js"></script>\n')
        out.append(f"<script>window.STUDENT_SLUG='{new_slug}';window.TOTAL_AULAS={total_aulas};</script>\n")

        out.append('</head>\n')
        out.append('<body>\n')
        out.append('\n')

        # --- LOGO BAR ---
        out.append('<!-- LOGO BAR -->\n')
        out.append('<div class="logo-bar">\n')
        out.append('  <img src="/assets/logo-alumni.png" alt="Alumni by Better">\n')
        out.append('  <span class="prof-badge">Professor View</span>\n')
        out.append(f'  <span class="slide-counter" id="slideCounter">01 / {num_slides:02d}</span>\n')
        out.append('</div>\n')
        out.append('\n')

        # --- MAIN CONTENT ---
        out.append('<!-- MAIN CONTENT -->\n')
        out.append('<div class="main-content">\n')
        out.append('\n')

        # Header hero (copy from main)
        if header_start is not None and header_end is not None:
            for i in range(header_start, header_end + 1):
                out.append(lines[i])
        out.append('\n')

        # Container + speed control
        out.append('<div class="container">\n')
        out.append('\n')
        if speed_start and speed_end:
            for i in range(speed_start, speed_end + 1):
                out.append(lines[i])
        out.append('\n')

        # Tabs
        out.append('<!-- TABS -->\n')
        out.append('<div class="tabs-wrapper">\n')
        out.append('  <div class="tabs">\n')
        out.append("    <button class=\"tab-btn active\" onclick=\"switchTab('planning')\">Planejamento</button>\n")
        out.append("    <button class=\"tab-btn\" onclick=\"switchTab('exercises')\">Pre-class</button>\n")
        out.append("    <button class=\"tab-btn\" onclick=\"switchTab('inclass')\">IN CLASS</button>\n")
        out.append("    <button class=\"tab-btn\" onclick=\"switchTab('complementary')\">Complementares</button>\n")
        out.append('  </div>\n')
        out.append('</div>\n')
        out.append('\n')

        # --- TAB 1: PLANNING ---
        if planning_start and planning_end:
            for i in range(planning_start, planning_end + 1):
                out.append(lines[i])
        out.append('\n')

        # --- TAB 2: PRE-CLASS ---
        out.append('<!-- ========== TAB 2: PRE-CLASS ========== -->\n')
        out.append('<div class="tab-content" id="tab-exercises">\n')
        ex_s, ex_e = lesson_exercises[lesson_num]

        # Include the welcome/onboarding card (between tab start and FIRST lesson card only)
        first_lesson_start = lesson_exercises[1][0] if 1 in lesson_exercises else ex_s
        if tab_exercises_start:
            for i in range(tab_exercises_start + 1, first_lesson_start):
                line = lines[i].strip()
                if line and not line.startswith('<!--'):
                    out.append(lines[i])

        # Copy the exercise content
        for i in range(ex_s, ex_e + 1):
            out.append(lines[i])

        out.append('\n</div><!-- /tab-exercises -->\n')
        out.append('\n')

        # --- TAB 3: IN CLASS ---
        out.append('<!-- ========== TAB 3: IN CLASS ========== -->\n')
        out.append('<div class="tab-content" id="tab-inclass">\n')
        out.append(f'  <h3 style="font-family:\'Cormorant Garamond\',serif;font-size:1.3rem;margin-bottom:1rem">IN CLASS — Aula {lesson_num}</h3>\n')
        out.append('  <div style="display:flex;flex-direction:column;gap:1rem">\n')
        out.append('    <div style="display:flex;align-items:center;gap:1rem;padding:1.2rem;background:rgba(255,255,255,.5);backdrop-filter:blur(8px);border:1px solid rgba(200,200,190,.5);border-radius:10px;cursor:pointer;transition:all .3s" onclick="enterSlideMode()" onmouseover="this.style.borderColor=\'var(--accent)\'" onmouseout="this.style.borderColor=\'rgba(200,200,190,.5)\'">\n')
        out.append(f'      <div style="width:48px;height:48px;background:var(--accent);border-radius:8px;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:1.1rem">{lesson_num:02d}</div>\n')
        out.append(f'      <div><div style="font-weight:600;font-size:.95rem">{lesson_title}</div><div style="font-size:.8rem;color:var(--text-dim)">{lesson_subtitle}</div></div>\n')
        out.append('    </div>\n')
        out.append('  </div>\n')
        out.append('</div>\n')
        out.append('\n')

        # --- TAB 4: COMPLEMENTARY ---
        out.append('<!-- ========== TAB 4: COMPLEMENTARES ========== -->\n')
        out.append('<div class="tab-content" id="tab-complementary">\n')
        out.append('\n')
        out.append(f'<h3 style="font-family:\'Cormorant Garamond\',serif;font-size:1.3rem;margin-bottom:.5rem">Materiais Complementares — Aula {lesson_num}</h3>\n')
        out.append('<p style="font-size:.82rem;color:var(--text-dim);margin-bottom:1.5rem">Conteúdos para reforçar o aprendizado fora de aula. Marque como concluído ao terminar.</p>\n')
        out.append('\n')

        if lesson_num in lesson_complementary:
            cs, ce = lesson_complementary[lesson_num]
            # Skip the header line (already added above) and get the media-grid
            in_media_grid = False
            for i in range(cs, ce + 1):
                if 'media-grid' in lines[i]:
                    in_media_grid = True
                if in_media_grid:
                    out.append(lines[i])
                    if '</div>' in lines[i] and lines[i].strip() == '</div>':
                        # Check if this closes the media-grid
                        pass
            # Ensure media-grid is closed
            if not any('</div>' == lines[ce].strip() for _ in [1]):
                pass

        out.append('\n</div><!-- /tab-complementary -->\n')
        out.append('\n')

        # Close container and main-content
        out.append('</div><!-- /container -->\n')
        out.append('</div><!-- /main-content -->\n')
        out.append('\n')

        # --- SLIDES WRAPPER (OUTSIDE main-content!!!) ---
        out.append('<!-- ============================== SLIDES WRAPPER (IN CLASS) ============================== -->\n')
        out.append('<div class="slides-wrapper">\n')
        out.append('\n')

        # Phase bar and labels
        if phase_bar_start and phase_labels_end:
            for i in range(phase_bar_start, phase_labels_end + 1):
                out.append(lines[i])
        out.append('\n')

        # Slides container
        out.append('<div class="slides-container" id="slidesContainer">\n')
        out.append('\n')

        # Copy slides for this lesson, renumbering
        for i in range(sinfo['start_line'], sinfo['end_line'] + 1):
            line = lines[i]
            # Renumber data-slide
            def renumber_slide(m):
                old_num = int(m.group(1))
                new_num = old_num - offset
                return f'data-slide="{new_num}"'

            line = re.sub(r'data-slide="(\d+)"', renumber_slide, line)

            # Remove data-lesson attribute (single lesson file doesn't need it)
            # Actually keep it for compatibility but set to 1
            line = re.sub(r'data-lesson="\d+"', 'data-lesson="1"', line)

            # Make first slide active
            if f'data-slide="1"' in line and 'class="slide' in line:
                if 'active' not in line:
                    line = line.replace('class="slide ', 'class="slide active ')
            elif 'active' in line and 'class="slide' in line and 'data-slide="1"' not in line:
                # Remove active from non-first slides
                line = line.replace(' active', '')

            out.append(line)

        out.append('\n</div><!-- /slides-container -->\n')
        out.append('</div><!-- /slides-wrapper -->\n')
        out.append('\n')

        # Teacher T icon
        out.append('<!-- Teacher T Icon -->\n')
        out.append('<div class="teacher-t" id="teacherT">T<div class="teacher-t-panel" id="teacherPanel"></div></div>\n')
        out.append('\n')

        # Nav bar
        out.append('<!-- Navigation Bar -->\n')
        out.append('<div class="nav-bar">\n')
        out.append('  <button class="nav-btn" id="prevBtn" onclick="changeSlide(-1)" disabled><svg viewBox="0 0 24 24"><polyline points="15 18 9 12 15 6"/></svg></button>\n')
        out.append('  <div class="slide-dots" id="slideDots"></div>\n')
        out.append('  <button class="nav-btn" id="nextBtn" onclick="changeSlide(1)"><svg viewBox="0 0 24 24"><polyline points="9 6 15 12 9 18"/></svg></button>\n')
        out.append('</div>\n')
        out.append('\n')

        # Confetti
        out.append('<!-- Confetti container -->\n')
        out.append('<div class="confetti-container" id="confettiContainer"></div>\n')
        out.append('\n')

        # --- JAVASCRIPT ---
        out.append('<script>\n')

        # Copy all JS but modify key variables
        if js_start and js_end:
            js_content = ''.join(lines[js_start + 1:js_end])

            # Replace totalSlides
            js_content = re.sub(r'var totalSlides\s*=\s*\d+;', f'var totalSlides = {num_slides};', js_content)

            # Replace lessonRanges
            js_content = re.sub(
                r'var lessonRanges\s*=\s*\{[^}]+\};',
                f'var lessonRanges = {{ 1: {{start: 1, end: {num_slides}}} }};',
                js_content
            )

            # Replace currentLesson
            js_content = re.sub(r'var currentLesson\s*=\s*\d+;', 'var currentLesson = 1;', js_content)

            # Replace slidePhases
            phases_str = ','.join([f'{k}:{v}' for k, v in sorted(slide_phases.items())])
            js_content = re.sub(
                r'var slidePhases\s*=\s*\{[^}]+\};',
                f'var slidePhases = {{{phases_str}}};',
                js_content
            )

            # Replace localStorage key
            js_content = js_content.replace(
                f"'{slug}-professor'",
                f"'{new_slug}-aula{lesson_num}-professor'"
            )
            js_content = js_content.replace(
                f'"{slug}-professor"',
                f'"{new_slug}-aula{lesson_num}-professor"'
            )

            # Fix enterSlideMode for single lesson
            # Make it always go to slide 1 when no arg
            js_content = js_content.replace(
                'function enterSlideMode(startSlide) {',
                'function enterSlideMode(startSlide) {\n  startSlide = startSlide || 1;'
            )

            out.append(js_content)

        out.append('</script>\n')
        out.append('<script src="/lib/lesson-progress.js"></script>\n')
        out.append('</body>\n')
        out.append('</html>\n')

        # ========== WRITE FILE ==========
        output_path = os.path.join(base_dir, 'public', 'professor', f'{new_slug}-aula{lesson_num}.html')
        with open(output_path, 'w', encoding='utf-8') as f:
            f.writelines(out)

        line_count = len(out)
        print(f"  Written: {output_path} ({line_count} lines)")

    # ========== VERIFY MAIN FILE NOT MODIFIED ==========
    with open(main_file, 'r', encoding='utf-8') as f:
        verify_lines = len(f.readlines())

    if verify_lines != total_lines:
        print(f"\n!!!!! CRITICAL ERROR: Main file changed from {total_lines} to {verify_lines} lines !!!!!")
        sys.exit(1)
    else:
        print(f"\nMain file verified: {verify_lines} lines (unchanged)")

    print("\nDone!")

if __name__ == '__main__':
    main()
