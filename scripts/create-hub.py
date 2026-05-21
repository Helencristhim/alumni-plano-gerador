#!/usr/bin/env python3
"""
Create a hub file from the monolithic professor HTML.
The hub is a FULL copy of the original (same CSS, header, stamps, tabs)
but Pre-class and IN CLASS show linked cards instead of inline content.

Usage: python3 scripts/create-hub.py eduarda-gabriel
"""
import sys
import re
import os

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 scripts/create-hub.py <slug>")
        sys.exit(1)

    slug = sys.argv[1]
    new_slug = slug + '-new'
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    main_file = os.path.join(base_dir, 'public', 'professor', f'{slug}.html')

    with open(main_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    total_lines = len(lines)
    print(f"Read {total_lines} lines from {slug}.html")

    # ========== IDENTIFY KEY SECTIONS ==========

    # Find lesson info from IN CLASS tab cards
    lessons = []
    in_inclass = False
    for i, line in enumerate(lines):
        if 'id="tab-inclass"' in line:
            in_inclass = True
        if in_inclass and 'id="tab-complementary"' in line:
            break
        if in_inclass:
            m = re.search(r'onclick="enterSlideMode\((\d+)\)"', line)
            if m:
                start_slide = int(m.group(1))
                # Find title and subtitle in nearby lines
                title = ""
                subtitle = ""
                for j in range(i, min(i+5, len(lines))):
                    tm = re.search(r'font-weight:600[^>]*>([^<]+)<', lines[j])
                    if tm:
                        title = tm.group(1)
                    sm = re.search(r'text-dim[^>]*>([^<]+)<', lines[j])
                    if sm:
                        subtitle = sm.group(1)
                lessons.append({'start_slide': start_slide, 'title': title, 'subtitle': subtitle})

    # Get lesson images from stamps
    stamp_images = []
    for i, line in enumerate(lines):
        m = re.search(r'class="stamp"[^>]*data-label="([^"]*)"[^>]*background-image:url\(\'([^\']+)\'\)', line)
        if m:
            stamp_images.append({'label': m.group(1), 'url': m.group(2)})

    print(f"Found {len(lessons)} lessons, {len(stamp_images)} stamps")

    # ========== FIND SECTION BOUNDARIES ==========

    # audioMap
    audiomap_start = audiomap_end = None
    for i, line in enumerate(lines):
        if 'var audioMap = {' in line:
            audiomap_start = i
        if audiomap_start and line.strip() == '};':
            audiomap_end = i
            break

    # CSS end
    css_end = None
    for i, line in enumerate(lines):
        if '</style>' in line:
            css_end = i
            break

    # Supabase lines
    supabase_start = None
    supabase_end = None
    for i in range(css_end + 1, len(lines)):
        if 'supabase' in lines[i].lower() and '<script' in lines[i]:
            supabase_start = i
        if supabase_start and 'TOTAL_AULAS' in lines[i]:
            supabase_end = i
            break

    # </head> and <body>
    head_end = body_start = None
    for i, line in enumerate(lines):
        if '</head>' in line:
            head_end = i
        if '<body>' in line:
            body_start = i
            break

    # Logo bar to header end
    logobar_start = None
    for i, line in enumerate(lines):
        if 'class="logo-bar"' in line:
            logobar_start = i
            break

    # main-content start
    main_content_start = None
    for i, line in enumerate(lines):
        if 'class="main-content"' in line:
            main_content_start = i
            break

    # Header + speed control + tabs up to planning start
    planning_start = None
    for i, line in enumerate(lines):
        if 'id="tab-planning"' in line:
            planning_start = i
            break

    # Planning end
    planning_end = None
    for i, line in enumerate(lines):
        if planning_start and '/tab-planning' in line:
            planning_end = i
            break

    # Tab exercises start
    tab_exercises_start = None
    for i, line in enumerate(lines):
        if 'id="tab-exercises"' in line:
            tab_exercises_start = i
            break

    # Welcome card end (before first lesson card)
    welcome_end = None
    for i, line in enumerate(lines):
        if 'id="ex-lesson-1"' in line:
            welcome_end = i - 1
            break

    # Tab in-class
    tab_inclass_start = tab_inclass_end = None
    for i, line in enumerate(lines):
        if 'id="tab-inclass"' in line:
            tab_inclass_start = i
        if tab_inclass_start and not tab_inclass_end and 'id="tab-complementary"' in line:
            tab_inclass_end = i - 1
            break

    # Tab complementary
    tab_comp_start = tab_comp_end = None
    for i, line in enumerate(lines):
        if 'id="tab-complementary"' in line:
            tab_comp_start = i
        if tab_comp_start and '/tab-complementary' in line:
            tab_comp_end = i
            break

    # Container/main-content end
    main_content_end = None
    for i, line in enumerate(lines):
        if '/main-content' in line:
            main_content_end = i
            break

    # JS section (for tab switching and audio functions only)
    js_start = js_end = None
    for i, line in enumerate(lines):
        if '<script>' in line and 'src=' not in line and i > main_content_end:
            js_start = i
        if js_start and '</script>' in line and i > js_start:
            js_end = i
            break

    # lesson-progress.js
    progress_line = None
    for i, line in enumerate(lines):
        if 'lesson-progress.js' in line:
            progress_line = i
            break

    # ========== BUILD HUB FILE ==========
    out = []

    # 1. Copy HEAD: DOCTYPE through audioMap
    for i in range(0, audiomap_start):
        out.append(lines[i])

    # AudioMap: only survival phrases (5 phrases)
    out.append('<script>\n')
    out.append('var audioMap = {\n')
    survival_phrases = [
        ("Could you repeat that, please?", None),
        ("I am not sure I understand. Could you explain?", None),
        ("Let me think about that for a moment.", None),
        ("In my experience, I would say...", None),
        ("Could I add something to that?", None),
    ]
    # Find actual paths from the full audioMap
    content = ''.join(lines)
    audiomap_text = ''.join(lines[audiomap_start:audiomap_end + 1])
    audio_entries = {}
    for m in re.finditer(r'"([^"]+)":\s*"([^"]+)"', audiomap_text):
        audio_entries[m.group(1)] = m.group(2)

    phrases_with_paths = []
    for phrase, _ in survival_phrases:
        if phrase in audio_entries:
            phrases_with_paths.append((phrase, audio_entries[phrase]))

    for idx, (phrase, path) in enumerate(phrases_with_paths):
        comma = ',' if idx < len(phrases_with_paths) - 1 else ''
        out.append(f'  "{phrase}": "{path}"{comma}\n')
    out.append('};\n')
    out.append('</script>\n')

    # 2. CSS: from after audioMap to </style>
    style_start = None
    for i in range(audiomap_end + 1, len(lines)):
        if '<style>' in lines[i]:
            style_start = i
            break
    if style_start and css_end:
        for i in range(style_start, css_end + 1):
            out.append(lines[i])

    # 3. Supabase with new slug
    out.append('<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2/dist/umd/supabase.min.js"></script>\n')
    out.append('<script src="/lib/supabase-config.js"></script>\n')

    # Get TOTAL_AULAS from original
    total_aulas_match = re.search(r'TOTAL_AULAS=(\d+)', content)
    total_aulas = total_aulas_match.group(1) if total_aulas_match else '50'
    out.append(f"<script>window.STUDENT_SLUG='{new_slug}';window.TOTAL_AULAS={total_aulas};</script>\n")

    out.append('</head>\n')
    out.append('<body>\n\n')

    # 4. Logo bar (without slide counter)
    out.append('<!-- LOGO BAR -->\n')
    out.append('<div class="logo-bar">\n')
    out.append('  <img src="/assets/logo-alumni.png" alt="Alumni by Better">\n')
    out.append('  <span class="prof-badge">Professor View</span>\n')
    out.append('</div>\n\n')

    # 5. Main content start through header hero
    out.append('<!-- MAIN CONTENT -->\n')
    out.append('<div class="main-content">\n\n')

    # Copy header hero from original (main_content_start+1 to container start)
    header_start = None
    for i in range(main_content_start, len(lines)):
        if 'class="header"' in line or '<!-- HEADER' in lines[i]:
            header_start = i
            break

    container_start = None
    for i in range(main_content_start, len(lines)):
        if 'class="container"' in lines[i]:
            container_start = i
            break

    # Copy from after main-content div to planning start (header, speed, tabs)
    for i in range(main_content_start + 1, planning_start):
        out.append(lines[i])

    # 6. Planning tab (full copy)
    for i in range(planning_start, planning_end + 1):
        out.append(lines[i])
    out.append('\n')

    # 7. Pre-class tab — welcome card + linked lesson cards
    out.append('<!-- ========== TAB 2: PRE-CLASS ========== -->\n')
    out.append('<div class="tab-content" id="tab-exercises">\n\n')

    # Copy welcome card
    if tab_exercises_start and welcome_end:
        for i in range(tab_exercises_start + 1, welcome_end + 1):
            out.append(lines[i])
    out.append('\n')

    # Generate linked lesson cards
    for idx, lesson in enumerate(lessons):
        lesson_num = idx + 1
        img_url = stamp_images[idx]['url'] if idx < len(stamp_images) else 'https://images.unsplash.com/photo-1507679799987-c73779587ccf?w=600&q=80'
        title = lesson['title'] or f'Aula {lesson_num}'
        subtitle = lesson['subtitle'] or ''

        out.append(f'<!-- LESSON {lesson_num} CARD -->\n')
        out.append(f'<a href="/professor/{new_slug}-aula{lesson_num}.html" style="text-decoration:none;color:inherit;display:block">\n')
        out.append(f'<div class="lesson-card" id="ex-lesson-{lesson_num}" style="cursor:pointer">\n')
        out.append(f'  <div class="lesson-header" style="pointer-events:auto">\n')
        out.append(f"    <div class=\"lesson-header-img\" style=\"background-image:url('{img_url}')\"></div>\n")
        out.append(f'    <div class="lesson-header-content">\n')
        out.append(f'      <div class="lesson-number">Aula {lesson_num:02d} — Pre-class + IN CLASS</div>\n')
        out.append(f'      <h3>{title}</h3>\n')
        out.append(f'      <p style="font-size:.82rem;color:var(--text-dim)">{subtitle}</p>\n')
        out.append(f'    </div>\n')
        out.append(f'  </div>\n')
        out.append(f'</div>\n')
        out.append(f'</a>\n\n')

    out.append('</div><!-- /tab-exercises -->\n\n')

    # 8. IN CLASS tab — linked cards
    out.append('<!-- ========== TAB 3: IN CLASS ========== -->\n')
    out.append('<div class="tab-content" id="tab-inclass">\n')
    out.append('  <h3 style="font-family:\'Cormorant Garamond\',serif;font-size:1.3rem;margin-bottom:1rem">IN CLASS — Selecione a Aula</h3>\n')
    out.append('  <div style="display:flex;flex-direction:column;gap:1rem">\n')

    for idx, lesson in enumerate(lessons):
        lesson_num = idx + 1
        title = lesson['title'] or f'Aula {lesson_num}'
        subtitle = lesson['subtitle'] or ''
        out.append(f"    <a href=\"/professor/{new_slug}-aula{lesson_num}.html\" style=\"text-decoration:none;color:inherit;display:flex;align-items:center;gap:1rem;padding:1.2rem;background:rgba(255,255,255,.5);backdrop-filter:blur(8px);border:1px solid rgba(200,200,190,.5);border-radius:10px;cursor:pointer;transition:all .3s\" onmouseover=\"this.style.borderColor='var(--accent)'\" onmouseout=\"this.style.borderColor='rgba(200,200,190,.5)'\">\n")
        out.append(f"      <div style=\"width:48px;height:48px;background:var(--accent);border-radius:8px;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:1.1rem\">{lesson_num:02d}</div>\n")
        out.append(f"      <div><div style=\"font-weight:600;font-size:.95rem\">{title}</div><div style=\"font-size:.8rem;color:var(--text-dim)\">{subtitle}</div></div>\n")
        out.append(f'    </a>\n')

    out.append('  </div>\n')
    out.append('</div>\n\n')

    # 9. Complementary tab (full copy)
    if tab_comp_start and tab_comp_end:
        for i in range(tab_comp_start, tab_comp_end + 1):
            out.append(lines[i])
    out.append('\n')

    # 10. Close container and main-content
    out.append('</div><!-- /container -->\n')
    out.append('</div><!-- /main-content -->\n\n')

    # 11. Confetti container
    out.append('<div class="confetti-container" id="confettiContainer"></div>\n\n')

    # 12. JavaScript — tab switching + audio functions only (no slides)
    out.append('<script>\n')
    out.append('// Tab switching\n')
    out.append('function switchTab(tabId) {\n')
    out.append("  document.querySelectorAll('.tab-content').forEach(function(t) { t.classList.remove('active'); });\n")
    out.append("  document.querySelectorAll('.tab-btn').forEach(function(b) { b.classList.remove('active'); });\n")
    out.append("  document.getElementById('tab-' + tabId).classList.add('active');\n")
    out.append("  event.currentTarget.classList.add('active');\n")
    out.append("  window.scrollTo({ top: 0, behavior: 'smooth' });\n")
    out.append('}\n\n')

    out.append('// Lesson toggle\n')
    out.append('function toggleLesson(header) { header.parentElement.classList.toggle("open"); }\n\n')

    out.append('// Audio\n')
    out.append('var currentAudio = null;\n')
    out.append("var audioSpeed = parseFloat(localStorage.getItem('alumni-audio-speed') || '1');\n\n")

    out.append('function setAudioSpeed(speed, btn) {\n')
    out.append('  audioSpeed = speed;\n')
    out.append("  localStorage.setItem('alumni-audio-speed', speed);\n")
    out.append("  document.querySelectorAll('.speed-btn').forEach(function(b) {\n")
    out.append("    b.style.background = 'var(--bg-card)'; b.style.color = 'var(--text)';\n")
    out.append("    b.style.borderColor = 'var(--border)'; b.style.fontWeight = '400';\n")
    out.append("    b.classList.remove('active');\n")
    out.append('  });\n')
    out.append("  btn.style.background = 'var(--accent)'; btn.style.color = '#fff';\n")
    out.append("  btn.style.borderColor = 'var(--accent)'; btn.style.fontWeight = '600';\n")
    out.append("  btn.classList.add('active');\n")
    out.append('}\n\n')

    out.append("document.addEventListener('DOMContentLoaded', function() {\n")
    out.append("  var saved = parseFloat(localStorage.getItem('alumni-audio-speed') || '1');\n")
    out.append("  var btn = document.querySelector('.speed-btn[data-speed=\"' + saved + '\"]');\n")
    out.append('  if (btn) setAudioSpeed(saved, btn);\n')
    out.append('});\n\n')

    out.append('function speakText(text, btn) {\n')
    out.append('  if (currentAudio) { currentAudio.pause(); currentAudio.currentTime = 0; }\n')
    out.append("  var cleanText = text.replace(/\\\\'/g, \"'\");\n")
    out.append("  var file = audioMap[cleanText] || audioMap[cleanText.replace(/\\.$/, '')] || audioMap[cleanText + '.'];\n")
    out.append('  if (file) {\n')
    out.append('    currentAudio = new Audio(file);\n')
    out.append('    currentAudio.playbackRate = audioSpeed;\n')
    out.append("    currentAudio.play().catch(function() { ttsSpeak(cleanText); });\n")
    out.append('  } else { ttsSpeak(cleanText); }\n')
    out.append('}\n\n')

    out.append("function ttsSpeak(text) {\n")
    out.append("  if ('speechSynthesis' in window) {\n")
    out.append("    window.speechSynthesis.cancel();\n")
    out.append("    var u = new SpeechSynthesisUtterance(text);\n")
    out.append("    u.lang = 'en-US'; u.rate = audioSpeed * 0.85; u.pitch = 1;\n")
    out.append("    window.speechSynthesis.speak(u);\n")
    out.append("  }\n")
    out.append("}\n\n")

    out.append('// Media toggle\n')
    out.append('function toggleMediaDone(cb) {\n')
    out.append("  var wrapper = cb.closest('.media-card-wrapper');\n")
    out.append("  if (cb.checked) wrapper.classList.add('done');\n")
    out.append("  else wrapper.classList.remove('done');\n")
    out.append('}\n\n')

    out.append('// Progress (from stamps/checks)\n')
    out.append('function updateProgress() {\n')
    out.append("  var checks = document.querySelectorAll('.media-card-wrapper');\n")
    out.append("  var done = document.querySelectorAll('.media-card-wrapper.done');\n")
    out.append("  var pct = checks.length > 0 ? Math.round((done.length / checks.length) * 100) : 0;\n")
    out.append("  var bar = document.getElementById('progressBar');\n")
    out.append("  var txt = document.getElementById('progressPercent');\n")
    out.append("  if (bar) bar.style.width = pct + '%';\n")
    out.append("  if (txt) txt.textContent = pct + '%';\n")
    out.append('}\n')

    out.append('</script>\n')
    out.append('<script src="/lib/lesson-progress.js"></script>\n')
    out.append('</body>\n')
    out.append('</html>\n')

    # ========== WRITE ==========
    output_path = os.path.join(base_dir, 'public', 'professor', f'{new_slug}.html')
    with open(output_path, 'w', encoding='utf-8') as f:
        f.writelines(out)

    print(f"Written: {output_path} ({len(out)} lines)")

    # Verify main not changed
    with open(main_file, 'r') as f:
        if len(f.readlines()) != total_lines:
            print("CRITICAL: Main file was modified!")
            sys.exit(1)
    print(f"Main file verified: {total_lines} lines (unchanged)")

if __name__ == '__main__':
    main()
