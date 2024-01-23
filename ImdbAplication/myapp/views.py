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
        form=MovieForm(request.POST)
        if form.is_valid():
          data=form.cleaned_data
          Movie.objects.create(**data)
          return redirect("movie-list")
        else:
          return render(request,"movie_create.html",{"form":form})
        


# to update
    # localhost:8000/movies/{id}/change   
class MovieUpdateView(View):
   def get(self,request,*args,**kwargs):
      form=MovieForm()

      id=kwargs.get("pk")
      movie_object=Movie.objects.get(id=id)
      data={
         "name":movie_object.name,
         "language":movie_object.language,
         "run_time":movie_object.run_time,
         "genre":movie_object.genre,
         "director":movie_object.director,
         "year":movie_object.year,
         "actors":movie_object.actors
      }
      form=MovieForm(initial=data)
      return render(request,"movie_edit.html",{"form":form})
   
   def post(self,request,*args,**kwargs):
      form=MovieForm(request.POST)
      if form.is_valid():
         data=form.cleaned_data
         id=kwargs.get("pk")
         Movie.objects.filter(id=id).update(**data)
         return redirect("movie-list")
      else:
         return render(request,"movie_edit.html",{"form":form})
   
