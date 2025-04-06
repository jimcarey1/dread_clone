from django.http import HttpRequest, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse 

import json


from .models import SubDread, Flair, Rule

@login_required
def mod_tools(request:HttpRequest, subdread:str): # type: ignore
    subdread:SubDread = SubDread.objects.get(name=subdread)
    return render(request, 'subdread/mod/layout.html', {'subdread':subdread})

@login_required
def post_flair(request:HttpRequest, subdread:str):
    subdread:SubDread = get_object_or_404(SubDread, name=subdread)
    if request.method == 'POST':
        data = json.loads(request.body)
        flair_name= data.get('flair')
        flair = Flair(name=flair_name,subdread = subdread)
        flair.save()
        return JsonResponse({'status':'success', 'message':'flair created'})
    subdread_flairs = subdread.flairs.all()
    return render(request, 'subdread/mod/post_flair.html', {'subdread':subdread, 'flairs':subdread_flairs})


@login_required
def rules(request:HttpRequest, subdread:str):
    subdread:SubDread = get_object_or_404(SubDread, name=subdread)
    rules = subdread.rules.all()
    return render(request, 'subdread/mod/rules.html', {'subdread':subdread, 'rules':rules})

def create_new_rule(request:HttpRequest, subdread:str):
    subdread:SubDread = get_object_or_404(SubDread, name=subdread)
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        description = data.get('description')
        rule = Rule(name=name, description=description, subdread=subdread)
        rule.save()
        return JsonResponse({'redirect_url': reverse('community_mod_rules', args=[subdread])
})
    else:
        return render(request, 'subdread/mod/new_rule.html', {'subdread':subdread})