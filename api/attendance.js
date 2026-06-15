/**
 * Proxy de attendance — lê a planilha pública "Aulas utilizadas" (Google Sheets)
 * server-side (evita CORS) e devolve um mapa para o controle-aulas.html.
 *
 * Planilha: https://docs.google.com/spreadsheets/d/1e9pBj4nltJFZWArgYzq7q1CvqQ0rgg2BO3FuhXmtCvo
 *  - Aba 1 (gid 1531060196): Professor | Aluno | Student Card | Email | ... | Pacote(7) | Aulas utilizadas(8) | ... | Status(12)
 *  - Aba 2 (gid 926890008):  Professor | Aluno | Email | ... | Pacote(6) | Aulas utilizadas(7) | ... | Status(11)  (sem coluna Student Card)
 *
 * "Aulas utilizadas" = quantas aulas o aluno efetivamente fez (attendance).
 */

const SHEET_ID = '1e9pBj4nltJFZWArgYzq7q1CvqQ0rgg2BO3FuhXmtCvo';
const TABS = [
  // gid, colunas: name, card (null = aba sem card), used, status
  { gid: '1531060196', name: 1, card: 2, used: 8, status: 12 },
  { gid: '926890008', name: 1, card: null, used: 7, status: 11 }
];

// CSV parser simples com suporte a aspas e quebras de linha dentro de campos
function parseCSV(text) {
  var rows = [], row = [], field = '', inQuotes = false;
  for (var i = 0; i < text.length; i++) {
    var c = text[i];
    if (inQuotes) {
      if (c === '"') {
        if (text[i + 1] === '"') { field += '"'; i++; }
        else inQuotes = false;
      } else field += c;
    } else {
      if (c === '"') inQuotes = true;
      else if (c === ',') { row.push(field); field = ''; }
      else if (c === '\n') { row.push(field); rows.push(row); row = []; field = ''; }
      else if (c === '\r') { /* ignora */ }
      else field += c;
    }
  }
  if (field !== '' || row.length) { row.push(field); rows.push(row); }
  return rows;
}

function normName(s) {
  return (s || '')
    .toString()
    .toLowerCase()
    .normalize('NFD').replace(/[\u0300-\u036f]/g, '')
    .replace(/\t/g, ' ')
    .replace(/\s+/g, ' ')
    .trim();
}

function cardDigits(s) {
  var d = (s || '').toString().replace(/\D/g, '');
  return d || null;
}

async function fetchTab(tab) {
  var url = 'https://docs.google.com/spreadsheets/d/' + SHEET_ID +
    '/gviz/tq?tqx=out:csv&gid=' + tab.gid;
  var r = await fetch(url, { headers: { 'User-Agent': 'Mozilla/5.0' } });
  if (!r.ok) throw new Error('Sheet gid ' + tab.gid + ' HTTP ' + r.status);
  var csv = await r.text();
  if (csv.indexOf('<!DOCTYPE') !== -1 || csv.indexOf('<html') !== -1) {
    throw new Error('Sheet gid ' + tab.gid + ' não está pública (retornou HTML)');
  }
  var rows = parseCSV(csv);
  var out = [];
  for (var i = 0; i < rows.length; i++) {
    var row = rows[i];
    var name = (row[tab.name] || '').trim();
    if (!name || normName(name) === 'alunos') continue;
    var used = (row[tab.used] || '').trim();
    var card = tab.card != null ? (row[tab.card] || '').trim() : '';
    var status = (row[tab.status] || '').trim();
    // só inclui linhas que parecem ter um número de aulas utilizadas
    if (used === '' && !card && !status) continue;
    out.push({ name: name, card: card, used: used, status: status });
  }
  return out;
}

module.exports = async (req, res) => {
  try {
    var results = await Promise.all(TABS.map(fetchTab));
    var students = [].concat.apply([], results);

    var byCard = {};   // dígitos do card -> used
    var byName = {};    // nome normalizado -> used
    for (var i = 0; i < students.length; i++) {
      var s = students[i];
      var dig = cardDigits(s.card);
      if (dig && byCard[dig] === undefined) byCard[dig] = s.used;
      var nn = normName(s.name);
      if (nn && byName[nn] === undefined) byName[nn] = s.used;
    }

    res.setHeader('Cache-Control', 's-maxage=300, stale-while-revalidate=900');
    res.setHeader('Access-Control-Allow-Origin', '*');
    return res.status(200).json({
      ok: true,
      count: students.length,
      byCard: byCard,
      byName: byName
    });
  } catch (e) {
    res.setHeader('Cache-Control', 'no-store');
    return res.status(200).json({ ok: false, error: String(e && e.message || e), byCard: {}, byName: {} });
  }
};
