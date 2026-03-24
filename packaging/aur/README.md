# AUR Packaging

Pliki AUR dla `Mython` są trzymane osobno, żeby nie zaśmiecać głównego katalogu projektu.

## Pakiet

- `packaging/aur/mython-git/PKGBUILD`
- `packaging/aur/mython-git/.SRCINFO`

## Instalacja lokalna przez `makepkg`

```bash
cd packaging/aur/mython-git
makepkg -si
```

## Publikacja do AUR

1. Utwórz repo AUR `mython-git`.
2. Sklonuj repo AUR lokalnie.
3. Skopiuj do niego `PKGBUILD` i `.SRCINFO`.
4. Zacommituj i wypchnij do AUR.

Po publikacji użytkownik zainstaluje pakiet przez:

```bash
yay -S mython-git
```

## Uwaga

Przed publikacją warto dodać do głównego repo plik licencji i potem zaktualizować `license` w `PKGBUILD` oraz `.SRCINFO`.
