#!/usr/bin/env python3
"""
Asynchronous Comprehension Example

This script demonstrates the
use of asynchronous comprehensions in Python.

Modules and Functions:
- `async_generator`: Imported from
the `0-async_generator` module,
this asynchronous generator produces
random floating-point numbers
with a delay of one second between yields.

- `async_comprehension`: An asynchronous function that utilizes
an asynchronous comprehension to gather numbers produced
by `async_generator` into a list.

The script exemplifies how asynchronous comprehensions can simplify
the process of collecting data from asynchronous
generators while maintaining efficient execution.

Usage:
The `async_comprehension` function can be called
in an asynchronous
context to return a list of 10 random floating-point
numbers generated asynchronously.
"""

from typing import List

# Import the asynchronous generator from an external module
async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random floating-point numbers asynchronously
    using an asynchronous comprehension.

    This function leverages an asynchronous comprehension
    to iterate over the numbers yielded by
    `async_generator` and aggregate them into a list.

    Returns:
        List[float]: A list of 10 random floating-point numbers.
    """
    # Use an asynchronous comprehension to collect numbers into a list
    num_ten = [i async for i in async_generator()]
    return num_ten
