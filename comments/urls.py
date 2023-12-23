from django.urls import path

from main import settings
from .views import *



urlpatterns = [
    path("detail_book/<int:book_id>", add_comment, name='add_comment'),
    path("detail_book/<int:parent_id>/<int:book_id>", reply_comment, name='reply_comment'),

]