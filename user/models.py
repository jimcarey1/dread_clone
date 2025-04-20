from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.

user = settings.AUTH_USER_MODEL

class User(AbstractUser):
    chatted_with = models.ManyToManyField(user)
    class Meta:
        db_table = 'users'
        
