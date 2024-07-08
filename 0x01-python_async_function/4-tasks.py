#!/usr/bin/env python3
"""
Module for spawning multiple asynchronous tasks.
"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn task_wait_random n times with the specified max_delay and return the
    list of delays in the order they complete.

    Args:
        n (int): The number of tasks to spawn.
        max_delay (int): The maximum delay for each task.

    Returns:
        List[float]: A list of delays in the order they complete.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
