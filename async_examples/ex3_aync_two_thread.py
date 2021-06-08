import asyncio
import threading



def th():
    loop=asyncio.new_event_loop()
    async def tsk1():
        while True:
            await asyncio.sleep(2)
            print("money")

    async def  tsk2():
        while True:
            print("linux & python")
            await asyncio.sleep(2)

    async def caller(loop):
        t1=loop.create_task(tsk1())
        t2=loop.create_task(tsk2())
        await t1
        await t2

    loop.run_until_complete(caller(loop))
    loop.close()


threading.Thread(target=th).start()
threading.Thread(target=th).start()
threading.Thread(target=th).start()
threading.Thread(target=th).start()
threading.Thread(target=th).start()
