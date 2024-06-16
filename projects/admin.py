from django.contrib import admin
from .models import Project, ProjectImage

# Register your models here.
class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 5  # Number of extra forms to display

class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImageInline]

admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectImage)

