#!/usr/bin/env python3
"""
 Let's execute multiple coroutines at the same time with async
"""


import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times with the specified max_delay.

    Args:
        n (int): Number of times to spawn wait_random
        max_delay (int): Maximum delay for each wait_random call

    Returns:
        List[float]: List of delays in ascending order
    """
    # Create a list of tasks by spawning wait_random n times
    tasks = [wait_random(max_delay) for _ in range(n)]

    # Wait for all tasks to complete and gather their results
    delays = await asyncio.gather(*tasks)

    # Return delays in ascending order without using sort()
    return [x for x in sorted(delays)]
