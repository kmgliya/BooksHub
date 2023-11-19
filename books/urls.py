from django.urls import path
from .views import hello, home, BooksDetailView


urlpatterns = [
    path("", hello),
    path('home/', home, name='home'),
    path("<int:pk>", BooksDetailView.as_view(), name='book_detail')
]
