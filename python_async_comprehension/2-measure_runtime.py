#!/usr/bin/env python3
"""
2. Run time for four parallel comprehensions
-----------------------
"""

import asyncio
import random
import time  # Import time module for measuring runtime

async def async_generator():
    """
    Asynchronously generates random integers.

    Yields
    ------
    int
        A random integer between 0 and 100.

    Notes
    -----
    This function simulates an asynchronous operation by sleeping for 1 second
    before yielding each random number. It will generate up to 100 random numbers.
    """
    for _ in range(100):  # Generate 100 random numbers
        await asyncio.sleep(1)  # Simulate an asynchronous operation
        yield random.randint(0, 100)

async def async_comprehension():
    """
    Collects 10 random numbers using an asynchronous comprehension.

    Returns
    -------
    list of int
        A list containing 10 random integers collected from the async_generator.

    Notes
    -----
    This function uses an async for loop to gather random numbers until it has
    collected 10 numbers. It breaks out of the loop once the desired count is reached.
    """
    random_numbers = []
    async for num in async_generator():
        random_numbers.append(num)
        if len(random_numbers) == 10:
            break
    return random_numbers

async def measure_runtime():
    """
    Measures the total runtime of executing async_comprehension four times in parallel.

    Returns
    -------
    float
        The total runtime in seconds for executing async_comprehension four times.
    """
    start_time = time.time()  # Record the start time

    # Execute async_comprehension four times in parallel
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end_time = time.time()  # Record the end time
    return end_time - start_time  # Calculate the total runtime

async def main():
    """
    Main coroutine to execute measure_runtime and print the results.

    Notes
    -----
    This function calls measure_runtime and prints the total runtime for executing
    async_comprehension four times in parallel.
    """
    total_runtime = await measure_runtime()
    print(f"Total runtime: {total_runtime:.2f} seconds")

# Run the main function
if __name__ == "__main__":
    asyncio.run(main())