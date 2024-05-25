from django.shortcuts import render
from .models import project


def index(request):
    object = project.objects.all()


    print(object)
    dict = {
        'title':'страница',
        'project':object
    }
    return render(request, 'lab/index.html',dict)

def webApp(request):
    return render(request, 'lab/webApp.html')

def chatBot(request):
    return render(request, 'lab/chatBot.html')

def ML(request):
    return render(request, 'lab/ML.html')

def Games(request):
    return render(request, 'lab/Games.html')









