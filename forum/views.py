from django.http import HttpResponse
from django.shortcuts import render

from forum.models import *


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

def join_leave_discussion(request, discussion_title):
    user = request.user
    discussion = Discussion.objects.get(title=discussion_title)
    if discussion in user.discussions.all():
        user.discussions.remove(discussion)
        return redirect('forum')
    else:
        user.discussions.add(discussion)
        return redirect('forum')


def discussion_chat(request, discussion_title):
    discussion = Discussion.objects.get(title=discussion_title)
    try:
        messages = discussion.messages.objects.all().order_by("created_at")
        first_message = messages[0]
        messages = messages[1:]

    except:
        messages = False
        first_message = False
    print(discussion.messages.all())

    return render(request, "forum/discussion_chat.html", {"first_message": first_message, "messages": messages, "discussion": discussion})