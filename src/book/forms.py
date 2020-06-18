from django import forms
from . models import BookApp

class CreateBookAppForm(forms.ModelForm):
    class Meta:
        model = BookApp
        fields = (
            'name',
            'image',
            'genre',
            'authors',
            'publisher',
            'description',
            
        )