from django.urls import path 
#from apps.users.api.api import UserAPIview # *vista sin decorardo
from apps.users.api.api import user_api_view, user_detail_api_view # *vista con decorador


urlpatterns = [
    path('usuario/', user_api_view, name = 'usuario_api'),
    path('usuario/<int:pk>/', user_detail_api_view, name = 'usuario _detail_api_view'),
]