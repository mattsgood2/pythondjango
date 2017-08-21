from django.shortcuts import render

def welcome_to_films(request):
    return render(request, 'home.html')
