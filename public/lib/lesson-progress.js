/**
 * Alumni — Lesson Progress Tracking (Supabase)
 *
 * Requer: window.STUDENT_SLUG e window.TOTAL_AULAS definidos ANTES de carregar este script.
 * Requer: supabase.min.js e supabase-config.js carregados ANTES.
 *
 * Funcionalidades:
 * 1. Professor: quando marca 5/5 checks no "What I Learned" → salva inclass_done no Supabase
 * 2. Ambos: ao carregar, busca progresso do Supabase → atualiza barra + stamps
 */

(function() {
  var slug = window.STUDENT_SLUG;
  var totalAulas = window.TOTAL_AULAS || 48;

  if (!slug) { console.warn('lesson-progress.js: STUDENT_SLUG not defined'); return; }

  // ===== DETECT LESSON NUMBER FOR A SLIDE =====
  // Try data-lesson first, then lessonRanges/getLessonForSlide, then fallback to 1
  function detectLesson(slide) {
    if (!slide) return null;
    // 1. data-lesson attribute (Gabriela, newer materials)
    if (slide.dataset.lesson) return parseInt(slide.dataset.lesson);
    // 2. getLessonForSlide function + data-slide (Luiz, older materials)
    if (typeof window.getLessonForSlide === 'function' && slide.dataset.slide) {
      return window.getLessonForSlide(parseInt(slide.dataset.slide));
    }
    // 3. lessonRanges object + data-slide
    if (window.lessonRanges && slide.dataset.slide) {
      var slideNum = parseInt(slide.dataset.slide);
      for (var l in window.lessonRanges) {
        var range = window.lessonRanges[l];
        var start = Array.isArray(range) ? range[0] : range.start;
        var end = Array.isArray(range) ? range[1] : range.end;
        if (slideNum >= start && slideNum <= end) return parseInt(l);
      }
    }
    return null;
  }

  // ===== WRAP toggleCheck (Professor pages) =====
  if (typeof window.toggleCheck === 'function') {
    var _originalToggleCheck = window.toggleCheck;
    window.toggleCheck = function(item) {
      _originalToggleCheck(item);
      var slide = item.closest('.slide');
      var lessonNum = detectLesson(slide);
      if (!lessonNum) return;
      var grid = item.closest('.check-grid');
      if (!grid) return;
      var allItems = grid.querySelectorAll('.check-item');
      var checkedItems = grid.querySelectorAll('.check-item.checked');
      if (checkedItems.length === allItems.length) {
        saveInclassDone(lessonNum);
      }
    };
  }

  // ===== SAVE INCLASS DONE =====
  function saveInclassDone(lessonNum) {
    if (typeof sb === 'undefined') return;
    try {
      sb.from('lesson_progress')
        .upsert({
          student_slug: slug,
          lesson_number: lessonNum,
          inclass_done: true,
          inclass_marked_at: new Date().toISOString()
        }, { onConflict: 'student_slug,lesson_number' })
        .then(function(res) {
          if (res.error) console.error('Supabase error:', res.error.message);
          else {
            console.log('In-class done saved for lesson', lessonNum);
            var stampEl = document.getElementById('stamp' + lessonNum);
            if (stampEl) stampEl.classList.add('earned');
            loadGlobalProgress();
          }
        });
    } catch(e) { console.error('saveInclassDone error:', e); }
  }

  // ===== LOAD GLOBAL PROGRESS FROM SUPABASE =====
  function loadGlobalProgress() {
    if (typeof sb === 'undefined') return;
    try {
      sb.from('lesson_progress')
        .select('lesson_number, inclass_done')
        .eq('student_slug', slug)
        .then(function(res) {
          if (res.error || !res.data) return;
          var completedLessons = 0;
          var completedSet = {};
          res.data.forEach(function(row) {
            if (row.inclass_done) {
              completedLessons++;
              completedSet[row.lesson_number] = true;
              // Light up stamp
              var stampEl = document.getElementById('stamp' + row.lesson_number);
              if (stampEl) stampEl.classList.add('earned');
            }
          });
          // Restore visual checks on professor pages
          document.querySelectorAll('.check-grid').forEach(function(grid) {
            var slide = grid.closest('.slide');
            var lessonNum = detectLesson(slide);
            if (lessonNum && completedSet[lessonNum]) {
              grid.querySelectorAll('.check-item').forEach(function(item) {
                item.classList.add('checked');
              });
            }
          });
          var pct = Math.round(completedLessons / totalAulas * 100);
          var pb = document.getElementById('progressBar');
          var pp = document.getElementById('progressPercent');
          if (pb) pb.style.width = pct + '%';
          if (pp) pp.textContent = pct + '%';
          try { localStorage.setItem(slug + '-global-progress', JSON.stringify({ completed: completedLessons, total: totalAulas, pct: pct })); } catch(e) {}
        });
    } catch(e) { console.error('loadGlobalProgress error:', e); }
  }

  window.loadGlobalProgress = loadGlobalProgress;
  window.saveInclassDone = saveInclassDone;

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', loadGlobalProgress);
  } else {
    setTimeout(loadGlobalProgress, 100);
  }
})();
