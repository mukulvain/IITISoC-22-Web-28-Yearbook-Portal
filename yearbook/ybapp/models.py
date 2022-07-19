from email.policy import default
from django.db import models
from django.contrib.auth.models import User

# Create your models here

class Year(models.Model):
    ybyear = models.CharField(max_length=4)

    def __str__(self):
        return self.ybyear

class Branch(models.Model):
    branch = models.CharField(max_length=20,default='None')

    def __str__(self):
        return self.branch

class Student(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, default=None)
    auth_token = models.CharField(max_length=100, default='')
    is_verified = models.BooleanField(default=False)
    fname = models.CharField(max_length=50, default='')
    lname = models.CharField(max_length=50, default='')
    username = models.CharField(max_length=50)
    branch=models.CharField(max_length=20, default='')      
    year=models.IntegerField(blank=True, null=True, default=0)
    email = models.CharField(max_length=100, default='')
    image = models.ImageField(default='1920_1.jpg')     

    def __str__(self):
        return self.username

class Memories(models.Model):    
    memuname = models.CharField(max_length=50,default='')
    text=models.TextField(max_length=1000)
        
class Comments(models.Model):
    senderuname = models.CharField(max_length=50,default='')
    recieveruname = models.CharField(max_length=50,default='')
    content = models.CharField(max_length=200,default='')
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.recieveruname
