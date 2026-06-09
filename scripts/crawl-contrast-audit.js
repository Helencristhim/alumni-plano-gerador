/**
 * Puppeteer Contrast Audit Crawler
 *
 * Abre cada página de aluno no navegador, navega pelas abas e slides,
 * e detecta problemas de contraste (texto invisível/ilegível).
 *
 * Uso: node scripts/crawl-contrast-audit.js
 *
 * Gera relatório em: scripts/contrast-report/
 */

const puppeteer = require('puppeteer');
const fs = require('fs');
const path = require('path');

const BASE_URL = 'https://alumni-plano-gerador.vercel.app';

const delay = ms => new Promise(r => setTimeout(r, ms));
const REPORT_DIR = path.join(__dirname, 'contrast-report');
const SCREENSHOTS_DIR = path.join(REPORT_DIR, 'screenshots');

// Seletores de elementos interativos que costumam ter problema de contraste
const SELECTORS_TO_CHECK = [
  '.comp-q', '.comp-answer',
  '.check-item', '.check-label', '.checklist li',
  '.fill-item', '.fill-item p', '.fill-item label',
  '.error-card', '.error-card p',
  '.oral-item', '.oral-item p',
  '.roleplay-card', '.roleplay-body', '.roleplay-body p', '.roleplay-scenario',
  '.email-card', '.email-card p',
  '.boarding-pass', '.boarding-pass p',
  '.student-id-card', '.student-id-card p',
  '.vocab-card', '.vocab-card-ic',
  '.quiz-option', '.quiz-question',
  '.match-word', '.match-row select',
  '.speech-card', '.speech-phrase',
  '.fill-blank-sentence', '.blank-input',
  '.survival-phrase', '.sp-en', '.sp-pt',
  'h1', 'h2', 'h3', 'h4', 'p', 'span', 'label', 'li', 'td', 'th',
  '.slide-title', '.slide-subtitle',
  '.lesson-number', '.lesson-desc',
  '.info-item', '.info-value', '.info-label',
  '.badge', '.passport-badge',
  'button', '.btn',
];

// Limiar mínimo de contraste (WCAG AA = 4.5:1 para texto normal, 3:1 para large text)
const MIN_CONTRAST_RATIO = 3.0;

function luminance(r, g, b) {
  const [rs, gs, bs] = [r, g, b].map(c => {
    c = c / 255;
    return c <= 0.03928 ? c / 12.92 : Math.pow((c + 0.055) / 1.055, 2.4);
  });
  return 0.2126 * rs + 0.7152 * gs + 0.0722 * bs;
}

function contrastRatio(rgb1, rgb2) {
  const l1 = luminance(rgb1[0], rgb1[1], rgb1[2]);
  const l2 = luminance(rgb2[0], rgb2[1], rgb2[2]);
  const lighter = Math.max(l1, l2);
  const darker = Math.min(l1, l2);
  return (lighter + 0.05) / (darker + 0.05);
}

function parseColor(colorStr) {
  if (!colorStr || colorStr === 'transparent' || colorStr === 'rgba(0, 0, 0, 0)') return null;
  const rgba = colorStr.match(/rgba?\((\d+),\s*(\d+),\s*(\d+)(?:,\s*([\d.]+))?\)/);
  if (rgba) {
    const alpha = rgba[4] !== undefined ? parseFloat(rgba[4]) : 1;
    if (alpha < 0.1) return null; // praticamente transparente
    return [parseInt(rgba[1]), parseInt(rgba[2]), parseInt(rgba[3]), alpha];
  }
  return null;
}

async function getStudentPages() {
  const alunoDir = path.join(__dirname, '..', 'public', 'aluno');
  const files = fs.readdirSync(alunoDir).filter(f => f.endsWith('.html'));
  return files.map(f => ({
    name: f.replace('.html', ''),
    url: `${BASE_URL}/aluno/${f}`
  }));
}

async function checkElementContrast(page, context) {
  return await page.evaluate((selectors, minRatio) => {
    const issues = [];

    function getComputedBg(el) {
      let current = el;
      while (current && current !== document.documentElement) {
        const style = window.getComputedStyle(current);
        const bg = style.backgroundColor;
        if (bg && bg !== 'transparent' && bg !== 'rgba(0, 0, 0, 0)') {
          return bg;
        }
        current = current.parentElement;
      }
      return 'rgb(255, 255, 255)'; // default white
    }

    function parseRgb(str) {
      if (!str) return null;
      const m = str.match(/rgba?\((\d+),\s*(\d+),\s*(\d+)/);
      return m ? [parseInt(m[1]), parseInt(m[2]), parseInt(m[3])] : null;
    }

    function lum(r, g, b) {
      const [rs, gs, bs] = [r, g, b].map(c => {
        c = c / 255;
        return c <= 0.03928 ? c / 12.92 : Math.pow((c + 0.055) / 1.055, 2.4);
      });
      return 0.2126 * rs + 0.7152 * gs + 0.0722 * bs;
    }

    function ratio(c1, c2) {
      const l1 = lum(c1[0], c1[1], c1[2]);
      const l2 = lum(c2[0], c2[1], c2[2]);
      return (Math.max(l1, l2) + 0.05) / (Math.min(l1, l2) + 0.05);
    }

    for (const selector of selectors) {
      const elements = document.querySelectorAll(selector);
      for (const el of elements) {
        // Pular elementos invisíveis ou sem texto
        const rect = el.getBoundingClientRect();
        if (rect.width === 0 || rect.height === 0) continue;
        const style = window.getComputedStyle(el);
        if (style.display === 'none' || style.visibility === 'hidden' || style.opacity === '0') continue;

        const text = el.textContent?.trim();
        if (!text || text.length === 0) continue;

        const fgColor = style.color;
        const bgColor = getComputedBg(el);

        const fg = parseRgb(fgColor);
        const bg = parseRgb(bgColor);

        if (!fg || !bg) continue;

        const r = ratio(fg, bg);

        if (r < minRatio) {
          // Pegar contexto do slide (se estiver em slide mode)
          const slide = el.closest('.slide');
          const slideInfo = slide ? {
            slideNum: slide.dataset?.slide || '?',
            lesson: slide.dataset?.lesson || '?',
            isDark: slide.classList.contains('slide-dark') || slide.classList.contains('dark'),
          } : null;

          issues.push({
            selector: selector,
            text: text.substring(0, 80),
            fgColor: fgColor,
            bgColor: bgColor,
            contrastRatio: Math.round(r * 100) / 100,
            fontSize: style.fontSize,
            slideInfo: slideInfo,
            tagName: el.tagName,
            classes: el.className?.substring?.(0, 100) || '',
            xpath: getXPath(el),
          });
        }
      }
    }

    function getXPath(el) {
      const parts = [];
      let current = el;
      while (current && current !== document.body) {
        let idx = 1;
        let sibling = current.previousElementSibling;
        while (sibling) {
          if (sibling.tagName === current.tagName) idx++;
          sibling = sibling.previousElementSibling;
        }
        parts.unshift(`${current.tagName.toLowerCase()}[${idx}]`);
        current = current.parentElement;
      }
      return '/' + parts.join('/');
    }

    return issues;
  }, SELECTORS_TO_CHECK, MIN_CONTRAST_RATIO);
}

async function auditPage(browser, pageInfo, allIssues) {
  const page = await browser.newPage();
  await page.setViewport({ width: 1440, height: 900 });

  const studentIssues = {
    name: pageInfo.name,
    url: pageInfo.url,
    tabs: {},
    totalIssues: 0,
  };

  try {
    console.log(`  Abrindo ${pageInfo.name}...`);
    await page.goto(pageInfo.url, { waitUntil: 'networkidle2', timeout: 30000 });
    await delay(1000);

    // 1. Checar tab Pre-class (default)
    console.log(`    Checando Pre-class...`);
    const preClassIssues = await checkElementContrast(page, 'pre-class');
    if (preClassIssues.length > 0) {
      studentIssues.tabs['pre-class'] = preClassIssues;
      studentIssues.totalIssues += preClassIssues.length;
    }

    // 2. Checar se tem tab IN CLASS (aluno geralmente não tem, mas professor sim)
    const hasInClass = await page.evaluate(() => {
      const btn = Array.from(document.querySelectorAll('.tab-btn')).find(b =>
        b.textContent.includes('IN CLASS'));
      return !!btn;
    });

    if (hasInClass) {
      console.log(`    Checando IN CLASS...`);
      await page.evaluate(() => {
        const btn = Array.from(document.querySelectorAll('.tab-btn')).find(b =>
          b.textContent.includes('IN CLASS'));
        if (btn) btn.click();
      });
      await delay(500);

      const inClassIssues = await checkElementContrast(page, 'in-class-menu');
      if (inClassIssues.length > 0) {
        studentIssues.tabs['in-class-menu'] = inClassIssues;
        studentIssues.totalIssues += inClassIssues.length;
      }

      // Tentar entrar em slide mode para cada aula
      const slideButtons = await page.evaluate(() => {
        const buttons = document.querySelectorAll('[onclick*="enterSlideMode"]');
        return Array.from(buttons).map((b, i) => ({
          index: i,
          onclick: b.getAttribute('onclick'),
        }));
      });

      for (const slideBtn of slideButtons) {
        console.log(`    Checando slides (aula ${slideBtn.index + 1})...`);
        try {
          await page.evaluate((onclick) => {
            eval(onclick);
          }, slideBtn.onclick);
          await delay(800);

          // Navegar por todos os slides desta aula
          const totalSlides = await page.evaluate(() => {
            const slides = document.querySelectorAll('.slide');
            return slides.length;
          });

          const slideIssuesAll = [];

          // Checar cada slide (navegando com seta)
          const maxSlides = Math.min(totalSlides, 50); // limit para performance
          for (let s = 0; s < maxSlides; s++) {
            const slideIssues = await checkElementContrast(page, `slide-${s}`);
            if (slideIssues.length > 0) {
              slideIssuesAll.push(...slideIssues);
            }
            // Próximo slide
            await page.keyboard.press('ArrowRight');
            await delay(200);
          }

          if (slideIssuesAll.length > 0) {
            const key = `in-class-aula-${slideBtn.index + 1}`;
            studentIssues.tabs[key] = slideIssuesAll;
            studentIssues.totalIssues += slideIssuesAll.length;
          }

          // Sair do slide mode
          await page.keyboard.press('Escape');
          await delay(500);

        } catch (err) {
          console.log(`      Erro nos slides: ${err.message}`);
        }
      }
    }

    // 3. Checar Complementares
    const hasComplementary = await page.evaluate(() => {
      const btn = Array.from(document.querySelectorAll('.tab-btn')).find(b =>
        b.textContent.includes('Complementar'));
      return !!btn;
    });

    if (hasComplementary) {
      console.log(`    Checando Complementares...`);
      await page.evaluate(() => {
        const btn = Array.from(document.querySelectorAll('.tab-btn')).find(b =>
          b.textContent.includes('Complementar'));
        if (btn) btn.click();
      });
      await delay(500);

      const compIssues = await checkElementContrast(page, 'complementares');
      if (compIssues.length > 0) {
        studentIssues.tabs['complementares'] = compIssues;
        studentIssues.totalIssues += compIssues.length;
      }
    }

    // Screenshot se teve problemas
    if (studentIssues.totalIssues > 0) {
      const screenshotPath = path.join(SCREENSHOTS_DIR, `${pageInfo.name}.png`);
      await page.screenshot({ path: screenshotPath, fullPage: false });
      studentIssues.screenshot = screenshotPath;
    }

  } catch (err) {
    console.log(`  ERRO em ${pageInfo.name}: ${err.message}`);
    studentIssues.error = err.message;
  } finally {
    await page.close();
  }

  allIssues.push(studentIssues);
}

function generateReport(allIssues) {
  // Deduplicate issues por arquivo (mesmo selector+texto = 1 issue)
  for (const student of allIssues) {
    for (const [tab, issues] of Object.entries(student.tabs)) {
      const seen = new Set();
      student.tabs[tab] = issues.filter(issue => {
        const key = `${issue.selector}|${issue.text}|${issue.fgColor}|${issue.bgColor}`;
        if (seen.has(key)) return false;
        seen.add(key);
        return true;
      });
    }
    student.totalIssues = Object.values(student.tabs).reduce((sum, t) => sum + t.length, 0);
  }

  const withIssues = allIssues.filter(s => s.totalIssues > 0);
  const withoutIssues = allIssues.filter(s => s.totalIssues === 0 && !s.error);
  const withErrors = allIssues.filter(s => s.error);

  let md = `# Relatório de Auditoria de Contraste\n\n`;
  md += `**Data:** ${new Date().toLocaleString('pt-BR')}\n`;
  md += `**Total de páginas auditadas:** ${allIssues.length}\n`;
  md += `**Páginas com problemas:** ${withIssues.length}\n`;
  md += `**Páginas OK:** ${withoutIssues.length}\n`;
  md += `**Erros de acesso:** ${withErrors.length}\n\n`;

  md += `---\n\n`;

  // Resumo rápido
  md += `## Resumo\n\n`;
  md += `| Aluno | Problemas | Tabs Afetadas |\n`;
  md += `|-------|-----------|---------------|\n`;
  for (const s of withIssues.sort((a, b) => b.totalIssues - a.totalIssues)) {
    const tabs = Object.keys(s.tabs).join(', ');
    md += `| ${s.name} | ${s.totalIssues} | ${tabs} |\n`;
  }
  md += `\n`;

  // Detalhes por aluno
  md += `## Detalhes\n\n`;
  for (const s of withIssues) {
    md += `### ${s.name}\n\n`;
    md += `URL: ${s.url}\n\n`;

    for (const [tab, issues] of Object.entries(s.tabs)) {
      md += `**${tab}** (${issues.length} problemas):\n\n`;

      // Agrupar por tipo de problema
      const byType = {};
      for (const issue of issues) {
        const key = `${issue.fgColor} sobre ${issue.bgColor} (ratio: ${issue.contrastRatio}:1)`;
        if (!byType[key]) byType[key] = [];
        byType[key].push(issue);
      }

      for (const [type, typeIssues] of Object.entries(byType)) {
        md += `- **${type}**\n`;
        for (const issue of typeIssues.slice(0, 5)) {
          const slideCtx = issue.slideInfo
            ? ` [Slide ${issue.slideInfo.slideNum}, Aula ${issue.slideInfo.lesson}${issue.slideInfo.isDark ? ' DARK' : ''}]`
            : '';
          md += `  - \`${issue.selector}\` "${issue.text.substring(0, 50)}"${slideCtx}\n`;
        }
        if (typeIssues.length > 5) {
          md += `  - ... e mais ${typeIssues.length - 5} elementos\n`;
        }
      }
      md += `\n`;
    }
  }

  // Páginas OK
  if (withoutIssues.length > 0) {
    md += `## Páginas OK (sem problemas detectados)\n\n`;
    for (const s of withoutIssues) {
      md += `- ${s.name}\n`;
    }
    md += `\n`;
  }

  // Erros
  if (withErrors.length > 0) {
    md += `## Erros de Acesso\n\n`;
    for (const s of withErrors) {
      md += `- ${s.name}: ${s.error}\n`;
    }
    md += `\n`;
  }

  return md;
}

async function main() {
  console.log('=== Puppeteer Contrast Audit Crawler ===\n');

  // Criar diretórios
  if (!fs.existsSync(REPORT_DIR)) fs.mkdirSync(REPORT_DIR, { recursive: true });
  if (!fs.existsSync(SCREENSHOTS_DIR)) fs.mkdirSync(SCREENSHOTS_DIR, { recursive: true });

  const pages = await getStudentPages();
  console.log(`Encontradas ${pages.length} páginas de alunos.\n`);

  const browser = await puppeteer.launch({
    headless: 'new',
    args: ['--no-sandbox', '--disable-setuid-sandbox'],
  });

  const allIssues = [];

  // Processar 3 páginas em paralelo para velocidade
  const BATCH_SIZE = 3;
  for (let i = 0; i < pages.length; i += BATCH_SIZE) {
    const batch = pages.slice(i, i + BATCH_SIZE);
    console.log(`\nBatch ${Math.floor(i / BATCH_SIZE) + 1}/${Math.ceil(pages.length / BATCH_SIZE)}:`);
    await Promise.all(batch.map(p => auditPage(browser, p, allIssues)));
  }

  await browser.close();

  // Gerar relatório
  console.log('\n\nGerando relatório...');
  const report = generateReport(allIssues);
  const reportPath = path.join(REPORT_DIR, 'contrast-audit.md');
  fs.writeFileSync(reportPath, report);

  // Salvar JSON para processamento futuro
  const jsonPath = path.join(REPORT_DIR, 'contrast-audit.json');
  fs.writeFileSync(jsonPath, JSON.stringify(allIssues, null, 2));

  // Resumo no console
  const withIssues = allIssues.filter(s => s.totalIssues > 0);
  console.log(`\n=== RESULTADO ===`);
  console.log(`Total auditado: ${allIssues.length}`);
  console.log(`Com problemas: ${withIssues.length}`);
  console.log(`OK: ${allIssues.filter(s => s.totalIssues === 0 && !s.error).length}`);
  console.log(`Erros: ${allIssues.filter(s => s.error).length}`);
  console.log(`\nRelatório salvo em: ${reportPath}`);
  console.log(`JSON salvo em: ${jsonPath}`);

  if (withIssues.length > 0) {
    console.log(`\nAlunos com problemas:`);
    for (const s of withIssues.sort((a, b) => b.totalIssues - a.totalIssues)) {
      console.log(`  - ${s.name}: ${s.totalIssues} problemas`);
    }
  }
}

main().catch(console.error);
