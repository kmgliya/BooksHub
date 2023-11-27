from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="media/")
    author = models.CharField(max_length=100)
    book_cover = models.ImageField()
    file = models.FileField()

class Navigation(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField()

    def __str__(self):
        return self.title



