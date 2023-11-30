from django.shortcuts import render, redirect
from .forms import LoginUserForm, RegisterUserForm, CustomPasswordChangeForm
from django.contrib.auth import get_user_model

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout

from django.contrib.auth.forms import AuthenticationForm

from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect, HttpResponse
from .models import *
from django.views.generic.edit import CreateView, FormView
from django.contrib.auth.views import *

@login_required
def profile_view(request):
    return render(request, 'accounts/profile.html')

def test(request):
    return render(request, 'accounts/test.html')

class LoginJustUser(LoginView):
    form_class = LoginUserForm
    template_name = 'registration/login.html'
    extra_context = {'title': "Авторизация"}

    # def get_success_url(self):
    #     return reverse_lazy('profile')



class RegisterView(FormView):
    form_class = RegisterUserForm
    template_name = 'registration/register.html'
    def get_success_url(self):
        return reverse_lazy('accounts:login')
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


# def register(request):
#     return render(request, 'registration/register.html')

# def login_user(request):
#     if request.method == "POST":
#         form = JustUserForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(request, username=cd['username'], password=cd['password'])
#
#             if user and user.is_active:
#                 login(request, user)
#                 return HttpResponseRedirect(reverse("home"))
#     else:
#         form = JustUserForm()
#     return render(request, 'registration/login.html', {'form': form})


# def logout_user(request):
#     logout(request)
#     return HttpResponseRedirect('accounts:login')


class ChangePassword(PasswordChangeView):
    template_name = 'registration/password_change.html'
    form_class = CustomPasswordChangeForm
    extra_context = {'title': "Смена пароля"}

    def get_success_url(self):
        return reverse_lazy('accounts:profile')

