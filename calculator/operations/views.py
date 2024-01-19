from django.shortcuts import render
# inherit view from view class
from django.views.generic import View

from django import forms




class AdditionView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"add.html")
    
    def post(self,request,*args,**kwargs):
        print(request.POST)
        # reques.POST{} is the dict name
        n1=request.POST.get("num1")
        n2=request.POST.get("num2")
        result=int(n1)+int(n2)
        print("result",result)
        return render(request,"add.html",{"data":result})

class SubstractionView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"sub.html")
    
    def post(self,request,*args,**kwargs):
        print(request.POST)

        n1=request.POST.get("num1")
        n2=request.POST.get("num2")
        result=int(n1)-int(n2)
        print("result",result)
        return render(request,"sub.html",{"data":result})
    
class MultiplicationView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"mul.html")
    
    def post(self,request,*args,**kwargs):
        print(request.POST)

        n1=request.POST.get("num1")
        n2=request.POST.get("num2")
        result=int(n1)*int(n2)
        print("result",result)
        return render(request,"mul.html",{"data":result})



        
class DivssionView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"div.html")
    def post(self,request,*args,**kwargs):
        print(request.POST)

        n1=request.POST.get("num1")
        n2=request.POST.get("num2")
        result=int(n1) / int(n2)
        print("result",result)
        return render(request,"div.html",{"data":result})

class LeapYearView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"leap.html")
    
    def post(self,request,*args,**kwargs):
        year=int(request.POST.get("year"))
        result=""
        if year % 100==0 and year % 400==0 or year%100!=0 and year %4==0:
            result=f"{year} is leap year"
        else:
             result=f"{year} is not leap year"
        return render(request,"leap.html",{"data":result})

class IndexView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"index.html")
    


class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()

class SigninView(View):
     def get(self,request,*args,**kwargs):
         form=LoginForm()
         return render(request,"login.html",{"form":form})

class RegistrationForm(forms.Form):
    first_name=forms.CharField(label="FirstName")
    last_name=forms.CharField(label="LastName")
    email=forms.CharField(label="Email")
    username=forms.CharField(label="Username")
    password=forms.CharField(label="Password")

class RegisterView(View):
    def get(self,request,*args,**kwargs):
        form=RegistrationForm()
        return render(request,"reg.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=RegistrationForm()
        print(request.POST.get("first_name"))
        print(request.POST.get("last_name"))
        print(request.POST.get("email"))
        print(request.POST.get("username"))
        print(request.POST.get("password"))
        
        return render(request,"reg.html",{"form":form})

    

    

