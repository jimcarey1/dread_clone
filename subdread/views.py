from ast import Sub
from os import name
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden


from .forms import SubDreadForm
from .models import SubDread

from utils.community import is_community_setup

def community_home(request:HttpRequest, subdread:str):
    subdread:SubDread = SubDread.objects.get(name=subdread)
    return render(request, 'subdread/community_homepage.html', {'subdread':subdread})

# Create your views here.
@login_required
def create_community(request:HttpRequest):
    if request.method == 'POST':
        form = SubDreadForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            subdread = SubDread(
                name = data.get('name'),
                description = data.get('description'),
                type = data.get('type'),
                adults_only = data.get('adults_only'),
                creator = request.user
            )

            subdread.save()
            subdread.users.add(request.user)
            subdread.moderators.add(request.user)
            subdread.categories.add(*data.get('categories'))

            return redirect('community_setup_url', subdread = subdread.name)
        return render(request, 'subdread/create_community.html', {'form':form})
    else:
        form = SubDreadForm()
        return render(request, 'subdread/create_community.html', {'form':form})
        

@login_required
def community_setup(request:HttpRequest, subdread:str):
    subdread:SubDread = SubDread.objects.get(name=subdread)
    if not is_community_setup(subdread):
        return render(request, 'subdread/community_setup.html', {'subdread':subdread})
    return redirect('community_homepage_url', subdread=subdread)

def subdread_list(request:HttpRequest):
    subdreads = SubDread.objects.all()
    return render(request, 'subdread/subdread_list.html', {'subdreads':subdreads})


def subdread_detail(request:HttpRequest, subdread_id:int):
    subdread = get_object_or_404(SubDread, id=subdread_id)
    posts = subdread.posts.all().order_by('-created_on')
    is_member = request.user.is_authenticated and request.user in subdread.users.all()
    return render(request, 'subdread/subdread_detail.html', {
        'subdread': subdread,
        'posts': posts,
        'is_member': is_member})

@login_required
def join_subdread(request:HttpRequest, subdread_id:int):
    subdread = get_object_or_404(SubDread, id=subdread_id)
    if request.user not in subdread.users.all():
        subdread.users.add(request.user)
    return redirect('subdread_detail', subdread_id=subdread_id)

@login_required
def leave_subdread(request:HttpRequest, subdread_id:int):
    subdread = get_object_or_404(SubDread, id=subdread_id)
    if request.user in subdread.users.all():
        subdread.users.remove(request.user)
    return redirect('subdread_detail', subdread_id=subdread_id)

def delete_subdread(request:HttpRequest, subdread_id:int):
    subdread = get_object_or_404(SubDread, id=subdread_id)
    if subdread.creator != request.user:
        return HttpResponseForbidden("You dont have permission to delete this community")
    
    if request.method == 'POST':
        subdread.delete()
        return redirect('home_url')
    return render(request, 'subdread/subdread_confirm_delete.html', {'subdread': subdread})