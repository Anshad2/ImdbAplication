from django.db import models

# Create your models here.
class Book(models.Model):
    name=models.CharField(max_length=200,unique=True)
    author=models.CharField(max_length=200)
    language=models.CharField(max_length=200)
    genre=models.CharField(max_length=200)
    published_year=models.IntegerField()
    prize=models.IntegerField()
    rating=models.IntegerField()
    pages=models.IntegerField()
    
    def __str__(self): 
        return self.name
    