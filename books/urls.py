from django.urls import path

from main import settings
from .views import *



urlpatterns = [
    path("create/", AddBook.as_view()),
    path('', book_list_view, name='home'),
    # path("<int:pk>/update", BooksUpdateView.as_view(), name='book_update')
    path('book_list/<int:id>/', book_list_detail_view, name='book_detail'),
    # path("book_list/<int:id>/", rate_book),
    path('test/', test),
]


