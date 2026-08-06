#!/usr/bin/env python3
"""Treść poszczególnych stron serwisu."""
from photos import img, img_special, img_pas, zoom_fig, gallery_groups, opis

TEL = "+48 883 602 422"
TEL_E164 = "+48883602422"
MAIL = "stryszykirek@gmail.com"
# adres docelowy: zmiana w jednym miejscu (formularz, przekierowanie po wysłaniu)
SITE = "https://hydraulikchojnice.pl"

USLUGI_12 = [
    "Instalacje wodno-kanalizacyjne",
    "Instalacje C.O",
    "Instalacje ogrzewania podłogowego",
    "Montaż kotłów gazowych",
    "Montaż kotłów na pellet oraz stałopalnych",
    "Montaż pomp ciepła",
    "Montaż instalacji gazowych",
    "Montaż przydomowych oczyszczalni ścieków",
    "Montaż odkurzaczy centralnych",
    "Białe montaże",
    "Przeróbki łazienek",
    "Drobne bądź duże awarie",
]

KAFELKI = [
    ("wod-kan-01", "Montaż instalacji wodno kanalizacyjnych"),
    ("podlogowka-01", "Montaż instalacji C.O oraz ogrzewania podłogowego"),
    ("kotlownia-01", "Montaż kotłów na paliwa stałe, gazowych oraz pomp ciepła"),
    ("gaz-01", "Montaż instalacji gazowych"),
]

PROCES = [
    ("01", "Telefon", "Opisują Państwo zakres prac w swoim domu, a my wspólnie ustalamy termin spotkania na miejscu."),
    ("02", "Wycena", "Cena ustalona na podstawie wyceny jest ceną ostateczną, bez ukrytych kosztów."),
    ("03", "Wykonanie", "Wykonujemy instalacje według wcześniejszych ustaleń, uruchamiamy, konfigurujemy, regulujemy, "
                        "tłumaczymy zasadę działania oraz uczymy użytkowania instalacji."),
    ("04", "Odbiór i gwarancja", "Na wykonaną instalację otrzymują Państwo gwarancję, protokoły z prób szczelności "
                                 "oraz stały kontakt z nami w razie problemów."),
]

MIASTA = ["Chojnice", "Sępólno Krajeńskie", "Kamień Krajeński", "Tuchola", "Człuchów"]

FAQ = [
    ("Ile będzie kosztowała instalacja?",
     "Zakres prac wyceniamy po obejrzeniu miejsca. Cena ustalona po oględzinach jest ceną ostateczną, "
     "po zakończeniu prac nie dochodzą do niej żadne dopłaty."),
    ("Czy wycena jest płatna?",
     "Nie. Przyjazd i wycena są bezpłatne i do niczego nie zobowiązują."),
    ("Kiedy możecie zacząć?",
     "Termin ustalamy przy wycenie i trzymamy się go. Awarie traktujemy priorytetowo i przestawiamy grafik."),
    ("Co dostaję po zakończeniu montażu?",
     "Uruchomioną i wyregulowaną instalację, przeszkolenie z obsługi, gwarancję, protokoły z prób szczelności "
     "oraz stały kontakt z nami."),
    ("Czy dojedziecie do mnie?",
     "Pracujemy w Chojnicach, Sępólnie Krajeńskim, Kamieniu Krajeńskim, Tucholi i Człuchowie, a przy większych "
     "inwestycjach dojeżdżamy w promieniu 100 km."),
    ("Czy macie autoryzację producenta?",
     "Tak. Mamy autoryzację Vaillant na montaż i serwis kotłów gazowych oraz pomp ciepła. Certyfikaty pokazujemy "
     "w zakładce Partner."),
    ("Czy dostanę fakturę?",
     "Tak, na firmę albo na osobę prywatną. Dokument wystawiamy po zakończeniu prac."),
]

# kolejność kadrów w hero: pierwszy widzi każdy, kto wejdzie na stronę
HERO = [
    ("hero-3", "Kotłownia po zakończeniu montażu"),
    ("hero-1", "Ogrzewanie podłogowe, pętle rozłożone przed wylewką"),
    ("hero-2", "Rozdzielacz ogrzewania podłogowego w szafce"),
    ("hero-4", "Węzeł wodomierzowy z zaworami odcinającymi"),
]


WYRAZY_NIEROZDZIELNE = ["wodno-kanalizacyjne", "wodno-kanalizacyjnych", "wodno-kanalizacyjnej", "wod-kan"]


def chron(tekst):
    """Wyraz złożony ma przechodzić do nowej linii w całości, nie pękać po dywizie."""
    for w in WYRAZY_NIEROZDZIELNE:
        tekst = tekst.replace(w, f'<span class="nw">{w}</span>')
    return tekst


# ─────────────────────────── kawałki wspólne ───────────────────────────

def hero_block():
    figs = []
    for i, (base, cap) in enumerate(HERO):
        first = i == 0
        load = ' fetchpriority="high" decoding="async"' if first else ' loading="lazy" decoding="async"'
        figs.append(
            f'      <figure class="{"is-on" if first else ""}" data-cap="{cap}">'
            f'<img src="img/{base}-2000.webp" srcset="img/{base}-1200.webp 1200w, img/{base}-2000.webp 2000w" '
            f'sizes="100vw" width="2000" height="1500" alt="{cap}"{load}></figure>')
    return f"""<section class="hero">
  <div class="hero-media" aria-hidden="true">
{chr(10).join(figs)}
  </div>
  <div class="wrap hero-in">
    <p class="kicker">Chojnice i okolice, 100 km</p>
    <h1>Instalacje C.O, <span class="nw">wodno-kanalizacyjne,</span> gazowe, ogrzewania podłogowego</h1>
    <p class="hero-lead">Dwadzieścia lat pracy przy instalacjach, od domu w budowie po remont łazienki.
      Robimy od pierwszej rury po rozruch i przeszkolenie, w umówionym terminie i za cenę, którą znają Państwo
      przed rozpoczęciem prac.</p>
    <div class="hero-cta">
      <a class="btn btn-1" href="tel:{TEL_E164}">Zadzwoń <span class="num">{TEL}</span></a>
      <a class="btn btn-2" href="kontakt.html">Bezpłatna wycena</a>
    </div>
    <p class="hero-cap"></p>
  </div>
</section>

<section class="strip">
  <div class="strip-in">
    <div class="cell"><span class="k"><span class="big">20</span> lat</span><span class="v">doświadczenia w instalacjach</span></div>
    <div class="cell"><span class="k">Bezpłatna wycena</span><span class="v">przyjazd i pomiar na miejscu</span></div>
    <div class="cell"><span class="k">Cena ostateczna</span><span class="v">ustalona przed startem prac</span></div>
    <div class="cell"><span class="k"><span class="big">100</span> km</span><span class="v">zasięg dojazdu od Chojnic</span></div>
    <div class="cell"><span class="k">Vaillant</span><span class="v">autoryzowany montaż i serwis</span></div>
  </div>
</section>
"""


def cta_block(tytul, tekst):
    return f"""<section class="sec">
  <div class="wrap rv">
    <div class="cta">
      <div>
        <h2>{tytul}</h2>
        <p class="lead">{tekst}</p>
      </div>
      <div class="cta-side">
        <a class="btn btn-1" href="tel:{TEL_E164}">Zadzwoń <span class="num">{TEL}</span></a>
        <a class="btn btn-2" href="kontakt.html">Napisz do nas</a>
      </div>
    </div>
  </div>
</section>
"""


def strona_head(kicker, h1, lead, base):
    """Nagłówek podstrony, opcjonalnie z pasem zdjęciowym pod spodem."""
    pas = ""
    if base:
        tag = img_pas(base)
        tag = tag.replace('<img', '<img style="width:100%;height:100%;object-fit:cover"', 1)
        pas = f"""<div class="wrap-wide rv" style="margin-bottom:clamp(20px,4vw,40px)">
  <figure style="margin:0;overflow:hidden;border-radius:4px;aspect-ratio:21/8;background:#dedad3">
    {tag}
  </figure>
</div>"""
    return f"""<section class="sec sec-tight" style="padding-top:clamp(38px,5vw,64px)">
  <div class="wrap">
    <div class="head">
      <p class="kicker">{kicker}</p>
      <h1 style="font-size:clamp(30px,4.4vw,52px);margin-top:16px">{h1}</h1>
      <p class="lead">{lead}</p>
    </div>
  </div>
</section>
{pas}
"""


# ─────────────────────────── strona główna ───────────────────────────

SCHEMA_FIRMA = """  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Plumber",
    "name": "Usługi Hydrauliczne Ireneusz Stryszyk",
    "description": "Instalacje C.O, wodno-kanalizacyjne, gazowe i ogrzewania podłogowego. Montaż kotłów i pomp ciepła. Chojnice i okolice w promieniu 100 km.",
    "url": "https://hydraulikchojnice.pl/",
    "telephone": "+48883602422",
    "email": "stryszykirek@gmail.com",
    "image": "https://hydraulikchojnice.pl/img/og.jpg",
    "logo": "https://hydraulikchojnice.pl/img/logo.webp",
    "vatID": "PL5611428770",
    "taxID": "5611428770",
    "address": {
      "@type": "PostalAddress",
      "addressLocality": "Chojnice",
      "addressRegion": "pomorskie",
      "addressCountry": "PL"
    },
    "areaServed": [
      {"@type": "City", "name": "Chojnice"},
      {"@type": "City", "name": "Sępólno Krajeńskie"},
      {"@type": "City", "name": "Kamień Krajeński"},
      {"@type": "City", "name": "Tuchola"},
      {"@type": "City", "name": "Człuchów"}
    ],
    "knowsAbout": ["ogrzewanie podłogowe", "instalacje gazowe", "pompy ciepła", "kotły gazowe", "instalacje wodno-kanalizacyjne"],
    "makesOffer": [
      {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Montaż instalacji wodno-kanalizacyjnych"}},
      {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Montaż instalacji C.O i ogrzewania podłogowego"}},
      {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Montaż kotłów gazowych, na pellet i pomp ciepła"}},
      {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Montaż instalacji gazowych"}}
    ]
  }
  </script>
"""


def _schema_faq():
    items = ",\n      ".join(
        '{"@type": "Question", "name": "%s", "acceptedAnswer": {"@type": "Answer", "text": "%s"}}' % (q, a)
        for q, a in FAQ)
    return """  <script type="application/ld+json">
  {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
      %s
  ]}
  </script>
""" % items


def index_body():
    kafelki = "\n".join(
        f'      <a class="tile" href="oferta.html">{img(b, cls="")}'
        f'<span class="cap"><span class="idx">{i:02d}</span><span class="txt">{chron(t)}</span></span></a>'
        for i, (b, t) in enumerate(KAFELKI, start=1))

    kroki = "\n".join(
        f'      <div class="step"><span class="n">{n}</span><h3>{t}</h3><p>{o}</p></div>'
        for n, t, o in PROCES)

    oferta = "\n".join(
        f'      <a href="oferta.html"><span class="n">{i:02d}</span><span class="t">{chron(u)}</span></a>'
        for i, u in enumerate(USLUGI_12, start=1))

    miasta = "\n".join(f'      <span>{m}</span>' for m in MIASTA)

    faq = "\n".join(
        f'    <details><summary>{q}</summary><div class="ans">{a}</div></details>'
        for q, a in FAQ)

    # układ musi domykać się do pełnych rzędów po 4 kolumny, inaczej zostaje dziura
    bento = [
        ("zasobnik-02", "b-tall"), ("wod-kan-05", "b-wide"), ("rozdzielacz-02", ""),
        ("podlogowka-14", "b-wide"), ("sterowanie-02", ""),
    ]
    bento_html = "\n".join(
        f'      <figure class="{c}" data-zoom="img/{b}-1600.webp" data-alt="{opis(b)}" data-cap="{opis(b)}" tabindex="0">'
        f'{img(b)}</figure>' for b, c in bento)

    return f"""{hero_block()}

<section class="sec">
  <div class="wrap">
    <div class="head rv">
      <p class="kicker">Czym się zajmujemy</p>
      <h2>Cztery zakresy, w których pracujemy najczęściej</h2>
      <p class="lead">Instalacje C.O, wodno-kanalizacyjne, gazowe i ogrzewania podłogowego to dla nas codzienność.
        Jeśli szukają Państwo fachowego doradztwa, wykonania od A do Z i wyceny, po której wiadomo, ile instalacja
        będzie kosztować, są Państwo w odpowiednim miejscu.</p>
    </div>
    <div class="tiles rv">
{kafelki}
    </div>
  </div>
</section>

<section class="sec sec-paper">
  <div class="wrap">
    <div class="head rv">
      <p class="kicker">Jak pracujemy</p>
      <h2>Prosty, przewidywalny proces</h2>
      <p class="lead">Cztery kroki od telefonu do odbioru. Na każdym z nich wiedzą Państwo, co się dzieje i ile to kosztuje.</p>
    </div>
    <div class="steps rv">
{kroki}
    </div>
  </div>
</section>

<section class="sec sec-dark">
  <div class="wrap">
    <div class="hidden-layer">
      <div class="rv">
        <p class="kicker">Dlaczego to ważne</p>
        <h2>Najważniejsze zostaje pod jastrychem</h2>
        <p class="lead">Rury w posadzce i w bruzdach ścian znikają na kilkanaście lat. Poprawka po odbiorze
          oznacza skucie wylewki, więc pracujemy tak, żeby żadna poprawka nie była potrzebna. Instalację
          sprawdzamy pod ciśnieniem, zanim przyjedzie ekipa od jastrychu, a Państwo dostają dokumenty z tej próby.</p>
        <ul class="facts">
          <li><span class="lab">Próby</span><span class="val">Protokoły z prób szczelności przekazujemy przy odbiorze</span></li>
          <li><span class="lab">Rozruch</span><span class="val">Uruchomienie, konfiguracja i regulacja instalacji</span></li>
          <li><span class="lab">Obsługa</span><span class="val">Pokazujemy, jak instalacja działa i jak nią sterować</span></li>
          <li><span class="lab">Gwarancja</span><span class="val">Gwarancja na wykonaną pracę i stały kontakt z nami</span></li>
        </ul>
      </div>
      <div class="hl-frames rv">
        <figure data-zoom="img/podlogowka-17-1600.webp" data-alt="{opis('podlogowka-17')}" data-cap="{opis('podlogowka-17')}" tabindex="0">
          {img('podlogowka-17')}<figcaption>przed wylewką</figcaption></figure>
        <figure data-zoom="img/rozdzielacz-01-1600.webp" data-alt="{opis('rozdzielacz-01')}" data-cap="{opis('rozdzielacz-01')}" tabindex="0">
          {img('rozdzielacz-01')}<figcaption>rozdzielacz</figcaption></figure>
        <figure data-zoom="img/wod-kan-04-1600.webp" data-alt="{opis('wod-kan-04')}" data-cap="{opis('wod-kan-04')}" tabindex="0">
          {img('wod-kan-04')}<figcaption>przed zabudową</figcaption></figure>
      </div>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="head rv">
      <p class="kicker">Oferta</p>
      <h2>Od fundamentów po efekt finalny inwestycji</h2>
      <p class="lead">Zakres usług, jakie oferujemy, znajdą Państwo poniżej.</p>
    </div>
    <div class="offer rv">
{oferta}
    </div>
  </div>
</section>

<section class="sec sec-paper">
  <div class="wrap">
    <div class="partner">
      <div class="rv">
        <p class="kicker">Partner</p>
        <h2>Autoryzowany montaż i serwis Vaillant</h2>
        <p class="lead">Montujemy i serwisujemy kotły gazowe oraz pompy ciepła Vaillant. Prowadzimy również
          sprzedaż obu typów urządzeń, więc nie muszą Państwo szukać sprzętu na własną rękę.</p>
        <ul class="checks">
          <li>Montaż oraz serwis kotłów gazowych Vaillant</li>
          <li>Montaż pomp ciepła Vaillant</li>
          <li>Sprzedaż obu typów urządzeń</li>
        </ul>
        <p style="margin-top:26px"><a class="btn btn-3" href="partner.html">Certyfikaty i urządzenia</a></p>
      </div>
      <div class="rv">
        <figure style="margin:0;overflow:hidden;border-radius:4px;background:#dedad3" data-zoom="img/kotlownia-06-1600.webp"
          data-alt="{opis('kotlownia-06')}" data-cap="{opis('kotlownia-06')}" tabindex="0">
          {img('kotlownia-06')}
        </figure>
      </div>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="head rv">
      <p class="kicker">Realizacje</p>
      <h2>Zdjęcia z naszych montaży</h2>
      <p class="lead">Kotłownie, rozdzielacze, ogrzewanie podłogowe i podejścia wod-kan. Zdjęcia z budów,
        na których pracowaliśmy, bez upiększania.</p>
    </div>
    <div class="bento rv">
{bento_html}
    </div>
    <p style="margin-top:28px"><a class="btn btn-3" href="realizacje.html">Zobacz pełną galerię</a></p>
  </div>
</section>

<section class="sec sec-paper">
  <div class="wrap">
    <div class="area">
      <div class="rv">
        <p class="kicker">Obszar działania</p>
        <h2>Dojeżdżamy do Państwa</h2>
        <p class="lead">Pracujemy w Chojnicach i okolicy, a przy większych inwestycjach dojeżdżamy w promieniu
          100 km. Nie wiedzą Państwo, czy dojedziemy? Wystarczy jeden telefon.</p>
        <div class="towns">
{miasta}
          <span class="plus">+ 100 km</span>
        </div>
      </div>
      <div class="rv">
        <figure style="margin:0;overflow:hidden;border-radius:4px;background:#dedad3">
          {img_special('bus')}
        </figure>
      </div>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="head rv">
      <p class="kicker">Częste pytania</p>
      <h2>Dobrze wiedzieć przed rozmową</h2>
    </div>
    <div class="faq rv">
{faq}
    </div>
  </div>
</section>

{cta_block("Planują Państwo instalację? Wycenimy ją za darmo.",
           "Wystarczy telefon albo wiadomość. Przyjedziemy, obejrzymy zakres prac i podamy ostateczną cenę.")}
"""


# ─────────────────────────── oferta ───────────────────────────

OFERTA_OPISY = {
    "Instalacje wodno-kanalizacyjne": "Rozprowadzenie wody i kanalizacji w budowanym domu oraz przeróbki w budynkach, "
                                      "które już stoją. Podejścia pod przybory przygotowujemy pod konkretny projekt łazienki i kuchni.",
    "Instalacje C.O": "Rozprowadzenie centralnego ogrzewania, podejścia grzejnikowe, montaż grzejników i armatury. "
                      "Instalację sprawdzamy pod ciśnieniem przed zakryciem.",
    "Instalacje ogrzewania podłogowego": "Układanie pętli, montaż rozdzielaczy i szafek, podłączenie sterowania. "
                                         "Po zalaniu wylewki instalację uruchamiamy i regulujemy pomieszczenie po pomieszczeniu.",
    "Montaż kotłów gazowych": "Kotły wiszące i stojące, wraz z podłączeniem do instalacji, odprowadzeniem spalin "
                              "i rozruchem. Jako autoryzowany montażysta Vaillant prowadzimy też ich serwis.",
    "Montaż kotłów na pellet oraz stałopalnych": "Montaż kotła, podłączenie do komina i instalacji, uruchomienie "
                                                 "oraz przeszkolenie z obsługi i ustawień.",
    "Montaż pomp ciepła": "Dobór i montaż pompy ciepła wraz z zasobnikiem i automatyką. Montujemy pompy ciepła "
                          "Vaillant, na które mamy szkolenie autoryzacyjne producenta.",
    "Montaż instalacji gazowych": "Wykonanie instalacji gazowej i podłączenie urządzeń. Instalację przygotowujemy do próby "
                                  "szczelności i odbioru.",
    "Montaż przydomowych oczyszczalni ścieków": "Montaż oczyszczalni przy domach bez dostępu do kanalizacji, "
                                                "wraz z rozprowadzeniem i rozruchem.",
    "Montaż odkurzaczy centralnych": "Rozprowadzenie rur i gniazd na etapie budowy oraz montaż jednostki centralnej.",
    "Białe montaże": "Montaż wanien, kabin, umywalek, misek ustępowych i baterii, po zakończeniu prac wykończeniowych.",
    "Przeróbki łazienek": "Zmiana układu podejść wod-kan przy remoncie łazienki, dopasowana do nowego rozmieszczenia przyborów.",
    "Drobne bądź duże awarie": "Przecieki, niedrożna kanalizacja, brak ciepłej wody, awaria kotła. Awarie traktujemy "
                               "priorytetowo i przestawiamy pod nie grafik.",
}


def oferta_body():
    wiersze = []
    for i, u in enumerate(USLUGI_12, start=1):
        wiersze.append(f"""      <div class="step" style="border-right:0;border-bottom:1px solid var(--line);padding:24px 0">
        <span class="n">{i:02d}</span>
        <h3 style="margin:10px 0 8px">{chron(u)}</h3>
        <p style="max-width:78ch">{OFERTA_OPISY[u]}</p>
      </div>""")
    lista = "\n".join(wiersze)

    kafelki = "\n".join(
        f'      <figure class="{c}" data-zoom="img/{b}-1600.webp" data-alt="{opis(b)}" data-cap="{opis(b)}" tabindex="0">'
        f'{img(b)}</figure>'
        for b, c in [("wod-kan-06", "b-wide"), ("kotlownia-03", ""), ("grzejnik-01", ""),
                     ("podlogowka-08", ""), ("zasobnik-03", ""), ("wod-kan-02", "b-wide")])

    return f"""{strona_head("Oferta", "Od fundamentów po efekt finalny inwestycji",
                            "Zakres usług, jakie oferujemy, znajdą Państwo poniżej. Wycena zakresu jest bezpłatna, "
                            "a cena ustalona po obejrzeniu miejsca jest ceną ostateczną.", "wod-kan-05")}

<section class="sec" style="padding-top:0">
  <div class="wrap">
    <div class="rv" style="border-top:1px solid var(--line)">
{lista}
    </div>
  </div>
</section>

<section class="sec sec-paper">
  <div class="wrap">
    <div class="head rv">
      <p class="kicker">Z naszych budów</p>
      <h2>Tak wygląda robota w trakcie</h2>
      <p class="lead">Kilka kadrów z etapu, którego zwykle nikt nie ogląda, bo zaraz potem znika pod tynkiem i wylewką.</p>
    </div>
    <div class="bento rv">
{kafelki}
    </div>
  </div>
</section>

{cta_block("Mają Państwo listę prac do wyceny?",
           "Wystarczy telefon i krótki opis zakresu. Umówimy oględziny i podamy cenę, która się później nie zmieni.")}
"""


# ─────────────────────────── realizacje ───────────────────────────

def realizacje_body():
    sekcje = []
    for tytul, lista in gallery_groups():
        kafle = "\n".join("      " + zoom_fig(b) for b in lista)
        sekcje.append(f"""    <div class="group-head rv">
      <h3>{chron(tytul)}</h3>
      <span class="count">{len(lista)} zdjęć</span>
    </div>
    <div class="mosaic rv">
{kafle}
    </div>""")
    return f"""{strona_head("Realizacje", "Zdjęcia z naszych montaży",
                            "Kotłownie, rozdzielacze, ogrzewanie podłogowe, podejścia <span class=\"nw\">wodno-kanalizacyjne</span> i wentylacja. "
                            "Wszystkie zdjęcia pochodzą z budów, na których pracowaliśmy. Kliknięcie powiększa kadr.",
                            None)}

<section class="sec" style="padding-top:0">
  <div class="wrap">
{chr(10).join(sekcje)}
  </div>
</section>

{cta_block("Chcą Państwo podobną instalację u siebie?",
           "Wystarczy jeden telefon i informacja, na jakim etapie jest budowa. Przyjedziemy obejrzeć zakres prac.")}
"""


# ─────────────────────────── partner ───────────────────────────

def partner_body():
    URZADZENIA = [
        (1, "kotły stojące z zasobnikiem Vaillant"), (2, "pompa ciepła Vaillant"),
        (4, "kocioł wiszący Vaillant"), (5, "kocioł kondensacyjny Vaillant"),
    ]
    urzadzenia = "\n".join(
        f'      <figure data-zoom="img/vaillant-{i:02d}-1600.webp" data-alt="Urządzenie Vaillant, {t}" '
        f'data-cap="{t}" tabindex="0">'
        f'<img src="img/vaillant-{i:02d}-900.webp" srcset="img/vaillant-{i:02d}-900.webp 900w, img/vaillant-{i:02d}-1600.webp 1600w" '
        f'width="900" height="700" alt="Urządzenie Vaillant, {t}" loading="lazy" decoding="async"></figure>'
        for i, t in URZADZENIA)

    # tytuły i daty spisane ze skanów zaświadczeń, kolejność chronologiczna
    CERTYFIKATY = [
        (3, "Kotły gazowe, instalacje, pierwsze uruchomienia", "27 września 2023"),
        (2, "Przeglądy kotłów wydłużające gwarancję", "2 lipca 2024"),
        (1, "Pompy ciepła PCP Split i Monoblok, instalacje", "13 marca 2025"),
    ]
    certy = "\n".join(
        f"""      <figure style="margin:0;background:#fff;border:1px solid var(--line);border-radius:4px;overflow:hidden;cursor:zoom-in"
        data-zoom="img/certyfikat-{i}-1400.webp" data-alt="Zaświadczenie Vaillant, szkolenie autoryzacyjne: {t}"
        data-cap="Szkolenie autoryzacyjne Vaillant, {t}, {d}" tabindex="0">
        <img src="img/certyfikat-{i}-700.webp" width="495" height="700"
          alt="Zaświadczenie Vaillant dla Patryka Stryszyka, szkolenie autoryzacyjne: {t}" loading="lazy" decoding="async">
        <figcaption style="padding:14px 16px;font-family:var(--m);font-size:12px;letter-spacing:.05em;color:var(--ink-2)">
          {t}<br><span style="color:var(--ink-3)">{d}</span></figcaption>
      </figure>"""
        for i, t, d in CERTYFIKATY)

    return f"""{strona_head("Partner", "Autoryzowany montaż i serwis Vaillant",
                            "Pracujemy na urządzeniach Vaillant i mamy autoryzację producenta na ich montaż oraz serwis. "
                            "Dzięki temu sprzęt, gwarancja i przeglądy zostają w jednych rękach.", "vaillant-03")}

<section class="sec" style="padding-top:0">
  <div class="wrap">
    <div class="partner">
      <div class="rv">
        <div class="partner-logo">
          <img src="img/vaillant-logo.webp" width="220" height="58" alt="Logo Vaillant" loading="lazy" decoding="async">
        </div>
        <ul class="checks" style="margin-top:28px">
          <li>Montaż oraz serwis kotłów gazowych Vaillant</li>
          <li>Montaż pomp ciepła Vaillant</li>
          <li>Sprzedaż obu typów urządzeń</li>
        </ul>
      </div>
      <div class="rv">
        <p class="lead" style="margin-top:0">Autoryzacja oznacza, że urządzenie montuje ktoś przeszkolony przez producenta,
          a gwarancja zostaje utrzymana. Kupują Państwo sprzęt u nas albo we własnym zakresie, a my zajmujemy się
          montażem, rozruchem i późniejszymi przeglądami.</p>
        <ul class="facts">
          <li><span class="lab">Montaż</span><span class="val">Kotły gazowe i pompy ciepła, z rozruchem i konfiguracją</span></li>
          <li><span class="lab">Serwis</span><span class="val">Przeglądy okresowe i naprawy urządzeń Vaillant</span></li>
          <li><span class="lab">Sprzedaż</span><span class="val">Dobór i dostawa urządzeń do konkretnego domu</span></li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="sec sec-paper">
  <div class="wrap">
    <div class="head rv">
      <p class="kicker">Co montujemy</p>
      <h2>Urządzenia, na których pracujemy</h2>
      <p class="lead">Kotły kondensacyjne, pompy ciepła i zasobniki ciepłej wody Vaillant.</p>
    </div>
    <div class="devices rv">
{urzadzenia}
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="head rv" style="text-align:center;margin-inline:auto">
      <p class="kicker" style="justify-content:center">Certyfikaty</p>
      <h2>Autoryzacja producenta</h2>
      <p class="lead" style="margin-inline:auto">Zaświadczenia ze szkoleń autoryzacyjnych Vaillant: kotły gazowe,
        przeglądy wydłużające gwarancję i pompy ciepła. Wystawione są na Patryka Stryszyka, który prowadzi
        montaże razem z Ireneuszem.</p>
    </div>
    <div class="rv" style="display:grid;grid-template-columns:repeat(3,1fr);gap:18px;margin-top:40px">
{certy}
    </div>
  </div>
</section>

{cta_block("Planują Państwo kocioł albo pompę ciepła?",
           "Podpowiemy, co ma sens przy Państwa domu i instalacji, i podamy cenę razem z montażem.")}
"""


# ─────────────────────────── o nas ───────────────────────────

def o_nas_body():
    return f"""{strona_head("O nas", "Dwie osoby, dwadzieścia lat przy instalacjach",
                            "Usługi Hydrauliczne Ireneusz Stryszyk to firma z Chojnic. Pracujemy w dwie osoby, "
                            "ojciec i syn, przy instalacjach w domach jednorodzinnych.", "bus")}

<section class="sec" style="padding-top:0">
  <div class="wrap">
    <div class="hidden-layer">
      <div class="rv">
        <h2>Ta sama ekipa od pierwszej rury do odbioru</h2>
        <p class="lead">Instalacje C.O, wodno-kanalizacyjne, gazowe i ogrzewania podłogowego to dla nas codzienność.
          Jeśli oczekują Państwo fachowego doradztwa w tych sprawach, wykonania od A do Z, wykonania w ustalonym
          terminie oraz wyceny, po której wiadomo, ile instalacja będzie kosztować, są Państwo w odpowiednim miejscu.</p>
        <p class="lead">Pracujemy we dwóch, Ireneusz i Patryk. To znaczy, że na budowie są Państwo cały czas z tymi
          samymi ludźmi, a osoba, która wycenia, jest tą samą, która potem kładzie rury i podłącza kocioł.
          Patryk ma autoryzację Vaillant na montaż i serwis kotłów gazowych oraz pomp ciepła.</p>
      </div>
      <div class="hl-frames rv">
        <figure data-zoom="img/kotlownia-05-1600.webp" data-alt="{opis('kotlownia-05')}" data-cap="{opis('kotlownia-05')}" tabindex="0">
          {img('kotlownia-05')}<figcaption>kotłownia po montażu</figcaption></figure>
        <figure data-zoom="img/podlogowka-22-1600.webp" data-alt="{opis('podlogowka-22')}" data-cap="{opis('podlogowka-22')}" tabindex="0">
          {img('podlogowka-22')}<figcaption>podłogówka</figcaption></figure>
        <figure data-zoom="img/wod-kan-03-1600.webp" data-alt="{opis('wod-kan-03')}" data-cap="{opis('wod-kan-03')}" tabindex="0">
          {img('wod-kan-03')}<figcaption>podejścia wod-kan</figcaption></figure>
      </div>
    </div>
  </div>
</section>

<section class="sec sec-dark">
  <div class="wrap">
    <div class="head rv">
      <p class="kicker">Zasady, przy których zostajemy</p>
      <h2>Cztery rzeczy, które są u nas stałe</h2>
    </div>
    <ul class="facts rv" style="margin-top:34px;max-width:96ch">
      <li><span class="lab">Wycena</span><span class="val">Przyjazd i wycena są bezpłatne. Cena po oględzinach jest ceną ostateczną.</span></li>
      <li><span class="lab">Termin</span><span class="val">Termin ustalamy przy wycenie i trzymamy się go.</span></li>
      <li><span class="lab">Odbiór</span><span class="val">Instalację uruchamiamy, regulujemy i tłumaczymy, jak jej używać.</span></li>
      <li><span class="lab">Później</span><span class="val">Gwarancja, protokoły z prób szczelności i stały kontakt, gdy coś się dzieje.</span></li>
    </ul>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="area">
      <div class="rv">
        <p class="kicker">Gdzie pracujemy</p>
        <h2>Chojnice i okolice w promieniu 100 km</h2>
        <p class="lead">Najczęściej jeździmy do Chojnic, Sępólna Krajeńskiego, Kamienia Krajeńskiego, Tucholi
          i Człuchowa. Przy większych inwestycjach dojeżdżamy dalej.</p>
        <div class="towns">
{chr(10).join(f'          <span>{m}</span>' for m in MIASTA)}
          <span class="plus">+ 100 km</span>
        </div>
      </div>
      <div class="rv">
        <figure style="margin:0;overflow:hidden;border-radius:4px;background:#dedad3" data-zoom="img/rekuperacja-01-1600.webp"
          data-alt="{opis('rekuperacja-01')}" data-cap="{opis('rekuperacja-01')}" tabindex="0">
          {img('rekuperacja-01')}
        </figure>
      </div>
    </div>
  </div>
</section>

{cta_block("Budują Państwo dom albo remontują łazienkę?",
           "Wystarczy telefon. Umówimy oględziny, a wycenę dostaną Państwo bez żadnych zobowiązań.")}
"""


# ─────────────────────────── kontakt ───────────────────────────

def kontakt_body():
    return f"""{strona_head("Kontakt", "Porozmawiajmy o Państwa instalacji",
                            "Najszybciej jest zadzwonić. Można też zostawić wiadomość przez formularz, "
                            "wtedy oddzwonimy, gdy zejdziemy z budowy.", "wod-kan-07")}

<section class="sec" style="padding-top:0">
  <div class="wrap">
    <div class="contact">
      <div class="rv">
        <div class="cards">
          <div class="card">
            <span class="lab">Telefon</span>
            <a class="val" href="tel:{TEL_E164}">{TEL}</a>
            <p class="sub">Jeśli nie odbieramy, jesteśmy przy pracy. Proszę spróbować za chwilę albo napisać.</p>
          </div>
          <div class="card">
            <span class="lab">E-mail</span>
            <a class="val" href="mailto:{MAIL}">{MAIL}</a>
            <p class="sub">Można od razu dołączyć rzut albo zdjęcia z budowy.</p>
          </div>
          <div class="card">
            <span class="lab">Adres</span>
            <span class="val">ul. Cypriana Norwida 4<br>89-600 Chojnice</span>
            <p class="sub">Usługi Hydrauliczne Ireneusz Stryszyk, NIP 5611428770, REGON 361632447</p>
          </div>
          <div class="card">
            <span class="lab">Obszar</span>
            <span class="val">Chojnice i 100 km</span>
            <p class="sub">Chojnice, Sępólno Krajeńskie, Kamień Krajeński, Tuchola, Człuchów i dalej.</p>
          </div>
        </div>
      </div>

      <div class="rv">
        <h2 style="font-size:clamp(22px,2.6vw,30px)">Zamów bezpłatną wycenę</h2>
        <p class="lead" style="margin-bottom:26px">Proszę napisać, co jest do zrobienia i na jakim etapie jest budowa.
          Odezwiemy się i umówimy oględziny.</p>
        <form data-form action="https://formsubmit.co/{MAIL}" method="POST">
          <input type="hidden" name="_subject" value="Zapytanie ze strony hydraulikchojnice.pl">
          <input type="hidden" name="_template" value="table">
          <input type="hidden" name="_next" value="{SITE}/dziekujemy.html">
          <input type="hidden" name="_captcha" value="false">
          <div class="hp"><label for="_honey">Proszę zostawić puste</label>
            <input id="_honey" type="text" name="_honey" tabindex="-1" autocomplete="off"></div>
          <div class="form-grid">
            <div class="field full">
              <label for="imie">Imię i nazwisko</label>
              <input id="imie" name="imie" type="text" required autocomplete="name">
            </div>
            <div class="field">
              <label for="telefon">Telefon</label>
              <input id="telefon" name="telefon" type="tel" autocomplete="tel" inputmode="tel">
            </div>
            <div class="field">
              <label for="email">E-mail</label>
              <input id="email" name="email" type="email" autocomplete="email">
            </div>
            <div class="field full">
              <label for="wiadomosc">Co jest do zrobienia?</label>
              <textarea id="wiadomosc" name="wiadomosc" required
                placeholder="Na przykład: dom w budowie pod Chojnicami, do wykonania podłogówka na parterze i kotłownia."></textarea>
            </div>
            <div class="field full">
              <button class="btn btn-1" type="submit" style="border:0;cursor:pointer;font-family:var(--b)">Wyślij zapytanie</button>
              <p class="form-error" role="status" style="font-size:14px;margin-top:6px"></p>
            </div>
          </div>
          <p class="form-note">Formularz służy wyłącznie do kontaktu i nie służy do zawierania umów.
            Podane dane wykorzystamy tylko po to, żeby odpowiedzieć na zapytanie. Szczegóły opisaliśmy
            w <a href="polityka-prywatnosci.html">polityce prywatności</a>.</p>
        </form>
      </div>
    </div>
  </div>
</section>

<section class="sec sec-paper">
  <div class="wrap">
    <div class="head rv">
      <p class="kicker">Zanim Państwo zadzwonią</p>
      <h2>Najczęstsze pytania</h2>
    </div>
    <div class="faq rv">
{chr(10).join(f'    <details><summary>{q}</summary><div class="ans">{a}</div></details>' for q, a in FAQ[:4])}
    </div>
  </div>
</section>
"""


# ─────────────────────────── polityka, podziękowanie, 404 ───────────────────────────

POLITYKA = """<section class="sec">
  <div class="wrap prose">
    <p class="kicker">Dokument</p>
    <h1 style="font-size:clamp(28px,3.6vw,44px);margin-top:16px">Polityka prywatności</h1>
    <p>Dokument opisuje, jakie dane zbieramy przez tę stronę, po co i jak długo je trzymamy.
      Obowiązuje od 5 sierpnia 2026 roku.</p>

    <h2>Kto odpowiada za dane</h2>
    <p>Administratorem danych jest <strong>Usługi Hydrauliczne Ireneusz Stryszyk</strong>,
      ul. Cypriana Norwida 4, 89-600 Chojnice, NIP 5611428770, REGON 361632447.
      Kontakt: <a href="tel:+48883602422">+48 883 602 422</a>,
      <a href="mailto:stryszykirek@gmail.com">stryszykirek@gmail.com</a>.</p>

    <h2>Jakie dane zbieramy</h2>
    <ul>
      <li>Dane z formularza kontaktowego: imię i nazwisko, telefon lub e-mail oraz treść wiadomości.</li>
      <li>Dane, które przekazują Państwo w rozmowie telefonicznej lub mailowej, gdy ustalamy zakres prac.</li>
      <li>Podstawowe dane techniczne zapisywane przez serwer, na którym stoi strona (adres IP, data zapytania).</li>
    </ul>

    <h2>Po co ich używamy</h2>
    <p>Dane z formularza służą wyłącznie do odpowiedzi na zapytanie i przygotowania wyceny.
      Podstawą prawną jest nasz uzasadniony interes, czyli obsługa zapytania osoby, która sama się z nami
      kontaktuje (art. 6 ust. 1 lit. f RODO), a przy zleceniu prac wykonanie umowy (art. 6 ust. 1 lit. b RODO).
      Danych nie używamy do wysyłki reklam ani nie przekazujemy ich firmom trzecim w celach handlowych.</p>

    <h2>Jak długo je trzymamy</h2>
    <ul>
      <li>Zapytania, które nie skończyły się zleceniem: do 12 miesięcy od ostatniego kontaktu.</li>
      <li>Dokumenty związane z wykonanymi pracami: przez okres wymagany przepisami podatkowymi, czyli 5 lat
        licząc od końca roku, w którym wystawiliśmy dokument.</li>
    </ul>

    <h2>Komu powierzamy dane</h2>
    <p>Formularz kontaktowy obsługuje serwis <strong>FormSubmit</strong>, który przekazuje treść wiadomości
      na naszą skrzynkę pocztową. Serwis ma serwery w Stanach Zjednoczonych, więc dane z formularza są
      przesyłane poza Europejski Obszar Gospodarczy. Poczta prowadzona jest w usłudze Gmail
      (Google Ireland Limited). Strona hostowana jest w usłudze GitHub Pages.
      Jeśli wolą Państwo tego uniknąć, wystarczy zadzwonić zamiast wypełniać formularz.</p>

    <h2>Państwa prawa</h2>
    <ul>
      <li>Dostęp do swoich danych i otrzymanie ich kopii.</li>
      <li>Sprostowanie danych, które są nieprawidłowe.</li>
      <li>Usunięcie danych lub ograniczenie ich przetwarzania.</li>
      <li>Sprzeciw wobec przetwarzania opartego na uzasadnionym interesie.</li>
      <li>Skarga do Prezesa Urzędu Ochrony Danych Osobowych, ul. Stawki 2, 00-193 Warszawa.</li>
    </ul>
    <p>Żeby skorzystać z któregokolwiek z tych praw, wystarczy napisać na
      <a href="mailto:stryszykirek@gmail.com">stryszykirek@gmail.com</a> albo zadzwonić.</p>

    <h2>Ciasteczka i statystyki</h2>
    <p>Strona nie używa ciasteczek reklamowych ani narzędzi śledzących. Nie mamy tu Google Analytics,
      piksela Facebooka ani osadzonej mapy Google. Kroje pisma trzymamy na własnym serwerze, więc przeglądarka
      nie łączy się w tle z serwerami zewnętrznymi.</p>

    <h2>Zmiany dokumentu</h2>
    <p>Jeśli zmienimy zakres danych albo narzędzia, zaktualizujemy ten dokument i zmienimy datę na górze strony.</p>
  </div>
</section>
"""

DZIEKUJEMY = """<section class="sec mid">
  <div class="wrap">
    <p class="kicker" style="justify-content:center">Wiadomość wysłana</p>
    <h1 style="margin-top:18px">Dziękujemy, odezwiemy się</h1>
    <p class="lead" style="margin-inline:auto">Zapytanie do nas dotarło. Zwykle odpowiadamy tego samego albo
      następnego dnia roboczego, po zejściu z budowy. Jeśli sprawa jest pilna, prosimy dzwonić.</p>
    <div class="row">
      <a class="btn btn-1" href="tel:+48883602422">Zadzwoń <span class="num">+48 883 602 422</span></a>
      <a class="btn btn-3" href="index.html">Wróć na stronę główną</a>
    </div>
  </div>
</section>
"""

BLAD404 = """<section class="sec mid">
  <div class="wrap">
    <p class="kicker" style="justify-content:center">Błąd 404</p>
    <h1 style="margin-top:18px">Nie ma takiej strony</h1>
    <p class="lead" style="margin-inline:auto">Adres jest nieaktualny albo zawiera literówkę.
      Można wrócić na stronę główną albo od razu zajrzeć do oferty i realizacji.</p>
    <div class="row">
      <a class="btn btn-1" href="index.html">Strona główna</a>
      <a class="btn btn-3" href="oferta.html">Oferta</a>
      <a class="btn btn-3" href="realizacje.html">Realizacje</a>
    </div>
  </div>
</section>
"""


PAGES = [
    {
        "file": "index.html",
        "title": "Hydraulik Chojnice, instalacje C.O, wod-kan i gaz | Stryszyk",
        "desc": "Instalacje C.O, wod-kan, gazowe i ogrzewanie podłogowe. Montaż kotłów i pomp ciepła, "
                "Vaillant. Chojnice i 100 km. Bezpłatna wycena, 20 lat doświadczenia.",
        "prio": "1.0",
        "hero": True,
        "schema": SCHEMA_FIRMA + _schema_faq(),
        "foot": "Instalacje C.O, wodno-kanalizacyjne, gazowe i ogrzewania podłogowego. Dwadzieścia lat pracy "
                "przy instalacjach w domach jednorodzinnych, Chojnice i okolice w promieniu 100 km.",
        "body": index_body(),
    },
    {
        "file": "oferta.html",
        "title": "Oferta, zakres usług hydraulicznych | Hydraulik Chojnice",
        "desc": "Instalacje wod-kan i C.O, ogrzewanie podłogowe, kotły gazowe i na pellet, pompy ciepła, "
                "oczyszczalnie, białe montaże i awarie. Chojnice, wycena bezpłatna.",
        "prio": "0.9",
        "schema": SCHEMA_FIRMA,
        "foot": "Pełen zakres prac instalacyjnych przy budowie domu i remoncie: woda, kanalizacja, ogrzewanie, "
                "gaz oraz montaż urządzeń grzewczych.",
        "body": oferta_body(),
    },
    {
        "file": "realizacje.html",
        "title": "Realizacje, zdjęcia z naszych montaży | Hydraulik Chojnice",
        "desc": "Zdjęcia z naszych budów: kotłownie, rozdzielacze, ogrzewanie podłogowe, podejścia wodno-kanalizacyjne "
                "i wentylacja. Prace wykonane w Chojnicach i okolicy.",
        "prio": "0.8",
        "schema": SCHEMA_FIRMA,
        "foot": "Zdjęcia z budów, na których pracowaliśmy: kotłownie, rozdzielacze, pętle ogrzewania podłogowego "
                "i podejścia wodno-kanalizacyjne.",
        "body": realizacje_body(),
    },
    {
        "file": "partner.html",
        "title": "Montaż i serwis Vaillant | Hydraulik Chojnice, Stryszyk",
        "desc": "Montaż i serwis kotłów gazowych oraz pomp ciepła Vaillant, sprzedaż urządzeń. Certyfikaty "
                "ze szkoleń producenta. Chojnice i okolice.",
        "prio": "0.8",
        "schema": SCHEMA_FIRMA,
        "foot": "Autoryzowany montaż i serwis urządzeń Vaillant: kotły gazowe, pompy ciepła oraz sprzedaż "
                "obu typów urządzeń.",
        "body": partner_body(),
    },
    {
        "file": "o-nas.html",
        "title": "O nas, 20 lat przy instalacjach | Hydraulik Chojnice",
        "desc": "Firma z Chojnic prowadzona przez Ireneusza i Patryka Stryszyków. Dwadzieścia lat pracy "
                "przy instalacjach C.O, wod-kan, gazowych i ogrzewaniu podłogowym.",
        "prio": "0.6",
        "schema": SCHEMA_FIRMA,
        "foot": "Firma rodzinna z Chojnic. Pracujemy we dwóch przy instalacjach w domach jednorodzinnych, "
                "od rozprowadzenia rur po rozruch urządzeń.",
        "body": o_nas_body(),
    },
    {
        "file": "kontakt.html",
        "title": "Kontakt, bezpłatna wycena | Hydraulik Chojnice, Stryszyk",
        "desc": "Telefon +48 883 602 422, e-mail i formularz kontaktowy. Bezpłatna wycena instalacji "
                "w Chojnicach i okolicy do 100 km.",
        "prio": "0.9",
        "schema": SCHEMA_FIRMA,
        "foot": "Kontakt do firmy: telefon, e-mail i formularz zapytania o wycenę instalacji w Chojnicach "
                "oraz w okolicznych miejscowościach.",
        "body": kontakt_body(),
    },
    {
        "file": "polityka-prywatnosci.html",
        "title": "Polityka prywatności | Usługi Hydrauliczne Ireneusz Stryszyk",
        "desc": "Informacja o tym, jakie dane zbiera ta strona, w jakim celu i jak długo są przechowywane.",
        "prio": "0.2",
        "schema": "",
        "foot": "Dokument opisujący zasady przetwarzania danych osób, które kontaktują się z nami przez stronę.",
        "body": POLITYKA,
    },
    {
        "file": "dziekujemy.html",
        "title": "Dziękujemy za wiadomość | Usługi Hydrauliczne Ireneusz Stryszyk",
        "desc": "Potwierdzenie wysłania zapytania przez formularz kontaktowy.",
        "noindex": True,
        "schema": "",
        "foot": "Potwierdzenie, że zapytanie wysłane przez formularz dotarło na naszą skrzynkę.",
        "body": DZIEKUJEMY,
    },
    {
        "file": "404.html",
        "title": "Nie ma takiej strony | Usługi Hydrauliczne Ireneusz Stryszyk",
        "desc": "Strona o podanym adresie nie istnieje.",
        "noindex": True,
        "schema": "",
        "foot": "Strona o wpisanym adresie nie istnieje. Prosimy skorzystać z menu albo wrócić na stronę główną.",
        "body": BLAD404,
    },
]
