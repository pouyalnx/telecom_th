from telethon import TelegramClient
from django.conf import settings
import asyncio
import threading

async def main_telethon(api_id,api_hash):
    print(f"******object created {api_id}******")
    client=TelegramClient('anon',api_id,api_hash)
    await client.start()
    await client.send_message("me","Hello")
    await client.disconnect()


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
