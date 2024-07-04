#!/usr/bin/env python3
"""
This module contains a function that computes the length of elements
in an iterable of sequences.
"""
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Computes the length of each element in an iterable of sequences.

    Args:
        lst (Iterable[Sequence]): The iterable containing sequences whose
        lengths are to be computed.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples where each tuple
        contains a sequence from 'lst' and its corresponding length.
    """
    return [(i, len(i)) for i in lst]
