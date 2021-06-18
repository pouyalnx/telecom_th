from telethon import TelegramClient
from django.conf import settings
from telethon.events import NewMessage
import asyncio
import threading
from queue import Queue


def inbox_get_data():
    data=[]
    while not inbox.empty():
        data.append(inbox.get_nowait())
    return data 

def outbox_put_data(data):
    outbox.put_nowait(data)

async def main_telethon(api_id,api_hash):
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


def main_th(api_id,api_hash):
    asyncio.set_event_loop(asyncio.new_event_loop())
    asyncio.run(main_telethon(api_id,api_hash))


def main(api_id,api_hash):
    threading.Thread(target=main_th,args=(api_id,api_hash)).start()



try:
    with open(".lock","r") as f:
        f.read()
    print("[Warning]:Unable to start telethon")
except:
    with open(".lock","w") as f:
        f.write("locked")
    inbox=Queue()
    outbox=Queue()
    main(settings.API_ID,settings.API_HASH)
