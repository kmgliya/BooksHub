import random

from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    rating = models.IntegerField(default=random.randint(0, 10))
    genres = models.ManyToManyField(Genre)  # Используем ManyToManyField для поддержки нескольких жанров
    image = models.ImageField(upload_to='', verbose_name='Добавьте фото', null=True, blank=True)
    author = models.CharField(max_length=100, null=True, blank=True)
    file = models.FileField(upload_to='static/file', null=True, blank=True)


class Navigation(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField()

    def __str__(self):
        return self.title


class Slider(models.Model):
    slide = models.URLField()

    def __str__(self):
        return self.slide
