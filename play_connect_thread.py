from threading import Thread
from time import sleep
from telethon import TelegramClient
import asyncio 

api_id = 5910285
api_hash = "24e02b08be3f6a8085264780efb57af9"


async def ath(id,msg,time,client):
    while True:
        #await asyncio.sleep(time)
        await client.send_message(id,msg)
    

def th(id,msg,time):
    client=TelegramClient('anon',api_id,api_hash)
    while True:
        #sleep(time)
        with client:
            client.loop.run_until_complete(client.send_message(id,msg))

client=TelegramClient('anon',api_id,api_hash)
with client:
    client.loop.run_until_complete(ath('me','belive poxgaga rich very very rich attarctive fuking good programmer and man with pretty body and many people',0.5,client))

#th('me','belive poxgaga rich very very rich attarctive fuking good programmer and man with pretty body and many people',0.5)

#Thread(target=th,args=('me','belive poxgaga rich very very rich attarctive fuking good programmer and man with pretty body and many people',2)).start()



#it dont work with clients and lets check quera lessions for asyncs

