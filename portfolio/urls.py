"""
URL configuration for portfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# from django.views.generic import RedirectView
from projects.views import ProjectDetailView, CV_view, index


urlpatterns = [
    path('', index, name='home'),
    path('admin/', admin.site.urls),
    path('projects/', include('projects.urls'), name='projects'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    # path('cv', CV_view, name='cv')
    path('cv/', include('projects.urls')),  # Include the CV app URLs
    path('projects/', include('projects.urls')),  # Your existing portfolio app URLs

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
