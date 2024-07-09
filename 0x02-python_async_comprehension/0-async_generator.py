#!/usr/bin/env python3

"""
Module for generating a sequence of random numbers asynchronously.
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Generates a sequence of 10 random numbers asynchronously.

    This coroutine waits 1 second between generating each number and yields
    a random float between 0 and 10.

    Yields:
        float: A random float number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
