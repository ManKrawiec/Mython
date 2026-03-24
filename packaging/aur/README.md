# AUR Packaging

Pliki AUR dla `Mython` są trzymane osobno, żeby nie zaśmiecać głównego katalogu projektu.

## Pakiety

- `packaging/aur/mython/`
- `packaging/aur/mython-git/PKGBUILD`
- `packaging/aur/mython-git/.SRCINFO`
- `packaging/aur/mython/PKGBUILD`
- `packaging/aur/mython/.SRCINFO`

## Ktory wybrac

- `mython-git`: bierze najnowszy kod z GitHuba, dobre na start
- `mython`: stabilna paczka pod konkretna wersje, dobra pod `yay -S mython`

## Instalacja lokalna przez `makepkg`

```bash
cd packaging/aur/mython
makepkg -si
```

## Publikacja do AUR

1. Dla `yay -S mython` utwórz repo AUR `mython`.
2. Dla `yay -S mython-git` utwórz repo AUR `mython-git`.
3. Sklonuj wybrane repo AUR lokalnie.
4. Skopiuj do niego `PKGBUILD` i `.SRCINFO` z odpowiedniego folderu.
5. Zacommituj i wypchnij do AUR.

Po publikacji użytkownik zainstaluje pakiet przez:

```bash
yay -S mython
```

albo:

```bash
yay -S mython-git
```

## Wymaganie dla stabilnego `mython`

Pakiet `mython` zaklada, ze na GitHubie istnieje tag:

```bash
v0.1.0
```

Bez tego AUR nie pobierze archiwum z `refs/tags/`.

## Szybka publikacja stabilnej wersji

1. Utworz tag w repo projektu:

```bash
git tag v0.1.0
git push origin v0.1.0
```

2. Potem opublikuj pliki z katalogu `packaging/aur/mython`.

## Szybka publikacja wersji `-git`

1. Utwórz repo AUR `mython-git`.
2. Sklonuj repo AUR lokalnie.
3. Skopiuj do niego pliki z katalogu `packaging/aur/mython-git`.
4. Zacommituj i wypchnij do AUR.

## Uwaga

Przed publikacją warto dodać do głównego repo plik licencji i potem zaktualizować `license` w `PKGBUILD` oraz `.SRCINFO`.
