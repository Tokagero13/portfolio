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
from projects.views import index, auth, AuthView, logout_user
from cv.views import contact_us
from django.views.decorators.cache import cache_page


urlpatterns = [
    path('', index, name='home'), # cache_page(60 *15)(index) \\ cache for 15 min
    path("__debug__/", include("debug_toolbar.urls")),
    path('captcha/', include('captcha.urls')),
    path('auth', AuthView.as_view(), name='auth'),
    path('logout', logout_user, name='logout'),
    path('admin/', admin.site.urls, name='admin'),
    path('projects/', include('projects.urls')),
    path('cv/', include('cv.urls'), name='cv'),  # Include the CV app URLs
    path('contact_us', contact_us, name="contact_us")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
