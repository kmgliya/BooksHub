from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


app_name = "accounts"

urlpatterns = [
    # path("", views.register, name="register"),
    path("profile/", views.profile_view, name="profile"),
    path('test/', views.test),
    path('login/', views.LoginJustUser.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path("password_change/", views.ChangePassword.as_view(), name="password_change")
]
