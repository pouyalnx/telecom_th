from django.shortcuts import render
from django.views.generic import View
from django.http import HttpRequest,HttpResponse


# Create your views here.

from .init import inbox_get_data,outbox_put_data


class MainView(View):

    def get(self,request:HttpRequest): 
        msg="income queue>>>\n"
        for income in inbox_get_data():
            msg+=f"{income[0]}:{income[1]}\n"     
        return HttpResponse(msg)

    def post(self,request:HttpRequest):
        sender:str=request.POST.get('id','')
        msg:str=request.POST.get('msg','')
        if sender=="me":
            outbox_put_data([sender,msg])
        elif sender.isdigit():
            outbox_put_data([int(sender),msg])

        return HttpResponse("if format true msg added to queue")            




