from __future__ import annotations

from parser import translate_line as parse_line
from parser import translate_source, validate_source


def translate_code(source: str) -> str:
    return translate_source(source)


def translate_line(line: str) -> str:
    newline = "\n" if line.endswith("\n") else ""
    raw_line = line[:-1] if newline else line
    return parse_line(raw_line).translated + newline


def execute_mython(source: str, filename: str = "<mython>") -> dict[str, object]:
    python_code = translate_code(source)
    namespace: dict[str, object] = {"__name__": "__main__"}
    compiled = compile(python_code, filename, "exec")
    exec(compiled, namespace)
    return namespace


def validate_translated_code(source: str) -> None:
    validate_source(source)
