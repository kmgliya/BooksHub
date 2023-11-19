from django.shortcuts import render, redirect
from .forms import JustUserForm
from django.http import HttpResponse


def register(request):
    error = ''
    if request.method == "POST":

        form = JustUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("")
        else:
            error = 'Форма неправильно заполненна'
    else:
        form = JustUserForm()

    data = {
        "form": form,
        'error': error
    }
    return render(request, "accounts/registration.html", data)

