#!/usr/bin/env python3
"""
Module documentation
"""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Return the first element of a sequence safely.

    Args:
        lst (Sequence[Any]:The sequence from which first element is returned.

    Returns:
        Union[Any, None]: The first element sequence if it exists, else None.
    """
    if lst:
        return lst[0]
    else:
        return None
