from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User #this import the default user model provided by django

class Post(models.Model): #class which inherits from models.Model provided by Django
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now) #timezone.now stores the date when the object was created
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title    

