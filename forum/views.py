from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

def index(request):
    """ Returns index.html """
    return render(request, 'index.html')


