from django.urls import path

from main import settings
from .views import *



urlpatterns = [
    path("create/", AddBook.as_view(), name='create'),
    path('', book_list_view, name='home'),
    path('book_list/<int:book_id>/', book_detail, name='book_detail'),
    path('update_rating/<int:book_id>/<int:rating_value>/', update_rating, name='update_rating'),
    path('toggle_marked/<int:book_id>/', favorites_button, name='toggle_marked'),
    path('favorites/', favorites, name='favorites'),
    path('category/', category, name='category'),
    path('About_us/', about, name='About_us'),
    path('filtration/', filtration, name='filtration')

]