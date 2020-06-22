from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.contrib.auth.views import LoginView
from . models import Profiles
#from . forms import CreateprofilesForm
from django.urls import reverse_lazy


class ProfilesLogin(LoginView):
    template_name = 'login.html'
