from django.shortcuts import render
from .models import Navigation
from django.http import HttpResponse
from .models import *
from django.views.generic import DetailView


def hello(request):
    book = Book.objects.all()
    return render(request, "index.html", {"book":book})

def home(request):
    navigation_items = Navigation.objects.all()
    return render(request, 'home.html', {'navigation_items': navigation_items})

class BooksDetailView(DetailView):
    model = Book
    template_name = 'book.html'
    context_object_name = 'book'