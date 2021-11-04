from django.urls import path 
from apps.users.api.api import UserAPIview

urlpatterns = [
    path('usuario/', UserAPIview.as_view(), name = 'usuario_api'),
]