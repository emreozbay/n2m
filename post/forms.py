from django import forms
from .models import Post,Department

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = [
            'name',
            'surname',
            'department',


        ]


