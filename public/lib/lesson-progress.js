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
  var maxCompleted = 0;  // MAIOR aula concluída (inclass_done). Base do acender CUMULATIVO.

  function applyPackageProgress() {
    // O TEXTO mostra "feitas/contratadas" (ex: 2/48) — facilita contato de renovação.
    // Setado SEMPRE (usa cache/0), para sobrescrever o "%" que o updateProgress do
    // Pre-class escreve nesse mesmo elemento e evitar flash de porcentagem.
    var pp = document.getElementById('progressPercent');
    if (pp) pp.textContent = packageCompleted + '/' + totalAulas;
    if (!packageLoaded) return;
    // Stamps acendem CUMULATIVO: toda aula ATÉ a maior concluída (maxCompleted), não só
    // as marcadas individualmente. Aluno "na aula 7" tem 1..7 acesos mesmo que só 1,2,7
    // tenham inclass_done no Supabase (progresso é sequencial — decisão Dan 24/07/2026).
    // MONOTÔNICO: só ACENDE, nunca apaga. Progresso NÃO PODE SUMIR — se um load do
    // Supabase vier vazio/parcial (rede, race, erro), o que já acendeu FICA aceso.
    // (Ordem do Dan 24/07/2026: "que os quadros acendam e não apaguem".) Sem o `else
    // remove`, nenhum caminho tira o .earned de um stamp já ganho.
    document.querySelectorAll('[id^="stamp"]').forEach(function(st) {
      if (!/^stamp\d+$/.test(st.id)) return;
      var n = parseInt(st.id.replace('stamp', ''), 10);
      if (n <= maxCompleted) st.classList.add('earned');
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
  // Ultimo recurso: a aula pelo NOME DO ARQUIVO. Material standalone chama-se
  // {slug}-aula{N}.html e contem UMA aula so. Quando nem o slide nem o container
  // do checklist declaram data-lesson (andrea-aggio aula7/8), sem isto lessonNum
  // fica null e o material NUNCA registra a aula: a professora marca os 5 checks,
  // ve o visual mudar e nada e gravado — falha silenciosa. So entra depois que
  // todo o resto falhou, e nao vale para hub multi-aula (sem "-aulaN" no nome).
  function lessonFromFilename() {
    var m = (window.location.pathname || '').match(/-aula(\d+)\.html?$/i);
    return m ? parseInt(m[1], 10) : null;
  }

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
      // O container do checklist NAO tem um nome so no roster: e .check-grid, e
      // .check-list (milton-sayegh 11-20), e as vezes um <div> sem classe nenhuma
      // (luiz-bressane 13-20). Procurar so por .check-grid deixava `grid` null e o
      // `return` abaixo engolia o registro: 18 aulas em que a professora marcava os
      // 5 checks, via o visual mudar, e a aula NUNCA era concluida — por causa do
      // nome de uma classe CSS. Por isso o ultimo recurso e o PAI dos itens, aceito
      // so quando ele agrupa 2+ check-items (senao cada item viraria seu proprio
      // "grid completo" e a aula fecharia no primeiro clique).
      var grid = item.closest('.check-grid, .check-list');
      if (!grid) {
        var parent = item.parentElement;
        if (parent && parent.querySelectorAll('.check-item').length > 1) grid = parent;
      }
      // detecta a aula pelo slide (template novo) OU pelo data-lesson do próprio
      // container (template antigo retrofitado). NUNCA confiar no id="checklist-N":
      // é inconsistente entre alunos (patricia-xavier aula5 = checklist-1).
      var lessonNum = detectLesson(slide);
      if (!lessonNum && grid && grid.dataset.lesson) lessonNum = parseInt(grid.dataset.lesson);
      if (!lessonNum) lessonNum = lessonFromFilename();
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
    // Grava a aula marcada E TODAS AS ANTERIORES (1..N), nao so a N.
    //
    // Por que. O progresso e SEQUENCIAL: quem esta na aula 15 ja teve as 14 antes.
    // Os stamps e a barra do material ja tratavam assim desde 24/07/2026 (maxCompleted),
    // mas o BANCO guardava so as marcadas — e os paineis (controle-aulas, roster-status,
    // roster_dashboard) CONTAM LINHAS. O resultado era os dois discordarem: a Maria
    // Claudia aparecia com 7/60 no material dela e "3 concluidas" no painel, porque a
    // professora so marcou 1, 2 e 7. Marcar a 15 depois de meses sem marcar mostraria
    // "1 concluida" no painel.
    //
    // Consertar aqui, na ESCRITA, e o que faz todo consumidor concordar sozinho —
    // inclusive os que ainda nao existem. Consertar cada painel para usar max() em vez
    // de contar exigiria que todo consumidor novo lembrasse da regra.
    //
    // SAO DOIS UPSERTS, e a separacao e proposital.
    //
    // O upsert do PostgREST atualiza as colunas QUE ESTAO no payload. Se as anteriores
    // fossem no mesmo lote com `inclass_marked_at: null`, esse null SOBRESCREVERIA a
    // data real de uma aula que a professora marcou de verdade meses atras — o
    // historico de quando cada aula foi dada iria embora.
    //
    // Entao: a aula N vai com o timestamp; as anteriores vao SEM a coluna de data, o
    // que deixa intacto o que ja estiver la (e nasce null nas que nao existiam — elas
    // foram INFERIDAS, nao marcadas, e e correto que nao tenham data).
    var anteriores = [];
    for (var i = 1; i < lessonNum; i++) {
      anteriores.push({ student_slug: slug, lesson_number: i, inclass_done: true });
    }
    if (anteriores.length) {
      supabase.from('lesson_progress')
        .upsert(anteriores, { onConflict: 'student_slug,lesson_number' })
        .then(function(r) {
          if (r.error) console.error('lesson-progress backfill error:', r.error.message);
          else console.log('lesson-progress: aulas 1-' + (lessonNum - 1) + ' marcadas por inferencia');
        });
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
        maxCompleted = 0;
        res.data.forEach(function(row) {
          if (row.inclass_done) {
            completedLessons++;
            completedSet[row.lesson_number] = true;
            if (row.lesson_number > maxCompleted) maxCompleted = row.lesson_number;
          }
        });
        console.log('lesson-progress: ' + completedLessons + ' aulas concluídas de ' + totalAulas);
        // Restore visual checks on professor pages
        document.querySelectorAll('.check-grid, .check-list').forEach(function(grid) {
          var slide = grid.closest('.slide');
          var lessonNum = detectLesson(slide);
          if (!lessonNum && grid.dataset.lesson) lessonNum = parseInt(grid.dataset.lesson);
          if (!lessonNum) lessonNum = lessonFromFilename();
          if (lessonNum && completedSet[lessonNum]) {
            grid.querySelectorAll('.check-item').forEach(function(item) {
              item.classList.add('checked');
            });
          }
        });
        // NUNCA REGREDIR: se este load vier com menos do que já vimos (rede/partial),
        // mantém o maior já conhecido (cache local). Progresso nunca anda pra trás — nem
        // a barra, nem os stamps. Só sobe. (Ordem do Dan 24/07/2026.)
        try {
          var prevCache = JSON.parse(localStorage.getItem(slug + '-global-progress') || 'null');
          if (prevCache && typeof prevCache.completed === 'number' && prevCache.completed > maxCompleted) {
            maxCompleted = prevCache.completed;
          }
        } catch(e) {}
        var denom = totalAulas > 0 ? totalAulas : 1;
        // CUMULATIVO (decisão Dan 24/07/2026): barra e texto refletem a MAIOR aula
        // concluída, não a CONTAGEM. Aluno que fez 1,2,7 está "na aula 7" -> barra 7/N,
        // stamps 1..7 acesos. completedLessons segue só para o log de diagnóstico.
        packagePct = Math.min(100, Math.round(maxCompleted / denom * 100));
        packageCompleted = maxCompleted;
        packageLoaded = true;
        applyPackageProgress();
        try { localStorage.setItem(slug + '-global-progress', JSON.stringify({ completed: maxCompleted, total: totalAulas, pct: packagePct })); } catch(e) {}
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
