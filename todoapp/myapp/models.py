from django.db import models

# Create your models here.
class Task(models.Model):
    user=models.CharField(max_length=200)
    title= models.CharField(max_length=200,unique=True)
    description= models.CharField(max_length=1000)
    priority_choices=[
        ('Low_priority','Low_priority'),
        ('Medium_priority','Medium_priority'),
        ('High_priority','High_priority')
    ]
    priority=models.CharField(max_length=200,choices=priority_choices,default='High_priority')
    due_date=models.DateField(null=True,blank=True)

    completed=models.BooleanField(default=False)

    def __self__(self):
        return self.title