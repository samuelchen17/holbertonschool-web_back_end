#!/usr/bin/env python3
"""module contains async coroutine that waits and returns delay"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """wait for a random amount of time and return delay"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)

    return delay
