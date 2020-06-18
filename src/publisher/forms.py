from django import forms
from . models import Publisher

class CreatePublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = (
            'name',
            'description',
            'image'
        )