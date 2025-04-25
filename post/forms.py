from django import forms
from froala_editor.widgets import FroalaEditor

from .models import Post
from subdread.models import SubDread, Flair

class SubdreadChoiceField(forms.ModelChoiceField):
    def to_python(self, value):
        if not value:
            return None
        try:
            return self.queryset.get(name=value)
        except SubDread.DoesNotExist:
            raise forms.ValidationError("Invalid subdread selected.")

    def prepare_value(self, value):
        if isinstance(value, SubDread):
            return value.name
        return value

class PostForm(forms.ModelForm):
    subdread = SubdreadChoiceField(queryset=SubDread.objects.none())
    title = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Title',
    }))
    flairs = forms.ModelChoiceField(queryset=Flair.objects.none())
    content = forms.CharField(widget=FroalaEditor)
    class Meta:
        model = Post
        fields = ['subdread', 'title', 'content']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None) 
        subdread = kwargs.pop('subdread', None) 
        super().__init__(*args, **kwargs)
        if user is not None:
            print(user.subdreads.all())
            self.fields['subdread'].queryset = user.subdreads.all()

        if subdread is not None:
            self.fields['flairs'].queryset = subdread.flairs.all()
