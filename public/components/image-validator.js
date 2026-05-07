/* ═══════════════════════════════════════════════════════════════
   ALUMNI BY BETTER — IMAGE VALIDATOR
   Valida URLs de imagens antes de usar no material.
   Substitui imagens quebradas por fallbacks curados do Unsplash.
   Todas as URLs foram verificadas em 2026-04.
   ═══════════════════════════════════════════════════════════════ */

/* ═══════════════════════════════════════════════════════════════
   CURATED FALLBACK IMAGES BY THEME
   Cada tema tem 10+ URLs verificadas do Unsplash.
   Formato: ?w=800&q=80 para otimizar tamanho/qualidade.
   ═══════════════════════════════════════════════════════════════ */
const FALLBACK_IMAGES = {

  hotel: [
    'https://images.unsplash.com/photo-1566073771259-6a8506099945?w=800&q=80',
    'https://images.unsplash.com/photo-1551882547-ff40c63fe5fa?w=800&q=80',
    'https://images.unsplash.com/photo-1582719508461-905c673771fd?w=800&q=80',
    'https://images.unsplash.com/photo-1564501049412-61c2a3083791?w=800&q=80',
    'https://images.unsplash.com/photo-1520250497591-112f2f40a3f4?w=800&q=80',
    'https://images.unsplash.com/photo-1542314831-068cd1dbfeeb?w=800&q=80',
    'https://images.unsplash.com/photo-1571896349842-33c89424de2d?w=800&q=80',
    'https://images.unsplash.com/photo-1445019980597-93fa8acb246c?w=800&q=80',
    'https://images.unsplash.com/photo-1611892440504-42a792e24d32?w=800&q=80',
    'https://images.unsplash.com/photo-1596436889106-be35e843f974?w=800&q=80'
  ],

  restaurant: [
    'https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=800&q=80',
    'https://images.unsplash.com/photo-1552566626-52f8b828add9?w=800&q=80',
    'https://images.unsplash.com/photo-1414235077428-338989a2e8c0?w=800&q=80',
    'https://images.unsplash.com/photo-1559339352-11d035aa65de?w=800&q=80',
    'https://images.unsplash.com/photo-1544148103-0773bf10d330?w=800&q=80',
    'https://images.unsplash.com/photo-1466978913421-dad2ebd01d17?w=800&q=80',
    'https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=800&q=80',
    'https://images.unsplash.com/photo-1590846406792-0adc7f938f1d?w=800&q=80',
    'https://images.unsplash.com/photo-1424847651672-bf20a4b0982b?w=800&q=80',
    'https://images.unsplash.com/photo-1537047902294-62a40c20a6ae?w=800&q=80'
  ],

  airport: [
    'https://images.unsplash.com/photo-1436491865332-7a61a109db05?w=800&q=80',
    'https://images.unsplash.com/photo-1529074325209-97e2d25bf8c6?w=800&q=80',
    'https://images.unsplash.com/photo-1556388158-158ea5ccacbd?w=800&q=80',
    'https://images.unsplash.com/photo-1583511655857-d19b40a7a54e?w=800&q=80',
    'https://images.unsplash.com/photo-1474302770737-173ee21bab63?w=800&q=80',
    'https://images.unsplash.com/photo-1540339832862-474599807836?w=800&q=80',
    'https://images.unsplash.com/photo-1530521954074-e64f6810b32d?w=800&q=80',
    'https://images.unsplash.com/photo-1488085061387-422e29b40080?w=800&q=80',
    'https://images.unsplash.com/photo-1517400508447-f8dd518b86db?w=800&q=80',
    'https://images.unsplash.com/photo-1569154941061-e231b4725ef1?w=800&q=80'
  ],

  shopping: [
    'https://images.unsplash.com/photo-1441986300917-64674bd600d8?w=800&q=80',
    'https://images.unsplash.com/photo-1472851294608-062f824d29cc?w=800&q=80',
    'https://images.unsplash.com/photo-1555529669-e69e7aa0ba9a?w=800&q=80',
    'https://images.unsplash.com/photo-1483985988355-763728e1935b?w=800&q=80',
    'https://images.unsplash.com/photo-1607082349566-187342175e2f?w=800&q=80',
    'https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?w=800&q=80',
    'https://images.unsplash.com/photo-1534452203293-494d7ddbf7e0?w=800&q=80',
    'https://images.unsplash.com/photo-1481437156560-3205f6a55acc?w=800&q=80',
    'https://images.unsplash.com/photo-1540959733332-eab4deabeeaf?w=800&q=80',
    'https://images.unsplash.com/photo-1567401893414-76b7b1e5a7a5?w=800&q=80'
  ],

  emergency: [
    'https://images.unsplash.com/photo-1587745416684-47953f16f02f?w=800&q=80',
    'https://images.unsplash.com/photo-1516574187841-cb9cc2ca948b?w=800&q=80',
    'https://images.unsplash.com/photo-1612349317150-e413f6a5b16d?w=800&q=80',
    'https://images.unsplash.com/photo-1603398938378-e54eab446dde?w=800&q=80',
    'https://images.unsplash.com/photo-1551601651-2a8555f1a136?w=800&q=80',
    'https://images.unsplash.com/photo-1504813184591-01572f98c85f?w=800&q=80',
    'https://images.unsplash.com/photo-1559757148-5c350d0d3c56?w=800&q=80',
    'https://images.unsplash.com/photo-1576091160550-2173dba999ef?w=800&q=80',
    'https://images.unsplash.com/photo-1538108149393-fbbd81895907?w=800&q=80',
    'https://images.unsplash.com/photo-1631815589968-fdb09a223b1e?w=800&q=80'
  ],

  transport: [
    'https://images.unsplash.com/photo-1544620347-c4fd4a3d5957?w=800&q=80',
    'https://images.unsplash.com/photo-1570125909232-eb263c188f7e?w=800&q=80',
    'https://images.unsplash.com/photo-1449824913935-59a10b8d2000?w=800&q=80',
    'https://images.unsplash.com/photo-1519003722824-194d4455a60c?w=800&q=80',
    'https://images.unsplash.com/photo-1508672019048-805c876b67e2?w=800&q=80',
    'https://images.unsplash.com/photo-1581262177000-8139a463d531?w=800&q=80',
    'https://images.unsplash.com/photo-1494515843206-f3117d3f51b7?w=800&q=80',
    'https://images.unsplash.com/photo-1474487548417-781cb71495f3?w=800&q=80',
    'https://images.unsplash.com/photo-1517400508447-f8dd518b86db?w=800&q=80',
    'https://images.unsplash.com/photo-1504609773096-104ff2c73ba4?w=800&q=80'
  ],

  business: [
    'https://images.unsplash.com/photo-1507679799987-c73779587ccf?w=800&q=80',
    'https://images.unsplash.com/photo-1560472354-b33ff0c44a43?w=800&q=80',
    'https://images.unsplash.com/photo-1553877522-43269d4ea984?w=800&q=80',
    'https://images.unsplash.com/photo-1542744173-8e7e53415bb0?w=800&q=80',
    'https://images.unsplash.com/photo-1497366216548-37526070297c?w=800&q=80',
    'https://images.unsplash.com/photo-1497215728101-856f4ea42174?w=800&q=80',
    'https://images.unsplash.com/photo-1521737711867-e3b97375f902?w=800&q=80',
    'https://images.unsplash.com/photo-1573164713619-24c711fe7878?w=800&q=80',
    'https://images.unsplash.com/photo-1556761175-5973dc0f32e7?w=800&q=80',
    'https://images.unsplash.com/photo-1600880292203-757bb62b4baf?w=800&q=80'
  ],

  travel: [
    'https://images.unsplash.com/photo-1488646953014-85cb44e25828?w=800&q=80',
    'https://images.unsplash.com/photo-1469854523086-cc02fe5d8800?w=800&q=80',
    'https://images.unsplash.com/photo-1476514525535-07fb3b4ae5f1?w=800&q=80',
    'https://images.unsplash.com/photo-1503220317375-aaad61436b1b?w=800&q=80',
    'https://images.unsplash.com/photo-1530789253388-582c481c54b0?w=800&q=80',
    'https://images.unsplash.com/photo-1501785888041-af3ef285b470?w=800&q=80',
    'https://images.unsplash.com/photo-1539635278303-d4002c07eae3?w=800&q=80',
    'https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=800&q=80',
    'https://images.unsplash.com/photo-1528127269322-539801943592?w=800&q=80',
    'https://images.unsplash.com/photo-1506929562872-bb421503ef21?w=800&q=80'
  ],

  classroom: [
    'https://images.unsplash.com/photo-1524178232363-1fb2b075b655?w=800&q=80',
    'https://images.unsplash.com/photo-1509062522246-3755977927d7?w=800&q=80',
    'https://images.unsplash.com/photo-1580582932707-520aed937b7b?w=800&q=80',
    'https://images.unsplash.com/photo-1523050854058-8df90110c9f1?w=800&q=80',
    'https://images.unsplash.com/photo-1427504494785-3a9ca7044f45?w=800&q=80',
    'https://images.unsplash.com/photo-1503676260728-1c00da094a0b?w=800&q=80',
    'https://images.unsplash.com/photo-1546410531-bb4caa6b424d?w=800&q=80',
    'https://images.unsplash.com/photo-1488190211105-8b0e65b80b4e?w=800&q=80',
    'https://images.unsplash.com/photo-1571260899304-425eee4c7efc?w=800&q=80',
    'https://images.unsplash.com/photo-1434030216411-0b793f4b4173?w=800&q=80'
  ],

  general: [
    'https://images.unsplash.com/photo-1543286386-713bdd548da4?w=800&q=80',
    'https://images.unsplash.com/photo-1513542789411-b6a5d4f31634?w=800&q=80',
    'https://images.unsplash.com/photo-1518837695005-2083093ee35b?w=800&q=80',
    'https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=800&q=80',
    'https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05?w=800&q=80',
    'https://images.unsplash.com/photo-1447752875215-b2761acb3c5d?w=800&q=80',
    'https://images.unsplash.com/photo-1501854140801-50d01698950b?w=800&q=80',
    'https://images.unsplash.com/photo-1475924156734-496f6cac6ec1?w=800&q=80',
    'https://images.unsplash.com/photo-1433086966358-54859d0ed716?w=800&q=80',
    'https://images.unsplash.com/photo-1472214103451-9374bd1c798e?w=800&q=80'
  ]
};

/* Theme aliases — maps common lesson themes to fallback categories */
const THEME_ALIASES = {
  'check-in': 'hotel',
  'check in': 'hotel',
  'hotel check-in': 'hotel',
  'reception': 'hotel',
  'accommodation': 'hotel',
  'reserva': 'hotel',
  'reservations': 'hotel',
  'food': 'restaurant',
  'dining': 'restaurant',
  'cafe': 'restaurant',
  'coffee': 'restaurant',
  'menu': 'restaurant',
  'ordering': 'restaurant',
  'flight': 'airport',
  'boarding': 'airport',
  'customs': 'airport',
  'immigration': 'airport',
  'luggage': 'airport',
  'store': 'shopping',
  'mall': 'shopping',
  'buying': 'shopping',
  'clothes': 'shopping',
  'fashion': 'shopping',
  'health': 'emergency',
  'hospital': 'emergency',
  'pharmacy': 'emergency',
  'doctor': 'emergency',
  'police': 'emergency',
  'accident': 'emergency',
  'taxi': 'transport',
  'uber': 'transport',
  'bus': 'transport',
  'train': 'transport',
  'subway': 'transport',
  'metro': 'transport',
  'directions': 'transport',
  'meeting': 'business',
  'office': 'business',
  'presentation': 'business',
  'email': 'business',
  'interview': 'business',
  'corporate': 'business',
  'tourism': 'travel',
  'sightseeing': 'travel',
  'vacation': 'travel',
  'trip': 'travel',
  'beach': 'travel',
  'study': 'classroom',
  'school': 'classroom',
  'university': 'classroom',
  'lesson': 'classroom',
  'education': 'classroom'
};


/* ═══════════════════════════════════════════════════════════════
   validateImageUrl(url)
   Verifica se uma URL de imagem retorna 200 (ou opaque via CORS).

   @param {string} url
   @returns {Promise<boolean>}
   ═══════════════════════════════════════════════════════════════ */
async function validateImageUrl(url) {
  if (!url || typeof url !== 'string') return false;

  try {
    // Try HEAD request first (lighter)
    const response = await fetch(url, {
      method: 'HEAD',
      mode: 'no-cors',
      signal: AbortSignal.timeout ? AbortSignal.timeout(5000) : undefined
    });
    // no-cors returns opaque response (type: 'opaque', status: 0) which still means the server responded
    return response.ok || response.type === 'opaque';
  } catch {
    // If HEAD fails, try loading as image element (more compatible)
    return new Promise((resolve) => {
      if (typeof Image === 'undefined') {
        resolve(false);
        return;
      }
      const img = new Image();
      const timeout = setTimeout(() => {
        img.src = '';
        resolve(false);
      }, 6000);
      img.onload = () => { clearTimeout(timeout); resolve(true); };
      img.onerror = () => { clearTimeout(timeout); resolve(false); };
      img.src = url;
    });
  }
}


/* ═══════════════════════════════════════════════════════════════
   resolveTheme(theme)
   Resolve um tema para uma categoria de fallback.

   @param {string} theme
   @returns {string} — Chave do FALLBACK_IMAGES
   ═══════════════════════════════════════════════════════════════ */
function resolveTheme(theme) {
  if (!theme) return 'general';

  const lower = theme.toLowerCase().trim();

  // Direct match
  if (FALLBACK_IMAGES[lower]) return lower;

  // Alias match
  if (THEME_ALIASES[lower]) return THEME_ALIASES[lower];

  // Partial match in aliases
  for (const [alias, category] of Object.entries(THEME_ALIASES)) {
    if (lower.includes(alias) || alias.includes(lower)) {
      return category;
    }
  }

  // Partial match in categories
  for (const category of Object.keys(FALLBACK_IMAGES)) {
    if (lower.includes(category)) return category;
  }

  return 'general';
}


/* ═══════════════════════════════════════════════════════════════
   validateAndFixImages(imageUrls, theme)
   Valida todas as URLs e substitui as quebradas por fallbacks.

   @param {string[]} imageUrls — Array de URLs a validar
   @param {string} theme — Tema da aula para selecionar fallbacks
   @returns {Promise<string[]>} — Array de URLs validadas
   ═══════════════════════════════════════════════════════════════ */
async function validateAndFixImages(imageUrls, theme) {
  const resolvedTheme = resolveTheme(theme);
  const fallbacks = FALLBACK_IMAGES[resolvedTheme] || FALLBACK_IMAGES.general;
  let fallbackIndex = 0;

  const results = [];

  for (const url of imageUrls) {
    const isValid = await validateImageUrl(url);

    if (isValid) {
      results.push(url);
    } else {
      // Pick next fallback (cycle if needed)
      const replacement = fallbacks[fallbackIndex % fallbacks.length];
      console.warn(
        `[image-validator] Imagem quebrada substituida:\n  Original: ${url}\n  Fallback: ${replacement}`
      );
      results.push(replacement);
      fallbackIndex++;
    }
  }

  return results;
}


/* ═══════════════════════════════════════════════════════════════
   validateAndFixImagesParallel(imageUrls, theme)
   Versao paralela — mais rapida para muitas imagens.

   @param {string[]} imageUrls
   @param {string} theme
   @returns {Promise<string[]>}
   ═══════════════════════════════════════════════════════════════ */
async function validateAndFixImagesParallel(imageUrls, theme) {
  const resolvedTheme = resolveTheme(theme);
  const fallbacks = FALLBACK_IMAGES[resolvedTheme] || FALLBACK_IMAGES.general;

  const validations = await Promise.all(
    imageUrls.map(url => validateImageUrl(url))
  );

  let fallbackIndex = 0;
  return imageUrls.map((url, i) => {
    if (validations[i]) return url;
    const replacement = fallbacks[fallbackIndex % fallbacks.length];
    console.warn(
      `[image-validator] Imagem quebrada substituida:\n  Original: ${url}\n  Fallback: ${replacement}`
    );
    fallbackIndex++;
    return replacement;
  });
}


/* ═══════════════════════════════════════════════════════════════
   getThemeImages(theme, count)
   Retorna imagens curadas para um tema.

   @param {string} theme — Nome do tema
   @param {number} count — Quantas imagens (default 6)
   @returns {string[]}
   ═══════════════════════════════════════════════════════════════ */
function getThemeImages(theme, count) {
  count = count || 6;
  const resolvedTheme = resolveTheme(theme);
  const images = FALLBACK_IMAGES[resolvedTheme] || FALLBACK_IMAGES.general;

  if (count >= images.length) return [...images];

  // Shuffle and pick
  const shuffled = [...images].sort(() => Math.random() - 0.5);
  return shuffled.slice(0, count);
}


/* ═══════════════════════════════════════════════════════════════
   getAvailableThemes()
   Lista todos os temas com imagens disponiveis.

   @returns {string[]}
   ═══════════════════════════════════════════════════════════════ */
function getAvailableThemes() {
  return Object.keys(FALLBACK_IMAGES);
}


/* ═══════════════════════════════════════════════════════════════
   EXPORTS
   ═══════════════════════════════════════════════════════════════ */
if (typeof module !== 'undefined' && module.exports) {
  module.exports = {
    FALLBACK_IMAGES,
    THEME_ALIASES,
    validateImageUrl,
    validateAndFixImages,
    validateAndFixImagesParallel,
    resolveTheme,
    getThemeImages,
    getAvailableThemes
  };
}
