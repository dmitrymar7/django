from django import forms
from .models import Category, Recipe


class AddPostForm(forms.ModelForm):

    class Meta:
        exclude = ['author']
        model = Recipe

