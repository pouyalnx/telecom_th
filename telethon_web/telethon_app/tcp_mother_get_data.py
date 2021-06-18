import socket





line=socket.socket(socket.AF_INET,socket.SOCK_STREAM,socket.IPPROTO_TCP)
line.connect(('',8001))
data=line.recv(1024)
print(data)