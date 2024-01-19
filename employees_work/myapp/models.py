from django.db import models

# Create your models here.
class Employee(models.Model):
    managerid=models.IntegerField()
    Name=models.CharField(max_length=200)
    Department=models.CharField(max_length=200)
    Salary=models.IntegerField()
    City=models.CharField(max_length=200)

    def __str__(self):
        return self.Name


