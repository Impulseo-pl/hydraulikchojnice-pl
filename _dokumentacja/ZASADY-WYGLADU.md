# Zasady wyglądu stron — ściąga do każdej kolejnej strony

Spisane 06.08.2026 przy stronie Stryszyka, po tym jak Krzysztof wyłapał trzy błędy, których nie
widać w kodzie, a widać na ekranie: tekst przyklejony do kreski, nadpis niewidoczny na jasnym tle
i wyraz złożony pęknięty w połowie.

Sprawdzanie automatem: `sprawdz_wyglad.js` — wkleić do konsoli na gotowej stronie albo puścić przez
przeglądarkę na wszystkich podstronach. Zwraca listę problemów w trzech kategoriach.

---

## 1. Odstępy: skala i minimum przy liniach

**Skala 8 punktów.** Wszystkie odstępy z ciągu 8, 16, 24, 32, 40, 48, 64. Do drobiazgów (odstęp
etykiety od wartości) wolno zejść do 4. Powód nie jest estetyczny tylko techniczny: popularne
rozdzielczości dzielą się przez 8, więc układ nie rozjeżdża się na ułamki piksela. Tak robi
Material Design, Carbon (IBM), Fluent (Microsoft), Polaris (Shopify) i Primer (GitHub).

**Przestrzeń wokół elementu ≥ przestrzeń wewnątrz niego** (reguła *internal ≤ external*). Jeśli
karta ma 24 px paddingu, to odstęp między kartami ma być co najmniej 24 px. Odwrotna proporcja
sprawia, że elementy zlewają się w jedną plamę.

**Prawo bliskości (Gestalt).** Odstęp wewnątrz grupy musi być wyraźnie mniejszy niż odstęp między
grupami — inaczej oko nie wie, co z czym się łączy. Praktyczna proporcja: 1 : 2 (np. 16 px między
nagłówkiem a akapitem, 32 px między sekcjami).

### Minimum przy kresce — to był błąd na tej stronie

Rozróżniamy dwa przypadki, bo mają inne wymagania:

| Rodzaj linii | Minimum światła | Dlaczego |
|---|---|---|
| **Kreska oddzielająca** (border z jednej strony: kolumny procesu, siatka oferty, lista z liniami) | **24 px** w poziomie, **16 px** w pionie | po drugiej stronie kreski jest tekst sąsiada; przy 16 px litery „przyklejają się" do linii |
| **Ramka elementu** (border ze wszystkich stron: przycisk, pigułka, karta) | **12 px** w poziomie, **7 px** w pionie | forma jest zamknięta, oko czyta ją jako całość |

Skrajne kolumny w rzędzie **nie dostają paddingu od zewnątrz** — mają się wyrównać do krawędzi
kolumny tekstu, inaczej rząd wygląda na wsunięty względem nagłówka nad nim.

---

## 2. Kontrast: każdy napis sprawdzony wobec swojego tła

**Progi WCAG:** tekst zwykły **4,5 : 1**, tekst duży (od 24 px, albo od 18,7 px jeśli pogrubiony)
**3 : 1**. To nie jest kwestia gustu — przy niższych wartościach część ludzi po prostu nie przeczyta,
a klienci hydraulika bywają starsi.

**Skąd wziął się błąd z nadpisem „PARTNER":** styl nadpisu zaprojektowałem pod ciemne hero (biały
tekst) i nadpisywałem go tylko wewnątrz `.head`. W sekcji, gdzie nadpis stał poza `.head`, został
biały — na jasnym tle kontrast wyszedł **1,04 : 1**, czyli praktycznie niewidoczny.

**Reguła na przyszłość:** kolor domyślny elementu ustawiamy pod **najczęstsze** tło (u nas jasne),
a wariant jasny dodajemy wyłącznie jako wyjątek dla ciemnych sekcji:

```css
.kicker { color: var(--ink-3); }                       /* domyślnie: ciemne na jasnym */
.hero .kicker, .sec-dark .kicker { color: #fff; }      /* wyjątek: jasne na ciemnym */
```

Nigdy odwrotnie. Element bez pasującej reguły ma wtedy kolor bezpieczny, a nie niewidoczny.

**Tekst na zdjęciu** rządzi się osobno: automat go nie zmierzy, bo tło jest zmienne. Potrzebna
przyciemniająca nakładka albo gradient pod napisem (u nas: gradient w kaflach i podpisach zdjęć).
Sam cień tekstu nie wystarcza na jasnych kadrach.

---

## 3. Łamanie wierszy i typografia

**Wyrazy złożone z dywizem nie mogą pękać.** „wodno-kanalizacyjne" złamane na „wodno-" i
„kanalizacyjne" czyta się jak dwa osobne słowa. Zabezpieczenie: `<span class="nw">` z
`white-space: nowrap`, razem z przecinkiem, żeby znak interpunkcyjny nie zawisł na początku wiersza.

**Sierota w nagłówku** (jedno krótkie słowo w ostatniej linii) — używamy `text-wrap: balance` na
`h1`–`h3`, co rozkłada linie równomiernie. Automat zgłasza, gdy ostatnia linia ma mniej niż 22%
szerokości najdłuższej.

**Długość wiersza:** 45–75 znaków dla tekstu ciągłego (u nas `max-width` w jednostkach `ch`).
Dłuższe wiersze gubią oko przy powrocie do początku linii.

**Interlinia:** 1,4–1,6 dla tekstu ciągłego, 1,05–1,25 dla dużych nagłówków — im większy stopień
pisma, tym mniej światła między wierszami.

**Wyrównanie optyczne, nie matematyczne.** Litery o okrągłych i skośnych kształtach wystają poza
linię wyrównania; jeśli coś wygląda na przesunięte mimo równych liczb, wierzymy oku.

---

## 4. Kolejność sprawdzania przed oddaniem

1. `tekst_lint.py` — frazesy, długie myślniki, emoji.
2. `predeploy_check.py` — powtórzone zdjęcia, martwe formularze.
3. **`sprawdz_wyglad.js` — kontrast, odstępy przy liniach, łamanie nagłówków.**
4. Obejrzeć stronę na 1440, 1024 i 390 px. Zrzut headless bez ramki potrafi kłamać —
   podgląd mobilny robić przez `<iframe width=390>` na widocznej stronie.
5. Sonda `scrollWidth == clientWidth` na każdej podstronie (brak poziomego przewijania).

---

## 5. Rozdzielczość zdjęć: ekrany 2× i kiedy upscalować

**Najczęstsza przyczyna „zdjęcie wygląda miękko" to nie kadrowanie, tylko gęstość ekranu.**
MacBooki i telefony mają gęstość 2×: pas o szerokości 1440 punktów potrzebuje pliku **2880 px**,
inaczej przeglądarka rozciąga go dwukrotnie. Sprawdzenie w konsoli:

```js
const i = document.querySelector('.wrap-wide img');
i.naturalWidth / i.getBoundingClientRect().width   // ma być ≥ 1,7
```
⚠️ Wynik zafałszuje **zoom strony** (Cmd +/−). Przy zoomie 71% przeglądarka poda liczby zaniżone
o ten sam współczynnik — najpierw `Cmd+0`, potem mierz.

**Upscale AI (Upscayl, lokalnie i za darmo) — stosujemy wybiórczo:**

| Rodzaj zdjęcia | Upscale | Dlaczego |
|---|---|---|
| napisy, logo, oklejone auto, certyfikaty | ✅ TAK | czyste krawędzie liter, bez aureoli |
| zdjęcia produktowe, gładkie powierzchnie | ✅ TAK | mało faktury do zgubienia |
| cegła, tynk, beton, drewno, rdza | ⛔ NIE | wygładza do postaci renderu |
| wnętrza z budowy, instalacje w stanie surowym | ⛔ NIE | jak wyżej |

Do wszystkiego pozostałego: maska wyostrzająca po przeskalowaniu (`UnsharpMask`), siła dobrana
do miękkości kadru. Zawsze porównać wycinek 1:1 przed wdrożeniem.

---

## Źródła

- [Carbon Design System — Spacing](https://carbondesignsystem.com/elements/spacing/overview/)
- [Cieden — Spacing best practices (internal ≤ external)](https://cieden.com/book/sub-atomic/spacing/spacing-best-practices)
- [UX Planet — 8-point grid w UX](https://uxplanet.org/everything-you-should-know-about-8-point-grid-system-in-ux-design-b69cb945b18d)
- [Webflow — Web spacing guide](https://webflow.com/blog/web-design-how-element-spacing-works)
- [Fonts.com — Visual (optical) alignment](https://www.myfonts.com/pages/fontscom-learning-fontology-level-2-display-typography-visual-alignment)
