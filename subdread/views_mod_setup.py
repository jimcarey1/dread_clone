from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required


from .models import SubDread

@login_required
def mod_tools(request:HttpRequest, subdread:str): # type: ignore
    subdread:SubDread = SubDread.objects.get(name=subdread)
    return render(request, 'subdread/mod/layout.html', {'subdread':subdread})

@login_required
def post_flair(request:HttpRequest, subdread:str):
    subdread:SubDread = get_object_or_404(SubDread, name=subdread)
    return render(request, 'subdread/mod/post_flair.html', {'subdread':subdread})