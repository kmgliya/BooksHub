from django.shortcuts import render
from .models import Navigation
from django.http import HttpResponse
from .models import *

def hello(request):
    book = Book.objects.all()
    return render(request, "index.html", {"book":book})

def home(request):
    navigation_items = Navigation.objects.all()
    return render(request, 'home.html', {'navigation_items': navigation_items})
