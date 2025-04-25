from django import forms
from django.core.exceptions import ValidationError


from .models import User


class RegistrationForm(forms.Form):
    username = forms.CharField(
        max_length=50, 
        min_length=6, 
        strip=True,
        help_text='Username should be unique.')
    
    email = forms.EmailField(
        help_text='Enter a valid email address.',
        required=True
    )
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

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError('Email already exists.')
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password != password2:
            raise ValidationError('Passwords do not match')
        return cleaned_data
    

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)