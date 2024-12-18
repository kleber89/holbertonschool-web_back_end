#!/usr/bin/env python3
"""
Simple pagination
"""


import csv
import math
from typing import List


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


class Server:
    def get_page(elf, page=1, page_size=10):
        """
        Paginate the dataset based on page and page size.

        Args:
            page (int, optional): Page number. Defaults to 1.
            page_size (int, optional): Number of items per page. Defaults to 10.

        Returns:
            list: A list of rows for the specified page
        """
        # Assert that page and page_size are positive integers
        assert isinstance(page, int) and page > 0, "Page must be a positive integer"
        assert (
            isinstance(page_size, int) and page_size > 0
        ), "Page size must be a positive integer"

        # We'll use a placeholder dataset for now
        # In a real implementation, you would load the dataset from the CSV file
        dataset = [
            # Example rows - replace with actual CSV data
            ["row1_data1", "row1_data2"],
            ["row2_data1", "row2_data2"],
            # ... more rows
        ]

        # Calculate the start and end indexes using index_range
        start_index, end_index = index_range(page, page_size)

        # Return the appropriate page of the dataset
        # If the indexes are out of range, return an empty list
        return dataset[start_index:end_index]
