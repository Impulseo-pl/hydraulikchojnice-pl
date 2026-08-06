/* Bramka wyglądu: wkleja się do konsoli przeglądarki na gotowej stronie.
   Sprawdza trzy rzeczy, których nie widać w kodzie, a widać na stronie:
   1) czy każdy napis ma wystarczający kontrast wobec tła, na którym leży,
   2) czy tekst nie przykleja się do linii (border) sąsiada,
   3) czy nagłówki nie łamią wyrazów z dywizem i nie zostawiają sieroty.
   Zwraca obiekt z listami problemów. */
(() => {
  const wynik = { kontrast: [], odstepy: [], lamanie: [], podsumowanie: '' };

  const doRGB = (c) => {
    const m = c.match(/[\d.]+/g);
    if (!m) return null;
    return { r: +m[0], g: +m[1], b: +m[2], a: m[3] === undefined ? 1 : +m[3] };
  };
  const jasnosc = ({ r, g, b }) => {
    const f = (v) => { v /= 255; return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4); };
    return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b);
  };
  const kontrast = (a, b) => {
    const L1 = jasnosc(a), L2 = jasnosc(b);
    return (Math.max(L1, L2) + 0.05) / (Math.min(L1, L2) + 0.05);
  };
  /* tło, na którym element faktycznie leży: pierwszy przodek z nieprzezroczystym kolorem */
  const tlo = (el) => {
    let e = el;
    while (e && e !== document.documentElement) {
      const c = doRGB(getComputedStyle(e).backgroundColor);
      if (c && c.a > 0.85) return { kolor: c, zrodlo: e };
      e = e.parentElement;
    }
    return { kolor: { r: 255, g: 255, b: 255, a: 1 }, zrodlo: document.body };
  };
  /* czy pod elementem leży zdjęcie lub gradient (wtedy kontrastu nie liczymy automatem) */
  const naObrazie = (el) => {
    let e = el;
    while (e && e !== document.documentElement) {
      const s = getComputedStyle(e);
      if (s.backgroundImage && s.backgroundImage !== 'none') return true;
      if (e.matches && e.matches('.hero, .tile, .mosaic figure, .bento figure, .hl-frames figure')) return true;
      /* na stronie z pełnoekranowym hero nagłówek leży na zdjęciu, dopóki nie przewiniemy */
      if (e.matches && e.matches('.top') && document.body.classList.contains('hero-page')) return true;
      e = e.parentElement;
    }
    return false;
  };

  /* ── 1. kontrast napisów ── */
  document.querySelectorAll('body *').forEach((el) => {
    const bezposredniTekst = [...el.childNodes]
      .filter((n) => n.nodeType === 3 && n.textContent.trim().length > 1)
      .map((n) => n.textContent.trim()).join(' ');
    if (!bezposredniTekst) return;
    const s = getComputedStyle(el);
    if (s.display === 'none' || s.visibility === 'hidden' || +s.opacity === 0) return;
    if (el.offsetParent === null && s.position !== 'fixed') return;
    if (naObrazie(el)) return;

    const kol = doRGB(s.color);
    const bg = tlo(el);
    if (!kol) return;
    const wsp = kontrast(kol, bg.kolor);
    const px = parseFloat(s.fontSize);
    const gruby = parseInt(s.fontWeight, 10) >= 600;
    const duzy = px >= 24 || (px >= 18.66 && gruby);
    const prog = duzy ? 3 : 4.5;
    if (wsp < prog) {
      wynik.kontrast.push({
        tekst: bezposredniTekst.slice(0, 40),
        element: el.tagName + '.' + String(el.className).slice(0, 24),
        kontrast: wsp.toFixed(2), wymagany: prog, rozmiar: px + 'px',
      });
    }
  });

  /* ── 2. tekst przyklejony do linii ── */
  /* kreska ODDZIELAJĄCA (border z jednej strony, np. między kolumnami) potrzebuje dużo światła,
     bo tekst sąsiada jest tuż obok. RAMKA elementu (border ze wszystkich stron, np. przycisk,
     pigułka) to zamknięta forma i wystarcza jej mniej. */
  const MIN_PION = 24, MIN_POZIOM = 16;
  const MIN_RAMKA_PION = 12, MIN_RAMKA_POZIOM = 7;
  document.querySelectorAll('body *').forEach((el) => {
    const s = getComputedStyle(el);
    if (!el.textContent.trim() || el.offsetHeight < 16) return;
    const bok = (k) => parseFloat(s['border' + k + 'Width']) > 0;
    const ramka = bok('Left') && bok('Right') && bok('Top') && bok('Bottom');
    const pary = ramka
      ? [['Left', MIN_RAMKA_PION], ['Right', MIN_RAMKA_PION], ['Top', MIN_RAMKA_POZIOM], ['Bottom', MIN_RAMKA_POZIOM]]
      : [['Left', MIN_PION], ['Right', MIN_PION], ['Top', MIN_POZIOM], ['Bottom', MIN_POZIOM]];
    pary.forEach(([k, min]) => {
      const bw = parseFloat(s['border' + k + 'Width']);
      const bc = doRGB(s['border' + k + 'Color']);
      if (bw > 0 && bc && bc.a > 0.03) {
        const p = parseFloat(s['padding' + k]);
        const maBezposredniTekst = [...el.childNodes].some((n) => n.nodeType === 3 && n.textContent.trim());
        if (p < min && maBezposredniTekst) {
          wynik.odstepy.push({
            element: el.tagName + '.' + String(el.className).slice(0, 24),
            strona: k.toLowerCase(), padding: p, minimum: min,
            tekst: el.textContent.trim().slice(0, 30),
          });
        }
      }
    });
  });

  /* ── 2b. przyciski w menu: reguła `.nav a` bije `.tel-btn` specyficznością ── */
  document.querySelectorAll('.nav a.tel-btn, .nav a.btn, nav a[class*="btn"]').forEach((el) => {
    const s = getComputedStyle(el);
    const pion = parseFloat(s.paddingTop), poziom = parseFloat(s.paddingLeft);
    if (pion < 10 || poziom < 12) {
      wynik.odstepy.push({
        element: 'PRZYCISK W MENU ' + String(el.className).slice(0, 20),
        strona: 'wewnątrz', padding: pion + '/' + poziom, minimum: '10/12',
        tekst: el.textContent.trim().slice(0, 26) + ' (regula .nav a nadpisuje styl przycisku)',
      });
    }
  });

  /* ── 3. łamanie nagłówków ── */
  document.querySelectorAll('h1, h2, h3').forEach((el) => {
    const t = el.textContent.trim();
    const zakres = document.createRange();
    zakres.selectNodeContents(el);
    const linie = [...zakres.getClientRects()].filter((r) => r.width > 20);
    if (linie.length > 1) {
      const ost = linie[linie.length - 1].width;
      const max = Math.max(...linie.map((r) => r.width));
      if (ost < max * 0.22) {
        wynik.lamanie.push({ typ: 'sierota w ostatniej linii', tekst: t.slice(0, 45) });
      }
    }
    /* wyraz z dywizem bez zabezpieczenia przed pęknięciem */
    [...el.querySelectorAll('*')].concat([el]).forEach(() => {});
    const dywizy = t.match(/\p{L}+-\p{L}+/gu) || [];
    dywizy.forEach((w) => {
      const chroniony = [...el.querySelectorAll('.nw')].some((s) => s.textContent.includes(w));
      if (!chroniony && w.length > 12) {
        wynik.lamanie.push({ typ: 'wyraz z dywizem może pęknąć', tekst: w, w_naglowku: t.slice(0, 40) });
      }
    });
  });

  wynik.podsumowanie = `kontrast: ${wynik.kontrast.length} | odstępy: ${wynik.odstepy.length} | łamanie: ${wynik.lamanie.length}`;
  return wynik;
})();
