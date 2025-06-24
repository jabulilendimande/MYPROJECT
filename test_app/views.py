from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here. Returns what is on the template , from view.py 
def test_app(request):
    template = loader.get_template('results.html')
    return HttpResponse(template.render())
