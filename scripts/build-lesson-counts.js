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

// Skip non-main files
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
];

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

function run() {
    const files = fs.readdirSync(PROF_DIR).filter(f => f.endsWith('.html') && isMainFile(f));
    const results = [];

    for (const file of files) {
        const slug = file.replace('.html', '');
        const html = fs.readFileSync(path.join(PROF_DIR, file), 'utf-8');
        const lessonCount = countLessons(html);

        if (lessonCount === 0) continue; // skip empty/redirect files

        const name = extractName(html, slug);

        results.push({
            slug,
            name,
            aulasHtml: lessonCount
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
