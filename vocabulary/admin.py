from django.contrib import admin
from .models import Word

@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_display = ('english_word', 'russian_translation', 'text', 'image')
    search_fields = ('english_word', 'russian_translation')
    list_filter = ('english_word', 'russian_translation')
# Register your models here.
