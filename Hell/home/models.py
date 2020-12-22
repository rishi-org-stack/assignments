from os import name
from django.db import models

# Create your models here.
class user(models.Model):
    fname= models.CharField(max_length=20)
    email= models.CharField(max_length=50)
    lname= models.CharField(max_length=20,null=True)

class fav(models.Model):
    uid = models.IntegerField()
    name = models.CharField(max_length=20)
