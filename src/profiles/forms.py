from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone = forms.CharField(required=True, max_length=12, help_text="в формате 375291112233")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "phone")

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.image = self.cleaned_data["phone"]
        if commit:
            user.save()
        return user




#class RegisterForm(forms.Form):
    #username = forms.RegexField(label='Username', max_length=30)
    #username = forms.CharField(label='Username', max_length=30)
    #first_name = forms.CharField(label='First name', required=False)
    #last_name = forms.CharField(label='Last name', required=False)
    #email = forms.EmailField(label='Email')
    #password1 = forms.CharField(widget=forms.PasswordInput(render_value=False))
    #password2 = forms.CharField(widget=forms.PasswordInput(render_value=False))
    #phone = forms.CharField(label='Phone', max_length=30)
    