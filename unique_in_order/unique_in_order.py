from typing import Union, List, Any


def unique_in_order(input: Union[List[Any], str]):
    if not input:
        return []

    return [input[0]] + [
        input[i] for i in range(1, len(input)) if input[i - 1] != input[i]
    ]

