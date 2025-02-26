from django.shortcuts import render
from django.http import HttpRequest
# Create your views here.

from .forms import RegistrationForm
from .models import User

def home_view(request:HttpRequest):
    return render(request, 'user/index.html')


def registration_view(request:HttpRequest):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        print(form.data)
    else:
        form = RegistrationForm()
        return render(request, 'user/registration.html', {'form':form})
