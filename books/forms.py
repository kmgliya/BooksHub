from django.forms import ModelForm, Textarea, TextInput, ImageField, FileInput
from .models import Book


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'description', 'image', 'author', 'file']

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

<<<<<<< HEAD
            'image': FileInput(attrs={
                'class': "form-control",

            }),

=======
>>>>>>> f9cdd619fec9a166dc16e314287ab7d4cb869dc9
            'file': FileInput(attrs={
                'class': "form-control",
                'placeholder': "file"
            }),
        }
