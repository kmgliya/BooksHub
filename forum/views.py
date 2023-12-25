from django.http import HttpResponse
from django.shortcuts import render

from forum.models import Discussion


# Create your views here.
def forum(request):
    discussions = Discussion.objects.all()
    return render(request, "forum/forum.html", {"discussions": discussions})


from django.shortcuts import render, redirect
from .models import Discussion
from .forms import DiscussionForm

def add_discussion(request):
    if request.method == 'POST':
        form = DiscussionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('forum')
    else:
        form = DiscussionForm()

    return render(request, 'forum/add_discussion.html', {'form': form})



def discussion_chat(request):
    return render(request, "forum/discussion_chat.html")