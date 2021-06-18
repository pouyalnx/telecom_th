from django.shortcuts import render
from django.views.generic import View
from django.http import HttpRequest,HttpResponse
import socket
import json

class MainView(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get(self,request:HttpRequest): 
        msg="income queue>>>\n"
        line=socket.socket(socket.AF_INET,socket.SOCK_STREAM,socket.IPPROTO_TCP)
        line.connect(('',8001))
        data:bytes=line.recv(4096)
        line.close()
        msg=json.loads(data.decode('utf8'))
        for income in msg:
            msg+=f"{income[0]}:{income[1]}\n"     
        return HttpResponse(msg)

    def post(self,request:HttpRequest):
        sender:str=request.POST.get('id','')
        msg:str=request.POST.get('msg','')
        if sender=="me":
            self.line=socket.socket(socket.AF_INET,socket.SOCK_DGRAM,socket.SOL_UDP)
            self.line.sendto(f"{msg}".encode('ascii'),('127.0.0.1',8001))
            self.line.close()
        #    outbox_put_data([sender,msg])
        #elif sender.isdigit():
        #    outbox_put_data([int(sender),msg])

        return HttpResponse("if format true msg added to queue")            




