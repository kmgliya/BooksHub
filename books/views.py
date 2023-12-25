from django.http import FileResponse, HttpResponse
from .models import Book


from django.views.generic import CreateView
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.core.paginator import Paginator

from comments.models import Comment
from comments.forms import CommentForm

def hello(request):
    book = Book.objects.all()
    return render(request, "books/index.html", {"book":book})


class AddBook(LoginRequiredMixin, CreateView):
    form_class = BookForm
    template_name = "books/book_create.html"
    title_page = 'Добавление книги'
    login_url = '/accounts/login/'
    success_url = 'home'

    def form_valid(self, form):
        book = form.save(commit=False)
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
    books_rating = Book.objects.all().order_by("rating")[0:10:-1]
    return render(request, template_name='books/books_slide.html', context={'books_rating': books_rating})




def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    comments = Comment.objects.filter(book=book, parent_comment=None)
    file_path = book.file.path
    file_path_parts = file_path.split("/")

    file_name = file_path_parts[-1]

    comment_form = CommentForm()

    return render(request, template_name='books/book_detail.html', context={'book': book,
    "marked_book": book.marked_book.all(), 'comments': comments, 'comment_form': comment_form, 'file_path': file_path, 'file_name': file_name})





@login_required
def download_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    # Предполагается, что ваше поле файла названо 'file' в модели Book
    file_path = book.file.path
    with open(file_path, 'rb') as file:
        response = HttpResponse(file.read(), content_type='application/fb2')
        response['Content-Disposition'] = f'attachment; filename="{book.file.name}"'
        return response


@login_required
def update_rating(request, book_id, rating_value):
    book = get_object_or_404(Book, id=book_id)
    comments = book.comments.all()

    if request.method == 'POST':
            user_id = request.user.id
            rated_by = book.rated_by
            rated_by[user_id] = int(rating_value)

            book.rated_by = rated_by
            book.rating = round(sum(book.rated_by.values())/len(book.rated_by), 2)
            book.save()

    return render(request, template_name='books/book_detail.html', context={'book': book, "marked_book": book.marked_book.all(), 'comments': comments})




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
    comments = book.comments.all()
    user = request.user
    if user in book.marked_book.all():
        book.marked_book.remove(user)
    else:
        book.marked_book.add(user)
    book.save()

    return render(request, template_name='books/book_detail.html', context={'book': book, "marked_book": book.marked_book.all(), 'comments': comments})



@login_required
def favorites(request):
    user = request.user
    books = user.book_set.all()

    return render(request, 'books/test.html', {'books':books})


def about(request):
    return render(request, "books/About_us.html")




# CATEEEGOOOOOOOOOORIIIIEEEEEEEEEEESSSSSSSS cat

def filtration(request):
    genres = Genre.objects.all()
    books = Book.objects.all()
    genres_names = []
    if request.method == "POST":
        if "genres" in request.POST:
            genres_names = list(request.POST.getlist("genres"))
            print(genres_names)
            books = set([])
            for genre_name in genres_names:
                genre = get_object_or_404(Genre, name=genre_name)
                books_with_genre = genre.book_set.all()
                books.update(books_with_genre)

    return render(request, 'books/category.html', {'genres': genres, "books": books, "genres_names": genres_names})
