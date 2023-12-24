from django.urls import path
from .views import *





urlpatterns = [
    path("detail_book/<int:book_id>", add_comment, name='add_comment'),
    path("detail_book/<int:parent_id>/<int:book_id>", reply_comment, name='reply_comment'),
    path("edit_comment/<int:comment_id>", edit_comment, name='edit_comment'),
    path("delete_comment/<int:comment_id>", delete_comment, name='delete_comment'),
]
