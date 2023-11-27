from django.forms import ModelForm, Textarea, TextInput, ImageField, FileInput
from .models import Book


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'description', 'author', 'book_cover', 'file']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'title'
            }),

            "description": Textarea(attrs={
                "class": "form-control",
                "placeholder": "description"
            }),

            'author': TextInput(attrs={
                "class": "form-control",
                'placeholder': "author"
            }),

            'file': FileInput(attrs={
                'class': "form-control",
                'placeholder': "file"
            }),
        }
