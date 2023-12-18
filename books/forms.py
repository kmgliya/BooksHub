from django.forms import ModelForm, Textarea, TextInput, ImageField, FileInput
from .models import Book
from django import forms

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

            'image': FileInput(attrs={
                'class': "form-control",
            }),
            "file": FileInput(attrs={
                'class': "form-control",
            }),
        }


class FavoriteBookForm(forms.Form):
    favorite = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'onchange': 'this.form.submit();'}))
