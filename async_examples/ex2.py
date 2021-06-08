import asyncio
import time

async def get_val(delay):
    await asyncio.sleep(delay)


async def main():
    print(f"{time.strftime('%X')}")
    await asyncio.wait_for(get_val(1),5)
    print(f"{time.strftime('%X')}")


    print(f"{time.strftime('%X')}")
    try:
        await asyncio.wait_for(get_val(10),5)
    except asyncio.TimeoutError:
        print("Timeout")
    print(f"{time.strftime('%X')}")


asyncio.run(main())


