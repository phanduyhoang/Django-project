from django.contrib import admin

# Register your models here.
from .models import CustomUser

admin.site.register(CustomUser)
from .models import TrainingHistory

@admin.register(TrainingHistory)
class TrainingHistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'correct_count', 'incorrect_count')