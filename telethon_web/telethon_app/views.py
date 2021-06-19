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
        incomes=json.loads(data.decode('utf8'))
        for income in incomes:
            msg+=f"{income[0]}:{income[1]}\n"     
        return HttpResponse(msg)

    def post(self,request:HttpRequest):
        sender:str=request.POST.get('id','')
        msg:str=request.POST.get('msg','')
        if sender=="me":
            pkt=['me',msg]
        elif sender.isdigit():
            pkt=[int(sender),msg]
        pkt_dp=json.dumps(pkt)
        data=bytes(pkt_dp.encode('utf8'))
        line=socket.socket(socket.AF_INET,socket.SOCK_STREAM,socket.IPPROTO_TCP)
        line.connect(('',8002))
        line.send(data)
        line.close()

        return HttpResponse("if format true msg added to queue")            




