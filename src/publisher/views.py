
from django.views.generic.base import TemplateView
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from . models import Publisher
from . forms import CreatePublisherForm
from django.urls import reverse_lazy


class CreatePublisher(CreateView):
    model = CreatePublisherForm
    form_class = CreatePublisherForm   
    template_name = 'publisher/create-publisher.html'
    success_url = reverse_lazy('publisher:list')

class UpdatePublisher(UpdateView):
    model = Publisher
    form_class = CreatePublisherForm
    template_name = 'publisher/update-publisher.html'
    success_url = reverse_lazy('publisher:list')

class ListPublisher(ListView):
    model = Publisher
    template_name='publisher/list-publisher.html'
    queryset = Publisher.objects.all()
    success_url = reverse_lazy('publisher:list')
    context_object_name = 'publisher'
    
class DeletePublisher(DeleteView):
    model = Publisher
    template_name = 'publisher/delete-publisher.html'
    success_url = reverse_lazy('publisher:list')
    context_object_name = 'publisher'
