from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.views.generic import DetailView, UpdateView, CreateView
from .forms import BookForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
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
        book_list = Book.objects.all().order_by("rating")[::-1]
        return render(request, template_name='books/books_slide.html', context={
            'book_list': book_list,
        })


def book_list_detail_view(request, id):
    if request.method == 'GET':
        book_id = get_object_or_404(Book, id=id)
        return render(request, template_name='books/book_detail.html', context={'book_id': book_id})


def test(request):
    return render(request, 'books/test.html')
# def carousel_view(request):
#     images = Book.objects.all()
#     return render(request, 'carousel.html', {'images': images})



# def home(request):
#     navigation_items = Navigation.objects.all()
#     return render(request, 'home.html', {'navigation_items': navigation_items})


# Ваше представление для сохранения оценки


# def rate_book(request, book_id, user_id):
#     book = get_object_or_404(Book, id=book_id)
#     user = get_object_or_404(JustUser, id=user_id)
#
#     if request.method == 'POST':
#         rating = int(request.POST.get('rating', 0))
#
#         if not UserBookRating.objects.filter(user=user, book=book).exists():
#             user_rating = UserBookRating.objects.create(user=user, book=book, rating=rating)
#             book.total_rating += rating
#             book.num_ratings += 1
#             book.save()
#             book.update_rating()
#
#     return render(request, 'books/book_detail.html', {'book': book})
