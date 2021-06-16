from django.shortcuts import render
from django.views.generic import View
from django.http import HttpRequest,HttpResponse
from tinydb import Query,TinyDB

# Create your views here.


income_queue=[]
outcome_queue=[]


class MainView(View):

    def get(self,request:HttpRequest):
        db=TinyDB('db.json')
        
        global income_queue
        global outcome_queue 
        msg="outcome queue>>>\n"
        for outcome in outcome_queue:
            msg+=f"{outcome[0]}:{outcome[1]}\n"
        
        msg+="income queue>>>\n"
        for income in income_queue:
            msg+=f"{income[0]}:{income[1]}\n"
        income_queue=[]        
        return HttpResponse(msg)

    def post(self,request:HttpRequest):
        global income_queue
        global outcome_queue
        sender:str=request.POST.get('id','')
        msg:str=request.POST.get('msg','')
        if sender=="me":
            outcome_queue.append([sender,msg])
        elif sender.isdigit():
            outcome_queue.append([int(sender),msg])

        return HttpResponse("if format true msg added to queue")            




