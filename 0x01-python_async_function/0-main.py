#!/usr/bin/env python3

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random

#loop = asyncio.get_event_loop()
#loop.run_until_complete(asyncio.wait())
#loop.run_until_complete(asyncio.wait(5))
#loop.run_until_complete(asyncio.wait(15))

print(asyncio.run(wait_random()))
print(asyncio.run(wait_random(5)))
print(asyncio.run(wait_random(15)))
