from django.shortcuts import render
from django.http import HttpResponse
from . models import Parsing
from . parsin import all_ip , list_firefox, full_request


def bd(request):
    par = Parsing.objects.all()
    context = {'par': par}
    return render(request, template_name='test_bd/table.html', context= context)

def bdcr(request):
    for a in range(20):
        par_cr = Parsing.objects.create(ip = all_ip[a], name = list_firefox[a], description = full_request[a])
        
    context = {'par_cr': par_cr}
    return render(request, template_name='test_bd/table_cr.html', context= context)    
        
