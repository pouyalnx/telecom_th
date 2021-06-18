from telethon import TelegramClient
from django.conf import settings
from telethon.events import NewMessage
import asyncio
import threading
from queue import Queue
import socket
import json




async def inbox_get(addr,q:Queue):
    loop=asyncio.get_event_loop()
    print("socket called")
    line=socket.socket(socket.AF_INET,socket.SOCK_STREAM,socket.IPPROTO_TCP)
    print("socket opened")
    line.bind(addr)
    print("socket created")
    line.listen()
    while True:
        print("ready for clinets")
        (cline,_)=await loop.sock_accept(line)
        print("one here")
        dest=[]
        while not q.empty():
            dest.append(q.get_nowait())
        dest_str=json.dumps(dest,ensure_ascii=False)
        data=bytes(dest_str.encode('uft8'))
        await loop.sock_sendall(cline,data)
        cline.close()


async def main_telethon(api_id,api_hash,inbox:Queue):
    print(f"[Info]:telethon started")
    client=TelegramClient('anon',api_id,api_hash)
    

    @client.on(NewMessage())
    async def newmessage_event(event:NewMessage.Event):
        inbox.put([event.chat_id,event.raw_text])
    
    
    async def holder():
        while True:
            if not outbox.empty():
                req=outbox.get_nowait()
                await client.send_message(req[0],req[1])
            await asyncio.sleep(0.1)

    await client.start()
    await client.loop.create_task(holder())
    await client.run_until_disconnected()


async def main_co(api_id,api_hash,inbox:Queue):
    loop=asyncio.get_event_loop()
    await loop.create_task(main_telethon(api_id,api_hash,inbox))
    await loop.run_until_complete(inbox_get(('',8001),inbox))

def main_th(api_id,api_hash,inbox:Queue):
    asyncio.set_event_loop(asyncio.new_event_loop())
    asyncio.run(main_co(api_id,api_hash,inbox))


def main(api_id,api_hash,inbox:Queue):
    threading.Thread(target=main_th,args=(api_id,api_hash,inbox)).start()

TCP_PIPE_INBOX_PUT_ADDR=('',8001)
TCP_PIPE_INBOX_GET_ADDR=('',8001)
TCP_PIPE_OUTBOX_PUT_ADDR=('',8003)
TCP_PIPE_OUTBOX_GET_ADDR=('',8004)


try:
    with open(".lock","r") as f:
        f.read()
    print("[Warning]:Unable to start telethon")
except:
    with open(".lock","w") as f:
        f.write("locked")
    inbox=Queue()
    outbox=Queue()
    main(settings.API_ID,settings.API_HASH,inbox)

