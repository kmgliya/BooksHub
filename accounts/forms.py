from django.forms import ModelForm, EmailInput, DateTimeInput, TextInput
from .models import Just_User


class JustUserForm(ModelForm):
    class Meta:
        model = Just_User
        fields = ['email', 'password', 'username', 'first_name', 'last_name', 'date_of_birth']

        widgets = {
            "email": EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'email'
            }),

            "password": TextInput(attrs={
                "class": "form-control",
                "placeholder": "password"
            }),

            'username': TextInput(attrs={
                "class": "form-control",
                'placeholder': "username"
            }),

            'first_name': TextInput(attrs={
                'class': "form-control",
                'placeholder': "first name"
            }),

            'last_name': TextInput(attrs={
                'class': "form-control",
                'placeholder': "last name"
            }),

            'date_of_birth': DateTimeInput(attrs={
                'class': "form-control",
                "placeholder": "birthday"
            }),
        }
