from django import forms
from .models import Discussion

class DiscussionForm(forms.ModelForm):
    class Meta:
        model = Discussion
        fields = ['title', 'user', 'book', 'genre', 'description', 'chat_background']

