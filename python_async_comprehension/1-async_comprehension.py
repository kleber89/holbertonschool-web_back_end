#!/usr/bin/env python3

"""
1. Async Comprehensions
------------------------
"""

import asyncio
import random


async def async_generator():
    """
    An async generator that yields 10 random numbers between 0 and 10,
    with a 1-second delay between each yield.
    """
    for _ in range(10):
        await asyncio.sleep(1)  # Asynchronous delay of 1 second
        yield random.uniform(0, 10)  # Yield a random float between 0 and 10


async def async_comprehension():
    """
    Uses async comprehension to collect 10 random numbers from async_generator.

    Returns:
        list: A list of 10 random numbers collected asynchronously
    """
    return [number async for number in async_generator()]


async def main():
    """
    Demonstrate the usage of async_generator and async_comprehension.
    """
    print("Collecting random numbers using async comprehension:")
    result = await async_comprehension()
    print(result)


if __name__ == "__main__":
    asyncio.run(main())
