#!/usr/bin/env python3
"""
Module to measure the runtime of executing multiple asynchronous tasks.
"""

from asyncio import run
from time import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the average runtime of executing wait_n.

    Args:
        n (int): The number of times to call wait_random within wait_n.
        max_delay (int): The maximum delay for wait_random.

    Returns:
        float: The average runtime per call.
    """
    start = time()

    run(wait_n(n, max_delay))

    end = time()

    return (end - start) / n
