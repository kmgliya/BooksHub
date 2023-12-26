from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', forum, name='forum'),
    path('add_discussion/', add_discussion, name='add_discussion'),
    path("discussion_chat/<slug:discussion_title>", discussion_chat, name='discussion_chat'),
    path("discussion/<slug:discussion_title>", join_leave_discussion, name='join_leave_discussion')
]