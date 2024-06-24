from django.urls import path
from . import views
from .views import ProjectDetailView

urlpatterns = [
    path('', views.AllProjects, name='all_projects'),
    path('<slug:project_slug>/', ProjectDetailView.as_view(), name='project_detail'),
]
