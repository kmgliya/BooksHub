import uuid
from datetime import datetime

from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models

from books.models import Book

GENRES = [
    ('Hobby', 'Hobby'),
    ('Flood', 'Flood'),
    ('Book', 'Book'),
    ('Competition', 'Competition')
]

# Create your models here
class Discussion(models.Model):
    title = models.CharField(max_length=255, unique=True)
    user = models.ManyToManyField(get_user_model(), related_name='discussions')
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    genre = models.CharField(max_length=255, choices=GENRES)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    chat_background = models.ImageField()

    def __str__(self):
        return self.title


class Message(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE, related_name='messages')
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    parent_comment = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)

    def __str__(self):
        return f"Mes: {self.user.username} - {self.created_at}"

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now()
        super(Message, self).save(*args, **kwargs)

    def get_previous_message(self):
        discussion = self.discussion

        previous_message = Message.objects.filter(
            discussion=discussion,
            created_at__lt=self.created_at
        ).order_by('-created_at').first()

        return previous_message

    def created_at_hour(self):
        return self.created_at.strftime('%I:%M %p')

    def created_on(self):
        return self.created_at.strftime('%b. %d, %Y')

    def len_users(self):
        return len(self.user)-1