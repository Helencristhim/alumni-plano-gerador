var fs = require('fs');
var h = fs.readFileSync('public/professor/marlene-landucci.html', 'utf8');
var s = new Set();
var r1 = /speakText\(['"]([^'"]+)['"]/g;
var m;
while ((m = r1.exec(h)) !== null) s.add(m[1]);
var r2 = /data-phrase="([^"]+)"/g;
while ((m = r2.exec(h)) !== null) s.add(m[1]);
var a = new Set();
var r3 = /"([^"]+)":\s*"\/audio\/marlene-landucci\/[^"]+"/g;
while ((m = r3.exec(h)) !== null) a.add(m[1]);
var list = [];
s.forEach(function(p) {
  if (!a.has(p) && !a.has(p.replace(/\.$/, '')) && !a.has(p + '.')) list.push(p);
});
console.log('speakText: ' + s.size + ' | audioMap: ' + a.size + ' | Missing: ' + list.length);
if (list.length > 0) list.forEach(function(p) { console.log('  MISSING: ' + p); });
