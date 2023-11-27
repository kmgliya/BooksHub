from django.contrib import admin
from .models import *

class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'image']

admin.site.register(Book, BookAdmin)
admin.site.register(Slider)
admin.site.register(Genre)
