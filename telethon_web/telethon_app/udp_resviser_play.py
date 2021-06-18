import asyncio
import socket

async def main():
    loop=asyncio.get_event_loop()
    line=socket.socket(socket.AF_INET,socket.SOCK_DGRAM,socket.IPPROTO_UDP)
    line.bind(('',8001))
    while True:
        data=await loop.sock_recv(line,128)
        print(data)

asyncio.run(main())