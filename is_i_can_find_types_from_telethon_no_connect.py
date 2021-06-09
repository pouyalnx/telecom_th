from telethon import TelegramClient

api_id = 5910285
api_hash = "24e02b08be3f6a8085264780efb57af9"
client=TelegramClient('anon',api_id,api_hash)


print(type(client.iter_messages()))