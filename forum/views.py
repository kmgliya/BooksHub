from django.shortcuts import render

from django.http import HttpResponse
from .models import *

def bye(request):
    return render(request, "forum.html")

