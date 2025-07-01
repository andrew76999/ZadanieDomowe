# Kalkulator Online – GitHub Pages

Mój projekt to prosty frontendowy kalkulator stworzony w HTML, CSS i JavaScript. Hostowany jako statyczna strona na GitHub Pages i zarządzany automatycznie za pomocą GitHub Actions (CI/CD).

## Użyte technologie i narzędzia
W projekcie wykorzystałem technologie frontendowe: HTML, CSS i JavaScript, tworząc w pełni statyczną aplikację działającą w przeglądarce. Do automatyzacji wdrożeń i monitorowania użyłem GitHub Actions, konfigurując workflow CI/CD z health-checkiem i mechanizmem rollback. Strona została opublikowana za pomocą GitHub Pages, co umożliwiło łatwe i darmowe hostowanie bez potrzeby posiadania serwera backendowego.

### Laboratorium 1

Nauczyłem się:
- inicjować projekt w repozytorium GitHub i tworzyć strukturę katalogów,
- pisać rozbudowany plik `README.md` z użyciem składni Markdown,
- korzystać z `.gitignore`, aby wykluczyć pliki tymczasowe i zależności,
- dokumentować zmiany w historii commitów przy użyciu `git log`,
- dodawać pliki dokumentacyjne (`LICENSE`, `CONTRIBUTING.md`) do repozytorium.

---

### Laboratorium 2

Nauczyłem się:
- pracować z gałęziami Git: tworzyć `feature`, otwierać pull requesty i wykonywać self-review,
- rozwiązywać konflikty między gałęziami i dokumentować ten proces,
- stosować semantyczne wersjonowanie (`MAJOR`, `MINOR`, `PATCH`) oraz publikować tagi i changelogi,
- pracować metodą TDD — pisać testy przed implementacją i osiągać pełne pokrycie kodu.

---

### Laboratorium 3

Nauczyłem się:
- tworzyć pipeline CI/CD w GitHub Actions, zawierający testy, deploy oraz sprawdzanie jakości kodu,
- automatycznie wdrażać frontendową aplikację na GitHub Pages,
- wykorzystywać health-check (curl) i rollback w przypadku nieudanego wdrożenia,
- tworzyć konfigurację aplikacji przez plik `config.js` jako symulację zmiennych środowiskowych,
- aktualizować dokumentację (`README.md`) oraz opisywać konfigurację i procesy wdrażania.




---

## Sprawdź strone

 [Zobacz online](https://andrew76999.github.io/ZadanieDomowe/)

---

##  Deployment

Strona działa na GitHub Pages przy wykorzystaniu folderu `docs/`.

### Jak wdrożyć nową wersję:

1. Umieść zaktualizowane pliki `index.html` i `config.js` w katalogu `docs/`
2. Zrób commit i push na gałąź `main`
3. GitHub Actions uruchomi pipeline:
   - sprawdzi poprawność plików
   - wdroży nową wersję na GitHub Pages
   - wykona health-check strony
   - jeśli health-check zawiedzie — cofnie commit (rollback)

---

##  Workflow – `.github/workflows/ci-cd.yml`

Pipeline składa się z 2 głównych etapów:

###  `build-and-test`
- Sprawdza, czy w katalogu `docs/` istnieje plik `index.html`

###  `deploy`
- Wdraża zawartość `docs/` na GitHub Pages za pomocą `peaceiris/actions-gh-pages`
- Wykonuje `curl` do strony → sprawdza kod odpowiedzi HTTP
- W razie niepowodzenia automatycznie wykonuje `git revert HEAD` (rollback)

Używa tokenu `GITHUB_TOKEN` (wbudowanego w GitHub) do uwierzytelnienia.

---

##  Konfiguracja aplikacji (`config.js`)

Aplikacja korzysta z zewnętrznego pliku konfiguracyjnego w stylu "zmiennych środowiskowych":

```js
window.APP_CONFIG = {
  version: "1.0.2",
  maintainer: "Andrii",
  theme: "light"
};
ZadanieDomowe/

---

## Struktura projektu
ZadanieDomowe/
├── .git/                         # Folder kontroli wersji Git (niewidoczny w repo online)
├── .github/
│   └── workflows/
│       └── ci-cd.yml             # GitHub Actions – CI/CD + deploy + health-check + rollback
│
├── docs/                         # Strona frontendowa kalkulatora – publikowana na GitHub Pages
│   ├── index.html                # Główna strona kalkulatora
│   └── config.js                 # Zmienna środowiskowa
│
├── tests/                        # Folder testów – np. dla NewCalculator.py
│
├── .gitignore                    # Ignorowane pliki przez Git
├── CHANGELOG.md                  # Historia wersji/projektu
├── CONTRIBUTING.md               # Zasady współpracy (np. dla contributorów)
├── LICENSE                       # Plik licencji projektu
├── README.md                     # Dokumentacja – opis projektu, deploy, workflow itp.
└── requirements.txt              # Lista zależności Pythona (dla testów/backendu)

---
** Autor Andrii Perevertailo Wersja aplikacji: 1.0.2 Licencja: MIT**
