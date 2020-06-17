from django import forms
from . models import Authors

class CreateAuthorsForm(forms.ModelForm):
    class Meta:
        model = Authors
        fields = (
            'name',
            'description',
        )