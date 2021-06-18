import socket
import asyncio
import random


async def loop():
    line=socket.socket(socket.AF_INET,socket.SOCK_DGRAM,socket.IPPROTO_UDP)
    while True:
        line.sendto(b'fuck u',('127.0.0.1',8001))
        await asyncio.sleep(2)


asyncio.run(loop())
        


