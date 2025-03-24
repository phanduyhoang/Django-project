# forms.py

from django import forms
from .models import Word

class WordForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = ['english_word', 'russian_translation', 'text', 'image']
