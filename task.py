import asyncio
import time

async def mycoro(number):
    start = time.time()
    print(start)
    print(f'Starting {number}')
    await asyncio.sleep(1)
    print(f'Finishing {number}')
    end = time.time()
    print(end - start)
    return str(number)

async def call_async():
    await asyncio.gather(
        mycoro(1),
        mycoro(2),
        mycoro(3)
    )

asyncio.run(call_async())