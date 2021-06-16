from telethon import TelegramClient
from django.conf import settings
from telethon.events import NewMessage
import asyncio
import threading

from .views import income_queue,outcome_queue

async def main_telethon(api_id,api_hash):
    print(f"[Info]:telethon started")
    client=TelegramClient('anon',api_id,api_hash)
    

    @client.on(NewMessage())
    async def newmessage_event(event:NewMessage.Event):
        print(income_queue)
        income_queue.append([event.chat_id,event.raw_text])
    
    
    
    async def holder():
        while True:
            if len(outcome_queue):
                req=outcome_queue.pop()
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
    main(settings.API_ID,settings.API_HASH)
