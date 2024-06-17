from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('create/', views.create_cv , name='create_cv'),
    path('<int:pk>/', views.cv_detail, name='cv_detail'),
]
