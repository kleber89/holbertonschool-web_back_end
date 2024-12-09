#!/usr/bin/env python3
"""
Tasks
"""
import asyncio

# Assuming wait_random is imported from 0-basic_async_syntax as mentioned
wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create and return an asyncio Task that waits for a random duration.

    Args:
        max_delay (int): The maximum delay time in seconds.

    Returns:
        asyncio.Task: A task that waits for a random time up to max_delay.
    """
    return asyncio.create_task(wait_random(max_delay))
