from django.urls import path
<<<<<<< HEAD
from .views import *


urlpatterns = [
    # path("", hello),
    path("create/", AddBook.as_view()),
    path('', book_list_view, name='home'),
    # path("<int:pk>/update", BooksUpdateView.as_view(), name='book_update')
    path('book_list/<int:id>/', book_list_detail_view),
    path('test/', test),
=======
from .views import hello


urlpatterns = [
    path("", hello),
>>>>>>> d99a50dbd1556e3af7c349723d89d2aaa2375d36
]

