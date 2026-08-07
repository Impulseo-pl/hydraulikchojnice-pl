#!/usr/bin/env python3
"""Opisy zdjęć i pomocnicze funkcje do wstawiania ich na strony."""
import json, os

ROOT = os.path.dirname(os.path.abspath(__file__))
MANIFEST = {m["base"]: m for m in json.load(open(os.path.join(ROOT, "img/_manifest.json")))}

OPIS = {
    "gaz-01": "Instalacja gazowa doprowadzona do budynku",
    "wod-kan-01": "Podejścia wodno-kanalizacyjne przed zabudową",
    "kotlownia-01": "Kotłownia z kotłem stojącym Vaillant",
    "podlogowka-01": "Pętle ogrzewania podłogowego przed wylewką",
    "kotlownia-02": "Kocioł gazowy i podejścia w kotłowni",
    "kotlownia-03": "Kocioł wiszący po zakończonym montażu",
    "kotlownia-04": "Zasobnik ciepłej wody i rozdzielacz w kotłowni",
    "kotlownia-05": "Kotłownia po zakończeniu prac instalacyjnych",
    "kotlownia-06": "Pompa ciepła Vaillant ze stacją Afriso",
    "wod-kan-02": "Pion kanalizacyjny i rozprowadzenie wody",
    "wod-kan-03": "Podejścia wod-kan w narożniku pomieszczenia",
    "wod-kan-04": "Rozprowadzenie kanalizacji przy posadzce",
    "wod-kan-05": "Rury poprowadzone w bruzdach ściany",
    "wod-kan-06": "Podejścia przygotowane pod baterie i przybory",
    "wod-kan-07": "Węzeł wodomierzowy z zaworami odcinającymi",
    "rozdzielacz-01": "Szafka rozdzielacza ogrzewania podłogowego",
    "rozdzielacz-02": "Rozdzielacz podłączony do pętli w posadzce",
    "rozdzielacz-03": "Rozdzielacz z siłownikami i przewodami sterującymi",
    "grzejnik-01": "Grzejnik łazienkowy podłączony do instalacji",
    "rekuperacja-01": "Kanały wentylacyjne prowadzone w poddaszu",
    "rekuperacja-02": "Izolowane przewody wentylacyjne nad stropem",
    "sterowanie-01": "Termostat pokojowy sterujący ogrzewaniem",
    "sterowanie-02": "Panel sterowania instalacją Vaillant",
    "zasobnik-01": "Zasobnik ciepłej wody w wykończonej łazience",
    "zasobnik-02": "Zasobnik i kocioł w pomieszczeniu technicznym",
    "zasobnik-03": "Naczynie przeponowe i podłączenie zasobnika",
}

_PODLOGOWKA = [
    "Pętle ogrzewania podłogowego przed wylewką",
    "Rozprowadzenie pętli w korytarzu",
    "Ogrzewanie podłogowe w pomieszczeniu na parterze",
    "Pętle poprowadzone wzdłuż ściany zewnętrznej",
    "Podłogówka rozłożona przed wylewką",
    "Pętle doprowadzone do wyjścia na zewnątrz",
    "Pętle w pomieszczeniu z oknem połaciowym",
    "Rozłożone rury podłogówki na folii z siatką",
    "Podłogówka w pomieszczeniu narożnym",
    "Pętle i podejścia grzejnikowe obok siebie",
    "Pętle poprowadzone przez przejście",
    "Podłogówka w wąskim korytarzu",
    "Pętle w pomieszczeniu od strony okien",
    "Ogrzewanie podłogowe przed zalaniem wylewki",
    "Podłogówka rozłożona na całej powierzchni",
    "Pętle zagęszczone przy oknie",
    "Ogrzewanie podłogowe pod skosem dachu",
    "Podłogówka gotowa do zalania",
    "Pętle ułożone wokół przejścia w posadzce",
    "Ogrzewanie podłogowe w mniejszym pomieszczeniu",
    "Podłogówka doprowadzona do drzwi balkonowych",
    "Pętle podłogówki przed wejściem ekipy z jastrychem",
    "Ogrzewanie podłogowe w pomieszczeniu na piętrze",
    "Podłogówka rozłożona przy ścianie działowej",
]
for i, t in enumerate(_PODLOGOWKA, start=1):
    OPIS[f"podlogowka-{i:02d}"] = t


def opis(base):
    return OPIS.get(base, "Instalacja wykonana przez Usługi Hydrauliczne Ireneusz Stryszyk")


# ── deskryptor `w` MUSI wynikać z PLIKU, nie ze stałej docelowej ─────────────
# Lekcja 2026-08-06-005. Skalowanie liczy współczynnik od DŁUŻSZEGO boku, więc kadr
# pionowy zapisany jako „-1600.webp" ma realnie 1200 px szerokości, a deskryptor mówił
# 1600w. Przeglądarka wybiera kandydata WYŁĄCZNIE po deskryptorze — na Retinie liczyła,
# że ma 1600 px, dostawała 1200, i zdjęcie wyglądało miękko. Zmierzone przed poprawką:
# 45 kłamliwych deskryptorów w 36 plikach na tej oddanej, opłaconej stronie.
_ROZMIARY = {}
# kolejność bez znaczenia — i tak sortujemy po realnej szerokości
_WARIANTY = (900, 1400, 1600, 2048, 2400)


def _realne(sciezka):
    """Szerokość i wysokość PLIKU (z dysku), z pamięcią podręczną."""
    p = sciezka if os.path.isabs(sciezka) else os.path.join(ROOT, sciezka)
    if p not in _ROZMIARY:
        from PIL import Image
        with Image.open(p) as im:
            _ROZMIARY[p] = im.size
    return _ROZMIARY[p]


def _kandydaci(base):
    """Lista (ścieżka, szerokość, wysokość) dla wszystkich istniejących wariantów,
    posortowana rosnąco po REALNEJ szerokości."""
    out = []
    for w in _WARIANTY:
        rel = f"img/{base}-{w}.webp"
        if os.path.exists(os.path.join(ROOT, rel)):
            try:
                sz, ws = _realne(rel)
            except Exception:
                continue
            out.append((rel, sz, ws))
    out.sort(key=lambda x: x[1])
    return out


def _srcset(kandydaci):
    return ", ".join(f"{p} {w}w" for p, w, _ in kandydaci)


def srcset_z_plikow(base, maks=1600):
    """Gotowy atrybut srcset dla zdjęć wstawianych ręcznie w pages.py (Vaillant, certyfikaty).
    Deskryptory czytane z dysku — te wpisywane z ręki rozjeżdżały się o 6–27%."""
    kand = [k for k in _kandydaci(base) if k[1] <= maks] or _kandydaci(base)[:1]
    return _srcset(kand)


def dims(base, w=900):
    """Wymiary wariantu o podanej nazwie — czytane z pliku, z manifestu tylko awaryjnie."""
    rel = f"img/{base}-{w}.webp"
    if os.path.exists(os.path.join(ROOT, rel)):
        try:
            return _realne(rel)
        except Exception:
            pass
    m = MANIFEST.get(base)
    if not m:
        return (900, 900)
    if w == 900:
        return (m["w"], m["h"])
    k = w / max(m["w"], m["h"])
    return (round(m["w"] * k), round(m["h"] * k))


SPECJALNE = {
    # base: (plik 900, plik duży, szerokość, wysokość, opis)
    "bus": ("img/bus-900.webp", "img/bus-1400.webp", 900, 675,
            "Samochód firmowy z logo i numerem telefonu"),
}


def img_special(key, lazy=True, cls="", sizes=None):
    s900, sbig, w, h, alt = SPECJALNE[key]
    kand = []
    for rel in (s900, sbig):
        if os.path.exists(os.path.join(ROOT, rel)):
            try:
                sz_, ws_ = _realne(rel)
            except Exception:
                continue
            kand.append((rel, sz_, ws_))
    kand.sort(key=lambda x: x[1])
    if kand:
        w, h = kand[0][1], kand[0][2]
        srcset = _srcset(kand)
        src = kand[0][0]
    else:
        srcset, src = f"{s900} 900w, {sbig} 1400w", s900
    load = ' loading="lazy" decoding="async"' if lazy else ' fetchpriority="high" decoding="async"'
    sz = f' sizes="{sizes}"' if sizes else ""
    c = f' class="{cls}"' if cls else ""
    return (f'<img{c} src="{src}" srcset="{srcset}"{sz}'
            f' width="{w}" height="{h}" alt="{alt}"{load}>')


def img(base, w=900, cls="", lazy=True, sizes=None):
    """Zdjęcie z srcset zbudowanym z REALNYCH szerokości plików.

    ⚠️ Warianty POWYŻEJ 1600 px dokładamy WYŁĄCZNIE, gdy podano `sizes`. Bez `sizes`
    przeglądarka zakłada slot na całą szerokość okna i na Retinie bierze największy
    dostępny plik — czyli kafel galerii 404 px ściągałby zdjęcie 2048 px. Deskryptory
    naprawiamy zawsze, ale nie dokładamy przy okazji ciężaru tam, gdzie nikt nie prosił.
    """
    kand = _kandydaci(base)
    if not sizes:
        kand = [k for k in kand if k[1] <= 1600] or kand[:1]
    if not kand:                                  # awaryjnie: stara ścieżka
        ww, hh = dims(base, w)
        src, srcset = f"img/{base}-900.webp", f"img/{base}-900.webp {ww}w"
    else:
        src, ww, hh = kand[0]
        srcset = _srcset(kand)
    load = ' loading="lazy" decoding="async"' if lazy else ' fetchpriority="high" decoding="async"'
    sz = f' sizes="{sizes}"' if sizes else ""
    c = f' class="{cls}"' if cls else ""
    return (f'<img{c} src="{src}" srcset="{srcset}"{sz}'
            f' width="{ww}" height="{hh}" alt="{opis(base)}"{load}>')


def img_pas(base):
    """Zdjęcie do szerokiego pasa nagłówkowego. Pas ma ~1350 punktów szerokości,
    a na ekranie o gęstości 2x to 2700 pikseli — dlatego podajemy wariant
    w maksymalnej dostępnej rozdzielczości, inaczej kadr wygląda miękko."""
    duzy = {
        "bus": ("img/bus-2400.webp", 2400, "img/bus-1400.webp", 1400,
                "Samochód firmowy z logo i numerem telefonu"),
        "wod-kan-05": ("img/wod-kan-05-2048.webp", 2048, "img/wod-kan-05-1600.webp", 1600, None),
        "wod-kan-07": ("img/wod-kan-07-2048.webp", 2048, "img/wod-kan-07-1600.webp", 1600, None),
        "rozdzielacz-03": ("img/rozdzielacz-03-2048.webp", 2048, "img/rozdzielacz-03-1600.webp", 1600, None),
        "vaillant-03": ("img/vaillant-03-2400.webp", 2400, "img/vaillant-03-1600.webp", 1600,
                        "Kocioł kondensacyjny Vaillant"),
    }
    if base not in duzy:
        return img(base, lazy=False, sizes="100vw")
    src2, _w2, src1, _w1, alt = duzy[base]
    tekst = alt or opis(base)
    # deskryptory z PLIKÓW — te wpisane ręcznie (2048/1600) rozjeżdżały się z realnymi
    kand = []
    for rel in (src1, src2):
        if os.path.exists(os.path.join(ROOT, rel)):
            try:
                sz_, ws_ = _realne(rel)
            except Exception:
                continue
            kand.append((rel, sz_, ws_))
    kand.sort(key=lambda x: x[1])
    if not kand:
        return img(base, lazy=False, sizes="100vw")
    # width/height ZOSTAJĄ w proporcji pasa (0.38) — to rezerwacja miejsca pod baner
    # przycięty w CSS, nie proporcja pliku. Zmiana tego przesunęłaby układ.
    return (f'<img src="{kand[0][0]}" srcset="{_srcset(kand)}" sizes="100vw" '
            f'width="{_w2}" height="{int(_w2 * 0.38)}" alt="{tekst}" '
            f'fetchpriority="high" decoding="async">')


def zoom_fig(base, cls="", lazy=True):
    """Kafel galerii otwierany w powiększeniu.

    `lazy=False` dla PIERWSZEGO kafla na stronie: leniwe ładowanie największego obrazu
    pierwszego ekranu opóźnia moment, w którym strona wygląda na gotową — przeglądarka
    zaczyna go ściągać dopiero po przeliczeniu układu."""
    ww, hh = dims(base)
    c = f' class="{cls}"' if cls else ""
    return (f'<figure{c} data-zoom="img/{base}-1600.webp" data-alt="{opis(base)}" data-cap="{opis(base)}" tabindex="0">'
            f'{img(base, lazy=lazy)}<figcaption>{opis(base)}</figcaption></figure>')


def gallery_groups():
    """Zdjęcia realizacji pogrupowane tematycznie (bez 4 kadrów z kafelków usług)."""
    used_in_tiles = {"gaz-01", "wod-kan-01", "kotlownia-01", "podlogowka-01"}
    grupy = [
        ("Kotłownie i urządzenia", ["kotlownia-05", "kotlownia-06", "kotlownia-04", "kotlownia-02", "kotlownia-03",
                                    "zasobnik-01", "zasobnik-02", "zasobnik-03", "sterowanie-02", "sterowanie-01"]),
        ("Rozdzielacze i ogrzewanie podłogowe", ["rozdzielacz-03", "rozdzielacz-01", "rozdzielacz-02"] +
         [f"podlogowka-{i:02d}" for i in range(2, 25)]),
        ("Instalacje wodno-kanalizacyjne i wentylacja", ["wod-kan-07", "wod-kan-02", "wod-kan-03", "wod-kan-04",
                                                         "wod-kan-05", "wod-kan-06", "grzejnik-01",
                                                         "rekuperacja-01", "rekuperacja-02"]),
    ]
    out = []
    for tytul, lista in grupy:
        lista = [b for b in lista if b in MANIFEST and b not in used_in_tiles]
        out.append((tytul, lista))
    return out
