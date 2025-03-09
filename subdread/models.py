from django.db import models
from user.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = 'category'
    
    def __str__(self):
        return self.name
    
    def get_children(self, id:int):
        return Category.objects.filter(parent=id)
    
    def get_parent(self, id:int):
        return Category.objects.get(id=id).parent

class SubDread(models.Model):
    creator = models.OneToOneField(User, related_name='dread', on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    users = models.ManyToManyField(User, related_name='subdreads')
    moderators = models.ManyToManyField(User, related_name='moderated_subdreads')
    categories = models.ManyToManyField(Category, related_name='subdreads')

    class Meta:
        db_table = 'sub_dread'

    def __str__(self):
        return self.name


class Flair(models.Model):
    name = models.CharField(max_length=50)
    subdread = models.ForeignKey(SubDread, related_name='flairs', on_delete=models.CASCADE)

    class Meta:
        db_table = 'flair'
        unique_together = ('name', 'subdread')

    def __str__(self):
        return self.name