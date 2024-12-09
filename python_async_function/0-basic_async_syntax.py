#!/usr/bin/env python3
"""
The basics of async
"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random delay between 0 and max_delay seconds.

    Args:
        max_delay (int): Maximum delay in seconds. Defaults to 10.

    Returns:
        float: The actual delay time that was waited.
    """
    # Generate a random float between 0 and max_delay
    delay = random.uniform(0, max_delay)

    # Asynchronously wait for the generated delay
    await asyncio.sleep(delay)

    # Return the actual delay time
    return delay
