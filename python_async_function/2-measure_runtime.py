#!/usr/bin/env python3
"""This module measures abg runtime of wait_n"""

import asyncio
import time

wait_n = __import__("1-basic_async_syntax").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """return total average execution time"""

    start = time.perf_counter()

    asyncio.run(wait_n(n, max_delay))

    end = time.time()

    total_time = end - start

    return total_time / n
