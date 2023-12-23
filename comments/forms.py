from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'is_spoiler']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3}),
        }

# forms.py

from django import forms

