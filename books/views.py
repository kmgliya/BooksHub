from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def hello(request):
    book = Book.objects.all()
    return render(request, "index.html", {"book":book})
