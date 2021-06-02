from telethon import TelegramClient

api_id = 5910285
api_hash = "24e02b08be3f6a8085264780efb57af9"
client=TelegramClient('anon',api_id,api_hash)
#connet this file alone no problem !

with client:
    client.loop.run_until_complete(client.connect()) # it work with this style they should called from loops



def call_connect_client():                                           # this form work good and completly
    with client:                                                     #
        client.loop.run_until_complete(client.connect())             #      


call_connect_client()




