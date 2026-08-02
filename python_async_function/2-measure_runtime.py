#!/usr/bin/env python3
"""This module measures abg runtime of wait_n"""

import asyncio
import time

wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """return total average execution time"""

    start = time.perf_counter()

    asyncio.run(wait_n(n, max_delay))

    end = time.perf_counter()

    total_time = end - start

    return total_time / n
