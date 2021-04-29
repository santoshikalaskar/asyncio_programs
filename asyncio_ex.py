import asyncio
import time

async def async_say(delay, msg):
    await asyncio.sleep(delay)
    print(msg)

async def main():
    task1 = asyncio.ensure_future(async_say(4, 'hello'))
    task2 = asyncio.ensure_future(async_say(6, 'world'))

    print(f"started at {time.strftime('%X')}")
    await task1
    await task2
    print(f"finished at {time.strftime('%X')}")

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
