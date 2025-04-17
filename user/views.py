from typing import Dict, Any
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

from .forms import RegistrationForm, LoginForm
from .models import User
from post.models import Post

@login_required
def home_view(request:HttpRequest):
    data: Dict[str, Any] = dict()
    data['joined_subreddits'] = request.user.subdreads.all()
    data['created_subreddits'] = request.user.owned_subdreads.all()
    data['recent_posts'] = Post.objects.order_by('-created_on')[:3]
    return render(request, 'user/index.html', {'data':data})


def registration_view(request:HttpRequest):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User(username=form.cleaned_data.get('username'))
            user.set_password(form.cleaned_data.get('password'))
            user.save()
            return redirect('user_login_url')
        return render(request, 'user/registration.html', {'form':form})
    else:
        form = RegistrationForm()
        return render(request, 'user/registration.html', {'form':form})
    
def login_view(request:HttpRequest):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password'))
            if user is not None:
                login(request, user)
                next_url = request.GET.get('next') or request.POST.get('next') or '/'
                return redirect(next_url)
        return render(request, 'user/login.html', {'form':form})
    else:
        form = LoginForm()
        return render(request, 'user/login.html', {'form':form})

@login_required
def logout_view(request:HttpRequest):
    logout(request)
    return redirect('user_login_url')

@login_required(redirect_field_name='next')
def profile_view(request:HttpRequest):
    user = request.user
    return render(request, 'user/profile.html', {'user':user})


def user_profile_view(request:HttpRequest, username:str):
    user = get_object_or_404(User, username=username)
    return render(request, 'user/profile.html' ,{'user':user})
