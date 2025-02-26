from django import forms
from django.core.exceptions import ValidationError


from .models import User


class RegistrationForm(forms.Form):
    username = forms.CharField(
        max_length=50, 
        min_length=6, 
        strip=True,
        help_text='Username should be unique.')
    password = forms.CharField(
        min_length=8, 
        strip=True, 
        widget=forms.PasswordInput, 
        help_text='Password must be atleast 8 characters Alphanumeric special required.')
    password2 = forms.CharField(
        min_length=8,
        strip=True,
        widget=forms.PasswordInput,
        help_text='Re-enter the password'
    )
