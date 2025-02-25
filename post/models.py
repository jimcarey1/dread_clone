from django.db import models

from user.models import User
from subdread.models import SubDread
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    subdread = models.ForeignKey(SubDread, related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'posts'


class Comment(models.Model):
    author = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'comments'

