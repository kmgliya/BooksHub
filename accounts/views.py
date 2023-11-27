from django.shortcuts import render, redirect
from .forms import JustUserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect, HttpResponse
from .models import *
from django.views.generic.edit import CreateView, FormView

@login_required
def profile_view(request):
    return render(request, 'accounts/profile.html')

def test(request):
    return render(request, 'accounts/test.html')

def login_user(request):
    if request.method == "POST":
        form = JustUserForm()
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])

            if user and user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse("home"))
    else:
        form = JustUserForm()
    return render(request, 'registration/login.html')

def logout_user(request):
    return HttpResponse('qwertyu')

