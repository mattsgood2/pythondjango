from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.shortcuts import render

from .models import Film

# Create your views here.

#def film_list(request):
    #films = Film.objects.all()
    #output = ','.join([str(film) for film in films])
    #return render(request, 'films/film_list.html', {'films': films})

class FilmListView(TemplateView):
    template_name = 'films/film_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['films'] = Film.objects.all()
        return context


def filmdetail(request, pk):
    film = Film.objects.get(pk=pk)
    return render(request, 'films/film_detail.html', {'film': film })
