from django.urls import path
from . import views
# from users.views import update_training_history
urlpatterns = [
    path('cards', views.cards, name='vocabulary-cards'),
    path('trainer', views.english_trainer, name='english_trainer'),
    path('update_training_history', views.update_training_history, name='update_training_history'),
    # path('contact/', views.contact_view, name='contact_view'),
]