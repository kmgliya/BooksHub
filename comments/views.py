from django.shortcuts import render, get_object_or_404, redirect

from books.views import book_detail
from .models import Book, Comment
from .forms import CommentForm


def add_comment(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            user = request.user
            content = comment_form.cleaned_data['content']
            is_spoiler = comment_form.cleaned_data['is_spoiler']

            comment = Comment(user=user, book=book, content=content, is_spoiler=is_spoiler)
            comment.save()
    else:
        comment_form = CommentForm()

    return redirect(book_detail, book_id=book_id)


def reply_comment(request, parent_id, book_id):
    book = get_object_or_404(Book, id=book_id)
    parent_comment = Comment.objects.get(id=parent_id)
    if request.method == 'POST':

        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            user = request.user

            content = comment_form.cleaned_data['content']
            is_spoiler = comment_form.cleaned_data['is_spoiler']
            new_comment = Comment.objects.create(user=user, book=book, content=content, is_spoiler=is_spoiler, parent_comment=parent_comment)
            new_comment.parent_comment = parent_comment
            new_comment.save()


    return redirect(book_detail, book_id=book_id)


def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    book = comment.book
    book_id = book.id
    comment.delete()
    return redirect(book_detail, book_id=book_id)

def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST, instance=comment)
        if comment_form.is_valid():
            book_id = comment.book.id
            comment_form.save()

    return redirect(book_detail, book_id=book_id)

