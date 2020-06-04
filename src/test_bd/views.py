from django.shortcuts import render
from django.http import HttpResponse
import requests
# Create your views here.

from . models import Parsing

def bd(request):
    
    par = Parsing.objects.all()
    context = {'par': par}
    return render(request, template_name='test_bd/table.html', context= context)