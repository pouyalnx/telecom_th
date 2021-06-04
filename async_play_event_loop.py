import asyncio


async def jobs(a:int):
    while True:
        print(f"<<{a}>>")
        await asyncio.sleep(2)


loop=asyncio.get_event_loop()
loop.create_task(jobs(1))
loop.create_task(jobs(2))
loop.create_task(jobs(3))
loop.create_task(jobs(4))
loop.create_task(jobs(5))
loop.create_task(jobs(6))
loop.run_forever()

#loop.close()

