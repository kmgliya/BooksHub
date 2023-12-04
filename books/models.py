import random
from django.contrib.auth import get_user_model
from django.db import models
from accounts.models import JustUser
from django.core.exceptions import ValidationError



class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    rating = models.FloatField(default=0)
    genres = models.ManyToManyField(Genre)  # Используем ManyToManyField для поддержки нескольких жанров
    image = models.ImageField(upload_to='', verbose_name='Добавьте фото', null=True, blank=True)
    author = models.CharField(max_length=100, null=True, blank=True)
    file = models.FileField(upload_to='static/file', null=True, blank=True)
    uploaded_by = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, related_name='books', null=True, default=None)

# class UserBookRating(models.Model):
#     user = models.ForeignKey(JustUser, on_delete=models.CASCADE)
#     books = models.ManyToManyField(Book)
#     rating = models.IntegerField()

    # def check_unique_rating(sender, instance, **kwargs):
    #     # Проверка уникальности комбинации user и books
    #     if UserBookRating.objects.filter(user=instance.user, books__in=instance.books.all()).exists():
    #         raise ValidationError('This rating combination is not unique.')

