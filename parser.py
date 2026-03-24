from __future__ import annotations

from dataclasses import dataclass
import re

from lexer import Token, split_line_tokens


WORD_REPLACEMENTS = {
    "wypisz": "print",
    "jeżeli": "if",
    "inaczej": "else",
    "dopóki": "while",
    "dla": "for",
    "w": "in",
    "zakres": "range",
    "zakresie": "range",
    "funkcja": "def",
    "zwróć": "return",
    "czytaj": "input",
    "prawda": "True",
    "fałsz": "False",
    "oraz": "and",
    "lub": "or",
}

BLOCK_KEYWORDS = {"if", "else", "while", "for", "def"}
PRINT_STATEMENT_RE = re.compile(r"^(?P<indent>\s*)(?:wypisz|print)(?P<ws>\s+)(?P<expr>.+)$")
TO_SUFFIX_RE = re.compile(r"^(?P<body>.*?)(?P<ws>\s+)to\s*$")


@dataclass(frozen=True)
class ParsedLine:
    original: str
    translated: str


def _replace_word_boundaries(code: str, source: str, target: str) -> str:
    pattern = re.compile(rf"(?<!\w){re.escape(source)}(?!\w)")
    return pattern.sub(target, code)


def _translate_code_fragment(code: str) -> str:
    translated = code
    for source, target in WORD_REPLACEMENTS.items():
        translated = _replace_word_boundaries(translated, source, target)
    return translated


def _translate_print(code: str) -> str:
    match = PRINT_STATEMENT_RE.match(code)
    if not match:
        return code
    indent = match.group("indent")
    expr = match.group("expr").rstrip()
    return f"{indent}print({expr})"


def _translate_block_suffix(code: str) -> str:
    match = TO_SUFFIX_RE.match(code)
    if match:
        return f"{match.group('body')}:"

    stripped = code.strip()
    if stripped == "else":
        indent = code[: len(code) - len(code.lstrip())]
        return f"{indent}else:"

    return code


def translate_line(raw_line: str) -> ParsedLine:
    tokens = split_line_tokens(raw_line)
    code_parts: list[str] = []
    comment = ""

    for token in tokens:
        if token.kind == "code":
            code_parts.append(_translate_code_fragment(token.value))
        elif token.kind == "string":
            code_parts.append(token.value)
        else:
            comment = token.value
            break

    translated_code = "".join(code_parts)
    translated_code = _translate_print(translated_code)
    translated_code = _translate_block_suffix(translated_code)
    return ParsedLine(original=raw_line, translated=translated_code + comment)


def parse_source(source: str) -> list[ParsedLine]:
    return [translate_line(line) for line in source.splitlines()]


def translate_source(source: str) -> str:
    translated_lines = [line.translated for line in parse_source(source)]
    result = "\n".join(translated_lines)
    if source.endswith("\n"):
        return result + "\n"
    return result


def validate_source(source: str) -> None:
    for parsed_line in parse_source(source):
        stripped = parsed_line.translated.lstrip()
        if not stripped or stripped.startswith("#"):
            continue
        first_word = stripped.split(maxsplit=1)[0].rstrip(":")
        if first_word in BLOCK_KEYWORDS and not stripped.endswith(":"):
            raise SyntaxError(
                f"Brakuje 'to' na końcu bloku.\n"
                f"Mython: {parsed_line.original}\n"
                f"Python: {parsed_line.translated}"
            )
