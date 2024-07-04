#!/usr/bin/env python3
"""
This module contains a function that creates a tuple from a string and a
number.
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Creates a tuple from a string and the square of a number.

    Args:
        k (str): The string to be used as the first element of the tuple.
        v (Union[int, float]): The number to be squared and used as the second
        element of the tuple.

    Returns:
        Tuple[str, float]: A tuple containing the str and squared num
    """
    return (k, v ** 2)
