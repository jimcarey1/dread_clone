from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponseForbidden
from django.contrib.auth.decorators import login_required


from .forms import SubDreadForm
from .models import SubDread

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
                banner = data.get('banner'),
                icon = data.get('icon'),
            )
            subdread.save()
            subdread.creator = request.user
            subdread.users.add(request.user)
            subdread.moderators.add(request.user)

            for category in data.get('categories'):
                subdread.categories.add(category)

            return redirect('home_url')
        return render(request, 'subdread/create_community.html', {'form':form})
    else:
        form = SubDreadForm()
        return render(request, 'subdread/create_community.html', {'form':form})


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
        
