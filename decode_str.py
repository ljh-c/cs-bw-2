def decode(s: str, i: int = 0) -> (str, int):
    decoded = ""
    digits = ""

    while i < len(s):
        c = s[i]

        if c.isdigit():
            digits += c
            i += 1

        elif c == '[':
            seq, next_i = decode(s, i + 1)

            decoded += int(digits) * seq

            digits = ""
            i = next_i

        elif c == ']':
            return decoded, i + 1

        else:
            decoded += c
            i += 1

    return decoded, i


def decode_str(s: str) -> str:
    decoded, _ = decode(s)

    return decoded
