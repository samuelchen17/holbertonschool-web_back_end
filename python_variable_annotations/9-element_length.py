#!/usr/bin/env python3
"""module defines func that returns elements and their lengths"""

from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """return a list of tuples containing each element and its length"""
    return [(i, len(i)) for i in lst]
