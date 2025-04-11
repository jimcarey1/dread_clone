from django.db import models
from froala_editor.fields import FroalaField

from user.models import User
from subdread.models import SubDread, Flair
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    subdread = models.ForeignKey(SubDread, related_name='posts', on_delete=models.CASCADE)
    flair = models.ForeignKey(Flair, related_name='posts', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    content = FroalaField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'posts'

    def get_comments(self):
        return self.comments.all()


class Comment(models.Model):
    author = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, null=True)
    content = FroalaField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'comments'
    
    def get_children(self, id:int):
        '''
        This function returns the children
        of a comment instance.
        '''
        comment = Comment.objects.get(id=id)
        return comment.children.all()