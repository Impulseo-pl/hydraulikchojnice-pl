# Kontrola jakości tej strony

⛔ Bramki NIE leżą w tym repo — celowo. Kopie się rozjeżdżają i wtedy nowy test przestaje
łapać starsze strony. Jedna wspólna ścieżka znaczy, że każdy dopisany test działa WSTECZ
na wszystkich stronach.

```bash
python3 ~/.claude/skills/bramki/sprawdz.py .
```

Sprawdza: liczbę pojedynczą i inne reguły z rejestru lekcji · język (frazesy, myślniki) ·
zdjęcia (duplikaty, rozmiary, martwe ścieżki) · wygląd mierzony na prawdziwej przeglądarce
(kontrast liczony z pikseli zrzutu, odstępy przy liniach, łamanie nagłówków).

Dawny `sprawdz_wyglad.js` z tego katalogu → `~/Developer/_archive/2026-08-07/`.
Opis metody: `~/.claude/skills/bramki/SKILL.md`.
