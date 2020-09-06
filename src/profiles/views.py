from django.views.generic import  FormView
from . models import Profiles
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, authenticate
from django.contrib.contenttypes.models import ContentType 
from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType 
from django.contrib.auth.models import Permission, Group
from django.http import HttpResponseRedirect
from . forms import CreateProfileForm, UpdateProfileForm
from django.views.generic import FormView, UpdateView, DetailView, DeleteView, TemplateView

class MyRegisterFormView(FormView):
    form_class = CreateProfileForm
    template_name = 'profiles/create_profile.html'

    def form_valid(self, form):
        form_username = form.cleaned_data['username']
        form_password = form.cleaned_data['password']
        form_first_name = form.cleaned_data['first_name']
        form_last_name = form.cleaned_data['last_name']
        form_email = form.cleaned_data['email']
        form_phone_number = form.cleaned_data['phone_number']
        form_address1 = form.cleaned_data['address1']
        form_address2 = form.cleaned_data['address2']
        form_image = form.cleaned_data['image']
        
        if form.cleaned_data['password'] != form.cleaned_data['password1']:
            raise forms.ValidationError ("Пароли не совпадают")

        user, create = User.objects.get_or_create(
            username=form_username,
            password=form_password,
            first_name=form_first_name,
            last_name=form_last_name,
            email=form_email
        )
        user.groups.add(Group.objects.get(name='Customers'))
        if create:
            user.set_password(form_password)
            user.save()
        profiles, create = Profiles.objects.get_or_create(
            user = User.objects.get(username=form_username),
            first_name=form_first_name,
            last_name=form_last_name,
            email=form_email,
            phone_number=form_phone_number,
            address1=form_address1,
            address2=form_address2,
            image=form_image
        )
        if user.is_anonymous:
            user = None

        return HttpResponseRedirect(self.get_success_url())
        
    def get_success_url(self):
        return reverse_lazy('profiles:login_done')

class UpdateProfile(LoginRequiredMixin, UpdateView):
    model = Profiles
    form_class = UpdateProfileForm
    template_name = 'profiles/update_profile.html'
    
    def get_success_url(self):
        return reverse_lazy('profile:detail', kwargs={'pk': self.object.pk})


class DeleteProfile(LoginRequiredMixin, DeleteView):
    model = Profiles
    template_name = 'profiles/delete_profile.html'
    success_url = reverse_lazy('home')

class DetailProfile(LoginRequiredMixin, DetailView):
    model = Profiles
    template_name = 'profiles/detail_profile.html'

class LoginDone(TemplateView):
    template_name = 'profiles/login_done.html'

 

#Рабочий код. Регистрация пользователя
#class MyRegisterFormView(FormView):
#    form_class = CreateProfileForm
#    success_url = reverse_lazy('profiles:login')
#    template_name = "profiles/register.html"

#    def form_valid(self, form):
#        form.save()
#        return super(MyRegisterFormView, self).form_valid(form)

#    def form_invalid(self, form):
#        return super(MyRegisterFormView, self).form_invalid(form)

#class UserRoom(LoginRequiredMixin, UpdateView):
#    model = Profiles
#    form_class = CreateProfileForm
#    template_name = 'profiles/user_room.html'
#    success_url = reverse_lazy('profiles:user_room')



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


