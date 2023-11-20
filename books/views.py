from django.shortcuts import render, redirect
from .models import Navigation, Book
from django.http import HttpResponse
from .models import *
from django.views.generic import DetailView, UpdateView
from .forms import BookForm

def hello(request):
    book = Book.objects.all()
    return render(request, "index.html", {"book":book})

def home(request):
    navigation_items = Navigation.objects.all()
    return render(request, 'home.html', {'navigation_items': navigation_items})


def create(request):
    error = ''
    if request.method == "POST":

        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("")
        else:
            error = 'Форма неправильно заполненна'
    else:
        form = BookForm()

    data = {
        "form": form,
        'error': error
    }
    return render(request, "book_create.html", data)


class BooksDetailView(DetailView):
    model = Book
    template_name = 'book.html'
    context_object_name = 'book'

# class BooksUpdateView(UpdateView):
#     model = Book
#     template_name = 'book_create'


