from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from .views import ProjectDetailView

urlpatterns = [
    path('', views.AllProjects, name='all_projects'),
    path('<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)