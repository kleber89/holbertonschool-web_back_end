#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {i: dataset[i] for i in range(len(dataset))}
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Return deletion-resilient hypermedia pagination metadata.

        Args:
            index (int, optional): Starting index to retrieve data from. Defaults to None.
            page_size (int, optional): Number of items to retrieve. Defaults to 10.

        Returns:
            Dict: Pagination metadata with resilience to deletions
        """
        # Get the indexed dataset
        indexed_dataset = self.indexed_dataset()

        # Validate index
        assert index is None or (
            isinstance(index, int) and index >= 0
        ), "Index must be a non-negative integer"

        # If no index is provided, start from the beginning
        if index is None:
            index = 0

        # Initialize variables to collect data and track next index
        data = []
        current_index = index

        # Collect page_size number of items, skipping deleted indices
        while len(data) < page_size and current_index < len(indexed_dataset):
            if current_index in indexed_dataset:
                data.append(indexed_dataset[current_index])
            current_index += 1

        # Find the next index to query
        next_index = current_index
        while next_index < len(indexed_dataset) and next_index not in indexed_dataset:
            next_index += 1

        # If no more items found, set next_index to None
        if next_index >= len(indexed_dataset):
            next_index = None

        return {
            "index": index,
            "next_index": next_index,
            "page_size": len(data),
            "data": data,
        }
