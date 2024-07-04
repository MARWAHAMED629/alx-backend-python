#!/usr/bin/env python3
"""
This module contains a function for summing a list of integers and
floating-point numbers.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Sums a list of integers and floating-point numbers.

    Args:
        mxd_lst (List[Union[int, float]]): The list of integers and
        floating-point numbers to be summed.

    Returns:
        float: The sum of the given list of numbers.
    """
    return sum(mxd_lst)
