from telethon import TelegramClient
from asyncio import sleep
from .view import req_q,resp_q


async def send_msg(clinet:TelegramClient):
    while True:
        if len(resp_q):
            await clinet.send_message('me',resp_q.pop(0))
            req_q.append("sended to me")
        else:
            await sleep(1)


API_ID = 5910285
API_HASH = "24e02b08be3f6a8085264780efb57af9"

client=TelegramClient('anon',API_ID,API_HASH)
client.start()
client.loop.create_task(send_msg(client))
