#from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from . models import Genre, Book
from . forms import CreateGenreForm
from django.urls import reverse_lazy
#from django.shortcuts import render
#from django.http import HttpResponse

class CreateGenre(CreateView):
    model = Genre
    form_class = CreateGenreForm
    template_name = 'testgenre/create_genre.html'
    success_url = reverse_lazy('genres:list')

class UpdateGenre(UpdateView):
    model = Genre
    form_class = CreateGenreForm
    template_name = 'testgenre/update-genre.html'
    success_url = reverse_lazy('genres:list')

class ListGenre(ListView):
    model = Genre
    template_name='testgenre/list-genre.html'
    queryset = Genre.objects.all()
    success_url = reverse_lazy('genres:list')
    context_object_name = 'genres'
    paginate_by = 5

class DeleteGenre(DeleteView):
    model = Genre
    template_name = 'testgenre/delete-genre.html'
    success_url = reverse_lazy('genres:list')
    context_object_name = 'genres'

#class Test_gen(TemplateView):
#    template_name = 'testgenre/test.html'

#def all_list(request):
#    genre = Genre.objects.all()
#    context = {'genre': genre}
#    return render(request, template_name='testgenre/ok.html', context= context)



