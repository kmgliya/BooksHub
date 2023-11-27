from django.forms import ModelForm, EmailField, BooleanField, RadioSelect, EmailInput, CharField, TextInput
from .models import JustUser
from django.core.exceptions import ValidationError
from django import forms
from django.contrib.auth.forms import UserCreationForm


class JustUserForm(forms.Form):
    username = forms.CharField(label='Логин',
                               widget=forms.TextInput(attrs={'class': 'form-input input-area'}))
    password = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput(attrs={'class': 'form-input input-area'}))

