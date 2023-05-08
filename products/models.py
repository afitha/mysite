from platform import python_version
from django.db import models

# Create your models here.

class userinfo(models.Model):
    name = models.CharField(max_length=100)
    mail= models.EmailField()
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
