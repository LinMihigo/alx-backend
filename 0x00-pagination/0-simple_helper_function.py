#!/usr/bin/env python3
"""Task 0
"""


def index_range(page: int, page_size: int) -> tuple:
    """returns a tuple containing a range of indexes that are pagination params
    """
    return ((page_size * page - page_size), (page_size * page))
