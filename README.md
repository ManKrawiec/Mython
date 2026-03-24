# Mython

`Mython` to prosty interpreter języka inspirowanego Pythonem, ale z polskimi słowami kluczowymi.
Kod `.ps` jest tokenizowany przez `lexer.py`, przetwarzany przez `parser.py`, a potem wykonywany jako Python.

## Obsługiwane konstrukcje

- `wypisz` -> `print`
- `jeżeli ... to` -> `if ...:`
- `inaczej` -> `else`
- `dopóki ... to` -> `while ...:`
- `dla ... w zakresie(...) to` -> `for ... in range(...):`
- `funkcja ... to` -> `def ...:`
- `zwróć` -> `return`
- `czytaj` -> `input`
- `prawda` / `fałsz` -> `True` / `False`
- `oraz` / `lub` -> `and` / `or`

## Uruchamianie

```bash
python main.py example.ps
```

Podgląd wygenerowanego Pythona:

```bash
python main.py example.ps --emit-python
```

## Uruchamianie spoza folderu

Jeśli chcesz odpalać `Mython` z dowolnego katalogu, zainstaluj projekt jako lokalną komendę:

```bash
python -m pip install -e /home/mankrawiec/github/Mython
```

Po tym możesz uruchamiać pliki `.ps` z każdego miejsca:

```bash
mython /ścieżka/do/program.ps
mython /ścieżka/do/program.ps --emit-python
```

Przykład:

```bash
cd /tmp
mython /home/mankrawiec/github/Mython/example.ps
```

## Struktura projektu

```text
Mython/
├── main.py
├── translator.py
├── lexer.py
├── parser.py
├── example.ps
└── vscode-mython/
```

## Założenia

- Wcięcia muszą być poprawne, tak jak w Pythonie.
- Zamiana słów kluczowych nie dotyka stringów ani komentarzy.
- `to` jest zamieniane na `:` tylko na końcu linii.

## VS Code

Masz już gotowe wsparcie do codziennej pracy w VS Code:

1. Pliki `.ps` są skojarzone z językiem `mython` przez [.vscode/settings.json](/home/mankrawiec/github/Mython/.vscode/settings.json).
2. Jest lokalne rozszerzenie z koloryzacją składni w [vscode-mython/package.json](/home/mankrawiec/github/Mython/vscode-mython/package.json).
3. Jest task do uruchamiania bieżącego pliku w [.vscode/tasks.json](/home/mankrawiec/github/Mython/.vscode/tasks.json).
4. Jest konfiguracja debuggera w [.vscode/launch.json](/home/mankrawiec/github/Mython/.vscode/launch.json).

## Jak programować w VS Code

1. Otwórz folder projektu:

```bash
code /home/mankrawiec/github/Mython
```

2. Jeśli VS Code nie załaduje od razu lokalnego wsparcia, użyj:
`Developer: Install Extension from Location...`

3. Wskaż folder:
`/home/mankrawiec/github/Mython/vscode-mython`

4. Otwórz dowolny plik `.ps`, na przykład [example.ps](/home/mankrawiec/github/Mython/example.ps).

5. Uruchamianie:
- `Ctrl+Shift+B` odpala task `Run Current Mython File`
- `Terminal -> Run Task` pozwala też wypisać wygenerowany Python
- po lokalnej instalacji możesz też używać w terminalu po prostu `mython ${file}`

6. Debugowanie:
- przejdź do `Run and Debug`
- wybierz `Debug Current Mython File`
- uruchom `F5`

Jeśli chcesz pisać normalnie kod w `.ps`, to po tych krokach VS Code będzie rozpoznawał pliki, kolorował składnię i uruchamiał je bez ręcznego wpisywania komendy `python main.py plik.ps`.
