from django.http import HttpRequest
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required

from subdread.models import SubDread

# Create your views here.

from .forms import PostForm
from .models import Post

@login_required
def create_post(request:HttpRequest):
    form = PostForm(user=request.user)
    print(form.fields)
    return render(request, 'post/create_post.html', {'form': form})

@login_required
def create_post_to_community(request:HttpRequest, subdread:str):
    subdread:SubDread = get_object_or_404(SubDread, name=subdread)
    if request.method == 'POST':
        form = PostForm(request.POST, user=request.user, subdread=subdread)
        if form.is_valid():
            post = Post(
                title = form.cleaned_data['title'],
                content = form.cleaned_data['content'],
                subdread = form.cleaned_data['subdread'],
                flair = form.cleaned_data['flairs'],
                author = request.user,
            )
            post.save()
        return redirect('post_view_url', subdread=subdread.name, post_id=post.id)
    else:
        form = PostForm(initial={'subdread':subdread}, user=request.user, subdread=subdread)
        form.fields['subdread'].disabled = True
        return render(request, 'post/create_post.html', {'form':form, 'subdread':subdread})

def view_post(request:HttpRequest, subdread:str, post_id:int):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'post/post_view.html', {'post':post})