from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.http import HttpRequest, JsonResponse

from subdread.models import SubDread
from .models import Post, Comment

import json

def create_comment(request:HttpRequest, subdread:str, post_id:int):
    if request.method == 'POST':
        subdread:SubDread = get_object_or_404(SubDread, name=subdread)
        post:Post = get_object_or_404(Post, id=post_id)
        data = json.loads(request.body)
        content = data.get('content')
        if content:
            comment = Comment(content=content)
            comment.post = post
            comment.author = request.user
            comment.save()
            print(comment.__dict__)
        return JsonResponse({'redirect_url': reverse('post_view_url', args=[subdread.name, post_id])})