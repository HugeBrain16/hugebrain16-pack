import random
import string


def generate(**kwargs):
    """generate token from printable characters"""
    length = kwargs.get("length")
    if length is None:
        length = 8
    symbols = kwargs.get("symbols")
    digits = kwargs.get("digits")
    uppercase_letters = kwargs.get("uppercase_letters")
    lowercase_letters = kwargs.get("lowercase_letters")
    if lowercase_letters is None:
        lowercase_letters = True
    whitespace = kwargs.get("whitespace")
    allow_duplicates = kwargs.get("allow_duplicates")

    _CHAR = string.printable.strip()
    CHAR = ""
    result = ""

    if lowercase_letters:
        CHAR += _CHAR[10:36]
    if symbols:
        CHAR += _CHAR[62:]
    if digits:
        CHAR += _CHAR[:10]
    if uppercase_letters:
        CHAR += _CHAR[36:62]
    if whitespace:
        CHAR += " "

    while len(result) < length:
        char = random.choice(CHAR)
        if allow_duplicates:
            result += char
        else:
            if len(result) == len(CHAR):
                # cannot add more different characters
                break

            if char not in result:
                result += char

    return result
