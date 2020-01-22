from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
# Database

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # auto_now=True date will change each time it is updated implement it for last updated
    # auto_now_add=True Cannot be changed so date created
    date_posted = models.DateTimeField(default=timezone.now)
    # Delete user then delete post
    author= models.ForeignKey(User, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.title
