from django.shortcuts import render,redirect

from django.views.generic import View

from myapp.models import Movie

from django import forms

class MovieListView(View):
    def get(self,request,*args,**kwargs):
        qs=Movie.objects.all()
        return render(request,"movie_list.html",{"data":qs})
    
class DetaiesMovieView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Movie.objects.get(id=id)
        return render(request,"movie_details.html",{"data":qs})


# to delete a movie view
class MovieDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Movie.objects.get(id=id).delete()
        return redirect("movie-list")
    

# to create view

class MovieForm(forms.Form):
    name=forms.CharField()
    language=forms.CharField()
    run_time=forms.IntegerField()
    genre=forms.CharField()
    director=forms.CharField()
    actors=forms.CharField()
    year=forms.IntegerField()

class MovieCreateView(View):
    def get(self,request,*args,**kwargs):
     form=MovieForm()
     return render(request,"movie_create.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        data={k:v for k,v in request.POST.items()}

        data.pop("csrfmiddlewaretoken")

        Movie.objects.create(**data)
        return redirect("movie-list")

