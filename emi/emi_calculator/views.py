from django.shortcuts import render
from django.views.generic import View

# Create your views here.

class EmiView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"emi.html")
    
    def post(self,request,*args,**kwargs):
        print(request.POST)
        principal=int(request.POST.get('principal'))
        interest_rate=float(request.POST.get('interest_rate'))/100
        tenure=float(request.POST.get('tenure'))
        interest_rate = interest_rate / (12 * 100)
        tenure = tenure * 12

        emi = round(principal * interest_rate * ((1 + interest_rate) ** tenure) / (((1 + interest_rate) ** tenure) - 1))
        total_payment = emi * tenure
        total_interest = total_payment - principal
        context={
            "data":emi,"info":total_interest,"value":total_payment}
        
        return render(request,'emi.html',context)
        

class IndexView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"index.html")