#!/usr/bin/env python3

"""
1. Async Comprehensions
------------------------
"""

import asyncio
import random


async def async_generator():
    """
    Yield 10 random numbers with a 1-second interval.

    This function uses the asyncio library to asynchronously generate random numbers.
    It sleeps for 1 second between each number generation to simulate a delay.

    Returns:
        float: A random number between 0 and 1.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random()


async def async_comprehension():
    """
    Collect 10 random numbers using an async comprehension over async_generator.

    This function asynchronously iterates over the async_generator and collects
    the yielded random numbers into a list.

    Returns:
        list of float: A list containing 10 random numbers.
    """
    return [number async for number in async_generator()]
