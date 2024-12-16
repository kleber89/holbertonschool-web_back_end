#!/usr/bin/env python3
"""
Simple helper function
"""


def index_range(page, page_size) -> tuple:
    """
    Calculate the start and end indexes for a given page and page size.

    Args:
    page (int): The page number (1-indexed)
    page_size (int): Number of items per page

    Returns:
    tuple: A tuple containing the start and end indexes
    """
    # Calculate the start index (0-indexed)
    start_index = (page - 1) * page_size

    # Calculate the end index
    end_index = start_index + page_size

    return (start_index, end_index)
