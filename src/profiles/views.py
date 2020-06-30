from django.views.generic import  FormView
from . models import Profiles
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm


User = get_user_model()

class MyRegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = reverse_lazy('profiles:login')
    template_name = "profiles/register.html"

    def form_valid(self, form):
        form.save()
        # Функция super( тип [ , объект или тип ] ) 
        # Возвратите объект прокси, который делегирует вызовы метода родительскому или родственному классу типа .
        return super(MyRegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(MyRegisterFormView, self).form_invalid(form)







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


