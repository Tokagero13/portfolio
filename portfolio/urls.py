from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from projects.views import index, AuthView, logout_user, UserViewSet, technologies
from cv.views import contact_us
from django.views.decorators.cache import cache_page

from rest_framework import routers
from rest_framework.authtoken import views

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('', index, name='home'), # cache_page(60 *15)(index) \\ cache for 15 min
    path('api', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', views.obtain_auth_token),
    path("__debug__/", include("debug_toolbar.urls")),
    path('captcha/', include('captcha.urls')),
    path('auth', AuthView.as_view(), name='auth'),
    path('logout', logout_user, name='logout'),
    path('admin/', admin.site.urls, name='admin'),
    path('projects/', include('projects.urls')),
    path('cv/', include('cv.urls'), name='cv'),  # Include the CV app URLs
    path('contact_us', contact_us, name="contact_us"),
    path('technologies', technologies, name="technologies")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += router.urls

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
