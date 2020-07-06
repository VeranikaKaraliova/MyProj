
from django.views.generic.base import TemplateView
from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView
from django.shortcuts import render
from . models import BookApp
from . forms import CreateBookAppForm
from django.urls import reverse_lazy


class CreateBookApp(CreateView):
    model = CreateBookAppForm
    form_class = CreateBookAppForm   
    template_name = 'bookapp/create-bookapp.html'
    success_url = reverse_lazy('bookapp:list')
    
    
class UpdateBookApp(UpdateView):
    model = BookApp
    form_class = CreateBookAppForm
    template_name = 'bookapp/update-bookapp.html'
    success_url = reverse_lazy('bookapp:list')

class ListBookApp(ListView):
    model = BookApp
    template_name='bookapp/list-bookapp.html'
    queryset = BookApp.objects.all()
    success_url = reverse_lazy('bookapp:list')
    context_object_name = 'bookapp'
    def get_context_data(self, **kwargs): #для тренировки и примера
        key1 = self.request.GET.get('key1')
        print(key1)
        return super().get_context_data(**kwargs)
    

class DeleteBookApp(DeleteView):
    model = BookApp
    template_name = 'bookapp/delete-bookapp.html'
    success_url = reverse_lazy('bookapp:list')
    context_object_name = 'bookapp'

class DetailBookApp(DetailView):
    model = BookApp
    template_name = 'bookapp/detail-bookapp.html'
    context_object_name = 'bookapp'

#class HomePage()
class HomePage(ListView):
    model = BookApp
    #queryset = BookApp.objects.get(pk =0)
    context_object_name = 'bookapp'
    template_name = "bookapp/home-page.html"
    success_url = reverse_lazy('bookapp:home-page')
    paginate_by = 5
    #def get_context_data(self, **kwargs):
    #    context = super().get_context_data(**kwargs)
    #    context['book'] = BookApp.obgects.all()
    #    return context
