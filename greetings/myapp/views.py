# importing render to response html template response
from django.shortcuts import render
# importing view
from django.views.generic import View

# Create your views here.
# good morning view
# inherit class view

class GoodMorningView(View):
    # *args **kwargs multiple request
    def get(self,request,*args,**kwargs):
#to get html templte response
        return render(request,"morning.html")
    

# for good evening
    
class GoodEveningView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"evening.html")

class GoodAfterNoonView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"noon.html")
    
class GoodNightView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"night.html")