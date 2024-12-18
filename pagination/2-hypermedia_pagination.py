#!/usr/bin/env python3
"""
Hypermedia pagination
"""


import csv
import math
from typing import List, Dict


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
        """Initialize the server with the dataset."""
        self.dataset = []
        self.load_data()

    def load_data(self) -> None:
        """Load data from the CSV file."""
        with open(self.DATA_FILE, "r") as csvfile:
            reader = csv.reader(csvfile)
            # Skip the header
            next(reader)
            # Convert each row to a list and store
            self.dataset = list(reader)

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Return a page of the dataset.

        Args:
            page (int): The page number (1-indexed)
            page_size (int): Number of records per page

        Returns:
            List of lists representing the requested page
        """
        # Validate input
        assert isinstance(page, int) and page > 0, "Page must be a positive integer"
        assert (
            isinstance(page_size, int) and page_size > 0
        ), "Page size must be a positive integer"

        # Calculate start and end indices
        start_index = (page - 1) * page_size
        end_index = start_index + page_size

        # Return the appropriate slice of the dataset
        return self.dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Return hyperlinked pagination metadata.

        Args:
            page (int): The page number (1-indexed)
            page_size (int): Number of records per page

        Returns:
            Dictionary with pagination metadata
        """
        # Get the page data using get_page method
        data = self.get_page(page, page_size)

        # Calculate total number of pages
        total_pages = math.ceil(len(self.dataset) / page_size)

        # Determine next and previous page numbers
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        # Construct and return the metadata dictionary
        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages,
        }
