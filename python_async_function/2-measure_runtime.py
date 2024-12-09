#!/usr/bin/env python3
"""
Measure the runtime
"""

import asyncio
import time


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random delay between 0 and max_delay seconds.

    Args:
        max_delay (int): Maximum delay in seconds. Defaults to 10.

    Returns:
        float: The actual delay time that was waited.
    """
    import random

    # Generate a random float between 0 and max_delay
    delay = random.uniform(0, max_delay)

    # Asynchronously wait for the generated delay
    await asyncio.sleep(delay)

    # Return the actual delay time
    return delay


async def wait_n(n: int, max_delay: int) -> list[float]:
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


async def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time for wait_n and return average time per task.

    Args:
        n (int): Number of times to spawn wait_random
        max_delay (int): Maximum delay for each wait_random call

    Returns:
        float: Average execution time per task
    """
    # Record the start time
    start_time = time.time()

    # Run wait_n and await its completion
    await wait_n(n, max_delay)

    # Calculate total execution time
    end_time = time.time()
    total_time = end_time - start_time

    # Return average time per task
    return total_time / n


# Example usage
async def main():
    result = await measure_time(5, 10)
    print(f"Average execution time: {result} seconds")


if __name__ == "__main__":
    asyncio.run(main())
