from django.urls import path
from .views import bye



urlpatterns = [
    path("", bye),

]
