from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField

class Info(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = PhoneNumberField(default='')  # Add this line for phone numbers
    date_sent = models.DateTimeField(default=timezone.now)
    comment = models.TextField()
