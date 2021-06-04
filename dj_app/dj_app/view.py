from django.views.generic import View
from django.http import HttpRequest,HttpResponse
from django.views.decorators.csrf import csrf_exempt

req_q=[]
resp_q=[]


class BasePage(View):
    def get(self,request:HttpRequest):
        msg="<html>\n<h1>System states</h1>\n"
        while len(req_q):
            dat=req_q.pop(0)
            msg+=f"<p>msg-->{dat}</p>\n"
        msg+="</html>"
        return HttpResponse(msg)

    def post(self,requset:HttpRequest):
        dat=requset.POST.get("req")
        if dat:
            resp_q.append(dat)
        return HttpResponse(f"<html><p>msg {len(resp_q)} in queue</p></html>")



