from urllib import request, response
import requests
import asyncio

from timer import timer

uuid_url = 'https://httpbin.org/uuid'
stream_url = 'https://httpbin.org/stream/1';

async def fetch_uuid():
    resp = requests.get(uuid_url)
    data = resp.json()
    print(data)
    await asyncio.sleep(1)


async def get_stream():
    resp = requests.get(stream_url)
    data = await resp.json()
    print(data)


@timer(1,1)
async  def main():
        for _ in range(3):
            fetch_uuid()

        for _ in range(3):
            get_stream()


async def call_async():
    await asyncio.gather(
        mycoro(1),
        mycoro(2),
        mycoro(3)
    )

asyncio.run(main())
