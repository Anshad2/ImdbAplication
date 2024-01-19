from django.shortcuts import render,redirect

from django.views.generic import View

from books.models import Book


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