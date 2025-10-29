from django.urls import path
from . import views


urlpatterns = [
    path('', views.welcome , name='welcome' ),
    path('lab_sessions.html', views.lab_sessions , name='lab_sessions' ),
]
