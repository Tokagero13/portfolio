from django.urls import path
from . import views

urlpatterns = [
    path('', views.CV, name='my CV'),
    path('projects/', views.index, name='index'),
]
