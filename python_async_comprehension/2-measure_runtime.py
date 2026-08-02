#!/usr/bin/env python3
"""Module measures time it takes for asyn generator to run"""

import asyncio
import time

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """this function returns the time it takes to run async generators"""
    start_time = time.perf_counter()

    await asyncio.gather(*(async_comprehension() for _ in range(4)))

    end_time = time.perf_counter()

    return end_time - start_time
