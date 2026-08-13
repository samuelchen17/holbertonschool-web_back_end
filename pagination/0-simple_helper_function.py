"""Module contains helper function for pagination"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Return start and end index"""
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)
