from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Token:
    kind: str
    value: str


def split_line_tokens(line: str) -> list[Token]:
    tokens: list[Token] = []
    buffer: list[str] = []
    i = 0
    in_string = False
    string_delim = ""

    while i < len(line):
        char = line[i]

        if in_string:
            buffer.append(char)
            if char == "\\" and i + 1 < len(line):
                i += 1
                buffer.append(line[i])
            elif char == string_delim:
                tokens.append(Token("string", "".join(buffer)))
                buffer.clear()
                in_string = False
                string_delim = ""
            i += 1
            continue

        if char in {'"', "'"}:
            if buffer:
                tokens.append(Token("code", "".join(buffer)))
                buffer.clear()
            in_string = True
            string_delim = char
            buffer.append(char)
            i += 1
            continue

        if char == "#":
            if buffer:
                tokens.append(Token("code", "".join(buffer)))
                buffer.clear()
            tokens.append(Token("comment", line[i:]))
            return tokens

        buffer.append(char)
        i += 1

    if buffer:
        kind = "string" if in_string else "code"
        tokens.append(Token(kind, "".join(buffer)))

    return tokens
