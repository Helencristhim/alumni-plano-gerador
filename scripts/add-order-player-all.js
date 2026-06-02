/**
 * add-order-player-all.js
 *
 * Adds the order player CSS + JS to ALL student/professor files
 * that have ordering exercises. Transforms Listen buttons into
 * full audio players with play/pause/seek/skip/speed.
 *
 * Usage: node scripts/add-order-player-all.js [--dry-run]
 */

const fs = require('fs');
const path = require('path');

const DIRS = [
  path.join(__dirname, '..', 'public', 'aluno'),
  path.join(__dirname, '..', 'public', 'professor')
];
const DRY_RUN = process.argv.includes('--dry-run');

const ORDER_PLAYER_CSS = `
/* ORDER PLAYER */
.order-player{background:var(--bg-elevated);border:1px solid var(--border);border-radius:10px;padding:.8rem 1rem;margin-bottom:1rem;max-width:420px}
.op-row{display:flex;align-items:center;gap:.6rem;margin-bottom:.5rem}
.op-play{width:40px;height:40px;border-radius:50%;background:var(--accent);color:#fff;border:none;display:flex;align-items:center;justify-content:center;cursor:pointer;flex-shrink:0;transition:all .2s}
.op-play:hover{opacity:.85}
.op-play svg{width:16px;height:16px;fill:#fff}
.op-skip{width:32px;height:32px;border-radius:50%;background:none;border:1px solid var(--border);color:var(--text-dim);display:flex;align-items:center;justify-content:center;cursor:pointer;font-size:.65rem;font-weight:700;flex-shrink:0;transition:all .2s}
.op-skip:hover{border-color:var(--accent);color:var(--accent)}
.op-seekbar{flex:1;height:6px;background:var(--border);border-radius:3px;cursor:pointer;position:relative;overflow:hidden}
.op-fill{height:100%;background:var(--accent);border-radius:3px;width:0%;transition:width .1s linear}
.op-time{font-size:.7rem;color:var(--text-dim);font-variant-numeric:tabular-nums;white-space:nowrap;min-width:70px;text-align:right}
.op-speed{display:flex;gap:.3rem;margin-top:.4rem}
.op-speed button{padding:.2rem .5rem;border:1px solid var(--border);border-radius:5px;background:var(--bg-card);color:var(--text-dim);font-size:.7rem;font-weight:600;cursor:pointer;font-family:Inter,sans-serif;transition:all .15s}
.op-speed button.active{background:var(--accent);color:#fff;border-color:var(--accent)}`;

const ORDER_PLAYER_JS = `
// ===== ORDER PLAYER (replaces Listen buttons with full player) =====
(function() {
  var orderAudios = {};
  function fmt(s) { var m = Math.floor(s/60); var sec = Math.floor(s%60); return m + ':' + (sec < 10 ? '0' : '') + sec; }

  document.querySelectorAll('button[onclick]').forEach(function(btn) {
    var oc = btn.getAttribute('onclick') || '';
    if (oc.indexOf('speakText') === -1 || oc.indexOf('order') === -1) return;
    var m = oc.match(/speakText\\(['"](\\/\\[[^\\]]+\\])['"]/);
    if (!m) return;
    var key = m[1];
    var src = audioMap[key] || audioMap[key.replace(/\\\\'/g,"'")];
    if (!src) return;

    var player = document.createElement('div');
    player.className = 'order-player';
    player.innerHTML =
      '<div class="op-row">' +
        '<button class="op-skip" onclick="this.parentElement.parentElement._opSkip(-5)" aria-label="Back 5s">&laquo;5</button>' +
        '<button class="op-play" onclick="this.parentElement.parentElement._opToggle()" aria-label="Play">' +
          '<svg viewBox="0 0 24 24"><polygon class="op-icon-play" points="6 3 20 12 6 21 6 3"/><g class="op-icon-pause" style="display:none"><rect x="5" y="3" width="4" height="18"/><rect x="15" y="3" width="4" height="18"/></g></svg>' +
        '</button>' +
        '<button class="op-skip" onclick="this.parentElement.parentElement._opSkip(5)" aria-label="Forward 5s">5&raquo;</button>' +
        '<div class="op-seekbar" onclick="this.parentElement.parentElement._opSeek(event)"><div class="op-fill"></div></div>' +
        '<div class="op-time">0:00 / 0:00</div>' +
      '</div>' +
      '<div class="op-speed">' +
        '<button onclick="this.parentElement.parentElement._opSpeed(0.5,this)">0.5x</button>' +
        '<button onclick="this.parentElement.parentElement._opSpeed(0.75,this)">0.75x</button>' +
        '<button class="active" onclick="this.parentElement.parentElement._opSpeed(1,this)">1x</button>' +
        '<button onclick="this.parentElement.parentElement._opSpeed(1.25,this)">1.25x</button>' +
      '</div>';

    var audio = new Audio(src);
    audio.preload = 'metadata';
    var fill = player.querySelector('.op-fill');
    var timeEl = player.querySelector('.op-time');
    var playIcon = player.querySelector('.op-icon-play');
    var pauseIcon = player.querySelector('.op-icon-pause');
    var speed = 1;

    audio.addEventListener('loadedmetadata', function() { timeEl.textContent = '0:00 / ' + fmt(audio.duration); });
    audio.addEventListener('timeupdate', function() {
      if (audio.duration) {
        fill.style.width = (audio.currentTime / audio.duration * 100) + '%';
        timeEl.textContent = fmt(audio.currentTime) + ' / ' + fmt(audio.duration);
      }
    });
    audio.addEventListener('ended', function() { playIcon.style.display = ''; pauseIcon.style.display = 'none'; });

    player._opToggle = function() {
      if (audio.paused) { audio.playbackRate = speed; audio.play(); playIcon.style.display = 'none'; pauseIcon.style.display = ''; }
      else { audio.pause(); playIcon.style.display = ''; pauseIcon.style.display = 'none'; }
    };
    player._opSkip = function(s) { audio.currentTime = Math.max(0, Math.min(audio.duration || 0, audio.currentTime + s)); };
    player._opSeek = function(e) {
      var bar = player.querySelector('.op-seekbar');
      var pct = (e.clientX - bar.getBoundingClientRect().left) / bar.offsetWidth;
      audio.currentTime = pct * (audio.duration || 0);
    };
    player._opSpeed = function(s, b) {
      speed = s; audio.playbackRate = s;
      player.querySelectorAll('.op-speed button').forEach(function(x) { x.classList.remove('active'); });
      b.classList.add('active');
    };

    btn.parentNode.replaceChild(player, btn);
  });
})();`;

function processFile(filePath, label) {
  const file = path.basename(filePath);
  let html = fs.readFileSync(filePath, 'utf-8');

  // Skip if no ordering exercises
  if (!html.includes('checkOrder')) return false;

  // Skip if already has order player
  if (html.includes('.order-player{') || html.includes('ORDER PLAYER')) return 'already';

  let modified = false;

  // Add CSS before </style>
  const styleEnd = html.lastIndexOf('</style>');
  if (styleEnd !== -1) {
    html = html.substring(0, styleEnd) + ORDER_PLAYER_CSS + '\n</style>' + html.substring(styleEnd + 8);
    modified = true;
  }

  // Add JS before </script> (the LAST main script tag, before lesson-progress.js)
  // Find the </script> that comes before lesson-progress.js or controle-aulas.js
  const progressScript = html.indexOf('<script src="/lib/lesson-progress.js">');
  const controleScript = html.indexOf('<script src="/lib/controle-aulas.js">');
  const activityScript = html.indexOf('<script src="/lib/activity-sync.js">');

  // Find the </script> right before the first lib script
  let insertBefore = -1;
  for (const pos of [progressScript, controleScript, activityScript]) {
    if (pos !== -1 && (insertBefore === -1 || pos < insertBefore)) insertBefore = pos;
  }

  if (insertBefore !== -1) {
    // Find the </script> just before this position
    const scriptEnd = html.lastIndexOf('</script>', insertBefore);
    if (scriptEnd !== -1) {
      html = html.substring(0, scriptEnd) + ORDER_PLAYER_JS + '\n</script>' + html.substring(scriptEnd + 9);
      modified = true;
    }
  } else {
    // Fallback: find last </script> before </body>
    const bodyEnd = html.lastIndexOf('</body>');
    if (bodyEnd !== -1) {
      const scriptEnd = html.lastIndexOf('</script>', bodyEnd);
      if (scriptEnd !== -1) {
        html = html.substring(0, scriptEnd) + ORDER_PLAYER_JS + '\n</script>' + html.substring(scriptEnd + 9);
        modified = true;
      }
    }
  }

  if (modified) {
    if (!DRY_RUN) fs.writeFileSync(filePath, html);
    console.log(`  ${DRY_RUN ? '[DRY] ' : ''}${label}/${file}`);
    return true;
  }
  return false;
}

console.log(DRY_RUN ? '=== DRY RUN ===' : '=== ADDING ORDER PLAYER ===\n');

let total = 0;
let skipped = 0;
for (const dir of DIRS) {
  if (!fs.existsSync(dir)) continue;
  const label = path.basename(dir);
  const files = fs.readdirSync(dir).filter(f => f.endsWith('.html')).sort();
  for (const file of files) {
    const result = processFile(path.join(dir, file), label);
    if (result === true) total++;
    else if (result === 'already') skipped++;
  }
}

console.log(`\nTotal: ${total} updated, ${skipped} already had player`);
