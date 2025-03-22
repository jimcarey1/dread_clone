from django import forms
from froala_editor.widgets import FroalaEditor

from .models import Post

class PostForm(forms.ModelForm):
    content = forms.CharField(widget=FroalaEditor)
    class Meta:
        model = Post
        fields = ['title', 'content']