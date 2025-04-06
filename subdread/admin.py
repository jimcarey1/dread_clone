from django.contrib import admin
from .models import SubDread, Category, Flair, Rule
# Register your models here.

admin.site.register(SubDread)
admin.site.register(Category)
admin.site.register(Flair)
admin.site.register(Rule)