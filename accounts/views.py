from django.shortcuts import render, redirect
from .forms import JustUserForm
from django.http import HttpResponse


# def register(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("home")
#     else:
#         form = CustomUserCreationForm()
#
#     return render(request, 'accounts/registration.html', {'form': form})

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

def main_page(request):
    return HttpResponse("qwerty")

def testing(request):
    return render(request, 'accounts/test.html')
