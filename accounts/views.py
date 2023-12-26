from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import LoginUserForm, RegisterUserForm, CustomPasswordChangeForm

from django.contrib.auth.views import *

@login_required
def profile_view(request, username):
    just_user = get_user_model().objects.get(username=username)
    return render(request, 'accounts/profile.html', {"just_user": just_user})

def test(request):
    return render(request, 'accounts/test.html')

class LoginJustUser(LoginView):
    form_class = LoginUserForm
    template_name = 'registration/login.html'
    extra_context = {'title': "Авторизация"}
    def get_success_url(self):
        return redirect("/")



class RegisterView(FormView):
    form_class = RegisterUserForm
    template_name = 'registration/register.html'
    def get_success_url(self):
        return reverse_lazy('accounts:login')
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ChangePassword(PasswordChangeView):
    template_name = 'registration/password_change.html'
    form_class = CustomPasswordChangeForm
    extra_context = {'title': "Смена пароля"}

    def get_success_url(self):
        return reverse_lazy('accounts:profile')

