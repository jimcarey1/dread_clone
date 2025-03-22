from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from subdread.models import SubDread

# Create your views here.

from .forms import PostForm
from .models import Post

@login_required
def create_post(request:HttpRequest):
    subdread = SubDread.objects.first()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():

            data = form.cleaned_data
            title = data.get('title')
            content = data.get('content')
            post = Post(title = title, content = content)

            post.author = request.user
            post.subdread = subdread

            post.save()
            print(post.__dict__)
            return redirect('home_url')
        return render(request, 'post/create_post.html', {'form': form})
    else:
        form = PostForm()
        return render(request, 'post/create_post.html', {'form': form})

