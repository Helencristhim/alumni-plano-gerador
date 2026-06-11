#!/usr/bin/env node
/**
 * build-lesson-counts.js
 * Scans professor HTML files and counts actual lesson cards (id="ex-lesson-N").
 * Outputs /public/data/lesson-counts.json
 * Run: node scripts/build-lesson-counts.js
 */

const fs = require('fs');
const path = require('path');

const PROF_DIR = path.join(__dirname, '..', 'public', 'professor');
const OUT_FILE = path.join(__dirname, '..', 'public', 'data', 'lesson-counts.json');

// Skip non-main files (but track standalone aula files separately)
const SKIP_PATTERNS = [
    /-aula\d/,
    /-backup/,
    /-test/,
    /-v-[ab]/,
    /V2\./,
    /-new-?aula/,
    /-new\./,
    /-listening\./,
    /-palestra\./,
    /-speech-training\./,
    /^helen-mendes\./,  // aluna MOCK (template modelo) — fora do controle
];

const STANDALONE_AULA_RE = /^(.+)-aula(\d+)\.html$/;

function isMainFile(filename) {
    return !SKIP_PATTERNS.some(p => p.test(filename));
}

function countLessons(html) {
    const matches = html.match(/id="ex-lesson-/g);
    return matches ? matches.length : 0;
}

function extractName(html, slug) {
    // Try to get name from <h1> in header
    const h1Match = html.match(/<h1[^>]*>([^<]+)<\/h1>/);
    if (h1Match) return h1Match[1].trim();
    // Fallback: humanize slug
    return slug.split('-').map(w => w.charAt(0).toUpperCase() + w.slice(1)).join(' ');
}

function getStandaloneAulaNumbers(allFiles) {
    // Get standalone aula numbers (-aula2.html, -aula3.html, etc.) per slug
    const aulaNumbers = {};
    for (const file of allFiles) {
        const match = file.match(STANDALONE_AULA_RE);
        if (match) {
            const slug = match[1];
            const num = parseInt(match[2]);
            if (!aulaNumbers[slug]) aulaNumbers[slug] = [];
            aulaNumbers[slug].push(num);
        }
    }
    return aulaNumbers;
}

function getMaxLessonInMain(html) {
    // Find the highest lesson number in id="ex-lesson-N"
    const matches = html.match(/id="ex-lesson-(\d+)"/g);
    if (!matches) return 0;
    let max = 0;
    for (const m of matches) {
        const num = parseInt(m.match(/(\d+)/)[1]);
        if (num > max) max = num;
    }
    return max;
}

function run() {
    const allHtmlFiles = fs.readdirSync(PROF_DIR).filter(f => f.endsWith('.html'));
    const mainFiles = allHtmlFiles.filter(f => isMainFile(f));
    const standaloneAulaNumbers = getStandaloneAulaNumbers(allHtmlFiles);
    const results = [];

    for (const file of mainFiles) {
        const slug = file.replace('.html', '');
        const html = fs.readFileSync(path.join(PROF_DIR, file), 'utf-8');
        const lessonCount = countLessons(html);
        const maxInMain = getMaxLessonInMain(html);

        // Only count standalone aulas with numbers BEYOND what's in the main file
        const standaloneNums = standaloneAulaNumbers[slug] || [];
        const extraStandalone = standaloneNums.filter(n => n > maxInMain).length;
        const totalCount = lessonCount + extraStandalone;

        if (totalCount === 0) continue; // skip empty/redirect files

        const name = extractName(html, slug);

        results.push({
            slug,
            name,
            aulasHtml: totalCount
        });
    }

    results.sort((a, b) => a.name.localeCompare(b.name, 'pt-BR'));

    const output = {
        generatedAt: new Date().toISOString(),
        students: results
    };

    fs.mkdirSync(path.dirname(OUT_FILE), { recursive: true });
    fs.writeFileSync(OUT_FILE, JSON.stringify(output, null, 2));
    console.log(`Generated ${OUT_FILE} with ${results.length} students`);
}

run();
