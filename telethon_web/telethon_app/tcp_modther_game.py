import socket
import asyncio



async def buffer():
    loop=asyncio.get_event_loop()
    line=socket.socket(socket.AF_INET,socket.SOCK_STREAM,socket.IPPROTO_TCP)
    line.bind(('',8001))
    line.listen()
    while True:
        (sock,addr)=await loop.sock_accept(line)
        await loop.sock_sendall(sock,b'saba love pouya very very much and cant control herself')
        sock:socket.socket
        sock.close()


asyncio.run(buffer())