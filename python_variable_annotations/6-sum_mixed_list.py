#!/usr/bin/env python3
"""module defines function that returns sum of a list"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """return sum of all floats in list"""
    return float(sum(mxd_lst))
