#!/usr/bin/env python3
"""
 Let's execute multiple coroutines at the same time with async
"""

import asyncio
from typing import List

task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Create n tasks that wait for a random time up to max_delay
    and return the list of wait times in ascending order.

    Args:
        n (int): Number of tasks to create
        max_delay (int): Maximum delay time for each task

    Returns:
        List[float]: List of wait times sorted in ascending order
    """
    # Create n tasks using task_wait_random
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    # Wait for all tasks to complete and get their return values
    wait_times = await asyncio.gather(*tasks)

    # Return the wait times sorted in ascending order
    return sorted(wait_times)
