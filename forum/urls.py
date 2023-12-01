from django.urls import path
from .views import bye
from . import views



urlpatterns = [
    path("", bye),

]
