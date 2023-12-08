import random
from django.contrib.auth import get_user_model
from django.db import models
from accounts.models import JustUser
from django.core.exceptions import ValidationError



class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

RATINGS = [
    (1, "    *    "),
    (2, "   * *   "),
    (3, "  * * *  "),
    (4, " * * * * "),
    (5, "* * * * *")
]

class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    genres = models.ManyToManyField(Genre)  # Используем ManyToManyField для поддержки нескольких жанров
    image = models.ImageField(upload_to='', verbose_name='Добавьте фото', null=True, blank=True)
    author = models.CharField(max_length=100, null=True, blank=True)
    file = models.FileField(upload_to='static/file', null=True, blank=True)
    uploaded_by = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, related_name='books', null=True, default=None)

    rating = models.FloatField(default=0)
    rating_field = models.IntegerField(choices=RATINGS, null=True)
    rated_by = models.JSONField(default=dict)  # Use a JSONField for the dictionary

    def change_rating(self):
        if self.rated_by:
            self.rating = round(sum(self.rated_by.values()) / len(self.rated_by), 1)


