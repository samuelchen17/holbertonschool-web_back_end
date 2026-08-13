#!/usr/bin/env python3
"""Module for pagination"""

import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Return start and end index"""
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)


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
        pass


def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
    """return list of rows belonging to requested page"""
    assert page > 0 and isinstance(
        page, int
    ), "Page must be int and greater than 0"
    assert page_size > 0 and isinstance(
        page_size, int
    ), "Page size myst be in and greater than 0"

    start, end = index_range(page, page_size)

    if start >= len(self.dataset()):
        return []

    return self.dataset()[start:end]
