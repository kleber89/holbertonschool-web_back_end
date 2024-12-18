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
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start, end = index_range(page, page_size)

        dataset = self.dataset()

        if start >= len(dataset):
            return []

        return dataset[start:end]
