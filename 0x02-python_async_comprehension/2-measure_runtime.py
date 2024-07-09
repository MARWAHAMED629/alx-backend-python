#!/usr/bin/env python3

"""
Module for measuring the runtime of parallel async comprehensions.
"""

from asyncio import gather
from time import time

async_comprehension = __import__('1-async_comprehension').async_comprehension

async def measure_runtime() -> float:
    """
    Measures the runtime of executing four parallel async comprehensions.

    Returns:
        float: The total runtime in seconds.
    """
    start = time()
    tasks = [async_comprehension() for _ in range(4)]
    await gather(*tasks)
    end = time()
    return end - start
