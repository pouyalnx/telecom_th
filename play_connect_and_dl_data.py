from telethon import TelegramClient

api_id = 5910285
api_hash = "24e02b08be3f6a8085264780efb57af9"



def send_msg(id,msg):
    client=TelegramClient('anon',api_id,api_hash)
    with client:
        client.loop.run_until_complete(client.send_message(id,msg))

send_msg('me','hello lady sbh why still hope ?')


def send_file(id,path): #atention it should be file
    client=TelegramClient('anon',api_id,api_hash)
    with client:
        with open(path,'rb') as f:
            client.loop.run_until_complete(client.send_file(id,f))


send_file('me','play_connect.py')

