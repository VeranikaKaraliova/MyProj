from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.


def test(request):
    s = requests.get('https://www.nbrb.by/api/exrates/currencies/298?ondate-2016-7-5')
    result = s.json()
    rate = result.get('Cur_OfficialRate')
    context = {'rate': rate}
    return render(request, template_name='testapp/test.html', context= context)