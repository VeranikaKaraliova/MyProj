#from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from . models import Genre, Book
from . forms import CreateGenreForm
from django.shortcuts import render
from django.http import HttpResponse

class CreateGenre(CreateView):
    model = Genre
    form_class = CreateGenreForm
    template_name = 'testgenre/create_genre.html'
    success_url = '/ok/'

class UpdateGenre(UpdateView):
    model = Genre
    form_class = CreateGenreForm
    template_name = 'testgenre/update-genre.html'
    success_url = '/ok/'

class Test_gen(TemplateView):
    template_name = 'testgenre/test.html'

def all_list(request):
    genre = Genre.objects.all()
    context = {'genre': genre}
    return render(request, template_name='testgenre/ok.html', context= context)



