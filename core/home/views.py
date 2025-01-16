from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

peoples = [
    {'name' : 'Krishna', 'age' : 19},
    {'name' : 'Shrey', 'age' : 20},
    {'name' : 'Eliza', 'age' : 24},
    {'name' : 'Riya', 'age' : 16},
]

games = ['rdr2','gta 5','cyberpunk']

def home(request):
    return render(request, 'home/index.html', context={'page' : 'django 2025','peoples' : peoples, 'games' : games})

def about(request):
    context = {'page' : 'about'}
    return render(request, 'home/about.html', context)

def contact(request):
    context = {'page' : 'contact'}
    return render(request, 'home/contact.html', context)
