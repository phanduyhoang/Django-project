from django.db import models

class Word(models.Model):
    id = models.AutoField(primary_key=True)  # Automatically created ID field
    english_word = models.CharField(max_length=255, unique=True)  # English word with unique constraint
    russian_translation = models.CharField(max_length=255)
    text = models.TextField(blank=True, null=True)  # Optional text field
    image = models.ImageField(upload_to='word_images/', default='word_images/default_image.jpg', blank=True)

    def __str__(self):
        return self.english_word
