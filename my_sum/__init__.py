from typing import Iterable


def sum(arg: Iterable):
    total = 0
    for val in arg:
        total += val
    return total
