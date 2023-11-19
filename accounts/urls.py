from django.urls import path
from . import views

urlpatterns = [
    path("registration/", views.register, name="register"),
    path("", views.main_page,),
    path("test/", views.testing),

]