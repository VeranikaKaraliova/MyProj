
from django.views.generic.base import TemplateView
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from . models import Authors
from . forms import CreateAuthorsForm
from django.urls import reverse_lazy


class CreateAuthors(CreateView):
    model = Authors
    form_class = CreateAuthorsForm
    template_name = 'authors/create-authors.html'
    success_url = reverse_lazy('authors:list')

class UpdateAuthors(UpdateView):
    model = Authors
    form_class = CreateAuthorsForm
    template_name = 'authors/update-authors.html'
    success_url = reverse_lazy('authors:list')

class ListAuthors(ListView):
    model = Authors
    template_name='authors/list-authors.html'
    queryset = Authors.objects.all()
    success_url = reverse_lazy('authors:list')
    context_object_name = 'authors'
    
class DeleteAuthors(DeleteView):
    model = Authors
    template_name = 'authors/delete-authors.html'
    success_url = reverse_lazy('authors:list')
    context_object_name = 'authors'