from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from .views import ProjectDetailView

urlpatterns = [
    path('', views.index, name='index'),
    path('my_cv', views.CV, name='my CV'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)