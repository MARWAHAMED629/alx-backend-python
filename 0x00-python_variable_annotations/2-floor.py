#!/usr/bin/env python3
"""
This module contains a function for computing the floor of a floating-point
number.
"""
import math


def floor(n: float) -> int:
    """
    Computes the floor of a floating-point number.

    Args:
        n (float): The floating-point number to be floored.

    Returns:
        int: The largest integer less than or equal to the given number.
    """
    return math.floor(n)
