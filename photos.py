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


def dims(base, w=900):
    m = MANIFEST.get(base)
    if not m:
        return (900, 900)
    if w == 900:
        return (m["w"], m["h"])
    k = 1600 / max(m["w"], m["h"])
    return (round(m["w"] * k), round(m["h"] * k))


SPECJALNE = {
    # base: (plik 900, plik duży, szerokość, wysokość, opis)
    "bus": ("img/bus-900.webp", "img/bus-1400.webp", 900, 675,
            "Samochód firmowy z logo i numerem telefonu"),
}


def img_special(key, lazy=True, cls="", sizes=None):
    s900, sbig, w, h, alt = SPECJALNE[key]
    load = ' loading="lazy" decoding="async"' if lazy else ' fetchpriority="high" decoding="async"'
    sz = f' sizes="{sizes}"' if sizes else ""
    c = f' class="{cls}"' if cls else ""
    return (f'<img{c} src="{s900}" srcset="{s900} 900w, {sbig} 1400w"{sz}'
            f' width="{w}" height="{h}" alt="{alt}"{load}>')


def img(base, w=900, cls="", lazy=True, sizes=None):
    """Zdjęcie z srcset (900/1600) i wymiarami."""
    ww, hh = dims(base, w)
    load = ' loading="lazy" decoding="async"' if lazy else ' fetchpriority="high" decoding="async"'
    sz = f' sizes="{sizes}"' if sizes else ""
    c = f' class="{cls}"' if cls else ""
    return (f'<img{c} src="img/{base}-900.webp" srcset="img/{base}-900.webp 900w, img/{base}-1600.webp 1600w"{sz}'
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
    src2, w2, src1, w1, alt = duzy[base]
    tekst = alt or opis(base)
    return (f'<img src="{src1}" srcset="{src1} {w1}w, {src2} {w2}w" sizes="100vw" '
            f'width="{w2}" height="{int(w2 * 0.38)}" alt="{tekst}" fetchpriority="high" decoding="async">')


def zoom_fig(base, cls=""):
    """Kafel galerii otwierany w powiększeniu."""
    ww, hh = dims(base)
    c = f' class="{cls}"' if cls else ""
    return (f'<figure{c} data-zoom="img/{base}-1600.webp" data-alt="{opis(base)}" data-cap="{opis(base)}" tabindex="0">'
            f'{img(base)}<figcaption>{opis(base)}</figcaption></figure>')


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
