#!/usr/bin/env python3
"""
Module documentation
"""
from typing import Mapping, Any, Union, TypeVar

T = TypeVar("T")


def safely_get_value(
    dct: Mapping, key: Any, default: Union[T, None] = None
) -> Union[Any, T]:
    """
    Safely retrieve a value from a dictionary.

    Args:
        dct (Mapping): The dictionary from which to retrieve the value.
        key (Any): The key to look up in the dictionary.
        default (Union[T, None], optional): Default value to return
        if key not found (default is None).

    Returns:
        Union[Any, T]: The value corresponding to 'key' in 'dct'
        if found, otherwise 'default'.
    """
    if key in dct:
        return dct[key]
    else:
        return default
