#!/usr/bin/env python3
"""module"""

from typing import Iterable, List, Tuple


def element_length(lst: Iterable[str]) -> List[Tuple[str, int]]:
    """return"""
    return [(i, len(i)) for i in lst]
