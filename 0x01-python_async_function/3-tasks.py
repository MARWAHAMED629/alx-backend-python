#!/usr/bin/env python3
"""
Module for creating asynchronous tasks.
"""

from asyncio import Task, create_task

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """
    Create and return an asynchronous task for wait_random.

    Args:
        max_delay (int): The maximum delay for wait_random.

    Returns:
        Task: The created asynchronous task.
    """
    task = create_task(wait_random(max_delay))
    return task
