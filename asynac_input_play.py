import asyncio
import sys
import threading 

async def ainput():
    loop= asyncio.get_event_loop()
    fut=loop.create_future()
    def _run():
        line = input() #sys.stdin.readline()
        loop.call_soon_threadsafe(fut.set_result,line)
    threading.Thread(target=_run,daemon=True).start()
    return await fut


async def console_input_loop():
    while True:
        inp=await ainput()
        print(f"_input_{inp}_")

#asyncio.run(console_input_loop())
loop=asyncio.get_event_loop()
loop.run_until_complete(console_input_loop())
