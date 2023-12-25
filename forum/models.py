import uuid
from datetime import datetime

from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models

from books.models import Book


# Create your models here
class Discussion(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    genre = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    chat_background = models.ImageField()

    def __str__(self):
        return self.title


class Message(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_spoiler = models.BooleanField(default=False)
    parent_comment = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.book.title} - {self.created_at}"

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now()
        super(Message, self).save(*args, **kwargs)
