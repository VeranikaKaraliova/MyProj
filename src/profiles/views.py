from django.views.generic import  FormView
from . models import Profiles
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from . forms import RegisterForm
from django.views.generic import DeleteView, UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin


class MyRegisterFormView(FormView):
    form_class = RegisterForm
    success_url = reverse_lazy('profiles:login')
    template_name = "profiles/register.html"

    def form_valid(self, form):
        form.save()
        return super(MyRegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(MyRegisterFormView, self).form_invalid(form)

class UserRoom(LoginRequiredMixin, UpdateView):
    model = Profiles
    form_class = RegisterForm
    template_name = 'profiles/user_room.html'
    success_url = reverse_lazy('profiles:user_room')



# работает 
#class MyRegisterFormView(FormView):
#    form_class = UserCreationForm
#    success_url = reverse_lazy('profiles:login')
#    template_name = "profiles/register.html"
#
#    def form_valid(self, form):
#        form.save()
        # Функция super( тип [ , объект или тип ] ) 
        # Возвратите объект прокси, который делегирует вызовы метода родительскому или родственному классу типа .
#        return super(MyRegisterFormView, self).form_valid(form)

#    def form_invalid(self, form):
#        return super(MyRegisterFormView, self).form_invalid(form)





#class ProfileUpdate(UpdateView):
#    model = Profiles
#    fields = ('user', 'image')
#    template_name = 'profiles/register.html'
#    def get_object(self):
#        user_pk = self.kwargs.get('user_pk')
#        obj, created = self.model.objects.get_or_create(
#            user = User.objects.get(pk=user_pk),
#            defaults = {},
#        )
#        return obj


