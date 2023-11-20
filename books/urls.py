from django.urls import path
from .views import *


urlpatterns = [
    path("", hello),
    path('home/', home, name='home'),
    path("<int:pk>", BooksDetailView.as_view(), name='book_detail'),
    path("create", create),
    # path("<int:pk>/update", BooksUpdateView.as_view(), name='book_update')

]
