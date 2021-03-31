from typing import List

MUST_HAVE_LENGHT = 10
MAX = 9
MIN = 0


def create_phone_number(number: List[int]):
    if not len(number) == MUST_HAVE_LENGHT:
        raise ValueError(f"Lenght of attribute number must be {MUST_HAVE_LENGHT}")
    if any([i < MIN or i > MAX for i in number]):
        print(number)
        raise ValueError(f"All number should be in range ({MIN}, {MAX})")
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*number)
