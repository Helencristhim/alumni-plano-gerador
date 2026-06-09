/**
 * Alumni — Lesson Progress Tracking (Supabase)
 *
 * Requer: window.STUDENT_SLUG e window.TOTAL_AULAS definidos ANTES de carregar este script.
 * Requer: supabase.min.js e supabase-config.js carregados ANTES.
 *
 * Funcionalidades:
 * 1. Professor: quando marca todos os checks no "What I Learned" → salva inclass_done no Supabase
 * 2. Ambos: ao carregar, busca progresso do Supabase → atualiza barra + stamps
 * 3. Toast visual para confirmar salvamento
 */

(function() {
  var slug = window.STUDENT_SLUG;
  var totalAulas = window.TOTAL_AULAS || 48;

  if (!slug) { console.warn('lesson-progress.js: STUDENT_SLUG not defined'); return; }

  // ===== TOAST NOTIFICATION =====
  function showToast(msg, type) {
    var existing = document.getElementById('lp-toast');
    if (existing) existing.remove();
    var toast = document.createElement('div');
    toast.id = 'lp-toast';
    var bg = type === 'success' ? '#16a34a' : type === 'error' ? '#dc2626' : '#003080';
    toast.style.cssText = 'position:fixed;bottom:1.5rem;right:1.5rem;background:' + bg + ';color:#fff;padding:.75rem 1.2rem;border-radius:8px;font:500 .85rem/1.4 "Inter",sans-serif;box-shadow:0 4px 20px rgba(0,0,0,.25);z-index:99999;opacity:0;transform:translateY(10px);transition:all .3s ease;max-width:320px;';
    toast.textContent = msg;
    document.body.appendChild(toast);
    requestAnimationFrame(function() {
      toast.style.opacity = '1';
      toast.style.transform = 'translateY(0)';
    });
    setTimeout(function() {
      toast.style.opacity = '0';
      toast.style.transform = 'translateY(10px)';
      setTimeout(function() { toast.remove(); }, 300);
    }, 3000);
  }

  // ===== DETECT LESSON NUMBER FOR A SLIDE =====
  function detectLesson(slide) {
    if (!slide) return null;
    if (slide.dataset.lesson) return parseInt(slide.dataset.lesson);
    if (typeof window.getLessonForSlide === 'function' && slide.dataset.slide) {
      return window.getLessonForSlide(parseInt(slide.dataset.slide));
    }
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

  // ===== CHECK SUPABASE AVAILABILITY =====
  function getSb() {
    try {
      if (typeof sb !== 'undefined' && sb) return sb;
    } catch(e) {}
    try {
      if (window.sb) return window.sb;
    } catch(e) {}
    return null;
  }

  // ===== WRAP toggleCheck (Professor pages) =====
  if (typeof window.toggleCheck === 'function') {
    var _originalToggleCheck = window.toggleCheck;
    window.toggleCheck = function(item) {
      _originalToggleCheck(item);
      var slide = item.closest('.slide');
      var lessonNum = detectLesson(slide);
      if (!lessonNum) {
        console.warn('lesson-progress: could not detect lesson number for check item');
        return;
      }
      var grid = item.closest('.check-grid');
      if (!grid) return;
      var allItems = grid.querySelectorAll('.check-item');
      var checkedItems = grid.querySelectorAll('.check-item.checked');
      var remaining = allItems.length - checkedItems.length;
      if (remaining > 0) {
        console.log('lesson-progress: ' + checkedItems.length + '/' + allItems.length + ' checked (lesson ' + lessonNum + ')');
      }
      if (checkedItems.length === allItems.length) {
        saveInclassDone(lessonNum);
      }
    };
    console.log('lesson-progress: toggleCheck wrapped successfully');
  } else {
    console.warn('lesson-progress: toggleCheck not found, wrapping skipped');
  }

  // ===== SAVE INCLASS DONE =====
  function saveInclassDone(lessonNum) {
    var supabase = getSb();
    if (!supabase) {
      console.error('lesson-progress: Supabase client not available');
      showToast('Erro: Supabase não conectado', 'error');
      return;
    }
    supabase.from('lesson_progress')
      .upsert({
        student_slug: slug,
        lesson_number: lessonNum,
        inclass_done: true,
        inclass_marked_at: new Date().toISOString()
      }, { onConflict: 'student_slug,lesson_number' })
      .then(function(res) {
        if (res.error) {
          console.error('lesson-progress save error:', res.error.message);
          showToast('Erro ao salvar aula ' + lessonNum + ': ' + res.error.message, 'error');
        } else {
          console.log('lesson-progress: aula ' + lessonNum + ' salva com sucesso');
          showToast('Aula ' + lessonNum + ' concluída!', 'success');
          var stampEl = document.getElementById('stamp' + lessonNum);
          if (stampEl) {
            stampEl.classList.add('earned');
            stampEl.style.transition = 'all 0.6s ease';
            stampEl.style.transform = 'scale(1.15)';
            setTimeout(function() { stampEl.style.transform = ''; }, 600);
          }
          loadGlobalProgress();
        }
      })
      .catch(function(err) {
        console.error('lesson-progress save catch:', err);
        showToast('Erro de rede ao salvar aula ' + lessonNum, 'error');
      });
  }

  // ===== LOAD GLOBAL PROGRESS FROM SUPABASE =====
  function loadGlobalProgress() {
    var supabase = getSb();
    if (!supabase) {
      console.warn('lesson-progress: Supabase not available for loadGlobalProgress');
      return;
    }
    supabase.from('lesson_progress')
      .select('lesson_number, inclass_done')
      .eq('student_slug', slug)
      .then(function(res) {
        if (res.error) {
          console.error('lesson-progress load error:', res.error.message);
          return;
        }
        if (!res.data) {
          console.warn('lesson-progress: no data returned');
          return;
        }
        var completedLessons = 0;
        var completedSet = {};
        res.data.forEach(function(row) {
          if (row.inclass_done) {
            completedLessons++;
            completedSet[row.lesson_number] = true;
            var stampEl = document.getElementById('stamp' + row.lesson_number);
            if (stampEl) stampEl.classList.add('earned');
          }
        });
        console.log('lesson-progress: ' + completedLessons + ' aulas concluídas de ' + totalAulas);
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
      })
      .catch(function(err) {
        console.error('lesson-progress load catch:', err);
      });
  }

  window.loadGlobalProgress = loadGlobalProgress;
  window.saveInclassDone = saveInclassDone;

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', loadGlobalProgress);
  } else {
    setTimeout(loadGlobalProgress, 100);
  }
})();
