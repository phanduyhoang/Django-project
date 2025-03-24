from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='web-home'),
    path('about/', views.about, name='web-about'),
    path('news/', views.news, name='web-news'),
    path('info_form/', views.info_form_view, name='info_form_view'),
    # path('contact/', views.contact_view, name='contact_view'),
]