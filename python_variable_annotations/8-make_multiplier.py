#!/usr/bin/env python3
"""module provides a function that returns a multiplier function"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], [float]]:
    """returns a function that multiplies a float by a multiplier"""

    def multiply(value: float) -> float:
        """multiplies a float by multiplier"""
        return value * multiplier

    return multiply
