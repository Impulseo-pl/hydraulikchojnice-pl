# Instrukcja wdrożenia poprawek tekstowych

Strona: **Usługi Hydrauliczne Ireneusz Stryszyk** · `impulseo-pl/hydraulikchojnice-pl`

Dokument jest samodzielny. Nie trzeba znać wcześniejszych ustaleń — każda pozycja ma nazwę
podstrony, sekcję, stare brzmienie i nowe brzmienie.

---

## Zanim zaczniesz — gdzie edytować

Pliki `.html` w katalogu głównym są **generowane automatycznie**. Ręczna zmiana w nich zostanie
skasowana przy najbliższym przebudowaniu.

**Teksty edytuje się w pliku `pages.py`.** Po zmianach:

```bash
cd ~/Developer/impulseo-klienci/stryszyk
python3 build.py                     # przebudowanie wszystkich podstron
python3 ~/.claude/skills/strona-klienta/tekst_lint.py index.html    # kontrola języka
```

Podpisy zdjęć w galerii siedzą osobno, w pliku **`photos.py`**, w słowniku `OPIS` i liście
`_PODLOGOWKA`.

Wszystkie stare brzmienia poniżej zostały sprawdzone — występują w plikach dokładnie w tej postaci.

**Cztery miejsca oznaczone `[DO UZUPEŁNIENIA]` czekają na odpowiedź klienta.** Nie wpisuj tam nic
od siebie — lista pytań jest na końcu dokumentu.

---

# 1. STRONA GŁÓWNA (`index.html`)

## 1.1 Sekcja: pierwszy ekran, zdanie pod nagłówkiem

**STARE**
```
Dwadzieścia lat pracy przy instalacjach, od domu w budowie po remont łazienki.
      Robimy od pierwszej rury po rozruch i przeszkolenie, w umówionym terminie i za cenę, którą znacie
      przed rozpoczęciem prac.
```

**NOWE**
```
Dwadzieścia lat przy instalacjach, w Chojnicach i okolicy.
      Robimy całość: rozprowadzenie, montaż urządzeń, rozruch i regulację.
```

## 1.2 Sekcja: pasek pięciu haseł pod pierwszym ekranem

Zmienia się trzecia pozycja i kolejność wszystkich pięciu.

**STARE** (kolejność)
```
20 lat / Bezpłatna wycena / Cena ostateczna / 100 km / Vaillant
```

**NOWE** (kolejność i treść)
```
20 lat                  — przy instalacjach w domach
Vaillant                — autoryzowany montaż i serwis
Próby szczelności       — protokoły przy odbiorze
100 km                  — zasięg dojazdu od Chojnic
Bezpłatna wycena        — przyjazd i pomiar na miejscu
```

Pozycja „Cena ostateczna — ustalona przed startem prac" znika w całości.

## 1.3 Sekcja: usługi, nadpis nad nagłówkiem

**STARE**
```
<p class="kicker">Czym się zajmujemy</p>
```

**NOWE**
```
(usunąć całą linię)
```

## 1.4 Sekcja: usługi, akapit wprowadzający

**STARE**
```
Instalacje C.O, <span class="nw">wodno-kanalizacyjne</span>, gazowe i ogrzewania podłogowego to dla nas codzienność.
        Jeśli szukacie fachowego doradztwa, wykonania od A do Z i wyceny, po której wiadomo, ile instalacja
        będzie kosztować, jesteście w dobrym miejscu.
```

**NOWE**
```
Cztery zakresy, w których pracujemy przez większość roku. Resztę znajdziecie w ofercie.
```

## 1.5 Sekcja: proces, zdanie wprowadzające

**STARE**
```
Cztery kroki od telefonu do odbioru. Na każdym wiecie, co się dzieje i ile to kosztuje.
```

**NOWE**
```
(usunąć całe zdanie)
```

## 1.6 Sekcja: „Najważniejsze znika pod wylewką", akapit

**STARE**
```
Rury w posadzce i w bruzdach ścian znikają na kilkanaście lat. Poprawka po odbiorze
          oznacza skucie wylewki, więc pracujemy tak, żeby żadna poprawka nie była potrzebna. Instalację
          sprawdzamy pod ciśnieniem, zanim przyjedzie ekipa od jastrychu, a wy dostajecie z niej dokumenty.
```

**NOWE**
```
Rury w posadzce i w bruzdach ścian znikają na kilkanaście lat. Poprawka po odbiorze
          oznacza skucie wylewki. Dlatego instalację sprawdzamy pod ciśnieniem, zanim przyjedzie ekipa
          od jastrychu, a protokół z próby zostaje u was.
```

## 1.7 Sekcja: Vaillant, akapit

**STARE**
```
Montujemy i serwisujemy kotły gazowe oraz pompy ciepła Vaillant. Prowadzimy też
          sprzedaż obu typów urządzeń, więc nie musicie szukać sprzętu na własną rękę.
```

**NOWE**
```
Montujemy i serwisujemy kotły gazowe oraz pompy ciepła Vaillant. Sprzęt, gwarancja
          i przeglądy zostają w jednych rękach, bo urządzenie montuje ktoś przeszkolony przez producenta.
```

## 1.8 Sekcja: realizacje, akapit wprowadzający

**STARE**
```
Kotłownie, rozdzielacze, ogrzewanie podłogowe i podejścia wod-kan. Zdjęcia z budów,
        na których pracowaliśmy, bez upiększania.
```

**NOWE**
```
Zdjęcia z budów, na których pracowaliśmy. Bez upiększania.
```

## 1.9 Sekcja: obszar działania, akapit

**STARE**
```
Pracujemy w Chojnicach i okolicy, a przy większych inwestycjach dojeżdżamy w promieniu
          100 km. Nie wiecie, czy dojedziemy? Wystarczy jeden telefon.
```

**NOWE**
```
Pracujemy w Chojnicach i okolicy, dojeżdżamy w promieniu 100 km.
          Nie wiecie, czy dojedziemy do was? Wystarczy jeden telefon.
```

## 1.10 Sekcja: wezwanie na dole strony

**STARE** (nagłówek)
```
Planujecie instalację? Wycenimy ją za darmo.
```
**NOWE** (nagłówek)
```
Powiedzcie, co macie do zrobienia
```

**STARE** (zdanie pod nagłówkiem)
```
Wystarczy telefon albo wiadomość. Przyjedziemy, obejrzymy zakres prac i podamy ostateczną cenę.
```
**NOWE**
```
Przyjedziemy, obejrzymy zakres i podamy cenę. Przyjazd i wycena nic nie kosztują.
```

---

# 2. OFERTA (`oferta.html`)

## 2.1 Kolejność dwunastu pozycji — WYMAGA ZGODY KLIENTA

Pozycja „Drobne bądź duże awarie" przechodzi z **dwunastego** miejsca na **pierwsze**.
Reszta przesuwa się o jedno w dół, kolejność między nimi bez zmian.

W `pages.py` dotyczy to listy `USLUGI_12` oraz słownika `OFERTA_OPISY`.

**NOWA kolejność:**
```
01 Drobne bądź duże awarie
02 Instalacje wodno-kanalizacyjne
03 Instalacje C.O
04 Instalacje ogrzewania podłogowego
05 Montaż kotłów gazowych
06 Montaż kotłów na pellet oraz stałopalnych
07 Montaż pomp ciepła
08 Montaż instalacji gazowych
09 Montaż przydomowych oczyszczalni ścieków
10 Montaż odkurzaczy centralnych
11 Białe montaże
12 Przeróbki łazienek
```

Uwaga: ta sama lista w tej samej kolejności występuje też na stronie głównej (sekcja „Oferta").

## 2.2 Sekcja: zdanie pod nagłówkiem

**STARE**
```
Zakres usług, które wykonujemy, znajdziecie poniżej. Wycena jest bezpłatna, a cena ustalona po obejrzeniu miejsca jest ceną ostateczną.
```

**NOWE**
```
Przy każdej pozycji jest krótko napisane, co dokładnie robimy.
```

## 2.3 Opis usługi: Montaż kotłów gazowych

**STARE**
```
Jako autoryzowany montażysta Vaillant prowadzimy też ich serwis.
```
**NOWE**
```
Kotły Vaillant montujemy i serwisujemy z autoryzacją producenta.
```

## 2.4 Opis usługi: Montaż kotłów na pellet oraz stałopalnych

**STARE**
```
Montaż kotła, podłączenie do komina i instalacji, uruchomienie oraz przeszkolenie z obsługi i ustawień.
```
**NOWE**
```
Podłączamy kocioł do komina i instalacji, uruchamiamy i pokazujemy, jak ustawiać go pod paliwo, którego używacie.
```

## 2.5 Opis usługi: Montaż pomp ciepła

**STARE**
```
Dobór i montaż pompy ciepła wraz z zasobnikiem i automatyką. Montujemy pompy ciepła Vaillant, na które mamy szkolenie autoryzacyjne producenta.
```
**NOWE**
```
Dobór i montaż pompy ciepła wraz z zasobnikiem i automatyką. Pompy ciepła Vaillant montujemy z autoryzacją producenta.
```

## 2.6 Opis usługi: Montaż instalacji gazowych

**STARE**
```
Wykonanie instalacji gazowej i podłączenie urządzeń. Instalację przygotowujemy do próby szczelności i odbioru.
```
**NOWE**
```
Wykonujemy instalację i podłączamy urządzenia. Przygotowujemy ją do próby szczelności i odbioru.
```

## 2.7 Opis usługi: Montaż przydomowych oczyszczalni ścieków

**STARE**
```
Montaż oczyszczalni przy domach bez dostępu do kanalizacji, wraz z rozprowadzeniem i rozruchem.
```
**NOWE**
```
Dla domów bez dostępu do kanalizacji. Robimy rozprowadzenie, montaż i rozruch.
```

## 2.8 Opis usługi: Montaż odkurzaczy centralnych

**STARE**
```
Rozprowadzenie rur i gniazd na etapie budowy oraz montaż jednostki centralnej.
```
**NOWE**
```
Rury i gniazda rozprowadzamy na etapie budowy, razem z resztą instalacji. Jednostkę centralną montujemy na końcu.
```

## 2.9 Opis usługi: Białe montaże

**STARE**
```
Montaż wanien, kabin, umywalek, misek ustępowych i baterii, po zakończeniu prac wykończeniowych.
```
**NOWE**
```
Wanny, kabiny, umywalki, miski i baterie. Wchodzimy na końcu, po glazurze.
```

## 2.10 Sekcja: zdjęcia z budów, podpis

**STARE**
```
Kilka kadrów z etapu, którego zwykle nikt nie ogląda, bo zaraz potem znika pod tynkiem i wylewką.
```
**NOWE**
```
Kilka kadrów z trakcie roboty, zanim wszystko zniknie pod tynkiem.
```

## 2.11 Sekcja: wezwanie na dole

**STARE** (nagłówek)
```
Macie listę prac do wyceny?
```
**NOWE**
```
Nie wiecie, ile z tego potrzebujecie?
```

**STARE** (zdanie)
```
Wystarczy telefon i krótki opis zakresu. Umówimy oględziny i podamy cenę, która się później nie zmieni.
```
**NOWE**
```
Zadzwońcie i opiszcie, co macie do zrobienia. Przyjedziemy, obejrzymy i podamy cenę, która się później nie zmieni.
```

---

# 3. REALIZACJE (`realizacje.html`)

## 3.1 Sekcja: akapit wprowadzający

**STARE**
```
Kotłownie, rozdzielacze, ogrzewanie podłogowe, podejścia <span class="nw">wodno-kanalizacyjne</span> i wentylacja. Wszystkie zdjęcia pochodzą z budów, na których pracowaliśmy. Kliknięcie powiększa kadr.
```
**NOWE**
```
Wszystkie zdjęcia pochodzą z budów, na których pracowaliśmy.
```

## 3.2 Podpisy zdjęć podłogówki — 24 pozycje

Plik **`photos.py`**, lista `_PODLOGOWKA`. Zamienić całą listę.
Powód: obecne podpisy nazywają funkcje pomieszczeń (salon, gabinet, pokój dziecięcy), których
nie da się rozpoznać na kadrach ze stanu surowego i których nikt nie potwierdził.

| nr | STARE | NOWE |
|---|---|---|
| 01 | Pętle podłogówki w pokoju od strony ogrodu | Pętle ogrzewania podłogowego przed wylewką |
| 02 | Rozprowadzenie pętli w korytarzu | Rozprowadzenie pętli w korytarzu *(bez zmian)* |
| 03 | Ogrzewanie podłogowe w pomieszczeniu na parterze | Ogrzewanie podłogowe w pomieszczeniu na parterze *(bez zmian)* |
| 04 | Pętle poprowadzone wzdłuż ściany zewnętrznej | Pętle poprowadzone wzdłuż ściany zewnętrznej *(bez zmian)* |
| 05 | Podłogówka w sypialni przed wylewką | Podłogówka rozłożona przed wylewką |
| 06 | Ogrzewanie podłogowe przy wyjściu na taras | Pętle doprowadzone do wyjścia na zewnątrz |
| 07 | Pętle w pokoju z oknem połaciowym | Pętle w pomieszczeniu z oknem połaciowym |
| 08 | Rozłożone rury podłogówki na folii z siatką | Rozłożone rury podłogówki na folii z siatką *(bez zmian)* |
| 09 | Podłogówka w pomieszczeniu narożnym | Podłogówka w pomieszczeniu narożnym *(bez zmian)* |
| 10 | Pętle i podejścia grzejnikowe w jednym pomieszczeniu | Pętle i podejścia grzejnikowe obok siebie |
| 11 | Ogrzewanie podłogowe w przejściu między pokojami | Pętle poprowadzone przez przejście |
| 12 | Podłogówka poprowadzona w wąskim korytarzu | Podłogówka w wąskim korytarzu |
| 13 | Pętle w salonie z widokiem na ogród | Pętle w pomieszczeniu od strony okien |
| 14 | Ogrzewanie podłogowe w pokoju od strony podjazdu | Ogrzewanie podłogowe przed zalaniem wylewki |
| 15 | Podłogówka rozłożona w pomieszczeniu gospodarczym | Podłogówka rozłożona na całej powierzchni |
| 16 | Pętle w pokoju z oknem od południa | Pętle zagęszczone przy oknie |
| 17 | Ogrzewanie podłogowe na poddaszu użytkowym | Ogrzewanie podłogowe pod skosem dachu |
| 18 | Podłogówka w pokoju dziecięcym przed zalaniem | Podłogówka gotowa do zalania |
| 19 | Pętle ułożone wokół komina | Pętle ułożone wokół przejścia w posadzce |
| 20 | Ogrzewanie podłogowe w gabinecie | Ogrzewanie podłogowe w mniejszym pomieszczeniu |
| 21 | Podłogówka w pomieszczeniu z wyjściem na balkon | Podłogówka doprowadzona do drzwi balkonowych |
| 22 | Pętle podłogówki przed wejściem ekipy z jastrychem | Pętle podłogówki przed wejściem ekipy z jastrychem *(bez zmian)* |
| 23 | Ogrzewanie podłogowe w pokoju gościnnym | Ogrzewanie podłogowe w pomieszczeniu na piętrze |
| 24 | Podłogówka w pomieszczeniu przy kotłowni | Podłogówka rozłożona przy ścianie działowej |

## 3.3 Liczba zdjęć w grupie „Rozdzielacze i ogrzewanie podłogowe" — WYMAGA ZGODY KLIENTA

Grupa liczy 26 kadrów, w większości bardzo do siebie podobnych. Propozycja: zostawić 12 najlepszych.
Plik `photos.py`, funkcja `gallery_groups()`.

## 3.4 Sekcja: wezwanie na dole

**STARE** (nagłówek)
```
Chcecie podobną instalację u siebie?
```
**NOWE**
```
Chcecie coś podobnego u siebie?
```

**STARE** (zdanie)
```
Wystarczy jeden telefon i informacja, na jakim etapie jest budowa. Przyjedziemy obejrzeć zakres prac.
```
**NOWE**
```
Zadzwońcie i powiedzcie, na jakim etapie jesteście. Przyjedziemy obejrzeć zakres prac.
```

---

# 4. PARTNER (`partner.html`)

## 4.1 Sekcja: nagłówek główny

**STARE**
```
Autoryzowany montaż i serwis Vaillant
```
**NOWE**
```
Sprzęt, gwarancja i przeglądy w jednych rękach
```

## 4.2 Sekcja: zdanie pod nagłówkiem

**STARE**
```
Pracujemy na urządzeniach Vaillant i mamy autoryzację producenta na ich montaż oraz serwis. Dzięki temu sprzęt, gwarancja i przeglądy zostają w jednych rękach.
```
**NOWE**
```
Mamy autoryzację Vaillanta na montaż i serwis. To znaczy, że kocioł montuje ktoś przeszkolony przez producenta, a wy nie szukacie osobno serwisu, gdy przyjdzie przegląd.
```

## 4.3 Sekcja: pierwsza lista trzech punktów — usunąć w całości

**STARE**
```
Montaż oraz serwis kotłów gazowych Vaillant
Montaż pomp ciepła Vaillant
Sprzedaż obu typów urządzeń
```
**NOWE**
```
(usunąć całą listę — druga lista niżej mówi to samo, tylko konkretniej)
```

Uwaga: ta sama lista trzech punktów występuje także na **stronie głównej**, w sekcji Vaillanta.
Tam zostaje bez zmian.

## 4.4 Sekcja: akapit prawej kolumny

**STARE**
```
Autoryzacja oznacza, że urządzenie montuje ktoś przeszkolony przez producenta,
          a gwarancja zostaje utrzymana. Sprzęt kupujecie u nas albo we własnym zakresie, a my zajmujemy się montażem,
          rozruchem i późniejszymi przeglądami.
```
**NOWE**
```
Producent uzależnia gwarancję od tego, kto montuje urządzenie. Dlatego montaż
          i pierwsze uruchomienie robi u nas osoba z autoryzacją, a przeglądy w kolejnych latach zostają
          po naszej stronie.
          Sprzęt kupujecie u nas albo we własnym zakresie — montaż i rozruch wygląda tak samo.
```

## 4.5 Sekcja: trzy pozycje Montaż / Serwis / Sprzedaż

**STARE** (trzecia pozycja)
```
Dobór i dostawa urządzeń do konkretnego domu
```
**NOWE**
```
Dobór i dostawa urządzeń pod konkretny dom
```

Pozostałe dwie bez zmian.

## 4.6 Sekcja: urządzenia, nadpis

**STARE**
```
<p class="kicker">Co montujemy</p>
```
**NOWE**
```
(usunąć całą linię)
```

## 4.7 Sekcja: urządzenia, zdanie pod nagłówkiem

**STARE**
```
Kotły kondensacyjne, pompy ciepła i zasobniki ciepłej wody Vaillant.
```
**NOWE**
```
(usunąć całe zdanie)
```

## 4.8 Sekcja: certyfikaty, akapit

**STARE**
```
Zaświadczenia ze szkoleń autoryzacyjnych Vaillant: kotły gazowe,
        przeglądy wydłużające gwarancję i pompy ciepła. Wystawione są na Patryka Stryszyka, który prowadzi
        montaże razem z Ireneuszem.
```
**NOWE**
```
Patryk przeszedł trzy szkolenia autoryzacyjne Vaillanta w trzech kolejnych latach:
        kotły gazowe, przeglądy przedłużające gwarancję i pompy ciepła. Montaże prowadzi razem z Ireneuszem.
```

## 4.9 Podpisy pod skanami certyfikatów

**STARE**
```
Przeglądy kotłów wydłużające gwarancję
```
**NOWE**
```
Przeglądy kotłów przedłużające gwarancję
```

Dwa pozostałe podpisy i wszystkie daty bez zmian.

---

# 5. O NAS (`o-nas.html`)

## 5.1 Sekcja: nagłówek sekcji pod nagłówkiem głównym

**STARE**
```
Dwóch ludzi, jedna ekipa
```
**NOWE**
```
Wycenia ten sam człowiek, który potem kładzie rury
```

## 5.2 Sekcja: pierwszy akapit — usunąć w całości

**STARE**
```
Instalacje C.O, wodno-kanalizacyjne, gazowe i ogrzewania podłogowego to dla nas codzienność.
          Jeśli szukacie fachowego doradztwa w tych sprawach, wykonania od A do Z, w ustalonym terminie,
          i wyceny, po której wiadomo, ile instalacja będzie kosztować, jesteście w dobrym miejscu.
```
**NOWE**
```
(usunąć cały akapit — powtarza tekst ze strony głównej)
```

## 5.3 Sekcja: drugi akapit

**STARE**
```
Pracujemy we dwóch, Ireneusz i Patryk. To znaczy, że na budowie macie cały czas tych
          samych ludzi, a osoba, która wycenia, jest tą samą, która potem kładzie rury i podłącza kocioł.
          Patryk ma autoryzację Vaillant na montaż i serwis kotłów gazowych oraz pomp ciepła.
```
**NOWE**
```
Pracujemy we dwóch, Ireneusz i Patryk. Na budowie macie cały czas tych samych ludzi,
          bez podwykonawców i bez ekipy, która zmienia się w połowie roboty. Patryk ma autoryzację
          Vaillanta na kotły gazowe i pompy ciepła.
```

## 5.4 Sekcja: zasady, nadpis

**STARE**
```
<p class="kicker">Zasady, przy których zostajemy</p>
```
**NOWE**
```
(usunąć całą linię)
```

## 5.5 Sekcja: zasady, nagłówek

**STARE**
```
Cztery rzeczy bez zmian
```
**NOWE**
```
Na co możecie liczyć
```

## 5.6 Sekcja: cztery zasady — cała lista

**STARE**
```
Wycena    — Przyjazd i wycena są bezpłatne. Cena po oględzinach jest ceną ostateczną.
Termin    — Termin ustalamy przy wycenie i trzymamy się go.
Odbiór    — Instalację uruchamiamy, regulujemy i tłumaczymy, jak jej używać.
Później   — Gwarancja, protokoły z prób szczelności i stały kontakt, gdy coś się dzieje.
```
**NOWE**
```
Termin    — Ustalamy go przy wycenie i trzymamy się go.
Odbiór    — Instalację uruchamiamy, regulujemy i tłumaczymy, jak jej używać.
Papiery   — Protokoły z prób szczelności i gwarancja zostają u was.
Potem     — Odbieramy telefon także po skończonej robocie.
```

## 5.7 Sekcja: obszar działania — usunąć całą sekcję

Do usunięcia: nadpis „Gdzie pracujemy", nagłówek „Chojnice i okolice w promieniu 100 km",
akapit pod nim, lista pięciu miejscowości w pastylkach oraz zdjęcie obok.

Powód: dokładne powtórzenie sekcji ze strony głównej, tam z mapą i zdjęciem samochodu.

## 5.8 Sekcja: wezwanie na dole

**STARE** (zdanie, nagłówek zostaje bez zmian)
```
Wystarczy telefon. Umówimy oględziny, a wycenę dostajecie bez żadnych zobowiązań.
```
**NOWE**
```
Zadzwońcie. Przyjedziemy obejrzeć, co jest do zrobienia, i powiemy, ile to kosztuje.
```

---

# 6. KONTAKT (`kontakt.html`)

## 6.1 Sekcja: nagłówek główny

**STARE**
```
Porozmawiajmy o waszej instalacji
```
**NOWE**
```
Zadzwońcie albo napiszcie
```

## 6.2 Sekcja: zdanie pod nagłówkiem — `[DO UZUPEŁNIENIA]`

**STARE**
```
Najszybciej jest zadzwonić. Można też zostawić wiadomość przez formularz, wtedy oddzwonimy, gdy zejdziemy z budowy.
```
**NOWE**
```
Najszybciej jest zadzwonić. Jeśli wolicie napisać, zostawcie numer w formularzu — oddzwaniamy po zejściu z budowy, zwykle [TU WPISAĆ: tego samego dnia / do następnego dnia rano].
```

## 6.3 Sekcja: częste pytania — wymienić zestaw

Obecne cztery pytania są przeklejone ze strony głównej. Na tej podstronie mają być inne.

**STARE** (cztery pytania)
```
Ile będzie kosztowała instalacja?
Czy wycena jest płatna?
Kiedy możecie zacząć?
Co dostaję po zakończeniu montażu?
```

**NOWE** (cztery pytania)
```
Kiedy się odezwiecie, jak wyślę formularz?   [odpowiedź DO UZUPEŁNIENIA]
Kiedy możecie zacząć?                        [odpowiedź poprawiona, punkt 6.4]
Co dostaję po zakończeniu montażu?           [odpowiedź bez zmian]
Czy dostanę fakturę?                         [odpowiedź bez zmian, przeniesiona ze strony głównej]
```

Odpowiedzi „Co dostaję po zakończeniu montażu?" i „Czy dostanę fakturę?" przenieść bez zmian
z listy `FAQ` w `pages.py`.

## 6.4 Odpowiedź na pytanie „Kiedy możecie zacząć?" — `[DO UZUPEŁNIENIA]`

**STARE**
```
Termin ustalamy przy wycenie i trzymamy się go. Awarie traktujemy priorytetowo i przestawiamy grafik.
```
**NOWE**
```
Zwykle zaczynamy [TU WPISAĆ: w ciągu ilu tygodni], termin ustalamy przy wycenie i trzymamy się go. Awarie traktujemy priorytetowo i przestawiamy pod nie grafik.
```

## 6.5 Sekcja: formularz, zdanie pod przyciskiem

**STARE** (jedno zdanie pod przyciskiem „Wyślij zapytanie")
```
Formularz służy wyłącznie do kontaktu i nie służy do zawierania umów.
            Podane dane wykorzystamy tylko po to, żeby odpowiedzieć na zapytanie. Szczegóły opisaliśmy
            w <a href="polityka-prywatnosci.html">polityce prywatności</a>.
```

**NOWE** (rozdzielić na dwa, drugie mniejszą czcionką)
```
Dane wykorzystamy tylko po to, żeby odpowiedzieć na zapytanie.
```
```
Formularz służy wyłącznie do kontaktu i nie służy do zawierania umów.
            Szczegóły w <a href="polityka-prywatnosci.html">polityce prywatności</a>.
```

## 6.6 Sekcja: dane firmy, adres — `[DECYZJA KLIENTA]`

**STARE**
```
ul. Cypriana Norwida 4<br>89-600 Chojnice
```
**WARIANT A** (jeśli klient nie chce adresu domowego na stronie)
```
Chojnice
```
**WARIANT B**: bez zmian.

Pełny adres zostaje w polityce prywatności niezależnie od wyboru — jest tam wymagany.

---

# PYTANIA DO KLIENTA

Bez tych odpowiedzi cztery miejsca na stronie zostają niepełne. Nie wpisywać nic od siebie.

| # | Pytanie | Gdzie trafia |
|---|---|---|
| 1 | Jak szybko oddzwaniacie po formularzu? | 6.2 i 6.3 |
| 2 | Jaki jest zwykły termin startu prac? | 6.4 |
| 3 | Czy adres z umowy ma być publicznie na stronie? | 6.6 |
| 4 | Ile lat gwarancji i na co dokładnie? | oferta, nowa pozycja |
| 5 | Jedna, dwie realizacje z konkretem (metraż, zakres, czas) | realizacje |
| 6 | Ceny sprzętu Vaillant — jak w hurtowni czy z narzutem? | partner |
| 7 | Zgoda na wspólne zdjęcie Ireneusza i Patryka | o nas |
| 8 | Od kiedy działa firma i kiedy dołączył Patryk | o nas |

Osobno **trzy zmiany wymagające zgody klienta**, bo dotykają jego wcześniejszych ustaleń:
- przeniesienie awarii na pierwsze miejsce w ofercie (2.1),
- ograniczenie galerii podłogówki z 26 do 12 kadrów (3.3),
- ewentualna zmiana nagłówka głównego na stronie startowej.

---

# PO WPROWADZENIU ZMIAN

```bash
cd ~/Developer/impulseo-klienci/stryszyk
python3 build.py
python3 ~/.claude/skills/strona-klienta/tekst_lint.py index.html
python3 ~/.claude/skills/strona-klienta/predeploy_check.py .
```

Następnie otworzyć stronę i sprawdzić wzrokowo, czy nie zostały puste sekcje po usuniętych
akapitach (dotyczy 1.3, 1.5, 4.3, 4.6, 4.7, 5.2, 5.4, 5.7).
