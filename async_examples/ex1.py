import asyncio
import time


#it is an coroutine
async def say_after(delay,what):
    await asyncio.sleep(delay)
    print(what)


async def main():
    print(f"started at {time.strftime('%X')}")


   #call with await
    await say_after(2,"hello")
    await say_after(2,"saba")

    print(f"ended at {time.strftime('%X')}")



    print(f"v2---started at {time.strftime('%X')}")

    tsk1=asyncio.create_task(say_after(2,"hello"))
    tsk2=asyncio.create_task(say_after(2,"my love"))


    await tsk1
    await tsk2

    print(f"ended at {time.strftime('%X')}")




asyncio.run(main())
