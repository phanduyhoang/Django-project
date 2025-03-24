from django.urls import path
from users.views import register
from users.views import user_login
from .views import CustomLogoutView
urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
]


from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)