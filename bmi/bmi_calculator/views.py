from django.shortcuts import render
from django.views.generic import View

# Create your views here.

class BmiCalculatorView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"index.html")
    def post(self,request,*args,**kwargs):
        print(request.POST)
        height=float(request.POST.get("height"))/100
        weight=float(request.POST.get("weight"))
        bmi=weight/ height**2
        print("bmi",bmi)
        return render(request,"index.html",{"data":bmi})

