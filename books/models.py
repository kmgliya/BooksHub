from django.contrib.auth import get_user_model
from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    genres = models.ManyToManyField(Genre)  # Используем ManyToManyField для поддержки нескольких жанров
    image = models.ImageField(upload_to='', verbose_name='Добавьте фото', null=True, blank=True)
    author = models.CharField(max_length=100, null=True, blank=True)
    file = models.FileField(upload_to='static/file', null=True, blank=True)
    uploaded_by = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, related_name='books', null=True, default=None)

    rating = models.FloatField(default=0)
    rated_by = {}

