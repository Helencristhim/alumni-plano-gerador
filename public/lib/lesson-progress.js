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

  // ===== PROGRESSO DO PACOTE (concluídas ÷ contratadas) =====
  // Fonte da verdade: inclass_done (checklist do último slide) do Supabase.
  // Denominador: window.TOTAL_AULAS (o "48 aulas" mostrado no header). Teto 100%.
  // Totalmente INDEPENDENTE dos exercícios do Pre-class.
  var packageLoaded = false;
  var packagePct = 0;
  var packageCompleted = 0;
  var completedSet = {};

  function applyPackageProgress() {
    // O TEXTO mostra "feitas/contratadas" (ex: 2/48) — facilita contato de renovação.
    // Setado SEMPRE (usa cache/0), para sobrescrever o "%" que o updateProgress do
    // Pre-class escreve nesse mesmo elemento e evitar flash de porcentagem.
    var pp = document.getElementById('progressPercent');
    if (pp) pp.textContent = packageCompleted + '/' + totalAulas;
    if (!packageLoaded) return;
    // Stamps/cards acendem EXCLUSIVAMENTE pela conclusão do checklist (inclass_done)
    document.querySelectorAll('[id^="stamp"]').forEach(function(st) {
      if (!/^stamp\d+$/.test(st.id)) return;
      var n = parseInt(st.id.replace('stamp', ''), 10);
      if (completedSet[n]) st.classList.add('earned');
      else st.classList.remove('earned');
    });
    // Barra (largura visual) = concluídas ÷ contratadas em %
    var pb = document.getElementById('progressBar');
    if (pb) pb.style.width = packagePct + '%';
  }
  window.applyPackageProgress = applyPackageProgress;

  // ===== TOAST NOTIFICATION =====
  function showToast(msg, type) {
    var existing = document.getElementById('lp-toast');
    if (existing) existing.remove();
    var toast = document.createElement('div');
    toast.id = 'lp-toast';
    var bg = type === 'success' ? '#15803d' : type === 'error' ? '#dc2626' : '#003080';
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
      var grid = item.closest('.check-grid');
      // detecta a aula pelo slide (template novo) OU pelo data-lesson do próprio
      // check-grid (template antigo retrofitado). NUNCA confiar no id="checklist-N":
      // é inconsistente entre alunos (patricia-xavier aula5 = checklist-1).
      var lessonNum = detectLesson(slide);
      if (!lessonNum && grid && grid.dataset.lesson) lessonNum = parseInt(grid.dataset.lesson);
      if (!lessonNum) {
        console.warn('lesson-progress: could not detect lesson number for check item');
        return;
      }
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

  // ===== DETECT LESSON NUMBER FOR A LEGACY CHECKLIST =====
  // Template LEGADO: <ul class="checklist"><li><input onchange="toggleChecklist(this)">.
  // Sem .check-grid nem data-lesson proprio. Descobre a aula pela MESMA fonte confiavel
  // que o resto da lib usa, NUNCA pelo id="checklist-N" (inconsistente entre alunos —
  // patricia-xavier aula5 tem id="checklist-1"). Prioridade:
  //   1. o slide que contem o checklist (detectLesson: data-lesson do slide / lessonRanges)
  //   2. qualquer ancestral com [data-lesson]
  //   3. o lesson-card ancestral id="ex-lesson-N" (Pre-class accordion) → N
  function detectLessonForChecklist(list) {
    if (!list) return null;
    var lessonNum = detectLesson(list.closest('.slide'));
    if (lessonNum) return lessonNum;
    var dl = list.closest('[data-lesson]');
    if (dl && dl.dataset.lesson) {
      var n = parseInt(dl.dataset.lesson, 10);
      if (n) return n;
    }
    var card = list.closest('.lesson-card[id^="ex-lesson-"]');
    if (card) {
      var m = card.id.match(/^ex-lesson-(\d+)$/);
      if (m) return parseInt(m[1], 10);
    }
    return null;
  }

  // ===== WRAP toggleChecklist (paginas do template LEGADO) =====
  // Espelha o wrap de toggleCheck: quando TODOS os checkboxes de um <ul class="checklist">
  // estao marcados, grava inclass_done e acende o stamp. Idempotente (saveInclassDone faz
  // upsert onConflict). NAO dispara duas vezes se a pagina tambem tiver .check-grid: cada
  // template tem seu proprio handler e seus proprios checkboxes.
  if (typeof window.toggleChecklist === 'function') {
    var _originalToggleChecklist = window.toggleChecklist;
    window.toggleChecklist = function(cb) {
      _originalToggleChecklist(cb);
      var list = cb.closest ? cb.closest('.checklist') : null;
      if (!list) { var li = cb.closest ? cb.closest('li') : null; list = li ? li.parentElement : null; }
      if (!list) return;
      var lessonNum = detectLessonForChecklist(list);
      if (!lessonNum) {
        console.warn('lesson-progress: could not detect lesson number for checklist (legacy template)');
        return;
      }
      var boxes = list.querySelectorAll('input[type="checkbox"]');
      var checked = list.querySelectorAll('input[type="checkbox"]:checked');
      if (boxes.length > 0 && checked.length < boxes.length) {
        console.log('lesson-progress: ' + checked.length + '/' + boxes.length + ' checklist items checked (lesson ' + lessonNum + ')');
      }
      if (boxes.length > 0 && checked.length === boxes.length) {
        saveInclassDone(lessonNum);
      }
    };
    console.log('lesson-progress: toggleChecklist wrapped successfully');
  }

  // ===== WRAP updateProgress =====
  // updateProgress() (inline em cada hub) calcula a % dos EXERCÍCIOS do Pre-class
  // e escrevia por cima da barra do pacote + stamps. Aqui reafirmamos o progresso
  // do pacote (concluídas ÷ contratadas) depois que ela roda, mantendo as duas
  // coisas independentes. As mini-barras por aula seguem sendo atualizadas por ela.
  if (typeof window.updateProgress === 'function') {
    var _originalUpdateProgress = window.updateProgress;
    window.updateProgress = function() {
      var r = _originalUpdateProgress.apply(this, arguments);
      applyPackageProgress();
      return r;
    };
    console.log('lesson-progress: updateProgress wrapped (barra do pacote protegida)');
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
        completedSet = {};
        res.data.forEach(function(row) {
          if (row.inclass_done) {
            completedLessons++;
            completedSet[row.lesson_number] = true;
          }
        });
        console.log('lesson-progress: ' + completedLessons + ' aulas concluídas de ' + totalAulas);
        // Restore visual checks on professor pages
        document.querySelectorAll('.check-grid').forEach(function(grid) {
          var slide = grid.closest('.slide');
          var lessonNum = detectLesson(slide);
          if (!lessonNum && grid.dataset.lesson) lessonNum = parseInt(grid.dataset.lesson);
          if (lessonNum && completedSet[lessonNum]) {
            grid.querySelectorAll('.check-item').forEach(function(item) {
              item.classList.add('checked');
            });
          }
        });
        var denom = totalAulas > 0 ? totalAulas : 1;
        packagePct = Math.min(100, Math.round(completedLessons / denom * 100));
        packageCompleted = completedLessons;
        packageLoaded = true;
        applyPackageProgress();
        try { localStorage.setItem(slug + '-global-progress', JSON.stringify({ completed: completedLessons, total: totalAulas, pct: packagePct })); } catch(e) {}
      })
      .catch(function(err) {
        console.error('lesson-progress load catch:', err);
      });
  }

  window.loadGlobalProgress = loadGlobalProgress;
  window.saveInclassDone = saveInclassDone;

  function initProgress() {
    // valor imediato "feitas/contratadas" a partir do cache local (evita flash de "0%")
    try {
      var cached = JSON.parse(localStorage.getItem(slug + '-global-progress') || 'null');
      if (cached && typeof cached.completed === 'number') packageCompleted = cached.completed;
      var pp = document.getElementById('progressPercent');
      if (pp) pp.textContent = packageCompleted + '/' + totalAulas;
    } catch(e) {}
    loadGlobalProgress();
  }
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initProgress);
  } else {
    setTimeout(initProgress, 100);
  }
})();
