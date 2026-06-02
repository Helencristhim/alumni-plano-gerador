/**
 * Replaces the entire ORDER PLAYER JS block in all files
 * with the exact same code that works in Roberto Pires.
 */
const fs = require('fs');
const path = require('path');

const DIRS = [
  path.join(__dirname, '..', 'public', 'aluno'),
  path.join(__dirname, '..', 'public', 'professor')
];

const WORKING_JS = `// ===== ORDER PLAYER (replaces Listen buttons with full player) =====
(function() {
  function fmt(s) { var m = Math.floor(s/60); var sec = Math.floor(s%60); return m + ':' + (sec < 10 ? '0' : '') + sec; }

  document.querySelectorAll('button[onclick]').forEach(function(btn) {
    var oc = btn.getAttribute('onclick') || '';
    if (oc.indexOf('speakText') === -1 || oc.indexOf('order') === -1) return;
    var m = oc.match(/speakText\\(['"](\\/?(\\[[^\\]]+\\]))['"]/);
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

let total = 0;
for (const dir of DIRS) {
  if (!fs.existsSync(dir)) continue;
  for (const file of fs.readdirSync(dir).filter(f => f.endsWith('.html'))) {
    const fp = path.join(dir, file);
    let html = fs.readFileSync(fp, 'utf-8');
    if (!html.includes('ORDER PLAYER')) continue;

    // Extract the old ORDER PLAYER block
    const startMarker = '// ===== ORDER PLAYER';
    const startIdx = html.indexOf(startMarker);
    if (startIdx === -1) continue;

    // Find the end: })(); followed by newline
    const endPattern = '})();';
    let endIdx = html.indexOf(endPattern, startIdx);
    if (endIdx === -1) continue;
    endIdx += endPattern.length;

    const oldBlock = html.substring(startIdx, endIdx);
    html = html.substring(0, startIdx) + WORKING_JS + html.substring(endIdx);

    fs.writeFileSync(fp, html);
    console.log(`Fixed: ${path.basename(dir)}/${file}`);
    total++;
  }
}
console.log(`\nTotal: ${total}`);
