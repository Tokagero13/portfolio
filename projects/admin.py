from django.contrib import admin
from .models import Project, Repository

# Register your models here.
admin.site.register(Project)
admin.site.register(Repository)