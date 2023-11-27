from django.urls import path
from .views import *


urlpatterns = [
    # path("", hello),
    path("create", create),
    path('', book_list_view, name='home'),
    # path("<int:pk>/update", BooksUpdateView.as_view(), name='book_update')
    path('book_list/<int:id>/', book_list_detail_view),
    path('test/', test)
]

