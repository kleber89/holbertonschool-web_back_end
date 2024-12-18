#!/usr/bin/env python3
"""
Simple pagination.

This module provides a simple implementation of paginating a dataset
containing popular baby names. It includes utility functions and a class
to handle dataset retrieval and pagination.
"""

import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end indexes for a given page and page size.

    Args:
        page (int): The page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple containing the start index (inclusive) and the end index (exclusive) for the page.
    """
    # Calculate the start index (0-indexed).
    start_index = (page - 1) * page_size

    # Calculate the end index.
    end_index = start_index + page_size

    return start_index, end_index


class Server:
    """
    Server class to paginate a database of popular baby names.

    This class provides methods to load a dataset from a CSV file and retrieve
    paginated results based on the requested page and page size.
    """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """
        Initialize the Server instance.

        Attributes:
            __dataset (List[List] or None): A private attribute to cache the loaded dataset.
        """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Load and cache the dataset.

        If the dataset is not already loaded, this method reads the CSV file
        defined by `DATA_FILE` and caches the data, excluding the header row.

        Returns:
            List[List]: The dataset as a list of rows, where each row is a list of values.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip the header row.

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieve a page of the dataset.

        This method validates the inputs, calculates the start and end indexes
        for the requested page, and retrieves the corresponding rows from the dataset.

        Args:
            page (int): The page number (1-indexed). Must be a positive integer.
            page_size (int): The number of items per page. Must be a positive integer.

        Returns:
            List[List]: A list of rows for the requested page. If the page is out of range,
            an empty list is returned.

        Raises:
            AssertionError: If `page` or `page_size` are not positive integers.
        """
        # Validate inputs.
        assert isinstance(page, int) and page > 0, "Page must be a positive integer."
        assert (
            isinstance(page_size, int) and page_size > 0
        ), "Page size must be a positive integer."

        # Calculate the start and end indexes for the page.
        start, end = index_range(page, page_size)

        # Retrieve the dataset.
        dataset = self.dataset()

        # If the start index is out of range, return an empty list.
        if start >= len(dataset):
            return []

        # Return the slice of the dataset corresponding to the page.
        return dataset[start:end]
