from uuid import uuid4
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
    username = models.CharField(max_length=100, blank=True,null=True, unique=True)
    email = models.EmailField(unique = True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    def __str__(self):
        return "{}".format(self.email)

class Module(models.Model):
    id = models.CharField(max_length=150, primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=100, null=True)
    created_at =  models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)

class Courses(models.Model):
    id=models.CharField(max_length=150, primary_key=True, default=uuid4, editable=False)
    name=models.CharField(max_length=100)
    module= models.ForeignKey('Module', on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)