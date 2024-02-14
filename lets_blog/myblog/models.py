from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=250)
    details = models.TextField()
    imagae = models.ImageField (upload_to='products/')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    def edit(self,name,details,image):
        self.name=name
        self.details=details
        self.imgae=image
        self.save()

    
    
