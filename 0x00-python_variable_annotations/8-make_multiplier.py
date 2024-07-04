#!/usr/bin/env python3
"""
This module contains a function that returns a multiplier function.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies its argument by a given multiplier.

    Args:
        multiplier (float): The multiplier to be used by the returned function.

    Returns:
        Callable[[float], float]: A function that takes a float and returns its
        product with the multiplier.
    """

    def mult(m: float) -> float:
        """Multiplies a number by the given multiplier."""
        return m * multiplier

    return mult
