#!/usr/bin/env python3
"""
Module documentation
"""
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Zoom in on elements of a tuple by repeating them.

    Args:
        lst (Tuple): The tuple whose elements are to be zoomed in.
        factor (int, optional): The factor by which to zoom in (default is 2).

    Returns:
        List: A list containing elements of 'lst' repeated 'factor' times.
    """
    zoomed_in: List = [item for item in lst for i in range(factor)]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
