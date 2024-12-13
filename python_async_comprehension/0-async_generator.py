#!/usr/bin/env python3
"""
0. Async Generator
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


# Example usage
async def main():
    async for number in async_generator():
        print(f"Generated number: {number:.2f}")


if __name__ == "__main__":
    asyncio.run(main())
