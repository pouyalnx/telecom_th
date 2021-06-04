import asyncio
from telethon import TelegramClient
from threading import Thread
from time import sleep



buffer=[]

async def send_msg(client:TelegramClient):
    while True:
        if buffer:
            dat=buffer.pop()
            await client.send_message(dat[0],dat[1])
        else:
            await asyncio.sleep(1)


def th():
    while True:
        buffer.append(['me','hellp'])
        sleep(4)


client.start()
client.loop.create_task(send_msg(client))

Thread(target=th).start()

client.run_until_disconnected()