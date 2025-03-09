from django import forms

from .models import SubDread

class SubDreadForm(forms.ModelForm):
    class Meta:
        model = SubDread
        fields = ('name', 'description')