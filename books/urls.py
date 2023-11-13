from django.urls import path
from .views import hello
from .views import home


urlpatterns = [
    path("", hello),
    path('home/', home, name='home')
]
