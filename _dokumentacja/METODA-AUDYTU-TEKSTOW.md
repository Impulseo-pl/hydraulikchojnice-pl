# Metoda poprawiania tekstów na stronie klienta

Proces przeprowadzony 06.08.2026 na stronie Stryszyka, spisany tak, żeby dało się go powtórzyć
przy każdej kolejnej stronie docelowej. Siedem etapów, z których **etap 4 jest najważniejszy
i najczęściej pomijany**.

---

## ZANIM ZACZNIESZ: przygotowanie, bez którego proces się wykłada

### 1. Wyciągnij wszystkie teksty do jednego pliku

Nie audytuj, czytając kod. Potrzebny jest surowy tekst z oznaczeniem roli każdego fragmentu:

```python
# skrypt użyty u Stryszyka — do skopiowania
import re, html
for f in ['index.html','oferta.html', ...]:
    t = open(f).read()
    t = re.sub(r'<(script|style)[^>]*>.*?</\1>', '', t, flags=re.S)
    body = re.search(r'<main id="main">(.*?)</main>', t, re.S).group(1)
    body = re.sub(r'<h1[^>]*>(.*?)</h1>', r'\n[NAGŁÓWEK GŁÓWNY] \1\n', body, flags=re.S)
    body = re.sub(r'<h2[^>]*>(.*?)</h2>', r'\n[NAGŁÓWEK SEKCJI] \1\n', body, flags=re.S)
    body = re.sub(r'<p class="kicker"[^>]*>(.*?)</p>', r'\n[NADPIS] \1', body, flags=re.S)
    body = re.sub(r'<summary[^>]*>(.*?)</summary>', r'\n[PYTANIE] \1', body, flags=re.S)
    body = html.unescape(re.sub(r'<[^>]+>', ' ', body))
```

Bez etykiet `[NAGŁÓWEK]`, `[NADPIS]` audyt ocenia zdania w próżni i wychodzą bzdury.

### 2. ⛔ NAJWAŻNIEJSZE: oznacz teksty pochodzące OD KLIENTA

**To jest krok, którego nie zrobiłem u Stryszyka i trzy razy wyciąłem jego zdania, biorąc je
za własne frazesy.** Zanim zaczniesz oceniać cokolwiek, przejrzyj maile i notatki z briefu
i wypisz listę zdań, które klient podyktował.

U Stryszyka było ich pięć grup: nagłówek główny, cztery kroki procesu, dwanaście nazw usług,
trzy punkty na podstronie Partner i zdanie „to dla nas codzienność".

Te teksty **wolno skrytykować w audycie, ale nie wolno zmienić bez zgody klienta.** Oznacz je
w dokumencie przed pierwszym etapem.

### 3. Spisz, czego NIE wiesz

Lista faktów, których w materiałach nie ma: czas reakcji, godziny pracy, ceny, gwarancja,
liczba realizacji. Będzie potrzebna w etapie 3 — te miejsca zostają puste, a nie zmyślone.

---

## ETAP 1 — audyt, podstrona po podstronie

Jedna podstrona = jedna odpowiedź. Zatrzymanie po każdej, czekanie na „dalej". Powód: audyt
całości naraz robi się powierzchowny, bo model chce zdążyć ze wszystkim.

Dla każdego problemu: **cytat → dlaczego nie działa → jak wpływa na decyzję klienta → ważność 1-10**.

Perspektywa jest jedna i trzeba ją trzymać: **człowiek, który buduje dom albo remontuje łazienkę,
otwiera stronę na telefonie i chce zdecydować w dwie minuty.** Nie oceniać SEO, nie oceniać
estetyki, nie oceniać kodu.

Czego szukać (u Stryszyka wszystkie się pojawiły):
- powtórzeń tej samej informacji między sekcjami i podstronami — **policz je**, liczba robi wrażenie
  („lista usług 11 razy, bezpłatna wycena 7 razy")
- zdań pasujących do dowolnej innej firmy w branży („fachowe doradztwo", „od A do Z")
- konstrukcji, po których poznaje się tekst maszynowy („jesteście w dobrym miejscu")
- deklaracji bez pokrycia („pracujemy tak, żeby nie było poprawek") zamiast dowodów
  (protokół z próby szczelności)
- braku odpowiedzi na pytanie, które klient ma w głowie (kiedy oddzwonicie, ile to kosztuje)
- zdań opisujących stronę, nie firmę („znajdziecie poniżej", „kliknięcie powiększa")
- najlepszych zdań pochowanych w środku akapitów

**Wskaż też, co jest dobre — ale nie chwal na siłę.** U Stryszyka bronione były: proces w czterech
krokach, „Najważniejsze znika pod wylewką", „Jeśli nie odbieramy, jesteśmy przy pracy".

---

## ETAP 2 — poprawki w formacie STARE / NOWE

Nadal podstrona po podstronie. Dla każdej zmiany: cytat obecny, wersja nowa, jedno zdanie
uzasadnienia. Akapit nie do uratowania — pisany od nowa i tak nazwany.

Trzy twarde reguły:
1. **Nie dopisujesz faktów.** Brak = luka `[DO UZUPEŁNIENIA]`, nie zmyślenie.
2. **Nie ruszasz tekstów klienta** (lista z przygotowania). Możesz zaproponować obejście.
3. **Piszesz jak fachowiec, nie jak copywriter.** „Po glazurze" zamiast „po zakończeniu prac
   wykończeniowych".

---

## ETAP 3 — instrukcja wdrożeniowa

Dokument dla osoby, która nie zna rozmowy: podstrona, sekcja, stare brzmienie, nowe brzmienie.

**Zweryfikuj każdy stary cytat skryptem** — musi występować w pliku znak w znak, inaczej
„znajdź → zamień" nie zadziała:

```python
for plik, fragment in sprawdz:
    print('OK' if fragment in open(plik).read() else 'BRAK', fragment[:60])
```

Zaznacz wyraźnie, że edytuje się źródło (`pages.py`), nie generowany HTML.

---

## ETAP 4 — AUTOREWIZJA ⭐ najważniejszy etap

**Bez tego etapu proces daje tekst krótszy, ale słabszy.** U Stryszyka rewizja wykryła
11 błędów na 47 zmian, w tym jeden do całkowitego wycofania.

Do każdej własnej propozycji zadaj siedem pytań:

1. Czy ta zmiana **rzeczywiście zwiększa liczbę telefonów**?
2. Czy nowa wersja jest **lepsza od starej, czy tylko krótsza**?
3. Czy nie usuwam **argumentu sprzedażowego** tylko dlatego, że chciałem skrócić?
4. Czy klient ma po tej zmianie **więcej powodów, żeby zadzwonić**?
5. Czy brzmi **naturalniej** niż poprzednia?
6. Czy nie pogorszyłem **SEO ani czytelności nagłówków**?
7. Czy nie usuwam sekcji, która **jednak spełnia ważną funkcję**?

Format odpowiedzi: numer zmiany → dlaczego może być nietrafiona → co proponuję zamiast →
werdykt (zostawić / poprawić / **wycofać**).

### Sześć błędów, które wyszły w rewizji u Stryszyka — szukaj ich u siebie

| błąd | jak wyglądał |
|---|---|
| **wycięcie tekstu klienta** (3×) | uznałem jego zdania z maila za frazesy marketingowe |
| **argument sprzedażowy za techniczny** | „Cena ostateczna" → „Próby szczelności" w pasku haseł |
| **skrócenie kosztem argumentów** | z leadu wypadło rozpoznanie sytuacji klienta i cena z góry |
| **pominięty trade-off biznesowy** | awarie na 1. miejsce = więcej telefonów, ale drobnych zleceń |
| **marka wyrzucona z nagłówka** | „Vaillant" zniknął z H1 podstrony Partner |
| **własny błąd, wcześniej wytykany** | zamieniłem jedną instrukcję obsługi strony na drugą |

Wspólny mianownik: **optymalizowanie pod „mniej słów" zamiast pod „więcej powodów, żeby
zadzwonić"**. Skrócenie jest łatwo mierzalne, więc łatwo się nim zasugerować.

---

## ETAP 5 — przegląd całości

Dokument jako system, nie jako lista zdań. Sprawdzić skryptem i wzrokiem:

- czy zmiany **nie są ze sobą sprzeczne** (u Stryszyka rewizja sama zawierała sprzeczność:
  raz kazała zostawić zdanie na głównej, raz je stamtąd usunąć)
- czy **nie powstały nowe powtórzenia** — u Stryszyka „w jednych rękach" wchodziło jednocześnie
  na stronę główną i jako nagłówek Partnera
- czy argument usunięty w jednym miejscu **nie został dopisany w drugim**
- czy **nagłówki mają jeden styl** (sekcje = twierdzenia, wezwania = pytania)
- czy **wszystkie wezwania prowadzą do jednego celu**
- czy tekst brzmi jak **właściciel firmy, a nie copywriter**

```python
# wykrywanie nowych powtórzeń w propozycjach
for fraza in ['w jednych rękach','bezpłatn','gwarancj','100 km']:
    print(fraza, sum(1 for blok in nowe_teksty if fraza in blok.lower()))
```

---

## ETAP 6 — finalna redakcja i korekta

Dwa przejścia, osobno:

**Redakcja** — usunięcie ostatnich powtórzeń, skrócenie, poprawa H1 pod klienta z zachowaniem
fraz SEO, wyrzucenie resztek marketingu.

**Korekta** — literówki, sklejone słowa, interpunkcja, ucięte fragmenty. Skryptem, nie okiem:

```python
bledy = [(' z trakcie','ma być „w trakcie"'), (' ,','spacja przed przecinkiem'), ('..','podwójna kropka')]
```
U Stryszyka ta kontrola złapała błąd gramatyczny w mojej własnej propozycji.

---

## ETAP 7 — wdrożenie

1. **Punkt cofnięcia PRZED zmianami** — commit i tag:
   ```bash
   git tag -f przed-tekstami
   # cofnięcie: git reset --hard przed-tekstami && git push -f origin main
   ```
2. Zmiany skryptem, partiami po podstronie, z **raportem trafień**:
   ```python
   for stare, nowe, opis in ZMIANY:
       if stare in p: p = p.replace(stare, nowe, 1); print(f'  ✓ {opis}')
       else: print(f'  ✗ NIE ZNALEZIONO: {opis}')
   ```
   Nietrafione pozycje wynikają zwykle z innego łamania wierszy — sprawdź `grep -n` i popraw cytat.
3. Bramki: `tekst_lint.py`, `predeploy_check.py`, `sprawdz_wyglad.js`.
4. Kontrola wdrożenia grepem — czy stare frazy zniknęły, czy nowe są:
   ```bash
   grep -c "pokoju dziecięcym" realizacje.html    # ma być 0
   grep -c "W waszym domu" index.html             # ma być 1
   ```
5. Zrzut ekranu i obejrzenie — po usunięciu akapitów zostają puste sekcje.
6. Commit z opisem, co i dlaczego. Push.

---

## Czego ten proces NIE naprawi

Trzy braki u Stryszyka wróciły w każdym etapie i **żadnego nie da się załatać copywritingiem**:

1. **Czas reakcji** („oddzwaniamy tego samego dnia")
2. **Jakakolwiek liczba, której nie ma konkurencja** (metraż i czas jednej realizacji, liczba
   domów rocznie, orientacyjna cena)
3. **Opinie klientów**

Dlatego stałym produktem procesu jest **lista pytań do klienta**. U Stryszyka wyszło osiem.
Jedna rozmowa z właścicielem daje więcej niż cały audyt.

---

## Ile to trwa i ile daje

Sześć podstron, około 16 tys. znaków tekstu: **siedem etapów w jednej sesji**.
Wynik: 47 zmian, z czego 11 skorygowanych w rewizji, ~30% tekstu usunięte (prawie wyłącznie
powtórzenia), zero utraconych informacji.

Najcenniejsze nie były nowe zdania, tylko **trzy przeprowadzki**: najlepsze zdanie serwisu
z środka akapitu na nagłówek podstrony, korzyść na miejsce statusu w nagłówku i argument
o gwarancji z podstrony na stronę główną.
