from django.urls import path
from . import views


urlpatterns = [
    path('', views.welcome , name='welcome' ),
    path('projects/', views.projects , name='projects' ),
]
