from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', forum, name='forum'),
    path('add_discussion/', add_discussion, name='add_description'),
    path("discussion/", discussion_chat, name='discussion_chat')
]