from django.shortcuts import render, get_object_or_404

from .models import *
from django.views.generic import DetailView, UpdateView, CreateView
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.core.paginator import Paginator


def hello(request):
    book = Book.objects.all()
    return render(request, "books/index.html", {"book":book})


class AddBook(LoginRequiredMixin, CreateView):
    form_class = BookForm
    template_name = "books/book_create.html"
    title_page = 'Добавление книги'
    # login_url = 'home'
    success_url = 'home'

    def form_valid(self, form):
        book = form.save(commit=False) #Образуется обьект данных без занесения в БД
        book.uploaded_by = self.request.user
        return super().form_valid(form)


# def create(request):
#     error = ''
#     if request.method == "POST":
#
#         form = BookForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("home")
#         else:
#             error = 'Форма неправильно заполненна'
#     else:
#         form = BookForm()
#
#     data = {
#         "form": form,
#         'error': error
#     }
#     return render(request, "books/book_create.html", data)


# class BooksUpdateView(UpdateView):
#     model = Book
#     template_name = 'book_create'


def book_list_view(request):
    if request.method == "GET":
        books_rating = Book.objects.all().order_by("rating")[0:10:-1]
        return render(request, template_name='books/books_slide.html', context={
            'books_rating': books_rating,
        })




def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, template_name='books/book_detail.html', context={'book': book, "marked_book": book.marked_book.all()})

@login_required
def update_rating(request, book_id, rating_value):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
            user_id = request.user.id
            book.rated_by[user_id] = int(rating_value)
            book.rating = round(sum(book.rated_by.values())/len(book.rated_by), 2)
            book.save()

    return render(request, template_name='books/book_detail.html', context={'book': book})

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse

# @login_required
# def toggle_marked(request, book_id):
#     book = get_object_or_404(Book, id=book_id)
#     user = request.user
#
#     if request.method == 'POST':
#         if 'marked' in request.POST:
#             if user in book.marked_book.all():
#                 book.marked_book.remove(user)
#                 book.save()
#
#             else:
#                 book.marked_book.add(user)
#                 book.save()
#
#     return render(request, 'books/book_detail.html', {'book': book, "marked_book": book.marked_book.all()})

def favorites_button(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    user = request.user
    if user in book.marked_book.all():
        book.marked_book.remove(user)
    else:
        book.marked_book.add(user)
    book.save()

    return render(request, 'books/book_detail.html', {'book': book, "marked_book": book.marked_book.all()})


@login_required
def favorites(request):
    user = request.user
    books = user.book_set.all()

    return render(request, 'books/test.html', {'books':books})


def about(request):
    return render(request, "books/About_us.html")




# CATEEEGOOOOOOOOOORIIIIEEEEEEEEEEESSSSSSSS cat
def category(request):
    genres = Genre.objects.all()

    return render(request, 'books/categories.html', {'genres':genres})


def filtration(request):
    if request.method == "POST":
        genres_names = list(request.POST.getlist("genres"))
        for genre_name in genres_names:
            genre = get_object_or_404(Genre, name=genre_name)
            books_with_genre = genre.book_set.all()
            print(books_with_genre)

        return redirect('category')
