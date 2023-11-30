import random
from django.contrib.auth import get_user_model
from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
<<<<<<< HEAD
    rating = models.IntegerField(default=random.randint(0, 10))
    genres = models.ManyToManyField(Genre)  # Используем ManyToManyField для поддержки нескольких жанров
    image = models.ImageField(upload_to='', verbose_name='Добавьте фото', null=True, blank=True)
    author = models.CharField(max_length=100, null=True, blank=True)
    file = models.FileField(upload_to='static/file', null=True, blank=True)
    uploaded_by = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, related_name='books', null=True, default=None)
=======
    image = models.ImageField(upload_to="media/")
    author = models.CharField(max_length=100)
    book_cover = models.ImageField()
    file = models.FileField()

class Navigation(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField()

    def __str__(self):
        return self.title
>>>>>>> f9cdd619fec9a166dc16e314287ab7d4cb869dc9



# class Slider(models.Model):
#     slide = models.URLField()
#
#     def __str__(self):
#         return self.slide



# class Navigation(models.Model):
#     title = models.CharField(max_length=255)
#     url = models.URLField()
#
#     def __str__(self):
#         return self.title