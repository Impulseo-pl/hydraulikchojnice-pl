#!/usr/bin/env python3
"""Składa strony serwisu z części wspólnych. Treść stron siedzi w pages.py."""
import json, os, re, sys

# twarda spacja po jednoliterowym spójniku — jedno źródło dla wszystkich stron
# (kopia z ~/.claude/skills/strona-docelowa/rdzen/; poprawki idą DO ŹRÓDŁA)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from typografia import twarde_spacje

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE = "https://hydraulikchojnice.pl"
FIRMA = "Usługi Hydrauliczne Ireneusz Stryszyk"
TEL = "+48 883 602 422"
TEL_E164 = "+48883602422"
MAIL = "stryszykirek@gmail.com"
ADRES = "ul. Cypriana Norwida 4, 89-600 Chojnice"
NIP = "5611428770"
REGON = "361632447"

MENU = [
    ("oferta.html", "Oferta"),
    ("realizacje.html", "Realizacje"),
    ("partner.html", "Partner"),
    ("kontakt.html", "Kontakt"),
]


def head(p):
    """p: słownik strony (file, title, desc, ...)"""
    canonical = SITE + "/" + ("" if p["file"] == "index.html" else p["file"])
    schema = p.get("schema", "")
    noindex = '\n  <meta name="robots" content="noindex, follow">' if p.get("noindex") else ""
    return f"""<!doctype html>
<html lang="pl">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{p['title']}</title>
  <meta name="description" content="{p['desc']}">
  <link rel="canonical" href="{canonical}">{noindex}
  <meta name="theme-color" content="#132f49">
  <meta property="og:type" content="website">
  <meta property="og:locale" content="pl_PL">
  <meta property="og:site_name" content="{FIRMA}">
  <meta property="og:title" content="{p['title']}">
  <meta property="og:description" content="{p['desc']}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="{SITE}/img/og.jpg">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="icon" href="img/favicon.svg" type="image/svg+xml">
  <link rel="icon" href="img/favicon-32.png" sizes="32x32">
  <link rel="apple-touch-icon" href="img/favicon-180.png">
  <link rel="manifest" href="site.webmanifest">
  <link rel="preload" href="assets/fonts/barlow-600-latin.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="preload" href="assets/fonts/inter-latin.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="stylesheet" href="assets/app.css?v=37">
{schema}</head>
<body{' class="hero-page"' if p.get('hero') else ''}>
<a class="skip" href="#main">Przejdź do treści</a>

<header class="top">
  <div class="wrap top-in">
    <a class="brand" href="index.html" aria-label="{FIRMA}, strona główna">
      <img class="logo-dark" src="img/logo.webp" width="155" height="46" alt="Logo Hydraulik Ireneusz Stryszyk">
      <img class="logo-light" src="img/logo-jasne.webp" width="155" height="46" alt="" aria-hidden="true">
    </a>
    <button class="burger" aria-expanded="false" aria-controls="menu" aria-label="Menu">
      <span></span><span></span><span></span>
    </button>
    <nav class="nav" id="menu" aria-label="Menu główne">
      {menu_links(p['file'])}
      <a class="tel-btn" href="tel:{TEL_E164}">Zadzwoń {TEL}</a>
    </nav>
  </div>
</header>

<main id="main">
"""


def menu_links(current):
    out = []
    for href, label in MENU:
        cur = ' aria-current="page"' if href == current else ""
        out.append(f'<a href="{href}"{cur}>{label}</a>')
    return "\n      ".join(out)


def foot(p):
    opis = p.get("foot", "")
    return f"""</main>

<footer class="foot">
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <img class="logo" src="img/logo-jasne.webp" width="149" height="44" alt="Hydraulik Ireneusz Stryszyk">
        <p>{opis}</p>
      </div>
      <div>
        <h4>Na stronie</h4>
        <ul>
          <li><a href="index.html">Strona główna</a></li>
          <li><a href="oferta.html">Oferta</a></li>
          <li><a href="realizacje.html">Realizacje</a></li>
          <li><a href="partner.html">Partner Vaillant</a></li>
          <li><a href="kontakt.html">Kontakt</a></li>
        </ul>
      </div>
      <div>
        <h4>Kontakt</h4>
        <ul>
          <li><a href="tel:{TEL_E164}">{TEL}</a></li>
          <li><a href="mailto:{MAIL}">{MAIL}</a></li>
          <li>{ADRES}</li>
          <li>NIP {NIP}</li>
        </ul>
      </div>
    </div>
    <div class="fine">
      <span>&copy; <span data-year>2026</span> {FIRMA}</span>
      <a href="polityka-prywatnosci.html">Polityka prywatności</a>
      <span class="right">Projekt strony: <a href="https://impulseo.pl" rel="noopener">Impulseo</a></span>
    </div>
  </div>
</footer>

<div class="callbar">
  <a href="tel:{TEL_E164}">Zadzwoń</a>
  <a class="alt" href="kontakt.html">Bezpłatna wycena</a>
</div>

<div class="lb" hidden aria-modal="true" role="dialog" aria-label="Powiększone zdjęcie">
  <button class="lb-x" aria-label="Zamknij">&times;</button>
  <button class="lb-p" aria-label="Poprzednie zdjęcie">&#8249;</button>
  <button class="lb-n" aria-label="Następne zdjęcie">&#8250;</button>
  <img src="" alt="">
  <p class="lb-cap"></p>
</div>

<script src="assets/app.js?v=7"></script>
</body>
</html>
"""


def build():
    sys.path.insert(0, ROOT)
    import pages
    for p in pages.PAGES:
        html = head(p) + p["body"] + foot(p)
        html = html.replace("{menu_links(p['file'])}", menu_links(p["file"]))
        html = twarde_spacje(html)
        with open(os.path.join(ROOT, p["file"]), "w", encoding="utf-8") as f:
            f.write(html)
        print("zapisano", p["file"], len(html) // 1024, "KB")

    # sitemap
    urls = [p for p in pages.PAGES if not p.get("noindex")]
    items = "\n".join(
        f"  <url><loc>{SITE}/{'' if p['file']=='index.html' else p['file']}</loc>"
        f"<changefreq>monthly</changefreq><priority>{p.get('prio','0.7')}</priority></url>"
        for p in urls
    )
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n'
                '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
                + items + "\n</urlset>\n")
    print("zapisano sitemap.xml")


if __name__ == "__main__":
    build()
