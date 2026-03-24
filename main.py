from __future__ import annotations

import argparse
from pathlib import Path

from translator import execute_mython, translate_code, validate_translated_code


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="mython",
        description="Uruchamia pliki Mython (.ps) lub wypisuje wynik translacji do Pythona.",
    )
    parser.add_argument("file", help="Ścieżka do pliku .ps")
    parser.add_argument(
        "--emit-python",
        action="store_true",
        help="Wypisz przetłumaczony kod Pythona zamiast go wykonywać.",
    )
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    path = Path(args.file)
    source = path.read_text(encoding="utf-8")
    validate_translated_code(source)

    if args.emit_python:
        print(translate_code(source), end="")
        return 0

    execute_mython(source, filename=str(path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
