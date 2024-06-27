from django.conf import settings
from django.urls import path
from . import views
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='cv_home'),
    # path('create/', views.create_cv , name='create_cv'),
    path('django', views.cv_detail, name='cv_django'),
    path('html', views.cv_html, name='cv_html'),
]
