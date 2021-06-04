import asyncio
import time


async def func():
    s=time.perf_counter()
    print("saba in my mind ...")
    await asyncio.sleep(5)
    print("i will be best bussiness in this")
    print(f"time : {time.perf_counter()-s}")


async def call_many():
    asyncio.gather(func(),func(),func(),func(),func())
    

###############################################################

async def func2(a:int):
    print(f"this is {a}")
    time.sleep(5)
#    await asyncio.sleep(2)
    print(f"{a} end")


##############################################################
async def func4():
    s=time.perf_counter()
    await asyncio.gather(func2(1),func2(2),func2(3))
    print(f"time : {time.perf_counter()-s}")

#asyncio.run(call_many())
asyncio.run(func4())

