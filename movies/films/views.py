from django.http import HttpResponse
from django.views import View
from django.shortcuts import render

from .models import Film

# Create your views here.

def film_list(request):
    films = Film.objects.all()
    #output = ','.join([str(film) for film in films])
    return render(request, 'films/film_list.html', {'films': films})
