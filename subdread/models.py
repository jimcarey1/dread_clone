from django.db import models
from user.models import User

# Create your models here.
class SubDread(models.Model):
    creator = models.OneToOneField(User, related_name='dread', on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'sub_dread'