from django.shortcuts import render,redirect

from django.views.generic import View

from books.models import Book

from django import forms


# to list book
class BookListView(View):
    def get(self,request,*args,**kwargs):
        qs=Book.objects.all()
        return render(request,"book_list.html",{"data":qs})
    
# to take details of specific book by id number
class BookDetailsView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Book.objects.get(id=id)
        return render(request,"book_details.html",{"data":qs})
    
# to delete a book
    
class BookDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Book.objects.get("id=id").delete()
        return redirect("book-list")
    


# to create a form
    
class BookForm(forms.Form):
        name=forms.CharField()
        author=forms.CharField()
        language=forms.CharField()
        genre=forms.CharField()
        published_year=forms.IntegerField()
        prize=forms.IntegerField()
        rating=forms.IntegerField()
        pages=forms.IntegerField()

class BookCreateView(View):
     def get(self,request,*args,**kwargs):
        form=BookForm()
        return render(request,"book_create.html",{"form":form})
     
     def post(self,request,*args,**kwargs):
         form=BookForm(request.POST)
         if form.is_valid():
             data=form.cleaned_data
             Book.objects.create(**data)
             return redirect("book-list")
         else:
           return render(request,"book_create.html",{"form":form})


