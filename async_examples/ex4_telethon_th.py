from telethon import TelegramClient
from threading import Thread
import asyncio


async def send_msg():
    api_id = 5910285
    api_hash = "24e02b08be3f6a8085264780efb57af9"
    client=TelegramClient('anon',api_id,api_hash)
    await client.start()
    await client.send_message("me","Hello")


def th():
    asyncio.set_event_loop(asyncio.new_event_loop())
    loop=asyncio.get_event_loop()
    #loop.run_until_complete(send_msg())
    asyncio.run(send_msg())



Thread(target=th).start()
