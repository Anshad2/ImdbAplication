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


class BookUpdateView(View):
    def get(self,request,*args,**kwargs):
        form=BookForm()
        id=kwargs.get("pk")
        book_object=Book.objects.get(id=id)
        data={
            "name": book_object.name,
            "author": book_object.author,
            "language": book_object.language,
            "genre": book_object.genre,
            "published_year": book_object.published_year,
            "prize": book_object.prize,
            "rating": book_object.rating,
            "pages": book_object.pages
        }

        form=BookForm(initial=data)
        return render(request,"book_edit.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=BookForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            id=kwargs.get("pk")
            Book.objects.filter(id=id).update(**data)
            return redirect("book-list")
        else:
            return render(request,"book_edit.html",{"form":form})


    
