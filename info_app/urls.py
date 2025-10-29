from django.urls import path
from . import views


urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('resources/', views.resources, name='resources'),
    path('support', views.support , name='support' ),
]
