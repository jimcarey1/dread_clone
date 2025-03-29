from django import forms

from .models import SubDread, Category

class SubDreadForm(forms.ModelForm):
    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.exclude(parent=None),
        widget = forms.CheckboxSelectMultiple)
    class Meta:
        model = SubDread
        fields = ['name', 'description', 'type', 'adults_only', 'categories']