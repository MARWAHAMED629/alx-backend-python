#!/usr/bin/env python3
"""
Module for executing multiple asynchronous tasks.
"""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Executes wait_random n times and returns a list of the delays in ascending order.

    Args:
        n (int): The number of times to call wait_random.
        max_delay (int): The maximum delay for wait_random.

    Returns:
        List[float]: A list of the delays in ascending order.
    """
    wait_times = await asyncio.gather(
        *tuple(map(lambda _: wait_random(max_delay), range(n)))
    )
    return sorted(wait_times)
