from django.shortcuts import render
from django.http import HttpRequest


def create_comment(request:HttpRequest, post_id:int):
    if request.method == 'POST':
        pass
    else:
        pass