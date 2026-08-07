#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Twarda spacja po jednoliterowym spójniku/przyimku — jedno źródło dla wszystkich stron.

Polska norma składu (PN-83/P-55366; dziś Wolański, „Edycja tekstów", PWN): w wierszach
dłuższych niż 40 znaków nie zostawia się na końcu wiersza wyrazów „a i o u w z", a w tytułach
przyimek MUSI zostać w jednej linii z wyrazem, do którego należy.

DLACZEGO W POTOKU, A NIE W BRAMCE (lekcja 2026-08-07-021): bramka renderowa (`zawisy`) widzi
tylko te zawisy, które wypadły akurat przy szerokości pomiaru. Po naprawieniu ich przy 1440 px,
przy 1280 px zawiśnie coś innego. Twarda spacja w potoku rozwiązuje to na WSZYSTKICH
szerokościach naraz — to szczebel 1 drabiny, bramka przestaje mieć co łapać.

SPRAWDZONE 07.08.2026: w źródle obu opłaconych stron było ZERO wystąpień &nbsp; i ZERO
znaków U+00A0; bramka znalazła 11 zawisów u Stryszyka i 22 u WK Premium przy 1440 px.
"""
import re

_JEDNOLITEROWE = re.compile(r"(?<![\w&-])([aiouwzAIOUWZ]) (?=[\w„(])")
_POZA_ZNACZNIKAMI = re.compile(r"<(script|style)\b[^>]*>.*?</\1\s*>|<[^>]+>", re.S | re.I)


def twarde_spacje(html: str) -> str:
    """Wstawia U+00A0 po jednoliterowym spójniku — TYLKO w tekście widocznym.

    ⚠️ Nie wolno puścić tego na całym pliku jak zamiany myślników: twarda spacja w `href`,
    `src`, nazwie klasy albo w kodzie skryptu psuje stronę. Dlatego przechodzimy dokument
    kawałkami i podmieniamy wyłącznie to, co leży MIĘDZY znacznikami, z pominięciem
    zawartości <script> i <style>.

    Idempotentne: po podmianie stoi tam U+00A0, a wzorzec wymaga zwykłej spacji.
    """
    zamien = lambda m: m.group(1) + " "          # noqa: E731
    if "<" not in html:
        return _JEDNOLITEROWE.sub(zamien, html)
    out, i = [], 0
    for m in _POZA_ZNACZNIKAMI.finditer(html):
        out.append(_JEDNOLITEROWE.sub(zamien, html[i:m.start()]))
        out.append(m.group(0))
        i = m.end()
    out.append(_JEDNOLITEROWE.sub(zamien, html[i:]))
    return "".join(out)
